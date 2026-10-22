"""
Executive Compensation & Equity (ESOP) Engine - Pydantic Request & Response Validation Schemas
"""
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from .models import RecordStatus, PriorityLevel, RiskClassification

class EquityPlanSchemeCreateSchema(BaseModel):
    """Validation schema for creating a new EquityPlanScheme."""
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

class EquityPlanSchemeUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing EquityPlanScheme."""
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

class EquityPlanSchemeResponseSchema(BaseModel):
    """Standardized response representation for EquityPlanScheme."""
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

class EquityPlanSchemeFilterCriteria(BaseModel):
    """Structured search and filter parameters for EquityPlanScheme."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class EquityPlanSchemeBatchActionPayload(BaseModel):
    """Batch processing payload for multiple EquityPlanScheme records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class OptionGrantAgreementCreateSchema(BaseModel):
    """Validation schema for creating a new OptionGrantAgreement."""
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

class OptionGrantAgreementUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing OptionGrantAgreement."""
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

class OptionGrantAgreementResponseSchema(BaseModel):
    """Standardized response representation for OptionGrantAgreement."""
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

class OptionGrantAgreementFilterCriteria(BaseModel):
    """Structured search and filter parameters for OptionGrantAgreement."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class OptionGrantAgreementBatchActionPayload(BaseModel):
    """Batch processing payload for multiple OptionGrantAgreement records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class VestingScheduleRuleCreateSchema(BaseModel):
    """Validation schema for creating a new VestingScheduleRule."""
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

class VestingScheduleRuleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing VestingScheduleRule."""
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

class VestingScheduleRuleResponseSchema(BaseModel):
    """Standardized response representation for VestingScheduleRule."""
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

class VestingScheduleRuleFilterCriteria(BaseModel):
    """Structured search and filter parameters for VestingScheduleRule."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class VestingScheduleRuleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple VestingScheduleRule records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ExerciseNoticeOrderCreateSchema(BaseModel):
    """Validation schema for creating a new ExerciseNoticeOrder."""
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

class ExerciseNoticeOrderUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ExerciseNoticeOrder."""
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

class ExerciseNoticeOrderResponseSchema(BaseModel):
    """Standardized response representation for ExerciseNoticeOrder."""
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

class ExerciseNoticeOrderFilterCriteria(BaseModel):
    """Structured search and filter parameters for ExerciseNoticeOrder."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ExerciseNoticeOrderBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ExerciseNoticeOrder records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class CapTableShareholderCreateSchema(BaseModel):
    """Validation schema for creating a new CapTableShareholder."""
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

class CapTableShareholderUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing CapTableShareholder."""
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

class CapTableShareholderResponseSchema(BaseModel):
    """Standardized response representation for CapTableShareholder."""
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

class CapTableShareholderFilterCriteria(BaseModel):
    """Structured search and filter parameters for CapTableShareholder."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class CapTableShareholderBatchActionPayload(BaseModel):
    """Batch processing payload for multiple CapTableShareholder records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ShareRepurchaseBuybackCreateSchema(BaseModel):
    """Validation schema for creating a new ShareRepurchaseBuyback."""
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

class ShareRepurchaseBuybackUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ShareRepurchaseBuyback."""
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

class ShareRepurchaseBuybackResponseSchema(BaseModel):
    """Standardized response representation for ShareRepurchaseBuyback."""
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

class ShareRepurchaseBuybackFilterCriteria(BaseModel):
    """Structured search and filter parameters for ShareRepurchaseBuyback."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ShareRepurchaseBuybackBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ShareRepurchaseBuyback records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class AnnualBonusPoolCreateSchema(BaseModel):
    """Validation schema for creating a new AnnualBonusPool."""
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

class AnnualBonusPoolUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing AnnualBonusPool."""
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

class AnnualBonusPoolResponseSchema(BaseModel):
    """Standardized response representation for AnnualBonusPool."""
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

class AnnualBonusPoolFilterCriteria(BaseModel):
    """Structured search and filter parameters for AnnualBonusPool."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class AnnualBonusPoolBatchActionPayload(BaseModel):
    """Batch processing payload for multiple AnnualBonusPool records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class LongTermIncentivePlanCreateSchema(BaseModel):
    """Validation schema for creating a new LongTermIncentivePlan."""
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

class LongTermIncentivePlanUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing LongTermIncentivePlan."""
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

class LongTermIncentivePlanResponseSchema(BaseModel):
    """Standardized response representation for LongTermIncentivePlan."""
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

class LongTermIncentivePlanFilterCriteria(BaseModel):
    """Structured search and filter parameters for LongTermIncentivePlan."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class LongTermIncentivePlanBatchActionPayload(BaseModel):
    """Batch processing payload for multiple LongTermIncentivePlan records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class SalaryBenchmarkSurveyCreateSchema(BaseModel):
    """Validation schema for creating a new SalaryBenchmarkSurvey."""
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

class SalaryBenchmarkSurveyUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing SalaryBenchmarkSurvey."""
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

class SalaryBenchmarkSurveyResponseSchema(BaseModel):
    """Standardized response representation for SalaryBenchmarkSurvey."""
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

class SalaryBenchmarkSurveyFilterCriteria(BaseModel):
    """Structured search and filter parameters for SalaryBenchmarkSurvey."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class SalaryBenchmarkSurveyBatchActionPayload(BaseModel):
    """Batch processing payload for multiple SalaryBenchmarkSurvey records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class FairMarketValuation409ACreateSchema(BaseModel):
    """Validation schema for creating a new FairMarketValuation409A."""
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

class FairMarketValuation409AUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing FairMarketValuation409A."""
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

class FairMarketValuation409AResponseSchema(BaseModel):
    """Standardized response representation for FairMarketValuation409A."""
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

class FairMarketValuation409AFilterCriteria(BaseModel):
    """Structured search and filter parameters for FairMarketValuation409A."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class FairMarketValuation409ABatchActionPayload(BaseModel):
    """Batch processing payload for multiple FairMarketValuation409A records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DividendsDistributionCreateSchema(BaseModel):
    """Validation schema for creating a new DividendsDistribution."""
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

class DividendsDistributionUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DividendsDistribution."""
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

class DividendsDistributionResponseSchema(BaseModel):
    """Standardized response representation for DividendsDistribution."""
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

class DividendsDistributionFilterCriteria(BaseModel):
    """Structured search and filter parameters for DividendsDistribution."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DividendsDistributionBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DividendsDistribution records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class StockOptionCancellationCreateSchema(BaseModel):
    """Validation schema for creating a new StockOptionCancellation."""
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

class StockOptionCancellationUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing StockOptionCancellation."""
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

class StockOptionCancellationResponseSchema(BaseModel):
    """Standardized response representation for StockOptionCancellation."""
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

class StockOptionCancellationFilterCriteria(BaseModel):
    """Structured search and filter parameters for StockOptionCancellation."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class StockOptionCancellationBatchActionPayload(BaseModel):
    """Batch processing payload for multiple StockOptionCancellation records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class Form16StatutoryFilingCreateSchema(BaseModel):
    """Validation schema for creating a new Form16StatutoryFiling."""
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

class Form16StatutoryFilingUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing Form16StatutoryFiling."""
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

class Form16StatutoryFilingResponseSchema(BaseModel):
    """Standardized response representation for Form16StatutoryFiling."""
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

class Form16StatutoryFilingFilterCriteria(BaseModel):
    """Structured search and filter parameters for Form16StatutoryFiling."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class Form16StatutoryFilingBatchActionPayload(BaseModel):
    """Batch processing payload for multiple Form16StatutoryFiling records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ExecutivePerformanceScoreCreateSchema(BaseModel):
    """Validation schema for creating a new ExecutivePerformanceScore."""
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

class ExecutivePerformanceScoreUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ExecutivePerformanceScore."""
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

class ExecutivePerformanceScoreResponseSchema(BaseModel):
    """Standardized response representation for ExecutivePerformanceScore."""
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

class ExecutivePerformanceScoreFilterCriteria(BaseModel):
    """Structured search and filter parameters for ExecutivePerformanceScore."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ExecutivePerformanceScoreBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ExecutivePerformanceScore records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class EquityClawbackRuleCreateSchema(BaseModel):
    """Validation schema for creating a new EquityClawbackRule."""
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

class EquityClawbackRuleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing EquityClawbackRule."""
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

class EquityClawbackRuleResponseSchema(BaseModel):
    """Standardized response representation for EquityClawbackRule."""
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

class EquityClawbackRuleFilterCriteria(BaseModel):
    """Structured search and filter parameters for EquityClawbackRule."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class EquityClawbackRuleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple EquityClawbackRule records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class SecondarySaleWindowCreateSchema(BaseModel):
    """Validation schema for creating a new SecondarySaleWindow."""
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

class SecondarySaleWindowUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing SecondarySaleWindow."""
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

class SecondarySaleWindowResponseSchema(BaseModel):
    """Standardized response representation for SecondarySaleWindow."""
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

class SecondarySaleWindowFilterCriteria(BaseModel):
    """Structured search and filter parameters for SecondarySaleWindow."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class SecondarySaleWindowBatchActionPayload(BaseModel):
    """Batch processing payload for multiple SecondarySaleWindow records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

