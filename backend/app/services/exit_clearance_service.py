'''Employee Full & Final (FnF) Settlement Calculator.'''
class ExitClearanceService:
    @staticmethod
    def calculate_fnf(payable_salary: float, leave_encashment: float, gratuity: float, deductions: float) -> float:
        gross_payable = payable_salary + leave_encashment + gratuity
        return round(gross_payable - deductions, 2)
