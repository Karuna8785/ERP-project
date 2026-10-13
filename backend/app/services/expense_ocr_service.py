'''Receipt OCR Line-Item Extraction Interface.'''
import re

class ExpenseOCRService:
    @staticmethod
    def extract_totals_and_date(ocr_text: str) -> dict:
        date_pattern = r'(\d{2}[/-]\d{2}[/-]\d{4})'
        date_match = re.search(date_pattern, ocr_text)
        return {
            "detected_date": date_match.group(1) if date_match else None,
            "status": "PARSED"
        }
