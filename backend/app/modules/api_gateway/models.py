"""
Enterprise API Gateway & Integration Hub - Enterprise Domain Entities & Data Contracts
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
class APIEndpointDefinition:
    """Enterprise Domain entity representing a APIEndpointDefinition in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity APIEndpointDefinition code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity APIEndpointDefinition code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "APIEndpointDefinition":
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
            "entity_name": "APIEndpointDefinition",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "APIEndpointDefinition":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class APIConsumerApplication:
    """Enterprise Domain entity representing a APIConsumerApplication in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity APIConsumerApplication code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity APIConsumerApplication code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "APIConsumerApplication":
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
            "entity_name": "APIConsumerApplication",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "APIConsumerApplication":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class APIKeyCredential:
    """Enterprise Domain entity representing a APIKeyCredential in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity APIKeyCredential code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity APIKeyCredential code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "APIKeyCredential":
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
            "entity_name": "APIKeyCredential",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "APIKeyCredential":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class RateLimitQuotaRule:
    """Enterprise Domain entity representing a RateLimitQuotaRule in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity RateLimitQuotaRule code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity RateLimitQuotaRule code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "RateLimitQuotaRule":
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
            "entity_name": "RateLimitQuotaRule",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "RateLimitQuotaRule":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class OAuthScopePermission:
    """Enterprise Domain entity representing a OAuthScopePermission in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity OAuthScopePermission code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity OAuthScopePermission code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "OAuthScopePermission":
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
            "entity_name": "OAuthScopePermission",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "OAuthScopePermission":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class WebhookSubscriptionTarget:
    """Enterprise Domain entity representing a WebhookSubscriptionTarget in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity WebhookSubscriptionTarget code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity WebhookSubscriptionTarget code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "WebhookSubscriptionTarget":
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
            "entity_name": "WebhookSubscriptionTarget",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "WebhookSubscriptionTarget":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class PayloadTransformationMap:
    """Enterprise Domain entity representing a PayloadTransformationMap in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity PayloadTransformationMap code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity PayloadTransformationMap code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "PayloadTransformationMap":
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
            "entity_name": "PayloadTransformationMap",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "PayloadTransformationMap":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class GatewayTrafficMetric:
    """Enterprise Domain entity representing a GatewayTrafficMetric in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity GatewayTrafficMetric code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity GatewayTrafficMetric code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "GatewayTrafficMetric":
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
            "entity_name": "GatewayTrafficMetric",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "GatewayTrafficMetric":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class SecurityFirewallRule:
    """Enterprise Domain entity representing a SecurityFirewallRule in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity SecurityFirewallRule code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity SecurityFirewallRule code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "SecurityFirewallRule":
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
            "entity_name": "SecurityFirewallRule",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "SecurityFirewallRule":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class IPAllowlistEntry:
    """Enterprise Domain entity representing a IPAllowlistEntry in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity IPAllowlistEntry code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity IPAllowlistEntry code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "IPAllowlistEntry":
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
            "entity_name": "IPAllowlistEntry",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "IPAllowlistEntry":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class CircuitBreakerState:
    """Enterprise Domain entity representing a CircuitBreakerState in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity CircuitBreakerState code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity CircuitBreakerState code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "CircuitBreakerState":
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
            "entity_name": "CircuitBreakerState",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "CircuitBreakerState":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class APIVersionRelease:
    """Enterprise Domain entity representing a APIVersionRelease in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity APIVersionRelease code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity APIVersionRelease code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "APIVersionRelease":
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
            "entity_name": "APIVersionRelease",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "APIVersionRelease":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class RequestResponseAuditLog:
    """Enterprise Domain entity representing a RequestResponseAuditLog in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity RequestResponseAuditLog code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity RequestResponseAuditLog code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "RequestResponseAuditLog":
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
            "entity_name": "RequestResponseAuditLog",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "RequestResponseAuditLog":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class MockResponseTemplate:
    """Enterprise Domain entity representing a MockResponseTemplate in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity MockResponseTemplate code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity MockResponseTemplate code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "MockResponseTemplate":
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
            "entity_name": "MockResponseTemplate",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "MockResponseTemplate":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class IntegrationConnector:
    """Enterprise Domain entity representing a IntegrationConnector in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity IntegrationConnector code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity IntegrationConnector code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "IntegrationConnector":
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
            "entity_name": "IntegrationConnector",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "IntegrationConnector":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

@dataclass
class ServiceMeshProxy:
    """Enterprise Domain entity representing a ServiceMeshProxy in Enterprise API Gateway & Integration Hub."""
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
            raise ValueError("Entity ServiceMeshProxy code must be non-empty and at least 2 characters")
        if len(self.code) > 64:
            raise ValueError("Entity ServiceMeshProxy code cannot exceed 64 characters")
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
    def from_dict(cls, data: Dict[str, Any]) -> "ServiceMeshProxy":
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
            "entity_name": "ServiceMeshProxy",
            "entity_id": self.id,
            "code": self.code,
            "status": str(self.status),
            "amount": self.amount,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version_number,
        }

    def clone(self, new_code: str) -> "ServiceMeshProxy":
        """Create deep duplicate of entity with new identifier code."""
        d = self.to_dict()
        d["id"] = None
        d["code"] = new_code
        d["title"] = f"Copy of {self.title}"
        d["version_number"] = 1
        return cls.from_dict(d)

