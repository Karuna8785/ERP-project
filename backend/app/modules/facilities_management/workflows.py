"""
Facilities & Corporate Real Estate - Governance Approval Workflows & State Machine Transitions
"""
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from .models import RecordStatus, PriorityLevel

class FacilitiesManagementWorkflowEngine:
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
    def execute_facilitybuilding_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for FacilityBuilding record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_officefloorwing_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for OfficeFloorWing record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_roomdeskallocation_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for RoomDeskAllocation record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_hvaccontrolschedule_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for HVACControlSchedule record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_physicalbadgeaccesslog_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for PhysicalBadgeAccessLog record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_securityvisitorpass_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for SecurityVisitorPass record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_janitorialtasklog_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for JanitorialTaskLog record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_leasespacecontract_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for LeaseSpaceContract record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_emergencyevacuationplan_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for EmergencyEvacuationPlan record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_utilitymeterrecord_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for UtilityMeterRecord record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_parkingslotallocation_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for ParkingSlotAllocation record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_assettaglocation_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for AssetTagLocation record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_incidenthazardnotice_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for IncidentHazardNotice record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_mailroompackagelog_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for MailroomPackageLog record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_cateringrequestorder_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for CateringRequestOrder record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

    @classmethod
    def execute_facilityexpensecharge_transition(cls, item, new_status: RecordStatus, user_role: str = "MANAGER") -> Tuple[bool, str]:
        """Execute validated transition for FacilityExpenseCharge record."""
        if not cls.can_transition(item.status, new_status):
            return False, f"Illegal state transition from {item.status} to {new_status}"
        item.status = new_status
        item.updated_at = datetime.utcnow()
        return True, f"Successfully transitioned to {new_status}"

