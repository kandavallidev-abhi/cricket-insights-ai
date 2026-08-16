from app.models.match import MatchPlayer

def parse_players(page: str, our_team: str) -> list[MatchPlayer] :
    lines = [line.strip() for line in page.splitlines() if line.strip()]

    # find the player squad line+
    player_squad_index = next(index for index, line in enumerate(lines) if "Playing Squad" in line)
    # extract teams from player squad
    first_team = lines[player_squad_index + 1]
    second_team = lines[player_squad_index + 2]
    # identify team position
    if first_team == our_team:
        our_team_position = 1
    else:
        our_team_position = 2
    
    player = []
    expected_number = 1
    is_c = False
    is_wk = False
    # read all the line after player_squad_index+3
    for index in range(player_squad_index+2, len(lines)):
        if lines[index] != str(expected_number):
            continue
        
        raw_player_name = lines[index+our_team_position]

        if "C" in raw_player_name or "WK" in raw_player_name:
            player_name = raw_player_name.split(' (')[0]
            is_wk = "WK" in raw_player_name
            is_c = "C" in raw_player_name
        else:
            player_name = raw_player_name
            is_wk = False
            is_C = False
        player.append(MatchPlayer(
            player_name= player_name,
            is_captain= is_c,
            is_wicketkeeper= is_wk
        ))
        expected_number += 1

    return player
        