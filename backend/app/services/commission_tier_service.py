'''Sales Commission Tier Engine.'''
class CommissionTierService:
    TIERS = [
        (1000000, 0.08),
        (500000, 0.05),
        (200000, 0.03),
        (0, 0.01)
    ]
    @classmethod
    def calculate_commission(cls, booked_revenue: float) -> float:
        for threshold, rate in cls.TIERS:
            if booked_revenue >= threshold:
                return round(booked_revenue * rate, 2)
        return 0.0
