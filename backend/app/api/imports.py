from fastapi import APIRouter, File, UploadFile
from app.services.pdf_parser import extract_text 

router = APIRouter()

@router.post("/scorecard")
async def upload_scorecard(file: UploadFile = File(...)) :
    file_content = await file.read()
    
    extracted_text = extract_text(file_content)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "text": extracted_text
    }