from app.services.ai.llm_client import client
from app.services.ai.tools import (
    batting_ranking_tool,
    bowling_ranking_tool
)
from app.services.ai.tool_executor import execute_tool


def ask_cricket_question(question: str, innings, our_team: str) -> str:

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=question,
        tools=[
            batting_ranking_tool,
            bowling_ranking_tool
        ],
    )

    for item in response.output:

        if item.type == "function_call":

            result = execute_tool(
                item.name,
                item.arguments,
                innings,
                our_team
            )

            response = client.responses.create(
                model="gpt-5.6-luna",
                input=[
                    {
                        "role": "user",
                        "content": question
                    },
                    *response.output,
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result)
                    }
                ]
            )

            return response.output_text

    return response.output_text