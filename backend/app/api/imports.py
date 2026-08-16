from fastapi import APIRouter, File, UploadFile
from app.services.pdf_parser import extract_text 
from app.services.cricheroes.match_parser import parse_match
from app.services.cricheroes.players_parser import parse_players
from app.services.cricheroes.innings_parser import parse_innings

router = APIRouter()

@router.post("/scorecard")
async def upload_scorecard(file: UploadFile = File(...)) :
    file_content = await file.read()
    
    extracted_text = extract_text(file_content)
    # for index, page in enumerate(extracted_text):
    #     print(f"\n========== PAGE {index + 1} ==========")

    #     for line_number, line in enumerate(page.splitlines()):
    #         print(line_number, repr(line))

    parsed_match = parse_match(extracted_text[0], "Red Wings")
    parsed_players = parse_players(extracted_text[1], parsed_match.team_name)
    parsed_match.players = parsed_players
    parsed_match.wicketkeeper = next((player.player_name for player in parsed_players if player.is_wicketkeeper == True), None)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "match": parsed_match
    }