'''Two-Factor Authentication (2FA) TOTP Engine.'''
import secrets

class TOTPSecurityService:
    @staticmethod
    def generate_backup_codes(count: int = 8) -> list:
        return [secrets.token_hex(4).upper() for _ in range(count)]
