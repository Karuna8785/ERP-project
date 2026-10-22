"""
Omnichannel Notification & Alert Dispatcher - Governance Approval Workflows & State Machine Transitions
"""
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from .models import RecordStatus, PriorityLevel

class NotificationEngineWorkflowEngine:
    """Multi-tiered approval state machine with governance transition rules."""

    VALID_TRANSITIONS = {
        RecordStatus.DRAFT: [RecordStatus.PENDING_APPROVAL, RecordStatus.CANCELLED],
        RecordStatus.PENDING_APPROVAL: [RecordStatus.APPROVED, RecordStatus.REJECTED, RecordStatus.DRAFT],
        RecordStatus.APPROVED: [RecordStatus.ACTIVE, RecordStatus.IN_PROGRESS, RecordStatus.ON_HOLD],
        RecordStatus.ACTIVE: [RecordStatus.IN_PROGRESS, RecordStatus.ON_HOLD, RecordStatus.COMPLETED, RecordStatus.CANCELLED],
        RecordStatus.IN_PROGRESS: [RecordStatus.COMPLETED, RecordStatus.ON_HOLD, RecordStatus.CANCELLED],
        RecordStatus.ON_HOLD: [RecordStatus.IN_PROGRESS, RecordStatus.CANCELLED, RecordStatus.ACTIVE],
        RecordStatus.COMPLETED: [RecordStatus.ARCHIVED],
        RecordStatus.REJECTED: [RecordStatus.DRAFT, RecordStatus.ARCHIVED],
        RecordStatus.CANCELLED: [RecordStatus.ARCHIVED],
        RecordStatus.ARCHIVED: [],
    }

    @classmethod
    def can_transition(cls, current_status: RecordStatus, target_status: RecordStatus) -> bool:
        """Check if target state transition is legally permissible."""
        allowed = cls.VALID_TRANSITIONS.get(current_status, [])
        return target_status in allowed

    @classmethod
    def evaluate_approval_level_required(cls, amount: float, priority: PriorityLevel) -> int:
        """Determine multi-tier executive approval threshold based on risk value."""
        if amount > 1000000.0 or priority == PriorityLevel.EMERGENCY:
            return 3  # Board / Executive level
        elif amount > 100000.0 or priority == PriorityLevel.CRITICAL:
            return 2  # Department Director level
        elif amount > 25000.0 or priority == PriorityLevel.HIGH:
            return 1  # Unit Supervisor level
        return 0  # Auto-approved routine operations

    @classmethod
    def execute_notificationtemplate_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for NotificationTemplate record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_dispatchmessagequeue_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for DispatchMessageQueue record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_deliveryattemptlog_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for DeliveryAttemptLog record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_userchannelpreference_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for UserChannelPreference record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_emailtransportconfig_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for EmailTransportConfig record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_smsgatewayprovider_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for SMSGatewayProvider record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_pushnotificationtoken_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PushNotificationToken record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_inappnotificationfeed_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for InAppNotificationFeed record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_webhookdispatchtarget_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for WebhookDispatchTarget record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_notificationcategorygroup_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for NotificationCategoryGroup record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_ratelimitthrottlerule_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for RateLimitThrottleRule record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_optoutsubscriptionlist_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for OptOutSubscriptionList record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_templatelocalizationitem_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for TemplateLocalizationItem record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_digestaggregationschedule_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for DigestAggregationSchedule record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_bouncefailurereport_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for BounceFailureReport record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_engagementclicktracker_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for EngagementClickTracker record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

