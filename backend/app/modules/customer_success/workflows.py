"""
Customer Success & Retention Engineering - Governance Approval Workflows & State Machine Transitions
"""
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from .models import RecordStatus, PriorityLevel

class CustomerSuccessWorkflowEngine:
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
    def execute_customerhealthscore_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CustomerHealthScore record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_onboardingmilestoneplan_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for OnboardingMilestonePlan record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_quarterlybusinessreview_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for QuarterlyBusinessReview record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_npsfeedbacksurvey_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for NPSFeedbackSurvey record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_churnearlywarningsignal_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ChurnEarlyWarningSignal record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_accountexpansiondeal_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for AccountExpansionDeal record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_productadoptionmetric_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ProductAdoptionMetric record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_customerjourneytouchpoint_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CustomerJourneyTouchpoint record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_supportescalationflag_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for SupportEscalationFlag record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_successplanobjective_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for SuccessPlanObjective record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_clientreferenceadvocate_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ClientReferenceAdvocate record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_renewalforecastpipeline_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for RenewalForecastPipeline record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_productusageanalytics_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ProductUsageAnalytics record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_customerengagementscore_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CustomerEngagementScore record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_voiceofcustomerfeedback_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for VoiceOfCustomerFeedback record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_successexecutiveassignment_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for SuccessExecutiveAssignment record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

