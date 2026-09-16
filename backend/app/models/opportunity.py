from pydantic import BaseModel


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
    # opportunity_score: float
    # utilisation_score: float

class BowlingOpportunityResult(BaseModel):
    player_name: str
    matches_bowled: int
    overs: float
    wickets: int
    runs_conceded: int
    economy: float