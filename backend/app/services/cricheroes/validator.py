from app.models.match import Match


def validate_match(match: Match) -> None:
    # Basic team validation
    if match.team_name == match.opponent_name:
        raise ValueError("Team and opponent cannot be the same")

    # We expect exactly two innings
    if len(match.innings) != 2:
        raise ValueError(
            f"Expected 2 innings, found {len(match.innings)}"
        )

    for innings in match.innings:

        # Validate teams
        if innings.batting_team not in {
            match.team_name,
            match.opponent_name,
        }:
            raise ValueError(
                f"Unknown batting team: {innings.batting_team}"
            )

        if innings.bowling_team not in {
            match.team_name,
            match.opponent_name,
        }:
            raise ValueError(
                f"Unknown bowling team: {innings.bowling_team}"
            )

        if innings.batting_team == innings.bowling_team:
            raise ValueError(
                "Batting team and bowling team cannot be the same"
            )

        # Validate score
        if innings.runs < 0:
            raise ValueError("Runs cannot be negative")

        if innings.wickets < 0:
            raise ValueError("Wickets cannot be negative")

        if innings.wickets > 10:
            raise ValueError(
                f"Invalid wickets: {innings.wickets}"
            )

        # Validate batting players
        for player in innings.batting:
            if player.runs < 0:
                raise ValueError(
                    f"Invalid runs for {player.player_name}"
                )

            if player.balls_faced < 0:
                raise ValueError(
                    f"Invalid balls faced for {player.player_name}"
                )

        # Validate bowling players
        for bowler in innings.bowling:
            if bowler.runs_conceded < 0:
                raise ValueError(
                    f"Invalid runs conceded for {bowler.player_name}"
                )

            if bowler.wickets < 0:
                raise ValueError(
                    f"Invalid wickets for {bowler.player_name}"
                )