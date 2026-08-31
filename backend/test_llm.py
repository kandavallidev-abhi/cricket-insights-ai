from app.services.ai.llm_client import parser_user_question

question= "Who hit most sixers?"
query=parser_user_question(question)
print(query)
print("Metric:", query.metric)
print("Rank:", query.rank)
print("Innings: ", query.innings_scope)