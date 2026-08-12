from app.services.cricheroes.match_parser import parse_match


page = """SUPERSTARS T20 LEAGUE 29 (WEEKEND DAY) BY S2 SPORTS
Silver Final
Red Wings
The Trailblazers
SS Cricket Ground
2026-08-02, 09:24 AM UTC
Red Wings opt to bat
"""


parse_match(page)