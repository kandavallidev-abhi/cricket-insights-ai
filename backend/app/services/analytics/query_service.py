from app.models.analytic import BattingMetric, BattingQuery
from app.models.match import Innings
from app.services.analytics.batting_analytics import get_batting_ranking
from app.services.analytics.select_innings import select_innings

def answer_batting_query(innings: list[Innings], our_team: str):
    query = BattingQuery(
        metric=BattingMetric.FOURS,
        rank=1
    )
     
    selected_innings = select_innings(innings, query.innings_scope)

    selected_innings = [
        inning
        for inning in selected_innings
        if inning.batting_team == our_team
    ]

    result = get_batting_ranking(selected_innings, query)

    return result