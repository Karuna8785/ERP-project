"""
Enterprise Service Desk & SLA Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    SupportTicketService,
    TicketMessageService,
    SLAPolicyService,
    EscalationRuleService,
    TicketCategoryService,
    CannedResponseService,
    KnowledgeArticleService,
    CustomerSatisfactionService,
    WarrantyClaimService,
    RMAAuthorizationService,
    ServiceContractService,
    AgentWorkloadService,
    TimeTrackingService,
    FieldServiceJobService,
    IncidentReportService,
    ChangeRequestService,
)
from .schemas import (
    SupportTicketCreateSchema, SupportTicketUpdateSchema, SupportTicketResponseSchema,
    TicketMessageCreateSchema, TicketMessageUpdateSchema, TicketMessageResponseSchema,
    SLAPolicyCreateSchema, SLAPolicyUpdateSchema, SLAPolicyResponseSchema,
    EscalationRuleCreateSchema, EscalationRuleUpdateSchema, EscalationRuleResponseSchema,
    TicketCategoryCreateSchema, TicketCategoryUpdateSchema, TicketCategoryResponseSchema,
    CannedResponseCreateSchema, CannedResponseUpdateSchema, CannedResponseResponseSchema,
    KnowledgeArticleCreateSchema, KnowledgeArticleUpdateSchema, KnowledgeArticleResponseSchema,
    CustomerSatisfactionCreateSchema, CustomerSatisfactionUpdateSchema, CustomerSatisfactionResponseSchema,
    WarrantyClaimCreateSchema, WarrantyClaimUpdateSchema, WarrantyClaimResponseSchema,
    RMAAuthorizationCreateSchema, RMAAuthorizationUpdateSchema, RMAAuthorizationResponseSchema,
    ServiceContractCreateSchema, ServiceContractUpdateSchema, ServiceContractResponseSchema,
    AgentWorkloadCreateSchema, AgentWorkloadUpdateSchema, AgentWorkloadResponseSchema,
    TimeTrackingCreateSchema, TimeTrackingUpdateSchema, TimeTrackingResponseSchema,
    FieldServiceJobCreateSchema, FieldServiceJobUpdateSchema, FieldServiceJobResponseSchema,
    IncidentReportCreateSchema, IncidentReportUpdateSchema, IncidentReportResponseSchema,
    ChangeRequestCreateSchema, ChangeRequestUpdateSchema, ChangeRequestResponseSchema,
)

router = APIRouter(prefix="/helpdesk", tags=["Enterprise Service Desk & SLA Management"])

# ==================== SupportTicket Endpoints ====================
@router.get("/supporttickets", response_model=List[Dict[str, Any]])
def list_supporttickets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupportTicket records with pagination and filtering."""
    svc = SupportTicketService()
    items = svc.list_supporttickets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supporttickets/{item_id}", response_model=Dict[str, Any])
def get_supportticket_by_id(item_id: int):
    """Retrieve detailed record for SupportTicket by ID."""
    svc = SupportTicketService()
    item = svc.get_supportticket_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupportTicket with ID {item_id} not found")
    return item.to_dict()

@router.post("/supporttickets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supportticket(payload: SupportTicketCreateSchema):
    """Create new SupportTicket instance in enterprise repository."""
    svc = SupportTicketService()
    try:
        item = svc.create_supportticket(
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

@router.put("/supporttickets/{item_id}", response_model=Dict[str, Any])
def update_supportticket(item_id: int, payload: SupportTicketUpdateSchema):
    """Update existing SupportTicket record fields."""
    svc = SupportTicketService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supportticket(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupportTicket with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supporttickets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supportticket(item_id: int, hard: bool = Query(False)):
    """Delete SupportTicket record (soft-delete by default)."""
    svc = SupportTicketService()
    ok = svc.delete_supportticket(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupportTicket with ID {item_id} not found")
    return None

@router.get("/supporttickets/analytics/metrics", response_model=Dict[str, Any])
def get_supportticket_metrics():
    """Calculate summary statistical KPIs for SupportTicket collection."""
    svc = SupportTicketService()
    return svc.calculate_aggregate_metrics()

# ==================== TicketMessage Endpoints ====================
@router.get("/ticketmessages", response_model=List[Dict[str, Any]])
def list_ticketmessages(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TicketMessage records with pagination and filtering."""
    svc = TicketMessageService()
    items = svc.list_ticketmessages(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ticketmessages/{item_id}", response_model=Dict[str, Any])
def get_ticketmessage_by_id(item_id: int):
    """Retrieve detailed record for TicketMessage by ID."""
    svc = TicketMessageService()
    item = svc.get_ticketmessage_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TicketMessage with ID {item_id} not found")
    return item.to_dict()

@router.post("/ticketmessages", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ticketmessage(payload: TicketMessageCreateSchema):
    """Create new TicketMessage instance in enterprise repository."""
    svc = TicketMessageService()
    try:
        item = svc.create_ticketmessage(
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

@router.put("/ticketmessages/{item_id}", response_model=Dict[str, Any])
def update_ticketmessage(item_id: int, payload: TicketMessageUpdateSchema):
    """Update existing TicketMessage record fields."""
    svc = TicketMessageService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ticketmessage(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TicketMessage with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ticketmessages/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticketmessage(item_id: int, hard: bool = Query(False)):
    """Delete TicketMessage record (soft-delete by default)."""
    svc = TicketMessageService()
    ok = svc.delete_ticketmessage(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TicketMessage with ID {item_id} not found")
    return None

@router.get("/ticketmessages/analytics/metrics", response_model=Dict[str, Any])
def get_ticketmessage_metrics():
    """Calculate summary statistical KPIs for TicketMessage collection."""
    svc = TicketMessageService()
    return svc.calculate_aggregate_metrics()

# ==================== SLAPolicy Endpoints ====================
@router.get("/slapolicys", response_model=List[Dict[str, Any]])
def list_slapolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SLAPolicy records with pagination and filtering."""
    svc = SLAPolicyService()
    items = svc.list_slapolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/slapolicys/{item_id}", response_model=Dict[str, Any])
def get_slapolicy_by_id(item_id: int):
    """Retrieve detailed record for SLAPolicy by ID."""
    svc = SLAPolicyService()
    item = svc.get_slapolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SLAPolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/slapolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_slapolicy(payload: SLAPolicyCreateSchema):
    """Create new SLAPolicy instance in enterprise repository."""
    svc = SLAPolicyService()
    try:
        item = svc.create_slapolicy(
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

@router.put("/slapolicys/{item_id}", response_model=Dict[str, Any])
def update_slapolicy(item_id: int, payload: SLAPolicyUpdateSchema):
    """Update existing SLAPolicy record fields."""
    svc = SLAPolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_slapolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SLAPolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/slapolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_slapolicy(item_id: int, hard: bool = Query(False)):
    """Delete SLAPolicy record (soft-delete by default)."""
    svc = SLAPolicyService()
    ok = svc.delete_slapolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SLAPolicy with ID {item_id} not found")
    return None

@router.get("/slapolicys/analytics/metrics", response_model=Dict[str, Any])
def get_slapolicy_metrics():
    """Calculate summary statistical KPIs for SLAPolicy collection."""
    svc = SLAPolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== EscalationRule Endpoints ====================
@router.get("/escalationrules", response_model=List[Dict[str, Any]])
def list_escalationrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EscalationRule records with pagination and filtering."""
    svc = EscalationRuleService()
    items = svc.list_escalationrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/escalationrules/{item_id}", response_model=Dict[str, Any])
def get_escalationrule_by_id(item_id: int):
    """Retrieve detailed record for EscalationRule by ID."""
    svc = EscalationRuleService()
    item = svc.get_escalationrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EscalationRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/escalationrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_escalationrule(payload: EscalationRuleCreateSchema):
    """Create new EscalationRule instance in enterprise repository."""
    svc = EscalationRuleService()
    try:
        item = svc.create_escalationrule(
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

@router.put("/escalationrules/{item_id}", response_model=Dict[str, Any])
def update_escalationrule(item_id: int, payload: EscalationRuleUpdateSchema):
    """Update existing EscalationRule record fields."""
    svc = EscalationRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_escalationrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EscalationRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/escalationrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_escalationrule(item_id: int, hard: bool = Query(False)):
    """Delete EscalationRule record (soft-delete by default)."""
    svc = EscalationRuleService()
    ok = svc.delete_escalationrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EscalationRule with ID {item_id} not found")
    return None

@router.get("/escalationrules/analytics/metrics", response_model=Dict[str, Any])
def get_escalationrule_metrics():
    """Calculate summary statistical KPIs for EscalationRule collection."""
    svc = EscalationRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== TicketCategory Endpoints ====================
@router.get("/ticketcategorys", response_model=List[Dict[str, Any]])
def list_ticketcategorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TicketCategory records with pagination and filtering."""
    svc = TicketCategoryService()
    items = svc.list_ticketcategorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ticketcategorys/{item_id}", response_model=Dict[str, Any])
def get_ticketcategory_by_id(item_id: int):
    """Retrieve detailed record for TicketCategory by ID."""
    svc = TicketCategoryService()
    item = svc.get_ticketcategory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TicketCategory with ID {item_id} not found")
    return item.to_dict()

@router.post("/ticketcategorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ticketcategory(payload: TicketCategoryCreateSchema):
    """Create new TicketCategory instance in enterprise repository."""
    svc = TicketCategoryService()
    try:
        item = svc.create_ticketcategory(
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

@router.put("/ticketcategorys/{item_id}", response_model=Dict[str, Any])
def update_ticketcategory(item_id: int, payload: TicketCategoryUpdateSchema):
    """Update existing TicketCategory record fields."""
    svc = TicketCategoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ticketcategory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TicketCategory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ticketcategorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticketcategory(item_id: int, hard: bool = Query(False)):
    """Delete TicketCategory record (soft-delete by default)."""
    svc = TicketCategoryService()
    ok = svc.delete_ticketcategory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TicketCategory with ID {item_id} not found")
    return None

@router.get("/ticketcategorys/analytics/metrics", response_model=Dict[str, Any])
def get_ticketcategory_metrics():
    """Calculate summary statistical KPIs for TicketCategory collection."""
    svc = TicketCategoryService()
    return svc.calculate_aggregate_metrics()

# ==================== CannedResponse Endpoints ====================
@router.get("/cannedresponses", response_model=List[Dict[str, Any]])
def list_cannedresponses(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CannedResponse records with pagination and filtering."""
    svc = CannedResponseService()
    items = svc.list_cannedresponses(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cannedresponses/{item_id}", response_model=Dict[str, Any])
def get_cannedresponse_by_id(item_id: int):
    """Retrieve detailed record for CannedResponse by ID."""
    svc = CannedResponseService()
    item = svc.get_cannedresponse_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CannedResponse with ID {item_id} not found")
    return item.to_dict()

@router.post("/cannedresponses", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cannedresponse(payload: CannedResponseCreateSchema):
    """Create new CannedResponse instance in enterprise repository."""
    svc = CannedResponseService()
    try:
        item = svc.create_cannedresponse(
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

@router.put("/cannedresponses/{item_id}", response_model=Dict[str, Any])
def update_cannedresponse(item_id: int, payload: CannedResponseUpdateSchema):
    """Update existing CannedResponse record fields."""
    svc = CannedResponseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cannedresponse(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CannedResponse with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cannedresponses/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cannedresponse(item_id: int, hard: bool = Query(False)):
    """Delete CannedResponse record (soft-delete by default)."""
    svc = CannedResponseService()
    ok = svc.delete_cannedresponse(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CannedResponse with ID {item_id} not found")
    return None

@router.get("/cannedresponses/analytics/metrics", response_model=Dict[str, Any])
def get_cannedresponse_metrics():
    """Calculate summary statistical KPIs for CannedResponse collection."""
    svc = CannedResponseService()
    return svc.calculate_aggregate_metrics()

# ==================== KnowledgeArticle Endpoints ====================
@router.get("/knowledgearticles", response_model=List[Dict[str, Any]])
def list_knowledgearticles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List KnowledgeArticle records with pagination and filtering."""
    svc = KnowledgeArticleService()
    items = svc.list_knowledgearticles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/knowledgearticles/{item_id}", response_model=Dict[str, Any])
def get_knowledgearticle_by_id(item_id: int):
    """Retrieve detailed record for KnowledgeArticle by ID."""
    svc = KnowledgeArticleService()
    item = svc.get_knowledgearticle_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"KnowledgeArticle with ID {item_id} not found")
    return item.to_dict()

@router.post("/knowledgearticles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_knowledgearticle(payload: KnowledgeArticleCreateSchema):
    """Create new KnowledgeArticle instance in enterprise repository."""
    svc = KnowledgeArticleService()
    try:
        item = svc.create_knowledgearticle(
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

@router.put("/knowledgearticles/{item_id}", response_model=Dict[str, Any])
def update_knowledgearticle(item_id: int, payload: KnowledgeArticleUpdateSchema):
    """Update existing KnowledgeArticle record fields."""
    svc = KnowledgeArticleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_knowledgearticle(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"KnowledgeArticle with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/knowledgearticles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_knowledgearticle(item_id: int, hard: bool = Query(False)):
    """Delete KnowledgeArticle record (soft-delete by default)."""
    svc = KnowledgeArticleService()
    ok = svc.delete_knowledgearticle(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"KnowledgeArticle with ID {item_id} not found")
    return None

@router.get("/knowledgearticles/analytics/metrics", response_model=Dict[str, Any])
def get_knowledgearticle_metrics():
    """Calculate summary statistical KPIs for KnowledgeArticle collection."""
    svc = KnowledgeArticleService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerSatisfaction Endpoints ====================
@router.get("/customersatisfactions", response_model=List[Dict[str, Any]])
def list_customersatisfactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerSatisfaction records with pagination and filtering."""
    svc = CustomerSatisfactionService()
    items = svc.list_customersatisfactions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customersatisfactions/{item_id}", response_model=Dict[str, Any])
def get_customersatisfaction_by_id(item_id: int):
    """Retrieve detailed record for CustomerSatisfaction by ID."""
    svc = CustomerSatisfactionService()
    item = svc.get_customersatisfaction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerSatisfaction with ID {item_id} not found")
    return item.to_dict()

@router.post("/customersatisfactions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customersatisfaction(payload: CustomerSatisfactionCreateSchema):
    """Create new CustomerSatisfaction instance in enterprise repository."""
    svc = CustomerSatisfactionService()
    try:
        item = svc.create_customersatisfaction(
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

@router.put("/customersatisfactions/{item_id}", response_model=Dict[str, Any])
def update_customersatisfaction(item_id: int, payload: CustomerSatisfactionUpdateSchema):
    """Update existing CustomerSatisfaction record fields."""
    svc = CustomerSatisfactionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customersatisfaction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerSatisfaction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customersatisfactions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customersatisfaction(item_id: int, hard: bool = Query(False)):
    """Delete CustomerSatisfaction record (soft-delete by default)."""
    svc = CustomerSatisfactionService()
    ok = svc.delete_customersatisfaction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerSatisfaction with ID {item_id} not found")
    return None

@router.get("/customersatisfactions/analytics/metrics", response_model=Dict[str, Any])
def get_customersatisfaction_metrics():
    """Calculate summary statistical KPIs for CustomerSatisfaction collection."""
    svc = CustomerSatisfactionService()
    return svc.calculate_aggregate_metrics()

# ==================== WarrantyClaim Endpoints ====================
@router.get("/warrantyclaims", response_model=List[Dict[str, Any]])
def list_warrantyclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WarrantyClaim records with pagination and filtering."""
    svc = WarrantyClaimService()
    items = svc.list_warrantyclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/warrantyclaims/{item_id}", response_model=Dict[str, Any])
def get_warrantyclaim_by_id(item_id: int):
    """Retrieve detailed record for WarrantyClaim by ID."""
    svc = WarrantyClaimService()
    item = svc.get_warrantyclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WarrantyClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/warrantyclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_warrantyclaim(payload: WarrantyClaimCreateSchema):
    """Create new WarrantyClaim instance in enterprise repository."""
    svc = WarrantyClaimService()
    try:
        item = svc.create_warrantyclaim(
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

@router.put("/warrantyclaims/{item_id}", response_model=Dict[str, Any])
def update_warrantyclaim(item_id: int, payload: WarrantyClaimUpdateSchema):
    """Update existing WarrantyClaim record fields."""
    svc = WarrantyClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_warrantyclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WarrantyClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/warrantyclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warrantyclaim(item_id: int, hard: bool = Query(False)):
    """Delete WarrantyClaim record (soft-delete by default)."""
    svc = WarrantyClaimService()
    ok = svc.delete_warrantyclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WarrantyClaim with ID {item_id} not found")
    return None

@router.get("/warrantyclaims/analytics/metrics", response_model=Dict[str, Any])
def get_warrantyclaim_metrics():
    """Calculate summary statistical KPIs for WarrantyClaim collection."""
    svc = WarrantyClaimService()
    return svc.calculate_aggregate_metrics()

# ==================== RMAAuthorization Endpoints ====================
@router.get("/rmaauthorizations", response_model=List[Dict[str, Any]])
def list_rmaauthorizations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RMAAuthorization records with pagination and filtering."""
    svc = RMAAuthorizationService()
    items = svc.list_rmaauthorizations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/rmaauthorizations/{item_id}", response_model=Dict[str, Any])
def get_rmaauthorization_by_id(item_id: int):
    """Retrieve detailed record for RMAAuthorization by ID."""
    svc = RMAAuthorizationService()
    item = svc.get_rmaauthorization_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RMAAuthorization with ID {item_id} not found")
    return item.to_dict()

@router.post("/rmaauthorizations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_rmaauthorization(payload: RMAAuthorizationCreateSchema):
    """Create new RMAAuthorization instance in enterprise repository."""
    svc = RMAAuthorizationService()
    try:
        item = svc.create_rmaauthorization(
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

@router.put("/rmaauthorizations/{item_id}", response_model=Dict[str, Any])
def update_rmaauthorization(item_id: int, payload: RMAAuthorizationUpdateSchema):
    """Update existing RMAAuthorization record fields."""
    svc = RMAAuthorizationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_rmaauthorization(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RMAAuthorization with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/rmaauthorizations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rmaauthorization(item_id: int, hard: bool = Query(False)):
    """Delete RMAAuthorization record (soft-delete by default)."""
    svc = RMAAuthorizationService()
    ok = svc.delete_rmaauthorization(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RMAAuthorization with ID {item_id} not found")
    return None

@router.get("/rmaauthorizations/analytics/metrics", response_model=Dict[str, Any])
def get_rmaauthorization_metrics():
    """Calculate summary statistical KPIs for RMAAuthorization collection."""
    svc = RMAAuthorizationService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceContract Endpoints ====================
@router.get("/servicecontracts", response_model=List[Dict[str, Any]])
def list_servicecontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceContract records with pagination and filtering."""
    svc = ServiceContractService()
    items = svc.list_servicecontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicecontracts/{item_id}", response_model=Dict[str, Any])
def get_servicecontract_by_id(item_id: int):
    """Retrieve detailed record for ServiceContract by ID."""
    svc = ServiceContractService()
    item = svc.get_servicecontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicecontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicecontract(payload: ServiceContractCreateSchema):
    """Create new ServiceContract instance in enterprise repository."""
    svc = ServiceContractService()
    try:
        item = svc.create_servicecontract(
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

@router.put("/servicecontracts/{item_id}", response_model=Dict[str, Any])
def update_servicecontract(item_id: int, payload: ServiceContractUpdateSchema):
    """Update existing ServiceContract record fields."""
    svc = ServiceContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicecontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicecontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicecontract(item_id: int, hard: bool = Query(False)):
    """Delete ServiceContract record (soft-delete by default)."""
    svc = ServiceContractService()
    ok = svc.delete_servicecontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceContract with ID {item_id} not found")
    return None

@router.get("/servicecontracts/analytics/metrics", response_model=Dict[str, Any])
def get_servicecontract_metrics():
    """Calculate summary statistical KPIs for ServiceContract collection."""
    svc = ServiceContractService()
    return svc.calculate_aggregate_metrics()

# ==================== AgentWorkload Endpoints ====================
@router.get("/agentworkloads", response_model=List[Dict[str, Any]])
def list_agentworkloads(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AgentWorkload records with pagination and filtering."""
    svc = AgentWorkloadService()
    items = svc.list_agentworkloads(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/agentworkloads/{item_id}", response_model=Dict[str, Any])
def get_agentworkload_by_id(item_id: int):
    """Retrieve detailed record for AgentWorkload by ID."""
    svc = AgentWorkloadService()
    item = svc.get_agentworkload_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AgentWorkload with ID {item_id} not found")
    return item.to_dict()

@router.post("/agentworkloads", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_agentworkload(payload: AgentWorkloadCreateSchema):
    """Create new AgentWorkload instance in enterprise repository."""
    svc = AgentWorkloadService()
    try:
        item = svc.create_agentworkload(
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

@router.put("/agentworkloads/{item_id}", response_model=Dict[str, Any])
def update_agentworkload(item_id: int, payload: AgentWorkloadUpdateSchema):
    """Update existing AgentWorkload record fields."""
    svc = AgentWorkloadService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_agentworkload(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AgentWorkload with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/agentworkloads/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_agentworkload(item_id: int, hard: bool = Query(False)):
    """Delete AgentWorkload record (soft-delete by default)."""
    svc = AgentWorkloadService()
    ok = svc.delete_agentworkload(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AgentWorkload with ID {item_id} not found")
    return None

@router.get("/agentworkloads/analytics/metrics", response_model=Dict[str, Any])
def get_agentworkload_metrics():
    """Calculate summary statistical KPIs for AgentWorkload collection."""
    svc = AgentWorkloadService()
    return svc.calculate_aggregate_metrics()

# ==================== TimeTracking Endpoints ====================
@router.get("/timetrackings", response_model=List[Dict[str, Any]])
def list_timetrackings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TimeTracking records with pagination and filtering."""
    svc = TimeTrackingService()
    items = svc.list_timetrackings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/timetrackings/{item_id}", response_model=Dict[str, Any])
def get_timetracking_by_id(item_id: int):
    """Retrieve detailed record for TimeTracking by ID."""
    svc = TimeTrackingService()
    item = svc.get_timetracking_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TimeTracking with ID {item_id} not found")
    return item.to_dict()

@router.post("/timetrackings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_timetracking(payload: TimeTrackingCreateSchema):
    """Create new TimeTracking instance in enterprise repository."""
    svc = TimeTrackingService()
    try:
        item = svc.create_timetracking(
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

@router.put("/timetrackings/{item_id}", response_model=Dict[str, Any])
def update_timetracking(item_id: int, payload: TimeTrackingUpdateSchema):
    """Update existing TimeTracking record fields."""
    svc = TimeTrackingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_timetracking(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TimeTracking with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/timetrackings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_timetracking(item_id: int, hard: bool = Query(False)):
    """Delete TimeTracking record (soft-delete by default)."""
    svc = TimeTrackingService()
    ok = svc.delete_timetracking(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TimeTracking with ID {item_id} not found")
    return None

@router.get("/timetrackings/analytics/metrics", response_model=Dict[str, Any])
def get_timetracking_metrics():
    """Calculate summary statistical KPIs for TimeTracking collection."""
    svc = TimeTrackingService()
    return svc.calculate_aggregate_metrics()

# ==================== FieldServiceJob Endpoints ====================
@router.get("/fieldservicejobs", response_model=List[Dict[str, Any]])
def list_fieldservicejobs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FieldServiceJob records with pagination and filtering."""
    svc = FieldServiceJobService()
    items = svc.list_fieldservicejobs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fieldservicejobs/{item_id}", response_model=Dict[str, Any])
def get_fieldservicejob_by_id(item_id: int):
    """Retrieve detailed record for FieldServiceJob by ID."""
    svc = FieldServiceJobService()
    item = svc.get_fieldservicejob_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FieldServiceJob with ID {item_id} not found")
    return item.to_dict()

@router.post("/fieldservicejobs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fieldservicejob(payload: FieldServiceJobCreateSchema):
    """Create new FieldServiceJob instance in enterprise repository."""
    svc = FieldServiceJobService()
    try:
        item = svc.create_fieldservicejob(
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

@router.put("/fieldservicejobs/{item_id}", response_model=Dict[str, Any])
def update_fieldservicejob(item_id: int, payload: FieldServiceJobUpdateSchema):
    """Update existing FieldServiceJob record fields."""
    svc = FieldServiceJobService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fieldservicejob(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FieldServiceJob with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fieldservicejobs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fieldservicejob(item_id: int, hard: bool = Query(False)):
    """Delete FieldServiceJob record (soft-delete by default)."""
    svc = FieldServiceJobService()
    ok = svc.delete_fieldservicejob(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FieldServiceJob with ID {item_id} not found")
    return None

@router.get("/fieldservicejobs/analytics/metrics", response_model=Dict[str, Any])
def get_fieldservicejob_metrics():
    """Calculate summary statistical KPIs for FieldServiceJob collection."""
    svc = FieldServiceJobService()
    return svc.calculate_aggregate_metrics()

# ==================== IncidentReport Endpoints ====================
@router.get("/incidentreports", response_model=List[Dict[str, Any]])
def list_incidentreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IncidentReport records with pagination and filtering."""
    svc = IncidentReportService()
    items = svc.list_incidentreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/incidentreports/{item_id}", response_model=Dict[str, Any])
def get_incidentreport_by_id(item_id: int):
    """Retrieve detailed record for IncidentReport by ID."""
    svc = IncidentReportService()
    item = svc.get_incidentreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IncidentReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/incidentreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_incidentreport(payload: IncidentReportCreateSchema):
    """Create new IncidentReport instance in enterprise repository."""
    svc = IncidentReportService()
    try:
        item = svc.create_incidentreport(
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

@router.put("/incidentreports/{item_id}", response_model=Dict[str, Any])
def update_incidentreport(item_id: int, payload: IncidentReportUpdateSchema):
    """Update existing IncidentReport record fields."""
    svc = IncidentReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_incidentreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IncidentReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/incidentreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incidentreport(item_id: int, hard: bool = Query(False)):
    """Delete IncidentReport record (soft-delete by default)."""
    svc = IncidentReportService()
    ok = svc.delete_incidentreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IncidentReport with ID {item_id} not found")
    return None

@router.get("/incidentreports/analytics/metrics", response_model=Dict[str, Any])
def get_incidentreport_metrics():
    """Calculate summary statistical KPIs for IncidentReport collection."""
    svc = IncidentReportService()
    return svc.calculate_aggregate_metrics()

# ==================== ChangeRequest Endpoints ====================
@router.get("/changerequests", response_model=List[Dict[str, Any]])
def list_changerequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChangeRequest records with pagination and filtering."""
    svc = ChangeRequestService()
    items = svc.list_changerequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/changerequests/{item_id}", response_model=Dict[str, Any])
def get_changerequest_by_id(item_id: int):
    """Retrieve detailed record for ChangeRequest by ID."""
    svc = ChangeRequestService()
    item = svc.get_changerequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChangeRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/changerequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_changerequest(payload: ChangeRequestCreateSchema):
    """Create new ChangeRequest instance in enterprise repository."""
    svc = ChangeRequestService()
    try:
        item = svc.create_changerequest(
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

@router.put("/changerequests/{item_id}", response_model=Dict[str, Any])
def update_changerequest(item_id: int, payload: ChangeRequestUpdateSchema):
    """Update existing ChangeRequest record fields."""
    svc = ChangeRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_changerequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChangeRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/changerequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_changerequest(item_id: int, hard: bool = Query(False)):
    """Delete ChangeRequest record (soft-delete by default)."""
    svc = ChangeRequestService()
    ok = svc.delete_changerequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChangeRequest with ID {item_id} not found")
    return None

@router.get("/changerequests/analytics/metrics", response_model=Dict[str, Any])
def get_changerequest_metrics():
    """Calculate summary statistical KPIs for ChangeRequest collection."""
    svc = ChangeRequestService()
    return svc.calculate_aggregate_metrics()

