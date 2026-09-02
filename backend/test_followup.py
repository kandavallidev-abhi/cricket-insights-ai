from app.services.ai.llm_client import parser_user_question

q1 = "Who hit the most sixes"

query1 = parser_user_question(q1)

print("QUERY 1:")
print(query1)

#follow up question 
q2 = "what about the second most"

query2 = parser_user_question(q2, previous_query=query1)

print("\nQUERY 2:")
print(query2)
