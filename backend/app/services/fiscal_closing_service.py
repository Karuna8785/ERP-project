'''Fiscal Year End Ledger Closing & Retained Earnings Rollover.'''
class FiscalClosingService:
    @staticmethod
    def calculate_retained_earnings(total_income: float, total_expense: float, dividends: float = 0.0) -> float:
        net_income = total_income - total_expense
        return round(net_income - dividends, 2)
