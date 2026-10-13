'''Multi-Currency Exchange Rate Conversion Engine for SmartERP Enterprise.'''
from typing import Dict, Any, Optional
from datetime import datetime, timezone

class MultiCurrencyService:
    BASE_CURRENCY = "INR"

    DEFAULT_RATES = {
        "INR": 1.0,
        "USD": 86.45,
        "EUR": 93.20,
        "GBP": 110.15,
        "AED": 23.54,
        "SGD": 64.80,
        "JPY": 0.58,
    }

    @classmethod
    def convert(cls, amount: float, from_curr: str, to_curr: str, custom_rates: Optional[Dict[str, float]] = None) -> float:
        rates = custom_rates or cls.DEFAULT_RATES
        from_rate = rates.get(from_curr.upper(), 1.0)
        to_rate = rates.get(to_curr.upper(), 1.0)
        amount_in_inr = amount * from_rate
        return round(amount_in_inr / to_rate, 4)

    @classmethod
    def get_supported_currencies(cls) -> list:
        return list(cls.DEFAULT_RATES.keys())
