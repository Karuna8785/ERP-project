"""
Partner Relationship Management (PRM) - Governance Approval Workflows & State Machine Transitions
"""
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from .models import RecordStatus, PriorityLevel

class PartnerNetworkWorkflowEngine:
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
    def execute_channelpartnerprofile_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ChannelPartnerProfile record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_partnertierlevel_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PartnerTierLevel record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_dealregistrationlead_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for DealRegistrationLead record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_mdfmarketfundrequest_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for MDFMarketFundRequest record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_comarketingcampaign_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CoMarketingCampaign record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_partnercommissionpayout_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PartnerCommissionPayout record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_certificationcredential_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CertificationCredential record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_partnersalesgoal_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PartnerSalesGoal record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_reselleragreementcontract_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ResellerAgreementContract record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_leaddistributionrule_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for LeadDistributionRule record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_partnerportalcredential_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PartnerPortalCredential record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_channelconflictdispute_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ChannelConflictDispute record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_territorypartnerexclusivity_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for TerritoryPartnerExclusivity record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_partnertrainingprogress_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PartnerTrainingProgress record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_jointsolutionlisting_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for JointSolutionListing record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_channelrevenueforecast_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ChannelRevenueForecast record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

