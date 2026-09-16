from app.models.match import Match
from app.models.opportunity import BattingOpportunityResult
from app.services.analytics.opportunity_analytics import get_batting_opportunities
from app.services.analytics.select_matches import select_recent_matches
from app.models.analytic import BattingOpportunityQuery

def get_batting_opportunity_analysis(
    matches: list[Match],
    team_name: str,
    query: BattingOpportunityQuery
) -> list[BattingOpportunityResult]:

    selected_matches = matches

    if query.match_count is not None:
        selected_matches = select_recent_matches(matches, query.match_count)

    results = get_batting_opportunities(selected_matches, team_name)

    if query.player_name is not None:
        results = [
            player
            for player in results
            player.name.lower() == query.player_name.lower()
        ]


    results.sort(
        key=lambda player: (
            player.opportunities,
            player.average_position_weight
        ),
        reverse=True
    )

    return results