from io import BytesIO
from pypdf import PdfReader

def extract_text(file_content: bytes) -> list[str]:
    pdf = PdfReader(BytesIO(file_content))

    pages = [];

    for page in pdf.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return pages


