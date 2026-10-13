'''Statutory Payroll TDS & Professional Tax Engine.'''
class IndianPayrollTaxEngine:
    @staticmethod
    def calculate_new_tax_regime(annual_gross: float) -> dict:
        taxable = max(0.0, annual_gross - 75000.0) # standard deduction
        tax = 0.0
        if taxable <= 400000:
            tax = 0.0
        elif taxable <= 800000:
            tax = (taxable - 400000) * 0.05
        elif taxable <= 1200000:
            tax = 20000 + (taxable - 800000) * 0.10
        elif taxable <= 1600000:
            tax = 60000 + (taxable - 1200000) * 0.15
        elif taxable <= 2000000:
            tax = 120000 + (taxable - 1600000) * 0.20
        elif taxable <= 2400000:
            tax = 200000 + (taxable - 2000000) * 0.25
        else:
            tax = 300000 + (taxable - 2400000) * 0.30
        
        cess = tax * 0.04
        return {
            "taxable_income": taxable,
            "income_tax": round(tax, 2),
            "health_education_cess": round(cess, 2),
            "total_annual_tax": round(tax + cess, 2),
            "monthly_tds_deduction": round((tax + cess) / 12, 2)
        }
