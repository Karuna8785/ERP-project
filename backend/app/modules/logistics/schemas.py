"""
Supply Chain & Fleet Logistics - Pydantic Request & Response Validation Schemas
"""
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from .models import RecordStatus, PriorityLevel, RiskClassification

class ShipmentCreateSchema(BaseModel):
    """Validation schema for creating a new Shipment."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class ShipmentUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Shipment."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class ShipmentResponseSchema(BaseModel):
    """Standardized response representation for Shipment."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class ShipmentFilterCriteria(BaseModel):
    """Structured search and filter parameters for Shipment."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ShipmentBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Shipment records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class CarrierCreateSchema(BaseModel):
    """Validation schema for creating a new Carrier."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class CarrierUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Carrier."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class CarrierResponseSchema(BaseModel):
    """Standardized response representation for Carrier."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class CarrierFilterCriteria(BaseModel):
    """Structured search and filter parameters for Carrier."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class CarrierBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Carrier records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RouteCreateSchema(BaseModel):
    """Validation schema for creating a new Route."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class RouteUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Route."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class RouteResponseSchema(BaseModel):
    """Standardized response representation for Route."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class RouteFilterCriteria(BaseModel):
    """Structured search and filter parameters for Route."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RouteBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Route records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class VehicleCreateSchema(BaseModel):
    """Validation schema for creating a new Vehicle."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class VehicleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Vehicle."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class VehicleResponseSchema(BaseModel):
    """Standardized response representation for Vehicle."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class VehicleFilterCriteria(BaseModel):
    """Structured search and filter parameters for Vehicle."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class VehicleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Vehicle records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DriverCreateSchema(BaseModel):
    """Validation schema for creating a new Driver."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class DriverUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Driver."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class DriverResponseSchema(BaseModel):
    """Standardized response representation for Driver."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class DriverFilterCriteria(BaseModel):
    """Structured search and filter parameters for Driver."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DriverBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Driver records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DeliveryStopCreateSchema(BaseModel):
    """Validation schema for creating a new DeliveryStop."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class DeliveryStopUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DeliveryStop."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class DeliveryStopResponseSchema(BaseModel):
    """Standardized response representation for DeliveryStop."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class DeliveryStopFilterCriteria(BaseModel):
    """Structured search and filter parameters for DeliveryStop."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DeliveryStopBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DeliveryStop records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class FreightBillCreateSchema(BaseModel):
    """Validation schema for creating a new FreightBill."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class FreightBillUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing FreightBill."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class FreightBillResponseSchema(BaseModel):
    """Standardized response representation for FreightBill."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class FreightBillFilterCriteria(BaseModel):
    """Structured search and filter parameters for FreightBill."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class FreightBillBatchActionPayload(BaseModel):
    """Batch processing payload for multiple FreightBill records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class WaybillCreateSchema(BaseModel):
    """Validation schema for creating a new Waybill."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class WaybillUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Waybill."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class WaybillResponseSchema(BaseModel):
    """Standardized response representation for Waybill."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class WaybillFilterCriteria(BaseModel):
    """Structured search and filter parameters for Waybill."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class WaybillBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Waybill records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ContainerCreateSchema(BaseModel):
    """Validation schema for creating a new Container."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class ContainerUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Container."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class ContainerResponseSchema(BaseModel):
    """Standardized response representation for Container."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class ContainerFilterCriteria(BaseModel):
    """Structured search and filter parameters for Container."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ContainerBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Container records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DispatchOrderCreateSchema(BaseModel):
    """Validation schema for creating a new DispatchOrder."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class DispatchOrderUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DispatchOrder."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class DispatchOrderResponseSchema(BaseModel):
    """Standardized response representation for DispatchOrder."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class DispatchOrderFilterCriteria(BaseModel):
    """Structured search and filter parameters for DispatchOrder."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DispatchOrderBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DispatchOrder records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class FuelLogCreateSchema(BaseModel):
    """Validation schema for creating a new FuelLog."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class FuelLogUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing FuelLog."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class FuelLogResponseSchema(BaseModel):
    """Standardized response representation for FuelLog."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class FuelLogFilterCriteria(BaseModel):
    """Structured search and filter parameters for FuelLog."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class FuelLogBatchActionPayload(BaseModel):
    """Batch processing payload for multiple FuelLog records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class TollReceiptCreateSchema(BaseModel):
    """Validation schema for creating a new TollReceipt."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class TollReceiptUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing TollReceipt."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class TollReceiptResponseSchema(BaseModel):
    """Standardized response representation for TollReceipt."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class TollReceiptFilterCriteria(BaseModel):
    """Structured search and filter parameters for TollReceipt."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class TollReceiptBatchActionPayload(BaseModel):
    """Batch processing payload for multiple TollReceipt records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class MaintenanceLogCreateSchema(BaseModel):
    """Validation schema for creating a new MaintenanceLog."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class MaintenanceLogUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing MaintenanceLog."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class MaintenanceLogResponseSchema(BaseModel):
    """Standardized response representation for MaintenanceLog."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class MaintenanceLogFilterCriteria(BaseModel):
    """Structured search and filter parameters for MaintenanceLog."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class MaintenanceLogBatchActionPayload(BaseModel):
    """Batch processing payload for multiple MaintenanceLog records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class GPSPingCreateSchema(BaseModel):
    """Validation schema for creating a new GPSPing."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class GPSPingUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing GPSPing."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class GPSPingResponseSchema(BaseModel):
    """Standardized response representation for GPSPing."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class GPSPingFilterCriteria(BaseModel):
    """Structured search and filter parameters for GPSPing."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class GPSPingBatchActionPayload(BaseModel):
    """Batch processing payload for multiple GPSPing records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DockScheduleCreateSchema(BaseModel):
    """Validation schema for creating a new DockSchedule."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class DockScheduleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DockSchedule."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class DockScheduleResponseSchema(BaseModel):
    """Standardized response representation for DockSchedule."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class DockScheduleFilterCriteria(BaseModel):
    """Structured search and filter parameters for DockSchedule."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DockScheduleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DockSchedule records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class CustomsDocCreateSchema(BaseModel):
    """Validation schema for creating a new CustomsDoc."""
    code: str = Field(..., min_length=2, max_length=64, description="Unique alphanumeric identifier")
    title: str = Field(..., min_length=2, max_length=255, description="Primary human-readable label")
    description: Optional[str] = Field(None, max_length=2000, description="Detailed descriptive summary")
    status: RecordStatus = Field(default=RecordStatus.ACTIVE, description="Lifecycle status enum")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM, description="Operational priority")
    risk_rating: RiskClassification = Field(default=RiskClassification.MODERATE, description="Risk level")
    organization_id: int = Field(default=1, ge=1, description="Multi-tenant organization identifier")
    department_id: Optional[int] = Field(default=1, ge=1, description="Department business unit")
    amount: float = Field(default=0.0, ge=0.0, description="Monetary valuation")
    quantity: float = Field(default=0.0, ge=0.0, description="Quantitative measure units")
    unit_cost: float = Field(default=0.0, ge=0.0, description="Per-unit operational cost")
    unit_price: float = Field(default=0.0, ge=0.0, description="Per-unit commercial sales price")
    tax_rate: float = Field(default=0.18, ge=0.0, le=1.0, description="Statutory tax rate fraction")
    discount_rate: float = Field(default=0.0, ge=0.0, le=1.0, description="Commercial discount fraction")
    currency: str = Field(default="INR", max_length=8, description="ISO standard currency code")
    external_reference: Optional[str] = Field(default="", max_length=128, description="External reference")
    tags: List[str] = Field(default_factory=list, description="Categorization tag labels")
    metadata_json: Dict[str, Any] = Field(default_factory=dict, description="Extensible JSON metadata")

class CustomsDocUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing CustomsDoc."""
    title: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[RecordStatus] = None
    priority: Optional[PriorityLevel] = None
    risk_rating: Optional[RiskClassification] = None
    amount: Optional[float] = Field(None, ge=0.0)
    quantity: Optional[float] = Field(None, ge=0.0)
    unit_cost: Optional[float] = Field(None, ge=0.0)
    unit_price: Optional[float] = Field(None, ge=0.0)
    tax_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    discount_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    tags: Optional[List[str]] = None
    metadata_json: Optional[Dict[str, Any]] = None

class CustomsDocResponseSchema(BaseModel):
    """Standardized response representation for CustomsDoc."""
    id: int
    code: str
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    risk_rating: str
    organization_id: int
    department_id: Optional[int] = None
    amount: float
    quantity: float
    subtotal: float
    taxable_amount: float
    tax_amount: float
    total_amount: float
    profit_margin_pct: float
    currency: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    version_number: int
    is_active: bool
    tags: List[str] = []

class CustomsDocFilterCriteria(BaseModel):
    """Structured search and filter parameters for CustomsDoc."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class CustomsDocBatchActionPayload(BaseModel):
    """Batch processing payload for multiple CustomsDoc records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

