'''Biometric Device Time-Card Log Normalizer.'''
from datetime import datetime

class BiometricSyncService:
    @staticmethod
    def parse_punch_record(device_id: str, badge_num: str, timestamp_str: str, punch_type: int) -> dict:
        dt = datetime.fromisoformat(timestamp_str)
        return {
            "device_id": device_id,
            "badge_number": badge_num,
            "timestamp": dt.isoformat(),
            "punch_type": "CHECK_IN" if punch_type == 0 else "CHECK_OUT"
        }
