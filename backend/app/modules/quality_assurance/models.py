"""
Quality Management & CAPA Engine - Enterprise Domain Entities & Data Contracts
"""
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional, List, Dict, Any, Union
from enum import Enum
import uuid
import json

class RecordStatus(str, Enum):
    DRAFT = "DRAFT"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    APPROVED = "APPROVED"
    ACTIVE = "ACTIVE"
    IN_PROGRESS = "IN_PROGRESS"
    ON_HOLD = "ON_HOLD"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"

class PriorityLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"
    EMERGENCY = "EMERGENCY"

class RiskClassification(str, Enum):
    MINIMAL = "MINIMAL"
    MODERATE = "MODERATE"
    ELEVATED = "ELEVATED"
    SEVERE = "SEVERE"

@dataclass
class InspectionPlanTemplate:
    """Enterprise Domain entity representing a InspectionPlanTemplate in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity InspectionPlanTemplate code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity InspectionPlanTemplate code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InspectionPlanTemplate":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "InspectionPlanTemplate",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "InspectionPlanTemplate":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class IncomingInspectionRecord:
    """Enterprise Domain entity representing a IncomingInspectionRecord in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity IncomingInspectionRecord code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity IncomingInspectionRecord code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "IncomingInspectionRecord":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "IncomingInspectionRecord",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "IncomingInspectionRecord":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class InProcessAudit:
    """Enterprise Domain entity representing a InProcessAudit in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity InProcessAudit code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity InProcessAudit code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InProcessAudit":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "InProcessAudit",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "InProcessAudit":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class FinalReleaseInspection:
    """Enterprise Domain entity representing a FinalReleaseInspection in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity FinalReleaseInspection code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity FinalReleaseInspection code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FinalReleaseInspection":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "FinalReleaseInspection",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "FinalReleaseInspection":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class NonConformanceReport:
    """Enterprise Domain entity representing a NonConformanceReport in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity NonConformanceReport code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity NonConformanceReport code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NonConformanceReport":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "NonConformanceReport",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "NonConformanceReport":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class CorrectiveActionPlan:
    """Enterprise Domain entity representing a CorrectiveActionPlan in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity CorrectiveActionPlan code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity CorrectiveActionPlan code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CorrectiveActionPlan":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "CorrectiveActionPlan",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "CorrectiveActionPlan":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class PreventiveActionItem:
    """Enterprise Domain entity representing a PreventiveActionItem in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity PreventiveActionItem code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity PreventiveActionItem code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreventiveActionItem":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "PreventiveActionItem",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "PreventiveActionItem":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class RootCauseAnalysis:
    """Enterprise Domain entity representing a RootCauseAnalysis in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity RootCauseAnalysis code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity RootCauseAnalysis code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RootCauseAnalysis":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "RootCauseAnalysis",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "RootCauseAnalysis":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class CalibrationSchedule:
    """Enterprise Domain entity representing a CalibrationSchedule in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity CalibrationSchedule code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity CalibrationSchedule code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CalibrationSchedule":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "CalibrationSchedule",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "CalibrationSchedule":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class GaugeTool:
    """Enterprise Domain entity representing a GaugeTool in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity GaugeTool code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity GaugeTool code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GaugeTool":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "GaugeTool",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "GaugeTool":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class SamplingStandardRule:
    """Enterprise Domain entity representing a SamplingStandardRule in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity SamplingStandardRule code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity SamplingStandardRule code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SamplingStandardRule":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "SamplingStandardRule",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "SamplingStandardRule":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class SupplierQualityAudit:
    """Enterprise Domain entity representing a SupplierQualityAudit in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity SupplierQualityAudit code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity SupplierQualityAudit code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SupplierQualityAudit":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "SupplierQualityAudit",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "SupplierQualityAudit":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class CustomerComplaintQA:
    """Enterprise Domain entity representing a CustomerComplaintQA in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity CustomerComplaintQA code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity CustomerComplaintQA code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CustomerComplaintQA":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "CustomerComplaintQA",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "CustomerComplaintQA":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class CertificateOfAnalysis:
    """Enterprise Domain entity representing a CertificateOfAnalysis in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity CertificateOfAnalysis code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity CertificateOfAnalysis code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CertificateOfAnalysis":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "CertificateOfAnalysis",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "CertificateOfAnalysis":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class StabilityStudy:
    """Enterprise Domain entity representing a StabilityStudy in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity StabilityStudy code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity StabilityStudy code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StabilityStudy":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "StabilityStudy",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "StabilityStudy":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class RegulatoryAuditInspection:
    """Enterprise Domain entity representing a RegulatoryAuditInspection in Quality Management & CAPA Engine."""
    id: Optional[int] = None
    code: str = ""
    title: str = ""
    description: Optional[str] = None
    status: RecordStatus = RecordStatus.ACTIVE
    priority: PriorityLevel = PriorityLevel.MEDIUM
    risk_rating: RiskClassification = RiskClassification.MODERATE
    organization_id: int = 1
    department_id: Optional[int] = 1
    created_by_user_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    effective_date: Optional[date] = None
    expiry_date: Optional[date] = None
    metadata_json: Dict[str, Any] = field(default_factory=dict)
    amount: float = 0.0
    quantity: float = 0.0
    unit_cost: float = 0.0
    unit_price: float = 0.0
    tax_rate: float = 0.18
    discount_rate: float = 0.0
    currency: str = "INR"
    external_reference: str = ""
    uuid_token: str = field(default_factory=lambda: str(uuid.uuid4()))
    version_number: int = 1
    is_locked: bool = False
    is_active: bool = True
    is_deleted: bool = False
    approval_flow_id: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    audit_notes: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate enterprise entity business integrity constraints."""
        if not self.code or len(self.code.strip()) < 2:
            raise ValueError("Entity RegulatoryAuditInspection code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity RegulatoryAuditInspection code cannot exceed 64 characters")
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative")
        if self.tax_rate < 0 or self.tax_rate > 1.0:
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        if self.discount_rate < 0 or self.discount_rate > 1.0:
            raise ValueError("Discount rate must be between 0.0 and 1.0")
        return True

    def calculate_subtotal(self) -> float:
        """Calculate extended item subtotal prior to taxes and discounts."""
        return round(self.quantity * self.unit_price, 2) if self.quantity > 0 and self.unit_price > 0 else round(self.amount, 2)

    def calculate_discount_amount(self) -> float:
        """Calculate discount amount in base currency."""
        return round(self.calculate_subtotal() * self.discount_rate, 2)

    def calculate_taxable_amount(self) -> float:
        """Calculate net taxable base amount after discount."""
        return round(self.calculate_subtotal() - self.calculate_discount_amount(), 2)

    def calculate_tax_amount(self) -> float:
        """Calculate statutory tax liability amount."""
        return round(self.calculate_taxable_amount() * self.tax_rate, 2)

    def calculate_total_amount(self) -> float:
        """Calculate total gross settlement amount inclusive of tax and deductions."""
        return round(self.calculate_taxable_amount() + self.calculate_tax_amount(), 2)

    def calculate_profit_margin(self) -> float:
        """Calculate financial gross profit margin percentage."""
        subtotal = self.calculate_subtotal()
        total_cost = self.quantity * self.unit_cost
        if subtotal <= 0:
            return 0.0
        return round(((subtotal - total_cost) / subtotal) * 100.0, 2)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize entity state into JSON-compatible dictionary."""
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "status": self.status.value if hasattr(self.status, "value") else str(self.status),
            "priority": self.priority.value if hasattr(self.priority, "value") else str(self.priority),
            "risk_rating": self.risk_rating.value if hasattr(self.risk_rating, "value") else str(self.risk_rating),
            "organization_id": self.organization_id,
            "department_id": self.department_id,
            "created_by_user_id": self.created_by_user_id,
            "assigned_to_user_id": self.assigned_to_user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_date": self.effective_date.isoformat() if self.effective_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "amount": self.amount,
            "quantity": self.quantity,
            "unit_cost": self.unit_cost,
            "unit_price": self.unit_price,
            "subtotal": self.calculate_subtotal(),
            "taxable_amount": self.calculate_taxable_amount(),
            "tax_amount": self.calculate_tax_amount(),
            "total_amount": self.calculate_total_amount(),
            "profit_margin_pct": self.calculate_profit_margin(),
            "tax_rate": self.tax_rate,
            "discount_rate": self.discount_rate,
            "currency": self.currency,
            "external_reference": self.external_reference,
            "uuid_token": self.uuid_token,
            "version_number": self.version_number,
            "is_locked": self.is_locked,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "tags": self.tags,
            "metadata_json": self.metadata_json,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RegulatoryAuditInspection":
        """Instantiate entity instance from raw dictionary input."""
        return cls(
            id=data.get("id"),
            code=data.get("code", ""),
            title=data.get("title", ""),
            description=data.get("description"),
            status=RecordStatus(data.get("status", "ACTIVE")) if data.get("status") in RecordStatus.__members__ else RecordStatus.ACTIVE,
            priority=PriorityLevel(data.get("priority", "MEDIUM")) if data.get("priority") in PriorityLevel.__members__ else PriorityLevel.MEDIUM,
            risk_rating=RiskClassification(data.get("risk_rating", "MODERATE")) if data.get("risk_rating") in RiskClassification.__members__ else RiskClassification.MODERATE,
            organization_id=int(data.get("organization_id", 1)),
            department_id=int(data.get("department_id", 1)) if data.get("department_id") else None,
            created_by_user_id=data.get("created_by_user_id"),
            assigned_to_user_id=data.get("assigned_to_user_id"),
            amount=float(data.get("amount", 0.0)),
            quantity=float(data.get("quantity", 0.0)),
            unit_cost=float(data.get("unit_cost", 0.0)),
            unit_price=float(data.get("unit_price", 0.0)),
            tax_rate=float(data.get("tax_rate", 0.18)),
            discount_rate=float(data.get("discount_rate", 0.0)),
            currency=str(data.get("currency", "INR")),
            external_reference=str(data.get("external_reference", "")),
            version_number=int(data.get("version_number", 1)),
            is_locked=bool(data.get("is_locked", False)),
            is_active=bool(data.get("is_active", True)),
            is_deleted=bool(data.get("is_deleted", False)),
            tags=data.get("tags", []),
            metadata_json=data.get("metadata_json", {}),
        )

    def create_audit_snapshot(self) -> Dict[str, Any]:
        """Generate immutable audit log delta snapshot."""
        return {
            "entity_name": "RegulatoryAuditInspection",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "RegulatoryAuditInspection":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

