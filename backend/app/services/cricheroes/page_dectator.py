import re


def detect_pages(pages: list[str]) -> dict[str, list[str]]:
    result = {
        "match": [],
        "players": [],
        "innings": [],
    }

    for page in pages:
        lines = [
            line.strip()
            for line in page.splitlines()
            if line.strip()
        ]

        if "Match Details" in lines:
            result["match"].append(page)

        elif "Playing Squad" in lines:
            result["players"].append(page)

        elif any(
            re.search(r"\d+/\d+\s+\([\d.]+\s+Ov\)", line)
            and "Innings" in line
            for line in lines
        ):
            result["innings"].append(page)

    return result