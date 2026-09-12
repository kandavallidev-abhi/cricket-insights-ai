from app.models.analytic import BowlingMetric, BowlingQuery
from app.models.match import Innings

def get_bowling_ranking(
    innings: Innings,
    query: BowlingQuery
):
    bowling_performance_list = [
        player
        for inning in innings
        for player in inning.bowling
    ]
    player_stats = {}

    for player in bowling_performance_list:

        if player.player_name not in player_stats:
            player_stats[player.player_name] = {
                "wickets": 0,
                "runs_conceded": 0,
                "overs": 0.0,
                "dot_balls": 0,
                "fours_conceded": 0,
                "sixes_conceded": 0,
                "wides": 0,
                "no_balls": 0,
                "economy": 0.0
            }

        stats = player_stats[player.player_name]

        stats["wickets"] += player.wickets
        stats["runs_conceded"] += player.runs_conceded
        stats["dot_balls"] += player.dot_balls
        stats["fours_conceded"] += player.fours_conceded
        stats["sixes_conceded"] += player.sixes_conceded
        stats["wides"] += player.wides
        stats["no_balls"] += player.no_balls

        over_parts = player.overs.split(".")
        overs = int(over_parts[0])
        balls = int(over_parts[1]) if len(over_parts) > 1 else 0

        stats["overs"] += overs + (balls / 6)

        if stats["overs"] > 0:
            stats["economy"] = stats["runs_conceded"] / stats["overs"]
        else:
            stats["economy"] = 0.0
        
    ranked_players=[]
    
    for player_name, stats in player_stats.items():

        if query.metric == BowlingMetric.WICKETS:
            value = stats["wickets"]

        elif query.metric == BowlingMetric.RUNS_CONCEDED:
            value = stats["runs_conceded"]

        elif query.metric == BowlingMetric.OVERS:
            value = stats["overs"]

        elif query.metric == BowlingMetric.ECONOMY:
            value = stats["economy"]

        elif query.metric == BowlingMetric.DOT_BALLS:
            value = stats["dot_balls"]

        elif query.metric == BowlingMetric.FOURS_CONCEDED:
            value = stats["fours_conceded"]

        elif query.metric == BowlingMetric.SIXES_CONCEDED:
            value = stats["sixes_conceded"]

        elif query.metric == BowlingMetric.WIDES:
            value = stats["wides"]

        elif query.metric == BowlingMetric.NO_BALLS:
            value = stats["no_balls"]

        ranked_players.append({
            "player_name": player_name,
            "value": value
        })
    
    reverse = query.metric != BowlingMetric.ECONOMY

    ranked_players.sort(
        key=lambda player: player["value"],
        reverse=reverse
    )
    current_rank = 0
    previous_value = None

    for player in ranked_players:
        if player["value"] != previous_value:
            current_rank += 1
            previous_value = player["value"]

        player["rank"] = current_rank

    result = [player for player in ranked_players if player["rank"]==query.rank]

    return result