"""
Manufacturing Resource Planning (MRP II) - Statistical Computation and Business Intelligence Engine
"""
import math
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime, timedelta

class ManufacturingAnalyticsEngine:
    """Algorithmic calculation engine providing statistical forecasting and anomaly detection."""

    def __init__(self, organization_id: int = 1):
        self.organization_id = organization_id
        self.benchmark_rate = 0.085
        self.alpha_smoothing = 0.35

    # --- WorkOrder Analytical Algorithms ---
    @staticmethod
    def compute_workorder_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "WorkOrder",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_workorder_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_workorder_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_workorder_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_workorder_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- BillOfMaterial Analytical Algorithms ---
    @staticmethod
    def compute_billofmaterial_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "BillOfMaterial",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_billofmaterial_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_billofmaterial_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_billofmaterial_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_billofmaterial_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- Operation Analytical Algorithms ---
    @staticmethod
    def compute_operation_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "Operation",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_operation_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_operation_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_operation_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_operation_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- WorkCenter Analytical Algorithms ---
    @staticmethod
    def compute_workcenter_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "WorkCenter",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_workcenter_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_workcenter_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_workcenter_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_workcenter_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- Routing Analytical Algorithms ---
    @staticmethod
    def compute_routing_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "Routing",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_routing_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_routing_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_routing_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_routing_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ProductionSchedule Analytical Algorithms ---
    @staticmethod
    def compute_productionschedule_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ProductionSchedule",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_productionschedule_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_productionschedule_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_productionschedule_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_productionschedule_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ScrapRecord Analytical Algorithms ---
    @staticmethod
    def compute_scraprecord_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ScrapRecord",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_scraprecord_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_scraprecord_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_scraprecord_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_scraprecord_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- QualityCheck Analytical Algorithms ---
    @staticmethod
    def compute_qualitycheck_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "QualityCheck",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_qualitycheck_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_qualitycheck_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_qualitycheck_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_qualitycheck_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- MachineDowntime Analytical Algorithms ---
    @staticmethod
    def compute_machinedowntime_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "MachineDowntime",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_machinedowntime_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_machinedowntime_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_machinedowntime_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_machinedowntime_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ToolingAsset Analytical Algorithms ---
    @staticmethod
    def compute_toolingasset_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ToolingAsset",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_toolingasset_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_toolingasset_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_toolingasset_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_toolingasset_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- MaterialRequisition Analytical Algorithms ---
    @staticmethod
    def compute_materialrequisition_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "MaterialRequisition",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_materialrequisition_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_materialrequisition_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_materialrequisition_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_materialrequisition_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ECO Analytical Algorithms ---
    @staticmethod
    def compute_eco_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ECO",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_eco_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_eco_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_eco_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_eco_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- StandardCost Analytical Algorithms ---
    @staticmethod
    def compute_standardcost_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "StandardCost",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_standardcost_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_standardcost_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_standardcost_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_standardcost_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- AssemblyLine Analytical Algorithms ---
    @staticmethod
    def compute_assemblyline_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "AssemblyLine",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_assemblyline_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_assemblyline_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_assemblyline_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_assemblyline_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- ShiftOutput Analytical Algorithms ---
    @staticmethod
    def compute_shiftoutput_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "ShiftOutput",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_shiftoutput_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_shiftoutput_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_shiftoutput_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_shiftoutput_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- WIPStock Analytical Algorithms ---
    @staticmethod
    def compute_wipstock_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "WIPStock",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_wipstock_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_wipstock_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_wipstock_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_wipstock_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

