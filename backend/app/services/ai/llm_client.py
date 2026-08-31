import os 
from dotenv import load_dotenv
from openai import OpenAI 
from app.models.analytic import BattingQuery

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)

def parser_user_question(question: str) -> str :
    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=[{
            "role": "system",
            "content": """
            You are a cricket analytics query parser.
            
            Convert the user's question into BattingQuery
            
            Rules:
            
            -"sixes", "sixers", "sixs", "maximus" -> SIXES
            -"fours" -> FOURS
            -"runs", "score" -> RUNS
            -"most", "highest" -> rank 1
            -"second most", "second highest" -> rank 2
            -"third most", "third highest" -> rank 3
            -If the user does not specify an Innings Type -> ALL
            -"regular innings" -> REGULAR
            -"super over" -> SUPER OVER

            Return only the structured BattingQuery.

            """
        },
        {
            "role": "user",
            "content": question
        }
        ],
        text_format=BattingQuery,
    )

    return response.output_parsed
