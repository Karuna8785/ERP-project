'''Accounts Receivable (AR) Aging Engine.'''
from datetime import date

class ReceivablesAgingService:
    @staticmethod
    def categorize_overdue_days(days_overdue: int) -> str:
        if days_overdue <= 0: return "CURRENT"
        if days_overdue <= 30: return "1_TO_30_DAYS"
        if days_overdue <= 60: return "31_TO_60_DAYS"
        if days_overdue <= 90: return "61_TO_90_DAYS"
        return "OVER_90_DAYS"
