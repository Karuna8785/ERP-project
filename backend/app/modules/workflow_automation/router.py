"""
BPMN Business Process Automation - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ProcessDefinitionService,
    ProcessInstanceService,
    ActivityTaskInstanceService,
    ExecutionTokenService,
    GatewayConditionDecisionService,
    TimerEventSubscriptionService,
    UserTaskAssignmentService,
    EscalationTriggerRuleService,
    VariableScopeStorageService,
    ProcessHistoryAuditService,
    MessageCatchEventService,
    SignalThrowEventService,
    SubProcessScopeService,
    CompensationHandlerService,
    ProcessMetricsAnalyticsService,
    DeploymentPackageService,
)
from .schemas import (
    ProcessDefinitionCreateSchema, ProcessDefinitionUpdateSchema, ProcessDefinitionResponseSchema,
    ProcessInstanceCreateSchema, ProcessInstanceUpdateSchema, ProcessInstanceResponseSchema,
    ActivityTaskInstanceCreateSchema, ActivityTaskInstanceUpdateSchema, ActivityTaskInstanceResponseSchema,
    ExecutionTokenCreateSchema, ExecutionTokenUpdateSchema, ExecutionTokenResponseSchema,
    GatewayConditionDecisionCreateSchema, GatewayConditionDecisionUpdateSchema, GatewayConditionDecisionResponseSchema,
    TimerEventSubscriptionCreateSchema, TimerEventSubscriptionUpdateSchema, TimerEventSubscriptionResponseSchema,
    UserTaskAssignmentCreateSchema, UserTaskAssignmentUpdateSchema, UserTaskAssignmentResponseSchema,
    EscalationTriggerRuleCreateSchema, EscalationTriggerRuleUpdateSchema, EscalationTriggerRuleResponseSchema,
    VariableScopeStorageCreateSchema, VariableScopeStorageUpdateSchema, VariableScopeStorageResponseSchema,
    ProcessHistoryAuditCreateSchema, ProcessHistoryAuditUpdateSchema, ProcessHistoryAuditResponseSchema,
    MessageCatchEventCreateSchema, MessageCatchEventUpdateSchema, MessageCatchEventResponseSchema,
    SignalThrowEventCreateSchema, SignalThrowEventUpdateSchema, SignalThrowEventResponseSchema,
    SubProcessScopeCreateSchema, SubProcessScopeUpdateSchema, SubProcessScopeResponseSchema,
    CompensationHandlerCreateSchema, CompensationHandlerUpdateSchema, CompensationHandlerResponseSchema,
    ProcessMetricsAnalyticsCreateSchema, ProcessMetricsAnalyticsUpdateSchema, ProcessMetricsAnalyticsResponseSchema,
    DeploymentPackageCreateSchema, DeploymentPackageUpdateSchema, DeploymentPackageResponseSchema,
)

router = APIRouter(prefix="/workflow_automation", tags=["BPMN Business Process Automation"])

# ==================== ProcessDefinition Endpoints ====================
@router.get("/processdefinitions", response_model=List[Dict[str, Any]])
def list_processdefinitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProcessDefinition records with pagination and filtering."""
    svc = ProcessDefinitionService()
    items = svc.list_processdefinitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/processdefinitions/{item_id}", response_model=Dict[str, Any])
def get_processdefinition_by_id(item_id: int):
    """Retrieve detailed record for ProcessDefinition by ID."""
    svc = ProcessDefinitionService()
    item = svc.get_processdefinition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProcessDefinition with ID {item_id} not found")
    return item.to_dict()

@router.post("/processdefinitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_processdefinition(payload: ProcessDefinitionCreateSchema):
    """Create new ProcessDefinition instance in enterprise repository."""
    svc = ProcessDefinitionService()
    try:
        item = svc.create_processdefinition(
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

@router.put("/processdefinitions/{item_id}", response_model=Dict[str, Any])
def update_processdefinition(item_id: int, payload: ProcessDefinitionUpdateSchema):
    """Update existing ProcessDefinition record fields."""
    svc = ProcessDefinitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_processdefinition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProcessDefinition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/processdefinitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_processdefinition(item_id: int, hard: bool = Query(False)):
    """Delete ProcessDefinition record (soft-delete by default)."""
    svc = ProcessDefinitionService()
    ok = svc.delete_processdefinition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProcessDefinition with ID {item_id} not found")
    return None

@router.get("/processdefinitions/analytics/metrics", response_model=Dict[str, Any])
def get_processdefinition_metrics():
    """Calculate summary statistical KPIs for ProcessDefinition collection."""
    svc = ProcessDefinitionService()
    return svc.calculate_aggregate_metrics()

# ==================== ProcessInstance Endpoints ====================
@router.get("/processinstances", response_model=List[Dict[str, Any]])
def list_processinstances(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProcessInstance records with pagination and filtering."""
    svc = ProcessInstanceService()
    items = svc.list_processinstances(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/processinstances/{item_id}", response_model=Dict[str, Any])
def get_processinstance_by_id(item_id: int):
    """Retrieve detailed record for ProcessInstance by ID."""
    svc = ProcessInstanceService()
    item = svc.get_processinstance_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProcessInstance with ID {item_id} not found")
    return item.to_dict()

@router.post("/processinstances", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_processinstance(payload: ProcessInstanceCreateSchema):
    """Create new ProcessInstance instance in enterprise repository."""
    svc = ProcessInstanceService()
    try:
        item = svc.create_processinstance(
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

@router.put("/processinstances/{item_id}", response_model=Dict[str, Any])
def update_processinstance(item_id: int, payload: ProcessInstanceUpdateSchema):
    """Update existing ProcessInstance record fields."""
    svc = ProcessInstanceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_processinstance(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProcessInstance with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/processinstances/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_processinstance(item_id: int, hard: bool = Query(False)):
    """Delete ProcessInstance record (soft-delete by default)."""
    svc = ProcessInstanceService()
    ok = svc.delete_processinstance(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProcessInstance with ID {item_id} not found")
    return None

@router.get("/processinstances/analytics/metrics", response_model=Dict[str, Any])
def get_processinstance_metrics():
    """Calculate summary statistical KPIs for ProcessInstance collection."""
    svc = ProcessInstanceService()
    return svc.calculate_aggregate_metrics()

# ==================== ActivityTaskInstance Endpoints ====================
@router.get("/activitytaskinstances", response_model=List[Dict[str, Any]])
def list_activitytaskinstances(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ActivityTaskInstance records with pagination and filtering."""
    svc = ActivityTaskInstanceService()
    items = svc.list_activitytaskinstances(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/activitytaskinstances/{item_id}", response_model=Dict[str, Any])
def get_activitytaskinstance_by_id(item_id: int):
    """Retrieve detailed record for ActivityTaskInstance by ID."""
    svc = ActivityTaskInstanceService()
    item = svc.get_activitytaskinstance_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ActivityTaskInstance with ID {item_id} not found")
    return item.to_dict()

@router.post("/activitytaskinstances", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_activitytaskinstance(payload: ActivityTaskInstanceCreateSchema):
    """Create new ActivityTaskInstance instance in enterprise repository."""
    svc = ActivityTaskInstanceService()
    try:
        item = svc.create_activitytaskinstance(
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

@router.put("/activitytaskinstances/{item_id}", response_model=Dict[str, Any])
def update_activitytaskinstance(item_id: int, payload: ActivityTaskInstanceUpdateSchema):
    """Update existing ActivityTaskInstance record fields."""
    svc = ActivityTaskInstanceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_activitytaskinstance(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ActivityTaskInstance with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/activitytaskinstances/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_activitytaskinstance(item_id: int, hard: bool = Query(False)):
    """Delete ActivityTaskInstance record (soft-delete by default)."""
    svc = ActivityTaskInstanceService()
    ok = svc.delete_activitytaskinstance(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ActivityTaskInstance with ID {item_id} not found")
    return None

@router.get("/activitytaskinstances/analytics/metrics", response_model=Dict[str, Any])
def get_activitytaskinstance_metrics():
    """Calculate summary statistical KPIs for ActivityTaskInstance collection."""
    svc = ActivityTaskInstanceService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutionToken Endpoints ====================
@router.get("/executiontokens", response_model=List[Dict[str, Any]])
def list_executiontokens(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutionToken records with pagination and filtering."""
    svc = ExecutionTokenService()
    items = svc.list_executiontokens(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executiontokens/{item_id}", response_model=Dict[str, Any])
def get_executiontoken_by_id(item_id: int):
    """Retrieve detailed record for ExecutionToken by ID."""
    svc = ExecutionTokenService()
    item = svc.get_executiontoken_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutionToken with ID {item_id} not found")
    return item.to_dict()

@router.post("/executiontokens", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executiontoken(payload: ExecutionTokenCreateSchema):
    """Create new ExecutionToken instance in enterprise repository."""
    svc = ExecutionTokenService()
    try:
        item = svc.create_executiontoken(
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

@router.put("/executiontokens/{item_id}", response_model=Dict[str, Any])
def update_executiontoken(item_id: int, payload: ExecutionTokenUpdateSchema):
    """Update existing ExecutionToken record fields."""
    svc = ExecutionTokenService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executiontoken(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutionToken with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executiontokens/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executiontoken(item_id: int, hard: bool = Query(False)):
    """Delete ExecutionToken record (soft-delete by default)."""
    svc = ExecutionTokenService()
    ok = svc.delete_executiontoken(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutionToken with ID {item_id} not found")
    return None

@router.get("/executiontokens/analytics/metrics", response_model=Dict[str, Any])
def get_executiontoken_metrics():
    """Calculate summary statistical KPIs for ExecutionToken collection."""
    svc = ExecutionTokenService()
    return svc.calculate_aggregate_metrics()

# ==================== GatewayConditionDecision Endpoints ====================
@router.get("/gatewayconditiondecisions", response_model=List[Dict[str, Any]])
def list_gatewayconditiondecisions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GatewayConditionDecision records with pagination and filtering."""
    svc = GatewayConditionDecisionService()
    items = svc.list_gatewayconditiondecisions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/gatewayconditiondecisions/{item_id}", response_model=Dict[str, Any])
def get_gatewayconditiondecision_by_id(item_id: int):
    """Retrieve detailed record for GatewayConditionDecision by ID."""
    svc = GatewayConditionDecisionService()
    item = svc.get_gatewayconditiondecision_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GatewayConditionDecision with ID {item_id} not found")
    return item.to_dict()

@router.post("/gatewayconditiondecisions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_gatewayconditiondecision(payload: GatewayConditionDecisionCreateSchema):
    """Create new GatewayConditionDecision instance in enterprise repository."""
    svc = GatewayConditionDecisionService()
    try:
        item = svc.create_gatewayconditiondecision(
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

@router.put("/gatewayconditiondecisions/{item_id}", response_model=Dict[str, Any])
def update_gatewayconditiondecision(item_id: int, payload: GatewayConditionDecisionUpdateSchema):
    """Update existing GatewayConditionDecision record fields."""
    svc = GatewayConditionDecisionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_gatewayconditiondecision(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GatewayConditionDecision with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/gatewayconditiondecisions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gatewayconditiondecision(item_id: int, hard: bool = Query(False)):
    """Delete GatewayConditionDecision record (soft-delete by default)."""
    svc = GatewayConditionDecisionService()
    ok = svc.delete_gatewayconditiondecision(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GatewayConditionDecision with ID {item_id} not found")
    return None

@router.get("/gatewayconditiondecisions/analytics/metrics", response_model=Dict[str, Any])
def get_gatewayconditiondecision_metrics():
    """Calculate summary statistical KPIs for GatewayConditionDecision collection."""
    svc = GatewayConditionDecisionService()
    return svc.calculate_aggregate_metrics()

# ==================== TimerEventSubscription Endpoints ====================
@router.get("/timereventsubscriptions", response_model=List[Dict[str, Any]])
def list_timereventsubscriptions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TimerEventSubscription records with pagination and filtering."""
    svc = TimerEventSubscriptionService()
    items = svc.list_timereventsubscriptions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/timereventsubscriptions/{item_id}", response_model=Dict[str, Any])
def get_timereventsubscription_by_id(item_id: int):
    """Retrieve detailed record for TimerEventSubscription by ID."""
    svc = TimerEventSubscriptionService()
    item = svc.get_timereventsubscription_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TimerEventSubscription with ID {item_id} not found")
    return item.to_dict()

@router.post("/timereventsubscriptions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_timereventsubscription(payload: TimerEventSubscriptionCreateSchema):
    """Create new TimerEventSubscription instance in enterprise repository."""
    svc = TimerEventSubscriptionService()
    try:
        item = svc.create_timereventsubscription(
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

@router.put("/timereventsubscriptions/{item_id}", response_model=Dict[str, Any])
def update_timereventsubscription(item_id: int, payload: TimerEventSubscriptionUpdateSchema):
    """Update existing TimerEventSubscription record fields."""
    svc = TimerEventSubscriptionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_timereventsubscription(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TimerEventSubscription with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/timereventsubscriptions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_timereventsubscription(item_id: int, hard: bool = Query(False)):
    """Delete TimerEventSubscription record (soft-delete by default)."""
    svc = TimerEventSubscriptionService()
    ok = svc.delete_timereventsubscription(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TimerEventSubscription with ID {item_id} not found")
    return None

@router.get("/timereventsubscriptions/analytics/metrics", response_model=Dict[str, Any])
def get_timereventsubscription_metrics():
    """Calculate summary statistical KPIs for TimerEventSubscription collection."""
    svc = TimerEventSubscriptionService()
    return svc.calculate_aggregate_metrics()

# ==================== UserTaskAssignment Endpoints ====================
@router.get("/usertaskassignments", response_model=List[Dict[str, Any]])
def list_usertaskassignments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UserTaskAssignment records with pagination and filtering."""
    svc = UserTaskAssignmentService()
    items = svc.list_usertaskassignments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/usertaskassignments/{item_id}", response_model=Dict[str, Any])
def get_usertaskassignment_by_id(item_id: int):
    """Retrieve detailed record for UserTaskAssignment by ID."""
    svc = UserTaskAssignmentService()
    item = svc.get_usertaskassignment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UserTaskAssignment with ID {item_id} not found")
    return item.to_dict()

@router.post("/usertaskassignments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_usertaskassignment(payload: UserTaskAssignmentCreateSchema):
    """Create new UserTaskAssignment instance in enterprise repository."""
    svc = UserTaskAssignmentService()
    try:
        item = svc.create_usertaskassignment(
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

@router.put("/usertaskassignments/{item_id}", response_model=Dict[str, Any])
def update_usertaskassignment(item_id: int, payload: UserTaskAssignmentUpdateSchema):
    """Update existing UserTaskAssignment record fields."""
    svc = UserTaskAssignmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_usertaskassignment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UserTaskAssignment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/usertaskassignments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_usertaskassignment(item_id: int, hard: bool = Query(False)):
    """Delete UserTaskAssignment record (soft-delete by default)."""
    svc = UserTaskAssignmentService()
    ok = svc.delete_usertaskassignment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UserTaskAssignment with ID {item_id} not found")
    return None

@router.get("/usertaskassignments/analytics/metrics", response_model=Dict[str, Any])
def get_usertaskassignment_metrics():
    """Calculate summary statistical KPIs for UserTaskAssignment collection."""
    svc = UserTaskAssignmentService()
    return svc.calculate_aggregate_metrics()

# ==================== EscalationTriggerRule Endpoints ====================
@router.get("/escalationtriggerrules", response_model=List[Dict[str, Any]])
def list_escalationtriggerrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EscalationTriggerRule records with pagination and filtering."""
    svc = EscalationTriggerRuleService()
    items = svc.list_escalationtriggerrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/escalationtriggerrules/{item_id}", response_model=Dict[str, Any])
def get_escalationtriggerrule_by_id(item_id: int):
    """Retrieve detailed record for EscalationTriggerRule by ID."""
    svc = EscalationTriggerRuleService()
    item = svc.get_escalationtriggerrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EscalationTriggerRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/escalationtriggerrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_escalationtriggerrule(payload: EscalationTriggerRuleCreateSchema):
    """Create new EscalationTriggerRule instance in enterprise repository."""
    svc = EscalationTriggerRuleService()
    try:
        item = svc.create_escalationtriggerrule(
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

@router.put("/escalationtriggerrules/{item_id}", response_model=Dict[str, Any])
def update_escalationtriggerrule(item_id: int, payload: EscalationTriggerRuleUpdateSchema):
    """Update existing EscalationTriggerRule record fields."""
    svc = EscalationTriggerRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_escalationtriggerrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EscalationTriggerRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/escalationtriggerrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_escalationtriggerrule(item_id: int, hard: bool = Query(False)):
    """Delete EscalationTriggerRule record (soft-delete by default)."""
    svc = EscalationTriggerRuleService()
    ok = svc.delete_escalationtriggerrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EscalationTriggerRule with ID {item_id} not found")
    return None

@router.get("/escalationtriggerrules/analytics/metrics", response_model=Dict[str, Any])
def get_escalationtriggerrule_metrics():
    """Calculate summary statistical KPIs for EscalationTriggerRule collection."""
    svc = EscalationTriggerRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== VariableScopeStorage Endpoints ====================
@router.get("/variablescopestorages", response_model=List[Dict[str, Any]])
def list_variablescopestorages(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VariableScopeStorage records with pagination and filtering."""
    svc = VariableScopeStorageService()
    items = svc.list_variablescopestorages(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/variablescopestorages/{item_id}", response_model=Dict[str, Any])
def get_variablescopestorage_by_id(item_id: int):
    """Retrieve detailed record for VariableScopeStorage by ID."""
    svc = VariableScopeStorageService()
    item = svc.get_variablescopestorage_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VariableScopeStorage with ID {item_id} not found")
    return item.to_dict()

@router.post("/variablescopestorages", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_variablescopestorage(payload: VariableScopeStorageCreateSchema):
    """Create new VariableScopeStorage instance in enterprise repository."""
    svc = VariableScopeStorageService()
    try:
        item = svc.create_variablescopestorage(
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

@router.put("/variablescopestorages/{item_id}", response_model=Dict[str, Any])
def update_variablescopestorage(item_id: int, payload: VariableScopeStorageUpdateSchema):
    """Update existing VariableScopeStorage record fields."""
    svc = VariableScopeStorageService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_variablescopestorage(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VariableScopeStorage with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/variablescopestorages/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_variablescopestorage(item_id: int, hard: bool = Query(False)):
    """Delete VariableScopeStorage record (soft-delete by default)."""
    svc = VariableScopeStorageService()
    ok = svc.delete_variablescopestorage(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VariableScopeStorage with ID {item_id} not found")
    return None

@router.get("/variablescopestorages/analytics/metrics", response_model=Dict[str, Any])
def get_variablescopestorage_metrics():
    """Calculate summary statistical KPIs for VariableScopeStorage collection."""
    svc = VariableScopeStorageService()
    return svc.calculate_aggregate_metrics()

# ==================== ProcessHistoryAudit Endpoints ====================
@router.get("/processhistoryaudits", response_model=List[Dict[str, Any]])
def list_processhistoryaudits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProcessHistoryAudit records with pagination and filtering."""
    svc = ProcessHistoryAuditService()
    items = svc.list_processhistoryaudits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/processhistoryaudits/{item_id}", response_model=Dict[str, Any])
def get_processhistoryaudit_by_id(item_id: int):
    """Retrieve detailed record for ProcessHistoryAudit by ID."""
    svc = ProcessHistoryAuditService()
    item = svc.get_processhistoryaudit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProcessHistoryAudit with ID {item_id} not found")
    return item.to_dict()

@router.post("/processhistoryaudits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_processhistoryaudit(payload: ProcessHistoryAuditCreateSchema):
    """Create new ProcessHistoryAudit instance in enterprise repository."""
    svc = ProcessHistoryAuditService()
    try:
        item = svc.create_processhistoryaudit(
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

@router.put("/processhistoryaudits/{item_id}", response_model=Dict[str, Any])
def update_processhistoryaudit(item_id: int, payload: ProcessHistoryAuditUpdateSchema):
    """Update existing ProcessHistoryAudit record fields."""
    svc = ProcessHistoryAuditService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_processhistoryaudit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProcessHistoryAudit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/processhistoryaudits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_processhistoryaudit(item_id: int, hard: bool = Query(False)):
    """Delete ProcessHistoryAudit record (soft-delete by default)."""
    svc = ProcessHistoryAuditService()
    ok = svc.delete_processhistoryaudit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProcessHistoryAudit with ID {item_id} not found")
    return None

@router.get("/processhistoryaudits/analytics/metrics", response_model=Dict[str, Any])
def get_processhistoryaudit_metrics():
    """Calculate summary statistical KPIs for ProcessHistoryAudit collection."""
    svc = ProcessHistoryAuditService()
    return svc.calculate_aggregate_metrics()

# ==================== MessageCatchEvent Endpoints ====================
@router.get("/messagecatchevents", response_model=List[Dict[str, Any]])
def list_messagecatchevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MessageCatchEvent records with pagination and filtering."""
    svc = MessageCatchEventService()
    items = svc.list_messagecatchevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/messagecatchevents/{item_id}", response_model=Dict[str, Any])
def get_messagecatchevent_by_id(item_id: int):
    """Retrieve detailed record for MessageCatchEvent by ID."""
    svc = MessageCatchEventService()
    item = svc.get_messagecatchevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MessageCatchEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/messagecatchevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_messagecatchevent(payload: MessageCatchEventCreateSchema):
    """Create new MessageCatchEvent instance in enterprise repository."""
    svc = MessageCatchEventService()
    try:
        item = svc.create_messagecatchevent(
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

@router.put("/messagecatchevents/{item_id}", response_model=Dict[str, Any])
def update_messagecatchevent(item_id: int, payload: MessageCatchEventUpdateSchema):
    """Update existing MessageCatchEvent record fields."""
    svc = MessageCatchEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_messagecatchevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MessageCatchEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/messagecatchevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_messagecatchevent(item_id: int, hard: bool = Query(False)):
    """Delete MessageCatchEvent record (soft-delete by default)."""
    svc = MessageCatchEventService()
    ok = svc.delete_messagecatchevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MessageCatchEvent with ID {item_id} not found")
    return None

@router.get("/messagecatchevents/analytics/metrics", response_model=Dict[str, Any])
def get_messagecatchevent_metrics():
    """Calculate summary statistical KPIs for MessageCatchEvent collection."""
    svc = MessageCatchEventService()
    return svc.calculate_aggregate_metrics()

# ==================== SignalThrowEvent Endpoints ====================
@router.get("/signalthrowevents", response_model=List[Dict[str, Any]])
def list_signalthrowevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SignalThrowEvent records with pagination and filtering."""
    svc = SignalThrowEventService()
    items = svc.list_signalthrowevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/signalthrowevents/{item_id}", response_model=Dict[str, Any])
def get_signalthrowevent_by_id(item_id: int):
    """Retrieve detailed record for SignalThrowEvent by ID."""
    svc = SignalThrowEventService()
    item = svc.get_signalthrowevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SignalThrowEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/signalthrowevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_signalthrowevent(payload: SignalThrowEventCreateSchema):
    """Create new SignalThrowEvent instance in enterprise repository."""
    svc = SignalThrowEventService()
    try:
        item = svc.create_signalthrowevent(
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

@router.put("/signalthrowevents/{item_id}", response_model=Dict[str, Any])
def update_signalthrowevent(item_id: int, payload: SignalThrowEventUpdateSchema):
    """Update existing SignalThrowEvent record fields."""
    svc = SignalThrowEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_signalthrowevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SignalThrowEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/signalthrowevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_signalthrowevent(item_id: int, hard: bool = Query(False)):
    """Delete SignalThrowEvent record (soft-delete by default)."""
    svc = SignalThrowEventService()
    ok = svc.delete_signalthrowevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SignalThrowEvent with ID {item_id} not found")
    return None

@router.get("/signalthrowevents/analytics/metrics", response_model=Dict[str, Any])
def get_signalthrowevent_metrics():
    """Calculate summary statistical KPIs for SignalThrowEvent collection."""
    svc = SignalThrowEventService()
    return svc.calculate_aggregate_metrics()

# ==================== SubProcessScope Endpoints ====================
@router.get("/subprocessscopes", response_model=List[Dict[str, Any]])
def list_subprocessscopes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SubProcessScope records with pagination and filtering."""
    svc = SubProcessScopeService()
    items = svc.list_subprocessscopes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/subprocessscopes/{item_id}", response_model=Dict[str, Any])
def get_subprocessscope_by_id(item_id: int):
    """Retrieve detailed record for SubProcessScope by ID."""
    svc = SubProcessScopeService()
    item = svc.get_subprocessscope_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SubProcessScope with ID {item_id} not found")
    return item.to_dict()

@router.post("/subprocessscopes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_subprocessscope(payload: SubProcessScopeCreateSchema):
    """Create new SubProcessScope instance in enterprise repository."""
    svc = SubProcessScopeService()
    try:
        item = svc.create_subprocessscope(
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

@router.put("/subprocessscopes/{item_id}", response_model=Dict[str, Any])
def update_subprocessscope(item_id: int, payload: SubProcessScopeUpdateSchema):
    """Update existing SubProcessScope record fields."""
    svc = SubProcessScopeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_subprocessscope(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SubProcessScope with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/subprocessscopes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subprocessscope(item_id: int, hard: bool = Query(False)):
    """Delete SubProcessScope record (soft-delete by default)."""
    svc = SubProcessScopeService()
    ok = svc.delete_subprocessscope(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SubProcessScope with ID {item_id} not found")
    return None

@router.get("/subprocessscopes/analytics/metrics", response_model=Dict[str, Any])
def get_subprocessscope_metrics():
    """Calculate summary statistical KPIs for SubProcessScope collection."""
    svc = SubProcessScopeService()
    return svc.calculate_aggregate_metrics()

# ==================== CompensationHandler Endpoints ====================
@router.get("/compensationhandlers", response_model=List[Dict[str, Any]])
def list_compensationhandlers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CompensationHandler records with pagination and filtering."""
    svc = CompensationHandlerService()
    items = svc.list_compensationhandlers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/compensationhandlers/{item_id}", response_model=Dict[str, Any])
def get_compensationhandler_by_id(item_id: int):
    """Retrieve detailed record for CompensationHandler by ID."""
    svc = CompensationHandlerService()
    item = svc.get_compensationhandler_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CompensationHandler with ID {item_id} not found")
    return item.to_dict()

@router.post("/compensationhandlers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_compensationhandler(payload: CompensationHandlerCreateSchema):
    """Create new CompensationHandler instance in enterprise repository."""
    svc = CompensationHandlerService()
    try:
        item = svc.create_compensationhandler(
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

@router.put("/compensationhandlers/{item_id}", response_model=Dict[str, Any])
def update_compensationhandler(item_id: int, payload: CompensationHandlerUpdateSchema):
    """Update existing CompensationHandler record fields."""
    svc = CompensationHandlerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_compensationhandler(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CompensationHandler with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/compensationhandlers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_compensationhandler(item_id: int, hard: bool = Query(False)):
    """Delete CompensationHandler record (soft-delete by default)."""
    svc = CompensationHandlerService()
    ok = svc.delete_compensationhandler(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CompensationHandler with ID {item_id} not found")
    return None

@router.get("/compensationhandlers/analytics/metrics", response_model=Dict[str, Any])
def get_compensationhandler_metrics():
    """Calculate summary statistical KPIs for CompensationHandler collection."""
    svc = CompensationHandlerService()
    return svc.calculate_aggregate_metrics()

# ==================== ProcessMetricsAnalytics Endpoints ====================
@router.get("/processmetricsanalyticss", response_model=List[Dict[str, Any]])
def list_processmetricsanalyticss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProcessMetricsAnalytics records with pagination and filtering."""
    svc = ProcessMetricsAnalyticsService()
    items = svc.list_processmetricsanalyticss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/processmetricsanalyticss/{item_id}", response_model=Dict[str, Any])
def get_processmetricsanalytics_by_id(item_id: int):
    """Retrieve detailed record for ProcessMetricsAnalytics by ID."""
    svc = ProcessMetricsAnalyticsService()
    item = svc.get_processmetricsanalytics_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProcessMetricsAnalytics with ID {item_id} not found")
    return item.to_dict()

@router.post("/processmetricsanalyticss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_processmetricsanalytics(payload: ProcessMetricsAnalyticsCreateSchema):
    """Create new ProcessMetricsAnalytics instance in enterprise repository."""
    svc = ProcessMetricsAnalyticsService()
    try:
        item = svc.create_processmetricsanalytics(
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

@router.put("/processmetricsanalyticss/{item_id}", response_model=Dict[str, Any])
def update_processmetricsanalytics(item_id: int, payload: ProcessMetricsAnalyticsUpdateSchema):
    """Update existing ProcessMetricsAnalytics record fields."""
    svc = ProcessMetricsAnalyticsService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_processmetricsanalytics(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProcessMetricsAnalytics with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/processmetricsanalyticss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_processmetricsanalytics(item_id: int, hard: bool = Query(False)):
    """Delete ProcessMetricsAnalytics record (soft-delete by default)."""
    svc = ProcessMetricsAnalyticsService()
    ok = svc.delete_processmetricsanalytics(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProcessMetricsAnalytics with ID {item_id} not found")
    return None

@router.get("/processmetricsanalyticss/analytics/metrics", response_model=Dict[str, Any])
def get_processmetricsanalytics_metrics():
    """Calculate summary statistical KPIs for ProcessMetricsAnalytics collection."""
    svc = ProcessMetricsAnalyticsService()
    return svc.calculate_aggregate_metrics()

# ==================== DeploymentPackage Endpoints ====================
@router.get("/deploymentpackages", response_model=List[Dict[str, Any]])
def list_deploymentpackages(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeploymentPackage records with pagination and filtering."""
    svc = DeploymentPackageService()
    items = svc.list_deploymentpackages(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/deploymentpackages/{item_id}", response_model=Dict[str, Any])
def get_deploymentpackage_by_id(item_id: int):
    """Retrieve detailed record for DeploymentPackage by ID."""
    svc = DeploymentPackageService()
    item = svc.get_deploymentpackage_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeploymentPackage with ID {item_id} not found")
    return item.to_dict()

@router.post("/deploymentpackages", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_deploymentpackage(payload: DeploymentPackageCreateSchema):
    """Create new DeploymentPackage instance in enterprise repository."""
    svc = DeploymentPackageService()
    try:
        item = svc.create_deploymentpackage(
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

@router.put("/deploymentpackages/{item_id}", response_model=Dict[str, Any])
def update_deploymentpackage(item_id: int, payload: DeploymentPackageUpdateSchema):
    """Update existing DeploymentPackage record fields."""
    svc = DeploymentPackageService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_deploymentpackage(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeploymentPackage with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/deploymentpackages/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deploymentpackage(item_id: int, hard: bool = Query(False)):
    """Delete DeploymentPackage record (soft-delete by default)."""
    svc = DeploymentPackageService()
    ok = svc.delete_deploymentpackage(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeploymentPackage with ID {item_id} not found")
    return None

@router.get("/deploymentpackages/analytics/metrics", response_model=Dict[str, Any])
def get_deploymentpackage_metrics():
    """Calculate summary statistical KPIs for DeploymentPackage collection."""
    svc = DeploymentPackageService()
    return svc.calculate_aggregate_metrics()

