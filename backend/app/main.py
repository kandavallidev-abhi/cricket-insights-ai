from fastapi import FastAPI

app = FastAPI(
    title= "Cricket Insights AI API",
    version= "0.1.0"
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "cricket-insights-ai-api",
    }

