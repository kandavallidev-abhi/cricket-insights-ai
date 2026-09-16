from app.models.match import Match


def select_recent_matches(
    matches: list[Match],
    number_of_matches: int
) -> list[Match]:

    if number_of_matches < 1:
        raise ValueError("number_of_matches must be at least 1")

    sorted_matches = sorted(
        matches,
        key=lambda match: match.match_date,
        reverse=True
    )

    return sorted_matches[:number_of_matches]