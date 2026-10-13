'''Customer Credit Limit and Exposure Enforcement.'''
class CreditLimitService:
    @staticmethod
    def check_exposure(credit_limit: float, current_outstanding: float, new_order_total: float) -> dict:
        total_exposure = current_outstanding + new_order_total
        exceeded = total_exposure > credit_limit
        return {
            "credit_limit": credit_limit,
            "current_outstanding": current_outstanding,
            "new_order_total": new_order_total,
            "total_exposure": total_exposure,
            "is_exceeded": exceeded,
            "shortfall": max(0.0, total_exposure - credit_limit)
        }
