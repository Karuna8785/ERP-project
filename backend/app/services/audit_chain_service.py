'''Cryptographic Hash-Chained Audit Trail for Financial Records.'''
import hashlib
import json

class AuditChainService:
    @staticmethod
    def compute_hash(prev_hash: str, payload: dict) -> str:
        serialized = json.dumps(payload, sort_keys=True)
        raw = f"{prev_hash}:{serialized}"
        return hashlib.sha256(raw.encode('utf-8')).hexdigest()
