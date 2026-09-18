from app.models.match import Match
from app.models.opportunity import BattingOpportunityResult


def get_batting_opportunities(
    matches: list[Match],
    team_name: str
) -> list[BattingOpportunityResult]:

    player_stats = {}

    for match in matches:

        # Initialize every squad player
        for player in match.players:
            if player.player_name not in player_stats:
                player_stats[player.player_name] = {
                    "opportunities": 0,
                    "regular_opportunities": 0,
                    "super_over_opportunities": 0,
                    "batting_positions": {},
                    "total_position_weight": 0.0,
                    "runs": 0,
                    "balls_faced": 0
                }

        team_size = len(match.players)

        for inning in match.innings:

            if inning.batting_team != team_name:
                continue

            for batting in inning.batting:

                if batting.player_name not in player_stats:
                    continue

                stats = player_stats[batting.player_name]

                stats["opportunities"] += 1
                stats["runs"] += batting.runs
                stats["balls_faced"] += batting.balls_faced

                if inning.innings_type.value == "regular":

                    stats["regular_opportunities"] += 1

                    position = batting.batting_position

                    if position is not None:
                        stats["batting_positions"][position] = (
                            stats["batting_positions"].get(position, 0) + 1
                        )

                        position_weight = (
                            team_size - position + 1
                        ) / team_size

                        stats["total_position_weight"] += position_weight

                elif inning.innings_type.value == "super_over":

                    stats["super_over_opportunities"] += 1

    results = []

    for player_name, stats in player_stats.items():

        if stats["balls_faced"] > 0:
            strike_rate = (
                stats["runs"] / stats["balls_faced"]
            ) * 100
        else:
            strike_rate = 0.0

        if stats["regular_opportunities"] > 0:
            average_position_weight = (
                stats["total_position_weight"]
                / stats["regular_opportunities"]
            )
        else:
            average_position_weight = 0.0

        results.append(
            BattingOpportunityResult(
                player_name=player_name,
                opportunities=stats["opportunities"],
                regular_opportunities=stats["regular_opportunities"],
                super_over_opportunities=stats["super_over_opportunities"],
                batting_positions=stats["batting_positions"],
                total_position_weight=stats["total_position_weight"],
                average_position_weight=average_position_weight,
                runs=stats["runs"],
                balls_faced=stats["balls_faced"],
                strike_rate=strike_rate
            )
        )

    return results