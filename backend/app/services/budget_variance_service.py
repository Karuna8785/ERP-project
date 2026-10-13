'''Cost Center Budget vs Actual Expenditure Variance Analytics.'''
class BudgetVarianceService:
    @staticmethod
    def compute_variance(budgeted: float, actual: float) -> dict:
        var = budgeted - actual
        pct = (var / budgeted) * 100 if budgeted > 0 else 0
        return {"variance": round(var, 2), "variance_percentage": round(pct, 2), "status": "FAVORABLE" if var >= 0 else "ADVERSE"}
