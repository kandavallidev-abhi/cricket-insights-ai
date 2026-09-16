import re
from app.models.match import MatchPlayer


def parse_players(page: str, our_team: str) -> list[MatchPlayer]:
    lines = [line.strip() for line in page.splitlines() if line.strip()]

    player_squad_index = next(
        index
        for index, line in enumerate(lines)
        if "Playing Squad" in line
    )

    first_team = lines[player_squad_index + 1]
    second_team = lines[player_squad_index + 2]

    if first_team == our_team:
        our_team_position = 1
    else:
        our_team_position = 2

    players = []
    expected_number = 1

    for index in range(player_squad_index + 3, len(lines)):

        # Normal format:
        #
        # 10
        # Kasi Vishwanth Reddy
        # Hegde 07
        #
        if lines[index] == str(expected_number):
            raw_player_name = lines[index + our_team_position]

        else:
            # Combined format:
            #
            # 11 Vardhan ( WK )
            # Paulus Kumar
            #
            match = re.match(
                rf"^{expected_number}\s+(.+)$",
                lines[index]
            )

            if not match:
                continue

            if our_team_position == 1:
                raw_player_name = match.group(1)
            else:
                raw_player_name = lines[index + 1]

        is_wk = bool(re.search(r"\(\s*WK\s*\)", raw_player_name, re.IGNORECASE))
        is_c = bool(re.search(r"\(\s*C\s*\)", raw_player_name, re.IGNORECASE))

        player_name = re.sub(
            r"\s*\(\s*(?:C|WK)\s*\)",
            "",
            raw_player_name,
            flags=re.IGNORECASE
        ).strip()

        players.append(
            MatchPlayer(
                player_name=player_name,
                is_captain=is_c,
                is_wicketkeeper=is_wk
            )
        )

        expected_number += 1

        # We currently expect a maximum of 12 players.
        if expected_number > 12:
            break

    return players