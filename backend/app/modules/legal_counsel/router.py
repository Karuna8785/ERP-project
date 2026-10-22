"""
Enterprise Legal Operations & Matter Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    LegalMatterCaseService,
    LitigationDocketService,
    OutsideCounselBillingService,
    LegalHoldOrderService,
    DiscoveryRequestEsiService,
    DepositionScheduleService,
    SubpoenaResponseService,
    SettlementAgreementService,
    RegulatoryInquiryCaseService,
    CourtFilingDocService,
    LegalBudgetForecastService,
    LegalSpendInvoiceService,
    ExpertWitnessRetainerService,
    PrivilegeLogDocumentService,
    ArbitrationProceedingService,
    CorporateResolutionService,
)
from .schemas import (
    LegalMatterCaseCreateSchema, LegalMatterCaseUpdateSchema, LegalMatterCaseResponseSchema,
    LitigationDocketCreateSchema, LitigationDocketUpdateSchema, LitigationDocketResponseSchema,
    OutsideCounselBillingCreateSchema, OutsideCounselBillingUpdateSchema, OutsideCounselBillingResponseSchema,
    LegalHoldOrderCreateSchema, LegalHoldOrderUpdateSchema, LegalHoldOrderResponseSchema,
    DiscoveryRequestEsiCreateSchema, DiscoveryRequestEsiUpdateSchema, DiscoveryRequestEsiResponseSchema,
    DepositionScheduleCreateSchema, DepositionScheduleUpdateSchema, DepositionScheduleResponseSchema,
    SubpoenaResponseCreateSchema, SubpoenaResponseUpdateSchema, SubpoenaResponseResponseSchema,
    SettlementAgreementCreateSchema, SettlementAgreementUpdateSchema, SettlementAgreementResponseSchema,
    RegulatoryInquiryCaseCreateSchema, RegulatoryInquiryCaseUpdateSchema, RegulatoryInquiryCaseResponseSchema,
    CourtFilingDocCreateSchema, CourtFilingDocUpdateSchema, CourtFilingDocResponseSchema,
    LegalBudgetForecastCreateSchema, LegalBudgetForecastUpdateSchema, LegalBudgetForecastResponseSchema,
    LegalSpendInvoiceCreateSchema, LegalSpendInvoiceUpdateSchema, LegalSpendInvoiceResponseSchema,
    ExpertWitnessRetainerCreateSchema, ExpertWitnessRetainerUpdateSchema, ExpertWitnessRetainerResponseSchema,
    PrivilegeLogDocumentCreateSchema, PrivilegeLogDocumentUpdateSchema, PrivilegeLogDocumentResponseSchema,
    ArbitrationProceedingCreateSchema, ArbitrationProceedingUpdateSchema, ArbitrationProceedingResponseSchema,
    CorporateResolutionCreateSchema, CorporateResolutionUpdateSchema, CorporateResolutionResponseSchema,
)

router = APIRouter(prefix="/legal_counsel", tags=["Enterprise Legal Operations & Matter Management"])

# ==================== LegalMatterCase Endpoints ====================
@router.get("/legalmattercases", response_model=List[Dict[str, Any]])
def list_legalmattercases(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LegalMatterCase records with pagination and filtering."""
    svc = LegalMatterCaseService()
    items = svc.list_legalmattercases(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/legalmattercases/{item_id}", response_model=Dict[str, Any])
def get_legalmattercase_by_id(item_id: int):
    """Retrieve detailed record for LegalMatterCase by ID."""
    svc = LegalMatterCaseService()
    item = svc.get_legalmattercase_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LegalMatterCase with ID {item_id} not found")
    return item.to_dict()

@router.post("/legalmattercases", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_legalmattercase(payload: LegalMatterCaseCreateSchema):
    """Create new LegalMatterCase instance in enterprise repository."""
    svc = LegalMatterCaseService()
    try:
        item = svc.create_legalmattercase(
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

@router.put("/legalmattercases/{item_id}", response_model=Dict[str, Any])
def update_legalmattercase(item_id: int, payload: LegalMatterCaseUpdateSchema):
    """Update existing LegalMatterCase record fields."""
    svc = LegalMatterCaseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_legalmattercase(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LegalMatterCase with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/legalmattercases/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legalmattercase(item_id: int, hard: bool = Query(False)):
    """Delete LegalMatterCase record (soft-delete by default)."""
    svc = LegalMatterCaseService()
    ok = svc.delete_legalmattercase(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LegalMatterCase with ID {item_id} not found")
    return None

@router.get("/legalmattercases/analytics/metrics", response_model=Dict[str, Any])
def get_legalmattercase_metrics():
    """Calculate summary statistical KPIs for LegalMatterCase collection."""
    svc = LegalMatterCaseService()
    return svc.calculate_aggregate_metrics()

# ==================== LitigationDocket Endpoints ====================
@router.get("/litigationdockets", response_model=List[Dict[str, Any]])
def list_litigationdockets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LitigationDocket records with pagination and filtering."""
    svc = LitigationDocketService()
    items = svc.list_litigationdockets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/litigationdockets/{item_id}", response_model=Dict[str, Any])
def get_litigationdocket_by_id(item_id: int):
    """Retrieve detailed record for LitigationDocket by ID."""
    svc = LitigationDocketService()
    item = svc.get_litigationdocket_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LitigationDocket with ID {item_id} not found")
    return item.to_dict()

@router.post("/litigationdockets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_litigationdocket(payload: LitigationDocketCreateSchema):
    """Create new LitigationDocket instance in enterprise repository."""
    svc = LitigationDocketService()
    try:
        item = svc.create_litigationdocket(
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

@router.put("/litigationdockets/{item_id}", response_model=Dict[str, Any])
def update_litigationdocket(item_id: int, payload: LitigationDocketUpdateSchema):
    """Update existing LitigationDocket record fields."""
    svc = LitigationDocketService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_litigationdocket(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LitigationDocket with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/litigationdockets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_litigationdocket(item_id: int, hard: bool = Query(False)):
    """Delete LitigationDocket record (soft-delete by default)."""
    svc = LitigationDocketService()
    ok = svc.delete_litigationdocket(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LitigationDocket with ID {item_id} not found")
    return None

@router.get("/litigationdockets/analytics/metrics", response_model=Dict[str, Any])
def get_litigationdocket_metrics():
    """Calculate summary statistical KPIs for LitigationDocket collection."""
    svc = LitigationDocketService()
    return svc.calculate_aggregate_metrics()

# ==================== OutsideCounselBilling Endpoints ====================
@router.get("/outsidecounselbillings", response_model=List[Dict[str, Any]])
def list_outsidecounselbillings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OutsideCounselBilling records with pagination and filtering."""
    svc = OutsideCounselBillingService()
    items = svc.list_outsidecounselbillings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/outsidecounselbillings/{item_id}", response_model=Dict[str, Any])
def get_outsidecounselbilling_by_id(item_id: int):
    """Retrieve detailed record for OutsideCounselBilling by ID."""
    svc = OutsideCounselBillingService()
    item = svc.get_outsidecounselbilling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OutsideCounselBilling with ID {item_id} not found")
    return item.to_dict()

@router.post("/outsidecounselbillings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_outsidecounselbilling(payload: OutsideCounselBillingCreateSchema):
    """Create new OutsideCounselBilling instance in enterprise repository."""
    svc = OutsideCounselBillingService()
    try:
        item = svc.create_outsidecounselbilling(
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

@router.put("/outsidecounselbillings/{item_id}", response_model=Dict[str, Any])
def update_outsidecounselbilling(item_id: int, payload: OutsideCounselBillingUpdateSchema):
    """Update existing OutsideCounselBilling record fields."""
    svc = OutsideCounselBillingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_outsidecounselbilling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OutsideCounselBilling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/outsidecounselbillings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_outsidecounselbilling(item_id: int, hard: bool = Query(False)):
    """Delete OutsideCounselBilling record (soft-delete by default)."""
    svc = OutsideCounselBillingService()
    ok = svc.delete_outsidecounselbilling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OutsideCounselBilling with ID {item_id} not found")
    return None

@router.get("/outsidecounselbillings/analytics/metrics", response_model=Dict[str, Any])
def get_outsidecounselbilling_metrics():
    """Calculate summary statistical KPIs for OutsideCounselBilling collection."""
    svc = OutsideCounselBillingService()
    return svc.calculate_aggregate_metrics()

# ==================== LegalHoldOrder Endpoints ====================
@router.get("/legalholdorders", response_model=List[Dict[str, Any]])
def list_legalholdorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LegalHoldOrder records with pagination and filtering."""
    svc = LegalHoldOrderService()
    items = svc.list_legalholdorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/legalholdorders/{item_id}", response_model=Dict[str, Any])
def get_legalholdorder_by_id(item_id: int):
    """Retrieve detailed record for LegalHoldOrder by ID."""
    svc = LegalHoldOrderService()
    item = svc.get_legalholdorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LegalHoldOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/legalholdorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_legalholdorder(payload: LegalHoldOrderCreateSchema):
    """Create new LegalHoldOrder instance in enterprise repository."""
    svc = LegalHoldOrderService()
    try:
        item = svc.create_legalholdorder(
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

@router.put("/legalholdorders/{item_id}", response_model=Dict[str, Any])
def update_legalholdorder(item_id: int, payload: LegalHoldOrderUpdateSchema):
    """Update existing LegalHoldOrder record fields."""
    svc = LegalHoldOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_legalholdorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LegalHoldOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/legalholdorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legalholdorder(item_id: int, hard: bool = Query(False)):
    """Delete LegalHoldOrder record (soft-delete by default)."""
    svc = LegalHoldOrderService()
    ok = svc.delete_legalholdorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LegalHoldOrder with ID {item_id} not found")
    return None

@router.get("/legalholdorders/analytics/metrics", response_model=Dict[str, Any])
def get_legalholdorder_metrics():
    """Calculate summary statistical KPIs for LegalHoldOrder collection."""
    svc = LegalHoldOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== DiscoveryRequestEsi Endpoints ====================
@router.get("/discoveryrequestesis", response_model=List[Dict[str, Any]])
def list_discoveryrequestesis(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DiscoveryRequestEsi records with pagination and filtering."""
    svc = DiscoveryRequestEsiService()
    items = svc.list_discoveryrequestesis(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/discoveryrequestesis/{item_id}", response_model=Dict[str, Any])
def get_discoveryrequestesi_by_id(item_id: int):
    """Retrieve detailed record for DiscoveryRequestEsi by ID."""
    svc = DiscoveryRequestEsiService()
    item = svc.get_discoveryrequestesi_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DiscoveryRequestEsi with ID {item_id} not found")
    return item.to_dict()

@router.post("/discoveryrequestesis", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_discoveryrequestesi(payload: DiscoveryRequestEsiCreateSchema):
    """Create new DiscoveryRequestEsi instance in enterprise repository."""
    svc = DiscoveryRequestEsiService()
    try:
        item = svc.create_discoveryrequestesi(
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

@router.put("/discoveryrequestesis/{item_id}", response_model=Dict[str, Any])
def update_discoveryrequestesi(item_id: int, payload: DiscoveryRequestEsiUpdateSchema):
    """Update existing DiscoveryRequestEsi record fields."""
    svc = DiscoveryRequestEsiService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_discoveryrequestesi(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DiscoveryRequestEsi with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/discoveryrequestesis/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_discoveryrequestesi(item_id: int, hard: bool = Query(False)):
    """Delete DiscoveryRequestEsi record (soft-delete by default)."""
    svc = DiscoveryRequestEsiService()
    ok = svc.delete_discoveryrequestesi(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DiscoveryRequestEsi with ID {item_id} not found")
    return None

@router.get("/discoveryrequestesis/analytics/metrics", response_model=Dict[str, Any])
def get_discoveryrequestesi_metrics():
    """Calculate summary statistical KPIs for DiscoveryRequestEsi collection."""
    svc = DiscoveryRequestEsiService()
    return svc.calculate_aggregate_metrics()

# ==================== DepositionSchedule Endpoints ====================
@router.get("/depositionschedules", response_model=List[Dict[str, Any]])
def list_depositionschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DepositionSchedule records with pagination and filtering."""
    svc = DepositionScheduleService()
    items = svc.list_depositionschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/depositionschedules/{item_id}", response_model=Dict[str, Any])
def get_depositionschedule_by_id(item_id: int):
    """Retrieve detailed record for DepositionSchedule by ID."""
    svc = DepositionScheduleService()
    item = svc.get_depositionschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DepositionSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/depositionschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_depositionschedule(payload: DepositionScheduleCreateSchema):
    """Create new DepositionSchedule instance in enterprise repository."""
    svc = DepositionScheduleService()
    try:
        item = svc.create_depositionschedule(
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

@router.put("/depositionschedules/{item_id}", response_model=Dict[str, Any])
def update_depositionschedule(item_id: int, payload: DepositionScheduleUpdateSchema):
    """Update existing DepositionSchedule record fields."""
    svc = DepositionScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_depositionschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DepositionSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/depositionschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_depositionschedule(item_id: int, hard: bool = Query(False)):
    """Delete DepositionSchedule record (soft-delete by default)."""
    svc = DepositionScheduleService()
    ok = svc.delete_depositionschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DepositionSchedule with ID {item_id} not found")
    return None

@router.get("/depositionschedules/analytics/metrics", response_model=Dict[str, Any])
def get_depositionschedule_metrics():
    """Calculate summary statistical KPIs for DepositionSchedule collection."""
    svc = DepositionScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== SubpoenaResponse Endpoints ====================
@router.get("/subpoenaresponses", response_model=List[Dict[str, Any]])
def list_subpoenaresponses(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SubpoenaResponse records with pagination and filtering."""
    svc = SubpoenaResponseService()
    items = svc.list_subpoenaresponses(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/subpoenaresponses/{item_id}", response_model=Dict[str, Any])
def get_subpoenaresponse_by_id(item_id: int):
    """Retrieve detailed record for SubpoenaResponse by ID."""
    svc = SubpoenaResponseService()
    item = svc.get_subpoenaresponse_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SubpoenaResponse with ID {item_id} not found")
    return item.to_dict()

@router.post("/subpoenaresponses", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_subpoenaresponse(payload: SubpoenaResponseCreateSchema):
    """Create new SubpoenaResponse instance in enterprise repository."""
    svc = SubpoenaResponseService()
    try:
        item = svc.create_subpoenaresponse(
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

@router.put("/subpoenaresponses/{item_id}", response_model=Dict[str, Any])
def update_subpoenaresponse(item_id: int, payload: SubpoenaResponseUpdateSchema):
    """Update existing SubpoenaResponse record fields."""
    svc = SubpoenaResponseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_subpoenaresponse(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SubpoenaResponse with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/subpoenaresponses/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subpoenaresponse(item_id: int, hard: bool = Query(False)):
    """Delete SubpoenaResponse record (soft-delete by default)."""
    svc = SubpoenaResponseService()
    ok = svc.delete_subpoenaresponse(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SubpoenaResponse with ID {item_id} not found")
    return None

@router.get("/subpoenaresponses/analytics/metrics", response_model=Dict[str, Any])
def get_subpoenaresponse_metrics():
    """Calculate summary statistical KPIs for SubpoenaResponse collection."""
    svc = SubpoenaResponseService()
    return svc.calculate_aggregate_metrics()

# ==================== SettlementAgreement Endpoints ====================
@router.get("/settlementagreements", response_model=List[Dict[str, Any]])
def list_settlementagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SettlementAgreement records with pagination and filtering."""
    svc = SettlementAgreementService()
    items = svc.list_settlementagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/settlementagreements/{item_id}", response_model=Dict[str, Any])
def get_settlementagreement_by_id(item_id: int):
    """Retrieve detailed record for SettlementAgreement by ID."""
    svc = SettlementAgreementService()
    item = svc.get_settlementagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SettlementAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/settlementagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_settlementagreement(payload: SettlementAgreementCreateSchema):
    """Create new SettlementAgreement instance in enterprise repository."""
    svc = SettlementAgreementService()
    try:
        item = svc.create_settlementagreement(
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

@router.put("/settlementagreements/{item_id}", response_model=Dict[str, Any])
def update_settlementagreement(item_id: int, payload: SettlementAgreementUpdateSchema):
    """Update existing SettlementAgreement record fields."""
    svc = SettlementAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_settlementagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SettlementAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/settlementagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_settlementagreement(item_id: int, hard: bool = Query(False)):
    """Delete SettlementAgreement record (soft-delete by default)."""
    svc = SettlementAgreementService()
    ok = svc.delete_settlementagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SettlementAgreement with ID {item_id} not found")
    return None

@router.get("/settlementagreements/analytics/metrics", response_model=Dict[str, Any])
def get_settlementagreement_metrics():
    """Calculate summary statistical KPIs for SettlementAgreement collection."""
    svc = SettlementAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== RegulatoryInquiryCase Endpoints ====================
@router.get("/regulatoryinquirycases", response_model=List[Dict[str, Any]])
def list_regulatoryinquirycases(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RegulatoryInquiryCase records with pagination and filtering."""
    svc = RegulatoryInquiryCaseService()
    items = svc.list_regulatoryinquirycases(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/regulatoryinquirycases/{item_id}", response_model=Dict[str, Any])
def get_regulatoryinquirycase_by_id(item_id: int):
    """Retrieve detailed record for RegulatoryInquiryCase by ID."""
    svc = RegulatoryInquiryCaseService()
    item = svc.get_regulatoryinquirycase_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RegulatoryInquiryCase with ID {item_id} not found")
    return item.to_dict()

@router.post("/regulatoryinquirycases", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_regulatoryinquirycase(payload: RegulatoryInquiryCaseCreateSchema):
    """Create new RegulatoryInquiryCase instance in enterprise repository."""
    svc = RegulatoryInquiryCaseService()
    try:
        item = svc.create_regulatoryinquirycase(
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

@router.put("/regulatoryinquirycases/{item_id}", response_model=Dict[str, Any])
def update_regulatoryinquirycase(item_id: int, payload: RegulatoryInquiryCaseUpdateSchema):
    """Update existing RegulatoryInquiryCase record fields."""
    svc = RegulatoryInquiryCaseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_regulatoryinquirycase(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RegulatoryInquiryCase with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/regulatoryinquirycases/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_regulatoryinquirycase(item_id: int, hard: bool = Query(False)):
    """Delete RegulatoryInquiryCase record (soft-delete by default)."""
    svc = RegulatoryInquiryCaseService()
    ok = svc.delete_regulatoryinquirycase(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RegulatoryInquiryCase with ID {item_id} not found")
    return None

@router.get("/regulatoryinquirycases/analytics/metrics", response_model=Dict[str, Any])
def get_regulatoryinquirycase_metrics():
    """Calculate summary statistical KPIs for RegulatoryInquiryCase collection."""
    svc = RegulatoryInquiryCaseService()
    return svc.calculate_aggregate_metrics()

# ==================== CourtFilingDoc Endpoints ====================
@router.get("/courtfilingdocs", response_model=List[Dict[str, Any]])
def list_courtfilingdocs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CourtFilingDoc records with pagination and filtering."""
    svc = CourtFilingDocService()
    items = svc.list_courtfilingdocs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/courtfilingdocs/{item_id}", response_model=Dict[str, Any])
def get_courtfilingdoc_by_id(item_id: int):
    """Retrieve detailed record for CourtFilingDoc by ID."""
    svc = CourtFilingDocService()
    item = svc.get_courtfilingdoc_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CourtFilingDoc with ID {item_id} not found")
    return item.to_dict()

@router.post("/courtfilingdocs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_courtfilingdoc(payload: CourtFilingDocCreateSchema):
    """Create new CourtFilingDoc instance in enterprise repository."""
    svc = CourtFilingDocService()
    try:
        item = svc.create_courtfilingdoc(
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

@router.put("/courtfilingdocs/{item_id}", response_model=Dict[str, Any])
def update_courtfilingdoc(item_id: int, payload: CourtFilingDocUpdateSchema):
    """Update existing CourtFilingDoc record fields."""
    svc = CourtFilingDocService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_courtfilingdoc(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CourtFilingDoc with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/courtfilingdocs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_courtfilingdoc(item_id: int, hard: bool = Query(False)):
    """Delete CourtFilingDoc record (soft-delete by default)."""
    svc = CourtFilingDocService()
    ok = svc.delete_courtfilingdoc(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CourtFilingDoc with ID {item_id} not found")
    return None

@router.get("/courtfilingdocs/analytics/metrics", response_model=Dict[str, Any])
def get_courtfilingdoc_metrics():
    """Calculate summary statistical KPIs for CourtFilingDoc collection."""
    svc = CourtFilingDocService()
    return svc.calculate_aggregate_metrics()

# ==================== LegalBudgetForecast Endpoints ====================
@router.get("/legalbudgetforecasts", response_model=List[Dict[str, Any]])
def list_legalbudgetforecasts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LegalBudgetForecast records with pagination and filtering."""
    svc = LegalBudgetForecastService()
    items = svc.list_legalbudgetforecasts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/legalbudgetforecasts/{item_id}", response_model=Dict[str, Any])
def get_legalbudgetforecast_by_id(item_id: int):
    """Retrieve detailed record for LegalBudgetForecast by ID."""
    svc = LegalBudgetForecastService()
    item = svc.get_legalbudgetforecast_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LegalBudgetForecast with ID {item_id} not found")
    return item.to_dict()

@router.post("/legalbudgetforecasts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_legalbudgetforecast(payload: LegalBudgetForecastCreateSchema):
    """Create new LegalBudgetForecast instance in enterprise repository."""
    svc = LegalBudgetForecastService()
    try:
        item = svc.create_legalbudgetforecast(
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

@router.put("/legalbudgetforecasts/{item_id}", response_model=Dict[str, Any])
def update_legalbudgetforecast(item_id: int, payload: LegalBudgetForecastUpdateSchema):
    """Update existing LegalBudgetForecast record fields."""
    svc = LegalBudgetForecastService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_legalbudgetforecast(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LegalBudgetForecast with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/legalbudgetforecasts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legalbudgetforecast(item_id: int, hard: bool = Query(False)):
    """Delete LegalBudgetForecast record (soft-delete by default)."""
    svc = LegalBudgetForecastService()
    ok = svc.delete_legalbudgetforecast(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LegalBudgetForecast with ID {item_id} not found")
    return None

@router.get("/legalbudgetforecasts/analytics/metrics", response_model=Dict[str, Any])
def get_legalbudgetforecast_metrics():
    """Calculate summary statistical KPIs for LegalBudgetForecast collection."""
    svc = LegalBudgetForecastService()
    return svc.calculate_aggregate_metrics()

# ==================== LegalSpendInvoice Endpoints ====================
@router.get("/legalspendinvoices", response_model=List[Dict[str, Any]])
def list_legalspendinvoices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LegalSpendInvoice records with pagination and filtering."""
    svc = LegalSpendInvoiceService()
    items = svc.list_legalspendinvoices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/legalspendinvoices/{item_id}", response_model=Dict[str, Any])
def get_legalspendinvoice_by_id(item_id: int):
    """Retrieve detailed record for LegalSpendInvoice by ID."""
    svc = LegalSpendInvoiceService()
    item = svc.get_legalspendinvoice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LegalSpendInvoice with ID {item_id} not found")
    return item.to_dict()

@router.post("/legalspendinvoices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_legalspendinvoice(payload: LegalSpendInvoiceCreateSchema):
    """Create new LegalSpendInvoice instance in enterprise repository."""
    svc = LegalSpendInvoiceService()
    try:
        item = svc.create_legalspendinvoice(
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

@router.put("/legalspendinvoices/{item_id}", response_model=Dict[str, Any])
def update_legalspendinvoice(item_id: int, payload: LegalSpendInvoiceUpdateSchema):
    """Update existing LegalSpendInvoice record fields."""
    svc = LegalSpendInvoiceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_legalspendinvoice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LegalSpendInvoice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/legalspendinvoices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legalspendinvoice(item_id: int, hard: bool = Query(False)):
    """Delete LegalSpendInvoice record (soft-delete by default)."""
    svc = LegalSpendInvoiceService()
    ok = svc.delete_legalspendinvoice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LegalSpendInvoice with ID {item_id} not found")
    return None

@router.get("/legalspendinvoices/analytics/metrics", response_model=Dict[str, Any])
def get_legalspendinvoice_metrics():
    """Calculate summary statistical KPIs for LegalSpendInvoice collection."""
    svc = LegalSpendInvoiceService()
    return svc.calculate_aggregate_metrics()

# ==================== ExpertWitnessRetainer Endpoints ====================
@router.get("/expertwitnessretainers", response_model=List[Dict[str, Any]])
def list_expertwitnessretainers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExpertWitnessRetainer records with pagination and filtering."""
    svc = ExpertWitnessRetainerService()
    items = svc.list_expertwitnessretainers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/expertwitnessretainers/{item_id}", response_model=Dict[str, Any])
def get_expertwitnessretainer_by_id(item_id: int):
    """Retrieve detailed record for ExpertWitnessRetainer by ID."""
    svc = ExpertWitnessRetainerService()
    item = svc.get_expertwitnessretainer_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExpertWitnessRetainer with ID {item_id} not found")
    return item.to_dict()

@router.post("/expertwitnessretainers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_expertwitnessretainer(payload: ExpertWitnessRetainerCreateSchema):
    """Create new ExpertWitnessRetainer instance in enterprise repository."""
    svc = ExpertWitnessRetainerService()
    try:
        item = svc.create_expertwitnessretainer(
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

@router.put("/expertwitnessretainers/{item_id}", response_model=Dict[str, Any])
def update_expertwitnessretainer(item_id: int, payload: ExpertWitnessRetainerUpdateSchema):
    """Update existing ExpertWitnessRetainer record fields."""
    svc = ExpertWitnessRetainerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_expertwitnessretainer(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExpertWitnessRetainer with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/expertwitnessretainers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expertwitnessretainer(item_id: int, hard: bool = Query(False)):
    """Delete ExpertWitnessRetainer record (soft-delete by default)."""
    svc = ExpertWitnessRetainerService()
    ok = svc.delete_expertwitnessretainer(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExpertWitnessRetainer with ID {item_id} not found")
    return None

@router.get("/expertwitnessretainers/analytics/metrics", response_model=Dict[str, Any])
def get_expertwitnessretainer_metrics():
    """Calculate summary statistical KPIs for ExpertWitnessRetainer collection."""
    svc = ExpertWitnessRetainerService()
    return svc.calculate_aggregate_metrics()

# ==================== PrivilegeLogDocument Endpoints ====================
@router.get("/privilegelogdocuments", response_model=List[Dict[str, Any]])
def list_privilegelogdocuments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PrivilegeLogDocument records with pagination and filtering."""
    svc = PrivilegeLogDocumentService()
    items = svc.list_privilegelogdocuments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/privilegelogdocuments/{item_id}", response_model=Dict[str, Any])
def get_privilegelogdocument_by_id(item_id: int):
    """Retrieve detailed record for PrivilegeLogDocument by ID."""
    svc = PrivilegeLogDocumentService()
    item = svc.get_privilegelogdocument_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PrivilegeLogDocument with ID {item_id} not found")
    return item.to_dict()

@router.post("/privilegelogdocuments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_privilegelogdocument(payload: PrivilegeLogDocumentCreateSchema):
    """Create new PrivilegeLogDocument instance in enterprise repository."""
    svc = PrivilegeLogDocumentService()
    try:
        item = svc.create_privilegelogdocument(
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

@router.put("/privilegelogdocuments/{item_id}", response_model=Dict[str, Any])
def update_privilegelogdocument(item_id: int, payload: PrivilegeLogDocumentUpdateSchema):
    """Update existing PrivilegeLogDocument record fields."""
    svc = PrivilegeLogDocumentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_privilegelogdocument(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PrivilegeLogDocument with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/privilegelogdocuments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_privilegelogdocument(item_id: int, hard: bool = Query(False)):
    """Delete PrivilegeLogDocument record (soft-delete by default)."""
    svc = PrivilegeLogDocumentService()
    ok = svc.delete_privilegelogdocument(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PrivilegeLogDocument with ID {item_id} not found")
    return None

@router.get("/privilegelogdocuments/analytics/metrics", response_model=Dict[str, Any])
def get_privilegelogdocument_metrics():
    """Calculate summary statistical KPIs for PrivilegeLogDocument collection."""
    svc = PrivilegeLogDocumentService()
    return svc.calculate_aggregate_metrics()

# ==================== ArbitrationProceeding Endpoints ====================
@router.get("/arbitrationproceedings", response_model=List[Dict[str, Any]])
def list_arbitrationproceedings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ArbitrationProceeding records with pagination and filtering."""
    svc = ArbitrationProceedingService()
    items = svc.list_arbitrationproceedings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/arbitrationproceedings/{item_id}", response_model=Dict[str, Any])
def get_arbitrationproceeding_by_id(item_id: int):
    """Retrieve detailed record for ArbitrationProceeding by ID."""
    svc = ArbitrationProceedingService()
    item = svc.get_arbitrationproceeding_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ArbitrationProceeding with ID {item_id} not found")
    return item.to_dict()

@router.post("/arbitrationproceedings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_arbitrationproceeding(payload: ArbitrationProceedingCreateSchema):
    """Create new ArbitrationProceeding instance in enterprise repository."""
    svc = ArbitrationProceedingService()
    try:
        item = svc.create_arbitrationproceeding(
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

@router.put("/arbitrationproceedings/{item_id}", response_model=Dict[str, Any])
def update_arbitrationproceeding(item_id: int, payload: ArbitrationProceedingUpdateSchema):
    """Update existing ArbitrationProceeding record fields."""
    svc = ArbitrationProceedingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_arbitrationproceeding(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ArbitrationProceeding with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/arbitrationproceedings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_arbitrationproceeding(item_id: int, hard: bool = Query(False)):
    """Delete ArbitrationProceeding record (soft-delete by default)."""
    svc = ArbitrationProceedingService()
    ok = svc.delete_arbitrationproceeding(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ArbitrationProceeding with ID {item_id} not found")
    return None

@router.get("/arbitrationproceedings/analytics/metrics", response_model=Dict[str, Any])
def get_arbitrationproceeding_metrics():
    """Calculate summary statistical KPIs for ArbitrationProceeding collection."""
    svc = ArbitrationProceedingService()
    return svc.calculate_aggregate_metrics()

# ==================== CorporateResolution Endpoints ====================
@router.get("/corporateresolutions", response_model=List[Dict[str, Any]])
def list_corporateresolutions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CorporateResolution records with pagination and filtering."""
    svc = CorporateResolutionService()
    items = svc.list_corporateresolutions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/corporateresolutions/{item_id}", response_model=Dict[str, Any])
def get_corporateresolution_by_id(item_id: int):
    """Retrieve detailed record for CorporateResolution by ID."""
    svc = CorporateResolutionService()
    item = svc.get_corporateresolution_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CorporateResolution with ID {item_id} not found")
    return item.to_dict()

@router.post("/corporateresolutions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_corporateresolution(payload: CorporateResolutionCreateSchema):
    """Create new CorporateResolution instance in enterprise repository."""
    svc = CorporateResolutionService()
    try:
        item = svc.create_corporateresolution(
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

@router.put("/corporateresolutions/{item_id}", response_model=Dict[str, Any])
def update_corporateresolution(item_id: int, payload: CorporateResolutionUpdateSchema):
    """Update existing CorporateResolution record fields."""
    svc = CorporateResolutionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_corporateresolution(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CorporateResolution with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/corporateresolutions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_corporateresolution(item_id: int, hard: bool = Query(False)):
    """Delete CorporateResolution record (soft-delete by default)."""
    svc = CorporateResolutionService()
    ok = svc.delete_corporateresolution(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CorporateResolution with ID {item_id} not found")
    return None

@router.get("/corporateresolutions/analytics/metrics", response_model=Dict[str, Any])
def get_corporateresolution_metrics():
    """Calculate summary statistical KPIs for CorporateResolution collection."""
    svc = CorporateResolutionService()
    return svc.calculate_aggregate_metrics()

