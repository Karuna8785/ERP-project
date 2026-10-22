"""
Sales & Operations Planning (S&OP) - Business Logic Service Layer
"""
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import logging
from .models import RecordStatus, PriorityLevel, RiskClassification

from .models import DemandForecastPlan
from .models import SupplyConstraintModel
from .models import SafetyStockThreshold
from .models import ProductionCapacityLimit
from .models import LeadTimeVariability
from .models import MaterialRequirementPlan
from .models import DistributionPlan
from .models import StockAllocationRule
from .models import SupplierCommitment
from .models import ForecastAccuracyMetric
from .models import InventoryBufferZone
from .models import MasterProductionSchedule
from .models import BottleneckWorkstation
from .models import ScenarioComparison
from .models import ExpeditedShipmentOrder
from .models import ExecutiveSOPConsensus

logger = logging.getLogger("supply_chain_planning.services")

class DemandForecastPlanService:
    """Core enterprise business service for managing DemandForecastPlan entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, DemandForecastPlan] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"DEM-{1000 + i}"
            item = DemandForecastPlan(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise DemandForecastPlan {i}",
                description=f"Primary operational DemandForecastPlan record generated for organization unit 1.",
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

    def create_demandforecastplan(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> DemandForecastPlan:
        """Create, validate, index, and commit new DemandForecastPlan instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = DemandForecastPlan(
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
        self._record_audit_event("CREATE", instance.id, f"Created DemandForecastPlan {code}")
        logger.info(f"Created DemandForecastPlan id={instance.id} code={code}")
        return instance

    def get_demandforecastplan_by_id(self, item_id: int) -> Optional[DemandForecastPlan]:
        """Retrieve single DemandForecastPlan by primary key identifier."""
        return self._cache.get(item_id)

    def get_demandforecastplan_by_code(self, code: str) -> Optional[DemandForecastPlan]:
        """Lookup DemandForecastPlan by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_demandforecastplans(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[DemandForecastPlan]:
        """Return paginated, filtered collection of DemandForecastPlan entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_demandforecastplans(self, query: str, limit: int = 50) -> List[DemandForecastPlan]:
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

    def update_demandforecastplan(self, item_id: int, updates: Dict[str, Any]) -> Optional[DemandForecastPlan]:
        """Apply partial updates to existing DemandForecastPlan entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked DemandForecastPlan record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_demandforecastplan(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of DemandForecastPlan record."""
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
        """Calculate operational and financial aggregate metrics for DemandForecastPlan."""
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

class SupplyConstraintModelService:
    """Core enterprise business service for managing SupplyConstraintModel entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, SupplyConstraintModel] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SUP-{1000 + i}"
            item = SupplyConstraintModel(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise SupplyConstraintModel {i}",
                description=f"Primary operational SupplyConstraintModel record generated for organization unit 1.",
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

    def create_supplyconstraintmodel(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> SupplyConstraintModel:
        """Create, validate, index, and commit new SupplyConstraintModel instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = SupplyConstraintModel(
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
        self._record_audit_event("CREATE", instance.id, f"Created SupplyConstraintModel {code}")
        logger.info(f"Created SupplyConstraintModel id={instance.id} code={code}")
        return instance

    def get_supplyconstraintmodel_by_id(self, item_id: int) -> Optional[SupplyConstraintModel]:
        """Retrieve single SupplyConstraintModel by primary key identifier."""
        return self._cache.get(item_id)

    def get_supplyconstraintmodel_by_code(self, code: str) -> Optional[SupplyConstraintModel]:
        """Lookup SupplyConstraintModel by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_supplyconstraintmodels(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[SupplyConstraintModel]:
        """Return paginated, filtered collection of SupplyConstraintModel entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_supplyconstraintmodels(self, query: str, limit: int = 50) -> List[SupplyConstraintModel]:
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

    def update_supplyconstraintmodel(self, item_id: int, updates: Dict[str, Any]) -> Optional[SupplyConstraintModel]:
        """Apply partial updates to existing SupplyConstraintModel entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked SupplyConstraintModel record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_supplyconstraintmodel(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of SupplyConstraintModel record."""
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
        """Calculate operational and financial aggregate metrics for SupplyConstraintModel."""
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

class SafetyStockThresholdService:
    """Core enterprise business service for managing SafetyStockThreshold entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, SafetyStockThreshold] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SAF-{1000 + i}"
            item = SafetyStockThreshold(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise SafetyStockThreshold {i}",
                description=f"Primary operational SafetyStockThreshold record generated for organization unit 1.",
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

    def create_safetystockthreshold(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> SafetyStockThreshold:
        """Create, validate, index, and commit new SafetyStockThreshold instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = SafetyStockThreshold(
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
        self._record_audit_event("CREATE", instance.id, f"Created SafetyStockThreshold {code}")
        logger.info(f"Created SafetyStockThreshold id={instance.id} code={code}")
        return instance

    def get_safetystockthreshold_by_id(self, item_id: int) -> Optional[SafetyStockThreshold]:
        """Retrieve single SafetyStockThreshold by primary key identifier."""
        return self._cache.get(item_id)

    def get_safetystockthreshold_by_code(self, code: str) -> Optional[SafetyStockThreshold]:
        """Lookup SafetyStockThreshold by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_safetystockthresholds(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[SafetyStockThreshold]:
        """Return paginated, filtered collection of SafetyStockThreshold entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_safetystockthresholds(self, query: str, limit: int = 50) -> List[SafetyStockThreshold]:
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

    def update_safetystockthreshold(self, item_id: int, updates: Dict[str, Any]) -> Optional[SafetyStockThreshold]:
        """Apply partial updates to existing SafetyStockThreshold entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked SafetyStockThreshold record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_safetystockthreshold(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of SafetyStockThreshold record."""
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
        """Calculate operational and financial aggregate metrics for SafetyStockThreshold."""
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

class ProductionCapacityLimitService:
    """Core enterprise business service for managing ProductionCapacityLimit entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ProductionCapacityLimit] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"PRO-{1000 + i}"
            item = ProductionCapacityLimit(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ProductionCapacityLimit {i}",
                description=f"Primary operational ProductionCapacityLimit record generated for organization unit 1.",
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

    def create_productioncapacitylimit(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ProductionCapacityLimit:
        """Create, validate, index, and commit new ProductionCapacityLimit instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ProductionCapacityLimit(
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
        self._record_audit_event("CREATE", instance.id, f"Created ProductionCapacityLimit {code}")
        logger.info(f"Created ProductionCapacityLimit id={instance.id} code={code}")
        return instance

    def get_productioncapacitylimit_by_id(self, item_id: int) -> Optional[ProductionCapacityLimit]:
        """Retrieve single ProductionCapacityLimit by primary key identifier."""
        return self._cache.get(item_id)

    def get_productioncapacitylimit_by_code(self, code: str) -> Optional[ProductionCapacityLimit]:
        """Lookup ProductionCapacityLimit by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_productioncapacitylimits(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ProductionCapacityLimit]:
        """Return paginated, filtered collection of ProductionCapacityLimit entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_productioncapacitylimits(self, query: str, limit: int = 50) -> List[ProductionCapacityLimit]:
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

    def update_productioncapacitylimit(self, item_id: int, updates: Dict[str, Any]) -> Optional[ProductionCapacityLimit]:
        """Apply partial updates to existing ProductionCapacityLimit entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ProductionCapacityLimit record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_productioncapacitylimit(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ProductionCapacityLimit record."""
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
        """Calculate operational and financial aggregate metrics for ProductionCapacityLimit."""
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

class LeadTimeVariabilityService:
    """Core enterprise business service for managing LeadTimeVariability entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, LeadTimeVariability] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"LEA-{1000 + i}"
            item = LeadTimeVariability(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise LeadTimeVariability {i}",
                description=f"Primary operational LeadTimeVariability record generated for organization unit 1.",
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

    def create_leadtimevariability(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> LeadTimeVariability:
        """Create, validate, index, and commit new LeadTimeVariability instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = LeadTimeVariability(
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
        self._record_audit_event("CREATE", instance.id, f"Created LeadTimeVariability {code}")
        logger.info(f"Created LeadTimeVariability id={instance.id} code={code}")
        return instance

    def get_leadtimevariability_by_id(self, item_id: int) -> Optional[LeadTimeVariability]:
        """Retrieve single LeadTimeVariability by primary key identifier."""
        return self._cache.get(item_id)

    def get_leadtimevariability_by_code(self, code: str) -> Optional[LeadTimeVariability]:
        """Lookup LeadTimeVariability by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_leadtimevariabilitys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[LeadTimeVariability]:
        """Return paginated, filtered collection of LeadTimeVariability entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_leadtimevariabilitys(self, query: str, limit: int = 50) -> List[LeadTimeVariability]:
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

    def update_leadtimevariability(self, item_id: int, updates: Dict[str, Any]) -> Optional[LeadTimeVariability]:
        """Apply partial updates to existing LeadTimeVariability entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked LeadTimeVariability record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_leadtimevariability(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of LeadTimeVariability record."""
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
        """Calculate operational and financial aggregate metrics for LeadTimeVariability."""
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

class MaterialRequirementPlanService:
    """Core enterprise business service for managing MaterialRequirementPlan entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, MaterialRequirementPlan] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"MAT-{1000 + i}"
            item = MaterialRequirementPlan(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise MaterialRequirementPlan {i}",
                description=f"Primary operational MaterialRequirementPlan record generated for organization unit 1.",
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

    def create_materialrequirementplan(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> MaterialRequirementPlan:
        """Create, validate, index, and commit new MaterialRequirementPlan instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = MaterialRequirementPlan(
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
        self._record_audit_event("CREATE", instance.id, f"Created MaterialRequirementPlan {code}")
        logger.info(f"Created MaterialRequirementPlan id={instance.id} code={code}")
        return instance

    def get_materialrequirementplan_by_id(self, item_id: int) -> Optional[MaterialRequirementPlan]:
        """Retrieve single MaterialRequirementPlan by primary key identifier."""
        return self._cache.get(item_id)

    def get_materialrequirementplan_by_code(self, code: str) -> Optional[MaterialRequirementPlan]:
        """Lookup MaterialRequirementPlan by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_materialrequirementplans(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[MaterialRequirementPlan]:
        """Return paginated, filtered collection of MaterialRequirementPlan entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_materialrequirementplans(self, query: str, limit: int = 50) -> List[MaterialRequirementPlan]:
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

    def update_materialrequirementplan(self, item_id: int, updates: Dict[str, Any]) -> Optional[MaterialRequirementPlan]:
        """Apply partial updates to existing MaterialRequirementPlan entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked MaterialRequirementPlan record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_materialrequirementplan(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of MaterialRequirementPlan record."""
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
        """Calculate operational and financial aggregate metrics for MaterialRequirementPlan."""
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

class DistributionPlanService:
    """Core enterprise business service for managing DistributionPlan entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, DistributionPlan] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"DIS-{1000 + i}"
            item = DistributionPlan(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise DistributionPlan {i}",
                description=f"Primary operational DistributionPlan record generated for organization unit 1.",
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

    def create_distributionplan(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> DistributionPlan:
        """Create, validate, index, and commit new DistributionPlan instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = DistributionPlan(
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
        self._record_audit_event("CREATE", instance.id, f"Created DistributionPlan {code}")
        logger.info(f"Created DistributionPlan id={instance.id} code={code}")
        return instance

    def get_distributionplan_by_id(self, item_id: int) -> Optional[DistributionPlan]:
        """Retrieve single DistributionPlan by primary key identifier."""
        return self._cache.get(item_id)

    def get_distributionplan_by_code(self, code: str) -> Optional[DistributionPlan]:
        """Lookup DistributionPlan by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_distributionplans(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[DistributionPlan]:
        """Return paginated, filtered collection of DistributionPlan entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_distributionplans(self, query: str, limit: int = 50) -> List[DistributionPlan]:
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

    def update_distributionplan(self, item_id: int, updates: Dict[str, Any]) -> Optional[DistributionPlan]:
        """Apply partial updates to existing DistributionPlan entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked DistributionPlan record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_distributionplan(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of DistributionPlan record."""
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
        """Calculate operational and financial aggregate metrics for DistributionPlan."""
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

class StockAllocationRuleService:
    """Core enterprise business service for managing StockAllocationRule entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, StockAllocationRule] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"STO-{1000 + i}"
            item = StockAllocationRule(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise StockAllocationRule {i}",
                description=f"Primary operational StockAllocationRule record generated for organization unit 1.",
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

    def create_stockallocationrule(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> StockAllocationRule:
        """Create, validate, index, and commit new StockAllocationRule instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = StockAllocationRule(
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
        self._record_audit_event("CREATE", instance.id, f"Created StockAllocationRule {code}")
        logger.info(f"Created StockAllocationRule id={instance.id} code={code}")
        return instance

    def get_stockallocationrule_by_id(self, item_id: int) -> Optional[StockAllocationRule]:
        """Retrieve single StockAllocationRule by primary key identifier."""
        return self._cache.get(item_id)

    def get_stockallocationrule_by_code(self, code: str) -> Optional[StockAllocationRule]:
        """Lookup StockAllocationRule by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_stockallocationrules(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[StockAllocationRule]:
        """Return paginated, filtered collection of StockAllocationRule entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_stockallocationrules(self, query: str, limit: int = 50) -> List[StockAllocationRule]:
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

    def update_stockallocationrule(self, item_id: int, updates: Dict[str, Any]) -> Optional[StockAllocationRule]:
        """Apply partial updates to existing StockAllocationRule entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked StockAllocationRule record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_stockallocationrule(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of StockAllocationRule record."""
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
        """Calculate operational and financial aggregate metrics for StockAllocationRule."""
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

class SupplierCommitmentService:
    """Core enterprise business service for managing SupplierCommitment entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, SupplierCommitment] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SUP-{1000 + i}"
            item = SupplierCommitment(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise SupplierCommitment {i}",
                description=f"Primary operational SupplierCommitment record generated for organization unit 1.",
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

    def create_suppliercommitment(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> SupplierCommitment:
        """Create, validate, index, and commit new SupplierCommitment instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = SupplierCommitment(
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
        self._record_audit_event("CREATE", instance.id, f"Created SupplierCommitment {code}")
        logger.info(f"Created SupplierCommitment id={instance.id} code={code}")
        return instance

    def get_suppliercommitment_by_id(self, item_id: int) -> Optional[SupplierCommitment]:
        """Retrieve single SupplierCommitment by primary key identifier."""
        return self._cache.get(item_id)

    def get_suppliercommitment_by_code(self, code: str) -> Optional[SupplierCommitment]:
        """Lookup SupplierCommitment by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_suppliercommitments(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[SupplierCommitment]:
        """Return paginated, filtered collection of SupplierCommitment entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_suppliercommitments(self, query: str, limit: int = 50) -> List[SupplierCommitment]:
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

    def update_suppliercommitment(self, item_id: int, updates: Dict[str, Any]) -> Optional[SupplierCommitment]:
        """Apply partial updates to existing SupplierCommitment entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked SupplierCommitment record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_suppliercommitment(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of SupplierCommitment record."""
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
        """Calculate operational and financial aggregate metrics for SupplierCommitment."""
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

class ForecastAccuracyMetricService:
    """Core enterprise business service for managing ForecastAccuracyMetric entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ForecastAccuracyMetric] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"FOR-{1000 + i}"
            item = ForecastAccuracyMetric(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ForecastAccuracyMetric {i}",
                description=f"Primary operational ForecastAccuracyMetric record generated for organization unit 1.",
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

    def create_forecastaccuracymetric(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ForecastAccuracyMetric:
        """Create, validate, index, and commit new ForecastAccuracyMetric instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ForecastAccuracyMetric(
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
        self._record_audit_event("CREATE", instance.id, f"Created ForecastAccuracyMetric {code}")
        logger.info(f"Created ForecastAccuracyMetric id={instance.id} code={code}")
        return instance

    def get_forecastaccuracymetric_by_id(self, item_id: int) -> Optional[ForecastAccuracyMetric]:
        """Retrieve single ForecastAccuracyMetric by primary key identifier."""
        return self._cache.get(item_id)

    def get_forecastaccuracymetric_by_code(self, code: str) -> Optional[ForecastAccuracyMetric]:
        """Lookup ForecastAccuracyMetric by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_forecastaccuracymetrics(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ForecastAccuracyMetric]:
        """Return paginated, filtered collection of ForecastAccuracyMetric entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_forecastaccuracymetrics(self, query: str, limit: int = 50) -> List[ForecastAccuracyMetric]:
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

    def update_forecastaccuracymetric(self, item_id: int, updates: Dict[str, Any]) -> Optional[ForecastAccuracyMetric]:
        """Apply partial updates to existing ForecastAccuracyMetric entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ForecastAccuracyMetric record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_forecastaccuracymetric(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ForecastAccuracyMetric record."""
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
        """Calculate operational and financial aggregate metrics for ForecastAccuracyMetric."""
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

class InventoryBufferZoneService:
    """Core enterprise business service for managing InventoryBufferZone entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, InventoryBufferZone] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"INV-{1000 + i}"
            item = InventoryBufferZone(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise InventoryBufferZone {i}",
                description=f"Primary operational InventoryBufferZone record generated for organization unit 1.",
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

    def create_inventorybufferzone(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> InventoryBufferZone:
        """Create, validate, index, and commit new InventoryBufferZone instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = InventoryBufferZone(
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
        self._record_audit_event("CREATE", instance.id, f"Created InventoryBufferZone {code}")
        logger.info(f"Created InventoryBufferZone id={instance.id} code={code}")
        return instance

    def get_inventorybufferzone_by_id(self, item_id: int) -> Optional[InventoryBufferZone]:
        """Retrieve single InventoryBufferZone by primary key identifier."""
        return self._cache.get(item_id)

    def get_inventorybufferzone_by_code(self, code: str) -> Optional[InventoryBufferZone]:
        """Lookup InventoryBufferZone by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_inventorybufferzones(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[InventoryBufferZone]:
        """Return paginated, filtered collection of InventoryBufferZone entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_inventorybufferzones(self, query: str, limit: int = 50) -> List[InventoryBufferZone]:
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

    def update_inventorybufferzone(self, item_id: int, updates: Dict[str, Any]) -> Optional[InventoryBufferZone]:
        """Apply partial updates to existing InventoryBufferZone entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked InventoryBufferZone record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_inventorybufferzone(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of InventoryBufferZone record."""
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
        """Calculate operational and financial aggregate metrics for InventoryBufferZone."""
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

class MasterProductionScheduleService:
    """Core enterprise business service for managing MasterProductionSchedule entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, MasterProductionSchedule] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"MAS-{1000 + i}"
            item = MasterProductionSchedule(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise MasterProductionSchedule {i}",
                description=f"Primary operational MasterProductionSchedule record generated for organization unit 1.",
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

    def create_masterproductionschedule(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> MasterProductionSchedule:
        """Create, validate, index, and commit new MasterProductionSchedule instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = MasterProductionSchedule(
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
        self._record_audit_event("CREATE", instance.id, f"Created MasterProductionSchedule {code}")
        logger.info(f"Created MasterProductionSchedule id={instance.id} code={code}")
        return instance

    def get_masterproductionschedule_by_id(self, item_id: int) -> Optional[MasterProductionSchedule]:
        """Retrieve single MasterProductionSchedule by primary key identifier."""
        return self._cache.get(item_id)

    def get_masterproductionschedule_by_code(self, code: str) -> Optional[MasterProductionSchedule]:
        """Lookup MasterProductionSchedule by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_masterproductionschedules(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[MasterProductionSchedule]:
        """Return paginated, filtered collection of MasterProductionSchedule entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_masterproductionschedules(self, query: str, limit: int = 50) -> List[MasterProductionSchedule]:
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

    def update_masterproductionschedule(self, item_id: int, updates: Dict[str, Any]) -> Optional[MasterProductionSchedule]:
        """Apply partial updates to existing MasterProductionSchedule entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked MasterProductionSchedule record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_masterproductionschedule(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of MasterProductionSchedule record."""
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
        """Calculate operational and financial aggregate metrics for MasterProductionSchedule."""
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

class BottleneckWorkstationService:
    """Core enterprise business service for managing BottleneckWorkstation entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, BottleneckWorkstation] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"BOT-{1000 + i}"
            item = BottleneckWorkstation(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise BottleneckWorkstation {i}",
                description=f"Primary operational BottleneckWorkstation record generated for organization unit 1.",
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

    def create_bottleneckworkstation(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> BottleneckWorkstation:
        """Create, validate, index, and commit new BottleneckWorkstation instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = BottleneckWorkstation(
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
        self._record_audit_event("CREATE", instance.id, f"Created BottleneckWorkstation {code}")
        logger.info(f"Created BottleneckWorkstation id={instance.id} code={code}")
        return instance

    def get_bottleneckworkstation_by_id(self, item_id: int) -> Optional[BottleneckWorkstation]:
        """Retrieve single BottleneckWorkstation by primary key identifier."""
        return self._cache.get(item_id)

    def get_bottleneckworkstation_by_code(self, code: str) -> Optional[BottleneckWorkstation]:
        """Lookup BottleneckWorkstation by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_bottleneckworkstations(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[BottleneckWorkstation]:
        """Return paginated, filtered collection of BottleneckWorkstation entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_bottleneckworkstations(self, query: str, limit: int = 50) -> List[BottleneckWorkstation]:
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

    def update_bottleneckworkstation(self, item_id: int, updates: Dict[str, Any]) -> Optional[BottleneckWorkstation]:
        """Apply partial updates to existing BottleneckWorkstation entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked BottleneckWorkstation record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_bottleneckworkstation(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of BottleneckWorkstation record."""
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
        """Calculate operational and financial aggregate metrics for BottleneckWorkstation."""
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

class ScenarioComparisonService:
    """Core enterprise business service for managing ScenarioComparison entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ScenarioComparison] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SCE-{1000 + i}"
            item = ScenarioComparison(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ScenarioComparison {i}",
                description=f"Primary operational ScenarioComparison record generated for organization unit 1.",
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

    def create_scenariocomparison(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ScenarioComparison:
        """Create, validate, index, and commit new ScenarioComparison instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ScenarioComparison(
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
        self._record_audit_event("CREATE", instance.id, f"Created ScenarioComparison {code}")
        logger.info(f"Created ScenarioComparison id={instance.id} code={code}")
        return instance

    def get_scenariocomparison_by_id(self, item_id: int) -> Optional[ScenarioComparison]:
        """Retrieve single ScenarioComparison by primary key identifier."""
        return self._cache.get(item_id)

    def get_scenariocomparison_by_code(self, code: str) -> Optional[ScenarioComparison]:
        """Lookup ScenarioComparison by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_scenariocomparisons(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ScenarioComparison]:
        """Return paginated, filtered collection of ScenarioComparison entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_scenariocomparisons(self, query: str, limit: int = 50) -> List[ScenarioComparison]:
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

    def update_scenariocomparison(self, item_id: int, updates: Dict[str, Any]) -> Optional[ScenarioComparison]:
        """Apply partial updates to existing ScenarioComparison entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ScenarioComparison record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_scenariocomparison(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ScenarioComparison record."""
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
        """Calculate operational and financial aggregate metrics for ScenarioComparison."""
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

class ExpeditedShipmentOrderService:
    """Core enterprise business service for managing ExpeditedShipmentOrder entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ExpeditedShipmentOrder] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"EXP-{1000 + i}"
            item = ExpeditedShipmentOrder(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ExpeditedShipmentOrder {i}",
                description=f"Primary operational ExpeditedShipmentOrder record generated for organization unit 1.",
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

    def create_expeditedshipmentorder(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ExpeditedShipmentOrder:
        """Create, validate, index, and commit new ExpeditedShipmentOrder instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ExpeditedShipmentOrder(
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
        self._record_audit_event("CREATE", instance.id, f"Created ExpeditedShipmentOrder {code}")
        logger.info(f"Created ExpeditedShipmentOrder id={instance.id} code={code}")
        return instance

    def get_expeditedshipmentorder_by_id(self, item_id: int) -> Optional[ExpeditedShipmentOrder]:
        """Retrieve single ExpeditedShipmentOrder by primary key identifier."""
        return self._cache.get(item_id)

    def get_expeditedshipmentorder_by_code(self, code: str) -> Optional[ExpeditedShipmentOrder]:
        """Lookup ExpeditedShipmentOrder by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_expeditedshipmentorders(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ExpeditedShipmentOrder]:
        """Return paginated, filtered collection of ExpeditedShipmentOrder entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_expeditedshipmentorders(self, query: str, limit: int = 50) -> List[ExpeditedShipmentOrder]:
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

    def update_expeditedshipmentorder(self, item_id: int, updates: Dict[str, Any]) -> Optional[ExpeditedShipmentOrder]:
        """Apply partial updates to existing ExpeditedShipmentOrder entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ExpeditedShipmentOrder record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_expeditedshipmentorder(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ExpeditedShipmentOrder record."""
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
        """Calculate operational and financial aggregate metrics for ExpeditedShipmentOrder."""
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

class ExecutiveSOPConsensusService:
    """Core enterprise business service for managing ExecutiveSOPConsensus entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ExecutiveSOPConsensus] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"EXE-{1000 + i}"
            item = ExecutiveSOPConsensus(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ExecutiveSOPConsensus {i}",
                description=f"Primary operational ExecutiveSOPConsensus record generated for organization unit 1.",
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

    def create_executivesopconsensus(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ExecutiveSOPConsensus:
        """Create, validate, index, and commit new ExecutiveSOPConsensus instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ExecutiveSOPConsensus(
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
        self._record_audit_event("CREATE", instance.id, f"Created ExecutiveSOPConsensus {code}")
        logger.info(f"Created ExecutiveSOPConsensus id={instance.id} code={code}")
        return instance

    def get_executivesopconsensus_by_id(self, item_id: int) -> Optional[ExecutiveSOPConsensus]:
        """Retrieve single ExecutiveSOPConsensus by primary key identifier."""
        return self._cache.get(item_id)

    def get_executivesopconsensus_by_code(self, code: str) -> Optional[ExecutiveSOPConsensus]:
        """Lookup ExecutiveSOPConsensus by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_executivesopconsensuss(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ExecutiveSOPConsensus]:
        """Return paginated, filtered collection of ExecutiveSOPConsensus entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_executivesopconsensuss(self, query: str, limit: int = 50) -> List[ExecutiveSOPConsensus]:
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

    def update_executivesopconsensus(self, item_id: int, updates: Dict[str, Any]) -> Optional[ExecutiveSOPConsensus]:
        """Apply partial updates to existing ExecutiveSOPConsensus entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ExecutiveSOPConsensus record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_executivesopconsensus(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ExecutiveSOPConsensus record."""
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
        """Calculate operational and financial aggregate metrics for ExecutiveSOPConsensus."""
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

