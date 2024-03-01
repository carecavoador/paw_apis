from pathlib import Path

import pytesseract
from pdf2image import convert_from_path

POPPLER = Path(__file__).parent.joinpath("poppler/Library/bin")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def generate_texts_from_image_pdf(pdf_path: Path, lang: str = "por") -> str:
    """Performs an OCR in a PDF file and returns it's text content."""
    image = convert_from_path(pdf_path, poppler_path=POPPLER)
    text: str = pytesseract.image_to_string(image[0], lang=lang)
    print(text)
    return text
