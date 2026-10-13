'''Warehouse Bin and Slot Allocation Service.'''
class BinLocatorService:
    @staticmethod
    def format_bin_code(zone: str, aisle: str, rack: str, shelf: str, bin_num: str) -> str:
        return f"{zone.upper()}-{aisle.zfill(2)}-{rack.zfill(2)}-{shelf.upper()}-{bin_num.zfill(2)}"

    @staticmethod
    def parse_bin_code(code: str) -> dict:
        parts = code.split("-")
        if len(parts) == 5:
            return {"zone": parts[0], "aisle": parts[1], "rack": parts[2], "shelf": parts[3], "bin": parts[4]}
        return {}
