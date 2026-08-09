from fastapi import FastAPI
from app.api.imports import router as imports_router

app = FastAPI(
    title= "Cricket Insights AI API",
    version= "0.1.0"
)

app.include_router(
    imports_router,
    prefix="/api/v1/imports",
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "cricket-insights-ai-api",
    }

