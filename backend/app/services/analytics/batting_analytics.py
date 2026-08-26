from app.models.match import Innings
from app.models.performance import BattingRankingResult
from app.models.analytic import BattingQuery

def get_batting_ranking(innings: list[Innings], query: BattingQuery) -> list[BattingRankingResult]:


    # if not innings.batting:
    #     return []
    
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

    batting_performance_list = [player for inning in innings for player in inning.batting]

    player_metrics_totals = {}
    for player in batting_performance_list:
        value = metric_function(player)

        if player.player_name in player_metrics_totals:
            player_metrics_totals[player.player_name] += value
        else:
            player_metrics_totals[player.player_name] = value

    metric_values = sorted(
        set(player_metrics_totals.values()),
        reverse=True
    )

    if query.rank > len(metric_values):
        return []
    
    rank_value = metric_values[query.rank - 1]

    ranked_players = [
        BattingRankingResult( 
            player_name=player_name,
            value=value
        )
        for player_name, value in player_metrics_totals.items()
        if value == rank_value
    ]

    return ranked_players





