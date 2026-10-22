"""
Multi-Entity Financial Consolidation & Reporting - Business Logic Service Layer
"""
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import logging
from .models import RecordStatus, PriorityLevel, RiskClassification

from .models import ConsolidationEntityGroup
from .models import IntercompanyEliminationEntry
from .models import ConsolidatedTrialBalance
from .models import CurrencyTranslationRate
from .models import MinorityInterestShare
from .models import JointVentureEquityShare
from .models import FinancialAdjustmentVoucher
from .models import GoodwillImpairmentSchedule
from .models import SegmentalReportingUnit
from .models import ConsolidatedCashFlow
from .models import StatutoryBalanceSheet
from .models import ConsolidatedIncomeStatement
from .models import AuditTrailElimination
from .models import TaxProvisioningConsolidated
from .models import FinancialClosingChecklist
from .models import ExecutiveBoardFinancialReport

logger = logging.getLogger("financial_consolidation.services")

class ConsolidationEntityGroupService:
    """Core enterprise business service for managing ConsolidationEntityGroup entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ConsolidationEntityGroup] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CON-{1000 + i}"
            item = ConsolidationEntityGroup(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ConsolidationEntityGroup {i}",
                description=f"Primary operational ConsolidationEntityGroup record generated for organization unit 1.",
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

    def create_consolidationentitygroup(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ConsolidationEntityGroup:
        """Create, validate, index, and commit new ConsolidationEntityGroup instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ConsolidationEntityGroup(
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
        self._record_audit_event("CREATE", instance.id, f"Created ConsolidationEntityGroup {code}")
        logger.info(f"Created ConsolidationEntityGroup id={instance.id} code={code}")
        return instance

    def get_consolidationentitygroup_by_id(self, item_id: int) -> Optional[ConsolidationEntityGroup]:
        """Retrieve single ConsolidationEntityGroup by primary key identifier."""
        return self._cache.get(item_id)

    def get_consolidationentitygroup_by_code(self, code: str) -> Optional[ConsolidationEntityGroup]:
        """Lookup ConsolidationEntityGroup by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_consolidationentitygroups(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ConsolidationEntityGroup]:
        """Return paginated, filtered collection of ConsolidationEntityGroup entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_consolidationentitygroups(self, query: str, limit: int = 50) -> List[ConsolidationEntityGroup]:
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

    def update_consolidationentitygroup(self, item_id: int, updates: Dict[str, Any]) -> Optional[ConsolidationEntityGroup]:
        """Apply partial updates to existing ConsolidationEntityGroup entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ConsolidationEntityGroup record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_consolidationentitygroup(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ConsolidationEntityGroup record."""
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
        """Calculate operational and financial aggregate metrics for ConsolidationEntityGroup."""
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

class IntercompanyEliminationEntryService:
    """Core enterprise business service for managing IntercompanyEliminationEntry entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, IntercompanyEliminationEntry] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"INT-{1000 + i}"
            item = IntercompanyEliminationEntry(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise IntercompanyEliminationEntry {i}",
                description=f"Primary operational IntercompanyEliminationEntry record generated for organization unit 1.",
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

    def create_intercompanyeliminationentry(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> IntercompanyEliminationEntry:
        """Create, validate, index, and commit new IntercompanyEliminationEntry instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = IntercompanyEliminationEntry(
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
        self._record_audit_event("CREATE", instance.id, f"Created IntercompanyEliminationEntry {code}")
        logger.info(f"Created IntercompanyEliminationEntry id={instance.id} code={code}")
        return instance

    def get_intercompanyeliminationentry_by_id(self, item_id: int) -> Optional[IntercompanyEliminationEntry]:
        """Retrieve single IntercompanyEliminationEntry by primary key identifier."""
        return self._cache.get(item_id)

    def get_intercompanyeliminationentry_by_code(self, code: str) -> Optional[IntercompanyEliminationEntry]:
        """Lookup IntercompanyEliminationEntry by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_intercompanyeliminationentrys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[IntercompanyEliminationEntry]:
        """Return paginated, filtered collection of IntercompanyEliminationEntry entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_intercompanyeliminationentrys(self, query: str, limit: int = 50) -> List[IntercompanyEliminationEntry]:
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

    def update_intercompanyeliminationentry(self, item_id: int, updates: Dict[str, Any]) -> Optional[IntercompanyEliminationEntry]:
        """Apply partial updates to existing IntercompanyEliminationEntry entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked IntercompanyEliminationEntry record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_intercompanyeliminationentry(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of IntercompanyEliminationEntry record."""
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
        """Calculate operational and financial aggregate metrics for IntercompanyEliminationEntry."""
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

class ConsolidatedTrialBalanceService:
    """Core enterprise business service for managing ConsolidatedTrialBalance entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ConsolidatedTrialBalance] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CON-{1000 + i}"
            item = ConsolidatedTrialBalance(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ConsolidatedTrialBalance {i}",
                description=f"Primary operational ConsolidatedTrialBalance record generated for organization unit 1.",
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

    def create_consolidatedtrialbalance(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ConsolidatedTrialBalance:
        """Create, validate, index, and commit new ConsolidatedTrialBalance instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ConsolidatedTrialBalance(
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
        self._record_audit_event("CREATE", instance.id, f"Created ConsolidatedTrialBalance {code}")
        logger.info(f"Created ConsolidatedTrialBalance id={instance.id} code={code}")
        return instance

    def get_consolidatedtrialbalance_by_id(self, item_id: int) -> Optional[ConsolidatedTrialBalance]:
        """Retrieve single ConsolidatedTrialBalance by primary key identifier."""
        return self._cache.get(item_id)

    def get_consolidatedtrialbalance_by_code(self, code: str) -> Optional[ConsolidatedTrialBalance]:
        """Lookup ConsolidatedTrialBalance by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_consolidatedtrialbalances(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ConsolidatedTrialBalance]:
        """Return paginated, filtered collection of ConsolidatedTrialBalance entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_consolidatedtrialbalances(self, query: str, limit: int = 50) -> List[ConsolidatedTrialBalance]:
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

    def update_consolidatedtrialbalance(self, item_id: int, updates: Dict[str, Any]) -> Optional[ConsolidatedTrialBalance]:
        """Apply partial updates to existing ConsolidatedTrialBalance entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ConsolidatedTrialBalance record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_consolidatedtrialbalance(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ConsolidatedTrialBalance record."""
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
        """Calculate operational and financial aggregate metrics for ConsolidatedTrialBalance."""
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

class CurrencyTranslationRateService:
    """Core enterprise business service for managing CurrencyTranslationRate entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, CurrencyTranslationRate] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CUR-{1000 + i}"
            item = CurrencyTranslationRate(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise CurrencyTranslationRate {i}",
                description=f"Primary operational CurrencyTranslationRate record generated for organization unit 1.",
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

    def create_currencytranslationrate(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> CurrencyTranslationRate:
        """Create, validate, index, and commit new CurrencyTranslationRate instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = CurrencyTranslationRate(
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
        self._record_audit_event("CREATE", instance.id, f"Created CurrencyTranslationRate {code}")
        logger.info(f"Created CurrencyTranslationRate id={instance.id} code={code}")
        return instance

    def get_currencytranslationrate_by_id(self, item_id: int) -> Optional[CurrencyTranslationRate]:
        """Retrieve single CurrencyTranslationRate by primary key identifier."""
        return self._cache.get(item_id)

    def get_currencytranslationrate_by_code(self, code: str) -> Optional[CurrencyTranslationRate]:
        """Lookup CurrencyTranslationRate by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_currencytranslationrates(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[CurrencyTranslationRate]:
        """Return paginated, filtered collection of CurrencyTranslationRate entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_currencytranslationrates(self, query: str, limit: int = 50) -> List[CurrencyTranslationRate]:
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

    def update_currencytranslationrate(self, item_id: int, updates: Dict[str, Any]) -> Optional[CurrencyTranslationRate]:
        """Apply partial updates to existing CurrencyTranslationRate entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked CurrencyTranslationRate record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_currencytranslationrate(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of CurrencyTranslationRate record."""
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
        """Calculate operational and financial aggregate metrics for CurrencyTranslationRate."""
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

class MinorityInterestShareService:
    """Core enterprise business service for managing MinorityInterestShare entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, MinorityInterestShare] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"MIN-{1000 + i}"
            item = MinorityInterestShare(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise MinorityInterestShare {i}",
                description=f"Primary operational MinorityInterestShare record generated for organization unit 1.",
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

    def create_minorityinterestshare(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> MinorityInterestShare:
        """Create, validate, index, and commit new MinorityInterestShare instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = MinorityInterestShare(
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
        self._record_audit_event("CREATE", instance.id, f"Created MinorityInterestShare {code}")
        logger.info(f"Created MinorityInterestShare id={instance.id} code={code}")
        return instance

    def get_minorityinterestshare_by_id(self, item_id: int) -> Optional[MinorityInterestShare]:
        """Retrieve single MinorityInterestShare by primary key identifier."""
        return self._cache.get(item_id)

    def get_minorityinterestshare_by_code(self, code: str) -> Optional[MinorityInterestShare]:
        """Lookup MinorityInterestShare by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_minorityinterestshares(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[MinorityInterestShare]:
        """Return paginated, filtered collection of MinorityInterestShare entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_minorityinterestshares(self, query: str, limit: int = 50) -> List[MinorityInterestShare]:
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

    def update_minorityinterestshare(self, item_id: int, updates: Dict[str, Any]) -> Optional[MinorityInterestShare]:
        """Apply partial updates to existing MinorityInterestShare entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked MinorityInterestShare record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_minorityinterestshare(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of MinorityInterestShare record."""
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
        """Calculate operational and financial aggregate metrics for MinorityInterestShare."""
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

class JointVentureEquityShareService:
    """Core enterprise business service for managing JointVentureEquityShare entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, JointVentureEquityShare] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"JOI-{1000 + i}"
            item = JointVentureEquityShare(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise JointVentureEquityShare {i}",
                description=f"Primary operational JointVentureEquityShare record generated for organization unit 1.",
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

    def create_jointventureequityshare(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> JointVentureEquityShare:
        """Create, validate, index, and commit new JointVentureEquityShare instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = JointVentureEquityShare(
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
        self._record_audit_event("CREATE", instance.id, f"Created JointVentureEquityShare {code}")
        logger.info(f"Created JointVentureEquityShare id={instance.id} code={code}")
        return instance

    def get_jointventureequityshare_by_id(self, item_id: int) -> Optional[JointVentureEquityShare]:
        """Retrieve single JointVentureEquityShare by primary key identifier."""
        return self._cache.get(item_id)

    def get_jointventureequityshare_by_code(self, code: str) -> Optional[JointVentureEquityShare]:
        """Lookup JointVentureEquityShare by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_jointventureequityshares(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[JointVentureEquityShare]:
        """Return paginated, filtered collection of JointVentureEquityShare entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_jointventureequityshares(self, query: str, limit: int = 50) -> List[JointVentureEquityShare]:
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

    def update_jointventureequityshare(self, item_id: int, updates: Dict[str, Any]) -> Optional[JointVentureEquityShare]:
        """Apply partial updates to existing JointVentureEquityShare entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked JointVentureEquityShare record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_jointventureequityshare(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of JointVentureEquityShare record."""
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
        """Calculate operational and financial aggregate metrics for JointVentureEquityShare."""
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

class FinancialAdjustmentVoucherService:
    """Core enterprise business service for managing FinancialAdjustmentVoucher entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, FinancialAdjustmentVoucher] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"FIN-{1000 + i}"
            item = FinancialAdjustmentVoucher(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise FinancialAdjustmentVoucher {i}",
                description=f"Primary operational FinancialAdjustmentVoucher record generated for organization unit 1.",
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

    def create_financialadjustmentvoucher(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> FinancialAdjustmentVoucher:
        """Create, validate, index, and commit new FinancialAdjustmentVoucher instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = FinancialAdjustmentVoucher(
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
        self._record_audit_event("CREATE", instance.id, f"Created FinancialAdjustmentVoucher {code}")
        logger.info(f"Created FinancialAdjustmentVoucher id={instance.id} code={code}")
        return instance

    def get_financialadjustmentvoucher_by_id(self, item_id: int) -> Optional[FinancialAdjustmentVoucher]:
        """Retrieve single FinancialAdjustmentVoucher by primary key identifier."""
        return self._cache.get(item_id)

    def get_financialadjustmentvoucher_by_code(self, code: str) -> Optional[FinancialAdjustmentVoucher]:
        """Lookup FinancialAdjustmentVoucher by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_financialadjustmentvouchers(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[FinancialAdjustmentVoucher]:
        """Return paginated, filtered collection of FinancialAdjustmentVoucher entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_financialadjustmentvouchers(self, query: str, limit: int = 50) -> List[FinancialAdjustmentVoucher]:
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

    def update_financialadjustmentvoucher(self, item_id: int, updates: Dict[str, Any]) -> Optional[FinancialAdjustmentVoucher]:
        """Apply partial updates to existing FinancialAdjustmentVoucher entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked FinancialAdjustmentVoucher record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_financialadjustmentvoucher(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of FinancialAdjustmentVoucher record."""
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
        """Calculate operational and financial aggregate metrics for FinancialAdjustmentVoucher."""
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

class GoodwillImpairmentScheduleService:
    """Core enterprise business service for managing GoodwillImpairmentSchedule entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, GoodwillImpairmentSchedule] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"GOO-{1000 + i}"
            item = GoodwillImpairmentSchedule(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise GoodwillImpairmentSchedule {i}",
                description=f"Primary operational GoodwillImpairmentSchedule record generated for organization unit 1.",
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

    def create_goodwillimpairmentschedule(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> GoodwillImpairmentSchedule:
        """Create, validate, index, and commit new GoodwillImpairmentSchedule instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = GoodwillImpairmentSchedule(
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
        self._record_audit_event("CREATE", instance.id, f"Created GoodwillImpairmentSchedule {code}")
        logger.info(f"Created GoodwillImpairmentSchedule id={instance.id} code={code}")
        return instance

    def get_goodwillimpairmentschedule_by_id(self, item_id: int) -> Optional[GoodwillImpairmentSchedule]:
        """Retrieve single GoodwillImpairmentSchedule by primary key identifier."""
        return self._cache.get(item_id)

    def get_goodwillimpairmentschedule_by_code(self, code: str) -> Optional[GoodwillImpairmentSchedule]:
        """Lookup GoodwillImpairmentSchedule by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_goodwillimpairmentschedules(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[GoodwillImpairmentSchedule]:
        """Return paginated, filtered collection of GoodwillImpairmentSchedule entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_goodwillimpairmentschedules(self, query: str, limit: int = 50) -> List[GoodwillImpairmentSchedule]:
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

    def update_goodwillimpairmentschedule(self, item_id: int, updates: Dict[str, Any]) -> Optional[GoodwillImpairmentSchedule]:
        """Apply partial updates to existing GoodwillImpairmentSchedule entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked GoodwillImpairmentSchedule record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_goodwillimpairmentschedule(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of GoodwillImpairmentSchedule record."""
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
        """Calculate operational and financial aggregate metrics for GoodwillImpairmentSchedule."""
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

class SegmentalReportingUnitService:
    """Core enterprise business service for managing SegmentalReportingUnit entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, SegmentalReportingUnit] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"SEG-{1000 + i}"
            item = SegmentalReportingUnit(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise SegmentalReportingUnit {i}",
                description=f"Primary operational SegmentalReportingUnit record generated for organization unit 1.",
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

    def create_segmentalreportingunit(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> SegmentalReportingUnit:
        """Create, validate, index, and commit new SegmentalReportingUnit instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = SegmentalReportingUnit(
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
        self._record_audit_event("CREATE", instance.id, f"Created SegmentalReportingUnit {code}")
        logger.info(f"Created SegmentalReportingUnit id={instance.id} code={code}")
        return instance

    def get_segmentalreportingunit_by_id(self, item_id: int) -> Optional[SegmentalReportingUnit]:
        """Retrieve single SegmentalReportingUnit by primary key identifier."""
        return self._cache.get(item_id)

    def get_segmentalreportingunit_by_code(self, code: str) -> Optional[SegmentalReportingUnit]:
        """Lookup SegmentalReportingUnit by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_segmentalreportingunits(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[SegmentalReportingUnit]:
        """Return paginated, filtered collection of SegmentalReportingUnit entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_segmentalreportingunits(self, query: str, limit: int = 50) -> List[SegmentalReportingUnit]:
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

    def update_segmentalreportingunit(self, item_id: int, updates: Dict[str, Any]) -> Optional[SegmentalReportingUnit]:
        """Apply partial updates to existing SegmentalReportingUnit entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked SegmentalReportingUnit record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_segmentalreportingunit(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of SegmentalReportingUnit record."""
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
        """Calculate operational and financial aggregate metrics for SegmentalReportingUnit."""
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

class ConsolidatedCashFlowService:
    """Core enterprise business service for managing ConsolidatedCashFlow entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ConsolidatedCashFlow] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CON-{1000 + i}"
            item = ConsolidatedCashFlow(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ConsolidatedCashFlow {i}",
                description=f"Primary operational ConsolidatedCashFlow record generated for organization unit 1.",
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

    def create_consolidatedcashflow(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ConsolidatedCashFlow:
        """Create, validate, index, and commit new ConsolidatedCashFlow instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ConsolidatedCashFlow(
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
        self._record_audit_event("CREATE", instance.id, f"Created ConsolidatedCashFlow {code}")
        logger.info(f"Created ConsolidatedCashFlow id={instance.id} code={code}")
        return instance

    def get_consolidatedcashflow_by_id(self, item_id: int) -> Optional[ConsolidatedCashFlow]:
        """Retrieve single ConsolidatedCashFlow by primary key identifier."""
        return self._cache.get(item_id)

    def get_consolidatedcashflow_by_code(self, code: str) -> Optional[ConsolidatedCashFlow]:
        """Lookup ConsolidatedCashFlow by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_consolidatedcashflows(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ConsolidatedCashFlow]:
        """Return paginated, filtered collection of ConsolidatedCashFlow entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_consolidatedcashflows(self, query: str, limit: int = 50) -> List[ConsolidatedCashFlow]:
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

    def update_consolidatedcashflow(self, item_id: int, updates: Dict[str, Any]) -> Optional[ConsolidatedCashFlow]:
        """Apply partial updates to existing ConsolidatedCashFlow entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ConsolidatedCashFlow record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_consolidatedcashflow(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ConsolidatedCashFlow record."""
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
        """Calculate operational and financial aggregate metrics for ConsolidatedCashFlow."""
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

class StatutoryBalanceSheetService:
    """Core enterprise business service for managing StatutoryBalanceSheet entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, StatutoryBalanceSheet] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"STA-{1000 + i}"
            item = StatutoryBalanceSheet(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise StatutoryBalanceSheet {i}",
                description=f"Primary operational StatutoryBalanceSheet record generated for organization unit 1.",
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

    def create_statutorybalancesheet(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> StatutoryBalanceSheet:
        """Create, validate, index, and commit new StatutoryBalanceSheet instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = StatutoryBalanceSheet(
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
        self._record_audit_event("CREATE", instance.id, f"Created StatutoryBalanceSheet {code}")
        logger.info(f"Created StatutoryBalanceSheet id={instance.id} code={code}")
        return instance

    def get_statutorybalancesheet_by_id(self, item_id: int) -> Optional[StatutoryBalanceSheet]:
        """Retrieve single StatutoryBalanceSheet by primary key identifier."""
        return self._cache.get(item_id)

    def get_statutorybalancesheet_by_code(self, code: str) -> Optional[StatutoryBalanceSheet]:
        """Lookup StatutoryBalanceSheet by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_statutorybalancesheets(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[StatutoryBalanceSheet]:
        """Return paginated, filtered collection of StatutoryBalanceSheet entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_statutorybalancesheets(self, query: str, limit: int = 50) -> List[StatutoryBalanceSheet]:
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

    def update_statutorybalancesheet(self, item_id: int, updates: Dict[str, Any]) -> Optional[StatutoryBalanceSheet]:
        """Apply partial updates to existing StatutoryBalanceSheet entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked StatutoryBalanceSheet record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_statutorybalancesheet(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of StatutoryBalanceSheet record."""
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
        """Calculate operational and financial aggregate metrics for StatutoryBalanceSheet."""
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

class ConsolidatedIncomeStatementService:
    """Core enterprise business service for managing ConsolidatedIncomeStatement entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ConsolidatedIncomeStatement] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CON-{1000 + i}"
            item = ConsolidatedIncomeStatement(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ConsolidatedIncomeStatement {i}",
                description=f"Primary operational ConsolidatedIncomeStatement record generated for organization unit 1.",
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

    def create_consolidatedincomestatement(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ConsolidatedIncomeStatement:
        """Create, validate, index, and commit new ConsolidatedIncomeStatement instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ConsolidatedIncomeStatement(
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
        self._record_audit_event("CREATE", instance.id, f"Created ConsolidatedIncomeStatement {code}")
        logger.info(f"Created ConsolidatedIncomeStatement id={instance.id} code={code}")
        return instance

    def get_consolidatedincomestatement_by_id(self, item_id: int) -> Optional[ConsolidatedIncomeStatement]:
        """Retrieve single ConsolidatedIncomeStatement by primary key identifier."""
        return self._cache.get(item_id)

    def get_consolidatedincomestatement_by_code(self, code: str) -> Optional[ConsolidatedIncomeStatement]:
        """Lookup ConsolidatedIncomeStatement by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_consolidatedincomestatements(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ConsolidatedIncomeStatement]:
        """Return paginated, filtered collection of ConsolidatedIncomeStatement entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_consolidatedincomestatements(self, query: str, limit: int = 50) -> List[ConsolidatedIncomeStatement]:
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

    def update_consolidatedincomestatement(self, item_id: int, updates: Dict[str, Any]) -> Optional[ConsolidatedIncomeStatement]:
        """Apply partial updates to existing ConsolidatedIncomeStatement entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ConsolidatedIncomeStatement record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_consolidatedincomestatement(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ConsolidatedIncomeStatement record."""
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
        """Calculate operational and financial aggregate metrics for ConsolidatedIncomeStatement."""
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

class AuditTrailEliminationService:
    """Core enterprise business service for managing AuditTrailElimination entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, AuditTrailElimination] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"AUD-{1000 + i}"
            item = AuditTrailElimination(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise AuditTrailElimination {i}",
                description=f"Primary operational AuditTrailElimination record generated for organization unit 1.",
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

    def create_audittrailelimination(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> AuditTrailElimination:
        """Create, validate, index, and commit new AuditTrailElimination instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = AuditTrailElimination(
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
        self._record_audit_event("CREATE", instance.id, f"Created AuditTrailElimination {code}")
        logger.info(f"Created AuditTrailElimination id={instance.id} code={code}")
        return instance

    def get_audittrailelimination_by_id(self, item_id: int) -> Optional[AuditTrailElimination]:
        """Retrieve single AuditTrailElimination by primary key identifier."""
        return self._cache.get(item_id)

    def get_audittrailelimination_by_code(self, code: str) -> Optional[AuditTrailElimination]:
        """Lookup AuditTrailElimination by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_audittraileliminations(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[AuditTrailElimination]:
        """Return paginated, filtered collection of AuditTrailElimination entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_audittraileliminations(self, query: str, limit: int = 50) -> List[AuditTrailElimination]:
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

    def update_audittrailelimination(self, item_id: int, updates: Dict[str, Any]) -> Optional[AuditTrailElimination]:
        """Apply partial updates to existing AuditTrailElimination entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked AuditTrailElimination record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_audittrailelimination(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of AuditTrailElimination record."""
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
        """Calculate operational and financial aggregate metrics for AuditTrailElimination."""
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

class TaxProvisioningConsolidatedService:
    """Core enterprise business service for managing TaxProvisioningConsolidated entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, TaxProvisioningConsolidated] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"TAX-{1000 + i}"
            item = TaxProvisioningConsolidated(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise TaxProvisioningConsolidated {i}",
                description=f"Primary operational TaxProvisioningConsolidated record generated for organization unit 1.",
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

    def create_taxprovisioningconsolidated(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> TaxProvisioningConsolidated:
        """Create, validate, index, and commit new TaxProvisioningConsolidated instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = TaxProvisioningConsolidated(
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
        self._record_audit_event("CREATE", instance.id, f"Created TaxProvisioningConsolidated {code}")
        logger.info(f"Created TaxProvisioningConsolidated id={instance.id} code={code}")
        return instance

    def get_taxprovisioningconsolidated_by_id(self, item_id: int) -> Optional[TaxProvisioningConsolidated]:
        """Retrieve single TaxProvisioningConsolidated by primary key identifier."""
        return self._cache.get(item_id)

    def get_taxprovisioningconsolidated_by_code(self, code: str) -> Optional[TaxProvisioningConsolidated]:
        """Lookup TaxProvisioningConsolidated by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_taxprovisioningconsolidateds(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[TaxProvisioningConsolidated]:
        """Return paginated, filtered collection of TaxProvisioningConsolidated entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_taxprovisioningconsolidateds(self, query: str, limit: int = 50) -> List[TaxProvisioningConsolidated]:
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

    def update_taxprovisioningconsolidated(self, item_id: int, updates: Dict[str, Any]) -> Optional[TaxProvisioningConsolidated]:
        """Apply partial updates to existing TaxProvisioningConsolidated entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked TaxProvisioningConsolidated record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_taxprovisioningconsolidated(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of TaxProvisioningConsolidated record."""
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
        """Calculate operational and financial aggregate metrics for TaxProvisioningConsolidated."""
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

class FinancialClosingChecklistService:
    """Core enterprise business service for managing FinancialClosingChecklist entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, FinancialClosingChecklist] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"FIN-{1000 + i}"
            item = FinancialClosingChecklist(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise FinancialClosingChecklist {i}",
                description=f"Primary operational FinancialClosingChecklist record generated for organization unit 1.",
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

    def create_financialclosingchecklist(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> FinancialClosingChecklist:
        """Create, validate, index, and commit new FinancialClosingChecklist instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = FinancialClosingChecklist(
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
        self._record_audit_event("CREATE", instance.id, f"Created FinancialClosingChecklist {code}")
        logger.info(f"Created FinancialClosingChecklist id={instance.id} code={code}")
        return instance

    def get_financialclosingchecklist_by_id(self, item_id: int) -> Optional[FinancialClosingChecklist]:
        """Retrieve single FinancialClosingChecklist by primary key identifier."""
        return self._cache.get(item_id)

    def get_financialclosingchecklist_by_code(self, code: str) -> Optional[FinancialClosingChecklist]:
        """Lookup FinancialClosingChecklist by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_financialclosingchecklists(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[FinancialClosingChecklist]:
        """Return paginated, filtered collection of FinancialClosingChecklist entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_financialclosingchecklists(self, query: str, limit: int = 50) -> List[FinancialClosingChecklist]:
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

    def update_financialclosingchecklist(self, item_id: int, updates: Dict[str, Any]) -> Optional[FinancialClosingChecklist]:
        """Apply partial updates to existing FinancialClosingChecklist entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked FinancialClosingChecklist record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_financialclosingchecklist(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of FinancialClosingChecklist record."""
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
        """Calculate operational and financial aggregate metrics for FinancialClosingChecklist."""
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

class ExecutiveBoardFinancialReportService:
    """Core enterprise business service for managing ExecutiveBoardFinancialReport entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ExecutiveBoardFinancialReport] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"EXE-{1000 + i}"
            item = ExecutiveBoardFinancialReport(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ExecutiveBoardFinancialReport {i}",
                description=f"Primary operational ExecutiveBoardFinancialReport record generated for organization unit 1.",
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

    def create_executiveboardfinancialreport(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ExecutiveBoardFinancialReport:
        """Create, validate, index, and commit new ExecutiveBoardFinancialReport instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ExecutiveBoardFinancialReport(
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
        self._record_audit_event("CREATE", instance.id, f"Created ExecutiveBoardFinancialReport {code}")
        logger.info(f"Created ExecutiveBoardFinancialReport id={instance.id} code={code}")
        return instance

    def get_executiveboardfinancialreport_by_id(self, item_id: int) -> Optional[ExecutiveBoardFinancialReport]:
        """Retrieve single ExecutiveBoardFinancialReport by primary key identifier."""
        return self._cache.get(item_id)

    def get_executiveboardfinancialreport_by_code(self, code: str) -> Optional[ExecutiveBoardFinancialReport]:
        """Lookup ExecutiveBoardFinancialReport by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_executiveboardfinancialreports(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ExecutiveBoardFinancialReport]:
        """Return paginated, filtered collection of ExecutiveBoardFinancialReport entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_executiveboardfinancialreports(self, query: str, limit: int = 50) -> List[ExecutiveBoardFinancialReport]:
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

    def update_executiveboardfinancialreport(self, item_id: int, updates: Dict[str, Any]) -> Optional[ExecutiveBoardFinancialReport]:
        """Apply partial updates to existing ExecutiveBoardFinancialReport entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ExecutiveBoardFinancialReport record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_executiveboardfinancialreport(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ExecutiveBoardFinancialReport record."""
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
        """Calculate operational and financial aggregate metrics for ExecutiveBoardFinancialReport."""
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

