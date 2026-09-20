from app.services.ai.cricket_assistant import ask_cricket_question
from test_data import innings
from test_match_parser import matches


our_team = "Red Wings"

answer = ask_cricket_question(
    "Who got the most batting opportunities in the last 12 matches?",
    innings,
    matches,
    our_team
)

print(answer)