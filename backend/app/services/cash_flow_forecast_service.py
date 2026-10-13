'''90-Day Predictive Cash Flow & Liquidity Forecaster.'''
class CashFlowForecastService:
    @staticmethod
    def project_balance(current_cash: float, expected_inflows: list, scheduled_outflows: list) -> float:
        return round(current_cash + sum(expected_inflows) - sum(scheduled_outflows), 2)
