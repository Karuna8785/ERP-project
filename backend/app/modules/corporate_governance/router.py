"""
Board Governance & Shareholder Proxy Resolutions - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    BoardResolutionVoteService,
    ShareholderProxyFilingService,
    CommitteeMeetingCharterService,
    DirectorFiduciaryDutyService,
    AnnualGeneralMeetingNoticeService,
    ExecutiveSuccessionMatrixService,
    StatutoryFilingDisclosureService,
    ConflictOfInterestDeclarationService,
    ShareholderProposalEntryService,
    MinutesOfMeetingDocService,
    BoardMemberEvaluationService,
    DelegationOfAuthorityRuleService,
    WhistleblowerTriageCaseService,
    FiduciaryRiskAssessmentService,
    InvestorRelationsReleaseService,
    CorporateSealRegisterService,
)
from .schemas import (
    BoardResolutionVoteCreateSchema, BoardResolutionVoteUpdateSchema, BoardResolutionVoteResponseSchema,
    ShareholderProxyFilingCreateSchema, ShareholderProxyFilingUpdateSchema, ShareholderProxyFilingResponseSchema,
    CommitteeMeetingCharterCreateSchema, CommitteeMeetingCharterUpdateSchema, CommitteeMeetingCharterResponseSchema,
    DirectorFiduciaryDutyCreateSchema, DirectorFiduciaryDutyUpdateSchema, DirectorFiduciaryDutyResponseSchema,
    AnnualGeneralMeetingNoticeCreateSchema, AnnualGeneralMeetingNoticeUpdateSchema, AnnualGeneralMeetingNoticeResponseSchema,
    ExecutiveSuccessionMatrixCreateSchema, ExecutiveSuccessionMatrixUpdateSchema, ExecutiveSuccessionMatrixResponseSchema,
    StatutoryFilingDisclosureCreateSchema, StatutoryFilingDisclosureUpdateSchema, StatutoryFilingDisclosureResponseSchema,
    ConflictOfInterestDeclarationCreateSchema, ConflictOfInterestDeclarationUpdateSchema, ConflictOfInterestDeclarationResponseSchema,
    ShareholderProposalEntryCreateSchema, ShareholderProposalEntryUpdateSchema, ShareholderProposalEntryResponseSchema,
    MinutesOfMeetingDocCreateSchema, MinutesOfMeetingDocUpdateSchema, MinutesOfMeetingDocResponseSchema,
    BoardMemberEvaluationCreateSchema, BoardMemberEvaluationUpdateSchema, BoardMemberEvaluationResponseSchema,
    DelegationOfAuthorityRuleCreateSchema, DelegationOfAuthorityRuleUpdateSchema, DelegationOfAuthorityRuleResponseSchema,
    WhistleblowerTriageCaseCreateSchema, WhistleblowerTriageCaseUpdateSchema, WhistleblowerTriageCaseResponseSchema,
    FiduciaryRiskAssessmentCreateSchema, FiduciaryRiskAssessmentUpdateSchema, FiduciaryRiskAssessmentResponseSchema,
    InvestorRelationsReleaseCreateSchema, InvestorRelationsReleaseUpdateSchema, InvestorRelationsReleaseResponseSchema,
    CorporateSealRegisterCreateSchema, CorporateSealRegisterUpdateSchema, CorporateSealRegisterResponseSchema,
)

router = APIRouter(prefix="/corporate_governance", tags=["Board Governance & Shareholder Proxy Resolutions"])

# ==================== BoardResolutionVote Endpoints ====================
@router.get("/boardresolutionvotes", response_model=List[Dict[str, Any]])
def list_boardresolutionvotes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BoardResolutionVote records with pagination and filtering."""
    svc = BoardResolutionVoteService()
    items = svc.list_boardresolutionvotes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/boardresolutionvotes/{item_id}", response_model=Dict[str, Any])
def get_boardresolutionvote_by_id(item_id: int):
    """Retrieve detailed record for BoardResolutionVote by ID."""
    svc = BoardResolutionVoteService()
    item = svc.get_boardresolutionvote_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BoardResolutionVote with ID {item_id} not found")
    return item.to_dict()

@router.post("/boardresolutionvotes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_boardresolutionvote(payload: BoardResolutionVoteCreateSchema):
    """Create new BoardResolutionVote instance in enterprise repository."""
    svc = BoardResolutionVoteService()
    try:
        item = svc.create_boardresolutionvote(
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

@router.put("/boardresolutionvotes/{item_id}", response_model=Dict[str, Any])
def update_boardresolutionvote(item_id: int, payload: BoardResolutionVoteUpdateSchema):
    """Update existing BoardResolutionVote record fields."""
    svc = BoardResolutionVoteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_boardresolutionvote(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BoardResolutionVote with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/boardresolutionvotes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_boardresolutionvote(item_id: int, hard: bool = Query(False)):
    """Delete BoardResolutionVote record (soft-delete by default)."""
    svc = BoardResolutionVoteService()
    ok = svc.delete_boardresolutionvote(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BoardResolutionVote with ID {item_id} not found")
    return None

@router.get("/boardresolutionvotes/analytics/metrics", response_model=Dict[str, Any])
def get_boardresolutionvote_metrics():
    """Calculate summary statistical KPIs for BoardResolutionVote collection."""
    svc = BoardResolutionVoteService()
    return svc.calculate_aggregate_metrics()

# ==================== ShareholderProxyFiling Endpoints ====================
@router.get("/shareholderproxyfilings", response_model=List[Dict[str, Any]])
def list_shareholderproxyfilings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShareholderProxyFiling records with pagination and filtering."""
    svc = ShareholderProxyFilingService()
    items = svc.list_shareholderproxyfilings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shareholderproxyfilings/{item_id}", response_model=Dict[str, Any])
def get_shareholderproxyfiling_by_id(item_id: int):
    """Retrieve detailed record for ShareholderProxyFiling by ID."""
    svc = ShareholderProxyFilingService()
    item = svc.get_shareholderproxyfiling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShareholderProxyFiling with ID {item_id} not found")
    return item.to_dict()

@router.post("/shareholderproxyfilings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shareholderproxyfiling(payload: ShareholderProxyFilingCreateSchema):
    """Create new ShareholderProxyFiling instance in enterprise repository."""
    svc = ShareholderProxyFilingService()
    try:
        item = svc.create_shareholderproxyfiling(
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

@router.put("/shareholderproxyfilings/{item_id}", response_model=Dict[str, Any])
def update_shareholderproxyfiling(item_id: int, payload: ShareholderProxyFilingUpdateSchema):
    """Update existing ShareholderProxyFiling record fields."""
    svc = ShareholderProxyFilingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shareholderproxyfiling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShareholderProxyFiling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shareholderproxyfilings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shareholderproxyfiling(item_id: int, hard: bool = Query(False)):
    """Delete ShareholderProxyFiling record (soft-delete by default)."""
    svc = ShareholderProxyFilingService()
    ok = svc.delete_shareholderproxyfiling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShareholderProxyFiling with ID {item_id} not found")
    return None

@router.get("/shareholderproxyfilings/analytics/metrics", response_model=Dict[str, Any])
def get_shareholderproxyfiling_metrics():
    """Calculate summary statistical KPIs for ShareholderProxyFiling collection."""
    svc = ShareholderProxyFilingService()
    return svc.calculate_aggregate_metrics()

# ==================== CommitteeMeetingCharter Endpoints ====================
@router.get("/committeemeetingcharters", response_model=List[Dict[str, Any]])
def list_committeemeetingcharters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CommitteeMeetingCharter records with pagination and filtering."""
    svc = CommitteeMeetingCharterService()
    items = svc.list_committeemeetingcharters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/committeemeetingcharters/{item_id}", response_model=Dict[str, Any])
def get_committeemeetingcharter_by_id(item_id: int):
    """Retrieve detailed record for CommitteeMeetingCharter by ID."""
    svc = CommitteeMeetingCharterService()
    item = svc.get_committeemeetingcharter_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CommitteeMeetingCharter with ID {item_id} not found")
    return item.to_dict()

@router.post("/committeemeetingcharters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_committeemeetingcharter(payload: CommitteeMeetingCharterCreateSchema):
    """Create new CommitteeMeetingCharter instance in enterprise repository."""
    svc = CommitteeMeetingCharterService()
    try:
        item = svc.create_committeemeetingcharter(
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

@router.put("/committeemeetingcharters/{item_id}", response_model=Dict[str, Any])
def update_committeemeetingcharter(item_id: int, payload: CommitteeMeetingCharterUpdateSchema):
    """Update existing CommitteeMeetingCharter record fields."""
    svc = CommitteeMeetingCharterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_committeemeetingcharter(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CommitteeMeetingCharter with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/committeemeetingcharters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_committeemeetingcharter(item_id: int, hard: bool = Query(False)):
    """Delete CommitteeMeetingCharter record (soft-delete by default)."""
    svc = CommitteeMeetingCharterService()
    ok = svc.delete_committeemeetingcharter(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CommitteeMeetingCharter with ID {item_id} not found")
    return None

@router.get("/committeemeetingcharters/analytics/metrics", response_model=Dict[str, Any])
def get_committeemeetingcharter_metrics():
    """Calculate summary statistical KPIs for CommitteeMeetingCharter collection."""
    svc = CommitteeMeetingCharterService()
    return svc.calculate_aggregate_metrics()

# ==================== DirectorFiduciaryDuty Endpoints ====================
@router.get("/directorfiduciarydutys", response_model=List[Dict[str, Any]])
def list_directorfiduciarydutys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DirectorFiduciaryDuty records with pagination and filtering."""
    svc = DirectorFiduciaryDutyService()
    items = svc.list_directorfiduciarydutys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/directorfiduciarydutys/{item_id}", response_model=Dict[str, Any])
def get_directorfiduciaryduty_by_id(item_id: int):
    """Retrieve detailed record for DirectorFiduciaryDuty by ID."""
    svc = DirectorFiduciaryDutyService()
    item = svc.get_directorfiduciaryduty_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DirectorFiduciaryDuty with ID {item_id} not found")
    return item.to_dict()

@router.post("/directorfiduciarydutys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_directorfiduciaryduty(payload: DirectorFiduciaryDutyCreateSchema):
    """Create new DirectorFiduciaryDuty instance in enterprise repository."""
    svc = DirectorFiduciaryDutyService()
    try:
        item = svc.create_directorfiduciaryduty(
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

@router.put("/directorfiduciarydutys/{item_id}", response_model=Dict[str, Any])
def update_directorfiduciaryduty(item_id: int, payload: DirectorFiduciaryDutyUpdateSchema):
    """Update existing DirectorFiduciaryDuty record fields."""
    svc = DirectorFiduciaryDutyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_directorfiduciaryduty(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DirectorFiduciaryDuty with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/directorfiduciarydutys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_directorfiduciaryduty(item_id: int, hard: bool = Query(False)):
    """Delete DirectorFiduciaryDuty record (soft-delete by default)."""
    svc = DirectorFiduciaryDutyService()
    ok = svc.delete_directorfiduciaryduty(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DirectorFiduciaryDuty with ID {item_id} not found")
    return None

@router.get("/directorfiduciarydutys/analytics/metrics", response_model=Dict[str, Any])
def get_directorfiduciaryduty_metrics():
    """Calculate summary statistical KPIs for DirectorFiduciaryDuty collection."""
    svc = DirectorFiduciaryDutyService()
    return svc.calculate_aggregate_metrics()

# ==================== AnnualGeneralMeetingNotice Endpoints ====================
@router.get("/annualgeneralmeetingnotices", response_model=List[Dict[str, Any]])
def list_annualgeneralmeetingnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AnnualGeneralMeetingNotice records with pagination and filtering."""
    svc = AnnualGeneralMeetingNoticeService()
    items = svc.list_annualgeneralmeetingnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/annualgeneralmeetingnotices/{item_id}", response_model=Dict[str, Any])
def get_annualgeneralmeetingnotice_by_id(item_id: int):
    """Retrieve detailed record for AnnualGeneralMeetingNotice by ID."""
    svc = AnnualGeneralMeetingNoticeService()
    item = svc.get_annualgeneralmeetingnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AnnualGeneralMeetingNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/annualgeneralmeetingnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_annualgeneralmeetingnotice(payload: AnnualGeneralMeetingNoticeCreateSchema):
    """Create new AnnualGeneralMeetingNotice instance in enterprise repository."""
    svc = AnnualGeneralMeetingNoticeService()
    try:
        item = svc.create_annualgeneralmeetingnotice(
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

@router.put("/annualgeneralmeetingnotices/{item_id}", response_model=Dict[str, Any])
def update_annualgeneralmeetingnotice(item_id: int, payload: AnnualGeneralMeetingNoticeUpdateSchema):
    """Update existing AnnualGeneralMeetingNotice record fields."""
    svc = AnnualGeneralMeetingNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_annualgeneralmeetingnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AnnualGeneralMeetingNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/annualgeneralmeetingnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_annualgeneralmeetingnotice(item_id: int, hard: bool = Query(False)):
    """Delete AnnualGeneralMeetingNotice record (soft-delete by default)."""
    svc = AnnualGeneralMeetingNoticeService()
    ok = svc.delete_annualgeneralmeetingnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AnnualGeneralMeetingNotice with ID {item_id} not found")
    return None

@router.get("/annualgeneralmeetingnotices/analytics/metrics", response_model=Dict[str, Any])
def get_annualgeneralmeetingnotice_metrics():
    """Calculate summary statistical KPIs for AnnualGeneralMeetingNotice collection."""
    svc = AnnualGeneralMeetingNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutiveSuccessionMatrix Endpoints ====================
@router.get("/executivesuccessionmatrixs", response_model=List[Dict[str, Any]])
def list_executivesuccessionmatrixs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutiveSuccessionMatrix records with pagination and filtering."""
    svc = ExecutiveSuccessionMatrixService()
    items = svc.list_executivesuccessionmatrixs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executivesuccessionmatrixs/{item_id}", response_model=Dict[str, Any])
def get_executivesuccessionmatrix_by_id(item_id: int):
    """Retrieve detailed record for ExecutiveSuccessionMatrix by ID."""
    svc = ExecutiveSuccessionMatrixService()
    item = svc.get_executivesuccessionmatrix_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutiveSuccessionMatrix with ID {item_id} not found")
    return item.to_dict()

@router.post("/executivesuccessionmatrixs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executivesuccessionmatrix(payload: ExecutiveSuccessionMatrixCreateSchema):
    """Create new ExecutiveSuccessionMatrix instance in enterprise repository."""
    svc = ExecutiveSuccessionMatrixService()
    try:
        item = svc.create_executivesuccessionmatrix(
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

@router.put("/executivesuccessionmatrixs/{item_id}", response_model=Dict[str, Any])
def update_executivesuccessionmatrix(item_id: int, payload: ExecutiveSuccessionMatrixUpdateSchema):
    """Update existing ExecutiveSuccessionMatrix record fields."""
    svc = ExecutiveSuccessionMatrixService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executivesuccessionmatrix(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutiveSuccessionMatrix with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executivesuccessionmatrixs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executivesuccessionmatrix(item_id: int, hard: bool = Query(False)):
    """Delete ExecutiveSuccessionMatrix record (soft-delete by default)."""
    svc = ExecutiveSuccessionMatrixService()
    ok = svc.delete_executivesuccessionmatrix(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutiveSuccessionMatrix with ID {item_id} not found")
    return None

@router.get("/executivesuccessionmatrixs/analytics/metrics", response_model=Dict[str, Any])
def get_executivesuccessionmatrix_metrics():
    """Calculate summary statistical KPIs for ExecutiveSuccessionMatrix collection."""
    svc = ExecutiveSuccessionMatrixService()
    return svc.calculate_aggregate_metrics()

# ==================== StatutoryFilingDisclosure Endpoints ====================
@router.get("/statutoryfilingdisclosures", response_model=List[Dict[str, Any]])
def list_statutoryfilingdisclosures(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StatutoryFilingDisclosure records with pagination and filtering."""
    svc = StatutoryFilingDisclosureService()
    items = svc.list_statutoryfilingdisclosures(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/statutoryfilingdisclosures/{item_id}", response_model=Dict[str, Any])
def get_statutoryfilingdisclosure_by_id(item_id: int):
    """Retrieve detailed record for StatutoryFilingDisclosure by ID."""
    svc = StatutoryFilingDisclosureService()
    item = svc.get_statutoryfilingdisclosure_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StatutoryFilingDisclosure with ID {item_id} not found")
    return item.to_dict()

@router.post("/statutoryfilingdisclosures", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_statutoryfilingdisclosure(payload: StatutoryFilingDisclosureCreateSchema):
    """Create new StatutoryFilingDisclosure instance in enterprise repository."""
    svc = StatutoryFilingDisclosureService()
    try:
        item = svc.create_statutoryfilingdisclosure(
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

@router.put("/statutoryfilingdisclosures/{item_id}", response_model=Dict[str, Any])
def update_statutoryfilingdisclosure(item_id: int, payload: StatutoryFilingDisclosureUpdateSchema):
    """Update existing StatutoryFilingDisclosure record fields."""
    svc = StatutoryFilingDisclosureService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_statutoryfilingdisclosure(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StatutoryFilingDisclosure with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/statutoryfilingdisclosures/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_statutoryfilingdisclosure(item_id: int, hard: bool = Query(False)):
    """Delete StatutoryFilingDisclosure record (soft-delete by default)."""
    svc = StatutoryFilingDisclosureService()
    ok = svc.delete_statutoryfilingdisclosure(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StatutoryFilingDisclosure with ID {item_id} not found")
    return None

@router.get("/statutoryfilingdisclosures/analytics/metrics", response_model=Dict[str, Any])
def get_statutoryfilingdisclosure_metrics():
    """Calculate summary statistical KPIs for StatutoryFilingDisclosure collection."""
    svc = StatutoryFilingDisclosureService()
    return svc.calculate_aggregate_metrics()

# ==================== ConflictOfInterestDeclaration Endpoints ====================
@router.get("/conflictofinterestdeclarations", response_model=List[Dict[str, Any]])
def list_conflictofinterestdeclarations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ConflictOfInterestDeclaration records with pagination and filtering."""
    svc = ConflictOfInterestDeclarationService()
    items = svc.list_conflictofinterestdeclarations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/conflictofinterestdeclarations/{item_id}", response_model=Dict[str, Any])
def get_conflictofinterestdeclaration_by_id(item_id: int):
    """Retrieve detailed record for ConflictOfInterestDeclaration by ID."""
    svc = ConflictOfInterestDeclarationService()
    item = svc.get_conflictofinterestdeclaration_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ConflictOfInterestDeclaration with ID {item_id} not found")
    return item.to_dict()

@router.post("/conflictofinterestdeclarations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_conflictofinterestdeclaration(payload: ConflictOfInterestDeclarationCreateSchema):
    """Create new ConflictOfInterestDeclaration instance in enterprise repository."""
    svc = ConflictOfInterestDeclarationService()
    try:
        item = svc.create_conflictofinterestdeclaration(
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

@router.put("/conflictofinterestdeclarations/{item_id}", response_model=Dict[str, Any])
def update_conflictofinterestdeclaration(item_id: int, payload: ConflictOfInterestDeclarationUpdateSchema):
    """Update existing ConflictOfInterestDeclaration record fields."""
    svc = ConflictOfInterestDeclarationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_conflictofinterestdeclaration(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ConflictOfInterestDeclaration with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/conflictofinterestdeclarations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_conflictofinterestdeclaration(item_id: int, hard: bool = Query(False)):
    """Delete ConflictOfInterestDeclaration record (soft-delete by default)."""
    svc = ConflictOfInterestDeclarationService()
    ok = svc.delete_conflictofinterestdeclaration(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ConflictOfInterestDeclaration with ID {item_id} not found")
    return None

@router.get("/conflictofinterestdeclarations/analytics/metrics", response_model=Dict[str, Any])
def get_conflictofinterestdeclaration_metrics():
    """Calculate summary statistical KPIs for ConflictOfInterestDeclaration collection."""
    svc = ConflictOfInterestDeclarationService()
    return svc.calculate_aggregate_metrics()

# ==================== ShareholderProposalEntry Endpoints ====================
@router.get("/shareholderproposalentrys", response_model=List[Dict[str, Any]])
def list_shareholderproposalentrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShareholderProposalEntry records with pagination and filtering."""
    svc = ShareholderProposalEntryService()
    items = svc.list_shareholderproposalentrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shareholderproposalentrys/{item_id}", response_model=Dict[str, Any])
def get_shareholderproposalentry_by_id(item_id: int):
    """Retrieve detailed record for ShareholderProposalEntry by ID."""
    svc = ShareholderProposalEntryService()
    item = svc.get_shareholderproposalentry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShareholderProposalEntry with ID {item_id} not found")
    return item.to_dict()

@router.post("/shareholderproposalentrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shareholderproposalentry(payload: ShareholderProposalEntryCreateSchema):
    """Create new ShareholderProposalEntry instance in enterprise repository."""
    svc = ShareholderProposalEntryService()
    try:
        item = svc.create_shareholderproposalentry(
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

@router.put("/shareholderproposalentrys/{item_id}", response_model=Dict[str, Any])
def update_shareholderproposalentry(item_id: int, payload: ShareholderProposalEntryUpdateSchema):
    """Update existing ShareholderProposalEntry record fields."""
    svc = ShareholderProposalEntryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shareholderproposalentry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShareholderProposalEntry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shareholderproposalentrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shareholderproposalentry(item_id: int, hard: bool = Query(False)):
    """Delete ShareholderProposalEntry record (soft-delete by default)."""
    svc = ShareholderProposalEntryService()
    ok = svc.delete_shareholderproposalentry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShareholderProposalEntry with ID {item_id} not found")
    return None

@router.get("/shareholderproposalentrys/analytics/metrics", response_model=Dict[str, Any])
def get_shareholderproposalentry_metrics():
    """Calculate summary statistical KPIs for ShareholderProposalEntry collection."""
    svc = ShareholderProposalEntryService()
    return svc.calculate_aggregate_metrics()

# ==================== MinutesOfMeetingDoc Endpoints ====================
@router.get("/minutesofmeetingdocs", response_model=List[Dict[str, Any]])
def list_minutesofmeetingdocs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MinutesOfMeetingDoc records with pagination and filtering."""
    svc = MinutesOfMeetingDocService()
    items = svc.list_minutesofmeetingdocs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/minutesofmeetingdocs/{item_id}", response_model=Dict[str, Any])
def get_minutesofmeetingdoc_by_id(item_id: int):
    """Retrieve detailed record for MinutesOfMeetingDoc by ID."""
    svc = MinutesOfMeetingDocService()
    item = svc.get_minutesofmeetingdoc_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MinutesOfMeetingDoc with ID {item_id} not found")
    return item.to_dict()

@router.post("/minutesofmeetingdocs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_minutesofmeetingdoc(payload: MinutesOfMeetingDocCreateSchema):
    """Create new MinutesOfMeetingDoc instance in enterprise repository."""
    svc = MinutesOfMeetingDocService()
    try:
        item = svc.create_minutesofmeetingdoc(
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

@router.put("/minutesofmeetingdocs/{item_id}", response_model=Dict[str, Any])
def update_minutesofmeetingdoc(item_id: int, payload: MinutesOfMeetingDocUpdateSchema):
    """Update existing MinutesOfMeetingDoc record fields."""
    svc = MinutesOfMeetingDocService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_minutesofmeetingdoc(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MinutesOfMeetingDoc with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/minutesofmeetingdocs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_minutesofmeetingdoc(item_id: int, hard: bool = Query(False)):
    """Delete MinutesOfMeetingDoc record (soft-delete by default)."""
    svc = MinutesOfMeetingDocService()
    ok = svc.delete_minutesofmeetingdoc(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MinutesOfMeetingDoc with ID {item_id} not found")
    return None

@router.get("/minutesofmeetingdocs/analytics/metrics", response_model=Dict[str, Any])
def get_minutesofmeetingdoc_metrics():
    """Calculate summary statistical KPIs for MinutesOfMeetingDoc collection."""
    svc = MinutesOfMeetingDocService()
    return svc.calculate_aggregate_metrics()

# ==================== BoardMemberEvaluation Endpoints ====================
@router.get("/boardmemberevaluations", response_model=List[Dict[str, Any]])
def list_boardmemberevaluations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BoardMemberEvaluation records with pagination and filtering."""
    svc = BoardMemberEvaluationService()
    items = svc.list_boardmemberevaluations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/boardmemberevaluations/{item_id}", response_model=Dict[str, Any])
def get_boardmemberevaluation_by_id(item_id: int):
    """Retrieve detailed record for BoardMemberEvaluation by ID."""
    svc = BoardMemberEvaluationService()
    item = svc.get_boardmemberevaluation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BoardMemberEvaluation with ID {item_id} not found")
    return item.to_dict()

@router.post("/boardmemberevaluations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_boardmemberevaluation(payload: BoardMemberEvaluationCreateSchema):
    """Create new BoardMemberEvaluation instance in enterprise repository."""
    svc = BoardMemberEvaluationService()
    try:
        item = svc.create_boardmemberevaluation(
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

@router.put("/boardmemberevaluations/{item_id}", response_model=Dict[str, Any])
def update_boardmemberevaluation(item_id: int, payload: BoardMemberEvaluationUpdateSchema):
    """Update existing BoardMemberEvaluation record fields."""
    svc = BoardMemberEvaluationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_boardmemberevaluation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BoardMemberEvaluation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/boardmemberevaluations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_boardmemberevaluation(item_id: int, hard: bool = Query(False)):
    """Delete BoardMemberEvaluation record (soft-delete by default)."""
    svc = BoardMemberEvaluationService()
    ok = svc.delete_boardmemberevaluation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BoardMemberEvaluation with ID {item_id} not found")
    return None

@router.get("/boardmemberevaluations/analytics/metrics", response_model=Dict[str, Any])
def get_boardmemberevaluation_metrics():
    """Calculate summary statistical KPIs for BoardMemberEvaluation collection."""
    svc = BoardMemberEvaluationService()
    return svc.calculate_aggregate_metrics()

# ==================== DelegationOfAuthorityRule Endpoints ====================
@router.get("/delegationofauthorityrules", response_model=List[Dict[str, Any]])
def list_delegationofauthorityrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DelegationOfAuthorityRule records with pagination and filtering."""
    svc = DelegationOfAuthorityRuleService()
    items = svc.list_delegationofauthorityrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/delegationofauthorityrules/{item_id}", response_model=Dict[str, Any])
def get_delegationofauthorityrule_by_id(item_id: int):
    """Retrieve detailed record for DelegationOfAuthorityRule by ID."""
    svc = DelegationOfAuthorityRuleService()
    item = svc.get_delegationofauthorityrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DelegationOfAuthorityRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/delegationofauthorityrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_delegationofauthorityrule(payload: DelegationOfAuthorityRuleCreateSchema):
    """Create new DelegationOfAuthorityRule instance in enterprise repository."""
    svc = DelegationOfAuthorityRuleService()
    try:
        item = svc.create_delegationofauthorityrule(
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

@router.put("/delegationofauthorityrules/{item_id}", response_model=Dict[str, Any])
def update_delegationofauthorityrule(item_id: int, payload: DelegationOfAuthorityRuleUpdateSchema):
    """Update existing DelegationOfAuthorityRule record fields."""
    svc = DelegationOfAuthorityRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_delegationofauthorityrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DelegationOfAuthorityRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/delegationofauthorityrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_delegationofauthorityrule(item_id: int, hard: bool = Query(False)):
    """Delete DelegationOfAuthorityRule record (soft-delete by default)."""
    svc = DelegationOfAuthorityRuleService()
    ok = svc.delete_delegationofauthorityrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DelegationOfAuthorityRule with ID {item_id} not found")
    return None

@router.get("/delegationofauthorityrules/analytics/metrics", response_model=Dict[str, Any])
def get_delegationofauthorityrule_metrics():
    """Calculate summary statistical KPIs for DelegationOfAuthorityRule collection."""
    svc = DelegationOfAuthorityRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== WhistleblowerTriageCase Endpoints ====================
@router.get("/whistleblowertriagecases", response_model=List[Dict[str, Any]])
def list_whistleblowertriagecases(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WhistleblowerTriageCase records with pagination and filtering."""
    svc = WhistleblowerTriageCaseService()
    items = svc.list_whistleblowertriagecases(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/whistleblowertriagecases/{item_id}", response_model=Dict[str, Any])
def get_whistleblowertriagecase_by_id(item_id: int):
    """Retrieve detailed record for WhistleblowerTriageCase by ID."""
    svc = WhistleblowerTriageCaseService()
    item = svc.get_whistleblowertriagecase_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WhistleblowerTriageCase with ID {item_id} not found")
    return item.to_dict()

@router.post("/whistleblowertriagecases", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_whistleblowertriagecase(payload: WhistleblowerTriageCaseCreateSchema):
    """Create new WhistleblowerTriageCase instance in enterprise repository."""
    svc = WhistleblowerTriageCaseService()
    try:
        item = svc.create_whistleblowertriagecase(
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

@router.put("/whistleblowertriagecases/{item_id}", response_model=Dict[str, Any])
def update_whistleblowertriagecase(item_id: int, payload: WhistleblowerTriageCaseUpdateSchema):
    """Update existing WhistleblowerTriageCase record fields."""
    svc = WhistleblowerTriageCaseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_whistleblowertriagecase(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WhistleblowerTriageCase with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/whistleblowertriagecases/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_whistleblowertriagecase(item_id: int, hard: bool = Query(False)):
    """Delete WhistleblowerTriageCase record (soft-delete by default)."""
    svc = WhistleblowerTriageCaseService()
    ok = svc.delete_whistleblowertriagecase(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WhistleblowerTriageCase with ID {item_id} not found")
    return None

@router.get("/whistleblowertriagecases/analytics/metrics", response_model=Dict[str, Any])
def get_whistleblowertriagecase_metrics():
    """Calculate summary statistical KPIs for WhistleblowerTriageCase collection."""
    svc = WhistleblowerTriageCaseService()
    return svc.calculate_aggregate_metrics()

# ==================== FiduciaryRiskAssessment Endpoints ====================
@router.get("/fiduciaryriskassessments", response_model=List[Dict[str, Any]])
def list_fiduciaryriskassessments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FiduciaryRiskAssessment records with pagination and filtering."""
    svc = FiduciaryRiskAssessmentService()
    items = svc.list_fiduciaryriskassessments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fiduciaryriskassessments/{item_id}", response_model=Dict[str, Any])
def get_fiduciaryriskassessment_by_id(item_id: int):
    """Retrieve detailed record for FiduciaryRiskAssessment by ID."""
    svc = FiduciaryRiskAssessmentService()
    item = svc.get_fiduciaryriskassessment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FiduciaryRiskAssessment with ID {item_id} not found")
    return item.to_dict()

@router.post("/fiduciaryriskassessments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fiduciaryriskassessment(payload: FiduciaryRiskAssessmentCreateSchema):
    """Create new FiduciaryRiskAssessment instance in enterprise repository."""
    svc = FiduciaryRiskAssessmentService()
    try:
        item = svc.create_fiduciaryriskassessment(
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

@router.put("/fiduciaryriskassessments/{item_id}", response_model=Dict[str, Any])
def update_fiduciaryriskassessment(item_id: int, payload: FiduciaryRiskAssessmentUpdateSchema):
    """Update existing FiduciaryRiskAssessment record fields."""
    svc = FiduciaryRiskAssessmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fiduciaryriskassessment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FiduciaryRiskAssessment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fiduciaryriskassessments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fiduciaryriskassessment(item_id: int, hard: bool = Query(False)):
    """Delete FiduciaryRiskAssessment record (soft-delete by default)."""
    svc = FiduciaryRiskAssessmentService()
    ok = svc.delete_fiduciaryriskassessment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FiduciaryRiskAssessment with ID {item_id} not found")
    return None

@router.get("/fiduciaryriskassessments/analytics/metrics", response_model=Dict[str, Any])
def get_fiduciaryriskassessment_metrics():
    """Calculate summary statistical KPIs for FiduciaryRiskAssessment collection."""
    svc = FiduciaryRiskAssessmentService()
    return svc.calculate_aggregate_metrics()

# ==================== InvestorRelationsRelease Endpoints ====================
@router.get("/investorrelationsreleases", response_model=List[Dict[str, Any]])
def list_investorrelationsreleases(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InvestorRelationsRelease records with pagination and filtering."""
    svc = InvestorRelationsReleaseService()
    items = svc.list_investorrelationsreleases(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/investorrelationsreleases/{item_id}", response_model=Dict[str, Any])
def get_investorrelationsrelease_by_id(item_id: int):
    """Retrieve detailed record for InvestorRelationsRelease by ID."""
    svc = InvestorRelationsReleaseService()
    item = svc.get_investorrelationsrelease_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InvestorRelationsRelease with ID {item_id} not found")
    return item.to_dict()

@router.post("/investorrelationsreleases", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_investorrelationsrelease(payload: InvestorRelationsReleaseCreateSchema):
    """Create new InvestorRelationsRelease instance in enterprise repository."""
    svc = InvestorRelationsReleaseService()
    try:
        item = svc.create_investorrelationsrelease(
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

@router.put("/investorrelationsreleases/{item_id}", response_model=Dict[str, Any])
def update_investorrelationsrelease(item_id: int, payload: InvestorRelationsReleaseUpdateSchema):
    """Update existing InvestorRelationsRelease record fields."""
    svc = InvestorRelationsReleaseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_investorrelationsrelease(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InvestorRelationsRelease with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/investorrelationsreleases/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_investorrelationsrelease(item_id: int, hard: bool = Query(False)):
    """Delete InvestorRelationsRelease record (soft-delete by default)."""
    svc = InvestorRelationsReleaseService()
    ok = svc.delete_investorrelationsrelease(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InvestorRelationsRelease with ID {item_id} not found")
    return None

@router.get("/investorrelationsreleases/analytics/metrics", response_model=Dict[str, Any])
def get_investorrelationsrelease_metrics():
    """Calculate summary statistical KPIs for InvestorRelationsRelease collection."""
    svc = InvestorRelationsReleaseService()
    return svc.calculate_aggregate_metrics()

# ==================== CorporateSealRegister Endpoints ====================
@router.get("/corporatesealregisters", response_model=List[Dict[str, Any]])
def list_corporatesealregisters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CorporateSealRegister records with pagination and filtering."""
    svc = CorporateSealRegisterService()
    items = svc.list_corporatesealregisters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/corporatesealregisters/{item_id}", response_model=Dict[str, Any])
def get_corporatesealregister_by_id(item_id: int):
    """Retrieve detailed record for CorporateSealRegister by ID."""
    svc = CorporateSealRegisterService()
    item = svc.get_corporatesealregister_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CorporateSealRegister with ID {item_id} not found")
    return item.to_dict()

@router.post("/corporatesealregisters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_corporatesealregister(payload: CorporateSealRegisterCreateSchema):
    """Create new CorporateSealRegister instance in enterprise repository."""
    svc = CorporateSealRegisterService()
    try:
        item = svc.create_corporatesealregister(
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

@router.put("/corporatesealregisters/{item_id}", response_model=Dict[str, Any])
def update_corporatesealregister(item_id: int, payload: CorporateSealRegisterUpdateSchema):
    """Update existing CorporateSealRegister record fields."""
    svc = CorporateSealRegisterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_corporatesealregister(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CorporateSealRegister with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/corporatesealregisters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_corporatesealregister(item_id: int, hard: bool = Query(False)):
    """Delete CorporateSealRegister record (soft-delete by default)."""
    svc = CorporateSealRegisterService()
    ok = svc.delete_corporatesealregister(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CorporateSealRegister with ID {item_id} not found")
    return None

@router.get("/corporatesealregisters/analytics/metrics", response_model=Dict[str, Any])
def get_corporatesealregister_metrics():
    """Calculate summary statistical KPIs for CorporateSealRegister collection."""
    svc = CorporateSealRegisterService()
    return svc.calculate_aggregate_metrics()

