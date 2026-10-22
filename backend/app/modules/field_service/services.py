"""
Field Service & Dispatch Automation - Business Logic Service Layer
"""
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import logging
from .models import RecordStatus, PriorityLevel, RiskClassification

from .models import ServiceWorkOrder
from .models import TechnicianProfile
from .models import SkillCertification
from .models import DispatchAssignment
from .models import RouteWayfinding
from .models import PartsRequirement
from .models import VanInventoryStock
from .models import ServiceReportSignature
from .models import CustomerFeedbackRating
from .models import EmergencyCallout
from .models import MaintenanceChecklist
from .models import WarrantyEntitlement
from .models import ServiceLevelBreachAlert
from .models import TimeOnSiteLog
from .models import EquipmentAssetHistory
from .models import FieldExpenseClaim

logger = logging.getLogger("field_service.services")

class ServiceWorkOrderService:
    """Core enterprise business service for managing ServiceWorkOrder entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ServiceWorkOrder] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SER-{1000 + i}"
            item = ServiceWorkOrder(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ServiceWorkOrder {i}",
                description=f"Primary operational ServiceWorkOrder record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_serviceworkorder(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ServiceWorkOrder:
        """Create, validate, index, and commit new ServiceWorkOrder instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ServiceWorkOrder(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created ServiceWorkOrder {code}")
        logger.info(f"Created ServiceWorkOrder id={instance.id} code={code}")
        return instance

    def get_serviceworkorder_by_id(self, item_id: int) -> Optional[ServiceWorkOrder]:
        """Retrieve single ServiceWorkOrder by primary key identifier."""
        return self._cache.get(item_id)

    def get_serviceworkorder_by_code(self, code: str) -> Optional[ServiceWorkOrder]:
        """Lookup ServiceWorkOrder by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_serviceworkorders(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ServiceWorkOrder]:
        """Return paginated, filtered collection of ServiceWorkOrder entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_serviceworkorders(self, query: str, limit: int = 50) -> List[ServiceWorkOrder]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_serviceworkorder(self, item_id: int, updates: Dict[str, Any]) -> Optional[ServiceWorkOrder]:
        """Apply partial updates to existing ServiceWorkOrder entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ServiceWorkOrder record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_serviceworkorder(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ServiceWorkOrder record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for ServiceWorkOrder."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class TechnicianProfileService:
    """Core enterprise business service for managing TechnicianProfile entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, TechnicianProfile] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"TEC-{1000 + i}"
            item = TechnicianProfile(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise TechnicianProfile {i}",
                description=f"Primary operational TechnicianProfile record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_technicianprofile(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> TechnicianProfile:
        """Create, validate, index, and commit new TechnicianProfile instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = TechnicianProfile(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created TechnicianProfile {code}")
        logger.info(f"Created TechnicianProfile id={instance.id} code={code}")
        return instance

    def get_technicianprofile_by_id(self, item_id: int) -> Optional[TechnicianProfile]:
        """Retrieve single TechnicianProfile by primary key identifier."""
        return self._cache.get(item_id)

    def get_technicianprofile_by_code(self, code: str) -> Optional[TechnicianProfile]:
        """Lookup TechnicianProfile by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_technicianprofiles(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[TechnicianProfile]:
        """Return paginated, filtered collection of TechnicianProfile entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_technicianprofiles(self, query: str, limit: int = 50) -> List[TechnicianProfile]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_technicianprofile(self, item_id: int, updates: Dict[str, Any]) -> Optional[TechnicianProfile]:
        """Apply partial updates to existing TechnicianProfile entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked TechnicianProfile record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_technicianprofile(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of TechnicianProfile record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for TechnicianProfile."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class SkillCertificationService:
    """Core enterprise business service for managing SkillCertification entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, SkillCertification] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SKI-{1000 + i}"
            item = SkillCertification(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise SkillCertification {i}",
                description=f"Primary operational SkillCertification record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_skillcertification(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> SkillCertification:
        """Create, validate, index, and commit new SkillCertification instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = SkillCertification(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created SkillCertification {code}")
        logger.info(f"Created SkillCertification id={instance.id} code={code}")
        return instance

    def get_skillcertification_by_id(self, item_id: int) -> Optional[SkillCertification]:
        """Retrieve single SkillCertification by primary key identifier."""
        return self._cache.get(item_id)

    def get_skillcertification_by_code(self, code: str) -> Optional[SkillCertification]:
        """Lookup SkillCertification by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_skillcertifications(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[SkillCertification]:
        """Return paginated, filtered collection of SkillCertification entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_skillcertifications(self, query: str, limit: int = 50) -> List[SkillCertification]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_skillcertification(self, item_id: int, updates: Dict[str, Any]) -> Optional[SkillCertification]:
        """Apply partial updates to existing SkillCertification entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked SkillCertification record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_skillcertification(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of SkillCertification record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for SkillCertification."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class DispatchAssignmentService:
    """Core enterprise business service for managing DispatchAssignment entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, DispatchAssignment] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"DIS-{1000 + i}"
            item = DispatchAssignment(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise DispatchAssignment {i}",
                description=f"Primary operational DispatchAssignment record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_dispatchassignment(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> DispatchAssignment:
        """Create, validate, index, and commit new DispatchAssignment instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = DispatchAssignment(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created DispatchAssignment {code}")
        logger.info(f"Created DispatchAssignment id={instance.id} code={code}")
        return instance

    def get_dispatchassignment_by_id(self, item_id: int) -> Optional[DispatchAssignment]:
        """Retrieve single DispatchAssignment by primary key identifier."""
        return self._cache.get(item_id)

    def get_dispatchassignment_by_code(self, code: str) -> Optional[DispatchAssignment]:
        """Lookup DispatchAssignment by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_dispatchassignments(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[DispatchAssignment]:
        """Return paginated, filtered collection of DispatchAssignment entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_dispatchassignments(self, query: str, limit: int = 50) -> List[DispatchAssignment]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_dispatchassignment(self, item_id: int, updates: Dict[str, Any]) -> Optional[DispatchAssignment]:
        """Apply partial updates to existing DispatchAssignment entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked DispatchAssignment record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_dispatchassignment(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of DispatchAssignment record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for DispatchAssignment."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class RouteWayfindingService:
    """Core enterprise business service for managing RouteWayfinding entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, RouteWayfinding] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ROU-{1000 + i}"
            item = RouteWayfinding(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise RouteWayfinding {i}",
                description=f"Primary operational RouteWayfinding record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_routewayfinding(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> RouteWayfinding:
        """Create, validate, index, and commit new RouteWayfinding instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = RouteWayfinding(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created RouteWayfinding {code}")
        logger.info(f"Created RouteWayfinding id={instance.id} code={code}")
        return instance

    def get_routewayfinding_by_id(self, item_id: int) -> Optional[RouteWayfinding]:
        """Retrieve single RouteWayfinding by primary key identifier."""
        return self._cache.get(item_id)

    def get_routewayfinding_by_code(self, code: str) -> Optional[RouteWayfinding]:
        """Lookup RouteWayfinding by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_routewayfindings(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[RouteWayfinding]:
        """Return paginated, filtered collection of RouteWayfinding entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_routewayfindings(self, query: str, limit: int = 50) -> List[RouteWayfinding]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_routewayfinding(self, item_id: int, updates: Dict[str, Any]) -> Optional[RouteWayfinding]:
        """Apply partial updates to existing RouteWayfinding entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked RouteWayfinding record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_routewayfinding(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of RouteWayfinding record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for RouteWayfinding."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class PartsRequirementService:
    """Core enterprise business service for managing PartsRequirement entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, PartsRequirement] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"PAR-{1000 + i}"
            item = PartsRequirement(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise PartsRequirement {i}",
                description=f"Primary operational PartsRequirement record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_partsrequirement(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> PartsRequirement:
        """Create, validate, index, and commit new PartsRequirement instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = PartsRequirement(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created PartsRequirement {code}")
        logger.info(f"Created PartsRequirement id={instance.id} code={code}")
        return instance

    def get_partsrequirement_by_id(self, item_id: int) -> Optional[PartsRequirement]:
        """Retrieve single PartsRequirement by primary key identifier."""
        return self._cache.get(item_id)

    def get_partsrequirement_by_code(self, code: str) -> Optional[PartsRequirement]:
        """Lookup PartsRequirement by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_partsrequirements(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[PartsRequirement]:
        """Return paginated, filtered collection of PartsRequirement entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_partsrequirements(self, query: str, limit: int = 50) -> List[PartsRequirement]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_partsrequirement(self, item_id: int, updates: Dict[str, Any]) -> Optional[PartsRequirement]:
        """Apply partial updates to existing PartsRequirement entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked PartsRequirement record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_partsrequirement(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of PartsRequirement record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for PartsRequirement."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class VanInventoryStockService:
    """Core enterprise business service for managing VanInventoryStock entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, VanInventoryStock] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"VAN-{1000 + i}"
            item = VanInventoryStock(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise VanInventoryStock {i}",
                description=f"Primary operational VanInventoryStock record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_vaninventorystock(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> VanInventoryStock:
        """Create, validate, index, and commit new VanInventoryStock instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = VanInventoryStock(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created VanInventoryStock {code}")
        logger.info(f"Created VanInventoryStock id={instance.id} code={code}")
        return instance

    def get_vaninventorystock_by_id(self, item_id: int) -> Optional[VanInventoryStock]:
        """Retrieve single VanInventoryStock by primary key identifier."""
        return self._cache.get(item_id)

    def get_vaninventorystock_by_code(self, code: str) -> Optional[VanInventoryStock]:
        """Lookup VanInventoryStock by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_vaninventorystocks(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[VanInventoryStock]:
        """Return paginated, filtered collection of VanInventoryStock entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_vaninventorystocks(self, query: str, limit: int = 50) -> List[VanInventoryStock]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_vaninventorystock(self, item_id: int, updates: Dict[str, Any]) -> Optional[VanInventoryStock]:
        """Apply partial updates to existing VanInventoryStock entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked VanInventoryStock record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_vaninventorystock(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of VanInventoryStock record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for VanInventoryStock."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class ServiceReportSignatureService:
    """Core enterprise business service for managing ServiceReportSignature entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ServiceReportSignature] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SER-{1000 + i}"
            item = ServiceReportSignature(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ServiceReportSignature {i}",
                description=f"Primary operational ServiceReportSignature record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_servicereportsignature(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ServiceReportSignature:
        """Create, validate, index, and commit new ServiceReportSignature instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ServiceReportSignature(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created ServiceReportSignature {code}")
        logger.info(f"Created ServiceReportSignature id={instance.id} code={code}")
        return instance

    def get_servicereportsignature_by_id(self, item_id: int) -> Optional[ServiceReportSignature]:
        """Retrieve single ServiceReportSignature by primary key identifier."""
        return self._cache.get(item_id)

    def get_servicereportsignature_by_code(self, code: str) -> Optional[ServiceReportSignature]:
        """Lookup ServiceReportSignature by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_servicereportsignatures(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ServiceReportSignature]:
        """Return paginated, filtered collection of ServiceReportSignature entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_servicereportsignatures(self, query: str, limit: int = 50) -> List[ServiceReportSignature]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_servicereportsignature(self, item_id: int, updates: Dict[str, Any]) -> Optional[ServiceReportSignature]:
        """Apply partial updates to existing ServiceReportSignature entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ServiceReportSignature record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_servicereportsignature(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ServiceReportSignature record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for ServiceReportSignature."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class CustomerFeedbackRatingService:
    """Core enterprise business service for managing CustomerFeedbackRating entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, CustomerFeedbackRating] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CUS-{1000 + i}"
            item = CustomerFeedbackRating(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise CustomerFeedbackRating {i}",
                description=f"Primary operational CustomerFeedbackRating record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_customerfeedbackrating(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> CustomerFeedbackRating:
        """Create, validate, index, and commit new CustomerFeedbackRating instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = CustomerFeedbackRating(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created CustomerFeedbackRating {code}")
        logger.info(f"Created CustomerFeedbackRating id={instance.id} code={code}")
        return instance

    def get_customerfeedbackrating_by_id(self, item_id: int) -> Optional[CustomerFeedbackRating]:
        """Retrieve single CustomerFeedbackRating by primary key identifier."""
        return self._cache.get(item_id)

    def get_customerfeedbackrating_by_code(self, code: str) -> Optional[CustomerFeedbackRating]:
        """Lookup CustomerFeedbackRating by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_customerfeedbackratings(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[CustomerFeedbackRating]:
        """Return paginated, filtered collection of CustomerFeedbackRating entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_customerfeedbackratings(self, query: str, limit: int = 50) -> List[CustomerFeedbackRating]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_customerfeedbackrating(self, item_id: int, updates: Dict[str, Any]) -> Optional[CustomerFeedbackRating]:
        """Apply partial updates to existing CustomerFeedbackRating entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked CustomerFeedbackRating record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_customerfeedbackrating(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of CustomerFeedbackRating record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for CustomerFeedbackRating."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class EmergencyCalloutService:
    """Core enterprise business service for managing EmergencyCallout entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, EmergencyCallout] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"EME-{1000 + i}"
            item = EmergencyCallout(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise EmergencyCallout {i}",
                description=f"Primary operational EmergencyCallout record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_emergencycallout(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> EmergencyCallout:
        """Create, validate, index, and commit new EmergencyCallout instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = EmergencyCallout(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created EmergencyCallout {code}")
        logger.info(f"Created EmergencyCallout id={instance.id} code={code}")
        return instance

    def get_emergencycallout_by_id(self, item_id: int) -> Optional[EmergencyCallout]:
        """Retrieve single EmergencyCallout by primary key identifier."""
        return self._cache.get(item_id)

    def get_emergencycallout_by_code(self, code: str) -> Optional[EmergencyCallout]:
        """Lookup EmergencyCallout by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_emergencycallouts(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[EmergencyCallout]:
        """Return paginated, filtered collection of EmergencyCallout entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_emergencycallouts(self, query: str, limit: int = 50) -> List[EmergencyCallout]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_emergencycallout(self, item_id: int, updates: Dict[str, Any]) -> Optional[EmergencyCallout]:
        """Apply partial updates to existing EmergencyCallout entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked EmergencyCallout record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_emergencycallout(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of EmergencyCallout record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for EmergencyCallout."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class MaintenanceChecklistService:
    """Core enterprise business service for managing MaintenanceChecklist entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, MaintenanceChecklist] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"MAI-{1000 + i}"
            item = MaintenanceChecklist(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise MaintenanceChecklist {i}",
                description=f"Primary operational MaintenanceChecklist record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_maintenancechecklist(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> MaintenanceChecklist:
        """Create, validate, index, and commit new MaintenanceChecklist instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = MaintenanceChecklist(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created MaintenanceChecklist {code}")
        logger.info(f"Created MaintenanceChecklist id={instance.id} code={code}")
        return instance

    def get_maintenancechecklist_by_id(self, item_id: int) -> Optional[MaintenanceChecklist]:
        """Retrieve single MaintenanceChecklist by primary key identifier."""
        return self._cache.get(item_id)

    def get_maintenancechecklist_by_code(self, code: str) -> Optional[MaintenanceChecklist]:
        """Lookup MaintenanceChecklist by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_maintenancechecklists(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[MaintenanceChecklist]:
        """Return paginated, filtered collection of MaintenanceChecklist entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_maintenancechecklists(self, query: str, limit: int = 50) -> List[MaintenanceChecklist]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_maintenancechecklist(self, item_id: int, updates: Dict[str, Any]) -> Optional[MaintenanceChecklist]:
        """Apply partial updates to existing MaintenanceChecklist entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked MaintenanceChecklist record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_maintenancechecklist(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of MaintenanceChecklist record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for MaintenanceChecklist."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class WarrantyEntitlementService:
    """Core enterprise business service for managing WarrantyEntitlement entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, WarrantyEntitlement] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"WAR-{1000 + i}"
            item = WarrantyEntitlement(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise WarrantyEntitlement {i}",
                description=f"Primary operational WarrantyEntitlement record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_warrantyentitlement(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> WarrantyEntitlement:
        """Create, validate, index, and commit new WarrantyEntitlement instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = WarrantyEntitlement(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created WarrantyEntitlement {code}")
        logger.info(f"Created WarrantyEntitlement id={instance.id} code={code}")
        return instance

    def get_warrantyentitlement_by_id(self, item_id: int) -> Optional[WarrantyEntitlement]:
        """Retrieve single WarrantyEntitlement by primary key identifier."""
        return self._cache.get(item_id)

    def get_warrantyentitlement_by_code(self, code: str) -> Optional[WarrantyEntitlement]:
        """Lookup WarrantyEntitlement by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_warrantyentitlements(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[WarrantyEntitlement]:
        """Return paginated, filtered collection of WarrantyEntitlement entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_warrantyentitlements(self, query: str, limit: int = 50) -> List[WarrantyEntitlement]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_warrantyentitlement(self, item_id: int, updates: Dict[str, Any]) -> Optional[WarrantyEntitlement]:
        """Apply partial updates to existing WarrantyEntitlement entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked WarrantyEntitlement record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_warrantyentitlement(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of WarrantyEntitlement record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for WarrantyEntitlement."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class ServiceLevelBreachAlertService:
    """Core enterprise business service for managing ServiceLevelBreachAlert entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ServiceLevelBreachAlert] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SER-{1000 + i}"
            item = ServiceLevelBreachAlert(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ServiceLevelBreachAlert {i}",
                description=f"Primary operational ServiceLevelBreachAlert record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_servicelevelbreachalert(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ServiceLevelBreachAlert:
        """Create, validate, index, and commit new ServiceLevelBreachAlert instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ServiceLevelBreachAlert(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created ServiceLevelBreachAlert {code}")
        logger.info(f"Created ServiceLevelBreachAlert id={instance.id} code={code}")
        return instance

    def get_servicelevelbreachalert_by_id(self, item_id: int) -> Optional[ServiceLevelBreachAlert]:
        """Retrieve single ServiceLevelBreachAlert by primary key identifier."""
        return self._cache.get(item_id)

    def get_servicelevelbreachalert_by_code(self, code: str) -> Optional[ServiceLevelBreachAlert]:
        """Lookup ServiceLevelBreachAlert by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_servicelevelbreachalerts(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ServiceLevelBreachAlert]:
        """Return paginated, filtered collection of ServiceLevelBreachAlert entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_servicelevelbreachalerts(self, query: str, limit: int = 50) -> List[ServiceLevelBreachAlert]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_servicelevelbreachalert(self, item_id: int, updates: Dict[str, Any]) -> Optional[ServiceLevelBreachAlert]:
        """Apply partial updates to existing ServiceLevelBreachAlert entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ServiceLevelBreachAlert record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_servicelevelbreachalert(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ServiceLevelBreachAlert record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for ServiceLevelBreachAlert."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class TimeOnSiteLogService:
    """Core enterprise business service for managing TimeOnSiteLog entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, TimeOnSiteLog] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"TIM-{1000 + i}"
            item = TimeOnSiteLog(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise TimeOnSiteLog {i}",
                description=f"Primary operational TimeOnSiteLog record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_timeonsitelog(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> TimeOnSiteLog:
        """Create, validate, index, and commit new TimeOnSiteLog instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = TimeOnSiteLog(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created TimeOnSiteLog {code}")
        logger.info(f"Created TimeOnSiteLog id={instance.id} code={code}")
        return instance

    def get_timeonsitelog_by_id(self, item_id: int) -> Optional[TimeOnSiteLog]:
        """Retrieve single TimeOnSiteLog by primary key identifier."""
        return self._cache.get(item_id)

    def get_timeonsitelog_by_code(self, code: str) -> Optional[TimeOnSiteLog]:
        """Lookup TimeOnSiteLog by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_timeonsitelogs(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[TimeOnSiteLog]:
        """Return paginated, filtered collection of TimeOnSiteLog entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_timeonsitelogs(self, query: str, limit: int = 50) -> List[TimeOnSiteLog]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_timeonsitelog(self, item_id: int, updates: Dict[str, Any]) -> Optional[TimeOnSiteLog]:
        """Apply partial updates to existing TimeOnSiteLog entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked TimeOnSiteLog record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_timeonsitelog(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of TimeOnSiteLog record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for TimeOnSiteLog."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class EquipmentAssetHistoryService:
    """Core enterprise business service for managing EquipmentAssetHistory entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, EquipmentAssetHistory] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"EQU-{1000 + i}"
            item = EquipmentAssetHistory(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise EquipmentAssetHistory {i}",
                description=f"Primary operational EquipmentAssetHistory record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_equipmentassethistory(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> EquipmentAssetHistory:
        """Create, validate, index, and commit new EquipmentAssetHistory instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = EquipmentAssetHistory(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created EquipmentAssetHistory {code}")
        logger.info(f"Created EquipmentAssetHistory id={instance.id} code={code}")
        return instance

    def get_equipmentassethistory_by_id(self, item_id: int) -> Optional[EquipmentAssetHistory]:
        """Retrieve single EquipmentAssetHistory by primary key identifier."""
        return self._cache.get(item_id)

    def get_equipmentassethistory_by_code(self, code: str) -> Optional[EquipmentAssetHistory]:
        """Lookup EquipmentAssetHistory by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_equipmentassethistorys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[EquipmentAssetHistory]:
        """Return paginated, filtered collection of EquipmentAssetHistory entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_equipmentassethistorys(self, query: str, limit: int = 50) -> List[EquipmentAssetHistory]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_equipmentassethistory(self, item_id: int, updates: Dict[str, Any]) -> Optional[EquipmentAssetHistory]:
        """Apply partial updates to existing EquipmentAssetHistory entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked EquipmentAssetHistory record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_equipmentassethistory(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of EquipmentAssetHistory record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for EquipmentAssetHistory."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

class FieldExpenseClaimService:
    """Core enterprise business service for managing FieldExpenseClaim entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, FieldExpenseClaim] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"FIE-{1000 + i}"
            item = FieldExpenseClaim(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise FieldExpenseClaim {i}",
                description=f"Primary operational FieldExpenseClaim record generated for organization unit 1.",
                status=RecordStatus.ACTIVE,
                priority=PriorityLevel.MEDIUM,
                amount=float(i * 12500.0),
                quantity=float(i * 25.0),
                unit_price=500.0,
                unit_cost=320.0,
                tax_rate=0.18,
                currency="INR",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            self._cache[item.id] = item
            self._code_index[code] = item.id
        self._id_sequence += 10

    def create_fieldexpenseclaim(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> FieldExpenseClaim:
        """Create, validate, index, and commit new FieldExpenseClaim instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = FieldExpenseClaim(
            id=self._id_sequence,
            code=code,
            title=title,
            amount=amount,
            quantity=quantity,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **kwargs
        )
        instance.validate()
        self._cache[instance.id] = instance
        self._code_index[code] = instance.id
        self._record_audit_event("CREATE", instance.id, f"Created FieldExpenseClaim {code}")
        logger.info(f"Created FieldExpenseClaim id={instance.id} code={code}")
        return instance

    def get_fieldexpenseclaim_by_id(self, item_id: int) -> Optional[FieldExpenseClaim]:
        """Retrieve single FieldExpenseClaim by primary key identifier."""
        return self._cache.get(item_id)

    def get_fieldexpenseclaim_by_code(self, code: str) -> Optional[FieldExpenseClaim]:
        """Lookup FieldExpenseClaim by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_fieldexpenseclaims(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[FieldExpenseClaim]:
        """Return paginated, filtered collection of FieldExpenseClaim entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_fieldexpenseclaims(self, query: str, limit: int = 50) -> List[FieldExpenseClaim]:
        """Fuzzy match query across code, title, and description fields."""
        q = query.lower().strip()
        matches = []
        for item in self._cache.values():
            if item.is_deleted:
                continue
            if q in item.code.lower() or q in item.title.lower() or (item.description and q in item.description.lower()):
                matches.append(item)
                if len(matches) >= limit:
                    break
        return matches

    def update_fieldexpenseclaim(self, item_id: int, updates: Dict[str, Any]) -> Optional[FieldExpenseClaim]:
        """Apply partial updates to existing FieldExpenseClaim entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked FieldExpenseClaim record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_fieldexpenseclaim(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of FieldExpenseClaim record."""
        item = self._cache.get(item_id)
        if not item:
            return False
        if hard_delete:
            del self._cache[item_id]
            if item.code in self._code_index:
                del self._code_index[item.code]
            self._record_audit_event("HARD_DELETE", item_id, "Permanently purged record")
        else:
            item.is_deleted = True
            item.is_active = False
            item.updated_at = datetime.utcnow()
            self._record_audit_event("SOFT_DELETE", item_id, "Marked record as deleted")
        return True

    def transition_status(self, item_id: int, new_status: RecordStatus, reason: str = "") -> bool:
        """Safely transition entity lifecycle status through governance rules."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return False
        old_status = item.status
        item.status = new_status
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        self._record_audit_event("STATUS_TRANSITION", item_id, f"Transition from {old_status} to {new_status}. Reason: {reason}")
        return True

    def calculate_aggregate_metrics(self) -> Dict[str, Any]:
        """Calculate operational and financial aggregate metrics for FieldExpenseClaim."""
        active_items = [x for x in self._cache.values() if not x.is_deleted and x.is_active]
        count = len(active_items)
        if count == 0:
            return {"count": 0, "total_amount": 0.0, "total_quantity": 0.0, "avg_amount": 0.0, "avg_margin": 0.0}
        total_amt = sum(x.calculate_total_amount() for x in active_items)
        total_qty = sum(x.quantity for x in active_items)
        avg_amt = total_amt / count
        avg_margin = sum(x.calculate_profit_margin() for x in active_items) / count
        return {
            "count": count,
            "total_amount": round(total_amt, 2),
            "total_quantity": round(total_qty, 2),
            "average_amount": round(avg_amt, 2),
            "average_margin_percent": round(avg_margin, 2),
        }

    def _record_audit_event(self, action: str, entity_id: int, description: str):
        """Log internal audit trail entry."""
        self._audit_log.append({
            "action": action,
            "entity_id": entity_id,
            "description": description,
            "timestamp": datetime.utcnow().isoformat(),
        })

    def get_audit_trail(self, entity_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve immutable audit log history."""
        if entity_id:
            return [x for x in self._audit_log if x["entity_id"] == entity_id]
        return self._audit_log

