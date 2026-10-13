'''Customer Loyalty Program & Tier Accrual Rules.'''
class LoyaltyPointsService:
    @staticmethod
    def calculate_earned_points(spend_amount: float, tier: str = "SILVER") -> int:
        multiplier = 2 if tier == "GOLD" else (3 if tier == "PLATINUM" else 1)
        return int((spend_amount / 100.0) * multiplier)
