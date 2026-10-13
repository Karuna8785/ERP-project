'''Statutory Leave Encashment and Carry Forward Engine.'''
class LeaveEncashmentService:
    @staticmethod
    def calculate_encashment(earned_leaves: float, basic_monthly_salary: float, daily_div: int = 30) -> float:
        per_day_wage = basic_monthly_salary / daily_div
        return round(earned_leaves * per_day_wage, 2)
