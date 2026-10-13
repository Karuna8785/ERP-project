'''Dynamic Safety Stock & Wilson EOQ Calculator.'''
import math

class SafetyStockService:
    @staticmethod
    def calculate_eoq(annual_demand: float, order_cost: float, holding_cost_per_unit: float) -> float:
        if holding_cost_per_unit <= 0: return 0.0
        return round(math.sqrt((2 * annual_demand * order_cost) / holding_cost_per_unit), 2)
