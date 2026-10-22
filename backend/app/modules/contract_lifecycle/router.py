"""
Enterprise Contract Lifecycle Management (CLM) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    MasterServiceAgreementService,
    NonDisclosureAgreementService,
    StatementOfWorkService,
    ContractAmendmentService,
    ClauseLibraryItemService,
    ContractObligationService,
    MilestonePaymentTermService,
    RenewalNoticeEventService,
    ContractRiskAssessmentService,
    LegalRedlineVersionService,
    SignatoryApprovalMatrixService,
    TerminationNoticeService,
    SLAComplianceCheckService,
    ContractRepositoryIndexService,
    VendorContractLinkService,
    CustomerContractLinkService,
)
from .schemas import (
    MasterServiceAgreementCreateSchema, MasterServiceAgreementUpdateSchema, MasterServiceAgreementResponseSchema,
    NonDisclosureAgreementCreateSchema, NonDisclosureAgreementUpdateSchema, NonDisclosureAgreementResponseSchema,
    StatementOfWorkCreateSchema, StatementOfWorkUpdateSchema, StatementOfWorkResponseSchema,
    ContractAmendmentCreateSchema, ContractAmendmentUpdateSchema, ContractAmendmentResponseSchema,
    ClauseLibraryItemCreateSchema, ClauseLibraryItemUpdateSchema, ClauseLibraryItemResponseSchema,
    ContractObligationCreateSchema, ContractObligationUpdateSchema, ContractObligationResponseSchema,
    MilestonePaymentTermCreateSchema, MilestonePaymentTermUpdateSchema, MilestonePaymentTermResponseSchema,
    RenewalNoticeEventCreateSchema, RenewalNoticeEventUpdateSchema, RenewalNoticeEventResponseSchema,
    ContractRiskAssessmentCreateSchema, ContractRiskAssessmentUpdateSchema, ContractRiskAssessmentResponseSchema,
    LegalRedlineVersionCreateSchema, LegalRedlineVersionUpdateSchema, LegalRedlineVersionResponseSchema,
    SignatoryApprovalMatrixCreateSchema, SignatoryApprovalMatrixUpdateSchema, SignatoryApprovalMatrixResponseSchema,
    TerminationNoticeCreateSchema, TerminationNoticeUpdateSchema, TerminationNoticeResponseSchema,
    SLAComplianceCheckCreateSchema, SLAComplianceCheckUpdateSchema, SLAComplianceCheckResponseSchema,
    ContractRepositoryIndexCreateSchema, ContractRepositoryIndexUpdateSchema, ContractRepositoryIndexResponseSchema,
    VendorContractLinkCreateSchema, VendorContractLinkUpdateSchema, VendorContractLinkResponseSchema,
    CustomerContractLinkCreateSchema, CustomerContractLinkUpdateSchema, CustomerContractLinkResponseSchema,
)

router = APIRouter(prefix="/contract_lifecycle", tags=["Enterprise Contract Lifecycle Management (CLM)"])

# ==================== MasterServiceAgreement Endpoints ====================
@router.get("/masterserviceagreements", response_model=List[Dict[str, Any]])
def list_masterserviceagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MasterServiceAgreement records with pagination and filtering."""
    svc = MasterServiceAgreementService()
    items = svc.list_masterserviceagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/masterserviceagreements/{item_id}", response_model=Dict[str, Any])
def get_masterserviceagreement_by_id(item_id: int):
    """Retrieve detailed record for MasterServiceAgreement by ID."""
    svc = MasterServiceAgreementService()
    item = svc.get_masterserviceagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MasterServiceAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/masterserviceagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_masterserviceagreement(payload: MasterServiceAgreementCreateSchema):
    """Create new MasterServiceAgreement instance in enterprise repository."""
    svc = MasterServiceAgreementService()
    try:
        item = svc.create_masterserviceagreement(
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

@router.put("/masterserviceagreements/{item_id}", response_model=Dict[str, Any])
def update_masterserviceagreement(item_id: int, payload: MasterServiceAgreementUpdateSchema):
    """Update existing MasterServiceAgreement record fields."""
    svc = MasterServiceAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_masterserviceagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MasterServiceAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/masterserviceagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_masterserviceagreement(item_id: int, hard: bool = Query(False)):
    """Delete MasterServiceAgreement record (soft-delete by default)."""
    svc = MasterServiceAgreementService()
    ok = svc.delete_masterserviceagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MasterServiceAgreement with ID {item_id} not found")
    return None

@router.get("/masterserviceagreements/analytics/metrics", response_model=Dict[str, Any])
def get_masterserviceagreement_metrics():
    """Calculate summary statistical KPIs for MasterServiceAgreement collection."""
    svc = MasterServiceAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== NonDisclosureAgreement Endpoints ====================
@router.get("/nondisclosureagreements", response_model=List[Dict[str, Any]])
def list_nondisclosureagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List NonDisclosureAgreement records with pagination and filtering."""
    svc = NonDisclosureAgreementService()
    items = svc.list_nondisclosureagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/nondisclosureagreements/{item_id}", response_model=Dict[str, Any])
def get_nondisclosureagreement_by_id(item_id: int):
    """Retrieve detailed record for NonDisclosureAgreement by ID."""
    svc = NonDisclosureAgreementService()
    item = svc.get_nondisclosureagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"NonDisclosureAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/nondisclosureagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_nondisclosureagreement(payload: NonDisclosureAgreementCreateSchema):
    """Create new NonDisclosureAgreement instance in enterprise repository."""
    svc = NonDisclosureAgreementService()
    try:
        item = svc.create_nondisclosureagreement(
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

@router.put("/nondisclosureagreements/{item_id}", response_model=Dict[str, Any])
def update_nondisclosureagreement(item_id: int, payload: NonDisclosureAgreementUpdateSchema):
    """Update existing NonDisclosureAgreement record fields."""
    svc = NonDisclosureAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_nondisclosureagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"NonDisclosureAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/nondisclosureagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nondisclosureagreement(item_id: int, hard: bool = Query(False)):
    """Delete NonDisclosureAgreement record (soft-delete by default)."""
    svc = NonDisclosureAgreementService()
    ok = svc.delete_nondisclosureagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"NonDisclosureAgreement with ID {item_id} not found")
    return None

@router.get("/nondisclosureagreements/analytics/metrics", response_model=Dict[str, Any])
def get_nondisclosureagreement_metrics():
    """Calculate summary statistical KPIs for NonDisclosureAgreement collection."""
    svc = NonDisclosureAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== StatementOfWork Endpoints ====================
@router.get("/statementofworks", response_model=List[Dict[str, Any]])
def list_statementofworks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StatementOfWork records with pagination and filtering."""
    svc = StatementOfWorkService()
    items = svc.list_statementofworks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/statementofworks/{item_id}", response_model=Dict[str, Any])
def get_statementofwork_by_id(item_id: int):
    """Retrieve detailed record for StatementOfWork by ID."""
    svc = StatementOfWorkService()
    item = svc.get_statementofwork_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StatementOfWork with ID {item_id} not found")
    return item.to_dict()

@router.post("/statementofworks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_statementofwork(payload: StatementOfWorkCreateSchema):
    """Create new StatementOfWork instance in enterprise repository."""
    svc = StatementOfWorkService()
    try:
        item = svc.create_statementofwork(
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

@router.put("/statementofworks/{item_id}", response_model=Dict[str, Any])
def update_statementofwork(item_id: int, payload: StatementOfWorkUpdateSchema):
    """Update existing StatementOfWork record fields."""
    svc = StatementOfWorkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_statementofwork(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StatementOfWork with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/statementofworks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_statementofwork(item_id: int, hard: bool = Query(False)):
    """Delete StatementOfWork record (soft-delete by default)."""
    svc = StatementOfWorkService()
    ok = svc.delete_statementofwork(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StatementOfWork with ID {item_id} not found")
    return None

@router.get("/statementofworks/analytics/metrics", response_model=Dict[str, Any])
def get_statementofwork_metrics():
    """Calculate summary statistical KPIs for StatementOfWork collection."""
    svc = StatementOfWorkService()
    return svc.calculate_aggregate_metrics()

# ==================== ContractAmendment Endpoints ====================
@router.get("/contractamendments", response_model=List[Dict[str, Any]])
def list_contractamendments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContractAmendment records with pagination and filtering."""
    svc = ContractAmendmentService()
    items = svc.list_contractamendments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/contractamendments/{item_id}", response_model=Dict[str, Any])
def get_contractamendment_by_id(item_id: int):
    """Retrieve detailed record for ContractAmendment by ID."""
    svc = ContractAmendmentService()
    item = svc.get_contractamendment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContractAmendment with ID {item_id} not found")
    return item.to_dict()

@router.post("/contractamendments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_contractamendment(payload: ContractAmendmentCreateSchema):
    """Create new ContractAmendment instance in enterprise repository."""
    svc = ContractAmendmentService()
    try:
        item = svc.create_contractamendment(
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

@router.put("/contractamendments/{item_id}", response_model=Dict[str, Any])
def update_contractamendment(item_id: int, payload: ContractAmendmentUpdateSchema):
    """Update existing ContractAmendment record fields."""
    svc = ContractAmendmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_contractamendment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContractAmendment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/contractamendments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contractamendment(item_id: int, hard: bool = Query(False)):
    """Delete ContractAmendment record (soft-delete by default)."""
    svc = ContractAmendmentService()
    ok = svc.delete_contractamendment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContractAmendment with ID {item_id} not found")
    return None

@router.get("/contractamendments/analytics/metrics", response_model=Dict[str, Any])
def get_contractamendment_metrics():
    """Calculate summary statistical KPIs for ContractAmendment collection."""
    svc = ContractAmendmentService()
    return svc.calculate_aggregate_metrics()

# ==================== ClauseLibraryItem Endpoints ====================
@router.get("/clauselibraryitems", response_model=List[Dict[str, Any]])
def list_clauselibraryitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ClauseLibraryItem records with pagination and filtering."""
    svc = ClauseLibraryItemService()
    items = svc.list_clauselibraryitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/clauselibraryitems/{item_id}", response_model=Dict[str, Any])
def get_clauselibraryitem_by_id(item_id: int):
    """Retrieve detailed record for ClauseLibraryItem by ID."""
    svc = ClauseLibraryItemService()
    item = svc.get_clauselibraryitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ClauseLibraryItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/clauselibraryitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_clauselibraryitem(payload: ClauseLibraryItemCreateSchema):
    """Create new ClauseLibraryItem instance in enterprise repository."""
    svc = ClauseLibraryItemService()
    try:
        item = svc.create_clauselibraryitem(
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

@router.put("/clauselibraryitems/{item_id}", response_model=Dict[str, Any])
def update_clauselibraryitem(item_id: int, payload: ClauseLibraryItemUpdateSchema):
    """Update existing ClauseLibraryItem record fields."""
    svc = ClauseLibraryItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_clauselibraryitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ClauseLibraryItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/clauselibraryitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_clauselibraryitem(item_id: int, hard: bool = Query(False)):
    """Delete ClauseLibraryItem record (soft-delete by default)."""
    svc = ClauseLibraryItemService()
    ok = svc.delete_clauselibraryitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ClauseLibraryItem with ID {item_id} not found")
    return None

@router.get("/clauselibraryitems/analytics/metrics", response_model=Dict[str, Any])
def get_clauselibraryitem_metrics():
    """Calculate summary statistical KPIs for ClauseLibraryItem collection."""
    svc = ClauseLibraryItemService()
    return svc.calculate_aggregate_metrics()

# ==================== ContractObligation Endpoints ====================
@router.get("/contractobligations", response_model=List[Dict[str, Any]])
def list_contractobligations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContractObligation records with pagination and filtering."""
    svc = ContractObligationService()
    items = svc.list_contractobligations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/contractobligations/{item_id}", response_model=Dict[str, Any])
def get_contractobligation_by_id(item_id: int):
    """Retrieve detailed record for ContractObligation by ID."""
    svc = ContractObligationService()
    item = svc.get_contractobligation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContractObligation with ID {item_id} not found")
    return item.to_dict()

@router.post("/contractobligations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_contractobligation(payload: ContractObligationCreateSchema):
    """Create new ContractObligation instance in enterprise repository."""
    svc = ContractObligationService()
    try:
        item = svc.create_contractobligation(
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

@router.put("/contractobligations/{item_id}", response_model=Dict[str, Any])
def update_contractobligation(item_id: int, payload: ContractObligationUpdateSchema):
    """Update existing ContractObligation record fields."""
    svc = ContractObligationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_contractobligation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContractObligation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/contractobligations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contractobligation(item_id: int, hard: bool = Query(False)):
    """Delete ContractObligation record (soft-delete by default)."""
    svc = ContractObligationService()
    ok = svc.delete_contractobligation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContractObligation with ID {item_id} not found")
    return None

@router.get("/contractobligations/analytics/metrics", response_model=Dict[str, Any])
def get_contractobligation_metrics():
    """Calculate summary statistical KPIs for ContractObligation collection."""
    svc = ContractObligationService()
    return svc.calculate_aggregate_metrics()

# ==================== MilestonePaymentTerm Endpoints ====================
@router.get("/milestonepaymentterms", response_model=List[Dict[str, Any]])
def list_milestonepaymentterms(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MilestonePaymentTerm records with pagination and filtering."""
    svc = MilestonePaymentTermService()
    items = svc.list_milestonepaymentterms(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/milestonepaymentterms/{item_id}", response_model=Dict[str, Any])
def get_milestonepaymentterm_by_id(item_id: int):
    """Retrieve detailed record for MilestonePaymentTerm by ID."""
    svc = MilestonePaymentTermService()
    item = svc.get_milestonepaymentterm_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MilestonePaymentTerm with ID {item_id} not found")
    return item.to_dict()

@router.post("/milestonepaymentterms", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_milestonepaymentterm(payload: MilestonePaymentTermCreateSchema):
    """Create new MilestonePaymentTerm instance in enterprise repository."""
    svc = MilestonePaymentTermService()
    try:
        item = svc.create_milestonepaymentterm(
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

@router.put("/milestonepaymentterms/{item_id}", response_model=Dict[str, Any])
def update_milestonepaymentterm(item_id: int, payload: MilestonePaymentTermUpdateSchema):
    """Update existing MilestonePaymentTerm record fields."""
    svc = MilestonePaymentTermService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_milestonepaymentterm(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MilestonePaymentTerm with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/milestonepaymentterms/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_milestonepaymentterm(item_id: int, hard: bool = Query(False)):
    """Delete MilestonePaymentTerm record (soft-delete by default)."""
    svc = MilestonePaymentTermService()
    ok = svc.delete_milestonepaymentterm(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MilestonePaymentTerm with ID {item_id} not found")
    return None

@router.get("/milestonepaymentterms/analytics/metrics", response_model=Dict[str, Any])
def get_milestonepaymentterm_metrics():
    """Calculate summary statistical KPIs for MilestonePaymentTerm collection."""
    svc = MilestonePaymentTermService()
    return svc.calculate_aggregate_metrics()

# ==================== RenewalNoticeEvent Endpoints ====================
@router.get("/renewalnoticeevents", response_model=List[Dict[str, Any]])
def list_renewalnoticeevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RenewalNoticeEvent records with pagination and filtering."""
    svc = RenewalNoticeEventService()
    items = svc.list_renewalnoticeevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/renewalnoticeevents/{item_id}", response_model=Dict[str, Any])
def get_renewalnoticeevent_by_id(item_id: int):
    """Retrieve detailed record for RenewalNoticeEvent by ID."""
    svc = RenewalNoticeEventService()
    item = svc.get_renewalnoticeevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RenewalNoticeEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/renewalnoticeevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_renewalnoticeevent(payload: RenewalNoticeEventCreateSchema):
    """Create new RenewalNoticeEvent instance in enterprise repository."""
    svc = RenewalNoticeEventService()
    try:
        item = svc.create_renewalnoticeevent(
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

@router.put("/renewalnoticeevents/{item_id}", response_model=Dict[str, Any])
def update_renewalnoticeevent(item_id: int, payload: RenewalNoticeEventUpdateSchema):
    """Update existing RenewalNoticeEvent record fields."""
    svc = RenewalNoticeEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_renewalnoticeevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RenewalNoticeEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/renewalnoticeevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_renewalnoticeevent(item_id: int, hard: bool = Query(False)):
    """Delete RenewalNoticeEvent record (soft-delete by default)."""
    svc = RenewalNoticeEventService()
    ok = svc.delete_renewalnoticeevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RenewalNoticeEvent with ID {item_id} not found")
    return None

@router.get("/renewalnoticeevents/analytics/metrics", response_model=Dict[str, Any])
def get_renewalnoticeevent_metrics():
    """Calculate summary statistical KPIs for RenewalNoticeEvent collection."""
    svc = RenewalNoticeEventService()
    return svc.calculate_aggregate_metrics()

# ==================== ContractRiskAssessment Endpoints ====================
@router.get("/contractriskassessments", response_model=List[Dict[str, Any]])
def list_contractriskassessments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContractRiskAssessment records with pagination and filtering."""
    svc = ContractRiskAssessmentService()
    items = svc.list_contractriskassessments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/contractriskassessments/{item_id}", response_model=Dict[str, Any])
def get_contractriskassessment_by_id(item_id: int):
    """Retrieve detailed record for ContractRiskAssessment by ID."""
    svc = ContractRiskAssessmentService()
    item = svc.get_contractriskassessment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContractRiskAssessment with ID {item_id} not found")
    return item.to_dict()

@router.post("/contractriskassessments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_contractriskassessment(payload: ContractRiskAssessmentCreateSchema):
    """Create new ContractRiskAssessment instance in enterprise repository."""
    svc = ContractRiskAssessmentService()
    try:
        item = svc.create_contractriskassessment(
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

@router.put("/contractriskassessments/{item_id}", response_model=Dict[str, Any])
def update_contractriskassessment(item_id: int, payload: ContractRiskAssessmentUpdateSchema):
    """Update existing ContractRiskAssessment record fields."""
    svc = ContractRiskAssessmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_contractriskassessment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContractRiskAssessment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/contractriskassessments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contractriskassessment(item_id: int, hard: bool = Query(False)):
    """Delete ContractRiskAssessment record (soft-delete by default)."""
    svc = ContractRiskAssessmentService()
    ok = svc.delete_contractriskassessment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContractRiskAssessment with ID {item_id} not found")
    return None

@router.get("/contractriskassessments/analytics/metrics", response_model=Dict[str, Any])
def get_contractriskassessment_metrics():
    """Calculate summary statistical KPIs for ContractRiskAssessment collection."""
    svc = ContractRiskAssessmentService()
    return svc.calculate_aggregate_metrics()

# ==================== LegalRedlineVersion Endpoints ====================
@router.get("/legalredlineversions", response_model=List[Dict[str, Any]])
def list_legalredlineversions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LegalRedlineVersion records with pagination and filtering."""
    svc = LegalRedlineVersionService()
    items = svc.list_legalredlineversions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/legalredlineversions/{item_id}", response_model=Dict[str, Any])
def get_legalredlineversion_by_id(item_id: int):
    """Retrieve detailed record for LegalRedlineVersion by ID."""
    svc = LegalRedlineVersionService()
    item = svc.get_legalredlineversion_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LegalRedlineVersion with ID {item_id} not found")
    return item.to_dict()

@router.post("/legalredlineversions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_legalredlineversion(payload: LegalRedlineVersionCreateSchema):
    """Create new LegalRedlineVersion instance in enterprise repository."""
    svc = LegalRedlineVersionService()
    try:
        item = svc.create_legalredlineversion(
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

@router.put("/legalredlineversions/{item_id}", response_model=Dict[str, Any])
def update_legalredlineversion(item_id: int, payload: LegalRedlineVersionUpdateSchema):
    """Update existing LegalRedlineVersion record fields."""
    svc = LegalRedlineVersionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_legalredlineversion(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LegalRedlineVersion with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/legalredlineversions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legalredlineversion(item_id: int, hard: bool = Query(False)):
    """Delete LegalRedlineVersion record (soft-delete by default)."""
    svc = LegalRedlineVersionService()
    ok = svc.delete_legalredlineversion(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LegalRedlineVersion with ID {item_id} not found")
    return None

@router.get("/legalredlineversions/analytics/metrics", response_model=Dict[str, Any])
def get_legalredlineversion_metrics():
    """Calculate summary statistical KPIs for LegalRedlineVersion collection."""
    svc = LegalRedlineVersionService()
    return svc.calculate_aggregate_metrics()

# ==================== SignatoryApprovalMatrix Endpoints ====================
@router.get("/signatoryapprovalmatrixs", response_model=List[Dict[str, Any]])
def list_signatoryapprovalmatrixs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SignatoryApprovalMatrix records with pagination and filtering."""
    svc = SignatoryApprovalMatrixService()
    items = svc.list_signatoryapprovalmatrixs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/signatoryapprovalmatrixs/{item_id}", response_model=Dict[str, Any])
def get_signatoryapprovalmatrix_by_id(item_id: int):
    """Retrieve detailed record for SignatoryApprovalMatrix by ID."""
    svc = SignatoryApprovalMatrixService()
    item = svc.get_signatoryapprovalmatrix_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SignatoryApprovalMatrix with ID {item_id} not found")
    return item.to_dict()

@router.post("/signatoryapprovalmatrixs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_signatoryapprovalmatrix(payload: SignatoryApprovalMatrixCreateSchema):
    """Create new SignatoryApprovalMatrix instance in enterprise repository."""
    svc = SignatoryApprovalMatrixService()
    try:
        item = svc.create_signatoryapprovalmatrix(
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

@router.put("/signatoryapprovalmatrixs/{item_id}", response_model=Dict[str, Any])
def update_signatoryapprovalmatrix(item_id: int, payload: SignatoryApprovalMatrixUpdateSchema):
    """Update existing SignatoryApprovalMatrix record fields."""
    svc = SignatoryApprovalMatrixService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_signatoryapprovalmatrix(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SignatoryApprovalMatrix with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/signatoryapprovalmatrixs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_signatoryapprovalmatrix(item_id: int, hard: bool = Query(False)):
    """Delete SignatoryApprovalMatrix record (soft-delete by default)."""
    svc = SignatoryApprovalMatrixService()
    ok = svc.delete_signatoryapprovalmatrix(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SignatoryApprovalMatrix with ID {item_id} not found")
    return None

@router.get("/signatoryapprovalmatrixs/analytics/metrics", response_model=Dict[str, Any])
def get_signatoryapprovalmatrix_metrics():
    """Calculate summary statistical KPIs for SignatoryApprovalMatrix collection."""
    svc = SignatoryApprovalMatrixService()
    return svc.calculate_aggregate_metrics()

# ==================== TerminationNotice Endpoints ====================
@router.get("/terminationnotices", response_model=List[Dict[str, Any]])
def list_terminationnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TerminationNotice records with pagination and filtering."""
    svc = TerminationNoticeService()
    items = svc.list_terminationnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/terminationnotices/{item_id}", response_model=Dict[str, Any])
def get_terminationnotice_by_id(item_id: int):
    """Retrieve detailed record for TerminationNotice by ID."""
    svc = TerminationNoticeService()
    item = svc.get_terminationnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TerminationNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/terminationnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_terminationnotice(payload: TerminationNoticeCreateSchema):
    """Create new TerminationNotice instance in enterprise repository."""
    svc = TerminationNoticeService()
    try:
        item = svc.create_terminationnotice(
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

@router.put("/terminationnotices/{item_id}", response_model=Dict[str, Any])
def update_terminationnotice(item_id: int, payload: TerminationNoticeUpdateSchema):
    """Update existing TerminationNotice record fields."""
    svc = TerminationNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_terminationnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TerminationNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/terminationnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_terminationnotice(item_id: int, hard: bool = Query(False)):
    """Delete TerminationNotice record (soft-delete by default)."""
    svc = TerminationNoticeService()
    ok = svc.delete_terminationnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TerminationNotice with ID {item_id} not found")
    return None

@router.get("/terminationnotices/analytics/metrics", response_model=Dict[str, Any])
def get_terminationnotice_metrics():
    """Calculate summary statistical KPIs for TerminationNotice collection."""
    svc = TerminationNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== SLAComplianceCheck Endpoints ====================
@router.get("/slacompliancechecks", response_model=List[Dict[str, Any]])
def list_slacompliancechecks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SLAComplianceCheck records with pagination and filtering."""
    svc = SLAComplianceCheckService()
    items = svc.list_slacompliancechecks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/slacompliancechecks/{item_id}", response_model=Dict[str, Any])
def get_slacompliancecheck_by_id(item_id: int):
    """Retrieve detailed record for SLAComplianceCheck by ID."""
    svc = SLAComplianceCheckService()
    item = svc.get_slacompliancecheck_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SLAComplianceCheck with ID {item_id} not found")
    return item.to_dict()

@router.post("/slacompliancechecks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_slacompliancecheck(payload: SLAComplianceCheckCreateSchema):
    """Create new SLAComplianceCheck instance in enterprise repository."""
    svc = SLAComplianceCheckService()
    try:
        item = svc.create_slacompliancecheck(
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

@router.put("/slacompliancechecks/{item_id}", response_model=Dict[str, Any])
def update_slacompliancecheck(item_id: int, payload: SLAComplianceCheckUpdateSchema):
    """Update existing SLAComplianceCheck record fields."""
    svc = SLAComplianceCheckService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_slacompliancecheck(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SLAComplianceCheck with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/slacompliancechecks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_slacompliancecheck(item_id: int, hard: bool = Query(False)):
    """Delete SLAComplianceCheck record (soft-delete by default)."""
    svc = SLAComplianceCheckService()
    ok = svc.delete_slacompliancecheck(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SLAComplianceCheck with ID {item_id} not found")
    return None

@router.get("/slacompliancechecks/analytics/metrics", response_model=Dict[str, Any])
def get_slacompliancecheck_metrics():
    """Calculate summary statistical KPIs for SLAComplianceCheck collection."""
    svc = SLAComplianceCheckService()
    return svc.calculate_aggregate_metrics()

# ==================== ContractRepositoryIndex Endpoints ====================
@router.get("/contractrepositoryindexs", response_model=List[Dict[str, Any]])
def list_contractrepositoryindexs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContractRepositoryIndex records with pagination and filtering."""
    svc = ContractRepositoryIndexService()
    items = svc.list_contractrepositoryindexs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/contractrepositoryindexs/{item_id}", response_model=Dict[str, Any])
def get_contractrepositoryindex_by_id(item_id: int):
    """Retrieve detailed record for ContractRepositoryIndex by ID."""
    svc = ContractRepositoryIndexService()
    item = svc.get_contractrepositoryindex_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContractRepositoryIndex with ID {item_id} not found")
    return item.to_dict()

@router.post("/contractrepositoryindexs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_contractrepositoryindex(payload: ContractRepositoryIndexCreateSchema):
    """Create new ContractRepositoryIndex instance in enterprise repository."""
    svc = ContractRepositoryIndexService()
    try:
        item = svc.create_contractrepositoryindex(
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

@router.put("/contractrepositoryindexs/{item_id}", response_model=Dict[str, Any])
def update_contractrepositoryindex(item_id: int, payload: ContractRepositoryIndexUpdateSchema):
    """Update existing ContractRepositoryIndex record fields."""
    svc = ContractRepositoryIndexService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_contractrepositoryindex(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContractRepositoryIndex with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/contractrepositoryindexs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contractrepositoryindex(item_id: int, hard: bool = Query(False)):
    """Delete ContractRepositoryIndex record (soft-delete by default)."""
    svc = ContractRepositoryIndexService()
    ok = svc.delete_contractrepositoryindex(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContractRepositoryIndex with ID {item_id} not found")
    return None

@router.get("/contractrepositoryindexs/analytics/metrics", response_model=Dict[str, Any])
def get_contractrepositoryindex_metrics():
    """Calculate summary statistical KPIs for ContractRepositoryIndex collection."""
    svc = ContractRepositoryIndexService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorContractLink Endpoints ====================
@router.get("/vendorcontractlinks", response_model=List[Dict[str, Any]])
def list_vendorcontractlinks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorContractLink records with pagination and filtering."""
    svc = VendorContractLinkService()
    items = svc.list_vendorcontractlinks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorcontractlinks/{item_id}", response_model=Dict[str, Any])
def get_vendorcontractlink_by_id(item_id: int):
    """Retrieve detailed record for VendorContractLink by ID."""
    svc = VendorContractLinkService()
    item = svc.get_vendorcontractlink_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorContractLink with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorcontractlinks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorcontractlink(payload: VendorContractLinkCreateSchema):
    """Create new VendorContractLink instance in enterprise repository."""
    svc = VendorContractLinkService()
    try:
        item = svc.create_vendorcontractlink(
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

@router.put("/vendorcontractlinks/{item_id}", response_model=Dict[str, Any])
def update_vendorcontractlink(item_id: int, payload: VendorContractLinkUpdateSchema):
    """Update existing VendorContractLink record fields."""
    svc = VendorContractLinkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorcontractlink(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorContractLink with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorcontractlinks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorcontractlink(item_id: int, hard: bool = Query(False)):
    """Delete VendorContractLink record (soft-delete by default)."""
    svc = VendorContractLinkService()
    ok = svc.delete_vendorcontractlink(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorContractLink with ID {item_id} not found")
    return None

@router.get("/vendorcontractlinks/analytics/metrics", response_model=Dict[str, Any])
def get_vendorcontractlink_metrics():
    """Calculate summary statistical KPIs for VendorContractLink collection."""
    svc = VendorContractLinkService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerContractLink Endpoints ====================
@router.get("/customercontractlinks", response_model=List[Dict[str, Any]])
def list_customercontractlinks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerContractLink records with pagination and filtering."""
    svc = CustomerContractLinkService()
    items = svc.list_customercontractlinks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customercontractlinks/{item_id}", response_model=Dict[str, Any])
def get_customercontractlink_by_id(item_id: int):
    """Retrieve detailed record for CustomerContractLink by ID."""
    svc = CustomerContractLinkService()
    item = svc.get_customercontractlink_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerContractLink with ID {item_id} not found")
    return item.to_dict()

@router.post("/customercontractlinks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customercontractlink(payload: CustomerContractLinkCreateSchema):
    """Create new CustomerContractLink instance in enterprise repository."""
    svc = CustomerContractLinkService()
    try:
        item = svc.create_customercontractlink(
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

@router.put("/customercontractlinks/{item_id}", response_model=Dict[str, Any])
def update_customercontractlink(item_id: int, payload: CustomerContractLinkUpdateSchema):
    """Update existing CustomerContractLink record fields."""
    svc = CustomerContractLinkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customercontractlink(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerContractLink with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customercontractlinks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customercontractlink(item_id: int, hard: bool = Query(False)):
    """Delete CustomerContractLink record (soft-delete by default)."""
    svc = CustomerContractLinkService()
    ok = svc.delete_customercontractlink(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerContractLink with ID {item_id} not found")
    return None

@router.get("/customercontractlinks/analytics/metrics", response_model=Dict[str, Any])
def get_customercontractlink_metrics():
    """Calculate summary statistical KPIs for CustomerContractLink collection."""
    svc = CustomerContractLinkService()
    return svc.calculate_aggregate_metrics()

