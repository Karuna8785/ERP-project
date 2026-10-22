"""
Financial Derivatives & Mark-to-Market Hedging - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    InterestRateSwapContractService,
    FXForwardContractService,
    CommodityFutureHedgeService,
    CurrencyOptionStrategyService,
    MarkToMarketValuationService,
    ISDAMasterAgreementService,
    CollateralMarginCallService,
    CreditDefaultSwapSpreadService,
    HedgeEffectivenessTestService,
    GreeksRiskSensitivityService,
    CounterpartyCreditRiskService,
    YieldCurveInterpolationService,
    DerivativesSettlementEntryService,
    TreasuryExposureForecastService,
    RegulatoryEMIRFilingService,
    BasisRiskMeasurementService,
)
from .schemas import (
    InterestRateSwapContractCreateSchema, InterestRateSwapContractUpdateSchema, InterestRateSwapContractResponseSchema,
    FXForwardContractCreateSchema, FXForwardContractUpdateSchema, FXForwardContractResponseSchema,
    CommodityFutureHedgeCreateSchema, CommodityFutureHedgeUpdateSchema, CommodityFutureHedgeResponseSchema,
    CurrencyOptionStrategyCreateSchema, CurrencyOptionStrategyUpdateSchema, CurrencyOptionStrategyResponseSchema,
    MarkToMarketValuationCreateSchema, MarkToMarketValuationUpdateSchema, MarkToMarketValuationResponseSchema,
    ISDAMasterAgreementCreateSchema, ISDAMasterAgreementUpdateSchema, ISDAMasterAgreementResponseSchema,
    CollateralMarginCallCreateSchema, CollateralMarginCallUpdateSchema, CollateralMarginCallResponseSchema,
    CreditDefaultSwapSpreadCreateSchema, CreditDefaultSwapSpreadUpdateSchema, CreditDefaultSwapSpreadResponseSchema,
    HedgeEffectivenessTestCreateSchema, HedgeEffectivenessTestUpdateSchema, HedgeEffectivenessTestResponseSchema,
    GreeksRiskSensitivityCreateSchema, GreeksRiskSensitivityUpdateSchema, GreeksRiskSensitivityResponseSchema,
    CounterpartyCreditRiskCreateSchema, CounterpartyCreditRiskUpdateSchema, CounterpartyCreditRiskResponseSchema,
    YieldCurveInterpolationCreateSchema, YieldCurveInterpolationUpdateSchema, YieldCurveInterpolationResponseSchema,
    DerivativesSettlementEntryCreateSchema, DerivativesSettlementEntryUpdateSchema, DerivativesSettlementEntryResponseSchema,
    TreasuryExposureForecastCreateSchema, TreasuryExposureForecastUpdateSchema, TreasuryExposureForecastResponseSchema,
    RegulatoryEMIRFilingCreateSchema, RegulatoryEMIRFilingUpdateSchema, RegulatoryEMIRFilingResponseSchema,
    BasisRiskMeasurementCreateSchema, BasisRiskMeasurementUpdateSchema, BasisRiskMeasurementResponseSchema,
)

router = APIRouter(prefix="/treasury_derivatives", tags=["Financial Derivatives & Mark-to-Market Hedging"])

# ==================== InterestRateSwapContract Endpoints ====================
@router.get("/interestrateswapcontracts", response_model=List[Dict[str, Any]])
def list_interestrateswapcontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InterestRateSwapContract records with pagination and filtering."""
    svc = InterestRateSwapContractService()
    items = svc.list_interestrateswapcontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/interestrateswapcontracts/{item_id}", response_model=Dict[str, Any])
def get_interestrateswapcontract_by_id(item_id: int):
    """Retrieve detailed record for InterestRateSwapContract by ID."""
    svc = InterestRateSwapContractService()
    item = svc.get_interestrateswapcontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InterestRateSwapContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/interestrateswapcontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_interestrateswapcontract(payload: InterestRateSwapContractCreateSchema):
    """Create new InterestRateSwapContract instance in enterprise repository."""
    svc = InterestRateSwapContractService()
    try:
        item = svc.create_interestrateswapcontract(
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

@router.put("/interestrateswapcontracts/{item_id}", response_model=Dict[str, Any])
def update_interestrateswapcontract(item_id: int, payload: InterestRateSwapContractUpdateSchema):
    """Update existing InterestRateSwapContract record fields."""
    svc = InterestRateSwapContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_interestrateswapcontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InterestRateSwapContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/interestrateswapcontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_interestrateswapcontract(item_id: int, hard: bool = Query(False)):
    """Delete InterestRateSwapContract record (soft-delete by default)."""
    svc = InterestRateSwapContractService()
    ok = svc.delete_interestrateswapcontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InterestRateSwapContract with ID {item_id} not found")
    return None

@router.get("/interestrateswapcontracts/analytics/metrics", response_model=Dict[str, Any])
def get_interestrateswapcontract_metrics():
    """Calculate summary statistical KPIs for InterestRateSwapContract collection."""
    svc = InterestRateSwapContractService()
    return svc.calculate_aggregate_metrics()

# ==================== FXForwardContract Endpoints ====================
@router.get("/fxforwardcontracts", response_model=List[Dict[str, Any]])
def list_fxforwardcontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FXForwardContract records with pagination and filtering."""
    svc = FXForwardContractService()
    items = svc.list_fxforwardcontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fxforwardcontracts/{item_id}", response_model=Dict[str, Any])
def get_fxforwardcontract_by_id(item_id: int):
    """Retrieve detailed record for FXForwardContract by ID."""
    svc = FXForwardContractService()
    item = svc.get_fxforwardcontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FXForwardContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/fxforwardcontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fxforwardcontract(payload: FXForwardContractCreateSchema):
    """Create new FXForwardContract instance in enterprise repository."""
    svc = FXForwardContractService()
    try:
        item = svc.create_fxforwardcontract(
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

@router.put("/fxforwardcontracts/{item_id}", response_model=Dict[str, Any])
def update_fxforwardcontract(item_id: int, payload: FXForwardContractUpdateSchema):
    """Update existing FXForwardContract record fields."""
    svc = FXForwardContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fxforwardcontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FXForwardContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fxforwardcontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fxforwardcontract(item_id: int, hard: bool = Query(False)):
    """Delete FXForwardContract record (soft-delete by default)."""
    svc = FXForwardContractService()
    ok = svc.delete_fxforwardcontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FXForwardContract with ID {item_id} not found")
    return None

@router.get("/fxforwardcontracts/analytics/metrics", response_model=Dict[str, Any])
def get_fxforwardcontract_metrics():
    """Calculate summary statistical KPIs for FXForwardContract collection."""
    svc = FXForwardContractService()
    return svc.calculate_aggregate_metrics()

# ==================== CommodityFutureHedge Endpoints ====================
@router.get("/commodityfuturehedges", response_model=List[Dict[str, Any]])
def list_commodityfuturehedges(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CommodityFutureHedge records with pagination and filtering."""
    svc = CommodityFutureHedgeService()
    items = svc.list_commodityfuturehedges(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/commodityfuturehedges/{item_id}", response_model=Dict[str, Any])
def get_commodityfuturehedge_by_id(item_id: int):
    """Retrieve detailed record for CommodityFutureHedge by ID."""
    svc = CommodityFutureHedgeService()
    item = svc.get_commodityfuturehedge_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CommodityFutureHedge with ID {item_id} not found")
    return item.to_dict()

@router.post("/commodityfuturehedges", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_commodityfuturehedge(payload: CommodityFutureHedgeCreateSchema):
    """Create new CommodityFutureHedge instance in enterprise repository."""
    svc = CommodityFutureHedgeService()
    try:
        item = svc.create_commodityfuturehedge(
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

@router.put("/commodityfuturehedges/{item_id}", response_model=Dict[str, Any])
def update_commodityfuturehedge(item_id: int, payload: CommodityFutureHedgeUpdateSchema):
    """Update existing CommodityFutureHedge record fields."""
    svc = CommodityFutureHedgeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_commodityfuturehedge(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CommodityFutureHedge with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/commodityfuturehedges/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_commodityfuturehedge(item_id: int, hard: bool = Query(False)):
    """Delete CommodityFutureHedge record (soft-delete by default)."""
    svc = CommodityFutureHedgeService()
    ok = svc.delete_commodityfuturehedge(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CommodityFutureHedge with ID {item_id} not found")
    return None

@router.get("/commodityfuturehedges/analytics/metrics", response_model=Dict[str, Any])
def get_commodityfuturehedge_metrics():
    """Calculate summary statistical KPIs for CommodityFutureHedge collection."""
    svc = CommodityFutureHedgeService()
    return svc.calculate_aggregate_metrics()

# ==================== CurrencyOptionStrategy Endpoints ====================
@router.get("/currencyoptionstrategys", response_model=List[Dict[str, Any]])
def list_currencyoptionstrategys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CurrencyOptionStrategy records with pagination and filtering."""
    svc = CurrencyOptionStrategyService()
    items = svc.list_currencyoptionstrategys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/currencyoptionstrategys/{item_id}", response_model=Dict[str, Any])
def get_currencyoptionstrategy_by_id(item_id: int):
    """Retrieve detailed record for CurrencyOptionStrategy by ID."""
    svc = CurrencyOptionStrategyService()
    item = svc.get_currencyoptionstrategy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CurrencyOptionStrategy with ID {item_id} not found")
    return item.to_dict()

@router.post("/currencyoptionstrategys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_currencyoptionstrategy(payload: CurrencyOptionStrategyCreateSchema):
    """Create new CurrencyOptionStrategy instance in enterprise repository."""
    svc = CurrencyOptionStrategyService()
    try:
        item = svc.create_currencyoptionstrategy(
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

@router.put("/currencyoptionstrategys/{item_id}", response_model=Dict[str, Any])
def update_currencyoptionstrategy(item_id: int, payload: CurrencyOptionStrategyUpdateSchema):
    """Update existing CurrencyOptionStrategy record fields."""
    svc = CurrencyOptionStrategyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_currencyoptionstrategy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CurrencyOptionStrategy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/currencyoptionstrategys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_currencyoptionstrategy(item_id: int, hard: bool = Query(False)):
    """Delete CurrencyOptionStrategy record (soft-delete by default)."""
    svc = CurrencyOptionStrategyService()
    ok = svc.delete_currencyoptionstrategy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CurrencyOptionStrategy with ID {item_id} not found")
    return None

@router.get("/currencyoptionstrategys/analytics/metrics", response_model=Dict[str, Any])
def get_currencyoptionstrategy_metrics():
    """Calculate summary statistical KPIs for CurrencyOptionStrategy collection."""
    svc = CurrencyOptionStrategyService()
    return svc.calculate_aggregate_metrics()

# ==================== MarkToMarketValuation Endpoints ====================
@router.get("/marktomarketvaluations", response_model=List[Dict[str, Any]])
def list_marktomarketvaluations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MarkToMarketValuation records with pagination and filtering."""
    svc = MarkToMarketValuationService()
    items = svc.list_marktomarketvaluations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/marktomarketvaluations/{item_id}", response_model=Dict[str, Any])
def get_marktomarketvaluation_by_id(item_id: int):
    """Retrieve detailed record for MarkToMarketValuation by ID."""
    svc = MarkToMarketValuationService()
    item = svc.get_marktomarketvaluation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MarkToMarketValuation with ID {item_id} not found")
    return item.to_dict()

@router.post("/marktomarketvaluations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_marktomarketvaluation(payload: MarkToMarketValuationCreateSchema):
    """Create new MarkToMarketValuation instance in enterprise repository."""
    svc = MarkToMarketValuationService()
    try:
        item = svc.create_marktomarketvaluation(
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

@router.put("/marktomarketvaluations/{item_id}", response_model=Dict[str, Any])
def update_marktomarketvaluation(item_id: int, payload: MarkToMarketValuationUpdateSchema):
    """Update existing MarkToMarketValuation record fields."""
    svc = MarkToMarketValuationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_marktomarketvaluation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MarkToMarketValuation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/marktomarketvaluations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_marktomarketvaluation(item_id: int, hard: bool = Query(False)):
    """Delete MarkToMarketValuation record (soft-delete by default)."""
    svc = MarkToMarketValuationService()
    ok = svc.delete_marktomarketvaluation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MarkToMarketValuation with ID {item_id} not found")
    return None

@router.get("/marktomarketvaluations/analytics/metrics", response_model=Dict[str, Any])
def get_marktomarketvaluation_metrics():
    """Calculate summary statistical KPIs for MarkToMarketValuation collection."""
    svc = MarkToMarketValuationService()
    return svc.calculate_aggregate_metrics()

# ==================== ISDAMasterAgreement Endpoints ====================
@router.get("/isdamasteragreements", response_model=List[Dict[str, Any]])
def list_isdamasteragreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ISDAMasterAgreement records with pagination and filtering."""
    svc = ISDAMasterAgreementService()
    items = svc.list_isdamasteragreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/isdamasteragreements/{item_id}", response_model=Dict[str, Any])
def get_isdamasteragreement_by_id(item_id: int):
    """Retrieve detailed record for ISDAMasterAgreement by ID."""
    svc = ISDAMasterAgreementService()
    item = svc.get_isdamasteragreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ISDAMasterAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/isdamasteragreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_isdamasteragreement(payload: ISDAMasterAgreementCreateSchema):
    """Create new ISDAMasterAgreement instance in enterprise repository."""
    svc = ISDAMasterAgreementService()
    try:
        item = svc.create_isdamasteragreement(
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

@router.put("/isdamasteragreements/{item_id}", response_model=Dict[str, Any])
def update_isdamasteragreement(item_id: int, payload: ISDAMasterAgreementUpdateSchema):
    """Update existing ISDAMasterAgreement record fields."""
    svc = ISDAMasterAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_isdamasteragreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ISDAMasterAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/isdamasteragreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_isdamasteragreement(item_id: int, hard: bool = Query(False)):
    """Delete ISDAMasterAgreement record (soft-delete by default)."""
    svc = ISDAMasterAgreementService()
    ok = svc.delete_isdamasteragreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ISDAMasterAgreement with ID {item_id} not found")
    return None

@router.get("/isdamasteragreements/analytics/metrics", response_model=Dict[str, Any])
def get_isdamasteragreement_metrics():
    """Calculate summary statistical KPIs for ISDAMasterAgreement collection."""
    svc = ISDAMasterAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== CollateralMarginCall Endpoints ====================
@router.get("/collateralmargincalls", response_model=List[Dict[str, Any]])
def list_collateralmargincalls(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CollateralMarginCall records with pagination and filtering."""
    svc = CollateralMarginCallService()
    items = svc.list_collateralmargincalls(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/collateralmargincalls/{item_id}", response_model=Dict[str, Any])
def get_collateralmargincall_by_id(item_id: int):
    """Retrieve detailed record for CollateralMarginCall by ID."""
    svc = CollateralMarginCallService()
    item = svc.get_collateralmargincall_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CollateralMarginCall with ID {item_id} not found")
    return item.to_dict()

@router.post("/collateralmargincalls", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_collateralmargincall(payload: CollateralMarginCallCreateSchema):
    """Create new CollateralMarginCall instance in enterprise repository."""
    svc = CollateralMarginCallService()
    try:
        item = svc.create_collateralmargincall(
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

@router.put("/collateralmargincalls/{item_id}", response_model=Dict[str, Any])
def update_collateralmargincall(item_id: int, payload: CollateralMarginCallUpdateSchema):
    """Update existing CollateralMarginCall record fields."""
    svc = CollateralMarginCallService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_collateralmargincall(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CollateralMarginCall with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/collateralmargincalls/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_collateralmargincall(item_id: int, hard: bool = Query(False)):
    """Delete CollateralMarginCall record (soft-delete by default)."""
    svc = CollateralMarginCallService()
    ok = svc.delete_collateralmargincall(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CollateralMarginCall with ID {item_id} not found")
    return None

@router.get("/collateralmargincalls/analytics/metrics", response_model=Dict[str, Any])
def get_collateralmargincall_metrics():
    """Calculate summary statistical KPIs for CollateralMarginCall collection."""
    svc = CollateralMarginCallService()
    return svc.calculate_aggregate_metrics()

# ==================== CreditDefaultSwapSpread Endpoints ====================
@router.get("/creditdefaultswapspreads", response_model=List[Dict[str, Any]])
def list_creditdefaultswapspreads(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CreditDefaultSwapSpread records with pagination and filtering."""
    svc = CreditDefaultSwapSpreadService()
    items = svc.list_creditdefaultswapspreads(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/creditdefaultswapspreads/{item_id}", response_model=Dict[str, Any])
def get_creditdefaultswapspread_by_id(item_id: int):
    """Retrieve detailed record for CreditDefaultSwapSpread by ID."""
    svc = CreditDefaultSwapSpreadService()
    item = svc.get_creditdefaultswapspread_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CreditDefaultSwapSpread with ID {item_id} not found")
    return item.to_dict()

@router.post("/creditdefaultswapspreads", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_creditdefaultswapspread(payload: CreditDefaultSwapSpreadCreateSchema):
    """Create new CreditDefaultSwapSpread instance in enterprise repository."""
    svc = CreditDefaultSwapSpreadService()
    try:
        item = svc.create_creditdefaultswapspread(
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

@router.put("/creditdefaultswapspreads/{item_id}", response_model=Dict[str, Any])
def update_creditdefaultswapspread(item_id: int, payload: CreditDefaultSwapSpreadUpdateSchema):
    """Update existing CreditDefaultSwapSpread record fields."""
    svc = CreditDefaultSwapSpreadService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_creditdefaultswapspread(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CreditDefaultSwapSpread with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/creditdefaultswapspreads/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_creditdefaultswapspread(item_id: int, hard: bool = Query(False)):
    """Delete CreditDefaultSwapSpread record (soft-delete by default)."""
    svc = CreditDefaultSwapSpreadService()
    ok = svc.delete_creditdefaultswapspread(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CreditDefaultSwapSpread with ID {item_id} not found")
    return None

@router.get("/creditdefaultswapspreads/analytics/metrics", response_model=Dict[str, Any])
def get_creditdefaultswapspread_metrics():
    """Calculate summary statistical KPIs for CreditDefaultSwapSpread collection."""
    svc = CreditDefaultSwapSpreadService()
    return svc.calculate_aggregate_metrics()

# ==================== HedgeEffectivenessTest Endpoints ====================
@router.get("/hedgeeffectivenesstests", response_model=List[Dict[str, Any]])
def list_hedgeeffectivenesstests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HedgeEffectivenessTest records with pagination and filtering."""
    svc = HedgeEffectivenessTestService()
    items = svc.list_hedgeeffectivenesstests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hedgeeffectivenesstests/{item_id}", response_model=Dict[str, Any])
def get_hedgeeffectivenesstest_by_id(item_id: int):
    """Retrieve detailed record for HedgeEffectivenessTest by ID."""
    svc = HedgeEffectivenessTestService()
    item = svc.get_hedgeeffectivenesstest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HedgeEffectivenessTest with ID {item_id} not found")
    return item.to_dict()

@router.post("/hedgeeffectivenesstests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hedgeeffectivenesstest(payload: HedgeEffectivenessTestCreateSchema):
    """Create new HedgeEffectivenessTest instance in enterprise repository."""
    svc = HedgeEffectivenessTestService()
    try:
        item = svc.create_hedgeeffectivenesstest(
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

@router.put("/hedgeeffectivenesstests/{item_id}", response_model=Dict[str, Any])
def update_hedgeeffectivenesstest(item_id: int, payload: HedgeEffectivenessTestUpdateSchema):
    """Update existing HedgeEffectivenessTest record fields."""
    svc = HedgeEffectivenessTestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hedgeeffectivenesstest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HedgeEffectivenessTest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hedgeeffectivenesstests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hedgeeffectivenesstest(item_id: int, hard: bool = Query(False)):
    """Delete HedgeEffectivenessTest record (soft-delete by default)."""
    svc = HedgeEffectivenessTestService()
    ok = svc.delete_hedgeeffectivenesstest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HedgeEffectivenessTest with ID {item_id} not found")
    return None

@router.get("/hedgeeffectivenesstests/analytics/metrics", response_model=Dict[str, Any])
def get_hedgeeffectivenesstest_metrics():
    """Calculate summary statistical KPIs for HedgeEffectivenessTest collection."""
    svc = HedgeEffectivenessTestService()
    return svc.calculate_aggregate_metrics()

# ==================== GreeksRiskSensitivity Endpoints ====================
@router.get("/greeksrisksensitivitys", response_model=List[Dict[str, Any]])
def list_greeksrisksensitivitys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GreeksRiskSensitivity records with pagination and filtering."""
    svc = GreeksRiskSensitivityService()
    items = svc.list_greeksrisksensitivitys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/greeksrisksensitivitys/{item_id}", response_model=Dict[str, Any])
def get_greeksrisksensitivity_by_id(item_id: int):
    """Retrieve detailed record for GreeksRiskSensitivity by ID."""
    svc = GreeksRiskSensitivityService()
    item = svc.get_greeksrisksensitivity_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GreeksRiskSensitivity with ID {item_id} not found")
    return item.to_dict()

@router.post("/greeksrisksensitivitys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_greeksrisksensitivity(payload: GreeksRiskSensitivityCreateSchema):
    """Create new GreeksRiskSensitivity instance in enterprise repository."""
    svc = GreeksRiskSensitivityService()
    try:
        item = svc.create_greeksrisksensitivity(
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

@router.put("/greeksrisksensitivitys/{item_id}", response_model=Dict[str, Any])
def update_greeksrisksensitivity(item_id: int, payload: GreeksRiskSensitivityUpdateSchema):
    """Update existing GreeksRiskSensitivity record fields."""
    svc = GreeksRiskSensitivityService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_greeksrisksensitivity(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GreeksRiskSensitivity with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/greeksrisksensitivitys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_greeksrisksensitivity(item_id: int, hard: bool = Query(False)):
    """Delete GreeksRiskSensitivity record (soft-delete by default)."""
    svc = GreeksRiskSensitivityService()
    ok = svc.delete_greeksrisksensitivity(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GreeksRiskSensitivity with ID {item_id} not found")
    return None

@router.get("/greeksrisksensitivitys/analytics/metrics", response_model=Dict[str, Any])
def get_greeksrisksensitivity_metrics():
    """Calculate summary statistical KPIs for GreeksRiskSensitivity collection."""
    svc = GreeksRiskSensitivityService()
    return svc.calculate_aggregate_metrics()

# ==================== CounterpartyCreditRisk Endpoints ====================
@router.get("/counterpartycreditrisks", response_model=List[Dict[str, Any]])
def list_counterpartycreditrisks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CounterpartyCreditRisk records with pagination and filtering."""
    svc = CounterpartyCreditRiskService()
    items = svc.list_counterpartycreditrisks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/counterpartycreditrisks/{item_id}", response_model=Dict[str, Any])
def get_counterpartycreditrisk_by_id(item_id: int):
    """Retrieve detailed record for CounterpartyCreditRisk by ID."""
    svc = CounterpartyCreditRiskService()
    item = svc.get_counterpartycreditrisk_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CounterpartyCreditRisk with ID {item_id} not found")
    return item.to_dict()

@router.post("/counterpartycreditrisks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_counterpartycreditrisk(payload: CounterpartyCreditRiskCreateSchema):
    """Create new CounterpartyCreditRisk instance in enterprise repository."""
    svc = CounterpartyCreditRiskService()
    try:
        item = svc.create_counterpartycreditrisk(
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

@router.put("/counterpartycreditrisks/{item_id}", response_model=Dict[str, Any])
def update_counterpartycreditrisk(item_id: int, payload: CounterpartyCreditRiskUpdateSchema):
    """Update existing CounterpartyCreditRisk record fields."""
    svc = CounterpartyCreditRiskService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_counterpartycreditrisk(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CounterpartyCreditRisk with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/counterpartycreditrisks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_counterpartycreditrisk(item_id: int, hard: bool = Query(False)):
    """Delete CounterpartyCreditRisk record (soft-delete by default)."""
    svc = CounterpartyCreditRiskService()
    ok = svc.delete_counterpartycreditrisk(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CounterpartyCreditRisk with ID {item_id} not found")
    return None

@router.get("/counterpartycreditrisks/analytics/metrics", response_model=Dict[str, Any])
def get_counterpartycreditrisk_metrics():
    """Calculate summary statistical KPIs for CounterpartyCreditRisk collection."""
    svc = CounterpartyCreditRiskService()
    return svc.calculate_aggregate_metrics()

# ==================== YieldCurveInterpolation Endpoints ====================
@router.get("/yieldcurveinterpolations", response_model=List[Dict[str, Any]])
def list_yieldcurveinterpolations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List YieldCurveInterpolation records with pagination and filtering."""
    svc = YieldCurveInterpolationService()
    items = svc.list_yieldcurveinterpolations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/yieldcurveinterpolations/{item_id}", response_model=Dict[str, Any])
def get_yieldcurveinterpolation_by_id(item_id: int):
    """Retrieve detailed record for YieldCurveInterpolation by ID."""
    svc = YieldCurveInterpolationService()
    item = svc.get_yieldcurveinterpolation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"YieldCurveInterpolation with ID {item_id} not found")
    return item.to_dict()

@router.post("/yieldcurveinterpolations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_yieldcurveinterpolation(payload: YieldCurveInterpolationCreateSchema):
    """Create new YieldCurveInterpolation instance in enterprise repository."""
    svc = YieldCurveInterpolationService()
    try:
        item = svc.create_yieldcurveinterpolation(
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

@router.put("/yieldcurveinterpolations/{item_id}", response_model=Dict[str, Any])
def update_yieldcurveinterpolation(item_id: int, payload: YieldCurveInterpolationUpdateSchema):
    """Update existing YieldCurveInterpolation record fields."""
    svc = YieldCurveInterpolationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_yieldcurveinterpolation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"YieldCurveInterpolation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/yieldcurveinterpolations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_yieldcurveinterpolation(item_id: int, hard: bool = Query(False)):
    """Delete YieldCurveInterpolation record (soft-delete by default)."""
    svc = YieldCurveInterpolationService()
    ok = svc.delete_yieldcurveinterpolation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"YieldCurveInterpolation with ID {item_id} not found")
    return None

@router.get("/yieldcurveinterpolations/analytics/metrics", response_model=Dict[str, Any])
def get_yieldcurveinterpolation_metrics():
    """Calculate summary statistical KPIs for YieldCurveInterpolation collection."""
    svc = YieldCurveInterpolationService()
    return svc.calculate_aggregate_metrics()

# ==================== DerivativesSettlementEntry Endpoints ====================
@router.get("/derivativessettlemententrys", response_model=List[Dict[str, Any]])
def list_derivativessettlemententrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DerivativesSettlementEntry records with pagination and filtering."""
    svc = DerivativesSettlementEntryService()
    items = svc.list_derivativessettlemententrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/derivativessettlemententrys/{item_id}", response_model=Dict[str, Any])
def get_derivativessettlemententry_by_id(item_id: int):
    """Retrieve detailed record for DerivativesSettlementEntry by ID."""
    svc = DerivativesSettlementEntryService()
    item = svc.get_derivativessettlemententry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DerivativesSettlementEntry with ID {item_id} not found")
    return item.to_dict()

@router.post("/derivativessettlemententrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_derivativessettlemententry(payload: DerivativesSettlementEntryCreateSchema):
    """Create new DerivativesSettlementEntry instance in enterprise repository."""
    svc = DerivativesSettlementEntryService()
    try:
        item = svc.create_derivativessettlemententry(
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

@router.put("/derivativessettlemententrys/{item_id}", response_model=Dict[str, Any])
def update_derivativessettlemententry(item_id: int, payload: DerivativesSettlementEntryUpdateSchema):
    """Update existing DerivativesSettlementEntry record fields."""
    svc = DerivativesSettlementEntryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_derivativessettlemententry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DerivativesSettlementEntry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/derivativessettlemententrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_derivativessettlemententry(item_id: int, hard: bool = Query(False)):
    """Delete DerivativesSettlementEntry record (soft-delete by default)."""
    svc = DerivativesSettlementEntryService()
    ok = svc.delete_derivativessettlemententry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DerivativesSettlementEntry with ID {item_id} not found")
    return None

@router.get("/derivativessettlemententrys/analytics/metrics", response_model=Dict[str, Any])
def get_derivativessettlemententry_metrics():
    """Calculate summary statistical KPIs for DerivativesSettlementEntry collection."""
    svc = DerivativesSettlementEntryService()
    return svc.calculate_aggregate_metrics()

# ==================== TreasuryExposureForecast Endpoints ====================
@router.get("/treasuryexposureforecasts", response_model=List[Dict[str, Any]])
def list_treasuryexposureforecasts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TreasuryExposureForecast records with pagination and filtering."""
    svc = TreasuryExposureForecastService()
    items = svc.list_treasuryexposureforecasts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/treasuryexposureforecasts/{item_id}", response_model=Dict[str, Any])
def get_treasuryexposureforecast_by_id(item_id: int):
    """Retrieve detailed record for TreasuryExposureForecast by ID."""
    svc = TreasuryExposureForecastService()
    item = svc.get_treasuryexposureforecast_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TreasuryExposureForecast with ID {item_id} not found")
    return item.to_dict()

@router.post("/treasuryexposureforecasts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_treasuryexposureforecast(payload: TreasuryExposureForecastCreateSchema):
    """Create new TreasuryExposureForecast instance in enterprise repository."""
    svc = TreasuryExposureForecastService()
    try:
        item = svc.create_treasuryexposureforecast(
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

@router.put("/treasuryexposureforecasts/{item_id}", response_model=Dict[str, Any])
def update_treasuryexposureforecast(item_id: int, payload: TreasuryExposureForecastUpdateSchema):
    """Update existing TreasuryExposureForecast record fields."""
    svc = TreasuryExposureForecastService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_treasuryexposureforecast(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TreasuryExposureForecast with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/treasuryexposureforecasts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_treasuryexposureforecast(item_id: int, hard: bool = Query(False)):
    """Delete TreasuryExposureForecast record (soft-delete by default)."""
    svc = TreasuryExposureForecastService()
    ok = svc.delete_treasuryexposureforecast(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TreasuryExposureForecast with ID {item_id} not found")
    return None

@router.get("/treasuryexposureforecasts/analytics/metrics", response_model=Dict[str, Any])
def get_treasuryexposureforecast_metrics():
    """Calculate summary statistical KPIs for TreasuryExposureForecast collection."""
    svc = TreasuryExposureForecastService()
    return svc.calculate_aggregate_metrics()

# ==================== RegulatoryEMIRFiling Endpoints ====================
@router.get("/regulatoryemirfilings", response_model=List[Dict[str, Any]])
def list_regulatoryemirfilings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RegulatoryEMIRFiling records with pagination and filtering."""
    svc = RegulatoryEMIRFilingService()
    items = svc.list_regulatoryemirfilings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/regulatoryemirfilings/{item_id}", response_model=Dict[str, Any])
def get_regulatoryemirfiling_by_id(item_id: int):
    """Retrieve detailed record for RegulatoryEMIRFiling by ID."""
    svc = RegulatoryEMIRFilingService()
    item = svc.get_regulatoryemirfiling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RegulatoryEMIRFiling with ID {item_id} not found")
    return item.to_dict()

@router.post("/regulatoryemirfilings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_regulatoryemirfiling(payload: RegulatoryEMIRFilingCreateSchema):
    """Create new RegulatoryEMIRFiling instance in enterprise repository."""
    svc = RegulatoryEMIRFilingService()
    try:
        item = svc.create_regulatoryemirfiling(
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

@router.put("/regulatoryemirfilings/{item_id}", response_model=Dict[str, Any])
def update_regulatoryemirfiling(item_id: int, payload: RegulatoryEMIRFilingUpdateSchema):
    """Update existing RegulatoryEMIRFiling record fields."""
    svc = RegulatoryEMIRFilingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_regulatoryemirfiling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RegulatoryEMIRFiling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/regulatoryemirfilings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_regulatoryemirfiling(item_id: int, hard: bool = Query(False)):
    """Delete RegulatoryEMIRFiling record (soft-delete by default)."""
    svc = RegulatoryEMIRFilingService()
    ok = svc.delete_regulatoryemirfiling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RegulatoryEMIRFiling with ID {item_id} not found")
    return None

@router.get("/regulatoryemirfilings/analytics/metrics", response_model=Dict[str, Any])
def get_regulatoryemirfiling_metrics():
    """Calculate summary statistical KPIs for RegulatoryEMIRFiling collection."""
    svc = RegulatoryEMIRFilingService()
    return svc.calculate_aggregate_metrics()

# ==================== BasisRiskMeasurement Endpoints ====================
@router.get("/basisriskmeasurements", response_model=List[Dict[str, Any]])
def list_basisriskmeasurements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BasisRiskMeasurement records with pagination and filtering."""
    svc = BasisRiskMeasurementService()
    items = svc.list_basisriskmeasurements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/basisriskmeasurements/{item_id}", response_model=Dict[str, Any])
def get_basisriskmeasurement_by_id(item_id: int):
    """Retrieve detailed record for BasisRiskMeasurement by ID."""
    svc = BasisRiskMeasurementService()
    item = svc.get_basisriskmeasurement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BasisRiskMeasurement with ID {item_id} not found")
    return item.to_dict()

@router.post("/basisriskmeasurements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_basisriskmeasurement(payload: BasisRiskMeasurementCreateSchema):
    """Create new BasisRiskMeasurement instance in enterprise repository."""
    svc = BasisRiskMeasurementService()
    try:
        item = svc.create_basisriskmeasurement(
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

@router.put("/basisriskmeasurements/{item_id}", response_model=Dict[str, Any])
def update_basisriskmeasurement(item_id: int, payload: BasisRiskMeasurementUpdateSchema):
    """Update existing BasisRiskMeasurement record fields."""
    svc = BasisRiskMeasurementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_basisriskmeasurement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BasisRiskMeasurement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/basisriskmeasurements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_basisriskmeasurement(item_id: int, hard: bool = Query(False)):
    """Delete BasisRiskMeasurement record (soft-delete by default)."""
    svc = BasisRiskMeasurementService()
    ok = svc.delete_basisriskmeasurement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BasisRiskMeasurement with ID {item_id} not found")
    return None

@router.get("/basisriskmeasurements/analytics/metrics", response_model=Dict[str, Any])
def get_basisriskmeasurement_metrics():
    """Calculate summary statistical KPIs for BasisRiskMeasurement collection."""
    svc = BasisRiskMeasurementService()
    return svc.calculate_aggregate_metrics()

