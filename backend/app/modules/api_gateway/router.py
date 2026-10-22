"""
Enterprise API Gateway & Integration Hub - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    APIEndpointDefinitionService,
    APIConsumerApplicationService,
    APIKeyCredentialService,
    RateLimitQuotaRuleService,
    OAuthScopePermissionService,
    WebhookSubscriptionTargetService,
    PayloadTransformationMapService,
    GatewayTrafficMetricService,
    SecurityFirewallRuleService,
    IPAllowlistEntryService,
    CircuitBreakerStateService,
    APIVersionReleaseService,
    RequestResponseAuditLogService,
    MockResponseTemplateService,
    IntegrationConnectorService,
    ServiceMeshProxyService,
)
from .schemas import (
    APIEndpointDefinitionCreateSchema, APIEndpointDefinitionUpdateSchema, APIEndpointDefinitionResponseSchema,
    APIConsumerApplicationCreateSchema, APIConsumerApplicationUpdateSchema, APIConsumerApplicationResponseSchema,
    APIKeyCredentialCreateSchema, APIKeyCredentialUpdateSchema, APIKeyCredentialResponseSchema,
    RateLimitQuotaRuleCreateSchema, RateLimitQuotaRuleUpdateSchema, RateLimitQuotaRuleResponseSchema,
    OAuthScopePermissionCreateSchema, OAuthScopePermissionUpdateSchema, OAuthScopePermissionResponseSchema,
    WebhookSubscriptionTargetCreateSchema, WebhookSubscriptionTargetUpdateSchema, WebhookSubscriptionTargetResponseSchema,
    PayloadTransformationMapCreateSchema, PayloadTransformationMapUpdateSchema, PayloadTransformationMapResponseSchema,
    GatewayTrafficMetricCreateSchema, GatewayTrafficMetricUpdateSchema, GatewayTrafficMetricResponseSchema,
    SecurityFirewallRuleCreateSchema, SecurityFirewallRuleUpdateSchema, SecurityFirewallRuleResponseSchema,
    IPAllowlistEntryCreateSchema, IPAllowlistEntryUpdateSchema, IPAllowlistEntryResponseSchema,
    CircuitBreakerStateCreateSchema, CircuitBreakerStateUpdateSchema, CircuitBreakerStateResponseSchema,
    APIVersionReleaseCreateSchema, APIVersionReleaseUpdateSchema, APIVersionReleaseResponseSchema,
    RequestResponseAuditLogCreateSchema, RequestResponseAuditLogUpdateSchema, RequestResponseAuditLogResponseSchema,
    MockResponseTemplateCreateSchema, MockResponseTemplateUpdateSchema, MockResponseTemplateResponseSchema,
    IntegrationConnectorCreateSchema, IntegrationConnectorUpdateSchema, IntegrationConnectorResponseSchema,
    ServiceMeshProxyCreateSchema, ServiceMeshProxyUpdateSchema, ServiceMeshProxyResponseSchema,
)

router = APIRouter(prefix="/api_gateway", tags=["Enterprise API Gateway & Integration Hub"])

# ==================== APIEndpointDefinition Endpoints ====================
@router.get("/apiendpointdefinitions", response_model=List[Dict[str, Any]])
def list_apiendpointdefinitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List APIEndpointDefinition records with pagination and filtering."""
    svc = APIEndpointDefinitionService()
    items = svc.list_apiendpointdefinitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/apiendpointdefinitions/{item_id}", response_model=Dict[str, Any])
def get_apiendpointdefinition_by_id(item_id: int):
    """Retrieve detailed record for APIEndpointDefinition by ID."""
    svc = APIEndpointDefinitionService()
    item = svc.get_apiendpointdefinition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"APIEndpointDefinition with ID {item_id} not found")
    return item.to_dict()

@router.post("/apiendpointdefinitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_apiendpointdefinition(payload: APIEndpointDefinitionCreateSchema):
    """Create new APIEndpointDefinition instance in enterprise repository."""
    svc = APIEndpointDefinitionService()
    try:
        item = svc.create_apiendpointdefinition(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/apiendpointdefinitions/{item_id}", response_model=Dict[str, Any])
def update_apiendpointdefinition(item_id: int, payload: APIEndpointDefinitionUpdateSchema):
    """Update existing APIEndpointDefinition record fields."""
    svc = APIEndpointDefinitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_apiendpointdefinition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"APIEndpointDefinition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/apiendpointdefinitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_apiendpointdefinition(item_id: int, hard: bool = Query(False)):
    """Delete APIEndpointDefinition record (soft-delete by default)."""
    svc = APIEndpointDefinitionService()
    ok = svc.delete_apiendpointdefinition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"APIEndpointDefinition with ID {item_id} not found")
    return None

@router.get("/apiendpointdefinitions/analytics/metrics", response_model=Dict[str, Any])
def get_apiendpointdefinition_metrics():
    """Calculate summary statistical KPIs for APIEndpointDefinition collection."""
    svc = APIEndpointDefinitionService()
    return svc.calculate_aggregate_metrics()

# ==================== APIConsumerApplication Endpoints ====================
@router.get("/apiconsumerapplications", response_model=List[Dict[str, Any]])
def list_apiconsumerapplications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List APIConsumerApplication records with pagination and filtering."""
    svc = APIConsumerApplicationService()
    items = svc.list_apiconsumerapplications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/apiconsumerapplications/{item_id}", response_model=Dict[str, Any])
def get_apiconsumerapplication_by_id(item_id: int):
    """Retrieve detailed record for APIConsumerApplication by ID."""
    svc = APIConsumerApplicationService()
    item = svc.get_apiconsumerapplication_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"APIConsumerApplication with ID {item_id} not found")
    return item.to_dict()

@router.post("/apiconsumerapplications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_apiconsumerapplication(payload: APIConsumerApplicationCreateSchema):
    """Create new APIConsumerApplication instance in enterprise repository."""
    svc = APIConsumerApplicationService()
    try:
        item = svc.create_apiconsumerapplication(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/apiconsumerapplications/{item_id}", response_model=Dict[str, Any])
def update_apiconsumerapplication(item_id: int, payload: APIConsumerApplicationUpdateSchema):
    """Update existing APIConsumerApplication record fields."""
    svc = APIConsumerApplicationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_apiconsumerapplication(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"APIConsumerApplication with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/apiconsumerapplications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_apiconsumerapplication(item_id: int, hard: bool = Query(False)):
    """Delete APIConsumerApplication record (soft-delete by default)."""
    svc = APIConsumerApplicationService()
    ok = svc.delete_apiconsumerapplication(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"APIConsumerApplication with ID {item_id} not found")
    return None

@router.get("/apiconsumerapplications/analytics/metrics", response_model=Dict[str, Any])
def get_apiconsumerapplication_metrics():
    """Calculate summary statistical KPIs for APIConsumerApplication collection."""
    svc = APIConsumerApplicationService()
    return svc.calculate_aggregate_metrics()

# ==================== APIKeyCredential Endpoints ====================
@router.get("/apikeycredentials", response_model=List[Dict[str, Any]])
def list_apikeycredentials(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List APIKeyCredential records with pagination and filtering."""
    svc = APIKeyCredentialService()
    items = svc.list_apikeycredentials(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/apikeycredentials/{item_id}", response_model=Dict[str, Any])
def get_apikeycredential_by_id(item_id: int):
    """Retrieve detailed record for APIKeyCredential by ID."""
    svc = APIKeyCredentialService()
    item = svc.get_apikeycredential_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"APIKeyCredential with ID {item_id} not found")
    return item.to_dict()

@router.post("/apikeycredentials", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_apikeycredential(payload: APIKeyCredentialCreateSchema):
    """Create new APIKeyCredential instance in enterprise repository."""
    svc = APIKeyCredentialService()
    try:
        item = svc.create_apikeycredential(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/apikeycredentials/{item_id}", response_model=Dict[str, Any])
def update_apikeycredential(item_id: int, payload: APIKeyCredentialUpdateSchema):
    """Update existing APIKeyCredential record fields."""
    svc = APIKeyCredentialService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_apikeycredential(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"APIKeyCredential with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/apikeycredentials/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_apikeycredential(item_id: int, hard: bool = Query(False)):
    """Delete APIKeyCredential record (soft-delete by default)."""
    svc = APIKeyCredentialService()
    ok = svc.delete_apikeycredential(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"APIKeyCredential with ID {item_id} not found")
    return None

@router.get("/apikeycredentials/analytics/metrics", response_model=Dict[str, Any])
def get_apikeycredential_metrics():
    """Calculate summary statistical KPIs for APIKeyCredential collection."""
    svc = APIKeyCredentialService()
    return svc.calculate_aggregate_metrics()

# ==================== RateLimitQuotaRule Endpoints ====================
@router.get("/ratelimitquotarules", response_model=List[Dict[str, Any]])
def list_ratelimitquotarules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RateLimitQuotaRule records with pagination and filtering."""
    svc = RateLimitQuotaRuleService()
    items = svc.list_ratelimitquotarules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ratelimitquotarules/{item_id}", response_model=Dict[str, Any])
def get_ratelimitquotarule_by_id(item_id: int):
    """Retrieve detailed record for RateLimitQuotaRule by ID."""
    svc = RateLimitQuotaRuleService()
    item = svc.get_ratelimitquotarule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RateLimitQuotaRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/ratelimitquotarules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ratelimitquotarule(payload: RateLimitQuotaRuleCreateSchema):
    """Create new RateLimitQuotaRule instance in enterprise repository."""
    svc = RateLimitQuotaRuleService()
    try:
        item = svc.create_ratelimitquotarule(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/ratelimitquotarules/{item_id}", response_model=Dict[str, Any])
def update_ratelimitquotarule(item_id: int, payload: RateLimitQuotaRuleUpdateSchema):
    """Update existing RateLimitQuotaRule record fields."""
    svc = RateLimitQuotaRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ratelimitquotarule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RateLimitQuotaRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ratelimitquotarules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ratelimitquotarule(item_id: int, hard: bool = Query(False)):
    """Delete RateLimitQuotaRule record (soft-delete by default)."""
    svc = RateLimitQuotaRuleService()
    ok = svc.delete_ratelimitquotarule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RateLimitQuotaRule with ID {item_id} not found")
    return None

@router.get("/ratelimitquotarules/analytics/metrics", response_model=Dict[str, Any])
def get_ratelimitquotarule_metrics():
    """Calculate summary statistical KPIs for RateLimitQuotaRule collection."""
    svc = RateLimitQuotaRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== OAuthScopePermission Endpoints ====================
@router.get("/oauthscopepermissions", response_model=List[Dict[str, Any]])
def list_oauthscopepermissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OAuthScopePermission records with pagination and filtering."""
    svc = OAuthScopePermissionService()
    items = svc.list_oauthscopepermissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/oauthscopepermissions/{item_id}", response_model=Dict[str, Any])
def get_oauthscopepermission_by_id(item_id: int):
    """Retrieve detailed record for OAuthScopePermission by ID."""
    svc = OAuthScopePermissionService()
    item = svc.get_oauthscopepermission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OAuthScopePermission with ID {item_id} not found")
    return item.to_dict()

@router.post("/oauthscopepermissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_oauthscopepermission(payload: OAuthScopePermissionCreateSchema):
    """Create new OAuthScopePermission instance in enterprise repository."""
    svc = OAuthScopePermissionService()
    try:
        item = svc.create_oauthscopepermission(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/oauthscopepermissions/{item_id}", response_model=Dict[str, Any])
def update_oauthscopepermission(item_id: int, payload: OAuthScopePermissionUpdateSchema):
    """Update existing OAuthScopePermission record fields."""
    svc = OAuthScopePermissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_oauthscopepermission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OAuthScopePermission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/oauthscopepermissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_oauthscopepermission(item_id: int, hard: bool = Query(False)):
    """Delete OAuthScopePermission record (soft-delete by default)."""
    svc = OAuthScopePermissionService()
    ok = svc.delete_oauthscopepermission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OAuthScopePermission with ID {item_id} not found")
    return None

@router.get("/oauthscopepermissions/analytics/metrics", response_model=Dict[str, Any])
def get_oauthscopepermission_metrics():
    """Calculate summary statistical KPIs for OAuthScopePermission collection."""
    svc = OAuthScopePermissionService()
    return svc.calculate_aggregate_metrics()

# ==================== WebhookSubscriptionTarget Endpoints ====================
@router.get("/webhooksubscriptiontargets", response_model=List[Dict[str, Any]])
def list_webhooksubscriptiontargets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WebhookSubscriptionTarget records with pagination and filtering."""
    svc = WebhookSubscriptionTargetService()
    items = svc.list_webhooksubscriptiontargets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/webhooksubscriptiontargets/{item_id}", response_model=Dict[str, Any])
def get_webhooksubscriptiontarget_by_id(item_id: int):
    """Retrieve detailed record for WebhookSubscriptionTarget by ID."""
    svc = WebhookSubscriptionTargetService()
    item = svc.get_webhooksubscriptiontarget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WebhookSubscriptionTarget with ID {item_id} not found")
    return item.to_dict()

@router.post("/webhooksubscriptiontargets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_webhooksubscriptiontarget(payload: WebhookSubscriptionTargetCreateSchema):
    """Create new WebhookSubscriptionTarget instance in enterprise repository."""
    svc = WebhookSubscriptionTargetService()
    try:
        item = svc.create_webhooksubscriptiontarget(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/webhooksubscriptiontargets/{item_id}", response_model=Dict[str, Any])
def update_webhooksubscriptiontarget(item_id: int, payload: WebhookSubscriptionTargetUpdateSchema):
    """Update existing WebhookSubscriptionTarget record fields."""
    svc = WebhookSubscriptionTargetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_webhooksubscriptiontarget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WebhookSubscriptionTarget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/webhooksubscriptiontargets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_webhooksubscriptiontarget(item_id: int, hard: bool = Query(False)):
    """Delete WebhookSubscriptionTarget record (soft-delete by default)."""
    svc = WebhookSubscriptionTargetService()
    ok = svc.delete_webhooksubscriptiontarget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WebhookSubscriptionTarget with ID {item_id} not found")
    return None

@router.get("/webhooksubscriptiontargets/analytics/metrics", response_model=Dict[str, Any])
def get_webhooksubscriptiontarget_metrics():
    """Calculate summary statistical KPIs for WebhookSubscriptionTarget collection."""
    svc = WebhookSubscriptionTargetService()
    return svc.calculate_aggregate_metrics()

# ==================== PayloadTransformationMap Endpoints ====================
@router.get("/payloadtransformationmaps", response_model=List[Dict[str, Any]])
def list_payloadtransformationmaps(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PayloadTransformationMap records with pagination and filtering."""
    svc = PayloadTransformationMapService()
    items = svc.list_payloadtransformationmaps(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/payloadtransformationmaps/{item_id}", response_model=Dict[str, Any])
def get_payloadtransformationmap_by_id(item_id: int):
    """Retrieve detailed record for PayloadTransformationMap by ID."""
    svc = PayloadTransformationMapService()
    item = svc.get_payloadtransformationmap_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PayloadTransformationMap with ID {item_id} not found")
    return item.to_dict()

@router.post("/payloadtransformationmaps", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_payloadtransformationmap(payload: PayloadTransformationMapCreateSchema):
    """Create new PayloadTransformationMap instance in enterprise repository."""
    svc = PayloadTransformationMapService()
    try:
        item = svc.create_payloadtransformationmap(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/payloadtransformationmaps/{item_id}", response_model=Dict[str, Any])
def update_payloadtransformationmap(item_id: int, payload: PayloadTransformationMapUpdateSchema):
    """Update existing PayloadTransformationMap record fields."""
    svc = PayloadTransformationMapService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_payloadtransformationmap(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PayloadTransformationMap with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/payloadtransformationmaps/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payloadtransformationmap(item_id: int, hard: bool = Query(False)):
    """Delete PayloadTransformationMap record (soft-delete by default)."""
    svc = PayloadTransformationMapService()
    ok = svc.delete_payloadtransformationmap(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PayloadTransformationMap with ID {item_id} not found")
    return None

@router.get("/payloadtransformationmaps/analytics/metrics", response_model=Dict[str, Any])
def get_payloadtransformationmap_metrics():
    """Calculate summary statistical KPIs for PayloadTransformationMap collection."""
    svc = PayloadTransformationMapService()
    return svc.calculate_aggregate_metrics()

# ==================== GatewayTrafficMetric Endpoints ====================
@router.get("/gatewaytrafficmetrics", response_model=List[Dict[str, Any]])
def list_gatewaytrafficmetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GatewayTrafficMetric records with pagination and filtering."""
    svc = GatewayTrafficMetricService()
    items = svc.list_gatewaytrafficmetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/gatewaytrafficmetrics/{item_id}", response_model=Dict[str, Any])
def get_gatewaytrafficmetric_by_id(item_id: int):
    """Retrieve detailed record for GatewayTrafficMetric by ID."""
    svc = GatewayTrafficMetricService()
    item = svc.get_gatewaytrafficmetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GatewayTrafficMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/gatewaytrafficmetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_gatewaytrafficmetric(payload: GatewayTrafficMetricCreateSchema):
    """Create new GatewayTrafficMetric instance in enterprise repository."""
    svc = GatewayTrafficMetricService()
    try:
        item = svc.create_gatewaytrafficmetric(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/gatewaytrafficmetrics/{item_id}", response_model=Dict[str, Any])
def update_gatewaytrafficmetric(item_id: int, payload: GatewayTrafficMetricUpdateSchema):
    """Update existing GatewayTrafficMetric record fields."""
    svc = GatewayTrafficMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_gatewaytrafficmetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GatewayTrafficMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/gatewaytrafficmetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gatewaytrafficmetric(item_id: int, hard: bool = Query(False)):
    """Delete GatewayTrafficMetric record (soft-delete by default)."""
    svc = GatewayTrafficMetricService()
    ok = svc.delete_gatewaytrafficmetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GatewayTrafficMetric with ID {item_id} not found")
    return None

@router.get("/gatewaytrafficmetrics/analytics/metrics", response_model=Dict[str, Any])
def get_gatewaytrafficmetric_metrics():
    """Calculate summary statistical KPIs for GatewayTrafficMetric collection."""
    svc = GatewayTrafficMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== SecurityFirewallRule Endpoints ====================
@router.get("/securityfirewallrules", response_model=List[Dict[str, Any]])
def list_securityfirewallrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SecurityFirewallRule records with pagination and filtering."""
    svc = SecurityFirewallRuleService()
    items = svc.list_securityfirewallrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/securityfirewallrules/{item_id}", response_model=Dict[str, Any])
def get_securityfirewallrule_by_id(item_id: int):
    """Retrieve detailed record for SecurityFirewallRule by ID."""
    svc = SecurityFirewallRuleService()
    item = svc.get_securityfirewallrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SecurityFirewallRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/securityfirewallrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_securityfirewallrule(payload: SecurityFirewallRuleCreateSchema):
    """Create new SecurityFirewallRule instance in enterprise repository."""
    svc = SecurityFirewallRuleService()
    try:
        item = svc.create_securityfirewallrule(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/securityfirewallrules/{item_id}", response_model=Dict[str, Any])
def update_securityfirewallrule(item_id: int, payload: SecurityFirewallRuleUpdateSchema):
    """Update existing SecurityFirewallRule record fields."""
    svc = SecurityFirewallRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_securityfirewallrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SecurityFirewallRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/securityfirewallrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_securityfirewallrule(item_id: int, hard: bool = Query(False)):
    """Delete SecurityFirewallRule record (soft-delete by default)."""
    svc = SecurityFirewallRuleService()
    ok = svc.delete_securityfirewallrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SecurityFirewallRule with ID {item_id} not found")
    return None

@router.get("/securityfirewallrules/analytics/metrics", response_model=Dict[str, Any])
def get_securityfirewallrule_metrics():
    """Calculate summary statistical KPIs for SecurityFirewallRule collection."""
    svc = SecurityFirewallRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== IPAllowlistEntry Endpoints ====================
@router.get("/ipallowlistentrys", response_model=List[Dict[str, Any]])
def list_ipallowlistentrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IPAllowlistEntry records with pagination and filtering."""
    svc = IPAllowlistEntryService()
    items = svc.list_ipallowlistentrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ipallowlistentrys/{item_id}", response_model=Dict[str, Any])
def get_ipallowlistentry_by_id(item_id: int):
    """Retrieve detailed record for IPAllowlistEntry by ID."""
    svc = IPAllowlistEntryService()
    item = svc.get_ipallowlistentry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IPAllowlistEntry with ID {item_id} not found")
    return item.to_dict()

@router.post("/ipallowlistentrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ipallowlistentry(payload: IPAllowlistEntryCreateSchema):
    """Create new IPAllowlistEntry instance in enterprise repository."""
    svc = IPAllowlistEntryService()
    try:
        item = svc.create_ipallowlistentry(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/ipallowlistentrys/{item_id}", response_model=Dict[str, Any])
def update_ipallowlistentry(item_id: int, payload: IPAllowlistEntryUpdateSchema):
    """Update existing IPAllowlistEntry record fields."""
    svc = IPAllowlistEntryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ipallowlistentry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IPAllowlistEntry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ipallowlistentrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ipallowlistentry(item_id: int, hard: bool = Query(False)):
    """Delete IPAllowlistEntry record (soft-delete by default)."""
    svc = IPAllowlistEntryService()
    ok = svc.delete_ipallowlistentry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IPAllowlistEntry with ID {item_id} not found")
    return None

@router.get("/ipallowlistentrys/analytics/metrics", response_model=Dict[str, Any])
def get_ipallowlistentry_metrics():
    """Calculate summary statistical KPIs for IPAllowlistEntry collection."""
    svc = IPAllowlistEntryService()
    return svc.calculate_aggregate_metrics()

# ==================== CircuitBreakerState Endpoints ====================
@router.get("/circuitbreakerstates", response_model=List[Dict[str, Any]])
def list_circuitbreakerstates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CircuitBreakerState records with pagination and filtering."""
    svc = CircuitBreakerStateService()
    items = svc.list_circuitbreakerstates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/circuitbreakerstates/{item_id}", response_model=Dict[str, Any])
def get_circuitbreakerstate_by_id(item_id: int):
    """Retrieve detailed record for CircuitBreakerState by ID."""
    svc = CircuitBreakerStateService()
    item = svc.get_circuitbreakerstate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CircuitBreakerState with ID {item_id} not found")
    return item.to_dict()

@router.post("/circuitbreakerstates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_circuitbreakerstate(payload: CircuitBreakerStateCreateSchema):
    """Create new CircuitBreakerState instance in enterprise repository."""
    svc = CircuitBreakerStateService()
    try:
        item = svc.create_circuitbreakerstate(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/circuitbreakerstates/{item_id}", response_model=Dict[str, Any])
def update_circuitbreakerstate(item_id: int, payload: CircuitBreakerStateUpdateSchema):
    """Update existing CircuitBreakerState record fields."""
    svc = CircuitBreakerStateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_circuitbreakerstate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CircuitBreakerState with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/circuitbreakerstates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_circuitbreakerstate(item_id: int, hard: bool = Query(False)):
    """Delete CircuitBreakerState record (soft-delete by default)."""
    svc = CircuitBreakerStateService()
    ok = svc.delete_circuitbreakerstate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CircuitBreakerState with ID {item_id} not found")
    return None

@router.get("/circuitbreakerstates/analytics/metrics", response_model=Dict[str, Any])
def get_circuitbreakerstate_metrics():
    """Calculate summary statistical KPIs for CircuitBreakerState collection."""
    svc = CircuitBreakerStateService()
    return svc.calculate_aggregate_metrics()

# ==================== APIVersionRelease Endpoints ====================
@router.get("/apiversionreleases", response_model=List[Dict[str, Any]])
def list_apiversionreleases(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List APIVersionRelease records with pagination and filtering."""
    svc = APIVersionReleaseService()
    items = svc.list_apiversionreleases(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/apiversionreleases/{item_id}", response_model=Dict[str, Any])
def get_apiversionrelease_by_id(item_id: int):
    """Retrieve detailed record for APIVersionRelease by ID."""
    svc = APIVersionReleaseService()
    item = svc.get_apiversionrelease_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"APIVersionRelease with ID {item_id} not found")
    return item.to_dict()

@router.post("/apiversionreleases", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_apiversionrelease(payload: APIVersionReleaseCreateSchema):
    """Create new APIVersionRelease instance in enterprise repository."""
    svc = APIVersionReleaseService()
    try:
        item = svc.create_apiversionrelease(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/apiversionreleases/{item_id}", response_model=Dict[str, Any])
def update_apiversionrelease(item_id: int, payload: APIVersionReleaseUpdateSchema):
    """Update existing APIVersionRelease record fields."""
    svc = APIVersionReleaseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_apiversionrelease(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"APIVersionRelease with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/apiversionreleases/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_apiversionrelease(item_id: int, hard: bool = Query(False)):
    """Delete APIVersionRelease record (soft-delete by default)."""
    svc = APIVersionReleaseService()
    ok = svc.delete_apiversionrelease(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"APIVersionRelease with ID {item_id} not found")
    return None

@router.get("/apiversionreleases/analytics/metrics", response_model=Dict[str, Any])
def get_apiversionrelease_metrics():
    """Calculate summary statistical KPIs for APIVersionRelease collection."""
    svc = APIVersionReleaseService()
    return svc.calculate_aggregate_metrics()

# ==================== RequestResponseAuditLog Endpoints ====================
@router.get("/requestresponseauditlogs", response_model=List[Dict[str, Any]])
def list_requestresponseauditlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RequestResponseAuditLog records with pagination and filtering."""
    svc = RequestResponseAuditLogService()
    items = svc.list_requestresponseauditlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/requestresponseauditlogs/{item_id}", response_model=Dict[str, Any])
def get_requestresponseauditlog_by_id(item_id: int):
    """Retrieve detailed record for RequestResponseAuditLog by ID."""
    svc = RequestResponseAuditLogService()
    item = svc.get_requestresponseauditlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RequestResponseAuditLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/requestresponseauditlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_requestresponseauditlog(payload: RequestResponseAuditLogCreateSchema):
    """Create new RequestResponseAuditLog instance in enterprise repository."""
    svc = RequestResponseAuditLogService()
    try:
        item = svc.create_requestresponseauditlog(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/requestresponseauditlogs/{item_id}", response_model=Dict[str, Any])
def update_requestresponseauditlog(item_id: int, payload: RequestResponseAuditLogUpdateSchema):
    """Update existing RequestResponseAuditLog record fields."""
    svc = RequestResponseAuditLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_requestresponseauditlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RequestResponseAuditLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/requestresponseauditlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_requestresponseauditlog(item_id: int, hard: bool = Query(False)):
    """Delete RequestResponseAuditLog record (soft-delete by default)."""
    svc = RequestResponseAuditLogService()
    ok = svc.delete_requestresponseauditlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RequestResponseAuditLog with ID {item_id} not found")
    return None

@router.get("/requestresponseauditlogs/analytics/metrics", response_model=Dict[str, Any])
def get_requestresponseauditlog_metrics():
    """Calculate summary statistical KPIs for RequestResponseAuditLog collection."""
    svc = RequestResponseAuditLogService()
    return svc.calculate_aggregate_metrics()

# ==================== MockResponseTemplate Endpoints ====================
@router.get("/mockresponsetemplates", response_model=List[Dict[str, Any]])
def list_mockresponsetemplates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MockResponseTemplate records with pagination and filtering."""
    svc = MockResponseTemplateService()
    items = svc.list_mockresponsetemplates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/mockresponsetemplates/{item_id}", response_model=Dict[str, Any])
def get_mockresponsetemplate_by_id(item_id: int):
    """Retrieve detailed record for MockResponseTemplate by ID."""
    svc = MockResponseTemplateService()
    item = svc.get_mockresponsetemplate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MockResponseTemplate with ID {item_id} not found")
    return item.to_dict()

@router.post("/mockresponsetemplates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_mockresponsetemplate(payload: MockResponseTemplateCreateSchema):
    """Create new MockResponseTemplate instance in enterprise repository."""
    svc = MockResponseTemplateService()
    try:
        item = svc.create_mockresponsetemplate(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/mockresponsetemplates/{item_id}", response_model=Dict[str, Any])
def update_mockresponsetemplate(item_id: int, payload: MockResponseTemplateUpdateSchema):
    """Update existing MockResponseTemplate record fields."""
    svc = MockResponseTemplateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_mockresponsetemplate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MockResponseTemplate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/mockresponsetemplates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mockresponsetemplate(item_id: int, hard: bool = Query(False)):
    """Delete MockResponseTemplate record (soft-delete by default)."""
    svc = MockResponseTemplateService()
    ok = svc.delete_mockresponsetemplate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MockResponseTemplate with ID {item_id} not found")
    return None

@router.get("/mockresponsetemplates/analytics/metrics", response_model=Dict[str, Any])
def get_mockresponsetemplate_metrics():
    """Calculate summary statistical KPIs for MockResponseTemplate collection."""
    svc = MockResponseTemplateService()
    return svc.calculate_aggregate_metrics()

# ==================== IntegrationConnector Endpoints ====================
@router.get("/integrationconnectors", response_model=List[Dict[str, Any]])
def list_integrationconnectors(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IntegrationConnector records with pagination and filtering."""
    svc = IntegrationConnectorService()
    items = svc.list_integrationconnectors(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/integrationconnectors/{item_id}", response_model=Dict[str, Any])
def get_integrationconnector_by_id(item_id: int):
    """Retrieve detailed record for IntegrationConnector by ID."""
    svc = IntegrationConnectorService()
    item = svc.get_integrationconnector_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IntegrationConnector with ID {item_id} not found")
    return item.to_dict()

@router.post("/integrationconnectors", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_integrationconnector(payload: IntegrationConnectorCreateSchema):
    """Create new IntegrationConnector instance in enterprise repository."""
    svc = IntegrationConnectorService()
    try:
        item = svc.create_integrationconnector(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/integrationconnectors/{item_id}", response_model=Dict[str, Any])
def update_integrationconnector(item_id: int, payload: IntegrationConnectorUpdateSchema):
    """Update existing IntegrationConnector record fields."""
    svc = IntegrationConnectorService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_integrationconnector(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IntegrationConnector with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/integrationconnectors/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_integrationconnector(item_id: int, hard: bool = Query(False)):
    """Delete IntegrationConnector record (soft-delete by default)."""
    svc = IntegrationConnectorService()
    ok = svc.delete_integrationconnector(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IntegrationConnector with ID {item_id} not found")
    return None

@router.get("/integrationconnectors/analytics/metrics", response_model=Dict[str, Any])
def get_integrationconnector_metrics():
    """Calculate summary statistical KPIs for IntegrationConnector collection."""
    svc = IntegrationConnectorService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceMeshProxy Endpoints ====================
@router.get("/servicemeshproxys", response_model=List[Dict[str, Any]])
def list_servicemeshproxys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceMeshProxy records with pagination and filtering."""
    svc = ServiceMeshProxyService()
    items = svc.list_servicemeshproxys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicemeshproxys/{item_id}", response_model=Dict[str, Any])
def get_servicemeshproxy_by_id(item_id: int):
    """Retrieve detailed record for ServiceMeshProxy by ID."""
    svc = ServiceMeshProxyService()
    item = svc.get_servicemeshproxy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceMeshProxy with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicemeshproxys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicemeshproxy(payload: ServiceMeshProxyCreateSchema):
    """Create new ServiceMeshProxy instance in enterprise repository."""
    svc = ServiceMeshProxyService()
    try:
        item = svc.create_servicemeshproxy(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/servicemeshproxys/{item_id}", response_model=Dict[str, Any])
def update_servicemeshproxy(item_id: int, payload: ServiceMeshProxyUpdateSchema):
    """Update existing ServiceMeshProxy record fields."""
    svc = ServiceMeshProxyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicemeshproxy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceMeshProxy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicemeshproxys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicemeshproxy(item_id: int, hard: bool = Query(False)):
    """Delete ServiceMeshProxy record (soft-delete by default)."""
    svc = ServiceMeshProxyService()
    ok = svc.delete_servicemeshproxy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceMeshProxy with ID {item_id} not found")
    return None

@router.get("/servicemeshproxys/analytics/metrics", response_model=Dict[str, Any])
def get_servicemeshproxy_metrics():
    """Calculate summary statistical KPIs for ServiceMeshProxy collection."""
    svc = ServiceMeshProxyService()
    return svc.calculate_aggregate_metrics()

