"""
Enterprise API Gateway & Integration Hub - Pydantic Request & Response Validation Schemas
"""
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from .models import RecordStatus, PriorityLevel, RiskClassification

class APIEndpointDefinitionCreateSchema(BaseModel):
    """Validation schema for creating a new APIEndpointDefinition."""
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

class APIEndpointDefinitionUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing APIEndpointDefinition."""
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

class APIEndpointDefinitionResponseSchema(BaseModel):
    """Standardized response representation for APIEndpointDefinition."""
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

class APIEndpointDefinitionFilterCriteria(BaseModel):
    """Structured search and filter parameters for APIEndpointDefinition."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class APIEndpointDefinitionBatchActionPayload(BaseModel):
    """Batch processing payload for multiple APIEndpointDefinition records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class APIConsumerApplicationCreateSchema(BaseModel):
    """Validation schema for creating a new APIConsumerApplication."""
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

class APIConsumerApplicationUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing APIConsumerApplication."""
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

class APIConsumerApplicationResponseSchema(BaseModel):
    """Standardized response representation for APIConsumerApplication."""
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

class APIConsumerApplicationFilterCriteria(BaseModel):
    """Structured search and filter parameters for APIConsumerApplication."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class APIConsumerApplicationBatchActionPayload(BaseModel):
    """Batch processing payload for multiple APIConsumerApplication records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class APIKeyCredentialCreateSchema(BaseModel):
    """Validation schema for creating a new APIKeyCredential."""
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

class APIKeyCredentialUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing APIKeyCredential."""
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

class APIKeyCredentialResponseSchema(BaseModel):
    """Standardized response representation for APIKeyCredential."""
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

class APIKeyCredentialFilterCriteria(BaseModel):
    """Structured search and filter parameters for APIKeyCredential."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class APIKeyCredentialBatchActionPayload(BaseModel):
    """Batch processing payload for multiple APIKeyCredential records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RateLimitQuotaRuleCreateSchema(BaseModel):
    """Validation schema for creating a new RateLimitQuotaRule."""
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

class RateLimitQuotaRuleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RateLimitQuotaRule."""
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

class RateLimitQuotaRuleResponseSchema(BaseModel):
    """Standardized response representation for RateLimitQuotaRule."""
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

class RateLimitQuotaRuleFilterCriteria(BaseModel):
    """Structured search and filter parameters for RateLimitQuotaRule."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RateLimitQuotaRuleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RateLimitQuotaRule records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class OAuthScopePermissionCreateSchema(BaseModel):
    """Validation schema for creating a new OAuthScopePermission."""
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

class OAuthScopePermissionUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing OAuthScopePermission."""
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

class OAuthScopePermissionResponseSchema(BaseModel):
    """Standardized response representation for OAuthScopePermission."""
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

class OAuthScopePermissionFilterCriteria(BaseModel):
    """Structured search and filter parameters for OAuthScopePermission."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class OAuthScopePermissionBatchActionPayload(BaseModel):
    """Batch processing payload for multiple OAuthScopePermission records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class WebhookSubscriptionTargetCreateSchema(BaseModel):
    """Validation schema for creating a new WebhookSubscriptionTarget."""
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

class WebhookSubscriptionTargetUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing WebhookSubscriptionTarget."""
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

class WebhookSubscriptionTargetResponseSchema(BaseModel):
    """Standardized response representation for WebhookSubscriptionTarget."""
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

class WebhookSubscriptionTargetFilterCriteria(BaseModel):
    """Structured search and filter parameters for WebhookSubscriptionTarget."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class WebhookSubscriptionTargetBatchActionPayload(BaseModel):
    """Batch processing payload for multiple WebhookSubscriptionTarget records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class PayloadTransformationMapCreateSchema(BaseModel):
    """Validation schema for creating a new PayloadTransformationMap."""
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

class PayloadTransformationMapUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing PayloadTransformationMap."""
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

class PayloadTransformationMapResponseSchema(BaseModel):
    """Standardized response representation for PayloadTransformationMap."""
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

class PayloadTransformationMapFilterCriteria(BaseModel):
    """Structured search and filter parameters for PayloadTransformationMap."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class PayloadTransformationMapBatchActionPayload(BaseModel):
    """Batch processing payload for multiple PayloadTransformationMap records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class GatewayTrafficMetricCreateSchema(BaseModel):
    """Validation schema for creating a new GatewayTrafficMetric."""
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

class GatewayTrafficMetricUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing GatewayTrafficMetric."""
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

class GatewayTrafficMetricResponseSchema(BaseModel):
    """Standardized response representation for GatewayTrafficMetric."""
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

class GatewayTrafficMetricFilterCriteria(BaseModel):
    """Structured search and filter parameters for GatewayTrafficMetric."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class GatewayTrafficMetricBatchActionPayload(BaseModel):
    """Batch processing payload for multiple GatewayTrafficMetric records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class SecurityFirewallRuleCreateSchema(BaseModel):
    """Validation schema for creating a new SecurityFirewallRule."""
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

class SecurityFirewallRuleUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing SecurityFirewallRule."""
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

class SecurityFirewallRuleResponseSchema(BaseModel):
    """Standardized response representation for SecurityFirewallRule."""
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

class SecurityFirewallRuleFilterCriteria(BaseModel):
    """Structured search and filter parameters for SecurityFirewallRule."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class SecurityFirewallRuleBatchActionPayload(BaseModel):
    """Batch processing payload for multiple SecurityFirewallRule records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class IPAllowlistEntryCreateSchema(BaseModel):
    """Validation schema for creating a new IPAllowlistEntry."""
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

class IPAllowlistEntryUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing IPAllowlistEntry."""
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

class IPAllowlistEntryResponseSchema(BaseModel):
    """Standardized response representation for IPAllowlistEntry."""
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

class IPAllowlistEntryFilterCriteria(BaseModel):
    """Structured search and filter parameters for IPAllowlistEntry."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class IPAllowlistEntryBatchActionPayload(BaseModel):
    """Batch processing payload for multiple IPAllowlistEntry records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class CircuitBreakerStateCreateSchema(BaseModel):
    """Validation schema for creating a new CircuitBreakerState."""
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

class CircuitBreakerStateUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing CircuitBreakerState."""
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

class CircuitBreakerStateResponseSchema(BaseModel):
    """Standardized response representation for CircuitBreakerState."""
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

class CircuitBreakerStateFilterCriteria(BaseModel):
    """Structured search and filter parameters for CircuitBreakerState."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class CircuitBreakerStateBatchActionPayload(BaseModel):
    """Batch processing payload for multiple CircuitBreakerState records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class APIVersionReleaseCreateSchema(BaseModel):
    """Validation schema for creating a new APIVersionRelease."""
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

class APIVersionReleaseUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing APIVersionRelease."""
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

class APIVersionReleaseResponseSchema(BaseModel):
    """Standardized response representation for APIVersionRelease."""
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

class APIVersionReleaseFilterCriteria(BaseModel):
    """Structured search and filter parameters for APIVersionRelease."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class APIVersionReleaseBatchActionPayload(BaseModel):
    """Batch processing payload for multiple APIVersionRelease records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class RequestResponseAuditLogCreateSchema(BaseModel):
    """Validation schema for creating a new RequestResponseAuditLog."""
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

class RequestResponseAuditLogUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing RequestResponseAuditLog."""
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

class RequestResponseAuditLogResponseSchema(BaseModel):
    """Standardized response representation for RequestResponseAuditLog."""
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

class RequestResponseAuditLogFilterCriteria(BaseModel):
    """Structured search and filter parameters for RequestResponseAuditLog."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class RequestResponseAuditLogBatchActionPayload(BaseModel):
    """Batch processing payload for multiple RequestResponseAuditLog records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class MockResponseTemplateCreateSchema(BaseModel):
    """Validation schema for creating a new MockResponseTemplate."""
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

class MockResponseTemplateUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing MockResponseTemplate."""
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

class MockResponseTemplateResponseSchema(BaseModel):
    """Standardized response representation for MockResponseTemplate."""
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

class MockResponseTemplateFilterCriteria(BaseModel):
    """Structured search and filter parameters for MockResponseTemplate."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class MockResponseTemplateBatchActionPayload(BaseModel):
    """Batch processing payload for multiple MockResponseTemplate records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class IntegrationConnectorCreateSchema(BaseModel):
    """Validation schema for creating a new IntegrationConnector."""
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

class IntegrationConnectorUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing IntegrationConnector."""
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

class IntegrationConnectorResponseSchema(BaseModel):
    """Standardized response representation for IntegrationConnector."""
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

class IntegrationConnectorFilterCriteria(BaseModel):
    """Structured search and filter parameters for IntegrationConnector."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class IntegrationConnectorBatchActionPayload(BaseModel):
    """Batch processing payload for multiple IntegrationConnector records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

class ServiceMeshProxyCreateSchema(BaseModel):
    """Validation schema for creating a new ServiceMeshProxy."""
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

class ServiceMeshProxyUpdateSchema(BaseModel):
    """Validation schema for partial updating of an existing ServiceMeshProxy."""
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

class ServiceMeshProxyResponseSchema(BaseModel):
    """Standardized response representation for ServiceMeshProxy."""
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

class ServiceMeshProxyFilterCriteria(BaseModel):
    """Structured search and filter parameters for ServiceMeshProxy."""
    status: Optional[str] = None
    priority: Optional[str] = None
    search_query: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    organization_id: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)

class ServiceMeshProxyBatchActionPayload(BaseModel):
    """Batch processing payload for multiple ServiceMeshProxy records."""
    item_ids: List[int] = Field(..., min_items=1, max_items=1000)
    action: str = Field(..., description="Action name: ARCHIVE, APPROVE, REJECT, DELETE")
    reason: Optional[str] = Field(None, max_length=500)

