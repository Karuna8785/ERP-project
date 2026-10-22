"""
Enterprise CRM & Account Management - Statistical Computation and Business Intelligence Engine
"""
import math
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime, timedelta

class CrmEnterpriseAnalyticsEngine:
    """Algorithmic calculation engine providing statistical forecasting and anomaly detection."""

    def __init__(self, organization_id: int = 1):
        self.organization_id = organization_id
        self.benchmark_rate = 0.085
        self.alpha_smoothing = 0.35

    # --- LeadAccount Analytical Algorithms ---
    @staticmethod
    def compute_leadaccount_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "LeadAccount",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_leadaccount_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_leadaccount_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_leadaccount_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_leadaccount_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- ContactPerson Analytical Algorithms ---
    @staticmethod
    def compute_contactperson_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ContactPerson",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_contactperson_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_contactperson_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_contactperson_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_contactperson_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- OpportunityDeal Analytical Algorithms ---
    @staticmethod
    def compute_opportunitydeal_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "OpportunityDeal",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_opportunitydeal_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_opportunitydeal_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_opportunitydeal_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_opportunitydeal_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- SalesPipelineStage Analytical Algorithms ---
    @staticmethod
    def compute_salespipelinestage_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "SalesPipelineStage",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_salespipelinestage_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_salespipelinestage_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_salespipelinestage_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_salespipelinestage_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- QuoteProposal Analytical Algorithms ---
    @staticmethod
    def compute_quoteproposal_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "QuoteProposal",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_quoteproposal_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_quoteproposal_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_quoteproposal_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_quoteproposal_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- TerritoryRegion Analytical Algorithms ---
    @staticmethod
    def compute_territoryregion_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "TerritoryRegion",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_territoryregion_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_territoryregion_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_territoryregion_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_territoryregion_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- SalesQuotaTarget Analytical Algorithms ---
    @staticmethod
    def compute_salesquotatarget_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "SalesQuotaTarget",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_salesquotatarget_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_salesquotatarget_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_salesquotatarget_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_salesquotatarget_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- CompetitorAnalysis Analytical Algorithms ---
    @staticmethod
    def compute_competitoranalysis_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CompetitorAnalysis",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_competitoranalysis_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_competitoranalysis_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_competitoranalysis_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_competitoranalysis_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- CustomerTouchpoint Analytical Algorithms ---
    @staticmethod
    def compute_customertouchpoint_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CustomerTouchpoint",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_customertouchpoint_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_customertouchpoint_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_customertouchpoint_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_customertouchpoint_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- CampaignTracking Analytical Algorithms ---
    @staticmethod
    def compute_campaigntracking_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CampaignTracking",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_campaigntracking_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_campaigntracking_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_campaigntracking_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_campaigntracking_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- LeadScoreMetric Analytical Algorithms ---
    @staticmethod
    def compute_leadscoremetric_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "LeadScoreMetric",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_leadscoremetric_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_leadscoremetric_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_leadscoremetric_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_leadscoremetric_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- DealCommission Analytical Algorithms ---
    @staticmethod
    def compute_dealcommission_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "DealCommission",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_dealcommission_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_dealcommission_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_dealcommission_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_dealcommission_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- CustomerChurnRisk Analytical Algorithms ---
    @staticmethod
    def compute_customerchurnrisk_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CustomerChurnRisk",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_customerchurnrisk_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_customerchurnrisk_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_customerchurnrisk_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_customerchurnrisk_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- MeetingTranscript Analytical Algorithms ---
    @staticmethod
    def compute_meetingtranscript_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "MeetingTranscript",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_meetingtranscript_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_meetingtranscript_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_meetingtranscript_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_meetingtranscript_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- ReferralSource Analytical Algorithms ---
    @staticmethod
    def compute_referralsource_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ReferralSource",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_referralsource_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_referralsource_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_referralsource_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_referralsource_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

    # --- PartnerChannel Analytical Algorithms ---
    @staticmethod
    def compute_partnerchannel_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PartnerChannel",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_partnerchannel_moving_average(series: List[float], window_size: int = 3) -> List[float]:
        """Compute simple moving average over temporal series data."""
        if not series or window_size <= 0:
            return []
        result = []
        for i in range(len(series)):
            start = max(0, i - window_size + 1)
            sub = series[start:i + 1]
            result.append(round(sum(sub) / len(sub), 3))
        return result

    @staticmethod
    def compute_partnerchannel_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
        """Calculate Single Exponential Smoothing forecast for trend projection."""
        if not series:
            return []
        smoothed = [series[0]]
        for val in series[1:]:
            prev = smoothed[-1]
            s = alpha * val + (1.0 - alpha) * prev
            smoothed.append(round(s, 3))
        return smoothed

    @staticmethod
    def detect_partnerchannel_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Detect outliers and anomalies using Gaussian Z-Score statistical distribution."""
        if len(series) < 3:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        anomalies = []
        for idx, val in enumerate(series):
            z = (val - mean) / std_dev
            if abs(z) >= z_score_threshold:
                anomalies.append({
                    "index": idx,
                    "value": round(val, 2),
                    "z_score": round(z, 2),
                    "is_high_outlier": z > 0,
                })
        return anomalies

    @staticmethod
    def compute_partnerchannel_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
        """Forecast compound multi-period financial trajectory with confidence intervals."""
        projection = []
        current = initial_amount
        for p in range(1, periods + 1):
            current = current * (1.0 + growth_rate)
            projection.append({
                "period": p,
                "projected_amount": round(current, 2),
                "upper_bound_95": round(current * 1.08, 2),
                "lower_bound_95": round(current * 0.92, 2),
            })
        return projection

