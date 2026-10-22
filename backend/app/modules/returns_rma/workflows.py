"""
Reverse Logistics & Customer Returns (RMA) - Governance Approval Workflows & State Machine Transitions
"""
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from .models import RecordStatus, PriorityLevel

class ReturnsRmaWorkflowEngine:
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
    def execute_returnmerchandiseauth_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ReturnMerchandiseAuth record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_receivinginspectionqa_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ReceivingInspectionQA record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_restockingfeerule_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for RestockingFeeRule record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_customerrefundcreditnote_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CustomerRefundCreditNote record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_quarantinedisposition_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for QuarantineDisposition record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_warrantyverification_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for WarrantyVerification record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_refurbishmentworkorder_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for RefurbishmentWorkOrder record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_scrapauthorization_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ScrapAuthorization record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_carrierreturnwaybill_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CarrierReturnWaybill record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_customerreturnreason_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CustomerReturnReason record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_replacementshipment_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ReplacementShipment record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_returnanalyticsmetric_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ReturnAnalyticsMetric record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_vendorchargebackclaim_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for VendorChargebackClaim record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_packagingconditionlog_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PackagingConditionLog record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_returnpolicyrule_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ReturnPolicyRule record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_depotrepairstatus_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for DepotRepairStatus record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

