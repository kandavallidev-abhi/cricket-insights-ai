from app.models.match import Innings, FallOfWicket
import re
from app.services.cricheroes.match_parser import extract_score_team
from app.models.performance import BattingPerformance, BowlingPerformance

def parse_innings(page: str, our_team: str, opponent_team: str) -> Innings:
    innings_line = next(line for line in page.splitlines() if re.search(r"\d+/\d+\s+\([\d.]+\s+Ov\)", line) and "Innings" in line)
    
    batting_team = extract_score_team(innings_line)

    if batting_team == our_team:
        bowling_team = opponent_team
    elif batting_team == opponent_team:
        bowling_team = our_team
    else:
        raise ValueError(f"Unknown batting team '{batting_team}'")

    score_match = re.search(
        r"(\d+)/(\d+)\s+\(([\d.]+)\s+Ov\)",
        innings_line
    )

    if not score_match:
        raise ValueError(f"Could not parse innings score: '{score_match}'")

    runs = int(score_match.group(1))
    wickets = int(score_match.group(2))
    overs = score_match.group(3)

    # extract fall of wickets
    lines = [line.strip() for line in page.splitlines() if line.strip()]

    fall_of_wickets_index = next(
        index
        for index, line in enumerate(lines)
        if line == "Fall of Wickets"
    )

    fow_lines = []
    for index in range(fall_of_wickets_index+1, len(lines)):
        
        if lines[index].startswith("No Bowler"):
            break
        
        fow_lines.append(lines[index])

    fow_text = " ".join(fow_lines)
    fow_pattern = re.compile(r"(\d+)-(\d+)\s+\(([^,]+),\s*([\d.]+)\s+ov\)")
    matches = fow_pattern.findall(fow_text)

    fall_of_wickets = []
    for score, wicket_number, player_name, over in matches:
        fall_of_wickets.append(
            FallOfWicket(
                score=score,
                wicket_number=wicket_number,
                player_name=player_name,
                over=over
            )
        )

    # parse batting performance
    batting_header_index = next(index for index, line in enumerate(lines) if "No Batsman Status" in line)
    batting_lines = []
    for index in range(batting_header_index+1, len(lines)):
        if lines[index].startswith("Extras:"):
            break
        
        batting_lines.append(lines[index])

    dismissal_keywords = {
        "c",
        "b",
        "lbw",
        "st",
        "run",
        "not",
        "hit",
        "retired",
    }
    batting_stats = []
    # 1 Abhi (c) (RHB) lbw b Aamir Raina 2 4 10 0 0 50.00
    for line in batting_lines:
        #batting position
        position_match = re.match(r"^(\d+)\s+", line)

        if not position_match:
            raise ValueError(
                f"Could not parse batting position: {line}"
            )
        batting_position = int(position_match.group(1))

        # batting stats
        # R B M 4s 6s SR
        stats_match = re.search(
            r"(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d.]+)$",
            line,
        )

        if not stats_match:
            raise ValueError(
                f"Could not parse batting statistics: {line}"
            )
        
        runs = int(stats_match.group(1))
        balls_faced = int(stats_match.group(2))
        minutes = int(stats_match.group(3))
        fours = int(stats_match.group(4))
        sixes = int(stats_match.group(5))
        strike_rate = float(stats_match.group(6))

        # player + dismissal section
        middle_text = line[
            position_match.end():stats_match.start()
        ].strip()

        middle = middle_text.split()
        # Remove batting style / captain / wicketkeeper markers
        middle = [
            part
            for part in middle
            if part.upper() not in {
                "(RHB)",
                "(LHB)",
                "(C)",
                "(WK)",
            }
        ]

        dismissal_index = next((index for index, part in enumerate(middle) if part.lower() in dismissal_keywords), None)

        if dismissal_index is None:
            player_name = " ".join(middle)
            dismissal_details = None
            dismissal = None
        elif middle[dismissal_index] == "not":
            player_name = " ".join(middle[:dismissal_index])
            dismissal_details = None
            dismissal = "not out"
        else:
            player_name = " ".join(middle[:dismissal_index])
            dismissal = middle[dismissal_index]
            dismissal_details = " ".join(middle[dismissal_index + 1:])

        batting_stats.append(
            BattingPerformance(
                player_name=player_name,
                batting_position=batting_position,
                dismissal=dismissal,
                dismissal_details=dismissal_details,
                runs=runs,
                balls_faced=balls_faced,
                minutes=minutes,
                fours=fours,
                sixes=sixes,
                strike_rate=strike_rate
            )
        )

    # extract bowling stats
    bowling_header_index = next(index for index, line in enumerate(lines) if "No Bowler" in line)
    bowling_stats = []
    for index in range(bowling_header_index+1, len(lines)):
        print(lines[index])
        # bowling stats
        # O M R W 0s 4s 6s WD NB Eco'
        bowling_stats_match = re.search(
            r"^(\d+)\s+(.*?)\s+"
            r"(\d+(?:\.\d+)?)\s+"  # 3 overs
            r"(\d+)\s+"             # 4 maidens
            r"(\d+)\s+"             # 5 runs
            r"(\d+)\s+"             # 6 wickets
            r"(\d+)\s+"             # 7 dots
            r"(\d+)\s+"             # 8 fours
            r"(\d+)\s+"             # 9 sixes
            r"(\d+)\s+"             # 10 wides
            r"(\d+)\s+"             # 11 no-balls
            r"([\d.]+)$",            # 12 economy
            lines[index]
        )
        
        bowling_position = int(bowling_stats_match.group(1))
        player_name = bowling_stats_match.group(2).strip()

        player_name = re.sub(
            r"\s*\(c\)",
            "",
            player_name,
            flags=re.IGNORECASE,
        ).strip()

        overs = bowling_stats_match.group(3)
        maidens = int(bowling_stats_match.group(4))
        runs_conceded = int(bowling_stats_match.group(5))
        wickets = int(bowling_stats_match.group(6))
        dot_balls = int(bowling_stats_match.group(7))
        fours_conceded = int(bowling_stats_match.group(8))
        sixes_conceded = int(bowling_stats_match.group(9))
        wides = int(bowling_stats_match.group(10))
        no_balls = int(bowling_stats_match.group(11))
        economy = float(bowling_stats_match.group(12))

        bowling_stats.append(
            BowlingPerformance(
                player_name= player_name,
                overs=overs,
                maidens=maidens,
                runs_conceded=runs_conceded,
                wickets=wickets,
                dot_balls=dot_balls,
                fours_conceded=fours_conceded,
                sixes_conceded=sixes_conceded,
                wides=wides,
                no_balls=no_balls,
                economy=economy
            )
        )

    return Innings(
        batting_team=batting_team,
        bowling_team=bowling_team,
        overs=overs,
        runs=runs,
        wickets=wickets,
        fall_of_wickets=fall_of_wickets,
        batting= batting_stats,
        bowling= bowling_stats
    )

