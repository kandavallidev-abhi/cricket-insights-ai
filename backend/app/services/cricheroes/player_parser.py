from app.models.match import MatchPlayer

def parse_players(page: str) -> list[MatchPlayer] :
    lines = [line for line in page.splitlines() if line.strip()]

    # find the player squad line+
    player_squad_index = next(index for index, line in enumerate(lines) if "Playing Squad" in line)
    # read all the line after player_squad_index
    for index in range(player_squad_index, len(lines)):
        print(index, lines[index])