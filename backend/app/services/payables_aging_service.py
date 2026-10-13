'''Accounts Payable (AP) Maturity and Prompt Payment Discount Engine.'''
class PayablesAgingService:
    @staticmethod
    def check_cash_discount_eligibility(days_since_invoice: int, discount_window_days: int = 10, discount_pct: float = 2.0) -> float:
        return discount_pct if days_since_invoice <= discount_window_days else 0.0
