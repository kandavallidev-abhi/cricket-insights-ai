from app.models.match import Match
from datetime import datetime,timezone
import re

def parse_match(page: str, our_team: str) -> Match:
    lines = [line.strip() for line in page.splitlines() if line.strip()]
    
    # --------------------------------------------------
    # Tournament name + stage
    # --------------------------------------------------

    # Find the CricHeroes page header.
    # Example:
    # 8/4/26, 3:55 AM cricheroes.com 1 of 4
    header_index = next(index for index, line in enumerate(lines) if "cricheroes.com" in line and "of 4" in line)

    title_line = lines[header_index - 1]
    stage = None
    stage_keywords = [
        "league",
        "group",
        "final",
        "semi",
        "quarter",
    ]

    # Case 1:
    # Stage is on its own line.
    #
    # SUPERSTARS T20 LEAGUE...
    # (Silver Final)
    # 8/4/26, 3:55 AM cricheroes.com 1 of 4
    if title_line.startswith("(") and title_line.endswith(")"):
        candidate_stage = title_line[1:-1].strip()

        if any(
            keyword in candidate_stage.lower()
            for keyword in stage_keywords
        ):
            stage = candidate_stage
            tournament_name = lines[header_index - 2]
        else:
            tournament_name = lines[header_index - 2]   

    # Case 2:
    # Stage is at the end of the tournament title.
    #
    # GENTLEMENS CRICKET LEAGUE (GCL -5) (League Matches)
    # 8/13/26, 5:47 PM cricheroes.com 1 of 4
    else:
        stage_match = re.search(
            r"\(([^()]*)\)\s*$",
            title_line,
        )

        if stage_match:
            candidate_stage = stage_match.group(1).strip()

            if any(
                keyword in candidate_stage.lower()
                for keyword in stage_keywords
            ):
                stage = candidate_stage
                tournament_name = (
                    title_line[:stage_match.start()]
                    .strip()
                )
            else:
                tournament_name = title_line
        else:
            tournament_name = title_line

    # --------------------------------------------------
    # Teams
    # --------------------------------------------------
    match_line_index = next(index for index, line in enumerate(lines) if line.startswith("Match") and "vs" in line)

    team_line = lines[match_line_index]
    first_team = team_line.replace("Match", "").replace("vs", "").strip()
    second_team = lines[match_line_index+1]

    if first_team == our_team:
        team_name = first_team
        opponent_name = second_team
    else:
        team_name = second_team
        opponent_name = first_team
        
    # --------------------------------------------------
    # Ground
    # --------------------------------------------------
    ground_line_index = next(index for index, line in enumerate(lines) if line.startswith("Ground"))

    ground = (lines[ground_line_index].replace("Ground ", "") + " " + lines[ground_line_index+1]).strip()

    # --------------------------------------------------
    # Date
    # --------------------------------------------------

    date_line = next(
        line for line in lines
        if line.startswith("Date ")
    )

    date_text = date_line.replace("Date ", "").strip()

    match_date = datetime.strptime(
        date_text,
        "%Y-%m-%d, %I:%M %p UTC" 
    ).replace(tzinfo=timezone.utc)

    day = match_date.strftime("%A")

    # --------------------------------------------------
    # Toss
    # --------------------------------------------------

    toss_line = next(
        line for line in lines
        if line.startswith("Toss ")
        ).replace("Toss ", "").strip()

    if "opt to bat" in toss_line:
        toss_winner = toss_line.replace("opt to bat", "").strip()
        toss_decision = "bat"
        batting_first = toss_winner
    elif "opt to bowl" in toss_line:
        toss_winner = toss_line.replace("opt to bowl", "").strip()
        toss_decision = "bowl"
        batting_first = (opponent_name if toss_winner == team_name else toss_winner)
    else:
        raise ValueError(f"Unsupported toss format:, {toss_line}")

    # --------------------------------------------------
    # Scores
    # --------------------------------------------------

    score_lines = [
        line 
        for line in lines 
        if re.search(
            r"\d+/\d+\s+\([\d.]+\s+Ov\)",
            line,
        )
    ]

    if len(score_lines) < 2:
        raise ValueError(
            f"Could not find two score lines: {score_lines}"
        )
    
    print("score_lines =", score_lines)

    first_score = parse_score(score_lines[0])
    second_score = parse_score(score_lines[1])

    # Determine which score belongs to our team.
    first_score_team = extract_score_team(score_lines[0])
    second_score_team = extract_score_team(score_lines[1])

    if first_score_team == our_team:
        team_score = first_score
        opponent_score = second_score
    elif second_score_team == our_team:
        team_score = second_score
        opponent_score = first_score
    else:
        raise ValueError(
            f"Could not match score to team: "
            f"{team_name}, {score_lines}"
        )

    # --------------------------------------------------
    # Result
    # --------------------------------------------------

    result = next(
        line for line in lines
        if line.startswith("Result ")
    ).replace("Result ", "").strip()

     # --------------------------------------------------
    # Captain
    # --------------------------------------------------
    # 2 Abhi (Red Wings) Captain 27
    captain_line = next((line for line in lines if "Captain" in line and team_name in line), None)
    captain = None
    if captain_line:
        captain = captain_line.split(" (")[0].split(" ", 1)[1]

    return Match(
         tournament_name=tournament_name,
        stage=stage,
        match_date=match_date,
        day=day,
        ground=ground,
        team_name=team_name,
        opponent_name=opponent_name,
        toss_winner=toss_winner,
        toss_decision=toss_decision,
        batting_first=batting_first,
        match_overs=team_score["overs"],
        team_runs=team_score["runs"],
        team_wickets=team_score["wickets"],
        opponent_runs=opponent_score["runs"],
        opponent_wickets=opponent_score["wickets"],
        result=result,
        captain=captain
    )

def parse_score(line: str) -> dict:
    match = re.search(r"(\d+)/(\d+)\s+\(([\d.]+)\s+Ov\)", line)
    if not match:
        raise ValueError(f"Could not parse score: {line}")

    return {
        "runs": int(match.group(1)),
        "wickets": int(match.group(2)),
        "overs": int(float(match.group(3)))
    }

def extract_score_team(line: str) -> str:
    # """
    # Example:
    # 'Total Red Wings 132/9 (20.0 Ov)'
    # 'The Trailblazers 100/10 (20.0 Ov)'
    # """

    score_match = re.search(
        r"\d+/\d+\s+\([\d.]+\s+Ov\)",
        line,
    )

    if not score_match:
        raise ValueError(
            f"Could not find score in line: {line}"
        )

    team_part = line[:score_match.start()].strip()

    team_part = team_part.removeprefix("Total").strip()

    return team_part
