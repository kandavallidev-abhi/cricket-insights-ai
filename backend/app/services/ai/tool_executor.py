import json

from app.models.analytic import BattingQuery, BowlingQuery
from app.services.analytics.batting_analytics import get_batting_ranking
from app.services.analytics.bowling_analytics import get_bowling_ranking
from app.services.analytics.select_innings import select_innings


def execute_batting_ranking(
    arguments: str,
    innings,
    our_team: str
):
    arguments_dict = json.loads(arguments)

    query = BattingQuery.model_validate(arguments_dict)

    selected_innings = select_innings(
        innings,
        query.innings_scope
    )

    selected_innings = [
        inning
        for inning in selected_innings
        if inning.batting_team == our_team
    ]

    return get_batting_ranking(
        selected_innings,
        query
    )

def execute_bowling_ranking(
    arguments: str,
    innings,
    our_team: str
): 
    arguments_dict = json.loads(arguments)

    query = BowlingQuery.model_validate(arguments_dict)

    selected_innings = select_innings(
        innings,
        query.innings_scope
    )

    selected_innings = [
        inning
        for inning in selected_innings
        if inning.bowling_team == our_team
    ]

    return get_bowling_ranking(
        selected_innings,
        query
    )

def execute_tool(
    tool_name: str,
    arguments: str,
    innings,
    our_team: str
):
    if tool_name == "get_batting_ranking":
        return execute_batting_ranking(
            arguments,
            innings,
            our_team
        )

    if tool_name == "get_bowling_ranking":
        return execute_bowling_ranking(
            arguments,
            innings,
            our_team
        )

    raise ValueError(f"Unknown tool: {tool_name}")