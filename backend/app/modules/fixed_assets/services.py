"""
Enterprise Fixed Asset Management - Business Logic Service Layer
"""
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import logging
from .models import RecordStatus, PriorityLevel, RiskClassification

from .models import AssetMaster
from .models import AssetCategory
from .models import DepreciationSchedule
from .models import DepreciationRun
from .models import AssetRevaluation
from .models import AssetImpairment
from .models import MaintenanceSchedule
from .models import WorkOrderAsset
from .models import AssetDisposal
from .models import AssetTransferLog
from .models import PhysicalVerification
from .models import WarrantyAgreement
from .models import InsurancePolicy
from .models import LeaseSchedule
from .models import ComponentAsset
from .models import DisposalProceeds

logger = logging.getLogger("fixed_assets.services")

class AssetMasterService:
    """Core enterprise business service for managing AssetMaster entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, AssetMaster] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ASS-{1000 + i}"
            item = AssetMaster(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise AssetMaster {i}",
                description=f"Primary operational AssetMaster record generated for organization unit 1.",
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

    def create_assetmaster(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> AssetMaster:
        """Create, validate, index, and commit new AssetMaster instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = AssetMaster(
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
        self._record_audit_event("CREATE", instance.id, f"Created AssetMaster {code}")
        logger.info(f"Created AssetMaster id={instance.id} code={code}")
        return instance

    def get_assetmaster_by_id(self, item_id: int) -> Optional[AssetMaster]:
        """Retrieve single AssetMaster by primary key identifier."""
        return self._cache.get(item_id)

    def get_assetmaster_by_code(self, code: str) -> Optional[AssetMaster]:
        """Lookup AssetMaster by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_assetmasters(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[AssetMaster]:
        """Return paginated, filtered collection of AssetMaster entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_assetmasters(self, query: str, limit: int = 50) -> List[AssetMaster]:
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

    def update_assetmaster(self, item_id: int, updates: Dict[str, Any]) -> Optional[AssetMaster]:
        """Apply partial updates to existing AssetMaster entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked AssetMaster record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_assetmaster(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of AssetMaster record."""
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
        """Calculate operational and financial aggregate metrics for AssetMaster."""
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

class AssetCategoryService:
    """Core enterprise business service for managing AssetCategory entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, AssetCategory] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ASS-{1000 + i}"
            item = AssetCategory(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise AssetCategory {i}",
                description=f"Primary operational AssetCategory record generated for organization unit 1.",
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

    def create_assetcategory(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> AssetCategory:
        """Create, validate, index, and commit new AssetCategory instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = AssetCategory(
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
        self._record_audit_event("CREATE", instance.id, f"Created AssetCategory {code}")
        logger.info(f"Created AssetCategory id={instance.id} code={code}")
        return instance

    def get_assetcategory_by_id(self, item_id: int) -> Optional[AssetCategory]:
        """Retrieve single AssetCategory by primary key identifier."""
        return self._cache.get(item_id)

    def get_assetcategory_by_code(self, code: str) -> Optional[AssetCategory]:
        """Lookup AssetCategory by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_assetcategorys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[AssetCategory]:
        """Return paginated, filtered collection of AssetCategory entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_assetcategorys(self, query: str, limit: int = 50) -> List[AssetCategory]:
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

    def update_assetcategory(self, item_id: int, updates: Dict[str, Any]) -> Optional[AssetCategory]:
        """Apply partial updates to existing AssetCategory entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked AssetCategory record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_assetcategory(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of AssetCategory record."""
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
        """Calculate operational and financial aggregate metrics for AssetCategory."""
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

class DepreciationScheduleService:
    """Core enterprise business service for managing DepreciationSchedule entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, DepreciationSchedule] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"DEP-{1000 + i}"
            item = DepreciationSchedule(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise DepreciationSchedule {i}",
                description=f"Primary operational DepreciationSchedule record generated for organization unit 1.",
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

    def create_depreciationschedule(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> DepreciationSchedule:
        """Create, validate, index, and commit new DepreciationSchedule instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = DepreciationSchedule(
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
        self._record_audit_event("CREATE", instance.id, f"Created DepreciationSchedule {code}")
        logger.info(f"Created DepreciationSchedule id={instance.id} code={code}")
        return instance

    def get_depreciationschedule_by_id(self, item_id: int) -> Optional[DepreciationSchedule]:
        """Retrieve single DepreciationSchedule by primary key identifier."""
        return self._cache.get(item_id)

    def get_depreciationschedule_by_code(self, code: str) -> Optional[DepreciationSchedule]:
        """Lookup DepreciationSchedule by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_depreciationschedules(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[DepreciationSchedule]:
        """Return paginated, filtered collection of DepreciationSchedule entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_depreciationschedules(self, query: str, limit: int = 50) -> List[DepreciationSchedule]:
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

    def update_depreciationschedule(self, item_id: int, updates: Dict[str, Any]) -> Optional[DepreciationSchedule]:
        """Apply partial updates to existing DepreciationSchedule entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked DepreciationSchedule record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_depreciationschedule(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of DepreciationSchedule record."""
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
        """Calculate operational and financial aggregate metrics for DepreciationSchedule."""
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

class DepreciationRunService:
    """Core enterprise business service for managing DepreciationRun entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, DepreciationRun] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"DEP-{1000 + i}"
            item = DepreciationRun(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise DepreciationRun {i}",
                description=f"Primary operational DepreciationRun record generated for organization unit 1.",
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

    def create_depreciationrun(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> DepreciationRun:
        """Create, validate, index, and commit new DepreciationRun instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = DepreciationRun(
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
        self._record_audit_event("CREATE", instance.id, f"Created DepreciationRun {code}")
        logger.info(f"Created DepreciationRun id={instance.id} code={code}")
        return instance

    def get_depreciationrun_by_id(self, item_id: int) -> Optional[DepreciationRun]:
        """Retrieve single DepreciationRun by primary key identifier."""
        return self._cache.get(item_id)

    def get_depreciationrun_by_code(self, code: str) -> Optional[DepreciationRun]:
        """Lookup DepreciationRun by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_depreciationruns(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[DepreciationRun]:
        """Return paginated, filtered collection of DepreciationRun entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_depreciationruns(self, query: str, limit: int = 50) -> List[DepreciationRun]:
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

    def update_depreciationrun(self, item_id: int, updates: Dict[str, Any]) -> Optional[DepreciationRun]:
        """Apply partial updates to existing DepreciationRun entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked DepreciationRun record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_depreciationrun(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of DepreciationRun record."""
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
        """Calculate operational and financial aggregate metrics for DepreciationRun."""
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

class AssetRevaluationService:
    """Core enterprise business service for managing AssetRevaluation entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, AssetRevaluation] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ASS-{1000 + i}"
            item = AssetRevaluation(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise AssetRevaluation {i}",
                description=f"Primary operational AssetRevaluation record generated for organization unit 1.",
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

    def create_assetrevaluation(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> AssetRevaluation:
        """Create, validate, index, and commit new AssetRevaluation instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = AssetRevaluation(
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
        self._record_audit_event("CREATE", instance.id, f"Created AssetRevaluation {code}")
        logger.info(f"Created AssetRevaluation id={instance.id} code={code}")
        return instance

    def get_assetrevaluation_by_id(self, item_id: int) -> Optional[AssetRevaluation]:
        """Retrieve single AssetRevaluation by primary key identifier."""
        return self._cache.get(item_id)

    def get_assetrevaluation_by_code(self, code: str) -> Optional[AssetRevaluation]:
        """Lookup AssetRevaluation by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_assetrevaluations(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[AssetRevaluation]:
        """Return paginated, filtered collection of AssetRevaluation entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_assetrevaluations(self, query: str, limit: int = 50) -> List[AssetRevaluation]:
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

    def update_assetrevaluation(self, item_id: int, updates: Dict[str, Any]) -> Optional[AssetRevaluation]:
        """Apply partial updates to existing AssetRevaluation entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked AssetRevaluation record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_assetrevaluation(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of AssetRevaluation record."""
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
        """Calculate operational and financial aggregate metrics for AssetRevaluation."""
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

class AssetImpairmentService:
    """Core enterprise business service for managing AssetImpairment entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, AssetImpairment] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ASS-{1000 + i}"
            item = AssetImpairment(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise AssetImpairment {i}",
                description=f"Primary operational AssetImpairment record generated for organization unit 1.",
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

    def create_assetimpairment(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> AssetImpairment:
        """Create, validate, index, and commit new AssetImpairment instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = AssetImpairment(
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
        self._record_audit_event("CREATE", instance.id, f"Created AssetImpairment {code}")
        logger.info(f"Created AssetImpairment id={instance.id} code={code}")
        return instance

    def get_assetimpairment_by_id(self, item_id: int) -> Optional[AssetImpairment]:
        """Retrieve single AssetImpairment by primary key identifier."""
        return self._cache.get(item_id)

    def get_assetimpairment_by_code(self, code: str) -> Optional[AssetImpairment]:
        """Lookup AssetImpairment by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_assetimpairments(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[AssetImpairment]:
        """Return paginated, filtered collection of AssetImpairment entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_assetimpairments(self, query: str, limit: int = 50) -> List[AssetImpairment]:
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

    def update_assetimpairment(self, item_id: int, updates: Dict[str, Any]) -> Optional[AssetImpairment]:
        """Apply partial updates to existing AssetImpairment entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked AssetImpairment record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_assetimpairment(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of AssetImpairment record."""
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
        """Calculate operational and financial aggregate metrics for AssetImpairment."""
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

class MaintenanceScheduleService:
    """Core enterprise business service for managing MaintenanceSchedule entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, MaintenanceSchedule] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"MAI-{1000 + i}"
            item = MaintenanceSchedule(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise MaintenanceSchedule {i}",
                description=f"Primary operational MaintenanceSchedule record generated for organization unit 1.",
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

    def create_maintenanceschedule(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> MaintenanceSchedule:
        """Create, validate, index, and commit new MaintenanceSchedule instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = MaintenanceSchedule(
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
        self._record_audit_event("CREATE", instance.id, f"Created MaintenanceSchedule {code}")
        logger.info(f"Created MaintenanceSchedule id={instance.id} code={code}")
        return instance

    def get_maintenanceschedule_by_id(self, item_id: int) -> Optional[MaintenanceSchedule]:
        """Retrieve single MaintenanceSchedule by primary key identifier."""
        return self._cache.get(item_id)

    def get_maintenanceschedule_by_code(self, code: str) -> Optional[MaintenanceSchedule]:
        """Lookup MaintenanceSchedule by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_maintenanceschedules(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[MaintenanceSchedule]:
        """Return paginated, filtered collection of MaintenanceSchedule entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_maintenanceschedules(self, query: str, limit: int = 50) -> List[MaintenanceSchedule]:
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

    def update_maintenanceschedule(self, item_id: int, updates: Dict[str, Any]) -> Optional[MaintenanceSchedule]:
        """Apply partial updates to existing MaintenanceSchedule entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked MaintenanceSchedule record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_maintenanceschedule(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of MaintenanceSchedule record."""
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
        """Calculate operational and financial aggregate metrics for MaintenanceSchedule."""
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

class WorkOrderAssetService:
    """Core enterprise business service for managing WorkOrderAsset entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, WorkOrderAsset] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"WOR-{1000 + i}"
            item = WorkOrderAsset(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise WorkOrderAsset {i}",
                description=f"Primary operational WorkOrderAsset record generated for organization unit 1.",
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

    def create_workorderasset(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> WorkOrderAsset:
        """Create, validate, index, and commit new WorkOrderAsset instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = WorkOrderAsset(
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
        self._record_audit_event("CREATE", instance.id, f"Created WorkOrderAsset {code}")
        logger.info(f"Created WorkOrderAsset id={instance.id} code={code}")
        return instance

    def get_workorderasset_by_id(self, item_id: int) -> Optional[WorkOrderAsset]:
        """Retrieve single WorkOrderAsset by primary key identifier."""
        return self._cache.get(item_id)

    def get_workorderasset_by_code(self, code: str) -> Optional[WorkOrderAsset]:
        """Lookup WorkOrderAsset by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_workorderassets(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[WorkOrderAsset]:
        """Return paginated, filtered collection of WorkOrderAsset entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_workorderassets(self, query: str, limit: int = 50) -> List[WorkOrderAsset]:
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

    def update_workorderasset(self, item_id: int, updates: Dict[str, Any]) -> Optional[WorkOrderAsset]:
        """Apply partial updates to existing WorkOrderAsset entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked WorkOrderAsset record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_workorderasset(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of WorkOrderAsset record."""
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
        """Calculate operational and financial aggregate metrics for WorkOrderAsset."""
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

class AssetDisposalService:
    """Core enterprise business service for managing AssetDisposal entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, AssetDisposal] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ASS-{1000 + i}"
            item = AssetDisposal(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise AssetDisposal {i}",
                description=f"Primary operational AssetDisposal record generated for organization unit 1.",
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

    def create_assetdisposal(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> AssetDisposal:
        """Create, validate, index, and commit new AssetDisposal instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = AssetDisposal(
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
        self._record_audit_event("CREATE", instance.id, f"Created AssetDisposal {code}")
        logger.info(f"Created AssetDisposal id={instance.id} code={code}")
        return instance

    def get_assetdisposal_by_id(self, item_id: int) -> Optional[AssetDisposal]:
        """Retrieve single AssetDisposal by primary key identifier."""
        return self._cache.get(item_id)

    def get_assetdisposal_by_code(self, code: str) -> Optional[AssetDisposal]:
        """Lookup AssetDisposal by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_assetdisposals(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[AssetDisposal]:
        """Return paginated, filtered collection of AssetDisposal entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_assetdisposals(self, query: str, limit: int = 50) -> List[AssetDisposal]:
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

    def update_assetdisposal(self, item_id: int, updates: Dict[str, Any]) -> Optional[AssetDisposal]:
        """Apply partial updates to existing AssetDisposal entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked AssetDisposal record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_assetdisposal(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of AssetDisposal record."""
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
        """Calculate operational and financial aggregate metrics for AssetDisposal."""
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

class AssetTransferLogService:
    """Core enterprise business service for managing AssetTransferLog entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, AssetTransferLog] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ASS-{1000 + i}"
            item = AssetTransferLog(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise AssetTransferLog {i}",
                description=f"Primary operational AssetTransferLog record generated for organization unit 1.",
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

    def create_assettransferlog(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> AssetTransferLog:
        """Create, validate, index, and commit new AssetTransferLog instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = AssetTransferLog(
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
        self._record_audit_event("CREATE", instance.id, f"Created AssetTransferLog {code}")
        logger.info(f"Created AssetTransferLog id={instance.id} code={code}")
        return instance

    def get_assettransferlog_by_id(self, item_id: int) -> Optional[AssetTransferLog]:
        """Retrieve single AssetTransferLog by primary key identifier."""
        return self._cache.get(item_id)

    def get_assettransferlog_by_code(self, code: str) -> Optional[AssetTransferLog]:
        """Lookup AssetTransferLog by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_assettransferlogs(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[AssetTransferLog]:
        """Return paginated, filtered collection of AssetTransferLog entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_assettransferlogs(self, query: str, limit: int = 50) -> List[AssetTransferLog]:
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

    def update_assettransferlog(self, item_id: int, updates: Dict[str, Any]) -> Optional[AssetTransferLog]:
        """Apply partial updates to existing AssetTransferLog entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked AssetTransferLog record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_assettransferlog(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of AssetTransferLog record."""
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
        """Calculate operational and financial aggregate metrics for AssetTransferLog."""
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

class PhysicalVerificationService:
    """Core enterprise business service for managing PhysicalVerification entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, PhysicalVerification] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"PHY-{1000 + i}"
            item = PhysicalVerification(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise PhysicalVerification {i}",
                description=f"Primary operational PhysicalVerification record generated for organization unit 1.",
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

    def create_physicalverification(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> PhysicalVerification:
        """Create, validate, index, and commit new PhysicalVerification instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = PhysicalVerification(
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
        self._record_audit_event("CREATE", instance.id, f"Created PhysicalVerification {code}")
        logger.info(f"Created PhysicalVerification id={instance.id} code={code}")
        return instance

    def get_physicalverification_by_id(self, item_id: int) -> Optional[PhysicalVerification]:
        """Retrieve single PhysicalVerification by primary key identifier."""
        return self._cache.get(item_id)

    def get_physicalverification_by_code(self, code: str) -> Optional[PhysicalVerification]:
        """Lookup PhysicalVerification by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_physicalverifications(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[PhysicalVerification]:
        """Return paginated, filtered collection of PhysicalVerification entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_physicalverifications(self, query: str, limit: int = 50) -> List[PhysicalVerification]:
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

    def update_physicalverification(self, item_id: int, updates: Dict[str, Any]) -> Optional[PhysicalVerification]:
        """Apply partial updates to existing PhysicalVerification entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked PhysicalVerification record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_physicalverification(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of PhysicalVerification record."""
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
        """Calculate operational and financial aggregate metrics for PhysicalVerification."""
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

class WarrantyAgreementService:
    """Core enterprise business service for managing WarrantyAgreement entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, WarrantyAgreement] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"WAR-{1000 + i}"
            item = WarrantyAgreement(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise WarrantyAgreement {i}",
                description=f"Primary operational WarrantyAgreement record generated for organization unit 1.",
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

    def create_warrantyagreement(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> WarrantyAgreement:
        """Create, validate, index, and commit new WarrantyAgreement instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = WarrantyAgreement(
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
        self._record_audit_event("CREATE", instance.id, f"Created WarrantyAgreement {code}")
        logger.info(f"Created WarrantyAgreement id={instance.id} code={code}")
        return instance

    def get_warrantyagreement_by_id(self, item_id: int) -> Optional[WarrantyAgreement]:
        """Retrieve single WarrantyAgreement by primary key identifier."""
        return self._cache.get(item_id)

    def get_warrantyagreement_by_code(self, code: str) -> Optional[WarrantyAgreement]:
        """Lookup WarrantyAgreement by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_warrantyagreements(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[WarrantyAgreement]:
        """Return paginated, filtered collection of WarrantyAgreement entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_warrantyagreements(self, query: str, limit: int = 50) -> List[WarrantyAgreement]:
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

    def update_warrantyagreement(self, item_id: int, updates: Dict[str, Any]) -> Optional[WarrantyAgreement]:
        """Apply partial updates to existing WarrantyAgreement entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked WarrantyAgreement record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_warrantyagreement(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of WarrantyAgreement record."""
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
        """Calculate operational and financial aggregate metrics for WarrantyAgreement."""
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

class InsurancePolicyService:
    """Core enterprise business service for managing InsurancePolicy entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, InsurancePolicy] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"INS-{1000 + i}"
            item = InsurancePolicy(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise InsurancePolicy {i}",
                description=f"Primary operational InsurancePolicy record generated for organization unit 1.",
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

    def create_insurancepolicy(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> InsurancePolicy:
        """Create, validate, index, and commit new InsurancePolicy instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = InsurancePolicy(
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
        self._record_audit_event("CREATE", instance.id, f"Created InsurancePolicy {code}")
        logger.info(f"Created InsurancePolicy id={instance.id} code={code}")
        return instance

    def get_insurancepolicy_by_id(self, item_id: int) -> Optional[InsurancePolicy]:
        """Retrieve single InsurancePolicy by primary key identifier."""
        return self._cache.get(item_id)

    def get_insurancepolicy_by_code(self, code: str) -> Optional[InsurancePolicy]:
        """Lookup InsurancePolicy by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_insurancepolicys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[InsurancePolicy]:
        """Return paginated, filtered collection of InsurancePolicy entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_insurancepolicys(self, query: str, limit: int = 50) -> List[InsurancePolicy]:
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

    def update_insurancepolicy(self, item_id: int, updates: Dict[str, Any]) -> Optional[InsurancePolicy]:
        """Apply partial updates to existing InsurancePolicy entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked InsurancePolicy record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_insurancepolicy(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of InsurancePolicy record."""
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
        """Calculate operational and financial aggregate metrics for InsurancePolicy."""
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

class LeaseScheduleService:
    """Core enterprise business service for managing LeaseSchedule entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, LeaseSchedule] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"LEA-{1000 + i}"
            item = LeaseSchedule(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise LeaseSchedule {i}",
                description=f"Primary operational LeaseSchedule record generated for organization unit 1.",
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

    def create_leaseschedule(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> LeaseSchedule:
        """Create, validate, index, and commit new LeaseSchedule instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = LeaseSchedule(
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
        self._record_audit_event("CREATE", instance.id, f"Created LeaseSchedule {code}")
        logger.info(f"Created LeaseSchedule id={instance.id} code={code}")
        return instance

    def get_leaseschedule_by_id(self, item_id: int) -> Optional[LeaseSchedule]:
        """Retrieve single LeaseSchedule by primary key identifier."""
        return self._cache.get(item_id)

    def get_leaseschedule_by_code(self, code: str) -> Optional[LeaseSchedule]:
        """Lookup LeaseSchedule by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_leaseschedules(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[LeaseSchedule]:
        """Return paginated, filtered collection of LeaseSchedule entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_leaseschedules(self, query: str, limit: int = 50) -> List[LeaseSchedule]:
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

    def update_leaseschedule(self, item_id: int, updates: Dict[str, Any]) -> Optional[LeaseSchedule]:
        """Apply partial updates to existing LeaseSchedule entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked LeaseSchedule record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_leaseschedule(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of LeaseSchedule record."""
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
        """Calculate operational and financial aggregate metrics for LeaseSchedule."""
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

class ComponentAssetService:
    """Core enterprise business service for managing ComponentAsset entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ComponentAsset] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"COM-{1000 + i}"
            item = ComponentAsset(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ComponentAsset {i}",
                description=f"Primary operational ComponentAsset record generated for organization unit 1.",
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

    def create_componentasset(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ComponentAsset:
        """Create, validate, index, and commit new ComponentAsset instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ComponentAsset(
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
        self._record_audit_event("CREATE", instance.id, f"Created ComponentAsset {code}")
        logger.info(f"Created ComponentAsset id={instance.id} code={code}")
        return instance

    def get_componentasset_by_id(self, item_id: int) -> Optional[ComponentAsset]:
        """Retrieve single ComponentAsset by primary key identifier."""
        return self._cache.get(item_id)

    def get_componentasset_by_code(self, code: str) -> Optional[ComponentAsset]:
        """Lookup ComponentAsset by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_componentassets(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ComponentAsset]:
        """Return paginated, filtered collection of ComponentAsset entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_componentassets(self, query: str, limit: int = 50) -> List[ComponentAsset]:
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

    def update_componentasset(self, item_id: int, updates: Dict[str, Any]) -> Optional[ComponentAsset]:
        """Apply partial updates to existing ComponentAsset entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ComponentAsset record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_componentasset(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ComponentAsset record."""
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
        """Calculate operational and financial aggregate metrics for ComponentAsset."""
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

class DisposalProceedsService:
    """Core enterprise business service for managing DisposalProceeds entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, DisposalProceeds] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"DIS-{1000 + i}"
            item = DisposalProceeds(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise DisposalProceeds {i}",
                description=f"Primary operational DisposalProceeds record generated for organization unit 1.",
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

    def create_disposalproceeds(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> DisposalProceeds:
        """Create, validate, index, and commit new DisposalProceeds instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = DisposalProceeds(
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
        self._record_audit_event("CREATE", instance.id, f"Created DisposalProceeds {code}")
        logger.info(f"Created DisposalProceeds id={instance.id} code={code}")
        return instance

    def get_disposalproceeds_by_id(self, item_id: int) -> Optional[DisposalProceeds]:
        """Retrieve single DisposalProceeds by primary key identifier."""
        return self._cache.get(item_id)

    def get_disposalproceeds_by_code(self, code: str) -> Optional[DisposalProceeds]:
        """Lookup DisposalProceeds by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_disposalproceedss(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[DisposalProceeds]:
        """Return paginated, filtered collection of DisposalProceeds entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_disposalproceedss(self, query: str, limit: int = 50) -> List[DisposalProceeds]:
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

    def update_disposalproceeds(self, item_id: int, updates: Dict[str, Any]) -> Optional[DisposalProceeds]:
        """Apply partial updates to existing DisposalProceeds entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked DisposalProceeds record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_disposalproceeds(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of DisposalProceeds record."""
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
        """Calculate operational and financial aggregate metrics for DisposalProceeds."""
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

