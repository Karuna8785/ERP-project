"""
Enterprise CRM & Account Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    LeadAccountService,
    ContactPersonService,
    OpportunityDealService,
    SalesPipelineStageService,
    QuoteProposalService,
    TerritoryRegionService,
    SalesQuotaTargetService,
    CompetitorAnalysisService,
    CustomerTouchpointService,
    CampaignTrackingService,
    LeadScoreMetricService,
    DealCommissionService,
    CustomerChurnRiskService,
    MeetingTranscriptService,
    ReferralSourceService,
    PartnerChannelService,
)
from .schemas import (
    LeadAccountCreateSchema, LeadAccountUpdateSchema, LeadAccountResponseSchema,
    ContactPersonCreateSchema, ContactPersonUpdateSchema, ContactPersonResponseSchema,
    OpportunityDealCreateSchema, OpportunityDealUpdateSchema, OpportunityDealResponseSchema,
    SalesPipelineStageCreateSchema, SalesPipelineStageUpdateSchema, SalesPipelineStageResponseSchema,
    QuoteProposalCreateSchema, QuoteProposalUpdateSchema, QuoteProposalResponseSchema,
    TerritoryRegionCreateSchema, TerritoryRegionUpdateSchema, TerritoryRegionResponseSchema,
    SalesQuotaTargetCreateSchema, SalesQuotaTargetUpdateSchema, SalesQuotaTargetResponseSchema,
    CompetitorAnalysisCreateSchema, CompetitorAnalysisUpdateSchema, CompetitorAnalysisResponseSchema,
    CustomerTouchpointCreateSchema, CustomerTouchpointUpdateSchema, CustomerTouchpointResponseSchema,
    CampaignTrackingCreateSchema, CampaignTrackingUpdateSchema, CampaignTrackingResponseSchema,
    LeadScoreMetricCreateSchema, LeadScoreMetricUpdateSchema, LeadScoreMetricResponseSchema,
    DealCommissionCreateSchema, DealCommissionUpdateSchema, DealCommissionResponseSchema,
    CustomerChurnRiskCreateSchema, CustomerChurnRiskUpdateSchema, CustomerChurnRiskResponseSchema,
    MeetingTranscriptCreateSchema, MeetingTranscriptUpdateSchema, MeetingTranscriptResponseSchema,
    ReferralSourceCreateSchema, ReferralSourceUpdateSchema, ReferralSourceResponseSchema,
    PartnerChannelCreateSchema, PartnerChannelUpdateSchema, PartnerChannelResponseSchema,
)

router = APIRouter(prefix="/crm_enterprise", tags=["Enterprise CRM & Account Management"])

# ==================== LeadAccount Endpoints ====================
@router.get("/leadaccounts", response_model=List[Dict[str, Any]])
def list_leadaccounts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeadAccount records with pagination and filtering."""
    svc = LeadAccountService()
    items = svc.list_leadaccounts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leadaccounts/{item_id}", response_model=Dict[str, Any])
def get_leadaccount_by_id(item_id: int):
    """Retrieve detailed record for LeadAccount by ID."""
    svc = LeadAccountService()
    item = svc.get_leadaccount_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeadAccount with ID {item_id} not found")
    return item.to_dict()

@router.post("/leadaccounts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leadaccount(payload: LeadAccountCreateSchema):
    """Create new LeadAccount instance in enterprise repository."""
    svc = LeadAccountService()
    try:
        item = svc.create_leadaccount(
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

@router.put("/leadaccounts/{item_id}", response_model=Dict[str, Any])
def update_leadaccount(item_id: int, payload: LeadAccountUpdateSchema):
    """Update existing LeadAccount record fields."""
    svc = LeadAccountService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leadaccount(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeadAccount with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leadaccounts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leadaccount(item_id: int, hard: bool = Query(False)):
    """Delete LeadAccount record (soft-delete by default)."""
    svc = LeadAccountService()
    ok = svc.delete_leadaccount(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeadAccount with ID {item_id} not found")
    return None

@router.get("/leadaccounts/analytics/metrics", response_model=Dict[str, Any])
def get_leadaccount_metrics():
    """Calculate summary statistical KPIs for LeadAccount collection."""
    svc = LeadAccountService()
    return svc.calculate_aggregate_metrics()

# ==================== ContactPerson Endpoints ====================
@router.get("/contactpersons", response_model=List[Dict[str, Any]])
def list_contactpersons(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContactPerson records with pagination and filtering."""
    svc = ContactPersonService()
    items = svc.list_contactpersons(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/contactpersons/{item_id}", response_model=Dict[str, Any])
def get_contactperson_by_id(item_id: int):
    """Retrieve detailed record for ContactPerson by ID."""
    svc = ContactPersonService()
    item = svc.get_contactperson_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContactPerson with ID {item_id} not found")
    return item.to_dict()

@router.post("/contactpersons", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_contactperson(payload: ContactPersonCreateSchema):
    """Create new ContactPerson instance in enterprise repository."""
    svc = ContactPersonService()
    try:
        item = svc.create_contactperson(
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

@router.put("/contactpersons/{item_id}", response_model=Dict[str, Any])
def update_contactperson(item_id: int, payload: ContactPersonUpdateSchema):
    """Update existing ContactPerson record fields."""
    svc = ContactPersonService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_contactperson(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContactPerson with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/contactpersons/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contactperson(item_id: int, hard: bool = Query(False)):
    """Delete ContactPerson record (soft-delete by default)."""
    svc = ContactPersonService()
    ok = svc.delete_contactperson(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContactPerson with ID {item_id} not found")
    return None

@router.get("/contactpersons/analytics/metrics", response_model=Dict[str, Any])
def get_contactperson_metrics():
    """Calculate summary statistical KPIs for ContactPerson collection."""
    svc = ContactPersonService()
    return svc.calculate_aggregate_metrics()

# ==================== OpportunityDeal Endpoints ====================
@router.get("/opportunitydeals", response_model=List[Dict[str, Any]])
def list_opportunitydeals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OpportunityDeal records with pagination and filtering."""
    svc = OpportunityDealService()
    items = svc.list_opportunitydeals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/opportunitydeals/{item_id}", response_model=Dict[str, Any])
def get_opportunitydeal_by_id(item_id: int):
    """Retrieve detailed record for OpportunityDeal by ID."""
    svc = OpportunityDealService()
    item = svc.get_opportunitydeal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OpportunityDeal with ID {item_id} not found")
    return item.to_dict()

@router.post("/opportunitydeals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_opportunitydeal(payload: OpportunityDealCreateSchema):
    """Create new OpportunityDeal instance in enterprise repository."""
    svc = OpportunityDealService()
    try:
        item = svc.create_opportunitydeal(
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

@router.put("/opportunitydeals/{item_id}", response_model=Dict[str, Any])
def update_opportunitydeal(item_id: int, payload: OpportunityDealUpdateSchema):
    """Update existing OpportunityDeal record fields."""
    svc = OpportunityDealService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_opportunitydeal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OpportunityDeal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/opportunitydeals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_opportunitydeal(item_id: int, hard: bool = Query(False)):
    """Delete OpportunityDeal record (soft-delete by default)."""
    svc = OpportunityDealService()
    ok = svc.delete_opportunitydeal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OpportunityDeal with ID {item_id} not found")
    return None

@router.get("/opportunitydeals/analytics/metrics", response_model=Dict[str, Any])
def get_opportunitydeal_metrics():
    """Calculate summary statistical KPIs for OpportunityDeal collection."""
    svc = OpportunityDealService()
    return svc.calculate_aggregate_metrics()

# ==================== SalesPipelineStage Endpoints ====================
@router.get("/salespipelinestages", response_model=List[Dict[str, Any]])
def list_salespipelinestages(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SalesPipelineStage records with pagination and filtering."""
    svc = SalesPipelineStageService()
    items = svc.list_salespipelinestages(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/salespipelinestages/{item_id}", response_model=Dict[str, Any])
def get_salespipelinestage_by_id(item_id: int):
    """Retrieve detailed record for SalesPipelineStage by ID."""
    svc = SalesPipelineStageService()
    item = svc.get_salespipelinestage_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SalesPipelineStage with ID {item_id} not found")
    return item.to_dict()

@router.post("/salespipelinestages", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_salespipelinestage(payload: SalesPipelineStageCreateSchema):
    """Create new SalesPipelineStage instance in enterprise repository."""
    svc = SalesPipelineStageService()
    try:
        item = svc.create_salespipelinestage(
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

@router.put("/salespipelinestages/{item_id}", response_model=Dict[str, Any])
def update_salespipelinestage(item_id: int, payload: SalesPipelineStageUpdateSchema):
    """Update existing SalesPipelineStage record fields."""
    svc = SalesPipelineStageService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_salespipelinestage(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SalesPipelineStage with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/salespipelinestages/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_salespipelinestage(item_id: int, hard: bool = Query(False)):
    """Delete SalesPipelineStage record (soft-delete by default)."""
    svc = SalesPipelineStageService()
    ok = svc.delete_salespipelinestage(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SalesPipelineStage with ID {item_id} not found")
    return None

@router.get("/salespipelinestages/analytics/metrics", response_model=Dict[str, Any])
def get_salespipelinestage_metrics():
    """Calculate summary statistical KPIs for SalesPipelineStage collection."""
    svc = SalesPipelineStageService()
    return svc.calculate_aggregate_metrics()

# ==================== QuoteProposal Endpoints ====================
@router.get("/quoteproposals", response_model=List[Dict[str, Any]])
def list_quoteproposals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List QuoteProposal records with pagination and filtering."""
    svc = QuoteProposalService()
    items = svc.list_quoteproposals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/quoteproposals/{item_id}", response_model=Dict[str, Any])
def get_quoteproposal_by_id(item_id: int):
    """Retrieve detailed record for QuoteProposal by ID."""
    svc = QuoteProposalService()
    item = svc.get_quoteproposal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"QuoteProposal with ID {item_id} not found")
    return item.to_dict()

@router.post("/quoteproposals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_quoteproposal(payload: QuoteProposalCreateSchema):
    """Create new QuoteProposal instance in enterprise repository."""
    svc = QuoteProposalService()
    try:
        item = svc.create_quoteproposal(
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

@router.put("/quoteproposals/{item_id}", response_model=Dict[str, Any])
def update_quoteproposal(item_id: int, payload: QuoteProposalUpdateSchema):
    """Update existing QuoteProposal record fields."""
    svc = QuoteProposalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_quoteproposal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"QuoteProposal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/quoteproposals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quoteproposal(item_id: int, hard: bool = Query(False)):
    """Delete QuoteProposal record (soft-delete by default)."""
    svc = QuoteProposalService()
    ok = svc.delete_quoteproposal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"QuoteProposal with ID {item_id} not found")
    return None

@router.get("/quoteproposals/analytics/metrics", response_model=Dict[str, Any])
def get_quoteproposal_metrics():
    """Calculate summary statistical KPIs for QuoteProposal collection."""
    svc = QuoteProposalService()
    return svc.calculate_aggregate_metrics()

# ==================== TerritoryRegion Endpoints ====================
@router.get("/territoryregions", response_model=List[Dict[str, Any]])
def list_territoryregions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TerritoryRegion records with pagination and filtering."""
    svc = TerritoryRegionService()
    items = svc.list_territoryregions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/territoryregions/{item_id}", response_model=Dict[str, Any])
def get_territoryregion_by_id(item_id: int):
    """Retrieve detailed record for TerritoryRegion by ID."""
    svc = TerritoryRegionService()
    item = svc.get_territoryregion_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TerritoryRegion with ID {item_id} not found")
    return item.to_dict()

@router.post("/territoryregions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_territoryregion(payload: TerritoryRegionCreateSchema):
    """Create new TerritoryRegion instance in enterprise repository."""
    svc = TerritoryRegionService()
    try:
        item = svc.create_territoryregion(
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

@router.put("/territoryregions/{item_id}", response_model=Dict[str, Any])
def update_territoryregion(item_id: int, payload: TerritoryRegionUpdateSchema):
    """Update existing TerritoryRegion record fields."""
    svc = TerritoryRegionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_territoryregion(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TerritoryRegion with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/territoryregions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_territoryregion(item_id: int, hard: bool = Query(False)):
    """Delete TerritoryRegion record (soft-delete by default)."""
    svc = TerritoryRegionService()
    ok = svc.delete_territoryregion(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TerritoryRegion with ID {item_id} not found")
    return None

@router.get("/territoryregions/analytics/metrics", response_model=Dict[str, Any])
def get_territoryregion_metrics():
    """Calculate summary statistical KPIs for TerritoryRegion collection."""
    svc = TerritoryRegionService()
    return svc.calculate_aggregate_metrics()

# ==================== SalesQuotaTarget Endpoints ====================
@router.get("/salesquotatargets", response_model=List[Dict[str, Any]])
def list_salesquotatargets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SalesQuotaTarget records with pagination and filtering."""
    svc = SalesQuotaTargetService()
    items = svc.list_salesquotatargets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/salesquotatargets/{item_id}", response_model=Dict[str, Any])
def get_salesquotatarget_by_id(item_id: int):
    """Retrieve detailed record for SalesQuotaTarget by ID."""
    svc = SalesQuotaTargetService()
    item = svc.get_salesquotatarget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SalesQuotaTarget with ID {item_id} not found")
    return item.to_dict()

@router.post("/salesquotatargets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_salesquotatarget(payload: SalesQuotaTargetCreateSchema):
    """Create new SalesQuotaTarget instance in enterprise repository."""
    svc = SalesQuotaTargetService()
    try:
        item = svc.create_salesquotatarget(
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

@router.put("/salesquotatargets/{item_id}", response_model=Dict[str, Any])
def update_salesquotatarget(item_id: int, payload: SalesQuotaTargetUpdateSchema):
    """Update existing SalesQuotaTarget record fields."""
    svc = SalesQuotaTargetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_salesquotatarget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SalesQuotaTarget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/salesquotatargets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_salesquotatarget(item_id: int, hard: bool = Query(False)):
    """Delete SalesQuotaTarget record (soft-delete by default)."""
    svc = SalesQuotaTargetService()
    ok = svc.delete_salesquotatarget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SalesQuotaTarget with ID {item_id} not found")
    return None

@router.get("/salesquotatargets/analytics/metrics", response_model=Dict[str, Any])
def get_salesquotatarget_metrics():
    """Calculate summary statistical KPIs for SalesQuotaTarget collection."""
    svc = SalesQuotaTargetService()
    return svc.calculate_aggregate_metrics()

# ==================== CompetitorAnalysis Endpoints ====================
@router.get("/competitoranalysiss", response_model=List[Dict[str, Any]])
def list_competitoranalysiss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CompetitorAnalysis records with pagination and filtering."""
    svc = CompetitorAnalysisService()
    items = svc.list_competitoranalysiss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/competitoranalysiss/{item_id}", response_model=Dict[str, Any])
def get_competitoranalysis_by_id(item_id: int):
    """Retrieve detailed record for CompetitorAnalysis by ID."""
    svc = CompetitorAnalysisService()
    item = svc.get_competitoranalysis_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CompetitorAnalysis with ID {item_id} not found")
    return item.to_dict()

@router.post("/competitoranalysiss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_competitoranalysis(payload: CompetitorAnalysisCreateSchema):
    """Create new CompetitorAnalysis instance in enterprise repository."""
    svc = CompetitorAnalysisService()
    try:
        item = svc.create_competitoranalysis(
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

@router.put("/competitoranalysiss/{item_id}", response_model=Dict[str, Any])
def update_competitoranalysis(item_id: int, payload: CompetitorAnalysisUpdateSchema):
    """Update existing CompetitorAnalysis record fields."""
    svc = CompetitorAnalysisService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_competitoranalysis(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CompetitorAnalysis with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/competitoranalysiss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_competitoranalysis(item_id: int, hard: bool = Query(False)):
    """Delete CompetitorAnalysis record (soft-delete by default)."""
    svc = CompetitorAnalysisService()
    ok = svc.delete_competitoranalysis(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CompetitorAnalysis with ID {item_id} not found")
    return None

@router.get("/competitoranalysiss/analytics/metrics", response_model=Dict[str, Any])
def get_competitoranalysis_metrics():
    """Calculate summary statistical KPIs for CompetitorAnalysis collection."""
    svc = CompetitorAnalysisService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerTouchpoint Endpoints ====================
@router.get("/customertouchpoints", response_model=List[Dict[str, Any]])
def list_customertouchpoints(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerTouchpoint records with pagination and filtering."""
    svc = CustomerTouchpointService()
    items = svc.list_customertouchpoints(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customertouchpoints/{item_id}", response_model=Dict[str, Any])
def get_customertouchpoint_by_id(item_id: int):
    """Retrieve detailed record for CustomerTouchpoint by ID."""
    svc = CustomerTouchpointService()
    item = svc.get_customertouchpoint_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerTouchpoint with ID {item_id} not found")
    return item.to_dict()

@router.post("/customertouchpoints", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customertouchpoint(payload: CustomerTouchpointCreateSchema):
    """Create new CustomerTouchpoint instance in enterprise repository."""
    svc = CustomerTouchpointService()
    try:
        item = svc.create_customertouchpoint(
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

@router.put("/customertouchpoints/{item_id}", response_model=Dict[str, Any])
def update_customertouchpoint(item_id: int, payload: CustomerTouchpointUpdateSchema):
    """Update existing CustomerTouchpoint record fields."""
    svc = CustomerTouchpointService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customertouchpoint(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerTouchpoint with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customertouchpoints/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customertouchpoint(item_id: int, hard: bool = Query(False)):
    """Delete CustomerTouchpoint record (soft-delete by default)."""
    svc = CustomerTouchpointService()
    ok = svc.delete_customertouchpoint(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerTouchpoint with ID {item_id} not found")
    return None

@router.get("/customertouchpoints/analytics/metrics", response_model=Dict[str, Any])
def get_customertouchpoint_metrics():
    """Calculate summary statistical KPIs for CustomerTouchpoint collection."""
    svc = CustomerTouchpointService()
    return svc.calculate_aggregate_metrics()

# ==================== CampaignTracking Endpoints ====================
@router.get("/campaigntrackings", response_model=List[Dict[str, Any]])
def list_campaigntrackings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CampaignTracking records with pagination and filtering."""
    svc = CampaignTrackingService()
    items = svc.list_campaigntrackings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/campaigntrackings/{item_id}", response_model=Dict[str, Any])
def get_campaigntracking_by_id(item_id: int):
    """Retrieve detailed record for CampaignTracking by ID."""
    svc = CampaignTrackingService()
    item = svc.get_campaigntracking_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CampaignTracking with ID {item_id} not found")
    return item.to_dict()

@router.post("/campaigntrackings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_campaigntracking(payload: CampaignTrackingCreateSchema):
    """Create new CampaignTracking instance in enterprise repository."""
    svc = CampaignTrackingService()
    try:
        item = svc.create_campaigntracking(
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

@router.put("/campaigntrackings/{item_id}", response_model=Dict[str, Any])
def update_campaigntracking(item_id: int, payload: CampaignTrackingUpdateSchema):
    """Update existing CampaignTracking record fields."""
    svc = CampaignTrackingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_campaigntracking(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CampaignTracking with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/campaigntrackings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_campaigntracking(item_id: int, hard: bool = Query(False)):
    """Delete CampaignTracking record (soft-delete by default)."""
    svc = CampaignTrackingService()
    ok = svc.delete_campaigntracking(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CampaignTracking with ID {item_id} not found")
    return None

@router.get("/campaigntrackings/analytics/metrics", response_model=Dict[str, Any])
def get_campaigntracking_metrics():
    """Calculate summary statistical KPIs for CampaignTracking collection."""
    svc = CampaignTrackingService()
    return svc.calculate_aggregate_metrics()

# ==================== LeadScoreMetric Endpoints ====================
@router.get("/leadscoremetrics", response_model=List[Dict[str, Any]])
def list_leadscoremetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeadScoreMetric records with pagination and filtering."""
    svc = LeadScoreMetricService()
    items = svc.list_leadscoremetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leadscoremetrics/{item_id}", response_model=Dict[str, Any])
def get_leadscoremetric_by_id(item_id: int):
    """Retrieve detailed record for LeadScoreMetric by ID."""
    svc = LeadScoreMetricService()
    item = svc.get_leadscoremetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeadScoreMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/leadscoremetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leadscoremetric(payload: LeadScoreMetricCreateSchema):
    """Create new LeadScoreMetric instance in enterprise repository."""
    svc = LeadScoreMetricService()
    try:
        item = svc.create_leadscoremetric(
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

@router.put("/leadscoremetrics/{item_id}", response_model=Dict[str, Any])
def update_leadscoremetric(item_id: int, payload: LeadScoreMetricUpdateSchema):
    """Update existing LeadScoreMetric record fields."""
    svc = LeadScoreMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leadscoremetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeadScoreMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leadscoremetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leadscoremetric(item_id: int, hard: bool = Query(False)):
    """Delete LeadScoreMetric record (soft-delete by default)."""
    svc = LeadScoreMetricService()
    ok = svc.delete_leadscoremetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeadScoreMetric with ID {item_id} not found")
    return None

@router.get("/leadscoremetrics/analytics/metrics", response_model=Dict[str, Any])
def get_leadscoremetric_metrics():
    """Calculate summary statistical KPIs for LeadScoreMetric collection."""
    svc = LeadScoreMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== DealCommission Endpoints ====================
@router.get("/dealcommissions", response_model=List[Dict[str, Any]])
def list_dealcommissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DealCommission records with pagination and filtering."""
    svc = DealCommissionService()
    items = svc.list_dealcommissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dealcommissions/{item_id}", response_model=Dict[str, Any])
def get_dealcommission_by_id(item_id: int):
    """Retrieve detailed record for DealCommission by ID."""
    svc = DealCommissionService()
    item = svc.get_dealcommission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DealCommission with ID {item_id} not found")
    return item.to_dict()

@router.post("/dealcommissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dealcommission(payload: DealCommissionCreateSchema):
    """Create new DealCommission instance in enterprise repository."""
    svc = DealCommissionService()
    try:
        item = svc.create_dealcommission(
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

@router.put("/dealcommissions/{item_id}", response_model=Dict[str, Any])
def update_dealcommission(item_id: int, payload: DealCommissionUpdateSchema):
    """Update existing DealCommission record fields."""
    svc = DealCommissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dealcommission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DealCommission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dealcommissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dealcommission(item_id: int, hard: bool = Query(False)):
    """Delete DealCommission record (soft-delete by default)."""
    svc = DealCommissionService()
    ok = svc.delete_dealcommission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DealCommission with ID {item_id} not found")
    return None

@router.get("/dealcommissions/analytics/metrics", response_model=Dict[str, Any])
def get_dealcommission_metrics():
    """Calculate summary statistical KPIs for DealCommission collection."""
    svc = DealCommissionService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerChurnRisk Endpoints ====================
@router.get("/customerchurnrisks", response_model=List[Dict[str, Any]])
def list_customerchurnrisks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerChurnRisk records with pagination and filtering."""
    svc = CustomerChurnRiskService()
    items = svc.list_customerchurnrisks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerchurnrisks/{item_id}", response_model=Dict[str, Any])
def get_customerchurnrisk_by_id(item_id: int):
    """Retrieve detailed record for CustomerChurnRisk by ID."""
    svc = CustomerChurnRiskService()
    item = svc.get_customerchurnrisk_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerChurnRisk with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerchurnrisks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerchurnrisk(payload: CustomerChurnRiskCreateSchema):
    """Create new CustomerChurnRisk instance in enterprise repository."""
    svc = CustomerChurnRiskService()
    try:
        item = svc.create_customerchurnrisk(
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

@router.put("/customerchurnrisks/{item_id}", response_model=Dict[str, Any])
def update_customerchurnrisk(item_id: int, payload: CustomerChurnRiskUpdateSchema):
    """Update existing CustomerChurnRisk record fields."""
    svc = CustomerChurnRiskService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerchurnrisk(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerChurnRisk with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerchurnrisks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerchurnrisk(item_id: int, hard: bool = Query(False)):
    """Delete CustomerChurnRisk record (soft-delete by default)."""
    svc = CustomerChurnRiskService()
    ok = svc.delete_customerchurnrisk(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerChurnRisk with ID {item_id} not found")
    return None

@router.get("/customerchurnrisks/analytics/metrics", response_model=Dict[str, Any])
def get_customerchurnrisk_metrics():
    """Calculate summary statistical KPIs for CustomerChurnRisk collection."""
    svc = CustomerChurnRiskService()
    return svc.calculate_aggregate_metrics()

# ==================== MeetingTranscript Endpoints ====================
@router.get("/meetingtranscripts", response_model=List[Dict[str, Any]])
def list_meetingtranscripts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MeetingTranscript records with pagination and filtering."""
    svc = MeetingTranscriptService()
    items = svc.list_meetingtranscripts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/meetingtranscripts/{item_id}", response_model=Dict[str, Any])
def get_meetingtranscript_by_id(item_id: int):
    """Retrieve detailed record for MeetingTranscript by ID."""
    svc = MeetingTranscriptService()
    item = svc.get_meetingtranscript_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MeetingTranscript with ID {item_id} not found")
    return item.to_dict()

@router.post("/meetingtranscripts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_meetingtranscript(payload: MeetingTranscriptCreateSchema):
    """Create new MeetingTranscript instance in enterprise repository."""
    svc = MeetingTranscriptService()
    try:
        item = svc.create_meetingtranscript(
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

@router.put("/meetingtranscripts/{item_id}", response_model=Dict[str, Any])
def update_meetingtranscript(item_id: int, payload: MeetingTranscriptUpdateSchema):
    """Update existing MeetingTranscript record fields."""
    svc = MeetingTranscriptService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_meetingtranscript(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MeetingTranscript with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/meetingtranscripts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meetingtranscript(item_id: int, hard: bool = Query(False)):
    """Delete MeetingTranscript record (soft-delete by default)."""
    svc = MeetingTranscriptService()
    ok = svc.delete_meetingtranscript(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MeetingTranscript with ID {item_id} not found")
    return None

@router.get("/meetingtranscripts/analytics/metrics", response_model=Dict[str, Any])
def get_meetingtranscript_metrics():
    """Calculate summary statistical KPIs for MeetingTranscript collection."""
    svc = MeetingTranscriptService()
    return svc.calculate_aggregate_metrics()

# ==================== ReferralSource Endpoints ====================
@router.get("/referralsources", response_model=List[Dict[str, Any]])
def list_referralsources(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReferralSource records with pagination and filtering."""
    svc = ReferralSourceService()
    items = svc.list_referralsources(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/referralsources/{item_id}", response_model=Dict[str, Any])
def get_referralsource_by_id(item_id: int):
    """Retrieve detailed record for ReferralSource by ID."""
    svc = ReferralSourceService()
    item = svc.get_referralsource_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReferralSource with ID {item_id} not found")
    return item.to_dict()

@router.post("/referralsources", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_referralsource(payload: ReferralSourceCreateSchema):
    """Create new ReferralSource instance in enterprise repository."""
    svc = ReferralSourceService()
    try:
        item = svc.create_referralsource(
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

@router.put("/referralsources/{item_id}", response_model=Dict[str, Any])
def update_referralsource(item_id: int, payload: ReferralSourceUpdateSchema):
    """Update existing ReferralSource record fields."""
    svc = ReferralSourceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_referralsource(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReferralSource with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/referralsources/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_referralsource(item_id: int, hard: bool = Query(False)):
    """Delete ReferralSource record (soft-delete by default)."""
    svc = ReferralSourceService()
    ok = svc.delete_referralsource(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReferralSource with ID {item_id} not found")
    return None

@router.get("/referralsources/analytics/metrics", response_model=Dict[str, Any])
def get_referralsource_metrics():
    """Calculate summary statistical KPIs for ReferralSource collection."""
    svc = ReferralSourceService()
    return svc.calculate_aggregate_metrics()

# ==================== PartnerChannel Endpoints ====================
@router.get("/partnerchannels", response_model=List[Dict[str, Any]])
def list_partnerchannels(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartnerChannel records with pagination and filtering."""
    svc = PartnerChannelService()
    items = svc.list_partnerchannels(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partnerchannels/{item_id}", response_model=Dict[str, Any])
def get_partnerchannel_by_id(item_id: int):
    """Retrieve detailed record for PartnerChannel by ID."""
    svc = PartnerChannelService()
    item = svc.get_partnerchannel_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartnerChannel with ID {item_id} not found")
    return item.to_dict()

@router.post("/partnerchannels", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partnerchannel(payload: PartnerChannelCreateSchema):
    """Create new PartnerChannel instance in enterprise repository."""
    svc = PartnerChannelService()
    try:
        item = svc.create_partnerchannel(
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

@router.put("/partnerchannels/{item_id}", response_model=Dict[str, Any])
def update_partnerchannel(item_id: int, payload: PartnerChannelUpdateSchema):
    """Update existing PartnerChannel record fields."""
    svc = PartnerChannelService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partnerchannel(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartnerChannel with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partnerchannels/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partnerchannel(item_id: int, hard: bool = Query(False)):
    """Delete PartnerChannel record (soft-delete by default)."""
    svc = PartnerChannelService()
    ok = svc.delete_partnerchannel(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartnerChannel with ID {item_id} not found")
    return None

@router.get("/partnerchannels/analytics/metrics", response_model=Dict[str, Any])
def get_partnerchannel_metrics():
    """Calculate summary statistical KPIs for PartnerChannel collection."""
    svc = PartnerChannelService()
    return svc.calculate_aggregate_metrics()

