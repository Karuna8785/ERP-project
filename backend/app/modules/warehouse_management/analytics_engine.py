"""
Advanced Warehouse Management (WMS) - Statistical Computation and Business Intelligence Engine
"""
import math
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime, timedelta

class WarehouseManagementAnalyticsEngine:
    """Algorithmic calculation engine providing statistical forecasting and anomaly detection."""

    def __init__(self, organization_id: int = 1):
        self.organization_id = organization_id
        self.benchmark_rate = 0.085
        self.alpha_smoothing = 0.35

    # --- WarehouseZone Analytical Algorithms ---
    @staticmethod
    def compute_warehousezone_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "WarehouseZone",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_warehousezone_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_warehousezone_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_warehousezone_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_warehousezone_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- StorageAisle Analytical Algorithms ---
    @staticmethod
    def compute_storageaisle_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "StorageAisle",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_storageaisle_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_storageaisle_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_storageaisle_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_storageaisle_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- RackBinLocation Analytical Algorithms ---
    @staticmethod
    def compute_rackbinlocation_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "RackBinLocation",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_rackbinlocation_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_rackbinlocation_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_rackbinlocation_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_rackbinlocation_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- StockPallet Analytical Algorithms ---
    @staticmethod
    def compute_stockpallet_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "StockPallet",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_stockpallet_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_stockpallet_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_stockpallet_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_stockpallet_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- WavePickingPlan Analytical Algorithms ---
    @staticmethod
    def compute_wavepickingplan_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "WavePickingPlan",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_wavepickingplan_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_wavepickingplan_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_wavepickingplan_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_wavepickingplan_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PutawayTask Analytical Algorithms ---
    @staticmethod
    def compute_putawaytask_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PutawayTask",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_putawaytask_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_putawaytask_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_putawaytask_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_putawaytask_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- CycleCountSheet Analytical Algorithms ---
    @staticmethod
    def compute_cyclecountsheet_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CycleCountSheet",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_cyclecountsheet_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_cyclecountsheet_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_cyclecountsheet_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_cyclecountsheet_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- BinTransferOrder Analytical Algorithms ---
    @staticmethod
    def compute_bintransferorder_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "BinTransferOrder",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_bintransferorder_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_bintransferorder_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_bintransferorder_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_bintransferorder_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- CrossDockRoute Analytical Algorithms ---
    @staticmethod
    def compute_crossdockroute_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "CrossDockRoute",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_crossdockroute_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_crossdockroute_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_crossdockroute_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_crossdockroute_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- LPNTag Analytical Algorithms ---
    @staticmethod
    def compute_lpntag_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "LPNTag",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_lpntag_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_lpntag_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_lpntag_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_lpntag_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- PackagingStation Analytical Algorithms ---
    @staticmethod
    def compute_packagingstation_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "PackagingStation",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_packagingstation_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_packagingstation_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_packagingstation_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_packagingstation_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- DockDoorAssignment Analytical Algorithms ---
    @staticmethod
    def compute_dockdoorassignment_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "DockDoorAssignment",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_dockdoorassignment_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_dockdoorassignment_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_dockdoorassignment_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_dockdoorassignment_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- KittingOrder Analytical Algorithms ---
    @staticmethod
    def compute_kittingorder_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "KittingOrder",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_kittingorder_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_kittingorder_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_kittingorder_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_kittingorder_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- DeKittingJob Analytical Algorithms ---
    @staticmethod
    def compute_dekittingjob_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "DeKittingJob",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_dekittingjob_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_dekittingjob_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_dekittingjob_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_dekittingjob_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- HazardClassification Analytical Algorithms ---
    @staticmethod
    def compute_hazardclassification_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "HazardClassification",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_hazardclassification_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_hazardclassification_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_hazardclassification_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_hazardclassification_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

    # --- TempLogRecord Analytical Algorithms ---
    @staticmethod
    def compute_templogrecord_variance(baseline: float, actual: float) -> Dict[str, Any]:
        """Calculate absolute and percentage budget variance with favorable/unfavorable indicators."""
        variance = actual - baseline
        pct = (variance / baseline * 100.0) if baseline > 0 else 0.0
        return {
            "entity": "TempLogRecord",
            "baseline_value": round(baseline, 2),
            "actual_value": round(actual, 2),
            "variance_absolute": round(variance, 2),
            "variance_percentage": round(pct, 2),
            "is_favorable": variance >= 0,
            "threshold_status": "NORMAL" if abs(pct) < 15.0 else ("WARNING" if abs(pct) < 30.0 else "CRITICAL"),
        }

    @staticmethod
    def calculate_templogrecord_moving_average(series: List[float], window_size: int = 3) -> List[float]:
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
    def compute_templogrecord_exponential_smoothing(series: List[float], alpha: float = 0.3) -> List[float]:
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
    def detect_templogrecord_statistical_anomalies(series: List[float], z_score_threshold: float = 2.0) -> List[Dict[str, Any]]:
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
    def compute_templogrecord_growth_projection(initial_amount: float, periods: int = 12, growth_rate: float = 0.05) -> List[Dict[str, Any]]:
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

