from fastapi import APIRouter
from app.services.analytics.query_service import answer_batting_query

router = APIRouter()

@router.get("/batting")
def batting_analysis():
    result = answer_batting_query(innings)

    return result

