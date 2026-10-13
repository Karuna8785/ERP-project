'''Barcode Parsing and GS1 Standard Normalizer.'''
class BarcodeService:
    @staticmethod
    def validate_ean13(code: str) -> bool:
        if len(code) != 13 or not code.isdigit():
            return False
        digits = [int(d) for d in code]
        checksum = sum(digits[i] * (1 if i % 2 == 0 else 3) for i in range(12))
        check_digit = (10 - (checksum % 10)) % 10
        return check_digit == digits[12]
