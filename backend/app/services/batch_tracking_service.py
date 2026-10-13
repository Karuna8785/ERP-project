'''Inventory Lot & Batch Management (FEFO/FIFO).'''
from datetime import datetime, date

class BatchTrackingService:
    @staticmethod
    def sort_by_fefo(batches: list) -> list:
        return sorted(batches, key=lambda b: b.get("expiry_date", "9999-12-31"))

    @staticmethod
    def is_expired(expiry_date: str) -> bool:
        try:
            exp = datetime.strptime(expiry_date, "%Y-%m-%d").date()
            return exp < date.today()
        except Exception:
            return False
