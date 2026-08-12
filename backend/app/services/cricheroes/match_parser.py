from app.models.match import Match
from datetime import datetime,timezone
import re

def parse_match(page: str) -> Match:
    lines = [line.strip() for line in page.splitlines() if line.strip()]
    
    tournament_name = lines[0]
    stage = lines[1].strip("()")

    team_line = lines[4]
    team_name = team_line.replace("Match", "").replace("vs", "").strip()

    opponent_name = lines[5]

    ground = (lines[6].replace("Ground ", "") + " " + lines[7]).strip()

    date_text = lines[8].replace("Date ", "").strip()
    match_date = datetime.strptime(
        date_text,
        "%Y-%m-%d, %I:%M %p UTC" 
    ).replace(tzinfo=timezone.utc)
    day = match_date.strftime("%A")
    # 11 'Toss Red Wings opt to bat'
    toss_line = lines[10].replace("Toss ", "").strip()

    if "opt to bat" in toss_line:
        toss_winner = toss_line.replace("opt to bat", "").strip()
        toss_decision = "bat"
        batting_first = toss_winner
    elif "opt to bowl" in toss_line:
        toss_winner = toss_line.replace("opt to bowl", "").strip()
        toss_decision = "bowl"
        batting_first = opponent_name
    else:
        raise ValueError(f"Unsupported toss format:, {toss_line}")

    team_score = parse_score(lines[11])
    opponent_score = parse_score(lines[12])

    result = lines[13].replace("Result", "").strip()
    # 2 Abhi (Red Wings) Captain 27
    captain_line = next(line for line in lines if "Captain" in line and team_name in line)
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

# 0 '\xa0'
# 1 'SUPERSTARS T20 LEAGUE...'
# 2 '(Silver Final)'
# 3 '8/4/26, 3:55 AM cricheroes.com 1 of 4'
# 4 'Match Details'
# 5 'Match Red Wings vs'
# 6 'The Trailblazers'
# 7 'Ground S2 Sports Infinity Cricket Arena,'
# 8 'Hyderabad (Telangana)'
# 9 'Date 2026-08-02, 09:24 AM UTC'
# 10 'Match Result'
# 11 'Toss Red Wings opt to bat'
# 12 'Total Red Wings 132/9 (20.0 Ov)'
# 13 'The Trailblazers 100/10 (20.0 Ov)'
# 14 'Result Red Wings won by 32 runs'
# --
# ['SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS', '(Silver Final)', '8/4/26, 3:55 AM cricheroes.com 1 of 4', 'Match Details', 'Match Red Wings vs', 'The Trailblazers', 'Ground S2 Sports Infinity Cricket Arena,', 'Hyderabad (Telangana)', 'Date 2026-08-02, 09:24 AM UTC', 'Match Result', 'Toss Red Wings opt to bat', 'Total Red Wings 132/9 (20.0 Ov)', 'The Trailblazers 100/10 (20.0 Ov)', 'Result Red Wings won by 32 runs', 'Best Performances - Batsmen', 'Players Name R B 4s 6s SR', 'Sandeep Mulpuri 59 53 5 1 111.32', 'Sk 54 55 3 2 98.18', 'Sai 24 16 3 1 150.00', 'Best Performances - Bowlers', 'Players Name O M R W Eco', 'Rakesh 1.0 0 3 3 3.00', 'Aamir Raina 4.0 0 15 3 3.75', 'Sai 4.0 0 17 3 4.25', 'Match Officials', 'No Name Role Signature', '1 Shawariq Scorer', '2 Abhi (Red Wings) Captain', '3 Amit Sharma (The Trailblazers) Captain']