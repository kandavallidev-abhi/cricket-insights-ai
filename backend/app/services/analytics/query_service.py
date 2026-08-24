from app.models.analytics import BattingMetric, BattingQuery
from app.models.match import Innings
from app.services.analytics.batting_analytics import get_batting_ranking

def answer_batting_query(innings: Innings):
     query = BattingQuery(
        metric=BattingMetric.FOURS,
        rank=2
    )

    result = get_batting_ranking(innings, query)

    return result