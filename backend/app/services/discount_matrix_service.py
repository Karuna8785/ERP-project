'''Tiered Volume & Customer Group Discount Matrix.'''
class DiscountMatrixService:
    @staticmethod
    def apply_discount(base_price: float, quantity: int, customer_tier: str = "RETAIL") -> float:
        disc = 0.0
        if quantity >= 100: disc = 0.15
        elif quantity >= 20: disc = 0.08
        if customer_tier == "WHOLESALE": disc += 0.05
        return round(base_price * (1.0 - min(0.35, disc)), 2)
