from pydantic import BaseModel
from datetime import datetime
from app.models.match import InningsType

class BattingOpportunityDetail(BaseModel):
    match_date: datetime
    batting_position: int | None
    runs: int
    balls_faced: int
    strike_rate: float
    innings_type: InningsType
    position_weight: float | None

class BattingOpportunityResult(BaseModel):
    player_name: str
    opportunities: int
    batting_positions: dict[int, int]
    runs: int
    balls_faced: int
    strike_rate: float
    regular_opportunities: int
    super_over_opportunities: int
    total_position_weight: float
    average_position_weight: float
    opportunity_details: list[BattingOpportunityDetail]
    # opportunity_score: float
    # utilisation_score: float

class BowlingOpportunityResult(BaseModel):
    player_name: str
    matches_bowled: int
    overs: float
    wickets: int
    runs_conceded: int
    economy: float
