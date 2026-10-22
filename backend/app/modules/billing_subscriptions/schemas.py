"""
Subscription Billing & Revenue Recognition - Pydantic Request & Response Validation Schemas
"""
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from .models import RecordStatus, PriorityLevel, RiskClassification

class SubscriptionPlanCreateSchema(BaseModel):
    """Validation schema for creating a new SubscriptionPlan."""
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

class SubscriptionPlanUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing SubscriptionPlan."""
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

class SubscriptionPlanResponseSchema(BaseModel):
    """Standardized response representation for SubscriptionPlan."""
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

class SubscriptionPlanFilterCriteria(BaseModel):
    """Structured search and filter parameters for SubscriptionPlan."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class SubscriptionPlanBatchActionPayload(BaseModel):
    """Batch processing payload for multiple SubscriptionPlan records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class CustomerSubscriptionCreateSchema(BaseModel):
    """Validation schema for creating a new CustomerSubscription."""
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

class CustomerSubscriptionUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing CustomerSubscription."""
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

class CustomerSubscriptionResponseSchema(BaseModel):
    """Standardized response representation for CustomerSubscription."""
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

class CustomerSubscriptionFilterCriteria(BaseModel):
    """Structured search and filter parameters for CustomerSubscription."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class CustomerSubscriptionBatchActionPayload(BaseModel):
    """Batch processing payload for multiple CustomerSubscription records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class BillingIntervalScheduleCreateSchema(BaseModel):
    """Validation schema for creating a new BillingIntervalSchedule."""
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

class BillingIntervalScheduleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing BillingIntervalSchedule."""
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

class BillingIntervalScheduleResponseSchema(BaseModel):
    """Standardized response representation for BillingIntervalSchedule."""
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

class BillingIntervalScheduleFilterCriteria(BaseModel):
    """Structured search and filter parameters for BillingIntervalSchedule."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class BillingIntervalScheduleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple BillingIntervalSchedule records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class MeteredUsageEventCreateSchema(BaseModel):
    """Validation schema for creating a new MeteredUsageEvent."""
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

class MeteredUsageEventUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing MeteredUsageEvent."""
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

class MeteredUsageEventResponseSchema(BaseModel):
    """Standardized response representation for MeteredUsageEvent."""
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

class MeteredUsageEventFilterCriteria(BaseModel):
    """Structured search and filter parameters for MeteredUsageEvent."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class MeteredUsageEventBatchActionPayload(BaseModel):
    """Batch processing payload for multiple MeteredUsageEvent records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class InvoiceChargeItemCreateSchema(BaseModel):
    """Validation schema for creating a new InvoiceChargeItem."""
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

class InvoiceChargeItemUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing InvoiceChargeItem."""
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

class InvoiceChargeItemResponseSchema(BaseModel):
    """Standardized response representation for InvoiceChargeItem."""
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

class InvoiceChargeItemFilterCriteria(BaseModel):
    """Structured search and filter parameters for InvoiceChargeItem."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class InvoiceChargeItemBatchActionPayload(BaseModel):
    """Batch processing payload for multiple InvoiceChargeItem records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DiscountCouponCreateSchema(BaseModel):
    """Validation schema for creating a new DiscountCoupon."""
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

class DiscountCouponUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DiscountCoupon."""
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

class DiscountCouponResponseSchema(BaseModel):
    """Standardized response representation for DiscountCoupon."""
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

class DiscountCouponFilterCriteria(BaseModel):
    """Structured search and filter parameters for DiscountCoupon."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DiscountCouponBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DiscountCoupon records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class PaymentMethodProfileCreateSchema(BaseModel):
    """Validation schema for creating a new PaymentMethodProfile."""
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

class PaymentMethodProfileUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing PaymentMethodProfile."""
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

class PaymentMethodProfileResponseSchema(BaseModel):
    """Standardized response representation for PaymentMethodProfile."""
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

class PaymentMethodProfileFilterCriteria(BaseModel):
    """Structured search and filter parameters for PaymentMethodProfile."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class PaymentMethodProfileBatchActionPayload(BaseModel):
    """Batch processing payload for multiple PaymentMethodProfile records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DunningSequenceCreateSchema(BaseModel):
    """Validation schema for creating a new DunningSequence."""
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

class DunningSequenceUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DunningSequence."""
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

class DunningSequenceResponseSchema(BaseModel):
    """Standardized response representation for DunningSequence."""
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

class DunningSequenceFilterCriteria(BaseModel):
    """Structured search and filter parameters for DunningSequence."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DunningSequenceBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DunningSequence records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RevenueContractASC606CreateSchema(BaseModel):
    """Validation schema for creating a new RevenueContractASC606."""
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

class RevenueContractASC606UpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RevenueContractASC606."""
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

class RevenueContractASC606ResponseSchema(BaseModel):
    """Standardized response representation for RevenueContractASC606."""
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

class RevenueContractASC606FilterCriteria(BaseModel):
    """Structured search and filter parameters for RevenueContractASC606."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RevenueContractASC606BatchActionPayload(BaseModel):
    """Batch processing payload for multiple RevenueContractASC606 records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class PerformanceObligationCreateSchema(BaseModel):
    """Validation schema for creating a new PerformanceObligation."""
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

class PerformanceObligationUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing PerformanceObligation."""
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

class PerformanceObligationResponseSchema(BaseModel):
    """Standardized response representation for PerformanceObligation."""
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

class PerformanceObligationFilterCriteria(BaseModel):
    """Structured search and filter parameters for PerformanceObligation."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class PerformanceObligationBatchActionPayload(BaseModel):
    """Batch processing payload for multiple PerformanceObligation records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DeferredRevenueAmortizationCreateSchema(BaseModel):
    """Validation schema for creating a new DeferredRevenueAmortization."""
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

class DeferredRevenueAmortizationUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DeferredRevenueAmortization."""
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

class DeferredRevenueAmortizationResponseSchema(BaseModel):
    """Standardized response representation for DeferredRevenueAmortization."""
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

class DeferredRevenueAmortizationFilterCriteria(BaseModel):
    """Structured search and filter parameters for DeferredRevenueAmortization."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DeferredRevenueAmortizationBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DeferredRevenueAmortization records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class CreditBalanceAdjustmentCreateSchema(BaseModel):
    """Validation schema for creating a new CreditBalanceAdjustment."""
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

class CreditBalanceAdjustmentUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing CreditBalanceAdjustment."""
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

class CreditBalanceAdjustmentResponseSchema(BaseModel):
    """Standardized response representation for CreditBalanceAdjustment."""
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

class CreditBalanceAdjustmentFilterCriteria(BaseModel):
    """Structured search and filter parameters for CreditBalanceAdjustment."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class CreditBalanceAdjustmentBatchActionPayload(BaseModel):
    """Batch processing payload for multiple CreditBalanceAdjustment records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ChurnNoticeCreateSchema(BaseModel):
    """Validation schema for creating a new ChurnNotice."""
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

class ChurnNoticeUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ChurnNotice."""
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

class ChurnNoticeResponseSchema(BaseModel):
    """Standardized response representation for ChurnNotice."""
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

class ChurnNoticeFilterCriteria(BaseModel):
    """Structured search and filter parameters for ChurnNotice."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ChurnNoticeBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ChurnNotice records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class UsageTierTieringCreateSchema(BaseModel):
    """Validation schema for creating a new UsageTierTiering."""
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

class UsageTierTieringUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing UsageTierTiering."""
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

class UsageTierTieringResponseSchema(BaseModel):
    """Standardized response representation for UsageTierTiering."""
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

class UsageTierTieringFilterCriteria(BaseModel):
    """Structured search and filter parameters for UsageTierTiering."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class UsageTierTieringBatchActionPayload(BaseModel):
    """Batch processing payload for multiple UsageTierTiering records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class TaxJurisdictionRuleCreateSchema(BaseModel):
    """Validation schema for creating a new TaxJurisdictionRule."""
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

class TaxJurisdictionRuleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing TaxJurisdictionRule."""
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

class TaxJurisdictionRuleResponseSchema(BaseModel):
    """Standardized response representation for TaxJurisdictionRule."""
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

class TaxJurisdictionRuleFilterCriteria(BaseModel):
    """Structured search and filter parameters for TaxJurisdictionRule."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class TaxJurisdictionRuleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple TaxJurisdictionRule records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class BillingReconciliationCreateSchema(BaseModel):
    """Validation schema for creating a new BillingReconciliation."""
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

class BillingReconciliationUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing BillingReconciliation."""
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

class BillingReconciliationResponseSchema(BaseModel):
    """Standardized response representation for BillingReconciliation."""
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

class BillingReconciliationFilterCriteria(BaseModel):
    """Structured search and filter parameters for BillingReconciliation."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class BillingReconciliationBatchActionPayload(BaseModel):
    """Batch processing payload for multiple BillingReconciliation records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

