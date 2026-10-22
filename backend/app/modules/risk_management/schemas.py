"""
Enterprise Risk Management & KRI Matrix - Pydantic Request & Response Validation Schemas
"""
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from .models import RecordStatus, PriorityLevel, RiskClassification

class RiskCategoryDefinitionCreateSchema(BaseModel):
    """Validation schema for creating a new RiskCategoryDefinition."""
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

class RiskCategoryDefinitionUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RiskCategoryDefinition."""
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

class RiskCategoryDefinitionResponseSchema(BaseModel):
    """Standardized response representation for RiskCategoryDefinition."""
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

class RiskCategoryDefinitionFilterCriteria(BaseModel):
    """Structured search and filter parameters for RiskCategoryDefinition."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RiskCategoryDefinitionBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RiskCategoryDefinition records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RiskRegisterItemCreateSchema(BaseModel):
    """Validation schema for creating a new RiskRegisterItem."""
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

class RiskRegisterItemUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RiskRegisterItem."""
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

class RiskRegisterItemResponseSchema(BaseModel):
    """Standardized response representation for RiskRegisterItem."""
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

class RiskRegisterItemFilterCriteria(BaseModel):
    """Structured search and filter parameters for RiskRegisterItem."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RiskRegisterItemBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RiskRegisterItem records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RiskAssessmentScoreCreateSchema(BaseModel):
    """Validation schema for creating a new RiskAssessmentScore."""
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

class RiskAssessmentScoreUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RiskAssessmentScore."""
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

class RiskAssessmentScoreResponseSchema(BaseModel):
    """Standardized response representation for RiskAssessmentScore."""
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

class RiskAssessmentScoreFilterCriteria(BaseModel):
    """Structured search and filter parameters for RiskAssessmentScore."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RiskAssessmentScoreBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RiskAssessmentScore records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class KeyRiskIndicatorCreateSchema(BaseModel):
    """Validation schema for creating a new KeyRiskIndicator."""
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

class KeyRiskIndicatorUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing KeyRiskIndicator."""
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

class KeyRiskIndicatorResponseSchema(BaseModel):
    """Standardized response representation for KeyRiskIndicator."""
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

class KeyRiskIndicatorFilterCriteria(BaseModel):
    """Structured search and filter parameters for KeyRiskIndicator."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class KeyRiskIndicatorBatchActionPayload(BaseModel):
    """Batch processing payload for multiple KeyRiskIndicator records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class KRIThresholdAlertCreateSchema(BaseModel):
    """Validation schema for creating a new KRIThresholdAlert."""
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

class KRIThresholdAlertUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing KRIThresholdAlert."""
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

class KRIThresholdAlertResponseSchema(BaseModel):
    """Standardized response representation for KRIThresholdAlert."""
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

class KRIThresholdAlertFilterCriteria(BaseModel):
    """Structured search and filter parameters for KRIThresholdAlert."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class KRIThresholdAlertBatchActionPayload(BaseModel):
    """Batch processing payload for multiple KRIThresholdAlert records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RiskMitigationStrategyCreateSchema(BaseModel):
    """Validation schema for creating a new RiskMitigationStrategy."""
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

class RiskMitigationStrategyUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RiskMitigationStrategy."""
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

class RiskMitigationStrategyResponseSchema(BaseModel):
    """Standardized response representation for RiskMitigationStrategy."""
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

class RiskMitigationStrategyFilterCriteria(BaseModel):
    """Structured search and filter parameters for RiskMitigationStrategy."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RiskMitigationStrategyBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RiskMitigationStrategy records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ActionOwnerAssignmentCreateSchema(BaseModel):
    """Validation schema for creating a new ActionOwnerAssignment."""
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

class ActionOwnerAssignmentUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ActionOwnerAssignment."""
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

class ActionOwnerAssignmentResponseSchema(BaseModel):
    """Standardized response representation for ActionOwnerAssignment."""
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

class ActionOwnerAssignmentFilterCriteria(BaseModel):
    """Structured search and filter parameters for ActionOwnerAssignment."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ActionOwnerAssignmentBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ActionOwnerAssignment records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ScenarioStressTestCreateSchema(BaseModel):
    """Validation schema for creating a new ScenarioStressTest."""
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

class ScenarioStressTestUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ScenarioStressTest."""
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

class ScenarioStressTestResponseSchema(BaseModel):
    """Standardized response representation for ScenarioStressTest."""
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

class ScenarioStressTestFilterCriteria(BaseModel):
    """Structured search and filter parameters for ScenarioStressTest."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ScenarioStressTestBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ScenarioStressTest records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class LossEventIncidentCreateSchema(BaseModel):
    """Validation schema for creating a new LossEventIncident."""
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

class LossEventIncidentUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing LossEventIncident."""
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

class LossEventIncidentResponseSchema(BaseModel):
    """Standardized response representation for LossEventIncident."""
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

class LossEventIncidentFilterCriteria(BaseModel):
    """Structured search and filter parameters for LossEventIncident."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class LossEventIncidentBatchActionPayload(BaseModel):
    """Batch processing payload for multiple LossEventIncident records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class BusinessContinuityPlanCreateSchema(BaseModel):
    """Validation schema for creating a new BusinessContinuityPlan."""
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

class BusinessContinuityPlanUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing BusinessContinuityPlan."""
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

class BusinessContinuityPlanResponseSchema(BaseModel):
    """Standardized response representation for BusinessContinuityPlan."""
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

class BusinessContinuityPlanFilterCriteria(BaseModel):
    """Structured search and filter parameters for BusinessContinuityPlan."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class BusinessContinuityPlanBatchActionPayload(BaseModel):
    """Batch processing payload for multiple BusinessContinuityPlan records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class DisasterRecoveryScenarioCreateSchema(BaseModel):
    """Validation schema for creating a new DisasterRecoveryScenario."""
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

class DisasterRecoveryScenarioUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing DisasterRecoveryScenario."""
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

class DisasterRecoveryScenarioResponseSchema(BaseModel):
    """Standardized response representation for DisasterRecoveryScenario."""
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

class DisasterRecoveryScenarioFilterCriteria(BaseModel):
    """Structured search and filter parameters for DisasterRecoveryScenario."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class DisasterRecoveryScenarioBatchActionPayload(BaseModel):
    """Batch processing payload for multiple DisasterRecoveryScenario records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ResidualRiskEvaluationCreateSchema(BaseModel):
    """Validation schema for creating a new ResidualRiskEvaluation."""
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

class ResidualRiskEvaluationUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ResidualRiskEvaluation."""
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

class ResidualRiskEvaluationResponseSchema(BaseModel):
    """Standardized response representation for ResidualRiskEvaluation."""
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

class ResidualRiskEvaluationFilterCriteria(BaseModel):
    """Structured search and filter parameters for ResidualRiskEvaluation."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ResidualRiskEvaluationBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ResidualRiskEvaluation records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RiskAppetiteStatementCreateSchema(BaseModel):
    """Validation schema for creating a new RiskAppetiteStatement."""
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

class RiskAppetiteStatementUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RiskAppetiteStatement."""
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

class RiskAppetiteStatementResponseSchema(BaseModel):
    """Standardized response representation for RiskAppetiteStatement."""
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

class RiskAppetiteStatementFilterCriteria(BaseModel):
    """Structured search and filter parameters for RiskAppetiteStatement."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RiskAppetiteStatementBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RiskAppetiteStatement records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class InsuranceCoverageLinkCreateSchema(BaseModel):
    """Validation schema for creating a new InsuranceCoverageLink."""
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

class InsuranceCoverageLinkUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing InsuranceCoverageLink."""
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

class InsuranceCoverageLinkResponseSchema(BaseModel):
    """Standardized response representation for InsuranceCoverageLink."""
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

class InsuranceCoverageLinkFilterCriteria(BaseModel):
    """Structured search and filter parameters for InsuranceCoverageLink."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class InsuranceCoverageLinkBatchActionPayload(BaseModel):
    """Batch processing payload for multiple InsuranceCoverageLink records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RiskCommitteeReportCreateSchema(BaseModel):
    """Validation schema for creating a new RiskCommitteeReport."""
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

class RiskCommitteeReportUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RiskCommitteeReport."""
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

class RiskCommitteeReportResponseSchema(BaseModel):
    """Standardized response representation for RiskCommitteeReport."""
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

class RiskCommitteeReportFilterCriteria(BaseModel):
    """Structured search and filter parameters for RiskCommitteeReport."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RiskCommitteeReportBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RiskCommitteeReport records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class AuditRecommendationCreateSchema(BaseModel):
    """Validation schema for creating a new AuditRecommendation."""
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

class AuditRecommendationUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing AuditRecommendation."""
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

class AuditRecommendationResponseSchema(BaseModel):
    """Standardized response representation for AuditRecommendation."""
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

class AuditRecommendationFilterCriteria(BaseModel):
    """Structured search and filter parameters for AuditRecommendation."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class AuditRecommendationBatchActionPayload(BaseModel):
    """Batch processing payload for multiple AuditRecommendation records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

