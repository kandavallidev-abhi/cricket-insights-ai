from app.models.opportunity import BattingOpportunityResult
from app.models.match import Match, InningsType


def get_batting_opportunities(
    matches: list[Match],
    team_name: str
) -> list[BattingOpportunityResult]:

    player_stats = {}

    for match in matches:

        team_size = len(match.players)

        for inning in match.innings:

            if inning.batting_team != team_name:
                continue

            if inning.innings_type == InningsType.REGULAR:

                for batter in inning.batting:

                    if batter.player_name not in player_stats:
                        player_stats[batter.player_name] = {
                            "opportunities": 0,
                            "regular_opportunities": 0,
                            "super_over_opportunities": 0,
                            "batting_positions": {},
                            "total_position_weight": 0.0,
                            "runs": 0,
                            "balls_faced": 0
                        }

                    stats = player_stats[batter.player_name]

                    stats["opportunities"] += 1
                    stats["regular_opportunities"] += 1

                    position = batter.batting_position

                    if position is not None:

                        if position > team_size:
                            raise ValueError(
                                f"Invalid batting position {position} "
                                f"for team size {team_size} "
                                f"for player {batter.player_name}"
                            )

                        if position not in stats["batting_positions"]:
                            stats["batting_positions"][position] = 0

                        stats["batting_positions"][position] += 1

                        position_weight = (
                            team_size - position + 1
                        ) / team_size

                        stats["total_position_weight"] += position_weight

                    stats["runs"] += batter.runs
                    stats["balls_faced"] += batter.balls_faced

            elif inning.innings_type == InningsType.SUPER_OVER:

                for batter in inning.batting:

                    if batter.player_name not in player_stats:
                        player_stats[batter.player_name] = {
                            "opportunities": 0,
                            "regular_opportunities": 0,
                            "super_over_opportunities": 0,
                            "batting_positions": {},
                            "total_position_weight": 0.0,
                            "runs": 0,
                            "balls_faced": 0
                        }

                    stats = player_stats[batter.player_name]

                    stats["opportunities"] += 1
                    stats["super_over_opportunities"] += 1

                    stats["runs"] += batter.runs
                    stats["balls_faced"] += batter.balls_faced

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