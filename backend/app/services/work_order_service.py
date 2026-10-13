'''Shop Floor Manufacturing Work Order Tracker.'''
class WorkOrderService:
    @staticmethod
    def estimate_cycle_time(units: int, seconds_per_unit: int) -> float:
        total_seconds = units * seconds_per_unit
        return round(total_seconds / 3600.0, 2)
