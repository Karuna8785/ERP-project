'''Sliding Window API Rate Limiter.'''
import time

class SlidingRateLimiter:
    @staticmethod
    def is_allowed(timestamps: list, max_requests: int = 60, window_seconds: int = 60) -> tuple:
        now = time.time()
        valid = [t for t in timestamps if now - t < window_seconds]
        if len(valid) < max_requests:
            valid.append(now)
            return True, valid
        return False, valid
