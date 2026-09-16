from app.services.analytics.batting_opportunity_analysis import get_batting_opportunity_analysis
from test_match_parser import matches


results = get_batting_opportunity_analysis(
    matches,
    "Red Wings"
)

for result in results:
    print(result)