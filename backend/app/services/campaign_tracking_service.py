'''CRM Marketing Campaign Tracker.'''
class CampaignTrackingService:
    @staticmethod
    def track_event(campaign_id: int, recipient_email: str, event_type: str) -> dict:
        return {"campaign_id": campaign_id, "email": recipient_email, "event": event_type, "status": "LOGGED"}
