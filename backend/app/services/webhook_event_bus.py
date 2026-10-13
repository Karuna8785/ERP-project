'''Outbound Webhook Dispatcher with Cryptographic HMAC Signatures.'''
import hmac
import hashlib
import json

class WebhookEventBus:
    @staticmethod
    def sign_payload(secret_key: str, payload: dict) -> str:
        body = json.dumps(payload, sort_keys=True).encode('utf-8')
        return hmac.new(secret_key.encode('utf-8'), body, hashlib.sha256).hexdigest()
