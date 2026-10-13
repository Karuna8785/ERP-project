'''Vendor RFQ Evaluation and Normalized Scoring Matrix.'''
class RFQScoringService:
    @staticmethod
    def evaluate_bid(price: float, min_price: float, delivery_days: int, min_delivery_days: int, quality_score: float) -> float:
        price_score = (min_price / price) * 50.0 if price > 0 else 0
        speed_score = (min_delivery_days / delivery_days) * 30.0 if delivery_days > 0 else 0
        qa_score = (quality_score / 100.0) * 20.0
        return round(price_score + speed_score + qa_score, 2)
