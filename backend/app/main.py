from fastapi import FastAPI
from app.api.imports import router as imports_router
from test_data import innings
from app.services.ai.cricket_assistant import ask_cricket_question

app = FastAPI(
    title= "Cricket Insights AI API",
    version= "0.1.0"
)

app.include_router(
    imports_router,
    prefix="/api/v1/imports",
)

@app.post("/ask")
def ask_question(question: str):
    answer = ask_cricket_question(
        question,
        innings,
        "Red Wings"
    )
    return {
        "answer": answer
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "cricket-insights-ai-api",
    }

