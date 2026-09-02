from app.services.ai.llm_client import client

def generate_answer(question: str, analytics_result) -> str:

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=[
            {
                "role": "system",
                "content": """
                You are cricket analytics assistant.

                Generate a concise and natural response to the users question
                using the verified analytics result provided by the application.

                Rules:
                - The analytics result is already calculated and verified.
                - Do not calculate or modify any statistics.
                - Do not invent players, numbers, or facts.
                - use only the information provided in the analytics result.
                - If multiple players have the same highest value, clearly mention that they are tied.
                """
            },
            {
                "role": "user",
                "content": f"""
                question: {question}
                verified analytics result: {analytics_result}"""
            }
        ]
    )

    return response.output_text

