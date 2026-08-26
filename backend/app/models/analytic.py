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
    rank: int = Field(default= 1, ge= 1)
    innings_scope: InningsScope = InningsScope.ALL
