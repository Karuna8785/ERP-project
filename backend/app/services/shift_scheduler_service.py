'''Shift Roster Scheduling & Allowance Dispatcher.'''
class ShiftSchedulerService:
    @staticmethod
    def calculate_night_allowance(night_shifts_worked: int, rate_per_shift: float = 350.0) -> float:
        return round(night_shifts_worked * rate_per_shift, 2)
