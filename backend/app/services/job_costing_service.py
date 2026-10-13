'''Project & Work Breakdown Structure (WBS) Job Costing.'''
class JobCostingService:
    @staticmethod
    def calculate_margin(material_cost: float, labor_hours: float, hourly_rate: float, billed_revenue: float) -> dict:
        total_labor = labor_hours * hourly_rate
        cogs = material_cost + total_labor
        gross_profit = billed_revenue - cogs
        margin_pct = (gross_profit / billed_revenue) * 100 if billed_revenue > 0 else 0
        return {"cogs": cogs, "gross_profit": gross_profit, "margin_percent": round(margin_pct, 2)}
