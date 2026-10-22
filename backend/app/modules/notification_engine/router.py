"""
Omnichannel Notification & Alert Dispatcher - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    NotificationTemplateService,
    DispatchMessageQueueService,
    DeliveryAttemptLogService,
    UserChannelPreferenceService,
    EmailTransportConfigService,
    SMSGatewayProviderService,
    PushNotificationTokenService,
    InAppNotificationFeedService,
    WebhookDispatchTargetService,
    NotificationCategoryGroupService,
    RateLimitThrottleRuleService,
    OptOutSubscriptionListService,
    TemplateLocalizationItemService,
    DigestAggregationScheduleService,
    BounceFailureReportService,
    EngagementClickTrackerService,
)
from .schemas import (
    NotificationTemplateCreateSchema, NotificationTemplateUpdateSchema, NotificationTemplateResponseSchema,
    DispatchMessageQueueCreateSchema, DispatchMessageQueueUpdateSchema, DispatchMessageQueueResponseSchema,
    DeliveryAttemptLogCreateSchema, DeliveryAttemptLogUpdateSchema, DeliveryAttemptLogResponseSchema,
    UserChannelPreferenceCreateSchema, UserChannelPreferenceUpdateSchema, UserChannelPreferenceResponseSchema,
    EmailTransportConfigCreateSchema, EmailTransportConfigUpdateSchema, EmailTransportConfigResponseSchema,
    SMSGatewayProviderCreateSchema, SMSGatewayProviderUpdateSchema, SMSGatewayProviderResponseSchema,
    PushNotificationTokenCreateSchema, PushNotificationTokenUpdateSchema, PushNotificationTokenResponseSchema,
    InAppNotificationFeedCreateSchema, InAppNotificationFeedUpdateSchema, InAppNotificationFeedResponseSchema,
    WebhookDispatchTargetCreateSchema, WebhookDispatchTargetUpdateSchema, WebhookDispatchTargetResponseSchema,
    NotificationCategoryGroupCreateSchema, NotificationCategoryGroupUpdateSchema, NotificationCategoryGroupResponseSchema,
    RateLimitThrottleRuleCreateSchema, RateLimitThrottleRuleUpdateSchema, RateLimitThrottleRuleResponseSchema,
    OptOutSubscriptionListCreateSchema, OptOutSubscriptionListUpdateSchema, OptOutSubscriptionListResponseSchema,
    TemplateLocalizationItemCreateSchema, TemplateLocalizationItemUpdateSchema, TemplateLocalizationItemResponseSchema,
    DigestAggregationScheduleCreateSchema, DigestAggregationScheduleUpdateSchema, DigestAggregationScheduleResponseSchema,
    BounceFailureReportCreateSchema, BounceFailureReportUpdateSchema, BounceFailureReportResponseSchema,
    EngagementClickTrackerCreateSchema, EngagementClickTrackerUpdateSchema, EngagementClickTrackerResponseSchema,
)

router = APIRouter(prefix="/notification_engine", tags=["Omnichannel Notification & Alert Dispatcher"])

# ==================== NotificationTemplate Endpoints ====================
@router.get("/notificationtemplates", response_model=List[Dict[str, Any]])
def list_notificationtemplates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List NotificationTemplate records with pagination and filtering."""
    svc = NotificationTemplateService()
    items = svc.list_notificationtemplates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/notificationtemplates/{item_id}", response_model=Dict[str, Any])
def get_notificationtemplate_by_id(item_id: int):
    """Retrieve detailed record for NotificationTemplate by ID."""
    svc = NotificationTemplateService()
    item = svc.get_notificationtemplate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"NotificationTemplate with ID {item_id} not found")
    return item.to_dict()

@router.post("/notificationtemplates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_notificationtemplate(payload: NotificationTemplateCreateSchema):
    """Create new NotificationTemplate instance in enterprise repository."""
    svc = NotificationTemplateService()
    try:
        item = svc.create_notificationtemplate(
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

@router.put("/notificationtemplates/{item_id}", response_model=Dict[str, Any])
def update_notificationtemplate(item_id: int, payload: NotificationTemplateUpdateSchema):
    """Update existing NotificationTemplate record fields."""
    svc = NotificationTemplateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_notificationtemplate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"NotificationTemplate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/notificationtemplates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_notificationtemplate(item_id: int, hard: bool = Query(False)):
    """Delete NotificationTemplate record (soft-delete by default)."""
    svc = NotificationTemplateService()
    ok = svc.delete_notificationtemplate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"NotificationTemplate with ID {item_id} not found")
    return None

@router.get("/notificationtemplates/analytics/metrics", response_model=Dict[str, Any])
def get_notificationtemplate_metrics():
    """Calculate summary statistical KPIs for NotificationTemplate collection."""
    svc = NotificationTemplateService()
    return svc.calculate_aggregate_metrics()

# ==================== DispatchMessageQueue Endpoints ====================
@router.get("/dispatchmessagequeues", response_model=List[Dict[str, Any]])
def list_dispatchmessagequeues(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DispatchMessageQueue records with pagination and filtering."""
    svc = DispatchMessageQueueService()
    items = svc.list_dispatchmessagequeues(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dispatchmessagequeues/{item_id}", response_model=Dict[str, Any])
def get_dispatchmessagequeue_by_id(item_id: int):
    """Retrieve detailed record for DispatchMessageQueue by ID."""
    svc = DispatchMessageQueueService()
    item = svc.get_dispatchmessagequeue_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DispatchMessageQueue with ID {item_id} not found")
    return item.to_dict()

@router.post("/dispatchmessagequeues", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dispatchmessagequeue(payload: DispatchMessageQueueCreateSchema):
    """Create new DispatchMessageQueue instance in enterprise repository."""
    svc = DispatchMessageQueueService()
    try:
        item = svc.create_dispatchmessagequeue(
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

@router.put("/dispatchmessagequeues/{item_id}", response_model=Dict[str, Any])
def update_dispatchmessagequeue(item_id: int, payload: DispatchMessageQueueUpdateSchema):
    """Update existing DispatchMessageQueue record fields."""
    svc = DispatchMessageQueueService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dispatchmessagequeue(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DispatchMessageQueue with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dispatchmessagequeues/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dispatchmessagequeue(item_id: int, hard: bool = Query(False)):
    """Delete DispatchMessageQueue record (soft-delete by default)."""
    svc = DispatchMessageQueueService()
    ok = svc.delete_dispatchmessagequeue(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DispatchMessageQueue with ID {item_id} not found")
    return None

@router.get("/dispatchmessagequeues/analytics/metrics", response_model=Dict[str, Any])
def get_dispatchmessagequeue_metrics():
    """Calculate summary statistical KPIs for DispatchMessageQueue collection."""
    svc = DispatchMessageQueueService()
    return svc.calculate_aggregate_metrics()

# ==================== DeliveryAttemptLog Endpoints ====================
@router.get("/deliveryattemptlogs", response_model=List[Dict[str, Any]])
def list_deliveryattemptlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeliveryAttemptLog records with pagination and filtering."""
    svc = DeliveryAttemptLogService()
    items = svc.list_deliveryattemptlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/deliveryattemptlogs/{item_id}", response_model=Dict[str, Any])
def get_deliveryattemptlog_by_id(item_id: int):
    """Retrieve detailed record for DeliveryAttemptLog by ID."""
    svc = DeliveryAttemptLogService()
    item = svc.get_deliveryattemptlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeliveryAttemptLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/deliveryattemptlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_deliveryattemptlog(payload: DeliveryAttemptLogCreateSchema):
    """Create new DeliveryAttemptLog instance in enterprise repository."""
    svc = DeliveryAttemptLogService()
    try:
        item = svc.create_deliveryattemptlog(
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

@router.put("/deliveryattemptlogs/{item_id}", response_model=Dict[str, Any])
def update_deliveryattemptlog(item_id: int, payload: DeliveryAttemptLogUpdateSchema):
    """Update existing DeliveryAttemptLog record fields."""
    svc = DeliveryAttemptLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_deliveryattemptlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeliveryAttemptLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/deliveryattemptlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deliveryattemptlog(item_id: int, hard: bool = Query(False)):
    """Delete DeliveryAttemptLog record (soft-delete by default)."""
    svc = DeliveryAttemptLogService()
    ok = svc.delete_deliveryattemptlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeliveryAttemptLog with ID {item_id} not found")
    return None

@router.get("/deliveryattemptlogs/analytics/metrics", response_model=Dict[str, Any])
def get_deliveryattemptlog_metrics():
    """Calculate summary statistical KPIs for DeliveryAttemptLog collection."""
    svc = DeliveryAttemptLogService()
    return svc.calculate_aggregate_metrics()

# ==================== UserChannelPreference Endpoints ====================
@router.get("/userchannelpreferences", response_model=List[Dict[str, Any]])
def list_userchannelpreferences(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UserChannelPreference records with pagination and filtering."""
    svc = UserChannelPreferenceService()
    items = svc.list_userchannelpreferences(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/userchannelpreferences/{item_id}", response_model=Dict[str, Any])
def get_userchannelpreference_by_id(item_id: int):
    """Retrieve detailed record for UserChannelPreference by ID."""
    svc = UserChannelPreferenceService()
    item = svc.get_userchannelpreference_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UserChannelPreference with ID {item_id} not found")
    return item.to_dict()

@router.post("/userchannelpreferences", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_userchannelpreference(payload: UserChannelPreferenceCreateSchema):
    """Create new UserChannelPreference instance in enterprise repository."""
    svc = UserChannelPreferenceService()
    try:
        item = svc.create_userchannelpreference(
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

@router.put("/userchannelpreferences/{item_id}", response_model=Dict[str, Any])
def update_userchannelpreference(item_id: int, payload: UserChannelPreferenceUpdateSchema):
    """Update existing UserChannelPreference record fields."""
    svc = UserChannelPreferenceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_userchannelpreference(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UserChannelPreference with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/userchannelpreferences/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_userchannelpreference(item_id: int, hard: bool = Query(False)):
    """Delete UserChannelPreference record (soft-delete by default)."""
    svc = UserChannelPreferenceService()
    ok = svc.delete_userchannelpreference(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UserChannelPreference with ID {item_id} not found")
    return None

@router.get("/userchannelpreferences/analytics/metrics", response_model=Dict[str, Any])
def get_userchannelpreference_metrics():
    """Calculate summary statistical KPIs for UserChannelPreference collection."""
    svc = UserChannelPreferenceService()
    return svc.calculate_aggregate_metrics()

# ==================== EmailTransportConfig Endpoints ====================
@router.get("/emailtransportconfigs", response_model=List[Dict[str, Any]])
def list_emailtransportconfigs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmailTransportConfig records with pagination and filtering."""
    svc = EmailTransportConfigService()
    items = svc.list_emailtransportconfigs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/emailtransportconfigs/{item_id}", response_model=Dict[str, Any])
def get_emailtransportconfig_by_id(item_id: int):
    """Retrieve detailed record for EmailTransportConfig by ID."""
    svc = EmailTransportConfigService()
    item = svc.get_emailtransportconfig_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmailTransportConfig with ID {item_id} not found")
    return item.to_dict()

@router.post("/emailtransportconfigs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_emailtransportconfig(payload: EmailTransportConfigCreateSchema):
    """Create new EmailTransportConfig instance in enterprise repository."""
    svc = EmailTransportConfigService()
    try:
        item = svc.create_emailtransportconfig(
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

@router.put("/emailtransportconfigs/{item_id}", response_model=Dict[str, Any])
def update_emailtransportconfig(item_id: int, payload: EmailTransportConfigUpdateSchema):
    """Update existing EmailTransportConfig record fields."""
    svc = EmailTransportConfigService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_emailtransportconfig(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmailTransportConfig with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/emailtransportconfigs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_emailtransportconfig(item_id: int, hard: bool = Query(False)):
    """Delete EmailTransportConfig record (soft-delete by default)."""
    svc = EmailTransportConfigService()
    ok = svc.delete_emailtransportconfig(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmailTransportConfig with ID {item_id} not found")
    return None

@router.get("/emailtransportconfigs/analytics/metrics", response_model=Dict[str, Any])
def get_emailtransportconfig_metrics():
    """Calculate summary statistical KPIs for EmailTransportConfig collection."""
    svc = EmailTransportConfigService()
    return svc.calculate_aggregate_metrics()

# ==================== SMSGatewayProvider Endpoints ====================
@router.get("/smsgatewayproviders", response_model=List[Dict[str, Any]])
def list_smsgatewayproviders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SMSGatewayProvider records with pagination and filtering."""
    svc = SMSGatewayProviderService()
    items = svc.list_smsgatewayproviders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/smsgatewayproviders/{item_id}", response_model=Dict[str, Any])
def get_smsgatewayprovider_by_id(item_id: int):
    """Retrieve detailed record for SMSGatewayProvider by ID."""
    svc = SMSGatewayProviderService()
    item = svc.get_smsgatewayprovider_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SMSGatewayProvider with ID {item_id} not found")
    return item.to_dict()

@router.post("/smsgatewayproviders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_smsgatewayprovider(payload: SMSGatewayProviderCreateSchema):
    """Create new SMSGatewayProvider instance in enterprise repository."""
    svc = SMSGatewayProviderService()
    try:
        item = svc.create_smsgatewayprovider(
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

@router.put("/smsgatewayproviders/{item_id}", response_model=Dict[str, Any])
def update_smsgatewayprovider(item_id: int, payload: SMSGatewayProviderUpdateSchema):
    """Update existing SMSGatewayProvider record fields."""
    svc = SMSGatewayProviderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_smsgatewayprovider(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SMSGatewayProvider with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/smsgatewayproviders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_smsgatewayprovider(item_id: int, hard: bool = Query(False)):
    """Delete SMSGatewayProvider record (soft-delete by default)."""
    svc = SMSGatewayProviderService()
    ok = svc.delete_smsgatewayprovider(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SMSGatewayProvider with ID {item_id} not found")
    return None

@router.get("/smsgatewayproviders/analytics/metrics", response_model=Dict[str, Any])
def get_smsgatewayprovider_metrics():
    """Calculate summary statistical KPIs for SMSGatewayProvider collection."""
    svc = SMSGatewayProviderService()
    return svc.calculate_aggregate_metrics()

# ==================== PushNotificationToken Endpoints ====================
@router.get("/pushnotificationtokens", response_model=List[Dict[str, Any]])
def list_pushnotificationtokens(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PushNotificationToken records with pagination and filtering."""
    svc = PushNotificationTokenService()
    items = svc.list_pushnotificationtokens(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/pushnotificationtokens/{item_id}", response_model=Dict[str, Any])
def get_pushnotificationtoken_by_id(item_id: int):
    """Retrieve detailed record for PushNotificationToken by ID."""
    svc = PushNotificationTokenService()
    item = svc.get_pushnotificationtoken_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PushNotificationToken with ID {item_id} not found")
    return item.to_dict()

@router.post("/pushnotificationtokens", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_pushnotificationtoken(payload: PushNotificationTokenCreateSchema):
    """Create new PushNotificationToken instance in enterprise repository."""
    svc = PushNotificationTokenService()
    try:
        item = svc.create_pushnotificationtoken(
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

@router.put("/pushnotificationtokens/{item_id}", response_model=Dict[str, Any])
def update_pushnotificationtoken(item_id: int, payload: PushNotificationTokenUpdateSchema):
    """Update existing PushNotificationToken record fields."""
    svc = PushNotificationTokenService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_pushnotificationtoken(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PushNotificationToken with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/pushnotificationtokens/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pushnotificationtoken(item_id: int, hard: bool = Query(False)):
    """Delete PushNotificationToken record (soft-delete by default)."""
    svc = PushNotificationTokenService()
    ok = svc.delete_pushnotificationtoken(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PushNotificationToken with ID {item_id} not found")
    return None

@router.get("/pushnotificationtokens/analytics/metrics", response_model=Dict[str, Any])
def get_pushnotificationtoken_metrics():
    """Calculate summary statistical KPIs for PushNotificationToken collection."""
    svc = PushNotificationTokenService()
    return svc.calculate_aggregate_metrics()

# ==================== InAppNotificationFeed Endpoints ====================
@router.get("/inappnotificationfeeds", response_model=List[Dict[str, Any]])
def list_inappnotificationfeeds(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InAppNotificationFeed records with pagination and filtering."""
    svc = InAppNotificationFeedService()
    items = svc.list_inappnotificationfeeds(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inappnotificationfeeds/{item_id}", response_model=Dict[str, Any])
def get_inappnotificationfeed_by_id(item_id: int):
    """Retrieve detailed record for InAppNotificationFeed by ID."""
    svc = InAppNotificationFeedService()
    item = svc.get_inappnotificationfeed_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InAppNotificationFeed with ID {item_id} not found")
    return item.to_dict()

@router.post("/inappnotificationfeeds", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inappnotificationfeed(payload: InAppNotificationFeedCreateSchema):
    """Create new InAppNotificationFeed instance in enterprise repository."""
    svc = InAppNotificationFeedService()
    try:
        item = svc.create_inappnotificationfeed(
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

@router.put("/inappnotificationfeeds/{item_id}", response_model=Dict[str, Any])
def update_inappnotificationfeed(item_id: int, payload: InAppNotificationFeedUpdateSchema):
    """Update existing InAppNotificationFeed record fields."""
    svc = InAppNotificationFeedService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inappnotificationfeed(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InAppNotificationFeed with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inappnotificationfeeds/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inappnotificationfeed(item_id: int, hard: bool = Query(False)):
    """Delete InAppNotificationFeed record (soft-delete by default)."""
    svc = InAppNotificationFeedService()
    ok = svc.delete_inappnotificationfeed(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InAppNotificationFeed with ID {item_id} not found")
    return None

@router.get("/inappnotificationfeeds/analytics/metrics", response_model=Dict[str, Any])
def get_inappnotificationfeed_metrics():
    """Calculate summary statistical KPIs for InAppNotificationFeed collection."""
    svc = InAppNotificationFeedService()
    return svc.calculate_aggregate_metrics()

# ==================== WebhookDispatchTarget Endpoints ====================
@router.get("/webhookdispatchtargets", response_model=List[Dict[str, Any]])
def list_webhookdispatchtargets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WebhookDispatchTarget records with pagination and filtering."""
    svc = WebhookDispatchTargetService()
    items = svc.list_webhookdispatchtargets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/webhookdispatchtargets/{item_id}", response_model=Dict[str, Any])
def get_webhookdispatchtarget_by_id(item_id: int):
    """Retrieve detailed record for WebhookDispatchTarget by ID."""
    svc = WebhookDispatchTargetService()
    item = svc.get_webhookdispatchtarget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WebhookDispatchTarget with ID {item_id} not found")
    return item.to_dict()

@router.post("/webhookdispatchtargets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_webhookdispatchtarget(payload: WebhookDispatchTargetCreateSchema):
    """Create new WebhookDispatchTarget instance in enterprise repository."""
    svc = WebhookDispatchTargetService()
    try:
        item = svc.create_webhookdispatchtarget(
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

@router.put("/webhookdispatchtargets/{item_id}", response_model=Dict[str, Any])
def update_webhookdispatchtarget(item_id: int, payload: WebhookDispatchTargetUpdateSchema):
    """Update existing WebhookDispatchTarget record fields."""
    svc = WebhookDispatchTargetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_webhookdispatchtarget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WebhookDispatchTarget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/webhookdispatchtargets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_webhookdispatchtarget(item_id: int, hard: bool = Query(False)):
    """Delete WebhookDispatchTarget record (soft-delete by default)."""
    svc = WebhookDispatchTargetService()
    ok = svc.delete_webhookdispatchtarget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WebhookDispatchTarget with ID {item_id} not found")
    return None

@router.get("/webhookdispatchtargets/analytics/metrics", response_model=Dict[str, Any])
def get_webhookdispatchtarget_metrics():
    """Calculate summary statistical KPIs for WebhookDispatchTarget collection."""
    svc = WebhookDispatchTargetService()
    return svc.calculate_aggregate_metrics()

# ==================== NotificationCategoryGroup Endpoints ====================
@router.get("/notificationcategorygroups", response_model=List[Dict[str, Any]])
def list_notificationcategorygroups(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List NotificationCategoryGroup records with pagination and filtering."""
    svc = NotificationCategoryGroupService()
    items = svc.list_notificationcategorygroups(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/notificationcategorygroups/{item_id}", response_model=Dict[str, Any])
def get_notificationcategorygroup_by_id(item_id: int):
    """Retrieve detailed record for NotificationCategoryGroup by ID."""
    svc = NotificationCategoryGroupService()
    item = svc.get_notificationcategorygroup_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"NotificationCategoryGroup with ID {item_id} not found")
    return item.to_dict()

@router.post("/notificationcategorygroups", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_notificationcategorygroup(payload: NotificationCategoryGroupCreateSchema):
    """Create new NotificationCategoryGroup instance in enterprise repository."""
    svc = NotificationCategoryGroupService()
    try:
        item = svc.create_notificationcategorygroup(
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

@router.put("/notificationcategorygroups/{item_id}", response_model=Dict[str, Any])
def update_notificationcategorygroup(item_id: int, payload: NotificationCategoryGroupUpdateSchema):
    """Update existing NotificationCategoryGroup record fields."""
    svc = NotificationCategoryGroupService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_notificationcategorygroup(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"NotificationCategoryGroup with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/notificationcategorygroups/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_notificationcategorygroup(item_id: int, hard: bool = Query(False)):
    """Delete NotificationCategoryGroup record (soft-delete by default)."""
    svc = NotificationCategoryGroupService()
    ok = svc.delete_notificationcategorygroup(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"NotificationCategoryGroup with ID {item_id} not found")
    return None

@router.get("/notificationcategorygroups/analytics/metrics", response_model=Dict[str, Any])
def get_notificationcategorygroup_metrics():
    """Calculate summary statistical KPIs for NotificationCategoryGroup collection."""
    svc = NotificationCategoryGroupService()
    return svc.calculate_aggregate_metrics()

# ==================== RateLimitThrottleRule Endpoints ====================
@router.get("/ratelimitthrottlerules", response_model=List[Dict[str, Any]])
def list_ratelimitthrottlerules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RateLimitThrottleRule records with pagination and filtering."""
    svc = RateLimitThrottleRuleService()
    items = svc.list_ratelimitthrottlerules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ratelimitthrottlerules/{item_id}", response_model=Dict[str, Any])
def get_ratelimitthrottlerule_by_id(item_id: int):
    """Retrieve detailed record for RateLimitThrottleRule by ID."""
    svc = RateLimitThrottleRuleService()
    item = svc.get_ratelimitthrottlerule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RateLimitThrottleRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/ratelimitthrottlerules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ratelimitthrottlerule(payload: RateLimitThrottleRuleCreateSchema):
    """Create new RateLimitThrottleRule instance in enterprise repository."""
    svc = RateLimitThrottleRuleService()
    try:
        item = svc.create_ratelimitthrottlerule(
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

@router.put("/ratelimitthrottlerules/{item_id}", response_model=Dict[str, Any])
def update_ratelimitthrottlerule(item_id: int, payload: RateLimitThrottleRuleUpdateSchema):
    """Update existing RateLimitThrottleRule record fields."""
    svc = RateLimitThrottleRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ratelimitthrottlerule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RateLimitThrottleRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ratelimitthrottlerules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ratelimitthrottlerule(item_id: int, hard: bool = Query(False)):
    """Delete RateLimitThrottleRule record (soft-delete by default)."""
    svc = RateLimitThrottleRuleService()
    ok = svc.delete_ratelimitthrottlerule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RateLimitThrottleRule with ID {item_id} not found")
    return None

@router.get("/ratelimitthrottlerules/analytics/metrics", response_model=Dict[str, Any])
def get_ratelimitthrottlerule_metrics():
    """Calculate summary statistical KPIs for RateLimitThrottleRule collection."""
    svc = RateLimitThrottleRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== OptOutSubscriptionList Endpoints ====================
@router.get("/optoutsubscriptionlists", response_model=List[Dict[str, Any]])
def list_optoutsubscriptionlists(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OptOutSubscriptionList records with pagination and filtering."""
    svc = OptOutSubscriptionListService()
    items = svc.list_optoutsubscriptionlists(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/optoutsubscriptionlists/{item_id}", response_model=Dict[str, Any])
def get_optoutsubscriptionlist_by_id(item_id: int):
    """Retrieve detailed record for OptOutSubscriptionList by ID."""
    svc = OptOutSubscriptionListService()
    item = svc.get_optoutsubscriptionlist_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OptOutSubscriptionList with ID {item_id} not found")
    return item.to_dict()

@router.post("/optoutsubscriptionlists", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_optoutsubscriptionlist(payload: OptOutSubscriptionListCreateSchema):
    """Create new OptOutSubscriptionList instance in enterprise repository."""
    svc = OptOutSubscriptionListService()
    try:
        item = svc.create_optoutsubscriptionlist(
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

@router.put("/optoutsubscriptionlists/{item_id}", response_model=Dict[str, Any])
def update_optoutsubscriptionlist(item_id: int, payload: OptOutSubscriptionListUpdateSchema):
    """Update existing OptOutSubscriptionList record fields."""
    svc = OptOutSubscriptionListService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_optoutsubscriptionlist(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OptOutSubscriptionList with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/optoutsubscriptionlists/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_optoutsubscriptionlist(item_id: int, hard: bool = Query(False)):
    """Delete OptOutSubscriptionList record (soft-delete by default)."""
    svc = OptOutSubscriptionListService()
    ok = svc.delete_optoutsubscriptionlist(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OptOutSubscriptionList with ID {item_id} not found")
    return None

@router.get("/optoutsubscriptionlists/analytics/metrics", response_model=Dict[str, Any])
def get_optoutsubscriptionlist_metrics():
    """Calculate summary statistical KPIs for OptOutSubscriptionList collection."""
    svc = OptOutSubscriptionListService()
    return svc.calculate_aggregate_metrics()

# ==================== TemplateLocalizationItem Endpoints ====================
@router.get("/templatelocalizationitems", response_model=List[Dict[str, Any]])
def list_templatelocalizationitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TemplateLocalizationItem records with pagination and filtering."""
    svc = TemplateLocalizationItemService()
    items = svc.list_templatelocalizationitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/templatelocalizationitems/{item_id}", response_model=Dict[str, Any])
def get_templatelocalizationitem_by_id(item_id: int):
    """Retrieve detailed record for TemplateLocalizationItem by ID."""
    svc = TemplateLocalizationItemService()
    item = svc.get_templatelocalizationitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TemplateLocalizationItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/templatelocalizationitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_templatelocalizationitem(payload: TemplateLocalizationItemCreateSchema):
    """Create new TemplateLocalizationItem instance in enterprise repository."""
    svc = TemplateLocalizationItemService()
    try:
        item = svc.create_templatelocalizationitem(
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

@router.put("/templatelocalizationitems/{item_id}", response_model=Dict[str, Any])
def update_templatelocalizationitem(item_id: int, payload: TemplateLocalizationItemUpdateSchema):
    """Update existing TemplateLocalizationItem record fields."""
    svc = TemplateLocalizationItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_templatelocalizationitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TemplateLocalizationItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/templatelocalizationitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_templatelocalizationitem(item_id: int, hard: bool = Query(False)):
    """Delete TemplateLocalizationItem record (soft-delete by default)."""
    svc = TemplateLocalizationItemService()
    ok = svc.delete_templatelocalizationitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TemplateLocalizationItem with ID {item_id} not found")
    return None

@router.get("/templatelocalizationitems/analytics/metrics", response_model=Dict[str, Any])
def get_templatelocalizationitem_metrics():
    """Calculate summary statistical KPIs for TemplateLocalizationItem collection."""
    svc = TemplateLocalizationItemService()
    return svc.calculate_aggregate_metrics()

# ==================== DigestAggregationSchedule Endpoints ====================
@router.get("/digestaggregationschedules", response_model=List[Dict[str, Any]])
def list_digestaggregationschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DigestAggregationSchedule records with pagination and filtering."""
    svc = DigestAggregationScheduleService()
    items = svc.list_digestaggregationschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/digestaggregationschedules/{item_id}", response_model=Dict[str, Any])
def get_digestaggregationschedule_by_id(item_id: int):
    """Retrieve detailed record for DigestAggregationSchedule by ID."""
    svc = DigestAggregationScheduleService()
    item = svc.get_digestaggregationschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DigestAggregationSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/digestaggregationschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_digestaggregationschedule(payload: DigestAggregationScheduleCreateSchema):
    """Create new DigestAggregationSchedule instance in enterprise repository."""
    svc = DigestAggregationScheduleService()
    try:
        item = svc.create_digestaggregationschedule(
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

@router.put("/digestaggregationschedules/{item_id}", response_model=Dict[str, Any])
def update_digestaggregationschedule(item_id: int, payload: DigestAggregationScheduleUpdateSchema):
    """Update existing DigestAggregationSchedule record fields."""
    svc = DigestAggregationScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_digestaggregationschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DigestAggregationSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/digestaggregationschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_digestaggregationschedule(item_id: int, hard: bool = Query(False)):
    """Delete DigestAggregationSchedule record (soft-delete by default)."""
    svc = DigestAggregationScheduleService()
    ok = svc.delete_digestaggregationschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DigestAggregationSchedule with ID {item_id} not found")
    return None

@router.get("/digestaggregationschedules/analytics/metrics", response_model=Dict[str, Any])
def get_digestaggregationschedule_metrics():
    """Calculate summary statistical KPIs for DigestAggregationSchedule collection."""
    svc = DigestAggregationScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== BounceFailureReport Endpoints ====================
@router.get("/bouncefailurereports", response_model=List[Dict[str, Any]])
def list_bouncefailurereports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BounceFailureReport records with pagination and filtering."""
    svc = BounceFailureReportService()
    items = svc.list_bouncefailurereports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bouncefailurereports/{item_id}", response_model=Dict[str, Any])
def get_bouncefailurereport_by_id(item_id: int):
    """Retrieve detailed record for BounceFailureReport by ID."""
    svc = BounceFailureReportService()
    item = svc.get_bouncefailurereport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BounceFailureReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/bouncefailurereports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bouncefailurereport(payload: BounceFailureReportCreateSchema):
    """Create new BounceFailureReport instance in enterprise repository."""
    svc = BounceFailureReportService()
    try:
        item = svc.create_bouncefailurereport(
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

@router.put("/bouncefailurereports/{item_id}", response_model=Dict[str, Any])
def update_bouncefailurereport(item_id: int, payload: BounceFailureReportUpdateSchema):
    """Update existing BounceFailureReport record fields."""
    svc = BounceFailureReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bouncefailurereport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BounceFailureReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bouncefailurereports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bouncefailurereport(item_id: int, hard: bool = Query(False)):
    """Delete BounceFailureReport record (soft-delete by default)."""
    svc = BounceFailureReportService()
    ok = svc.delete_bouncefailurereport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BounceFailureReport with ID {item_id} not found")
    return None

@router.get("/bouncefailurereports/analytics/metrics", response_model=Dict[str, Any])
def get_bouncefailurereport_metrics():
    """Calculate summary statistical KPIs for BounceFailureReport collection."""
    svc = BounceFailureReportService()
    return svc.calculate_aggregate_metrics()

# ==================== EngagementClickTracker Endpoints ====================
@router.get("/engagementclicktrackers", response_model=List[Dict[str, Any]])
def list_engagementclicktrackers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EngagementClickTracker records with pagination and filtering."""
    svc = EngagementClickTrackerService()
    items = svc.list_engagementclicktrackers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/engagementclicktrackers/{item_id}", response_model=Dict[str, Any])
def get_engagementclicktracker_by_id(item_id: int):
    """Retrieve detailed record for EngagementClickTracker by ID."""
    svc = EngagementClickTrackerService()
    item = svc.get_engagementclicktracker_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EngagementClickTracker with ID {item_id} not found")
    return item.to_dict()

@router.post("/engagementclicktrackers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_engagementclicktracker(payload: EngagementClickTrackerCreateSchema):
    """Create new EngagementClickTracker instance in enterprise repository."""
    svc = EngagementClickTrackerService()
    try:
        item = svc.create_engagementclicktracker(
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

@router.put("/engagementclicktrackers/{item_id}", response_model=Dict[str, Any])
def update_engagementclicktracker(item_id: int, payload: EngagementClickTrackerUpdateSchema):
    """Update existing EngagementClickTracker record fields."""
    svc = EngagementClickTrackerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_engagementclicktracker(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EngagementClickTracker with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/engagementclicktrackers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_engagementclicktracker(item_id: int, hard: bool = Query(False)):
    """Delete EngagementClickTracker record (soft-delete by default)."""
    svc = EngagementClickTrackerService()
    ok = svc.delete_engagementclicktracker(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EngagementClickTracker with ID {item_id} not found")
    return None

@router.get("/engagementclicktrackers/analytics/metrics", response_model=Dict[str, Any])
def get_engagementclicktracker_metrics():
    """Calculate summary statistical KPIs for EngagementClickTracker collection."""
    svc = EngagementClickTrackerService()
    return svc.calculate_aggregate_metrics()

