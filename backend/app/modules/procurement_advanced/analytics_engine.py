"""
Strategic Procurement & Sourcing - Statistical Computation and Business Intelligence Engine
"""
import math
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime, timedelta

class ProcurementAdvancedAnalyticsEngine:
    """Algorithmic calculation engine providing statistical forecasting and anomaly detection."""

    def __init__(self, organization_id: int = 1):
        self.organization_id = organization_id
        self.benchmark_rate = 0.085
        self.alpha_smoothing = 0.35

    # --- SourcingRequest Analytical Algorithms ---
    @staticmethod
    def compute_sourcingrequest_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "SourcingRequest",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_sourcingrequest_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_sourcingrequest_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_sourcingrequest_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_sourcingrequest_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- VendorQuote Analytical Algorithms ---
    @staticmethod
    def compute_vendorquote_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "VendorQuote",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_vendorquote_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_vendorquote_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_vendorquote_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_vendorquote_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- BidComparison Analytical Algorithms ---
    @staticmethod
    def compute_bidcomparison_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "BidComparison",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_bidcomparison_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_bidcomparison_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_bidcomparison_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_bidcomparison_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ContractAgreement Analytical Algorithms ---
    @staticmethod
    def compute_contractagreement_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ContractAgreement",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_contractagreement_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_contractagreement_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_contractagreement_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_contractagreement_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PurchaseRequisition Analytical Algorithms ---
    @staticmethod
    def compute_purchaserequisition_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PurchaseRequisition",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_purchaserequisition_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_purchaserequisition_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_purchaserequisition_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_purchaserequisition_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- BlanketPO Analytical Algorithms ---
    @staticmethod
    def compute_blanketpo_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "BlanketPO",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_blanketpo_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_blanketpo_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_blanketpo_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_blanketpo_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- VendorScorecard Analytical Algorithms ---
    @staticmethod
    def compute_vendorscorecard_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "VendorScorecard",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_vendorscorecard_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_vendorscorecard_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_vendorscorecard_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_vendorscorecard_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- SpendCategory Analytical Algorithms ---
    @staticmethod
    def compute_spendcategory_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "SpendCategory",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_spendcategory_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_spendcategory_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_spendcategory_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_spendcategory_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ProcurementPolicy Analytical Algorithms ---
    @staticmethod
    def compute_procurementpolicy_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ProcurementPolicy",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_procurementpolicy_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_procurementpolicy_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_procurementpolicy_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_procurementpolicy_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- CatalogItem Analytical Algorithms ---
    @staticmethod
    def compute_catalogitem_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CatalogItem",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_catalogitem_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_catalogitem_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_catalogitem_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_catalogitem_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- SupplierTier Analytical Algorithms ---
    @staticmethod
    def compute_suppliertier_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "SupplierTier",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_suppliertier_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_suppliertier_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_suppliertier_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_suppliertier_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- RebateProgram Analytical Algorithms ---
    @staticmethod
    def compute_rebateprogram_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "RebateProgram",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_rebateprogram_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_rebateprogram_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_rebateprogram_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_rebateprogram_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- FreightRateAgreement Analytical Algorithms ---
    @staticmethod
    def compute_freightrateagreement_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "FreightRateAgreement",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_freightrateagreement_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_freightrateagreement_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_freightrateagreement_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_freightrateagreement_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ImportPermit Analytical Algorithms ---
    @staticmethod
    def compute_importpermit_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ImportPermit",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_importpermit_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_importpermit_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_importpermit_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_importpermit_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PurchaseReturn Analytical Algorithms ---
    @staticmethod
    def compute_purchasereturn_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PurchaseReturn",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_purchasereturn_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_purchasereturn_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_purchasereturn_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_purchasereturn_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PaymentSchedule Analytical Algorithms ---
    @staticmethod
    def compute_paymentschedule_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PaymentSchedule",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_paymentschedule_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_paymentschedule_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_paymentschedule_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_paymentschedule_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

