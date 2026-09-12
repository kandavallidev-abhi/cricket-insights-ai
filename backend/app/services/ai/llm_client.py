import os 
from dotenv import load_dotenv
from openai import OpenAI 
from app.models.analytic import AnalyticsQuery

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)

def parser_user_question(question: str, previous_query: AnalyticsQuery | None = None ) -> AnalyticsQuery :

    previous_context = ""
    if previous_query:
        previous_context= f""" 
            Previous Query:  {previous_query.model_dump_json()}
        """
    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=[{
            "role": "system",
            "content": """
            You are a cricket analytics query parser.
            
            Convert the user's question into an AnalyticsQuery

            if a previous query is provided:
            - Use it as context for follow up questions.
            - Preserve values that the user did not change.
            - Modify only the parts relevant to the new question.

            Innings scope rules:
            - If the user explicitly asks for regular innings, use REGULAR.
            - If the user explicitly asks for Super Over, use SUPER_OVER.
            - If the user does not specify an innings scope, use ALL.

            Examples:

            "Who hit the most sixes?"
            - batting metric = SIXES, rank = 1, innings_scope = ALL

            "Who took the most wickets?"
            - bowling metric = WICKETS, rank = 1, innings_scope = ALL

            "Who took the most wickets in the regular innings?"
            - bowling metric = WICKETS, rank = 1, innings_scope = REGULAR

            "Who took the most wickets in the Super Over?"
            - bowling metric = WICKETS, rank = 1, innings_scope = SUPER_OVER

            "What about the second most?"
            - preserve metric and innings scope, change rank = 2

            "What about fours?"
            - preserve rank and innings scope, change metric = FOURS

            "Show me the Super Over"
            - change innings_scope = SUPER_OVER

            If the question is a standalone question, create a new query.
            
            """
        },
        {
            "role": "user",
            "content": f""" 
            {previous_context}
            current question: {question}
            """
        }
        ],
        text_format=AnalyticsQuery,
    )

    return response.output_parsed
