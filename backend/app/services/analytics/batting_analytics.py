from app.models.match import Innings
from app.models.performance import BattingPerformance
from app.models.analytic import BattingQuery

def get_batting_ranking(innings: Innings, query: BattingQuery) -> list[BattingPerformance]:

    if not innings.batting:
        return []
    
    metric_functions = {
        "runs": lambda player: player.runs,
        "fours": lambda player: player.fours,
        "sixes": lambda player: player.sixes,
        "strike_rate": lambda player: player.strike_rate,
        "boundaries": lambda player: player.fours+player.sixes,
        "runs_without_boundaries": lambda player: player.runs - (player.fours * 4 + player.sixes * 6)
    }
    
    if query.metric.value not in metric_functions:
        raise ValueError(f"Unsupported batting metric: {query.metric.value}")

    metric_function = metric_functions[query.metric.value]
    
    if query.rank < 1:
        raise ValueError(f"Rank should be greater than 0")

    batting_performance_list = sorted(
        innings.batting,
        key=metric_function,
        reverse=True
    )

    if query.rank > len(batting_performance_list):
        return []
    
    rank_value = metric_function(batting_performance_list[query.rank - 1])

    return [ 
        player
        for player in batting_performance_list
        if metric_function(player) ==  rank_value
    ]





