from app.models.analytic import BattingQuery, BowlingQuery, BattingOpportunityQuery

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

batting_opp_schema = BattingOpportunityQuery.model_json_schema()
batting_opp_schema["additionalProperties"] = False
batting_opp_schema["required"] = ["player_name", "match_count"]

batting_opportunity_tool = {
    "type": "function",
    "name": "get_batting_opportunity",
    "description": (
        "Analyze batting opportunities for the team. "
        "Use this when the user asks how many times a player batted, "
        "what batting positions they received, or who received the "
        "most batting opportunities. "
        "Opportunity is based on actual batting appearances and "
        "batting position context, not performance alone."
    ),
    "parameters": batting_opp_schema,
    "strict": True
}