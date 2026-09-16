from enum import Enum
from pydantic import BaseModel, Field

class BattingMetric(str, Enum):
    RUNS = "runs"
    STRIKE_RATE = "strike_rate"
    FOURS = "fours"
    SIXES = "sixes"
    BOUNDARIES = "boundaries"
    RUNS_WITHOUT_BOUNDARIES = "runs_without_boundaries"

class InningsScope(str, Enum):
    REGULAR = "regular"
    SUPER_OVER = "super_over"
    ALL = "all"

class BattingQuery(BaseModel):
    metric: BattingMetric
    rank: int = Field(ge= 1)
    innings_scope: InningsScope

class BowlingMetric(str, Enum):
    WICKETS="wickets"
    RUNS_CONCEDED="runs_conceded"
    OVERS="overs"
    ECONOMY="economy"
    DOT_BALLS="dot_balls"
    FOURS_CONCEDED="fours_conceded"
    SIXES_CONCEDED="sixes_conceded"
    WIDES="wides"
    NO_BALLS="no_balls"

class BowlingQuery(BaseModel):
    metric: BowlingMetric
    rank: int = Field(ge= 1)
    innings_scope: InningsScope

class QueryType(str, Enum):
    BATTING= "batting"
    BOWLING= "bowling"

class AnalyticsQuery(BaseModel):
    query_type: QueryType
    batting: BattingQuery | None = None
    bowling: BowlingQuery | None = None
    
class BattingOpportunityQuery(BaseModel):
    player_name: str | None = None
    match_count: int | None = Field(default=None, ge=1)

