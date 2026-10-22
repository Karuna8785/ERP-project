"""
Multi-Entity Financial Consolidation & Reporting - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ConsolidationEntityGroupService,
    IntercompanyEliminationEntryService,
    ConsolidatedTrialBalanceService,
    CurrencyTranslationRateService,
    MinorityInterestShareService,
    JointVentureEquityShareService,
    FinancialAdjustmentVoucherService,
    GoodwillImpairmentScheduleService,
    SegmentalReportingUnitService,
    ConsolidatedCashFlowService,
    StatutoryBalanceSheetService,
    ConsolidatedIncomeStatementService,
    AuditTrailEliminationService,
    TaxProvisioningConsolidatedService,
    FinancialClosingChecklistService,
    ExecutiveBoardFinancialReportService,
)
from .schemas import (
    ConsolidationEntityGroupCreateSchema, ConsolidationEntityGroupUpdateSchema, ConsolidationEntityGroupResponseSchema,
    IntercompanyEliminationEntryCreateSchema, IntercompanyEliminationEntryUpdateSchema, IntercompanyEliminationEntryResponseSchema,
    ConsolidatedTrialBalanceCreateSchema, ConsolidatedTrialBalanceUpdateSchema, ConsolidatedTrialBalanceResponseSchema,
    CurrencyTranslationRateCreateSchema, CurrencyTranslationRateUpdateSchema, CurrencyTranslationRateResponseSchema,
    MinorityInterestShareCreateSchema, MinorityInterestShareUpdateSchema, MinorityInterestShareResponseSchema,
    JointVentureEquityShareCreateSchema, JointVentureEquityShareUpdateSchema, JointVentureEquityShareResponseSchema,
    FinancialAdjustmentVoucherCreateSchema, FinancialAdjustmentVoucherUpdateSchema, FinancialAdjustmentVoucherResponseSchema,
    GoodwillImpairmentScheduleCreateSchema, GoodwillImpairmentScheduleUpdateSchema, GoodwillImpairmentScheduleResponseSchema,
    SegmentalReportingUnitCreateSchema, SegmentalReportingUnitUpdateSchema, SegmentalReportingUnitResponseSchema,
    ConsolidatedCashFlowCreateSchema, ConsolidatedCashFlowUpdateSchema, ConsolidatedCashFlowResponseSchema,
    StatutoryBalanceSheetCreateSchema, StatutoryBalanceSheetUpdateSchema, StatutoryBalanceSheetResponseSchema,
    ConsolidatedIncomeStatementCreateSchema, ConsolidatedIncomeStatementUpdateSchema, ConsolidatedIncomeStatementResponseSchema,
    AuditTrailEliminationCreateSchema, AuditTrailEliminationUpdateSchema, AuditTrailEliminationResponseSchema,
    TaxProvisioningConsolidatedCreateSchema, TaxProvisioningConsolidatedUpdateSchema, TaxProvisioningConsolidatedResponseSchema,
    FinancialClosingChecklistCreateSchema, FinancialClosingChecklistUpdateSchema, FinancialClosingChecklistResponseSchema,
    ExecutiveBoardFinancialReportCreateSchema, ExecutiveBoardFinancialReportUpdateSchema, ExecutiveBoardFinancialReportResponseSchema,
)

router = APIRouter(prefix="/financial_consolidation", tags=["Multi-Entity Financial Consolidation & Reporting"])

# ==================== ConsolidationEntityGroup Endpoints ====================
@router.get("/consolidationentitygroups", response_model=List[Dict[str, Any]])
def list_consolidationentitygroups(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ConsolidationEntityGroup records with pagination and filtering."""
    svc = ConsolidationEntityGroupService()
    items = svc.list_consolidationentitygroups(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/consolidationentitygroups/{item_id}", response_model=Dict[str, Any])
def get_consolidationentitygroup_by_id(item_id: int):
    """Retrieve detailed record for ConsolidationEntityGroup by ID."""
    svc = ConsolidationEntityGroupService()
    item = svc.get_consolidationentitygroup_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ConsolidationEntityGroup with ID {item_id} not found")
    return item.to_dict()

@router.post("/consolidationentitygroups", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_consolidationentitygroup(payload: ConsolidationEntityGroupCreateSchema):
    """Create new ConsolidationEntityGroup instance in enterprise repository."""
    svc = ConsolidationEntityGroupService()
    try:
        item = svc.create_consolidationentitygroup(
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

@router.put("/consolidationentitygroups/{item_id}", response_model=Dict[str, Any])
def update_consolidationentitygroup(item_id: int, payload: ConsolidationEntityGroupUpdateSchema):
    """Update existing ConsolidationEntityGroup record fields."""
    svc = ConsolidationEntityGroupService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_consolidationentitygroup(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ConsolidationEntityGroup with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/consolidationentitygroups/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_consolidationentitygroup(item_id: int, hard: bool = Query(False)):
    """Delete ConsolidationEntityGroup record (soft-delete by default)."""
    svc = ConsolidationEntityGroupService()
    ok = svc.delete_consolidationentitygroup(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ConsolidationEntityGroup with ID {item_id} not found")
    return None

@router.get("/consolidationentitygroups/analytics/metrics", response_model=Dict[str, Any])
def get_consolidationentitygroup_metrics():
    """Calculate summary statistical KPIs for ConsolidationEntityGroup collection."""
    svc = ConsolidationEntityGroupService()
    return svc.calculate_aggregate_metrics()

# ==================== IntercompanyEliminationEntry Endpoints ====================
@router.get("/intercompanyeliminationentrys", response_model=List[Dict[str, Any]])
def list_intercompanyeliminationentrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IntercompanyEliminationEntry records with pagination and filtering."""
    svc = IntercompanyEliminationEntryService()
    items = svc.list_intercompanyeliminationentrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/intercompanyeliminationentrys/{item_id}", response_model=Dict[str, Any])
def get_intercompanyeliminationentry_by_id(item_id: int):
    """Retrieve detailed record for IntercompanyEliminationEntry by ID."""
    svc = IntercompanyEliminationEntryService()
    item = svc.get_intercompanyeliminationentry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IntercompanyEliminationEntry with ID {item_id} not found")
    return item.to_dict()

@router.post("/intercompanyeliminationentrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_intercompanyeliminationentry(payload: IntercompanyEliminationEntryCreateSchema):
    """Create new IntercompanyEliminationEntry instance in enterprise repository."""
    svc = IntercompanyEliminationEntryService()
    try:
        item = svc.create_intercompanyeliminationentry(
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

@router.put("/intercompanyeliminationentrys/{item_id}", response_model=Dict[str, Any])
def update_intercompanyeliminationentry(item_id: int, payload: IntercompanyEliminationEntryUpdateSchema):
    """Update existing IntercompanyEliminationEntry record fields."""
    svc = IntercompanyEliminationEntryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_intercompanyeliminationentry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IntercompanyEliminationEntry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/intercompanyeliminationentrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_intercompanyeliminationentry(item_id: int, hard: bool = Query(False)):
    """Delete IntercompanyEliminationEntry record (soft-delete by default)."""
    svc = IntercompanyEliminationEntryService()
    ok = svc.delete_intercompanyeliminationentry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IntercompanyEliminationEntry with ID {item_id} not found")
    return None

@router.get("/intercompanyeliminationentrys/analytics/metrics", response_model=Dict[str, Any])
def get_intercompanyeliminationentry_metrics():
    """Calculate summary statistical KPIs for IntercompanyEliminationEntry collection."""
    svc = IntercompanyEliminationEntryService()
    return svc.calculate_aggregate_metrics()

# ==================== ConsolidatedTrialBalance Endpoints ====================
@router.get("/consolidatedtrialbalances", response_model=List[Dict[str, Any]])
def list_consolidatedtrialbalances(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ConsolidatedTrialBalance records with pagination and filtering."""
    svc = ConsolidatedTrialBalanceService()
    items = svc.list_consolidatedtrialbalances(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/consolidatedtrialbalances/{item_id}", response_model=Dict[str, Any])
def get_consolidatedtrialbalance_by_id(item_id: int):
    """Retrieve detailed record for ConsolidatedTrialBalance by ID."""
    svc = ConsolidatedTrialBalanceService()
    item = svc.get_consolidatedtrialbalance_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ConsolidatedTrialBalance with ID {item_id} not found")
    return item.to_dict()

@router.post("/consolidatedtrialbalances", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_consolidatedtrialbalance(payload: ConsolidatedTrialBalanceCreateSchema):
    """Create new ConsolidatedTrialBalance instance in enterprise repository."""
    svc = ConsolidatedTrialBalanceService()
    try:
        item = svc.create_consolidatedtrialbalance(
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

@router.put("/consolidatedtrialbalances/{item_id}", response_model=Dict[str, Any])
def update_consolidatedtrialbalance(item_id: int, payload: ConsolidatedTrialBalanceUpdateSchema):
    """Update existing ConsolidatedTrialBalance record fields."""
    svc = ConsolidatedTrialBalanceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_consolidatedtrialbalance(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ConsolidatedTrialBalance with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/consolidatedtrialbalances/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_consolidatedtrialbalance(item_id: int, hard: bool = Query(False)):
    """Delete ConsolidatedTrialBalance record (soft-delete by default)."""
    svc = ConsolidatedTrialBalanceService()
    ok = svc.delete_consolidatedtrialbalance(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ConsolidatedTrialBalance with ID {item_id} not found")
    return None

@router.get("/consolidatedtrialbalances/analytics/metrics", response_model=Dict[str, Any])
def get_consolidatedtrialbalance_metrics():
    """Calculate summary statistical KPIs for ConsolidatedTrialBalance collection."""
    svc = ConsolidatedTrialBalanceService()
    return svc.calculate_aggregate_metrics()

# ==================== CurrencyTranslationRate Endpoints ====================
@router.get("/currencytranslationrates", response_model=List[Dict[str, Any]])
def list_currencytranslationrates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CurrencyTranslationRate records with pagination and filtering."""
    svc = CurrencyTranslationRateService()
    items = svc.list_currencytranslationrates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/currencytranslationrates/{item_id}", response_model=Dict[str, Any])
def get_currencytranslationrate_by_id(item_id: int):
    """Retrieve detailed record for CurrencyTranslationRate by ID."""
    svc = CurrencyTranslationRateService()
    item = svc.get_currencytranslationrate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CurrencyTranslationRate with ID {item_id} not found")
    return item.to_dict()

@router.post("/currencytranslationrates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_currencytranslationrate(payload: CurrencyTranslationRateCreateSchema):
    """Create new CurrencyTranslationRate instance in enterprise repository."""
    svc = CurrencyTranslationRateService()
    try:
        item = svc.create_currencytranslationrate(
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

@router.put("/currencytranslationrates/{item_id}", response_model=Dict[str, Any])
def update_currencytranslationrate(item_id: int, payload: CurrencyTranslationRateUpdateSchema):
    """Update existing CurrencyTranslationRate record fields."""
    svc = CurrencyTranslationRateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_currencytranslationrate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CurrencyTranslationRate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/currencytranslationrates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_currencytranslationrate(item_id: int, hard: bool = Query(False)):
    """Delete CurrencyTranslationRate record (soft-delete by default)."""
    svc = CurrencyTranslationRateService()
    ok = svc.delete_currencytranslationrate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CurrencyTranslationRate with ID {item_id} not found")
    return None

@router.get("/currencytranslationrates/analytics/metrics", response_model=Dict[str, Any])
def get_currencytranslationrate_metrics():
    """Calculate summary statistical KPIs for CurrencyTranslationRate collection."""
    svc = CurrencyTranslationRateService()
    return svc.calculate_aggregate_metrics()

# ==================== MinorityInterestShare Endpoints ====================
@router.get("/minorityinterestshares", response_model=List[Dict[str, Any]])
def list_minorityinterestshares(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MinorityInterestShare records with pagination and filtering."""
    svc = MinorityInterestShareService()
    items = svc.list_minorityinterestshares(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/minorityinterestshares/{item_id}", response_model=Dict[str, Any])
def get_minorityinterestshare_by_id(item_id: int):
    """Retrieve detailed record for MinorityInterestShare by ID."""
    svc = MinorityInterestShareService()
    item = svc.get_minorityinterestshare_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MinorityInterestShare with ID {item_id} not found")
    return item.to_dict()

@router.post("/minorityinterestshares", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_minorityinterestshare(payload: MinorityInterestShareCreateSchema):
    """Create new MinorityInterestShare instance in enterprise repository."""
    svc = MinorityInterestShareService()
    try:
        item = svc.create_minorityinterestshare(
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

@router.put("/minorityinterestshares/{item_id}", response_model=Dict[str, Any])
def update_minorityinterestshare(item_id: int, payload: MinorityInterestShareUpdateSchema):
    """Update existing MinorityInterestShare record fields."""
    svc = MinorityInterestShareService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_minorityinterestshare(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MinorityInterestShare with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/minorityinterestshares/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_minorityinterestshare(item_id: int, hard: bool = Query(False)):
    """Delete MinorityInterestShare record (soft-delete by default)."""
    svc = MinorityInterestShareService()
    ok = svc.delete_minorityinterestshare(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MinorityInterestShare with ID {item_id} not found")
    return None

@router.get("/minorityinterestshares/analytics/metrics", response_model=Dict[str, Any])
def get_minorityinterestshare_metrics():
    """Calculate summary statistical KPIs for MinorityInterestShare collection."""
    svc = MinorityInterestShareService()
    return svc.calculate_aggregate_metrics()

# ==================== JointVentureEquityShare Endpoints ====================
@router.get("/jointventureequityshares", response_model=List[Dict[str, Any]])
def list_jointventureequityshares(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List JointVentureEquityShare records with pagination and filtering."""
    svc = JointVentureEquityShareService()
    items = svc.list_jointventureequityshares(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/jointventureequityshares/{item_id}", response_model=Dict[str, Any])
def get_jointventureequityshare_by_id(item_id: int):
    """Retrieve detailed record for JointVentureEquityShare by ID."""
    svc = JointVentureEquityShareService()
    item = svc.get_jointventureequityshare_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"JointVentureEquityShare with ID {item_id} not found")
    return item.to_dict()

@router.post("/jointventureequityshares", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_jointventureequityshare(payload: JointVentureEquityShareCreateSchema):
    """Create new JointVentureEquityShare instance in enterprise repository."""
    svc = JointVentureEquityShareService()
    try:
        item = svc.create_jointventureequityshare(
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

@router.put("/jointventureequityshares/{item_id}", response_model=Dict[str, Any])
def update_jointventureequityshare(item_id: int, payload: JointVentureEquityShareUpdateSchema):
    """Update existing JointVentureEquityShare record fields."""
    svc = JointVentureEquityShareService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_jointventureequityshare(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"JointVentureEquityShare with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/jointventureequityshares/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_jointventureequityshare(item_id: int, hard: bool = Query(False)):
    """Delete JointVentureEquityShare record (soft-delete by default)."""
    svc = JointVentureEquityShareService()
    ok = svc.delete_jointventureequityshare(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"JointVentureEquityShare with ID {item_id} not found")
    return None

@router.get("/jointventureequityshares/analytics/metrics", response_model=Dict[str, Any])
def get_jointventureequityshare_metrics():
    """Calculate summary statistical KPIs for JointVentureEquityShare collection."""
    svc = JointVentureEquityShareService()
    return svc.calculate_aggregate_metrics()

# ==================== FinancialAdjustmentVoucher Endpoints ====================
@router.get("/financialadjustmentvouchers", response_model=List[Dict[str, Any]])
def list_financialadjustmentvouchers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FinancialAdjustmentVoucher records with pagination and filtering."""
    svc = FinancialAdjustmentVoucherService()
    items = svc.list_financialadjustmentvouchers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/financialadjustmentvouchers/{item_id}", response_model=Dict[str, Any])
def get_financialadjustmentvoucher_by_id(item_id: int):
    """Retrieve detailed record for FinancialAdjustmentVoucher by ID."""
    svc = FinancialAdjustmentVoucherService()
    item = svc.get_financialadjustmentvoucher_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FinancialAdjustmentVoucher with ID {item_id} not found")
    return item.to_dict()

@router.post("/financialadjustmentvouchers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_financialadjustmentvoucher(payload: FinancialAdjustmentVoucherCreateSchema):
    """Create new FinancialAdjustmentVoucher instance in enterprise repository."""
    svc = FinancialAdjustmentVoucherService()
    try:
        item = svc.create_financialadjustmentvoucher(
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

@router.put("/financialadjustmentvouchers/{item_id}", response_model=Dict[str, Any])
def update_financialadjustmentvoucher(item_id: int, payload: FinancialAdjustmentVoucherUpdateSchema):
    """Update existing FinancialAdjustmentVoucher record fields."""
    svc = FinancialAdjustmentVoucherService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_financialadjustmentvoucher(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FinancialAdjustmentVoucher with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/financialadjustmentvouchers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_financialadjustmentvoucher(item_id: int, hard: bool = Query(False)):
    """Delete FinancialAdjustmentVoucher record (soft-delete by default)."""
    svc = FinancialAdjustmentVoucherService()
    ok = svc.delete_financialadjustmentvoucher(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FinancialAdjustmentVoucher with ID {item_id} not found")
    return None

@router.get("/financialadjustmentvouchers/analytics/metrics", response_model=Dict[str, Any])
def get_financialadjustmentvoucher_metrics():
    """Calculate summary statistical KPIs for FinancialAdjustmentVoucher collection."""
    svc = FinancialAdjustmentVoucherService()
    return svc.calculate_aggregate_metrics()

# ==================== GoodwillImpairmentSchedule Endpoints ====================
@router.get("/goodwillimpairmentschedules", response_model=List[Dict[str, Any]])
def list_goodwillimpairmentschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GoodwillImpairmentSchedule records with pagination and filtering."""
    svc = GoodwillImpairmentScheduleService()
    items = svc.list_goodwillimpairmentschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/goodwillimpairmentschedules/{item_id}", response_model=Dict[str, Any])
def get_goodwillimpairmentschedule_by_id(item_id: int):
    """Retrieve detailed record for GoodwillImpairmentSchedule by ID."""
    svc = GoodwillImpairmentScheduleService()
    item = svc.get_goodwillimpairmentschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GoodwillImpairmentSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/goodwillimpairmentschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_goodwillimpairmentschedule(payload: GoodwillImpairmentScheduleCreateSchema):
    """Create new GoodwillImpairmentSchedule instance in enterprise repository."""
    svc = GoodwillImpairmentScheduleService()
    try:
        item = svc.create_goodwillimpairmentschedule(
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

@router.put("/goodwillimpairmentschedules/{item_id}", response_model=Dict[str, Any])
def update_goodwillimpairmentschedule(item_id: int, payload: GoodwillImpairmentScheduleUpdateSchema):
    """Update existing GoodwillImpairmentSchedule record fields."""
    svc = GoodwillImpairmentScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_goodwillimpairmentschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GoodwillImpairmentSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/goodwillimpairmentschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_goodwillimpairmentschedule(item_id: int, hard: bool = Query(False)):
    """Delete GoodwillImpairmentSchedule record (soft-delete by default)."""
    svc = GoodwillImpairmentScheduleService()
    ok = svc.delete_goodwillimpairmentschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GoodwillImpairmentSchedule with ID {item_id} not found")
    return None

@router.get("/goodwillimpairmentschedules/analytics/metrics", response_model=Dict[str, Any])
def get_goodwillimpairmentschedule_metrics():
    """Calculate summary statistical KPIs for GoodwillImpairmentSchedule collection."""
    svc = GoodwillImpairmentScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== SegmentalReportingUnit Endpoints ====================
@router.get("/segmentalreportingunits", response_model=List[Dict[str, Any]])
def list_segmentalreportingunits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SegmentalReportingUnit records with pagination and filtering."""
    svc = SegmentalReportingUnitService()
    items = svc.list_segmentalreportingunits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/segmentalreportingunits/{item_id}", response_model=Dict[str, Any])
def get_segmentalreportingunit_by_id(item_id: int):
    """Retrieve detailed record for SegmentalReportingUnit by ID."""
    svc = SegmentalReportingUnitService()
    item = svc.get_segmentalreportingunit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SegmentalReportingUnit with ID {item_id} not found")
    return item.to_dict()

@router.post("/segmentalreportingunits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_segmentalreportingunit(payload: SegmentalReportingUnitCreateSchema):
    """Create new SegmentalReportingUnit instance in enterprise repository."""
    svc = SegmentalReportingUnitService()
    try:
        item = svc.create_segmentalreportingunit(
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

@router.put("/segmentalreportingunits/{item_id}", response_model=Dict[str, Any])
def update_segmentalreportingunit(item_id: int, payload: SegmentalReportingUnitUpdateSchema):
    """Update existing SegmentalReportingUnit record fields."""
    svc = SegmentalReportingUnitService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_segmentalreportingunit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SegmentalReportingUnit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/segmentalreportingunits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_segmentalreportingunit(item_id: int, hard: bool = Query(False)):
    """Delete SegmentalReportingUnit record (soft-delete by default)."""
    svc = SegmentalReportingUnitService()
    ok = svc.delete_segmentalreportingunit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SegmentalReportingUnit with ID {item_id} not found")
    return None

@router.get("/segmentalreportingunits/analytics/metrics", response_model=Dict[str, Any])
def get_segmentalreportingunit_metrics():
    """Calculate summary statistical KPIs for SegmentalReportingUnit collection."""
    svc = SegmentalReportingUnitService()
    return svc.calculate_aggregate_metrics()

# ==================== ConsolidatedCashFlow Endpoints ====================
@router.get("/consolidatedcashflows", response_model=List[Dict[str, Any]])
def list_consolidatedcashflows(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ConsolidatedCashFlow records with pagination and filtering."""
    svc = ConsolidatedCashFlowService()
    items = svc.list_consolidatedcashflows(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/consolidatedcashflows/{item_id}", response_model=Dict[str, Any])
def get_consolidatedcashflow_by_id(item_id: int):
    """Retrieve detailed record for ConsolidatedCashFlow by ID."""
    svc = ConsolidatedCashFlowService()
    item = svc.get_consolidatedcashflow_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ConsolidatedCashFlow with ID {item_id} not found")
    return item.to_dict()

@router.post("/consolidatedcashflows", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_consolidatedcashflow(payload: ConsolidatedCashFlowCreateSchema):
    """Create new ConsolidatedCashFlow instance in enterprise repository."""
    svc = ConsolidatedCashFlowService()
    try:
        item = svc.create_consolidatedcashflow(
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

@router.put("/consolidatedcashflows/{item_id}", response_model=Dict[str, Any])
def update_consolidatedcashflow(item_id: int, payload: ConsolidatedCashFlowUpdateSchema):
    """Update existing ConsolidatedCashFlow record fields."""
    svc = ConsolidatedCashFlowService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_consolidatedcashflow(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ConsolidatedCashFlow with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/consolidatedcashflows/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_consolidatedcashflow(item_id: int, hard: bool = Query(False)):
    """Delete ConsolidatedCashFlow record (soft-delete by default)."""
    svc = ConsolidatedCashFlowService()
    ok = svc.delete_consolidatedcashflow(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ConsolidatedCashFlow with ID {item_id} not found")
    return None

@router.get("/consolidatedcashflows/analytics/metrics", response_model=Dict[str, Any])
def get_consolidatedcashflow_metrics():
    """Calculate summary statistical KPIs for ConsolidatedCashFlow collection."""
    svc = ConsolidatedCashFlowService()
    return svc.calculate_aggregate_metrics()

# ==================== StatutoryBalanceSheet Endpoints ====================
@router.get("/statutorybalancesheets", response_model=List[Dict[str, Any]])
def list_statutorybalancesheets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StatutoryBalanceSheet records with pagination and filtering."""
    svc = StatutoryBalanceSheetService()
    items = svc.list_statutorybalancesheets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/statutorybalancesheets/{item_id}", response_model=Dict[str, Any])
def get_statutorybalancesheet_by_id(item_id: int):
    """Retrieve detailed record for StatutoryBalanceSheet by ID."""
    svc = StatutoryBalanceSheetService()
    item = svc.get_statutorybalancesheet_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StatutoryBalanceSheet with ID {item_id} not found")
    return item.to_dict()

@router.post("/statutorybalancesheets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_statutorybalancesheet(payload: StatutoryBalanceSheetCreateSchema):
    """Create new StatutoryBalanceSheet instance in enterprise repository."""
    svc = StatutoryBalanceSheetService()
    try:
        item = svc.create_statutorybalancesheet(
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

@router.put("/statutorybalancesheets/{item_id}", response_model=Dict[str, Any])
def update_statutorybalancesheet(item_id: int, payload: StatutoryBalanceSheetUpdateSchema):
    """Update existing StatutoryBalanceSheet record fields."""
    svc = StatutoryBalanceSheetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_statutorybalancesheet(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StatutoryBalanceSheet with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/statutorybalancesheets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_statutorybalancesheet(item_id: int, hard: bool = Query(False)):
    """Delete StatutoryBalanceSheet record (soft-delete by default)."""
    svc = StatutoryBalanceSheetService()
    ok = svc.delete_statutorybalancesheet(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StatutoryBalanceSheet with ID {item_id} not found")
    return None

@router.get("/statutorybalancesheets/analytics/metrics", response_model=Dict[str, Any])
def get_statutorybalancesheet_metrics():
    """Calculate summary statistical KPIs for StatutoryBalanceSheet collection."""
    svc = StatutoryBalanceSheetService()
    return svc.calculate_aggregate_metrics()

# ==================== ConsolidatedIncomeStatement Endpoints ====================
@router.get("/consolidatedincomestatements", response_model=List[Dict[str, Any]])
def list_consolidatedincomestatements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ConsolidatedIncomeStatement records with pagination and filtering."""
    svc = ConsolidatedIncomeStatementService()
    items = svc.list_consolidatedincomestatements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/consolidatedincomestatements/{item_id}", response_model=Dict[str, Any])
def get_consolidatedincomestatement_by_id(item_id: int):
    """Retrieve detailed record for ConsolidatedIncomeStatement by ID."""
    svc = ConsolidatedIncomeStatementService()
    item = svc.get_consolidatedincomestatement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ConsolidatedIncomeStatement with ID {item_id} not found")
    return item.to_dict()

@router.post("/consolidatedincomestatements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_consolidatedincomestatement(payload: ConsolidatedIncomeStatementCreateSchema):
    """Create new ConsolidatedIncomeStatement instance in enterprise repository."""
    svc = ConsolidatedIncomeStatementService()
    try:
        item = svc.create_consolidatedincomestatement(
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

@router.put("/consolidatedincomestatements/{item_id}", response_model=Dict[str, Any])
def update_consolidatedincomestatement(item_id: int, payload: ConsolidatedIncomeStatementUpdateSchema):
    """Update existing ConsolidatedIncomeStatement record fields."""
    svc = ConsolidatedIncomeStatementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_consolidatedincomestatement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ConsolidatedIncomeStatement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/consolidatedincomestatements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_consolidatedincomestatement(item_id: int, hard: bool = Query(False)):
    """Delete ConsolidatedIncomeStatement record (soft-delete by default)."""
    svc = ConsolidatedIncomeStatementService()
    ok = svc.delete_consolidatedincomestatement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ConsolidatedIncomeStatement with ID {item_id} not found")
    return None

@router.get("/consolidatedincomestatements/analytics/metrics", response_model=Dict[str, Any])
def get_consolidatedincomestatement_metrics():
    """Calculate summary statistical KPIs for ConsolidatedIncomeStatement collection."""
    svc = ConsolidatedIncomeStatementService()
    return svc.calculate_aggregate_metrics()

# ==================== AuditTrailElimination Endpoints ====================
@router.get("/audittraileliminations", response_model=List[Dict[str, Any]])
def list_audittraileliminations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AuditTrailElimination records with pagination and filtering."""
    svc = AuditTrailEliminationService()
    items = svc.list_audittraileliminations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/audittraileliminations/{item_id}", response_model=Dict[str, Any])
def get_audittrailelimination_by_id(item_id: int):
    """Retrieve detailed record for AuditTrailElimination by ID."""
    svc = AuditTrailEliminationService()
    item = svc.get_audittrailelimination_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AuditTrailElimination with ID {item_id} not found")
    return item.to_dict()

@router.post("/audittraileliminations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_audittrailelimination(payload: AuditTrailEliminationCreateSchema):
    """Create new AuditTrailElimination instance in enterprise repository."""
    svc = AuditTrailEliminationService()
    try:
        item = svc.create_audittrailelimination(
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

@router.put("/audittraileliminations/{item_id}", response_model=Dict[str, Any])
def update_audittrailelimination(item_id: int, payload: AuditTrailEliminationUpdateSchema):
    """Update existing AuditTrailElimination record fields."""
    svc = AuditTrailEliminationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_audittrailelimination(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AuditTrailElimination with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/audittraileliminations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_audittrailelimination(item_id: int, hard: bool = Query(False)):
    """Delete AuditTrailElimination record (soft-delete by default)."""
    svc = AuditTrailEliminationService()
    ok = svc.delete_audittrailelimination(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AuditTrailElimination with ID {item_id} not found")
    return None

@router.get("/audittraileliminations/analytics/metrics", response_model=Dict[str, Any])
def get_audittrailelimination_metrics():
    """Calculate summary statistical KPIs for AuditTrailElimination collection."""
    svc = AuditTrailEliminationService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxProvisioningConsolidated Endpoints ====================
@router.get("/taxprovisioningconsolidateds", response_model=List[Dict[str, Any]])
def list_taxprovisioningconsolidateds(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxProvisioningConsolidated records with pagination and filtering."""
    svc = TaxProvisioningConsolidatedService()
    items = svc.list_taxprovisioningconsolidateds(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxprovisioningconsolidateds/{item_id}", response_model=Dict[str, Any])
def get_taxprovisioningconsolidated_by_id(item_id: int):
    """Retrieve detailed record for TaxProvisioningConsolidated by ID."""
    svc = TaxProvisioningConsolidatedService()
    item = svc.get_taxprovisioningconsolidated_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxProvisioningConsolidated with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxprovisioningconsolidateds", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxprovisioningconsolidated(payload: TaxProvisioningConsolidatedCreateSchema):
    """Create new TaxProvisioningConsolidated instance in enterprise repository."""
    svc = TaxProvisioningConsolidatedService()
    try:
        item = svc.create_taxprovisioningconsolidated(
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

@router.put("/taxprovisioningconsolidateds/{item_id}", response_model=Dict[str, Any])
def update_taxprovisioningconsolidated(item_id: int, payload: TaxProvisioningConsolidatedUpdateSchema):
    """Update existing TaxProvisioningConsolidated record fields."""
    svc = TaxProvisioningConsolidatedService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxprovisioningconsolidated(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxProvisioningConsolidated with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxprovisioningconsolidateds/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxprovisioningconsolidated(item_id: int, hard: bool = Query(False)):
    """Delete TaxProvisioningConsolidated record (soft-delete by default)."""
    svc = TaxProvisioningConsolidatedService()
    ok = svc.delete_taxprovisioningconsolidated(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxProvisioningConsolidated with ID {item_id} not found")
    return None

@router.get("/taxprovisioningconsolidateds/analytics/metrics", response_model=Dict[str, Any])
def get_taxprovisioningconsolidated_metrics():
    """Calculate summary statistical KPIs for TaxProvisioningConsolidated collection."""
    svc = TaxProvisioningConsolidatedService()
    return svc.calculate_aggregate_metrics()

# ==================== FinancialClosingChecklist Endpoints ====================
@router.get("/financialclosingchecklists", response_model=List[Dict[str, Any]])
def list_financialclosingchecklists(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FinancialClosingChecklist records with pagination and filtering."""
    svc = FinancialClosingChecklistService()
    items = svc.list_financialclosingchecklists(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/financialclosingchecklists/{item_id}", response_model=Dict[str, Any])
def get_financialclosingchecklist_by_id(item_id: int):
    """Retrieve detailed record for FinancialClosingChecklist by ID."""
    svc = FinancialClosingChecklistService()
    item = svc.get_financialclosingchecklist_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FinancialClosingChecklist with ID {item_id} not found")
    return item.to_dict()

@router.post("/financialclosingchecklists", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_financialclosingchecklist(payload: FinancialClosingChecklistCreateSchema):
    """Create new FinancialClosingChecklist instance in enterprise repository."""
    svc = FinancialClosingChecklistService()
    try:
        item = svc.create_financialclosingchecklist(
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

@router.put("/financialclosingchecklists/{item_id}", response_model=Dict[str, Any])
def update_financialclosingchecklist(item_id: int, payload: FinancialClosingChecklistUpdateSchema):
    """Update existing FinancialClosingChecklist record fields."""
    svc = FinancialClosingChecklistService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_financialclosingchecklist(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FinancialClosingChecklist with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/financialclosingchecklists/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_financialclosingchecklist(item_id: int, hard: bool = Query(False)):
    """Delete FinancialClosingChecklist record (soft-delete by default)."""
    svc = FinancialClosingChecklistService()
    ok = svc.delete_financialclosingchecklist(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FinancialClosingChecklist with ID {item_id} not found")
    return None

@router.get("/financialclosingchecklists/analytics/metrics", response_model=Dict[str, Any])
def get_financialclosingchecklist_metrics():
    """Calculate summary statistical KPIs for FinancialClosingChecklist collection."""
    svc = FinancialClosingChecklistService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutiveBoardFinancialReport Endpoints ====================
@router.get("/executiveboardfinancialreports", response_model=List[Dict[str, Any]])
def list_executiveboardfinancialreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutiveBoardFinancialReport records with pagination and filtering."""
    svc = ExecutiveBoardFinancialReportService()
    items = svc.list_executiveboardfinancialreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executiveboardfinancialreports/{item_id}", response_model=Dict[str, Any])
def get_executiveboardfinancialreport_by_id(item_id: int):
    """Retrieve detailed record for ExecutiveBoardFinancialReport by ID."""
    svc = ExecutiveBoardFinancialReportService()
    item = svc.get_executiveboardfinancialreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutiveBoardFinancialReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/executiveboardfinancialreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executiveboardfinancialreport(payload: ExecutiveBoardFinancialReportCreateSchema):
    """Create new ExecutiveBoardFinancialReport instance in enterprise repository."""
    svc = ExecutiveBoardFinancialReportService()
    try:
        item = svc.create_executiveboardfinancialreport(
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

@router.put("/executiveboardfinancialreports/{item_id}", response_model=Dict[str, Any])
def update_executiveboardfinancialreport(item_id: int, payload: ExecutiveBoardFinancialReportUpdateSchema):
    """Update existing ExecutiveBoardFinancialReport record fields."""
    svc = ExecutiveBoardFinancialReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executiveboardfinancialreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutiveBoardFinancialReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executiveboardfinancialreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executiveboardfinancialreport(item_id: int, hard: bool = Query(False)):
    """Delete ExecutiveBoardFinancialReport record (soft-delete by default)."""
    svc = ExecutiveBoardFinancialReportService()
    ok = svc.delete_executiveboardfinancialreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutiveBoardFinancialReport with ID {item_id} not found")
    return None

@router.get("/executiveboardfinancialreports/analytics/metrics", response_model=Dict[str, Any])
def get_executiveboardfinancialreport_metrics():
    """Calculate summary statistical KPIs for ExecutiveBoardFinancialReport collection."""
    svc = ExecutiveBoardFinancialReportService()
    return svc.calculate_aggregate_metrics()

