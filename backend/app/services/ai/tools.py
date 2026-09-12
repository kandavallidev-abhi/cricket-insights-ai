from app.models.analytic import BattingQuery, BowlingQuery

batting_schema = BattingQuery.model_json_schema()
batting_schema["additionalProperties"] = False

batting_ranking_tool = {
    "type": "function",
    "name": "get_batting_ranking",
    "description": (
        "Get the batting ranking for the team based on a batting metric, "
        "ranking positions, and innings scope"
    ),
    "parameters": batting_schema,
    "strict": True
}

bowling_schema = BowlingQuery.model_json_schema()
bowling_schema["additionalProperties"] = False

bowling_ranking_tool = {
    "type": "function",
    "name": "get_bowling_ranking",
    "description": (
        "Get the bowling ranking for the team based on a bowling metric, "
        "ranking positions, and innings scope"
    ),
    "parameters": bowling_schema,
    "strict": True
}
