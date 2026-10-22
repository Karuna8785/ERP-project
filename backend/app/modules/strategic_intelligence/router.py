"""
Market Landscaping & Competitive Intelligence - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    MarketResearchReportService,
    CompetitorProductBenchmarkService,
    SWOTAnalysisMatrixService,
    IndustryTrendSignalService,
    PatentLandscapeStudyService,
    PricingIntelligenceDataService,
    CustomerWinLossInterviewService,
    MarketShareEstimateService,
    StrategicPartnershipOppService,
    MacroeconomicIndicatorService,
    DisruptiveThreatAlertService,
    AcquisitionTargetProfileService,
    BrandPerceptionIndexService,
    ValueChainMappingService,
    ScenarioSimulationModelService,
    ExecutiveBriefingBriefService,
)
from .schemas import (
    MarketResearchReportCreateSchema, MarketResearchReportUpdateSchema, MarketResearchReportResponseSchema,
    CompetitorProductBenchmarkCreateSchema, CompetitorProductBenchmarkUpdateSchema, CompetitorProductBenchmarkResponseSchema,
    SWOTAnalysisMatrixCreateSchema, SWOTAnalysisMatrixUpdateSchema, SWOTAnalysisMatrixResponseSchema,
    IndustryTrendSignalCreateSchema, IndustryTrendSignalUpdateSchema, IndustryTrendSignalResponseSchema,
    PatentLandscapeStudyCreateSchema, PatentLandscapeStudyUpdateSchema, PatentLandscapeStudyResponseSchema,
    PricingIntelligenceDataCreateSchema, PricingIntelligenceDataUpdateSchema, PricingIntelligenceDataResponseSchema,
    CustomerWinLossInterviewCreateSchema, CustomerWinLossInterviewUpdateSchema, CustomerWinLossInterviewResponseSchema,
    MarketShareEstimateCreateSchema, MarketShareEstimateUpdateSchema, MarketShareEstimateResponseSchema,
    StrategicPartnershipOppCreateSchema, StrategicPartnershipOppUpdateSchema, StrategicPartnershipOppResponseSchema,
    MacroeconomicIndicatorCreateSchema, MacroeconomicIndicatorUpdateSchema, MacroeconomicIndicatorResponseSchema,
    DisruptiveThreatAlertCreateSchema, DisruptiveThreatAlertUpdateSchema, DisruptiveThreatAlertResponseSchema,
    AcquisitionTargetProfileCreateSchema, AcquisitionTargetProfileUpdateSchema, AcquisitionTargetProfileResponseSchema,
    BrandPerceptionIndexCreateSchema, BrandPerceptionIndexUpdateSchema, BrandPerceptionIndexResponseSchema,
    ValueChainMappingCreateSchema, ValueChainMappingUpdateSchema, ValueChainMappingResponseSchema,
    ScenarioSimulationModelCreateSchema, ScenarioSimulationModelUpdateSchema, ScenarioSimulationModelResponseSchema,
    ExecutiveBriefingBriefCreateSchema, ExecutiveBriefingBriefUpdateSchema, ExecutiveBriefingBriefResponseSchema,
)

router = APIRouter(prefix="/strategic_intelligence", tags=["Market Landscaping & Competitive Intelligence"])

# ==================== MarketResearchReport Endpoints ====================
@router.get("/marketresearchreports", response_model=List[Dict[str, Any]])
def list_marketresearchreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MarketResearchReport records with pagination and filtering."""
    svc = MarketResearchReportService()
    items = svc.list_marketresearchreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/marketresearchreports/{item_id}", response_model=Dict[str, Any])
def get_marketresearchreport_by_id(item_id: int):
    """Retrieve detailed record for MarketResearchReport by ID."""
    svc = MarketResearchReportService()
    item = svc.get_marketresearchreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MarketResearchReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/marketresearchreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_marketresearchreport(payload: MarketResearchReportCreateSchema):
    """Create new MarketResearchReport instance in enterprise repository."""
    svc = MarketResearchReportService()
    try:
        item = svc.create_marketresearchreport(
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

@router.put("/marketresearchreports/{item_id}", response_model=Dict[str, Any])
def update_marketresearchreport(item_id: int, payload: MarketResearchReportUpdateSchema):
    """Update existing MarketResearchReport record fields."""
    svc = MarketResearchReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_marketresearchreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MarketResearchReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/marketresearchreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_marketresearchreport(item_id: int, hard: bool = Query(False)):
    """Delete MarketResearchReport record (soft-delete by default)."""
    svc = MarketResearchReportService()
    ok = svc.delete_marketresearchreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MarketResearchReport with ID {item_id} not found")
    return None

@router.get("/marketresearchreports/analytics/metrics", response_model=Dict[str, Any])
def get_marketresearchreport_metrics():
    """Calculate summary statistical KPIs for MarketResearchReport collection."""
    svc = MarketResearchReportService()
    return svc.calculate_aggregate_metrics()

# ==================== CompetitorProductBenchmark Endpoints ====================
@router.get("/competitorproductbenchmarks", response_model=List[Dict[str, Any]])
def list_competitorproductbenchmarks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CompetitorProductBenchmark records with pagination and filtering."""
    svc = CompetitorProductBenchmarkService()
    items = svc.list_competitorproductbenchmarks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/competitorproductbenchmarks/{item_id}", response_model=Dict[str, Any])
def get_competitorproductbenchmark_by_id(item_id: int):
    """Retrieve detailed record for CompetitorProductBenchmark by ID."""
    svc = CompetitorProductBenchmarkService()
    item = svc.get_competitorproductbenchmark_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CompetitorProductBenchmark with ID {item_id} not found")
    return item.to_dict()

@router.post("/competitorproductbenchmarks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_competitorproductbenchmark(payload: CompetitorProductBenchmarkCreateSchema):
    """Create new CompetitorProductBenchmark instance in enterprise repository."""
    svc = CompetitorProductBenchmarkService()
    try:
        item = svc.create_competitorproductbenchmark(
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

@router.put("/competitorproductbenchmarks/{item_id}", response_model=Dict[str, Any])
def update_competitorproductbenchmark(item_id: int, payload: CompetitorProductBenchmarkUpdateSchema):
    """Update existing CompetitorProductBenchmark record fields."""
    svc = CompetitorProductBenchmarkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_competitorproductbenchmark(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CompetitorProductBenchmark with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/competitorproductbenchmarks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_competitorproductbenchmark(item_id: int, hard: bool = Query(False)):
    """Delete CompetitorProductBenchmark record (soft-delete by default)."""
    svc = CompetitorProductBenchmarkService()
    ok = svc.delete_competitorproductbenchmark(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CompetitorProductBenchmark with ID {item_id} not found")
    return None

@router.get("/competitorproductbenchmarks/analytics/metrics", response_model=Dict[str, Any])
def get_competitorproductbenchmark_metrics():
    """Calculate summary statistical KPIs for CompetitorProductBenchmark collection."""
    svc = CompetitorProductBenchmarkService()
    return svc.calculate_aggregate_metrics()

# ==================== SWOTAnalysisMatrix Endpoints ====================
@router.get("/swotanalysismatrixs", response_model=List[Dict[str, Any]])
def list_swotanalysismatrixs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SWOTAnalysisMatrix records with pagination and filtering."""
    svc = SWOTAnalysisMatrixService()
    items = svc.list_swotanalysismatrixs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/swotanalysismatrixs/{item_id}", response_model=Dict[str, Any])
def get_swotanalysismatrix_by_id(item_id: int):
    """Retrieve detailed record for SWOTAnalysisMatrix by ID."""
    svc = SWOTAnalysisMatrixService()
    item = svc.get_swotanalysismatrix_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SWOTAnalysisMatrix with ID {item_id} not found")
    return item.to_dict()

@router.post("/swotanalysismatrixs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_swotanalysismatrix(payload: SWOTAnalysisMatrixCreateSchema):
    """Create new SWOTAnalysisMatrix instance in enterprise repository."""
    svc = SWOTAnalysisMatrixService()
    try:
        item = svc.create_swotanalysismatrix(
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

@router.put("/swotanalysismatrixs/{item_id}", response_model=Dict[str, Any])
def update_swotanalysismatrix(item_id: int, payload: SWOTAnalysisMatrixUpdateSchema):
    """Update existing SWOTAnalysisMatrix record fields."""
    svc = SWOTAnalysisMatrixService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_swotanalysismatrix(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SWOTAnalysisMatrix with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/swotanalysismatrixs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_swotanalysismatrix(item_id: int, hard: bool = Query(False)):
    """Delete SWOTAnalysisMatrix record (soft-delete by default)."""
    svc = SWOTAnalysisMatrixService()
    ok = svc.delete_swotanalysismatrix(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SWOTAnalysisMatrix with ID {item_id} not found")
    return None

@router.get("/swotanalysismatrixs/analytics/metrics", response_model=Dict[str, Any])
def get_swotanalysismatrix_metrics():
    """Calculate summary statistical KPIs for SWOTAnalysisMatrix collection."""
    svc = SWOTAnalysisMatrixService()
    return svc.calculate_aggregate_metrics()

# ==================== IndustryTrendSignal Endpoints ====================
@router.get("/industrytrendsignals", response_model=List[Dict[str, Any]])
def list_industrytrendsignals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IndustryTrendSignal records with pagination and filtering."""
    svc = IndustryTrendSignalService()
    items = svc.list_industrytrendsignals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/industrytrendsignals/{item_id}", response_model=Dict[str, Any])
def get_industrytrendsignal_by_id(item_id: int):
    """Retrieve detailed record for IndustryTrendSignal by ID."""
    svc = IndustryTrendSignalService()
    item = svc.get_industrytrendsignal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IndustryTrendSignal with ID {item_id} not found")
    return item.to_dict()

@router.post("/industrytrendsignals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_industrytrendsignal(payload: IndustryTrendSignalCreateSchema):
    """Create new IndustryTrendSignal instance in enterprise repository."""
    svc = IndustryTrendSignalService()
    try:
        item = svc.create_industrytrendsignal(
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

@router.put("/industrytrendsignals/{item_id}", response_model=Dict[str, Any])
def update_industrytrendsignal(item_id: int, payload: IndustryTrendSignalUpdateSchema):
    """Update existing IndustryTrendSignal record fields."""
    svc = IndustryTrendSignalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_industrytrendsignal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IndustryTrendSignal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/industrytrendsignals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_industrytrendsignal(item_id: int, hard: bool = Query(False)):
    """Delete IndustryTrendSignal record (soft-delete by default)."""
    svc = IndustryTrendSignalService()
    ok = svc.delete_industrytrendsignal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IndustryTrendSignal with ID {item_id} not found")
    return None

@router.get("/industrytrendsignals/analytics/metrics", response_model=Dict[str, Any])
def get_industrytrendsignal_metrics():
    """Calculate summary statistical KPIs for IndustryTrendSignal collection."""
    svc = IndustryTrendSignalService()
    return svc.calculate_aggregate_metrics()

# ==================== PatentLandscapeStudy Endpoints ====================
@router.get("/patentlandscapestudys", response_model=List[Dict[str, Any]])
def list_patentlandscapestudys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PatentLandscapeStudy records with pagination and filtering."""
    svc = PatentLandscapeStudyService()
    items = svc.list_patentlandscapestudys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/patentlandscapestudys/{item_id}", response_model=Dict[str, Any])
def get_patentlandscapestudy_by_id(item_id: int):
    """Retrieve detailed record for PatentLandscapeStudy by ID."""
    svc = PatentLandscapeStudyService()
    item = svc.get_patentlandscapestudy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PatentLandscapeStudy with ID {item_id} not found")
    return item.to_dict()

@router.post("/patentlandscapestudys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_patentlandscapestudy(payload: PatentLandscapeStudyCreateSchema):
    """Create new PatentLandscapeStudy instance in enterprise repository."""
    svc = PatentLandscapeStudyService()
    try:
        item = svc.create_patentlandscapestudy(
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

@router.put("/patentlandscapestudys/{item_id}", response_model=Dict[str, Any])
def update_patentlandscapestudy(item_id: int, payload: PatentLandscapeStudyUpdateSchema):
    """Update existing PatentLandscapeStudy record fields."""
    svc = PatentLandscapeStudyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_patentlandscapestudy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PatentLandscapeStudy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/patentlandscapestudys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patentlandscapestudy(item_id: int, hard: bool = Query(False)):
    """Delete PatentLandscapeStudy record (soft-delete by default)."""
    svc = PatentLandscapeStudyService()
    ok = svc.delete_patentlandscapestudy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PatentLandscapeStudy with ID {item_id} not found")
    return None

@router.get("/patentlandscapestudys/analytics/metrics", response_model=Dict[str, Any])
def get_patentlandscapestudy_metrics():
    """Calculate summary statistical KPIs for PatentLandscapeStudy collection."""
    svc = PatentLandscapeStudyService()
    return svc.calculate_aggregate_metrics()

# ==================== PricingIntelligenceData Endpoints ====================
@router.get("/pricingintelligencedatas", response_model=List[Dict[str, Any]])
def list_pricingintelligencedatas(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PricingIntelligenceData records with pagination and filtering."""
    svc = PricingIntelligenceDataService()
    items = svc.list_pricingintelligencedatas(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/pricingintelligencedatas/{item_id}", response_model=Dict[str, Any])
def get_pricingintelligencedata_by_id(item_id: int):
    """Retrieve detailed record for PricingIntelligenceData by ID."""
    svc = PricingIntelligenceDataService()
    item = svc.get_pricingintelligencedata_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PricingIntelligenceData with ID {item_id} not found")
    return item.to_dict()

@router.post("/pricingintelligencedatas", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_pricingintelligencedata(payload: PricingIntelligenceDataCreateSchema):
    """Create new PricingIntelligenceData instance in enterprise repository."""
    svc = PricingIntelligenceDataService()
    try:
        item = svc.create_pricingintelligencedata(
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

@router.put("/pricingintelligencedatas/{item_id}", response_model=Dict[str, Any])
def update_pricingintelligencedata(item_id: int, payload: PricingIntelligenceDataUpdateSchema):
    """Update existing PricingIntelligenceData record fields."""
    svc = PricingIntelligenceDataService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_pricingintelligencedata(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PricingIntelligenceData with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/pricingintelligencedatas/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pricingintelligencedata(item_id: int, hard: bool = Query(False)):
    """Delete PricingIntelligenceData record (soft-delete by default)."""
    svc = PricingIntelligenceDataService()
    ok = svc.delete_pricingintelligencedata(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PricingIntelligenceData with ID {item_id} not found")
    return None

@router.get("/pricingintelligencedatas/analytics/metrics", response_model=Dict[str, Any])
def get_pricingintelligencedata_metrics():
    """Calculate summary statistical KPIs for PricingIntelligenceData collection."""
    svc = PricingIntelligenceDataService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerWinLossInterview Endpoints ====================
@router.get("/customerwinlossinterviews", response_model=List[Dict[str, Any]])
def list_customerwinlossinterviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerWinLossInterview records with pagination and filtering."""
    svc = CustomerWinLossInterviewService()
    items = svc.list_customerwinlossinterviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerwinlossinterviews/{item_id}", response_model=Dict[str, Any])
def get_customerwinlossinterview_by_id(item_id: int):
    """Retrieve detailed record for CustomerWinLossInterview by ID."""
    svc = CustomerWinLossInterviewService()
    item = svc.get_customerwinlossinterview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerWinLossInterview with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerwinlossinterviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerwinlossinterview(payload: CustomerWinLossInterviewCreateSchema):
    """Create new CustomerWinLossInterview instance in enterprise repository."""
    svc = CustomerWinLossInterviewService()
    try:
        item = svc.create_customerwinlossinterview(
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

@router.put("/customerwinlossinterviews/{item_id}", response_model=Dict[str, Any])
def update_customerwinlossinterview(item_id: int, payload: CustomerWinLossInterviewUpdateSchema):
    """Update existing CustomerWinLossInterview record fields."""
    svc = CustomerWinLossInterviewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerwinlossinterview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerWinLossInterview with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerwinlossinterviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerwinlossinterview(item_id: int, hard: bool = Query(False)):
    """Delete CustomerWinLossInterview record (soft-delete by default)."""
    svc = CustomerWinLossInterviewService()
    ok = svc.delete_customerwinlossinterview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerWinLossInterview with ID {item_id} not found")
    return None

@router.get("/customerwinlossinterviews/analytics/metrics", response_model=Dict[str, Any])
def get_customerwinlossinterview_metrics():
    """Calculate summary statistical KPIs for CustomerWinLossInterview collection."""
    svc = CustomerWinLossInterviewService()
    return svc.calculate_aggregate_metrics()

# ==================== MarketShareEstimate Endpoints ====================
@router.get("/marketshareestimates", response_model=List[Dict[str, Any]])
def list_marketshareestimates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MarketShareEstimate records with pagination and filtering."""
    svc = MarketShareEstimateService()
    items = svc.list_marketshareestimates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/marketshareestimates/{item_id}", response_model=Dict[str, Any])
def get_marketshareestimate_by_id(item_id: int):
    """Retrieve detailed record for MarketShareEstimate by ID."""
    svc = MarketShareEstimateService()
    item = svc.get_marketshareestimate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MarketShareEstimate with ID {item_id} not found")
    return item.to_dict()

@router.post("/marketshareestimates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_marketshareestimate(payload: MarketShareEstimateCreateSchema):
    """Create new MarketShareEstimate instance in enterprise repository."""
    svc = MarketShareEstimateService()
    try:
        item = svc.create_marketshareestimate(
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

@router.put("/marketshareestimates/{item_id}", response_model=Dict[str, Any])
def update_marketshareestimate(item_id: int, payload: MarketShareEstimateUpdateSchema):
    """Update existing MarketShareEstimate record fields."""
    svc = MarketShareEstimateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_marketshareestimate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MarketShareEstimate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/marketshareestimates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_marketshareestimate(item_id: int, hard: bool = Query(False)):
    """Delete MarketShareEstimate record (soft-delete by default)."""
    svc = MarketShareEstimateService()
    ok = svc.delete_marketshareestimate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MarketShareEstimate with ID {item_id} not found")
    return None

@router.get("/marketshareestimates/analytics/metrics", response_model=Dict[str, Any])
def get_marketshareestimate_metrics():
    """Calculate summary statistical KPIs for MarketShareEstimate collection."""
    svc = MarketShareEstimateService()
    return svc.calculate_aggregate_metrics()

# ==================== StrategicPartnershipOpp Endpoints ====================
@router.get("/strategicpartnershipopps", response_model=List[Dict[str, Any]])
def list_strategicpartnershipopps(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StrategicPartnershipOpp records with pagination and filtering."""
    svc = StrategicPartnershipOppService()
    items = svc.list_strategicpartnershipopps(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/strategicpartnershipopps/{item_id}", response_model=Dict[str, Any])
def get_strategicpartnershipopp_by_id(item_id: int):
    """Retrieve detailed record for StrategicPartnershipOpp by ID."""
    svc = StrategicPartnershipOppService()
    item = svc.get_strategicpartnershipopp_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StrategicPartnershipOpp with ID {item_id} not found")
    return item.to_dict()

@router.post("/strategicpartnershipopps", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_strategicpartnershipopp(payload: StrategicPartnershipOppCreateSchema):
    """Create new StrategicPartnershipOpp instance in enterprise repository."""
    svc = StrategicPartnershipOppService()
    try:
        item = svc.create_strategicpartnershipopp(
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

@router.put("/strategicpartnershipopps/{item_id}", response_model=Dict[str, Any])
def update_strategicpartnershipopp(item_id: int, payload: StrategicPartnershipOppUpdateSchema):
    """Update existing StrategicPartnershipOpp record fields."""
    svc = StrategicPartnershipOppService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_strategicpartnershipopp(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StrategicPartnershipOpp with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/strategicpartnershipopps/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_strategicpartnershipopp(item_id: int, hard: bool = Query(False)):
    """Delete StrategicPartnershipOpp record (soft-delete by default)."""
    svc = StrategicPartnershipOppService()
    ok = svc.delete_strategicpartnershipopp(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StrategicPartnershipOpp with ID {item_id} not found")
    return None

@router.get("/strategicpartnershipopps/analytics/metrics", response_model=Dict[str, Any])
def get_strategicpartnershipopp_metrics():
    """Calculate summary statistical KPIs for StrategicPartnershipOpp collection."""
    svc = StrategicPartnershipOppService()
    return svc.calculate_aggregate_metrics()

# ==================== MacroeconomicIndicator Endpoints ====================
@router.get("/macroeconomicindicators", response_model=List[Dict[str, Any]])
def list_macroeconomicindicators(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MacroeconomicIndicator records with pagination and filtering."""
    svc = MacroeconomicIndicatorService()
    items = svc.list_macroeconomicindicators(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/macroeconomicindicators/{item_id}", response_model=Dict[str, Any])
def get_macroeconomicindicator_by_id(item_id: int):
    """Retrieve detailed record for MacroeconomicIndicator by ID."""
    svc = MacroeconomicIndicatorService()
    item = svc.get_macroeconomicindicator_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MacroeconomicIndicator with ID {item_id} not found")
    return item.to_dict()

@router.post("/macroeconomicindicators", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_macroeconomicindicator(payload: MacroeconomicIndicatorCreateSchema):
    """Create new MacroeconomicIndicator instance in enterprise repository."""
    svc = MacroeconomicIndicatorService()
    try:
        item = svc.create_macroeconomicindicator(
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

@router.put("/macroeconomicindicators/{item_id}", response_model=Dict[str, Any])
def update_macroeconomicindicator(item_id: int, payload: MacroeconomicIndicatorUpdateSchema):
    """Update existing MacroeconomicIndicator record fields."""
    svc = MacroeconomicIndicatorService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_macroeconomicindicator(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MacroeconomicIndicator with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/macroeconomicindicators/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_macroeconomicindicator(item_id: int, hard: bool = Query(False)):
    """Delete MacroeconomicIndicator record (soft-delete by default)."""
    svc = MacroeconomicIndicatorService()
    ok = svc.delete_macroeconomicindicator(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MacroeconomicIndicator with ID {item_id} not found")
    return None

@router.get("/macroeconomicindicators/analytics/metrics", response_model=Dict[str, Any])
def get_macroeconomicindicator_metrics():
    """Calculate summary statistical KPIs for MacroeconomicIndicator collection."""
    svc = MacroeconomicIndicatorService()
    return svc.calculate_aggregate_metrics()

# ==================== DisruptiveThreatAlert Endpoints ====================
@router.get("/disruptivethreatalerts", response_model=List[Dict[str, Any]])
def list_disruptivethreatalerts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DisruptiveThreatAlert records with pagination and filtering."""
    svc = DisruptiveThreatAlertService()
    items = svc.list_disruptivethreatalerts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/disruptivethreatalerts/{item_id}", response_model=Dict[str, Any])
def get_disruptivethreatalert_by_id(item_id: int):
    """Retrieve detailed record for DisruptiveThreatAlert by ID."""
    svc = DisruptiveThreatAlertService()
    item = svc.get_disruptivethreatalert_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DisruptiveThreatAlert with ID {item_id} not found")
    return item.to_dict()

@router.post("/disruptivethreatalerts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_disruptivethreatalert(payload: DisruptiveThreatAlertCreateSchema):
    """Create new DisruptiveThreatAlert instance in enterprise repository."""
    svc = DisruptiveThreatAlertService()
    try:
        item = svc.create_disruptivethreatalert(
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

@router.put("/disruptivethreatalerts/{item_id}", response_model=Dict[str, Any])
def update_disruptivethreatalert(item_id: int, payload: DisruptiveThreatAlertUpdateSchema):
    """Update existing DisruptiveThreatAlert record fields."""
    svc = DisruptiveThreatAlertService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_disruptivethreatalert(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DisruptiveThreatAlert with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/disruptivethreatalerts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_disruptivethreatalert(item_id: int, hard: bool = Query(False)):
    """Delete DisruptiveThreatAlert record (soft-delete by default)."""
    svc = DisruptiveThreatAlertService()
    ok = svc.delete_disruptivethreatalert(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DisruptiveThreatAlert with ID {item_id} not found")
    return None

@router.get("/disruptivethreatalerts/analytics/metrics", response_model=Dict[str, Any])
def get_disruptivethreatalert_metrics():
    """Calculate summary statistical KPIs for DisruptiveThreatAlert collection."""
    svc = DisruptiveThreatAlertService()
    return svc.calculate_aggregate_metrics()

# ==================== AcquisitionTargetProfile Endpoints ====================
@router.get("/acquisitiontargetprofiles", response_model=List[Dict[str, Any]])
def list_acquisitiontargetprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AcquisitionTargetProfile records with pagination and filtering."""
    svc = AcquisitionTargetProfileService()
    items = svc.list_acquisitiontargetprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/acquisitiontargetprofiles/{item_id}", response_model=Dict[str, Any])
def get_acquisitiontargetprofile_by_id(item_id: int):
    """Retrieve detailed record for AcquisitionTargetProfile by ID."""
    svc = AcquisitionTargetProfileService()
    item = svc.get_acquisitiontargetprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AcquisitionTargetProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/acquisitiontargetprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_acquisitiontargetprofile(payload: AcquisitionTargetProfileCreateSchema):
    """Create new AcquisitionTargetProfile instance in enterprise repository."""
    svc = AcquisitionTargetProfileService()
    try:
        item = svc.create_acquisitiontargetprofile(
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

@router.put("/acquisitiontargetprofiles/{item_id}", response_model=Dict[str, Any])
def update_acquisitiontargetprofile(item_id: int, payload: AcquisitionTargetProfileUpdateSchema):
    """Update existing AcquisitionTargetProfile record fields."""
    svc = AcquisitionTargetProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_acquisitiontargetprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AcquisitionTargetProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/acquisitiontargetprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_acquisitiontargetprofile(item_id: int, hard: bool = Query(False)):
    """Delete AcquisitionTargetProfile record (soft-delete by default)."""
    svc = AcquisitionTargetProfileService()
    ok = svc.delete_acquisitiontargetprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AcquisitionTargetProfile with ID {item_id} not found")
    return None

@router.get("/acquisitiontargetprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_acquisitiontargetprofile_metrics():
    """Calculate summary statistical KPIs for AcquisitionTargetProfile collection."""
    svc = AcquisitionTargetProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== BrandPerceptionIndex Endpoints ====================
@router.get("/brandperceptionindexs", response_model=List[Dict[str, Any]])
def list_brandperceptionindexs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BrandPerceptionIndex records with pagination and filtering."""
    svc = BrandPerceptionIndexService()
    items = svc.list_brandperceptionindexs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/brandperceptionindexs/{item_id}", response_model=Dict[str, Any])
def get_brandperceptionindex_by_id(item_id: int):
    """Retrieve detailed record for BrandPerceptionIndex by ID."""
    svc = BrandPerceptionIndexService()
    item = svc.get_brandperceptionindex_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BrandPerceptionIndex with ID {item_id} not found")
    return item.to_dict()

@router.post("/brandperceptionindexs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_brandperceptionindex(payload: BrandPerceptionIndexCreateSchema):
    """Create new BrandPerceptionIndex instance in enterprise repository."""
    svc = BrandPerceptionIndexService()
    try:
        item = svc.create_brandperceptionindex(
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

@router.put("/brandperceptionindexs/{item_id}", response_model=Dict[str, Any])
def update_brandperceptionindex(item_id: int, payload: BrandPerceptionIndexUpdateSchema):
    """Update existing BrandPerceptionIndex record fields."""
    svc = BrandPerceptionIndexService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_brandperceptionindex(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BrandPerceptionIndex with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/brandperceptionindexs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_brandperceptionindex(item_id: int, hard: bool = Query(False)):
    """Delete BrandPerceptionIndex record (soft-delete by default)."""
    svc = BrandPerceptionIndexService()
    ok = svc.delete_brandperceptionindex(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BrandPerceptionIndex with ID {item_id} not found")
    return None

@router.get("/brandperceptionindexs/analytics/metrics", response_model=Dict[str, Any])
def get_brandperceptionindex_metrics():
    """Calculate summary statistical KPIs for BrandPerceptionIndex collection."""
    svc = BrandPerceptionIndexService()
    return svc.calculate_aggregate_metrics()

# ==================== ValueChainMapping Endpoints ====================
@router.get("/valuechainmappings", response_model=List[Dict[str, Any]])
def list_valuechainmappings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ValueChainMapping records with pagination and filtering."""
    svc = ValueChainMappingService()
    items = svc.list_valuechainmappings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/valuechainmappings/{item_id}", response_model=Dict[str, Any])
def get_valuechainmapping_by_id(item_id: int):
    """Retrieve detailed record for ValueChainMapping by ID."""
    svc = ValueChainMappingService()
    item = svc.get_valuechainmapping_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ValueChainMapping with ID {item_id} not found")
    return item.to_dict()

@router.post("/valuechainmappings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_valuechainmapping(payload: ValueChainMappingCreateSchema):
    """Create new ValueChainMapping instance in enterprise repository."""
    svc = ValueChainMappingService()
    try:
        item = svc.create_valuechainmapping(
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

@router.put("/valuechainmappings/{item_id}", response_model=Dict[str, Any])
def update_valuechainmapping(item_id: int, payload: ValueChainMappingUpdateSchema):
    """Update existing ValueChainMapping record fields."""
    svc = ValueChainMappingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_valuechainmapping(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ValueChainMapping with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/valuechainmappings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_valuechainmapping(item_id: int, hard: bool = Query(False)):
    """Delete ValueChainMapping record (soft-delete by default)."""
    svc = ValueChainMappingService()
    ok = svc.delete_valuechainmapping(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ValueChainMapping with ID {item_id} not found")
    return None

@router.get("/valuechainmappings/analytics/metrics", response_model=Dict[str, Any])
def get_valuechainmapping_metrics():
    """Calculate summary statistical KPIs for ValueChainMapping collection."""
    svc = ValueChainMappingService()
    return svc.calculate_aggregate_metrics()

# ==================== ScenarioSimulationModel Endpoints ====================
@router.get("/scenariosimulationmodels", response_model=List[Dict[str, Any]])
def list_scenariosimulationmodels(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ScenarioSimulationModel records with pagination and filtering."""
    svc = ScenarioSimulationModelService()
    items = svc.list_scenariosimulationmodels(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/scenariosimulationmodels/{item_id}", response_model=Dict[str, Any])
def get_scenariosimulationmodel_by_id(item_id: int):
    """Retrieve detailed record for ScenarioSimulationModel by ID."""
    svc = ScenarioSimulationModelService()
    item = svc.get_scenariosimulationmodel_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ScenarioSimulationModel with ID {item_id} not found")
    return item.to_dict()

@router.post("/scenariosimulationmodels", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_scenariosimulationmodel(payload: ScenarioSimulationModelCreateSchema):
    """Create new ScenarioSimulationModel instance in enterprise repository."""
    svc = ScenarioSimulationModelService()
    try:
        item = svc.create_scenariosimulationmodel(
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

@router.put("/scenariosimulationmodels/{item_id}", response_model=Dict[str, Any])
def update_scenariosimulationmodel(item_id: int, payload: ScenarioSimulationModelUpdateSchema):
    """Update existing ScenarioSimulationModel record fields."""
    svc = ScenarioSimulationModelService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_scenariosimulationmodel(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ScenarioSimulationModel with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/scenariosimulationmodels/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scenariosimulationmodel(item_id: int, hard: bool = Query(False)):
    """Delete ScenarioSimulationModel record (soft-delete by default)."""
    svc = ScenarioSimulationModelService()
    ok = svc.delete_scenariosimulationmodel(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ScenarioSimulationModel with ID {item_id} not found")
    return None

@router.get("/scenariosimulationmodels/analytics/metrics", response_model=Dict[str, Any])
def get_scenariosimulationmodel_metrics():
    """Calculate summary statistical KPIs for ScenarioSimulationModel collection."""
    svc = ScenarioSimulationModelService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutiveBriefingBrief Endpoints ====================
@router.get("/executivebriefingbriefs", response_model=List[Dict[str, Any]])
def list_executivebriefingbriefs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutiveBriefingBrief records with pagination and filtering."""
    svc = ExecutiveBriefingBriefService()
    items = svc.list_executivebriefingbriefs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executivebriefingbriefs/{item_id}", response_model=Dict[str, Any])
def get_executivebriefingbrief_by_id(item_id: int):
    """Retrieve detailed record for ExecutiveBriefingBrief by ID."""
    svc = ExecutiveBriefingBriefService()
    item = svc.get_executivebriefingbrief_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutiveBriefingBrief with ID {item_id} not found")
    return item.to_dict()

@router.post("/executivebriefingbriefs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executivebriefingbrief(payload: ExecutiveBriefingBriefCreateSchema):
    """Create new ExecutiveBriefingBrief instance in enterprise repository."""
    svc = ExecutiveBriefingBriefService()
    try:
        item = svc.create_executivebriefingbrief(
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

@router.put("/executivebriefingbriefs/{item_id}", response_model=Dict[str, Any])
def update_executivebriefingbrief(item_id: int, payload: ExecutiveBriefingBriefUpdateSchema):
    """Update existing ExecutiveBriefingBrief record fields."""
    svc = ExecutiveBriefingBriefService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executivebriefingbrief(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutiveBriefingBrief with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executivebriefingbriefs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executivebriefingbrief(item_id: int, hard: bool = Query(False)):
    """Delete ExecutiveBriefingBrief record (soft-delete by default)."""
    svc = ExecutiveBriefingBriefService()
    ok = svc.delete_executivebriefingbrief(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutiveBriefingBrief with ID {item_id} not found")
    return None

@router.get("/executivebriefingbriefs/analytics/metrics", response_model=Dict[str, Any])
def get_executivebriefingbrief_metrics():
    """Calculate summary statistical KPIs for ExecutiveBriefingBrief collection."""
    svc = ExecutiveBriefingBriefService()
    return svc.calculate_aggregate_metrics()

