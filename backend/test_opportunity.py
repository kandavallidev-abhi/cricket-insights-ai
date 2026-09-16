from app.services.analytics.opportunity_analytics import get_batting_opportunities
from test_match_parser import matches


results = get_batting_opportunities(matches, "Red Wings")

for result in results:
    print(result)