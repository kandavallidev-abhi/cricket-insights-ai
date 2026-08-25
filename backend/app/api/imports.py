from fastapi import APIRouter, File, UploadFile
from app.services.pdf_parser import extract_text 
from app.services.cricheroes.page_dectator import detect_pages
from app.services.cricheroes.match_parser import parse_match
from app.services.cricheroes.players_parser import parse_players
from app.services.cricheroes.innings_parser import parse_innings
from app.services.cricheroes.validator import validate_match

router = APIRouter()

@router.post("/scorecard")
async def upload_scorecard(file: UploadFile = File(...)) :
    file_content = await file.read()
    
    extracted_text = extract_text(file_content)
    # for index, page in enumerate(extracted_text):
    #     print(f"\n========== PAGE {index + 1} ==========")

    #     for line_number, line in enumerate(page.splitlines()):
    #         print(line_number, repr(line))

    pages = detect_pages(extracted_text)
    parsed_match = parse_match(pages["match"][0], "Red Wings")

    parsed_players = parse_players(pages["players"][0], parsed_match.team_name)

    parsed_match.players = parsed_players

    parsed_match.wicketkeeper = next((player.player_name for player in parsed_players if player.is_wicketkeeper == True), None)
    #parsed inngins
    parsed_innings = []
    for index, page in enumerate(pages["innings"], start=1):
        print(f"\n========== INNINGS PAGE {index} ==========")

    for line in page.splitlines()[:15]:
        print(repr(line))

    for innings_page in pages["innings"]:
        innings = parse_innings(innings_page, parsed_match.team_name, parsed_match.opponent_name)
        parsed_innings.append(innings)

    parsed_match.innings = parsed_innings

    validate_match(parsed_match)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "match": parsed_match
    }