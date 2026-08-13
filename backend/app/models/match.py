from datetime import datetime
from pydantic import BaseModel, Field
from .performance import BattingPerformance, BowlingPerformance

class MatchPlayer(BaseModel):
    player_name: str

    is_captain: bool = False
    is_wicketkeeper: bool = False

class FallOfWicket(BaseModel):
    score: int
    wicket_number: int
    player_name: str
    over: str

class Innings(BaseModel): 
    batting_team: str
    bowling_team: str

    overs: str
    runs: int
    wickets: int

    batting: list[BattingPerformance] = Field(default_factory = list)
    bowling: list[BowlingPerformance] = Field(default_factory = list)

    fall_of_wickets: list[FallOfWicket] = Field(default_factory = list)

class Match(BaseModel):
    tournament_name: str
    stage: str | None = None

    match_date: datetime
    day: str | None = None

    ground: str

    team_name: str
    opponent_name: str

    toss_winner: str
    toss_decision: str
    batting_first: str

    match_overs: int

    team_runs: int
    team_wickets: int

    opponent_runs: int
    opponent_wickets: int

    result: str

    captain: str | None = None
    wicketkeeper: str | None = None 

    players: list[MatchPlayer] = Field(default_factory=list)
    innings: list[Innings] = Field(default_factory=list)
