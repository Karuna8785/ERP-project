'''Harmonized Tariff (HS) Duty & Customs Valuation.'''
class CustomsTariffService:
    @staticmethod
    def calculate_landed_cost(fob_price: float, freight: float, insurance: float, duty_pct: float) -> dict:
        cif_value = fob_price + freight + insurance
        customs_duty = cif_value * (duty_pct / 100.0)
        landed_cost = cif_value + customs_duty
        return {"cif_value": round(cif_value, 2), "customs_duty": round(customs_duty, 2), "landed_cost": round(landed_cost, 2)}
