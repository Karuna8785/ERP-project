'''Recurring SaaS & Retainer Invoice Scheduler.'''
from datetime import date, timedelta

class RecurringInvoiceService:
    @staticmethod
    def get_next_billing_date(current_date: date, frequency: str) -> date:
        if frequency == "MONTHLY":
            return current_date + timedelta(days=30)
        elif frequency == "QUARTERLY":
            return current_date + timedelta(days=91)
        return current_date + timedelta(days=365)
