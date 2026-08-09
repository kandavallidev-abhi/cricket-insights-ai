from datetime import datetime, timezone

from .match import Match, MatchPlayer, Innings, BattingPerformance, BowlingPerformance, FallOfWicket

players = [
    MatchPlayer(
        player_name= "Abhi",
        is_captain= True
    ),
    MatchPlayer(
        player_name= "Naveen Kumar",
        is_wicketkeeper= True
    )
]

batting_performance = BattingPerformance(
    player_name= "Sandeep Mulpuri",
    batting_position= 3,
    dismissal= "caught",
    dismissal_details="c Hashmat b WASEEM YOUSUF",
    runs=59,
    balls_faced=53,
    minutes=79,
    fours=5,
    sixes=1,
    strike_rate=111.32
)

rakesh_bowling = BowlingPerformance(
    player_name="Rakesh",
    overs="1",
    maidens=0,
    runs_conceded=3,
    wickets=3,
    dot_balls=3,
    fours_conceded=0,
    sixes_conceded=0,
    wides=0,
    no_balls=0,
    economy=3.00,
)

fall_of_wickets = [
    FallOfWicket(
        score=15,
        wicket_number=1,
        player_name="JD",
        over="1.4",
    ),
    FallOfWicket(
        score=16,
        wicket_number=2,
        player_name="Abhi",
        over="2",
    ),
    FallOfWicket(
        score=19,
        wicket_number=3,
        player_name="Naveen Kumar",
        over="2.3",
    ),
    FallOfWicket(
        score=19,
        wicket_number=4,
        player_name="SRI",
        over="2.5",
    ),
    FallOfWicket(
        score=36,
        wicket_number=5,
        player_name="Rakesh",
        over="5.2",
    ),
    FallOfWicket(
        score=47,
        wicket_number=6,
        player_name="Rahul Abraham N",
        over="8.4",
    ),
    FallOfWicket(
        score=95,
        wicket_number=7,
        player_name="Sudheer Reddy",
        over="15.4",
    ),
    FallOfWicket(
        score=127,
        wicket_number=8,
        player_name="Sai",
        over="19.1",
    ),
    FallOfWicket(
        score=132,
        wicket_number=9,
        player_name="Sandeep Mulpuri",
        over="20",
    ),
]

innings = Innings(
    batting_team= "Red Wings",
    bowling_team= "The Trailblazers",
    overs="20.0",
    runs=132,
    wickets=9,
    batting= [batting_performance],
    bowling= [rakesh_bowling],
    fall_of_wickets=fall_of_wickets
)
match = Match(
    tournament_name="SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS",
    stage="Silver Final",
    match_date=datetime(
        2026,
        8,
        2,
        9,
        24,
        tzinfo=timezone.utc,
    ),
    ground="SS Cricket Ground",
    team_name="Red Wings",
    opponent_name="The Trailblazers",
    toss_winner="Red Wings",
    toss_decision="bat",
    batting_first="Red Wings",
    match_overs=20,
    team_runs=132,
    team_wickets=9,
    opponent_runs=100,
    opponent_wickets=10,
    result="Red Wings won by 32 runs",
    captain="Abhi",
    wicketkeeper="Naveen Kumar",
    players= players,
    innings= [innings]
)

print(match)