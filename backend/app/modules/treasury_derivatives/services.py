"""
Financial Derivatives & Mark-to-Market Hedging - Business Logic Service Layer
"""
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import logging
from .models import RecordStatus, PriorityLevel, RiskClassification

from .models import InterestRateSwapContract
from .models import FXForwardContract
from .models import CommodityFutureHedge
from .models import CurrencyOptionStrategy
from .models import MarkToMarketValuation
from .models import ISDAMasterAgreement
from .models import CollateralMarginCall
from .models import CreditDefaultSwapSpread
from .models import HedgeEffectivenessTest
from .models import GreeksRiskSensitivity
from .models import CounterpartyCreditRisk
from .models import YieldCurveInterpolation
from .models import DerivativesSettlementEntry
from .models import TreasuryExposureForecast
from .models import RegulatoryEMIRFiling
from .models import BasisRiskMeasurement

logger = logging.getLogger("treasury_derivatives.services")

class InterestRateSwapContractService:
    """Core enterprise business service for managing InterestRateSwapContract entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, InterestRateSwapContract] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"INT-{1000 + i}"
            item = InterestRateSwapContract(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise InterestRateSwapContract {i}",
                description=f"Primary operational InterestRateSwapContract record generated for organization unit 1.",
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

    def create_interestrateswapcontract(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> InterestRateSwapContract:
        """Create, validate, index, and commit new InterestRateSwapContract instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = InterestRateSwapContract(
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
        self._record_audit_event("CREATE", instance.id, f"Created InterestRateSwapContract {code}")
        logger.info(f"Created InterestRateSwapContract id={instance.id} code={code}")
        return instance

    def get_interestrateswapcontract_by_id(self, item_id: int) -> Optional[InterestRateSwapContract]:
        """Retrieve single InterestRateSwapContract by primary key identifier."""
        return self._cache.get(item_id)

    def get_interestrateswapcontract_by_code(self, code: str) -> Optional[InterestRateSwapContract]:
        """Lookup InterestRateSwapContract by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_interestrateswapcontracts(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[InterestRateSwapContract]:
        """Return paginated, filtered collection of InterestRateSwapContract entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_interestrateswapcontracts(self, query: str, limit: int = 50) -> List[InterestRateSwapContract]:
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

    def update_interestrateswapcontract(self, item_id: int, updates: Dict[str, Any]) -> Optional[InterestRateSwapContract]:
        """Apply partial updates to existing InterestRateSwapContract entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked InterestRateSwapContract record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_interestrateswapcontract(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of InterestRateSwapContract record."""
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
        """Calculate operational and financial aggregate metrics for InterestRateSwapContract."""
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

class FXForwardContractService:
    """Core enterprise business service for managing FXForwardContract entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, FXForwardContract] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"FXF-{1000 + i}"
            item = FXForwardContract(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise FXForwardContract {i}",
                description=f"Primary operational FXForwardContract record generated for organization unit 1.",
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

    def create_fxforwardcontract(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> FXForwardContract:
        """Create, validate, index, and commit new FXForwardContract instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = FXForwardContract(
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
        self._record_audit_event("CREATE", instance.id, f"Created FXForwardContract {code}")
        logger.info(f"Created FXForwardContract id={instance.id} code={code}")
        return instance

    def get_fxforwardcontract_by_id(self, item_id: int) -> Optional[FXForwardContract]:
        """Retrieve single FXForwardContract by primary key identifier."""
        return self._cache.get(item_id)

    def get_fxforwardcontract_by_code(self, code: str) -> Optional[FXForwardContract]:
        """Lookup FXForwardContract by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_fxforwardcontracts(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[FXForwardContract]:
        """Return paginated, filtered collection of FXForwardContract entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_fxforwardcontracts(self, query: str, limit: int = 50) -> List[FXForwardContract]:
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

    def update_fxforwardcontract(self, item_id: int, updates: Dict[str, Any]) -> Optional[FXForwardContract]:
        """Apply partial updates to existing FXForwardContract entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked FXForwardContract record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_fxforwardcontract(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of FXForwardContract record."""
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
        """Calculate operational and financial aggregate metrics for FXForwardContract."""
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

class CommodityFutureHedgeService:
    """Core enterprise business service for managing CommodityFutureHedge entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, CommodityFutureHedge] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"COM-{1000 + i}"
            item = CommodityFutureHedge(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise CommodityFutureHedge {i}",
                description=f"Primary operational CommodityFutureHedge record generated for organization unit 1.",
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

    def create_commodityfuturehedge(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> CommodityFutureHedge:
        """Create, validate, index, and commit new CommodityFutureHedge instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = CommodityFutureHedge(
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
        self._record_audit_event("CREATE", instance.id, f"Created CommodityFutureHedge {code}")
        logger.info(f"Created CommodityFutureHedge id={instance.id} code={code}")
        return instance

    def get_commodityfuturehedge_by_id(self, item_id: int) -> Optional[CommodityFutureHedge]:
        """Retrieve single CommodityFutureHedge by primary key identifier."""
        return self._cache.get(item_id)

    def get_commodityfuturehedge_by_code(self, code: str) -> Optional[CommodityFutureHedge]:
        """Lookup CommodityFutureHedge by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_commodityfuturehedges(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[CommodityFutureHedge]:
        """Return paginated, filtered collection of CommodityFutureHedge entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_commodityfuturehedges(self, query: str, limit: int = 50) -> List[CommodityFutureHedge]:
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

    def update_commodityfuturehedge(self, item_id: int, updates: Dict[str, Any]) -> Optional[CommodityFutureHedge]:
        """Apply partial updates to existing CommodityFutureHedge entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked CommodityFutureHedge record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_commodityfuturehedge(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of CommodityFutureHedge record."""
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
        """Calculate operational and financial aggregate metrics for CommodityFutureHedge."""
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

class CurrencyOptionStrategyService:
    """Core enterprise business service for managing CurrencyOptionStrategy entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, CurrencyOptionStrategy] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CUR-{1000 + i}"
            item = CurrencyOptionStrategy(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise CurrencyOptionStrategy {i}",
                description=f"Primary operational CurrencyOptionStrategy record generated for organization unit 1.",
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

    def create_currencyoptionstrategy(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> CurrencyOptionStrategy:
        """Create, validate, index, and commit new CurrencyOptionStrategy instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = CurrencyOptionStrategy(
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
        self._record_audit_event("CREATE", instance.id, f"Created CurrencyOptionStrategy {code}")
        logger.info(f"Created CurrencyOptionStrategy id={instance.id} code={code}")
        return instance

    def get_currencyoptionstrategy_by_id(self, item_id: int) -> Optional[CurrencyOptionStrategy]:
        """Retrieve single CurrencyOptionStrategy by primary key identifier."""
        return self._cache.get(item_id)

    def get_currencyoptionstrategy_by_code(self, code: str) -> Optional[CurrencyOptionStrategy]:
        """Lookup CurrencyOptionStrategy by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_currencyoptionstrategys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[CurrencyOptionStrategy]:
        """Return paginated, filtered collection of CurrencyOptionStrategy entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_currencyoptionstrategys(self, query: str, limit: int = 50) -> List[CurrencyOptionStrategy]:
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

    def update_currencyoptionstrategy(self, item_id: int, updates: Dict[str, Any]) -> Optional[CurrencyOptionStrategy]:
        """Apply partial updates to existing CurrencyOptionStrategy entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked CurrencyOptionStrategy record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_currencyoptionstrategy(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of CurrencyOptionStrategy record."""
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
        """Calculate operational and financial aggregate metrics for CurrencyOptionStrategy."""
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

class MarkToMarketValuationService:
    """Core enterprise business service for managing MarkToMarketValuation entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, MarkToMarketValuation] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"MAR-{1000 + i}"
            item = MarkToMarketValuation(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise MarkToMarketValuation {i}",
                description=f"Primary operational MarkToMarketValuation record generated for organization unit 1.",
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

    def create_marktomarketvaluation(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> MarkToMarketValuation:
        """Create, validate, index, and commit new MarkToMarketValuation instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = MarkToMarketValuation(
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
        self._record_audit_event("CREATE", instance.id, f"Created MarkToMarketValuation {code}")
        logger.info(f"Created MarkToMarketValuation id={instance.id} code={code}")
        return instance

    def get_marktomarketvaluation_by_id(self, item_id: int) -> Optional[MarkToMarketValuation]:
        """Retrieve single MarkToMarketValuation by primary key identifier."""
        return self._cache.get(item_id)

    def get_marktomarketvaluation_by_code(self, code: str) -> Optional[MarkToMarketValuation]:
        """Lookup MarkToMarketValuation by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_marktomarketvaluations(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[MarkToMarketValuation]:
        """Return paginated, filtered collection of MarkToMarketValuation entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_marktomarketvaluations(self, query: str, limit: int = 50) -> List[MarkToMarketValuation]:
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

    def update_marktomarketvaluation(self, item_id: int, updates: Dict[str, Any]) -> Optional[MarkToMarketValuation]:
        """Apply partial updates to existing MarkToMarketValuation entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked MarkToMarketValuation record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_marktomarketvaluation(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of MarkToMarketValuation record."""
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
        """Calculate operational and financial aggregate metrics for MarkToMarketValuation."""
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

class ISDAMasterAgreementService:
    """Core enterprise business service for managing ISDAMasterAgreement entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, ISDAMasterAgreement] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"ISD-{1000 + i}"
            item = ISDAMasterAgreement(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise ISDAMasterAgreement {i}",
                description=f"Primary operational ISDAMasterAgreement record generated for organization unit 1.",
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

    def create_isdamasteragreement(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> ISDAMasterAgreement:
        """Create, validate, index, and commit new ISDAMasterAgreement instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = ISDAMasterAgreement(
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
        self._record_audit_event("CREATE", instance.id, f"Created ISDAMasterAgreement {code}")
        logger.info(f"Created ISDAMasterAgreement id={instance.id} code={code}")
        return instance

    def get_isdamasteragreement_by_id(self, item_id: int) -> Optional[ISDAMasterAgreement]:
        """Retrieve single ISDAMasterAgreement by primary key identifier."""
        return self._cache.get(item_id)

    def get_isdamasteragreement_by_code(self, code: str) -> Optional[ISDAMasterAgreement]:
        """Lookup ISDAMasterAgreement by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_isdamasteragreements(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[ISDAMasterAgreement]:
        """Return paginated, filtered collection of ISDAMasterAgreement entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_isdamasteragreements(self, query: str, limit: int = 50) -> List[ISDAMasterAgreement]:
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

    def update_isdamasteragreement(self, item_id: int, updates: Dict[str, Any]) -> Optional[ISDAMasterAgreement]:
        """Apply partial updates to existing ISDAMasterAgreement entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked ISDAMasterAgreement record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_isdamasteragreement(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of ISDAMasterAgreement record."""
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
        """Calculate operational and financial aggregate metrics for ISDAMasterAgreement."""
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

class CollateralMarginCallService:
    """Core enterprise business service for managing CollateralMarginCall entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, CollateralMarginCall] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"COL-{1000 + i}"
            item = CollateralMarginCall(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise CollateralMarginCall {i}",
                description=f"Primary operational CollateralMarginCall record generated for organization unit 1.",
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

    def create_collateralmargincall(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> CollateralMarginCall:
        """Create, validate, index, and commit new CollateralMarginCall instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = CollateralMarginCall(
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
        self._record_audit_event("CREATE", instance.id, f"Created CollateralMarginCall {code}")
        logger.info(f"Created CollateralMarginCall id={instance.id} code={code}")
        return instance

    def get_collateralmargincall_by_id(self, item_id: int) -> Optional[CollateralMarginCall]:
        """Retrieve single CollateralMarginCall by primary key identifier."""
        return self._cache.get(item_id)

    def get_collateralmargincall_by_code(self, code: str) -> Optional[CollateralMarginCall]:
        """Lookup CollateralMarginCall by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_collateralmargincalls(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[CollateralMarginCall]:
        """Return paginated, filtered collection of CollateralMarginCall entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_collateralmargincalls(self, query: str, limit: int = 50) -> List[CollateralMarginCall]:
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

    def update_collateralmargincall(self, item_id: int, updates: Dict[str, Any]) -> Optional[CollateralMarginCall]:
        """Apply partial updates to existing CollateralMarginCall entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked CollateralMarginCall record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_collateralmargincall(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of CollateralMarginCall record."""
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
        """Calculate operational and financial aggregate metrics for CollateralMarginCall."""
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

class CreditDefaultSwapSpreadService:
    """Core enterprise business service for managing CreditDefaultSwapSpread entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, CreditDefaultSwapSpread] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"CRE-{1000 + i}"
            item = CreditDefaultSwapSpread(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise CreditDefaultSwapSpread {i}",
                description=f"Primary operational CreditDefaultSwapSpread record generated for organization unit 1.",
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

    def create_creditdefaultswapspread(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> CreditDefaultSwapSpread:
        """Create, validate, index, and commit new CreditDefaultSwapSpread instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = CreditDefaultSwapSpread(
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
        self._record_audit_event("CREATE", instance.id, f"Created CreditDefaultSwapSpread {code}")
        logger.info(f"Created CreditDefaultSwapSpread id={instance.id} code={code}")
        return instance

    def get_creditdefaultswapspread_by_id(self, item_id: int) -> Optional[CreditDefaultSwapSpread]:
        """Retrieve single CreditDefaultSwapSpread by primary key identifier."""
        return self._cache.get(item_id)

    def get_creditdefaultswapspread_by_code(self, code: str) -> Optional[CreditDefaultSwapSpread]:
        """Lookup CreditDefaultSwapSpread by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_creditdefaultswapspreads(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[CreditDefaultSwapSpread]:
        """Return paginated, filtered collection of CreditDefaultSwapSpread entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_creditdefaultswapspreads(self, query: str, limit: int = 50) -> List[CreditDefaultSwapSpread]:
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

    def update_creditdefaultswapspread(self, item_id: int, updates: Dict[str, Any]) -> Optional[CreditDefaultSwapSpread]:
        """Apply partial updates to existing CreditDefaultSwapSpread entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked CreditDefaultSwapSpread record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_creditdefaultswapspread(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of CreditDefaultSwapSpread record."""
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
        """Calculate operational and financial aggregate metrics for CreditDefaultSwapSpread."""
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

class HedgeEffectivenessTestService:
    """Core enterprise business service for managing HedgeEffectivenessTest entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, HedgeEffectivenessTest] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"HED-{1000 + i}"
            item = HedgeEffectivenessTest(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise HedgeEffectivenessTest {i}",
                description=f"Primary operational HedgeEffectivenessTest record generated for organization unit 1.",
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

    def create_hedgeeffectivenesstest(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> HedgeEffectivenessTest:
        """Create, validate, index, and commit new HedgeEffectivenessTest instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = HedgeEffectivenessTest(
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
        self._record_audit_event("CREATE", instance.id, f"Created HedgeEffectivenessTest {code}")
        logger.info(f"Created HedgeEffectivenessTest id={instance.id} code={code}")
        return instance

    def get_hedgeeffectivenesstest_by_id(self, item_id: int) -> Optional[HedgeEffectivenessTest]:
        """Retrieve single HedgeEffectivenessTest by primary key identifier."""
        return self._cache.get(item_id)

    def get_hedgeeffectivenesstest_by_code(self, code: str) -> Optional[HedgeEffectivenessTest]:
        """Lookup HedgeEffectivenessTest by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_hedgeeffectivenesstests(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[HedgeEffectivenessTest]:
        """Return paginated, filtered collection of HedgeEffectivenessTest entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_hedgeeffectivenesstests(self, query: str, limit: int = 50) -> List[HedgeEffectivenessTest]:
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

    def update_hedgeeffectivenesstest(self, item_id: int, updates: Dict[str, Any]) -> Optional[HedgeEffectivenessTest]:
        """Apply partial updates to existing HedgeEffectivenessTest entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked HedgeEffectivenessTest record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_hedgeeffectivenesstest(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of HedgeEffectivenessTest record."""
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
        """Calculate operational and financial aggregate metrics for HedgeEffectivenessTest."""
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

class GreeksRiskSensitivityService:
    """Core enterprise business service for managing GreeksRiskSensitivity entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, GreeksRiskSensitivity] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"GRE-{1000 + i}"
            item = GreeksRiskSensitivity(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise GreeksRiskSensitivity {i}",
                description=f"Primary operational GreeksRiskSensitivity record generated for organization unit 1.",
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

    def create_greeksrisksensitivity(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> GreeksRiskSensitivity:
        """Create, validate, index, and commit new GreeksRiskSensitivity instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = GreeksRiskSensitivity(
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
        self._record_audit_event("CREATE", instance.id, f"Created GreeksRiskSensitivity {code}")
        logger.info(f"Created GreeksRiskSensitivity id={instance.id} code={code}")
        return instance

    def get_greeksrisksensitivity_by_id(self, item_id: int) -> Optional[GreeksRiskSensitivity]:
        """Retrieve single GreeksRiskSensitivity by primary key identifier."""
        return self._cache.get(item_id)

    def get_greeksrisksensitivity_by_code(self, code: str) -> Optional[GreeksRiskSensitivity]:
        """Lookup GreeksRiskSensitivity by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_greeksrisksensitivitys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[GreeksRiskSensitivity]:
        """Return paginated, filtered collection of GreeksRiskSensitivity entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_greeksrisksensitivitys(self, query: str, limit: int = 50) -> List[GreeksRiskSensitivity]:
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

    def update_greeksrisksensitivity(self, item_id: int, updates: Dict[str, Any]) -> Optional[GreeksRiskSensitivity]:
        """Apply partial updates to existing GreeksRiskSensitivity entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked GreeksRiskSensitivity record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_greeksrisksensitivity(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of GreeksRiskSensitivity record."""
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
        """Calculate operational and financial aggregate metrics for GreeksRiskSensitivity."""
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

class CounterpartyCreditRiskService:
    """Core enterprise business service for managing CounterpartyCreditRisk entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, CounterpartyCreditRisk] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"COU-{1000 + i}"
            item = CounterpartyCreditRisk(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise CounterpartyCreditRisk {i}",
                description=f"Primary operational CounterpartyCreditRisk record generated for organization unit 1.",
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

    def create_counterpartycreditrisk(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> CounterpartyCreditRisk:
        """Create, validate, index, and commit new CounterpartyCreditRisk instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = CounterpartyCreditRisk(
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
        self._record_audit_event("CREATE", instance.id, f"Created CounterpartyCreditRisk {code}")
        logger.info(f"Created CounterpartyCreditRisk id={instance.id} code={code}")
        return instance

    def get_counterpartycreditrisk_by_id(self, item_id: int) -> Optional[CounterpartyCreditRisk]:
        """Retrieve single CounterpartyCreditRisk by primary key identifier."""
        return self._cache.get(item_id)

    def get_counterpartycreditrisk_by_code(self, code: str) -> Optional[CounterpartyCreditRisk]:
        """Lookup CounterpartyCreditRisk by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_counterpartycreditrisks(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[CounterpartyCreditRisk]:
        """Return paginated, filtered collection of CounterpartyCreditRisk entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_counterpartycreditrisks(self, query: str, limit: int = 50) -> List[CounterpartyCreditRisk]:
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

    def update_counterpartycreditrisk(self, item_id: int, updates: Dict[str, Any]) -> Optional[CounterpartyCreditRisk]:
        """Apply partial updates to existing CounterpartyCreditRisk entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked CounterpartyCreditRisk record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_counterpartycreditrisk(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of CounterpartyCreditRisk record."""
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
        """Calculate operational and financial aggregate metrics for CounterpartyCreditRisk."""
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

class YieldCurveInterpolationService:
    """Core enterprise business service for managing YieldCurveInterpolation entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, YieldCurveInterpolation] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"YIE-{1000 + i}"
            item = YieldCurveInterpolation(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise YieldCurveInterpolation {i}",
                description=f"Primary operational YieldCurveInterpolation record generated for organization unit 1.",
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

    def create_yieldcurveinterpolation(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> YieldCurveInterpolation:
        """Create, validate, index, and commit new YieldCurveInterpolation instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = YieldCurveInterpolation(
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
        self._record_audit_event("CREATE", instance.id, f"Created YieldCurveInterpolation {code}")
        logger.info(f"Created YieldCurveInterpolation id={instance.id} code={code}")
        return instance

    def get_yieldcurveinterpolation_by_id(self, item_id: int) -> Optional[YieldCurveInterpolation]:
        """Retrieve single YieldCurveInterpolation by primary key identifier."""
        return self._cache.get(item_id)

    def get_yieldcurveinterpolation_by_code(self, code: str) -> Optional[YieldCurveInterpolation]:
        """Lookup YieldCurveInterpolation by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_yieldcurveinterpolations(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[YieldCurveInterpolation]:
        """Return paginated, filtered collection of YieldCurveInterpolation entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_yieldcurveinterpolations(self, query: str, limit: int = 50) -> List[YieldCurveInterpolation]:
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

    def update_yieldcurveinterpolation(self, item_id: int, updates: Dict[str, Any]) -> Optional[YieldCurveInterpolation]:
        """Apply partial updates to existing YieldCurveInterpolation entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked YieldCurveInterpolation record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_yieldcurveinterpolation(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of YieldCurveInterpolation record."""
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
        """Calculate operational and financial aggregate metrics for YieldCurveInterpolation."""
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

class DerivativesSettlementEntryService:
    """Core enterprise business service for managing DerivativesSettlementEntry entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, DerivativesSettlementEntry] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"DER-{1000 + i}"
            item = DerivativesSettlementEntry(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise DerivativesSettlementEntry {i}",
                description=f"Primary operational DerivativesSettlementEntry record generated for organization unit 1.",
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

    def create_derivativessettlemententry(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> DerivativesSettlementEntry:
        """Create, validate, index, and commit new DerivativesSettlementEntry instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = DerivativesSettlementEntry(
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
        self._record_audit_event("CREATE", instance.id, f"Created DerivativesSettlementEntry {code}")
        logger.info(f"Created DerivativesSettlementEntry id={instance.id} code={code}")
        return instance

    def get_derivativessettlemententry_by_id(self, item_id: int) -> Optional[DerivativesSettlementEntry]:
        """Retrieve single DerivativesSettlementEntry by primary key identifier."""
        return self._cache.get(item_id)

    def get_derivativessettlemententry_by_code(self, code: str) -> Optional[DerivativesSettlementEntry]:
        """Lookup DerivativesSettlementEntry by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_derivativessettlemententrys(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[DerivativesSettlementEntry]:
        """Return paginated, filtered collection of DerivativesSettlementEntry entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_derivativessettlemententrys(self, query: str, limit: int = 50) -> List[DerivativesSettlementEntry]:
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

    def update_derivativessettlemententry(self, item_id: int, updates: Dict[str, Any]) -> Optional[DerivativesSettlementEntry]:
        """Apply partial updates to existing DerivativesSettlementEntry entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked DerivativesSettlementEntry record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_derivativessettlemententry(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of DerivativesSettlementEntry record."""
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
        """Calculate operational and financial aggregate metrics for DerivativesSettlementEntry."""
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

class TreasuryExposureForecastService:
    """Core enterprise business service for managing TreasuryExposureForecast entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, TreasuryExposureForecast] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"TRE-{1000 + i}"
            item = TreasuryExposureForecast(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise TreasuryExposureForecast {i}",
                description=f"Primary operational TreasuryExposureForecast record generated for organization unit 1.",
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

    def create_treasuryexposureforecast(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> TreasuryExposureForecast:
        """Create, validate, index, and commit new TreasuryExposureForecast instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = TreasuryExposureForecast(
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
        self._record_audit_event("CREATE", instance.id, f"Created TreasuryExposureForecast {code}")
        logger.info(f"Created TreasuryExposureForecast id={instance.id} code={code}")
        return instance

    def get_treasuryexposureforecast_by_id(self, item_id: int) -> Optional[TreasuryExposureForecast]:
        """Retrieve single TreasuryExposureForecast by primary key identifier."""
        return self._cache.get(item_id)

    def get_treasuryexposureforecast_by_code(self, code: str) -> Optional[TreasuryExposureForecast]:
        """Lookup TreasuryExposureForecast by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_treasuryexposureforecasts(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[TreasuryExposureForecast]:
        """Return paginated, filtered collection of TreasuryExposureForecast entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_treasuryexposureforecasts(self, query: str, limit: int = 50) -> List[TreasuryExposureForecast]:
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

    def update_treasuryexposureforecast(self, item_id: int, updates: Dict[str, Any]) -> Optional[TreasuryExposureForecast]:
        """Apply partial updates to existing TreasuryExposureForecast entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked TreasuryExposureForecast record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_treasuryexposureforecast(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of TreasuryExposureForecast record."""
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
        """Calculate operational and financial aggregate metrics for TreasuryExposureForecast."""
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

class RegulatoryEMIRFilingService:
    """Core enterprise business service for managing RegulatoryEMIRFiling entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, RegulatoryEMIRFiling] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"REG-{1000 + i}"
            item = RegulatoryEMIRFiling(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise RegulatoryEMIRFiling {i}",
                description=f"Primary operational RegulatoryEMIRFiling record generated for organization unit 1.",
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

    def create_regulatoryemirfiling(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> RegulatoryEMIRFiling:
        """Create, validate, index, and commit new RegulatoryEMIRFiling instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = RegulatoryEMIRFiling(
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
        self._record_audit_event("CREATE", instance.id, f"Created RegulatoryEMIRFiling {code}")
        logger.info(f"Created RegulatoryEMIRFiling id={instance.id} code={code}")
        return instance

    def get_regulatoryemirfiling_by_id(self, item_id: int) -> Optional[RegulatoryEMIRFiling]:
        """Retrieve single RegulatoryEMIRFiling by primary key identifier."""
        return self._cache.get(item_id)

    def get_regulatoryemirfiling_by_code(self, code: str) -> Optional[RegulatoryEMIRFiling]:
        """Lookup RegulatoryEMIRFiling by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_regulatoryemirfilings(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[RegulatoryEMIRFiling]:
        """Return paginated, filtered collection of RegulatoryEMIRFiling entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_regulatoryemirfilings(self, query: str, limit: int = 50) -> List[RegulatoryEMIRFiling]:
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

    def update_regulatoryemirfiling(self, item_id: int, updates: Dict[str, Any]) -> Optional[RegulatoryEMIRFiling]:
        """Apply partial updates to existing RegulatoryEMIRFiling entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked RegulatoryEMIRFiling record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_regulatoryemirfiling(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of RegulatoryEMIRFiling record."""
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
        """Calculate operational and financial aggregate metrics for RegulatoryEMIRFiling."""
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

class BasisRiskMeasurementService:
    """Core enterprise business service for managing BasisRiskMeasurement entities."""

    def __init__(self, db_session=None):
        self.db = db_session
        self._cache: Dict[int, BasisRiskMeasurement] = {}
        self._code_index: Dict[str, int] = {}
        self._audit_log: List[Dict[str, Any]] = []
        self._id_sequence = 1000
        self._seed_default_enterprise_records()

    def _seed_default_enterprise_records(self):
        """Pre-populate repository with standard operational seed fixtures."""
        for i in range(1, 6):
            code = f"BAS-{1000 + i}"
            item = BasisRiskMeasurement(
                id=self._id_sequence + i,
                code=code,
                title=f"Standard Enterprise BasisRiskMeasurement {i}",
                description=f"Primary operational BasisRiskMeasurement record generated for organization unit 1.",
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

    def create_basisriskmeasurement(self, code: str, title: str, amount: float = 0.0, quantity: float = 0.0, **kwargs) -> BasisRiskMeasurement:
        """Create, validate, index, and commit new BasisRiskMeasurement instance."""
        if code in self._code_index:
            raise ValueError(f"Entity with code {code} already exists in system")
        self._id_sequence += 1
        instance = BasisRiskMeasurement(
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
        self._record_audit_event("CREATE", instance.id, f"Created BasisRiskMeasurement {code}")
        logger.info(f"Created BasisRiskMeasurement id={instance.id} code={code}")
        return instance

    def get_basisriskmeasurement_by_id(self, item_id: int) -> Optional[BasisRiskMeasurement]:
        """Retrieve single BasisRiskMeasurement by primary key identifier."""
        return self._cache.get(item_id)

    def get_basisriskmeasurement_by_code(self, code: str) -> Optional[BasisRiskMeasurement]:
        """Lookup BasisRiskMeasurement by unique alphanumeric code index."""
        item_id = self._code_index.get(code)
        return self._cache.get(item_id) if item_id else None

    def list_basisriskmeasurements(self, status: Optional[str] = None, priority: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[BasisRiskMeasurement]:
        """Return paginated, filtered collection of BasisRiskMeasurement entities."""
        items = [x for x in self._cache.values() if not x.is_deleted]
        if status:
            items = [x for x in items if x.status == status or x.status.value == status]
        if priority:
            items = [x for x in items if x.priority == priority or x.priority.value == priority]
        return items[offset:offset + limit]

    def search_basisriskmeasurements(self, query: str, limit: int = 50) -> List[BasisRiskMeasurement]:
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

    def update_basisriskmeasurement(self, item_id: int, updates: Dict[str, Any]) -> Optional[BasisRiskMeasurement]:
        """Apply partial updates to existing BasisRiskMeasurement entity."""
        item = self._cache.get(item_id)
        if not item or item.is_deleted:
            return None
        if item.is_locked:
            raise PermissionError(f"Cannot update locked BasisRiskMeasurement record id={item_id}")
        for field_name, new_val in updates.items():
            if hasattr(item, field_name) and field_name not in ["id", "uuid_token", "created_at"]:
                setattr(item, field_name, new_val)
        item.version_number += 1
        item.updated_at = datetime.utcnow()
        item.validate()
        self._record_audit_event("UPDATE", item.id, f"Updated fields: {list(updates.keys())}")
        return item

    def delete_basisriskmeasurement(self, item_id: int, hard_delete: bool = False) -> bool:
        """Perform soft or hard delete of BasisRiskMeasurement record."""
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
        """Calculate operational and financial aggregate metrics for BasisRiskMeasurement."""
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

