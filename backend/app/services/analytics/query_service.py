from app.models.analytic import BattingMetric
from app.models.match import Innings
from app.services.analytics.batting_analytics import get_batting_ranking
from app.services.analytics.select_innings import select_innings
from app.services.ai.llm_client import parser_user_question
from app.services.analytics.bowling_analytics import get_bowling_ranking

def get_batting_rankings(innings: list[Innings], our_team: str, question: str):
    query = parser_user_question(question)
     
    selected_innings = select_innings(innings, query.innings_scope)

    selected_innings = [
        inning
        for inning in selected_innings
        if inning.batting_team == our_team
    ]

    result = get_batting_ranking(selected_innings, query)

    return result

def get_bowling_rankings(innings: list[Innings], our_team: str, question: str):
    query = parser_user_question(question)
    selected_innings = select_innings(innings, query.bowling.innings_scope)

    selected_innings = [
        inning
        for inning in selected_innings
        if inning.bowling_team == our_team
    ]

    result = get_bowling_ranking(selected_innings, query.b)

    return result
