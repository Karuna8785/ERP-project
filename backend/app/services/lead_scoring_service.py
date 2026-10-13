'''Predictive Lead Scoring & Priority Queue.'''
class LeadScoringService:
    @staticmethod
    def calculate_score(employee_count: int, budget: float, has_verified_email: bool, decision_maker: bool) -> int:
        score = 0
        if employee_count > 500: score += 30
        elif employee_count > 50: score += 20
        else: score += 10
        if budget >= 500000: score += 40
        elif budget >= 100000: score += 25
        if has_verified_email: score += 15
        if decision_maker: score += 15
        return min(100, score)
