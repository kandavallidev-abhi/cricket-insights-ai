from app.services.ai.response_generator import generate_answer

question = "Who hit the most fours?"

analytics_result = [
    {
        "player_name": "jd",
        "value": 4
    },
    {
        "player_name": "Amarnath Mishra",
        "value": 4
    }
]

answer = generate_answer(
    question,
    analytics_result
)
print(answer)