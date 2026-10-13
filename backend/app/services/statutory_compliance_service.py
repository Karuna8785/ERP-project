'''Indian Statutory PF & ESIC Contribution Returns.'''
class StatutoryComplianceService:
    @staticmethod
    def calculate_pf_and_esi(basic_wage: float, gross_wage: float) -> dict:
        capped_basic = min(15000.0, basic_wage)
        emp_pf = round(capped_basic * 0.12, 2)
        empr_pf = round(capped_basic * 0.12, 2)
        emp_esi = round(gross_wage * 0.0075, 2) if gross_wage <= 21000 else 0.0
        empr_esi = round(gross_wage * 0.0325, 2) if gross_wage <= 21000 else 0.0
        return {"employee_pf": emp_pf, "employer_pf": empr_pf, "employee_esi": emp_esi, "employer_esi": empr_esi}
