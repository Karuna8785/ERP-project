"""
Partner Relationship Management (PRM) - Statistical Computation and Business Intelligence Engine
"""
import math
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime, timedelta

class PartnerNetworkAnalyticsEngine:
    """Algorithmic calculation engine providing statistical forecasting and anomaly detection."""

    def __init__(self, organization_id: int = 1):
        self.organization_id = organization_id
        self.benchmark_rate = 0.085
        self.alpha_smoothing = 0.35

    # --- ChannelPartnerProfile Analytical Algorithms ---
    @staticmethod
    def compute_channelpartnerprofile_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ChannelPartnerProfile",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_channelpartnerprofile_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_channelpartnerprofile_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_channelpartnerprofile_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_channelpartnerprofile_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PartnerTierLevel Analytical Algorithms ---
    @staticmethod
    def compute_partnertierlevel_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PartnerTierLevel",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_partnertierlevel_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_partnertierlevel_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_partnertierlevel_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_partnertierlevel_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- DealRegistrationLead Analytical Algorithms ---
    @staticmethod
    def compute_dealregistrationlead_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "DealRegistrationLead",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_dealregistrationlead_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_dealregistrationlead_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_dealregistrationlead_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_dealregistrationlead_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- MDFMarketFundRequest Analytical Algorithms ---
    @staticmethod
    def compute_mdfmarketfundrequest_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "MDFMarketFundRequest",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_mdfmarketfundrequest_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_mdfmarketfundrequest_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_mdfmarketfundrequest_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_mdfmarketfundrequest_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- CoMarketingCampaign Analytical Algorithms ---
    @staticmethod
    def compute_comarketingcampaign_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CoMarketingCampaign",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_comarketingcampaign_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_comarketingcampaign_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_comarketingcampaign_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_comarketingcampaign_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PartnerCommissionPayout Analytical Algorithms ---
    @staticmethod
    def compute_partnercommissionpayout_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PartnerCommissionPayout",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_partnercommissionpayout_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_partnercommissionpayout_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_partnercommissionpayout_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_partnercommissionpayout_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- CertificationCredential Analytical Algorithms ---
    @staticmethod
    def compute_certificationcredential_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CertificationCredential",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_certificationcredential_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_certificationcredential_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_certificationcredential_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_certificationcredential_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PartnerSalesGoal Analytical Algorithms ---
    @staticmethod
    def compute_partnersalesgoal_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PartnerSalesGoal",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_partnersalesgoal_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_partnersalesgoal_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_partnersalesgoal_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_partnersalesgoal_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ResellerAgreementContract Analytical Algorithms ---
    @staticmethod
    def compute_reselleragreementcontract_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ResellerAgreementContract",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_reselleragreementcontract_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_reselleragreementcontract_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_reselleragreementcontract_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_reselleragreementcontract_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- LeadDistributionRule Analytical Algorithms ---
    @staticmethod
    def compute_leaddistributionrule_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "LeadDistributionRule",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_leaddistributionrule_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_leaddistributionrule_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_leaddistributionrule_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_leaddistributionrule_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PartnerPortalCredential Analytical Algorithms ---
    @staticmethod
    def compute_partnerportalcredential_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PartnerPortalCredential",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_partnerportalcredential_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_partnerportalcredential_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_partnerportalcredential_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_partnerportalcredential_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ChannelConflictDispute Analytical Algorithms ---
    @staticmethod
    def compute_channelconflictdispute_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ChannelConflictDispute",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_channelconflictdispute_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_channelconflictdispute_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_channelconflictdispute_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_channelconflictdispute_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- TerritoryPartnerExclusivity Analytical Algorithms ---
    @staticmethod
    def compute_territorypartnerexclusivity_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "TerritoryPartnerExclusivity",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_territorypartnerexclusivity_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_territorypartnerexclusivity_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_territorypartnerexclusivity_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_territorypartnerexclusivity_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PartnerTrainingProgress Analytical Algorithms ---
    @staticmethod
    def compute_partnertrainingprogress_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PartnerTrainingProgress",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_partnertrainingprogress_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_partnertrainingprogress_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_partnertrainingprogress_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_partnertrainingprogress_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- JointSolutionListing Analytical Algorithms ---
    @staticmethod
    def compute_jointsolutionlisting_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "JointSolutionListing",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_jointsolutionlisting_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_jointsolutionlisting_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_jointsolutionlisting_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_jointsolutionlisting_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ChannelRevenueForecast Analytical Algorithms ---
    @staticmethod
    def compute_channelrevenueforecast_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ChannelRevenueForecast",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_channelrevenueforecast_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_channelrevenueforecast_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_channelrevenueforecast_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_channelrevenueforecast_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

