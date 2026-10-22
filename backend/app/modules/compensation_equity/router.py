"""
Executive Compensation & Equity (ESOP) Engine - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    EquityPlanSchemeService,
    OptionGrantAgreementService,
    VestingScheduleRuleService,
    ExerciseNoticeOrderService,
    CapTableShareholderService,
    ShareRepurchaseBuybackService,
    AnnualBonusPoolService,
    LongTermIncentivePlanService,
    SalaryBenchmarkSurveyService,
    FairMarketValuation409AService,
    DividendsDistributionService,
    StockOptionCancellationService,
    Form16StatutoryFilingService,
    ExecutivePerformanceScoreService,
    EquityClawbackRuleService,
    SecondarySaleWindowService,
)
from .schemas import (
    EquityPlanSchemeCreateSchema, EquityPlanSchemeUpdateSchema, EquityPlanSchemeResponseSchema,
    OptionGrantAgreementCreateSchema, OptionGrantAgreementUpdateSchema, OptionGrantAgreementResponseSchema,
    VestingScheduleRuleCreateSchema, VestingScheduleRuleUpdateSchema, VestingScheduleRuleResponseSchema,
    ExerciseNoticeOrderCreateSchema, ExerciseNoticeOrderUpdateSchema, ExerciseNoticeOrderResponseSchema,
    CapTableShareholderCreateSchema, CapTableShareholderUpdateSchema, CapTableShareholderResponseSchema,
    ShareRepurchaseBuybackCreateSchema, ShareRepurchaseBuybackUpdateSchema, ShareRepurchaseBuybackResponseSchema,
    AnnualBonusPoolCreateSchema, AnnualBonusPoolUpdateSchema, AnnualBonusPoolResponseSchema,
    LongTermIncentivePlanCreateSchema, LongTermIncentivePlanUpdateSchema, LongTermIncentivePlanResponseSchema,
    SalaryBenchmarkSurveyCreateSchema, SalaryBenchmarkSurveyUpdateSchema, SalaryBenchmarkSurveyResponseSchema,
    FairMarketValuation409ACreateSchema, FairMarketValuation409AUpdateSchema, FairMarketValuation409AResponseSchema,
    DividendsDistributionCreateSchema, DividendsDistributionUpdateSchema, DividendsDistributionResponseSchema,
    StockOptionCancellationCreateSchema, StockOptionCancellationUpdateSchema, StockOptionCancellationResponseSchema,
    Form16StatutoryFilingCreateSchema, Form16StatutoryFilingUpdateSchema, Form16StatutoryFilingResponseSchema,
    ExecutivePerformanceScoreCreateSchema, ExecutivePerformanceScoreUpdateSchema, ExecutivePerformanceScoreResponseSchema,
    EquityClawbackRuleCreateSchema, EquityClawbackRuleUpdateSchema, EquityClawbackRuleResponseSchema,
    SecondarySaleWindowCreateSchema, SecondarySaleWindowUpdateSchema, SecondarySaleWindowResponseSchema,
)

router = APIRouter(prefix="/compensation_equity", tags=["Executive Compensation & Equity (ESOP) Engine"])

# ==================== EquityPlanScheme Endpoints ====================
@router.get("/equityplanschemes", response_model=List[Dict[str, Any]])
def list_equityplanschemes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EquityPlanScheme records with pagination and filtering."""
    svc = EquityPlanSchemeService()
    items = svc.list_equityplanschemes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/equityplanschemes/{item_id}", response_model=Dict[str, Any])
def get_equityplanscheme_by_id(item_id: int):
    """Retrieve detailed record for EquityPlanScheme by ID."""
    svc = EquityPlanSchemeService()
    item = svc.get_equityplanscheme_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EquityPlanScheme with ID {item_id} not found")
    return item.to_dict()

@router.post("/equityplanschemes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_equityplanscheme(payload: EquityPlanSchemeCreateSchema):
    """Create new EquityPlanScheme instance in enterprise repository."""
    svc = EquityPlanSchemeService()
    try:
        item = svc.create_equityplanscheme(
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

@router.put("/equityplanschemes/{item_id}", response_model=Dict[str, Any])
def update_equityplanscheme(item_id: int, payload: EquityPlanSchemeUpdateSchema):
    """Update existing EquityPlanScheme record fields."""
    svc = EquityPlanSchemeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_equityplanscheme(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EquityPlanScheme with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/equityplanschemes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equityplanscheme(item_id: int, hard: bool = Query(False)):
    """Delete EquityPlanScheme record (soft-delete by default)."""
    svc = EquityPlanSchemeService()
    ok = svc.delete_equityplanscheme(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EquityPlanScheme with ID {item_id} not found")
    return None

@router.get("/equityplanschemes/analytics/metrics", response_model=Dict[str, Any])
def get_equityplanscheme_metrics():
    """Calculate summary statistical KPIs for EquityPlanScheme collection."""
    svc = EquityPlanSchemeService()
    return svc.calculate_aggregate_metrics()

# ==================== OptionGrantAgreement Endpoints ====================
@router.get("/optiongrantagreements", response_model=List[Dict[str, Any]])
def list_optiongrantagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OptionGrantAgreement records with pagination and filtering."""
    svc = OptionGrantAgreementService()
    items = svc.list_optiongrantagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/optiongrantagreements/{item_id}", response_model=Dict[str, Any])
def get_optiongrantagreement_by_id(item_id: int):
    """Retrieve detailed record for OptionGrantAgreement by ID."""
    svc = OptionGrantAgreementService()
    item = svc.get_optiongrantagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OptionGrantAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/optiongrantagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_optiongrantagreement(payload: OptionGrantAgreementCreateSchema):
    """Create new OptionGrantAgreement instance in enterprise repository."""
    svc = OptionGrantAgreementService()
    try:
        item = svc.create_optiongrantagreement(
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

@router.put("/optiongrantagreements/{item_id}", response_model=Dict[str, Any])
def update_optiongrantagreement(item_id: int, payload: OptionGrantAgreementUpdateSchema):
    """Update existing OptionGrantAgreement record fields."""
    svc = OptionGrantAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_optiongrantagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OptionGrantAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/optiongrantagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_optiongrantagreement(item_id: int, hard: bool = Query(False)):
    """Delete OptionGrantAgreement record (soft-delete by default)."""
    svc = OptionGrantAgreementService()
    ok = svc.delete_optiongrantagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OptionGrantAgreement with ID {item_id} not found")
    return None

@router.get("/optiongrantagreements/analytics/metrics", response_model=Dict[str, Any])
def get_optiongrantagreement_metrics():
    """Calculate summary statistical KPIs for OptionGrantAgreement collection."""
    svc = OptionGrantAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== VestingScheduleRule Endpoints ====================
@router.get("/vestingschedulerules", response_model=List[Dict[str, Any]])
def list_vestingschedulerules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VestingScheduleRule records with pagination and filtering."""
    svc = VestingScheduleRuleService()
    items = svc.list_vestingschedulerules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vestingschedulerules/{item_id}", response_model=Dict[str, Any])
def get_vestingschedulerule_by_id(item_id: int):
    """Retrieve detailed record for VestingScheduleRule by ID."""
    svc = VestingScheduleRuleService()
    item = svc.get_vestingschedulerule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VestingScheduleRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/vestingschedulerules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vestingschedulerule(payload: VestingScheduleRuleCreateSchema):
    """Create new VestingScheduleRule instance in enterprise repository."""
    svc = VestingScheduleRuleService()
    try:
        item = svc.create_vestingschedulerule(
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

@router.put("/vestingschedulerules/{item_id}", response_model=Dict[str, Any])
def update_vestingschedulerule(item_id: int, payload: VestingScheduleRuleUpdateSchema):
    """Update existing VestingScheduleRule record fields."""
    svc = VestingScheduleRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vestingschedulerule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VestingScheduleRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vestingschedulerules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vestingschedulerule(item_id: int, hard: bool = Query(False)):
    """Delete VestingScheduleRule record (soft-delete by default)."""
    svc = VestingScheduleRuleService()
    ok = svc.delete_vestingschedulerule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VestingScheduleRule with ID {item_id} not found")
    return None

@router.get("/vestingschedulerules/analytics/metrics", response_model=Dict[str, Any])
def get_vestingschedulerule_metrics():
    """Calculate summary statistical KPIs for VestingScheduleRule collection."""
    svc = VestingScheduleRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== ExerciseNoticeOrder Endpoints ====================
@router.get("/exercisenoticeorders", response_model=List[Dict[str, Any]])
def list_exercisenoticeorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExerciseNoticeOrder records with pagination and filtering."""
    svc = ExerciseNoticeOrderService()
    items = svc.list_exercisenoticeorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/exercisenoticeorders/{item_id}", response_model=Dict[str, Any])
def get_exercisenoticeorder_by_id(item_id: int):
    """Retrieve detailed record for ExerciseNoticeOrder by ID."""
    svc = ExerciseNoticeOrderService()
    item = svc.get_exercisenoticeorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExerciseNoticeOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/exercisenoticeorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_exercisenoticeorder(payload: ExerciseNoticeOrderCreateSchema):
    """Create new ExerciseNoticeOrder instance in enterprise repository."""
    svc = ExerciseNoticeOrderService()
    try:
        item = svc.create_exercisenoticeorder(
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

@router.put("/exercisenoticeorders/{item_id}", response_model=Dict[str, Any])
def update_exercisenoticeorder(item_id: int, payload: ExerciseNoticeOrderUpdateSchema):
    """Update existing ExerciseNoticeOrder record fields."""
    svc = ExerciseNoticeOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_exercisenoticeorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExerciseNoticeOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/exercisenoticeorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exercisenoticeorder(item_id: int, hard: bool = Query(False)):
    """Delete ExerciseNoticeOrder record (soft-delete by default)."""
    svc = ExerciseNoticeOrderService()
    ok = svc.delete_exercisenoticeorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExerciseNoticeOrder with ID {item_id} not found")
    return None

@router.get("/exercisenoticeorders/analytics/metrics", response_model=Dict[str, Any])
def get_exercisenoticeorder_metrics():
    """Calculate summary statistical KPIs for ExerciseNoticeOrder collection."""
    svc = ExerciseNoticeOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== CapTableShareholder Endpoints ====================
@router.get("/captableshareholders", response_model=List[Dict[str, Any]])
def list_captableshareholders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CapTableShareholder records with pagination and filtering."""
    svc = CapTableShareholderService()
    items = svc.list_captableshareholders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/captableshareholders/{item_id}", response_model=Dict[str, Any])
def get_captableshareholder_by_id(item_id: int):
    """Retrieve detailed record for CapTableShareholder by ID."""
    svc = CapTableShareholderService()
    item = svc.get_captableshareholder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CapTableShareholder with ID {item_id} not found")
    return item.to_dict()

@router.post("/captableshareholders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_captableshareholder(payload: CapTableShareholderCreateSchema):
    """Create new CapTableShareholder instance in enterprise repository."""
    svc = CapTableShareholderService()
    try:
        item = svc.create_captableshareholder(
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

@router.put("/captableshareholders/{item_id}", response_model=Dict[str, Any])
def update_captableshareholder(item_id: int, payload: CapTableShareholderUpdateSchema):
    """Update existing CapTableShareholder record fields."""
    svc = CapTableShareholderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_captableshareholder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CapTableShareholder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/captableshareholders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_captableshareholder(item_id: int, hard: bool = Query(False)):
    """Delete CapTableShareholder record (soft-delete by default)."""
    svc = CapTableShareholderService()
    ok = svc.delete_captableshareholder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CapTableShareholder with ID {item_id} not found")
    return None

@router.get("/captableshareholders/analytics/metrics", response_model=Dict[str, Any])
def get_captableshareholder_metrics():
    """Calculate summary statistical KPIs for CapTableShareholder collection."""
    svc = CapTableShareholderService()
    return svc.calculate_aggregate_metrics()

# ==================== ShareRepurchaseBuyback Endpoints ====================
@router.get("/sharerepurchasebuybacks", response_model=List[Dict[str, Any]])
def list_sharerepurchasebuybacks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShareRepurchaseBuyback records with pagination and filtering."""
    svc = ShareRepurchaseBuybackService()
    items = svc.list_sharerepurchasebuybacks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sharerepurchasebuybacks/{item_id}", response_model=Dict[str, Any])
def get_sharerepurchasebuyback_by_id(item_id: int):
    """Retrieve detailed record for ShareRepurchaseBuyback by ID."""
    svc = ShareRepurchaseBuybackService()
    item = svc.get_sharerepurchasebuyback_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShareRepurchaseBuyback with ID {item_id} not found")
    return item.to_dict()

@router.post("/sharerepurchasebuybacks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sharerepurchasebuyback(payload: ShareRepurchaseBuybackCreateSchema):
    """Create new ShareRepurchaseBuyback instance in enterprise repository."""
    svc = ShareRepurchaseBuybackService()
    try:
        item = svc.create_sharerepurchasebuyback(
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

@router.put("/sharerepurchasebuybacks/{item_id}", response_model=Dict[str, Any])
def update_sharerepurchasebuyback(item_id: int, payload: ShareRepurchaseBuybackUpdateSchema):
    """Update existing ShareRepurchaseBuyback record fields."""
    svc = ShareRepurchaseBuybackService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sharerepurchasebuyback(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShareRepurchaseBuyback with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sharerepurchasebuybacks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sharerepurchasebuyback(item_id: int, hard: bool = Query(False)):
    """Delete ShareRepurchaseBuyback record (soft-delete by default)."""
    svc = ShareRepurchaseBuybackService()
    ok = svc.delete_sharerepurchasebuyback(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShareRepurchaseBuyback with ID {item_id} not found")
    return None

@router.get("/sharerepurchasebuybacks/analytics/metrics", response_model=Dict[str, Any])
def get_sharerepurchasebuyback_metrics():
    """Calculate summary statistical KPIs for ShareRepurchaseBuyback collection."""
    svc = ShareRepurchaseBuybackService()
    return svc.calculate_aggregate_metrics()

# ==================== AnnualBonusPool Endpoints ====================
@router.get("/annualbonuspools", response_model=List[Dict[str, Any]])
def list_annualbonuspools(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AnnualBonusPool records with pagination and filtering."""
    svc = AnnualBonusPoolService()
    items = svc.list_annualbonuspools(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/annualbonuspools/{item_id}", response_model=Dict[str, Any])
def get_annualbonuspool_by_id(item_id: int):
    """Retrieve detailed record for AnnualBonusPool by ID."""
    svc = AnnualBonusPoolService()
    item = svc.get_annualbonuspool_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AnnualBonusPool with ID {item_id} not found")
    return item.to_dict()

@router.post("/annualbonuspools", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_annualbonuspool(payload: AnnualBonusPoolCreateSchema):
    """Create new AnnualBonusPool instance in enterprise repository."""
    svc = AnnualBonusPoolService()
    try:
        item = svc.create_annualbonuspool(
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

@router.put("/annualbonuspools/{item_id}", response_model=Dict[str, Any])
def update_annualbonuspool(item_id: int, payload: AnnualBonusPoolUpdateSchema):
    """Update existing AnnualBonusPool record fields."""
    svc = AnnualBonusPoolService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_annualbonuspool(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AnnualBonusPool with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/annualbonuspools/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_annualbonuspool(item_id: int, hard: bool = Query(False)):
    """Delete AnnualBonusPool record (soft-delete by default)."""
    svc = AnnualBonusPoolService()
    ok = svc.delete_annualbonuspool(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AnnualBonusPool with ID {item_id} not found")
    return None

@router.get("/annualbonuspools/analytics/metrics", response_model=Dict[str, Any])
def get_annualbonuspool_metrics():
    """Calculate summary statistical KPIs for AnnualBonusPool collection."""
    svc = AnnualBonusPoolService()
    return svc.calculate_aggregate_metrics()

# ==================== LongTermIncentivePlan Endpoints ====================
@router.get("/longtermincentiveplans", response_model=List[Dict[str, Any]])
def list_longtermincentiveplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LongTermIncentivePlan records with pagination and filtering."""
    svc = LongTermIncentivePlanService()
    items = svc.list_longtermincentiveplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/longtermincentiveplans/{item_id}", response_model=Dict[str, Any])
def get_longtermincentiveplan_by_id(item_id: int):
    """Retrieve detailed record for LongTermIncentivePlan by ID."""
    svc = LongTermIncentivePlanService()
    item = svc.get_longtermincentiveplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LongTermIncentivePlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/longtermincentiveplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_longtermincentiveplan(payload: LongTermIncentivePlanCreateSchema):
    """Create new LongTermIncentivePlan instance in enterprise repository."""
    svc = LongTermIncentivePlanService()
    try:
        item = svc.create_longtermincentiveplan(
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

@router.put("/longtermincentiveplans/{item_id}", response_model=Dict[str, Any])
def update_longtermincentiveplan(item_id: int, payload: LongTermIncentivePlanUpdateSchema):
    """Update existing LongTermIncentivePlan record fields."""
    svc = LongTermIncentivePlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_longtermincentiveplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LongTermIncentivePlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/longtermincentiveplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_longtermincentiveplan(item_id: int, hard: bool = Query(False)):
    """Delete LongTermIncentivePlan record (soft-delete by default)."""
    svc = LongTermIncentivePlanService()
    ok = svc.delete_longtermincentiveplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LongTermIncentivePlan with ID {item_id} not found")
    return None

@router.get("/longtermincentiveplans/analytics/metrics", response_model=Dict[str, Any])
def get_longtermincentiveplan_metrics():
    """Calculate summary statistical KPIs for LongTermIncentivePlan collection."""
    svc = LongTermIncentivePlanService()
    return svc.calculate_aggregate_metrics()

# ==================== SalaryBenchmarkSurvey Endpoints ====================
@router.get("/salarybenchmarksurveys", response_model=List[Dict[str, Any]])
def list_salarybenchmarksurveys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SalaryBenchmarkSurvey records with pagination and filtering."""
    svc = SalaryBenchmarkSurveyService()
    items = svc.list_salarybenchmarksurveys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/salarybenchmarksurveys/{item_id}", response_model=Dict[str, Any])
def get_salarybenchmarksurvey_by_id(item_id: int):
    """Retrieve detailed record for SalaryBenchmarkSurvey by ID."""
    svc = SalaryBenchmarkSurveyService()
    item = svc.get_salarybenchmarksurvey_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SalaryBenchmarkSurvey with ID {item_id} not found")
    return item.to_dict()

@router.post("/salarybenchmarksurveys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_salarybenchmarksurvey(payload: SalaryBenchmarkSurveyCreateSchema):
    """Create new SalaryBenchmarkSurvey instance in enterprise repository."""
    svc = SalaryBenchmarkSurveyService()
    try:
        item = svc.create_salarybenchmarksurvey(
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

@router.put("/salarybenchmarksurveys/{item_id}", response_model=Dict[str, Any])
def update_salarybenchmarksurvey(item_id: int, payload: SalaryBenchmarkSurveyUpdateSchema):
    """Update existing SalaryBenchmarkSurvey record fields."""
    svc = SalaryBenchmarkSurveyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_salarybenchmarksurvey(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SalaryBenchmarkSurvey with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/salarybenchmarksurveys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_salarybenchmarksurvey(item_id: int, hard: bool = Query(False)):
    """Delete SalaryBenchmarkSurvey record (soft-delete by default)."""
    svc = SalaryBenchmarkSurveyService()
    ok = svc.delete_salarybenchmarksurvey(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SalaryBenchmarkSurvey with ID {item_id} not found")
    return None

@router.get("/salarybenchmarksurveys/analytics/metrics", response_model=Dict[str, Any])
def get_salarybenchmarksurvey_metrics():
    """Calculate summary statistical KPIs for SalaryBenchmarkSurvey collection."""
    svc = SalaryBenchmarkSurveyService()
    return svc.calculate_aggregate_metrics()

# ==================== FairMarketValuation409A Endpoints ====================
@router.get("/fairmarketvaluation409as", response_model=List[Dict[str, Any]])
def list_fairmarketvaluation409as(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FairMarketValuation409A records with pagination and filtering."""
    svc = FairMarketValuation409AService()
    items = svc.list_fairmarketvaluation409as(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fairmarketvaluation409as/{item_id}", response_model=Dict[str, Any])
def get_fairmarketvaluation409a_by_id(item_id: int):
    """Retrieve detailed record for FairMarketValuation409A by ID."""
    svc = FairMarketValuation409AService()
    item = svc.get_fairmarketvaluation409a_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FairMarketValuation409A with ID {item_id} not found")
    return item.to_dict()

@router.post("/fairmarketvaluation409as", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fairmarketvaluation409a(payload: FairMarketValuation409ACreateSchema):
    """Create new FairMarketValuation409A instance in enterprise repository."""
    svc = FairMarketValuation409AService()
    try:
        item = svc.create_fairmarketvaluation409a(
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

@router.put("/fairmarketvaluation409as/{item_id}", response_model=Dict[str, Any])
def update_fairmarketvaluation409a(item_id: int, payload: FairMarketValuation409AUpdateSchema):
    """Update existing FairMarketValuation409A record fields."""
    svc = FairMarketValuation409AService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fairmarketvaluation409a(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FairMarketValuation409A with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fairmarketvaluation409as/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fairmarketvaluation409a(item_id: int, hard: bool = Query(False)):
    """Delete FairMarketValuation409A record (soft-delete by default)."""
    svc = FairMarketValuation409AService()
    ok = svc.delete_fairmarketvaluation409a(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FairMarketValuation409A with ID {item_id} not found")
    return None

@router.get("/fairmarketvaluation409as/analytics/metrics", response_model=Dict[str, Any])
def get_fairmarketvaluation409a_metrics():
    """Calculate summary statistical KPIs for FairMarketValuation409A collection."""
    svc = FairMarketValuation409AService()
    return svc.calculate_aggregate_metrics()

# ==================== DividendsDistribution Endpoints ====================
@router.get("/dividendsdistributions", response_model=List[Dict[str, Any]])
def list_dividendsdistributions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DividendsDistribution records with pagination and filtering."""
    svc = DividendsDistributionService()
    items = svc.list_dividendsdistributions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dividendsdistributions/{item_id}", response_model=Dict[str, Any])
def get_dividendsdistribution_by_id(item_id: int):
    """Retrieve detailed record for DividendsDistribution by ID."""
    svc = DividendsDistributionService()
    item = svc.get_dividendsdistribution_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DividendsDistribution with ID {item_id} not found")
    return item.to_dict()

@router.post("/dividendsdistributions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dividendsdistribution(payload: DividendsDistributionCreateSchema):
    """Create new DividendsDistribution instance in enterprise repository."""
    svc = DividendsDistributionService()
    try:
        item = svc.create_dividendsdistribution(
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

@router.put("/dividendsdistributions/{item_id}", response_model=Dict[str, Any])
def update_dividendsdistribution(item_id: int, payload: DividendsDistributionUpdateSchema):
    """Update existing DividendsDistribution record fields."""
    svc = DividendsDistributionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dividendsdistribution(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DividendsDistribution with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dividendsdistributions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dividendsdistribution(item_id: int, hard: bool = Query(False)):
    """Delete DividendsDistribution record (soft-delete by default)."""
    svc = DividendsDistributionService()
    ok = svc.delete_dividendsdistribution(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DividendsDistribution with ID {item_id} not found")
    return None

@router.get("/dividendsdistributions/analytics/metrics", response_model=Dict[str, Any])
def get_dividendsdistribution_metrics():
    """Calculate summary statistical KPIs for DividendsDistribution collection."""
    svc = DividendsDistributionService()
    return svc.calculate_aggregate_metrics()

# ==================== StockOptionCancellation Endpoints ====================
@router.get("/stockoptioncancellations", response_model=List[Dict[str, Any]])
def list_stockoptioncancellations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StockOptionCancellation records with pagination and filtering."""
    svc = StockOptionCancellationService()
    items = svc.list_stockoptioncancellations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/stockoptioncancellations/{item_id}", response_model=Dict[str, Any])
def get_stockoptioncancellation_by_id(item_id: int):
    """Retrieve detailed record for StockOptionCancellation by ID."""
    svc = StockOptionCancellationService()
    item = svc.get_stockoptioncancellation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StockOptionCancellation with ID {item_id} not found")
    return item.to_dict()

@router.post("/stockoptioncancellations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_stockoptioncancellation(payload: StockOptionCancellationCreateSchema):
    """Create new StockOptionCancellation instance in enterprise repository."""
    svc = StockOptionCancellationService()
    try:
        item = svc.create_stockoptioncancellation(
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

@router.put("/stockoptioncancellations/{item_id}", response_model=Dict[str, Any])
def update_stockoptioncancellation(item_id: int, payload: StockOptionCancellationUpdateSchema):
    """Update existing StockOptionCancellation record fields."""
    svc = StockOptionCancellationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_stockoptioncancellation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StockOptionCancellation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/stockoptioncancellations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stockoptioncancellation(item_id: int, hard: bool = Query(False)):
    """Delete StockOptionCancellation record (soft-delete by default)."""
    svc = StockOptionCancellationService()
    ok = svc.delete_stockoptioncancellation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StockOptionCancellation with ID {item_id} not found")
    return None

@router.get("/stockoptioncancellations/analytics/metrics", response_model=Dict[str, Any])
def get_stockoptioncancellation_metrics():
    """Calculate summary statistical KPIs for StockOptionCancellation collection."""
    svc = StockOptionCancellationService()
    return svc.calculate_aggregate_metrics()

# ==================== Form16StatutoryFiling Endpoints ====================
@router.get("/form16statutoryfilings", response_model=List[Dict[str, Any]])
def list_form16statutoryfilings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Form16StatutoryFiling records with pagination and filtering."""
    svc = Form16StatutoryFilingService()
    items = svc.list_form16statutoryfilings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/form16statutoryfilings/{item_id}", response_model=Dict[str, Any])
def get_form16statutoryfiling_by_id(item_id: int):
    """Retrieve detailed record for Form16StatutoryFiling by ID."""
    svc = Form16StatutoryFilingService()
    item = svc.get_form16statutoryfiling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Form16StatutoryFiling with ID {item_id} not found")
    return item.to_dict()

@router.post("/form16statutoryfilings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_form16statutoryfiling(payload: Form16StatutoryFilingCreateSchema):
    """Create new Form16StatutoryFiling instance in enterprise repository."""
    svc = Form16StatutoryFilingService()
    try:
        item = svc.create_form16statutoryfiling(
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

@router.put("/form16statutoryfilings/{item_id}", response_model=Dict[str, Any])
def update_form16statutoryfiling(item_id: int, payload: Form16StatutoryFilingUpdateSchema):
    """Update existing Form16StatutoryFiling record fields."""
    svc = Form16StatutoryFilingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_form16statutoryfiling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Form16StatutoryFiling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/form16statutoryfilings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_form16statutoryfiling(item_id: int, hard: bool = Query(False)):
    """Delete Form16StatutoryFiling record (soft-delete by default)."""
    svc = Form16StatutoryFilingService()
    ok = svc.delete_form16statutoryfiling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Form16StatutoryFiling with ID {item_id} not found")
    return None

@router.get("/form16statutoryfilings/analytics/metrics", response_model=Dict[str, Any])
def get_form16statutoryfiling_metrics():
    """Calculate summary statistical KPIs for Form16StatutoryFiling collection."""
    svc = Form16StatutoryFilingService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutivePerformanceScore Endpoints ====================
@router.get("/executiveperformancescores", response_model=List[Dict[str, Any]])
def list_executiveperformancescores(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutivePerformanceScore records with pagination and filtering."""
    svc = ExecutivePerformanceScoreService()
    items = svc.list_executiveperformancescores(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executiveperformancescores/{item_id}", response_model=Dict[str, Any])
def get_executiveperformancescore_by_id(item_id: int):
    """Retrieve detailed record for ExecutivePerformanceScore by ID."""
    svc = ExecutivePerformanceScoreService()
    item = svc.get_executiveperformancescore_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutivePerformanceScore with ID {item_id} not found")
    return item.to_dict()

@router.post("/executiveperformancescores", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executiveperformancescore(payload: ExecutivePerformanceScoreCreateSchema):
    """Create new ExecutivePerformanceScore instance in enterprise repository."""
    svc = ExecutivePerformanceScoreService()
    try:
        item = svc.create_executiveperformancescore(
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

@router.put("/executiveperformancescores/{item_id}", response_model=Dict[str, Any])
def update_executiveperformancescore(item_id: int, payload: ExecutivePerformanceScoreUpdateSchema):
    """Update existing ExecutivePerformanceScore record fields."""
    svc = ExecutivePerformanceScoreService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executiveperformancescore(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutivePerformanceScore with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executiveperformancescores/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executiveperformancescore(item_id: int, hard: bool = Query(False)):
    """Delete ExecutivePerformanceScore record (soft-delete by default)."""
    svc = ExecutivePerformanceScoreService()
    ok = svc.delete_executiveperformancescore(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutivePerformanceScore with ID {item_id} not found")
    return None

@router.get("/executiveperformancescores/analytics/metrics", response_model=Dict[str, Any])
def get_executiveperformancescore_metrics():
    """Calculate summary statistical KPIs for ExecutivePerformanceScore collection."""
    svc = ExecutivePerformanceScoreService()
    return svc.calculate_aggregate_metrics()

# ==================== EquityClawbackRule Endpoints ====================
@router.get("/equityclawbackrules", response_model=List[Dict[str, Any]])
def list_equityclawbackrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EquityClawbackRule records with pagination and filtering."""
    svc = EquityClawbackRuleService()
    items = svc.list_equityclawbackrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/equityclawbackrules/{item_id}", response_model=Dict[str, Any])
def get_equityclawbackrule_by_id(item_id: int):
    """Retrieve detailed record for EquityClawbackRule by ID."""
    svc = EquityClawbackRuleService()
    item = svc.get_equityclawbackrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EquityClawbackRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/equityclawbackrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_equityclawbackrule(payload: EquityClawbackRuleCreateSchema):
    """Create new EquityClawbackRule instance in enterprise repository."""
    svc = EquityClawbackRuleService()
    try:
        item = svc.create_equityclawbackrule(
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

@router.put("/equityclawbackrules/{item_id}", response_model=Dict[str, Any])
def update_equityclawbackrule(item_id: int, payload: EquityClawbackRuleUpdateSchema):
    """Update existing EquityClawbackRule record fields."""
    svc = EquityClawbackRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_equityclawbackrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EquityClawbackRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/equityclawbackrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equityclawbackrule(item_id: int, hard: bool = Query(False)):
    """Delete EquityClawbackRule record (soft-delete by default)."""
    svc = EquityClawbackRuleService()
    ok = svc.delete_equityclawbackrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EquityClawbackRule with ID {item_id} not found")
    return None

@router.get("/equityclawbackrules/analytics/metrics", response_model=Dict[str, Any])
def get_equityclawbackrule_metrics():
    """Calculate summary statistical KPIs for EquityClawbackRule collection."""
    svc = EquityClawbackRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== SecondarySaleWindow Endpoints ====================
@router.get("/secondarysalewindows", response_model=List[Dict[str, Any]])
def list_secondarysalewindows(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SecondarySaleWindow records with pagination and filtering."""
    svc = SecondarySaleWindowService()
    items = svc.list_secondarysalewindows(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/secondarysalewindows/{item_id}", response_model=Dict[str, Any])
def get_secondarysalewindow_by_id(item_id: int):
    """Retrieve detailed record for SecondarySaleWindow by ID."""
    svc = SecondarySaleWindowService()
    item = svc.get_secondarysalewindow_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SecondarySaleWindow with ID {item_id} not found")
    return item.to_dict()

@router.post("/secondarysalewindows", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_secondarysalewindow(payload: SecondarySaleWindowCreateSchema):
    """Create new SecondarySaleWindow instance in enterprise repository."""
    svc = SecondarySaleWindowService()
    try:
        item = svc.create_secondarysalewindow(
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

@router.put("/secondarysalewindows/{item_id}", response_model=Dict[str, Any])
def update_secondarysalewindow(item_id: int, payload: SecondarySaleWindowUpdateSchema):
    """Update existing SecondarySaleWindow record fields."""
    svc = SecondarySaleWindowService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_secondarysalewindow(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SecondarySaleWindow with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/secondarysalewindows/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_secondarysalewindow(item_id: int, hard: bool = Query(False)):
    """Delete SecondarySaleWindow record (soft-delete by default)."""
    svc = SecondarySaleWindowService()
    ok = svc.delete_secondarysalewindow(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SecondarySaleWindow with ID {item_id} not found")
    return None

@router.get("/secondarysalewindows/analytics/metrics", response_model=Dict[str, Any])
def get_secondarysalewindow_metrics():
    """Calculate summary statistical KPIs for SecondarySaleWindow collection."""
    svc = SecondarySaleWindowService()
    return svc.calculate_aggregate_metrics()

