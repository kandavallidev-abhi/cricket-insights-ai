from app.models.analytic import BattingMetric
from app.models.match import Innings
from app.services.analytics.batting_analytics import get_batting_ranking
from app.services.analytics.select_innings import select_innings
from app.services.ai.llm_client import parser_user_question

def answer_batting_query(innings: list[Innings], our_team: str, question: str):
    query = parser_user_question(question)
     
    selected_innings = select_innings(innings, query.innings_scope)

    selected_innings = [
        inning
        for inning in selected_innings
        if inning.batting_team == our_team
    ]

    result = get_batting_ranking(selected_innings, query)

    return result