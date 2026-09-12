from app.services.ai.llm_client import client
from app.services.ai.tools import (
    batting_ranking_tool,
    bowling_ranking_tool
)
from app.services.ai.tool_executor import execute_tool
from test_data import innings


our_team = "Red Wings"
question = "Who hit the most sixes?"
question = "Who took the most wickets?"

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

        print("Tool name:", item.name)
        print("Arguments:", item.arguments)
        print("Call ID:", item.call_id)

        result = execute_tool(
            item.name,
            item.arguments,
            innings,
            our_team
        )

        print("Analytics result:", result)

        # Send the tool result back to the model
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
            ],
            tools=[
                batting_ranking_tool,
                bowling_ranking_tool
            ],
        )

        print("Final answer:", response.output_text)