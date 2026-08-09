from pydantic import BaseModel

class BattingPerformance(BaseModel):
    player_name: str
    batting_position: int | None = None
    
    dismissal: str | None = None
    dismissal_details: str | None = None

    runs: int
    balls_faced: int
    minutes: int

    fours: int
    sixes: int
    strike_rate: float

class BowlingPerformance(BaseModel):
    player_name: str

    overs: str
    maidens: int

    runs_conceded: int
    wickets: int

    dot_balls: int
    fours_conceded: int
    sixes_conceded: int

    wides: int
    no_balls: int

    economy: float

class FieldingPerformance(BaseModel): 
    player_name: str

    catches: int = 0
    run_outs: int = 0
    run_out_assists: int = 0

class WicketKeepingPerformance(BaseModel):
    player_name: str

    catches: int = 0
    stumpings: int = 0
    run_outs: int = 0
    run_out_assists: int = 0