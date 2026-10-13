'''Supplier SLA and Scorecard Aggregator.'''
class VendorKPIService:
    @staticmethod
    def compute_scorecard(total_deliveries: int, on_time: int, total_units: int, rejected_units: int) -> dict:
        otd_rate = (on_time / total_deliveries) * 100.0 if total_deliveries > 0 else 100.0
        defect_ppm = (rejected_units / total_units) * 1_000_000 if total_units > 0 else 0
        return {"on_time_delivery_rate": round(otd_rate, 2), "defect_ppm": round(defect_ppm, 0)}
