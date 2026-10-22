"""
Dynamic Pricing & Revenue Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    PriceListMasterService,
    TieredVolumeDiscountService,
    PromotionalCampaignService,
    CustomerRebateAgreementService,
    CouponCodeRegistryService,
    CompetitorPriceMonitorService,
    MarginFloorThresholdService,
    CurrencyExchangeRateRuleService,
    DynamicSurgeMultiplierService,
    BundlePackageRuleService,
    ChannelPriceOverrideService,
    PriceChangeApprovalService,
    PromotionalPerformanceService,
    MarkdownScheduleService,
    LoyaltyPointsRuleService,
    PriceExceptionAuditService,
)
from .schemas import (
    PriceListMasterCreateSchema, PriceListMasterUpdateSchema, PriceListMasterResponseSchema,
    TieredVolumeDiscountCreateSchema, TieredVolumeDiscountUpdateSchema, TieredVolumeDiscountResponseSchema,
    PromotionalCampaignCreateSchema, PromotionalCampaignUpdateSchema, PromotionalCampaignResponseSchema,
    CustomerRebateAgreementCreateSchema, CustomerRebateAgreementUpdateSchema, CustomerRebateAgreementResponseSchema,
    CouponCodeRegistryCreateSchema, CouponCodeRegistryUpdateSchema, CouponCodeRegistryResponseSchema,
    CompetitorPriceMonitorCreateSchema, CompetitorPriceMonitorUpdateSchema, CompetitorPriceMonitorResponseSchema,
    MarginFloorThresholdCreateSchema, MarginFloorThresholdUpdateSchema, MarginFloorThresholdResponseSchema,
    CurrencyExchangeRateRuleCreateSchema, CurrencyExchangeRateRuleUpdateSchema, CurrencyExchangeRateRuleResponseSchema,
    DynamicSurgeMultiplierCreateSchema, DynamicSurgeMultiplierUpdateSchema, DynamicSurgeMultiplierResponseSchema,
    BundlePackageRuleCreateSchema, BundlePackageRuleUpdateSchema, BundlePackageRuleResponseSchema,
    ChannelPriceOverrideCreateSchema, ChannelPriceOverrideUpdateSchema, ChannelPriceOverrideResponseSchema,
    PriceChangeApprovalCreateSchema, PriceChangeApprovalUpdateSchema, PriceChangeApprovalResponseSchema,
    PromotionalPerformanceCreateSchema, PromotionalPerformanceUpdateSchema, PromotionalPerformanceResponseSchema,
    MarkdownScheduleCreateSchema, MarkdownScheduleUpdateSchema, MarkdownScheduleResponseSchema,
    LoyaltyPointsRuleCreateSchema, LoyaltyPointsRuleUpdateSchema, LoyaltyPointsRuleResponseSchema,
    PriceExceptionAuditCreateSchema, PriceExceptionAuditUpdateSchema, PriceExceptionAuditResponseSchema,
)

router = APIRouter(prefix="/pricing_promotions", tags=["Dynamic Pricing & Revenue Management"])

# ==================== PriceListMaster Endpoints ====================
@router.get("/pricelistmasters", response_model=List[Dict[str, Any]])
def list_pricelistmasters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PriceListMaster records with pagination and filtering."""
    svc = PriceListMasterService()
    items = svc.list_pricelistmasters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/pricelistmasters/{item_id}", response_model=Dict[str, Any])
def get_pricelistmaster_by_id(item_id: int):
    """Retrieve detailed record for PriceListMaster by ID."""
    svc = PriceListMasterService()
    item = svc.get_pricelistmaster_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PriceListMaster with ID {item_id} not found")
    return item.to_dict()

@router.post("/pricelistmasters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_pricelistmaster(payload: PriceListMasterCreateSchema):
    """Create new PriceListMaster instance in enterprise repository."""
    svc = PriceListMasterService()
    try:
        item = svc.create_pricelistmaster(
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

@router.put("/pricelistmasters/{item_id}", response_model=Dict[str, Any])
def update_pricelistmaster(item_id: int, payload: PriceListMasterUpdateSchema):
    """Update existing PriceListMaster record fields."""
    svc = PriceListMasterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_pricelistmaster(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PriceListMaster with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/pricelistmasters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pricelistmaster(item_id: int, hard: bool = Query(False)):
    """Delete PriceListMaster record (soft-delete by default)."""
    svc = PriceListMasterService()
    ok = svc.delete_pricelistmaster(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PriceListMaster with ID {item_id} not found")
    return None

@router.get("/pricelistmasters/analytics/metrics", response_model=Dict[str, Any])
def get_pricelistmaster_metrics():
    """Calculate summary statistical KPIs for PriceListMaster collection."""
    svc = PriceListMasterService()
    return svc.calculate_aggregate_metrics()

# ==================== TieredVolumeDiscount Endpoints ====================
@router.get("/tieredvolumediscounts", response_model=List[Dict[str, Any]])
def list_tieredvolumediscounts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TieredVolumeDiscount records with pagination and filtering."""
    svc = TieredVolumeDiscountService()
    items = svc.list_tieredvolumediscounts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tieredvolumediscounts/{item_id}", response_model=Dict[str, Any])
def get_tieredvolumediscount_by_id(item_id: int):
    """Retrieve detailed record for TieredVolumeDiscount by ID."""
    svc = TieredVolumeDiscountService()
    item = svc.get_tieredvolumediscount_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TieredVolumeDiscount with ID {item_id} not found")
    return item.to_dict()

@router.post("/tieredvolumediscounts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tieredvolumediscount(payload: TieredVolumeDiscountCreateSchema):
    """Create new TieredVolumeDiscount instance in enterprise repository."""
    svc = TieredVolumeDiscountService()
    try:
        item = svc.create_tieredvolumediscount(
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

@router.put("/tieredvolumediscounts/{item_id}", response_model=Dict[str, Any])
def update_tieredvolumediscount(item_id: int, payload: TieredVolumeDiscountUpdateSchema):
    """Update existing TieredVolumeDiscount record fields."""
    svc = TieredVolumeDiscountService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tieredvolumediscount(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TieredVolumeDiscount with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tieredvolumediscounts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tieredvolumediscount(item_id: int, hard: bool = Query(False)):
    """Delete TieredVolumeDiscount record (soft-delete by default)."""
    svc = TieredVolumeDiscountService()
    ok = svc.delete_tieredvolumediscount(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TieredVolumeDiscount with ID {item_id} not found")
    return None

@router.get("/tieredvolumediscounts/analytics/metrics", response_model=Dict[str, Any])
def get_tieredvolumediscount_metrics():
    """Calculate summary statistical KPIs for TieredVolumeDiscount collection."""
    svc = TieredVolumeDiscountService()
    return svc.calculate_aggregate_metrics()

# ==================== PromotionalCampaign Endpoints ====================
@router.get("/promotionalcampaigns", response_model=List[Dict[str, Any]])
def list_promotionalcampaigns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PromotionalCampaign records with pagination and filtering."""
    svc = PromotionalCampaignService()
    items = svc.list_promotionalcampaigns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/promotionalcampaigns/{item_id}", response_model=Dict[str, Any])
def get_promotionalcampaign_by_id(item_id: int):
    """Retrieve detailed record for PromotionalCampaign by ID."""
    svc = PromotionalCampaignService()
    item = svc.get_promotionalcampaign_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PromotionalCampaign with ID {item_id} not found")
    return item.to_dict()

@router.post("/promotionalcampaigns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_promotionalcampaign(payload: PromotionalCampaignCreateSchema):
    """Create new PromotionalCampaign instance in enterprise repository."""
    svc = PromotionalCampaignService()
    try:
        item = svc.create_promotionalcampaign(
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

@router.put("/promotionalcampaigns/{item_id}", response_model=Dict[str, Any])
def update_promotionalcampaign(item_id: int, payload: PromotionalCampaignUpdateSchema):
    """Update existing PromotionalCampaign record fields."""
    svc = PromotionalCampaignService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_promotionalcampaign(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PromotionalCampaign with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/promotionalcampaigns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotionalcampaign(item_id: int, hard: bool = Query(False)):
    """Delete PromotionalCampaign record (soft-delete by default)."""
    svc = PromotionalCampaignService()
    ok = svc.delete_promotionalcampaign(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PromotionalCampaign with ID {item_id} not found")
    return None

@router.get("/promotionalcampaigns/analytics/metrics", response_model=Dict[str, Any])
def get_promotionalcampaign_metrics():
    """Calculate summary statistical KPIs for PromotionalCampaign collection."""
    svc = PromotionalCampaignService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerRebateAgreement Endpoints ====================
@router.get("/customerrebateagreements", response_model=List[Dict[str, Any]])
def list_customerrebateagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerRebateAgreement records with pagination and filtering."""
    svc = CustomerRebateAgreementService()
    items = svc.list_customerrebateagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerrebateagreements/{item_id}", response_model=Dict[str, Any])
def get_customerrebateagreement_by_id(item_id: int):
    """Retrieve detailed record for CustomerRebateAgreement by ID."""
    svc = CustomerRebateAgreementService()
    item = svc.get_customerrebateagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerRebateAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerrebateagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerrebateagreement(payload: CustomerRebateAgreementCreateSchema):
    """Create new CustomerRebateAgreement instance in enterprise repository."""
    svc = CustomerRebateAgreementService()
    try:
        item = svc.create_customerrebateagreement(
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

@router.put("/customerrebateagreements/{item_id}", response_model=Dict[str, Any])
def update_customerrebateagreement(item_id: int, payload: CustomerRebateAgreementUpdateSchema):
    """Update existing CustomerRebateAgreement record fields."""
    svc = CustomerRebateAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerrebateagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerRebateAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerrebateagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerrebateagreement(item_id: int, hard: bool = Query(False)):
    """Delete CustomerRebateAgreement record (soft-delete by default)."""
    svc = CustomerRebateAgreementService()
    ok = svc.delete_customerrebateagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerRebateAgreement with ID {item_id} not found")
    return None

@router.get("/customerrebateagreements/analytics/metrics", response_model=Dict[str, Any])
def get_customerrebateagreement_metrics():
    """Calculate summary statistical KPIs for CustomerRebateAgreement collection."""
    svc = CustomerRebateAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== CouponCodeRegistry Endpoints ====================
@router.get("/couponcoderegistrys", response_model=List[Dict[str, Any]])
def list_couponcoderegistrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CouponCodeRegistry records with pagination and filtering."""
    svc = CouponCodeRegistryService()
    items = svc.list_couponcoderegistrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/couponcoderegistrys/{item_id}", response_model=Dict[str, Any])
def get_couponcoderegistry_by_id(item_id: int):
    """Retrieve detailed record for CouponCodeRegistry by ID."""
    svc = CouponCodeRegistryService()
    item = svc.get_couponcoderegistry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CouponCodeRegistry with ID {item_id} not found")
    return item.to_dict()

@router.post("/couponcoderegistrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_couponcoderegistry(payload: CouponCodeRegistryCreateSchema):
    """Create new CouponCodeRegistry instance in enterprise repository."""
    svc = CouponCodeRegistryService()
    try:
        item = svc.create_couponcoderegistry(
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

@router.put("/couponcoderegistrys/{item_id}", response_model=Dict[str, Any])
def update_couponcoderegistry(item_id: int, payload: CouponCodeRegistryUpdateSchema):
    """Update existing CouponCodeRegistry record fields."""
    svc = CouponCodeRegistryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_couponcoderegistry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CouponCodeRegistry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/couponcoderegistrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_couponcoderegistry(item_id: int, hard: bool = Query(False)):
    """Delete CouponCodeRegistry record (soft-delete by default)."""
    svc = CouponCodeRegistryService()
    ok = svc.delete_couponcoderegistry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CouponCodeRegistry with ID {item_id} not found")
    return None

@router.get("/couponcoderegistrys/analytics/metrics", response_model=Dict[str, Any])
def get_couponcoderegistry_metrics():
    """Calculate summary statistical KPIs for CouponCodeRegistry collection."""
    svc = CouponCodeRegistryService()
    return svc.calculate_aggregate_metrics()

# ==================== CompetitorPriceMonitor Endpoints ====================
@router.get("/competitorpricemonitors", response_model=List[Dict[str, Any]])
def list_competitorpricemonitors(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CompetitorPriceMonitor records with pagination and filtering."""
    svc = CompetitorPriceMonitorService()
    items = svc.list_competitorpricemonitors(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/competitorpricemonitors/{item_id}", response_model=Dict[str, Any])
def get_competitorpricemonitor_by_id(item_id: int):
    """Retrieve detailed record for CompetitorPriceMonitor by ID."""
    svc = CompetitorPriceMonitorService()
    item = svc.get_competitorpricemonitor_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CompetitorPriceMonitor with ID {item_id} not found")
    return item.to_dict()

@router.post("/competitorpricemonitors", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_competitorpricemonitor(payload: CompetitorPriceMonitorCreateSchema):
    """Create new CompetitorPriceMonitor instance in enterprise repository."""
    svc = CompetitorPriceMonitorService()
    try:
        item = svc.create_competitorpricemonitor(
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

@router.put("/competitorpricemonitors/{item_id}", response_model=Dict[str, Any])
def update_competitorpricemonitor(item_id: int, payload: CompetitorPriceMonitorUpdateSchema):
    """Update existing CompetitorPriceMonitor record fields."""
    svc = CompetitorPriceMonitorService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_competitorpricemonitor(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CompetitorPriceMonitor with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/competitorpricemonitors/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_competitorpricemonitor(item_id: int, hard: bool = Query(False)):
    """Delete CompetitorPriceMonitor record (soft-delete by default)."""
    svc = CompetitorPriceMonitorService()
    ok = svc.delete_competitorpricemonitor(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CompetitorPriceMonitor with ID {item_id} not found")
    return None

@router.get("/competitorpricemonitors/analytics/metrics", response_model=Dict[str, Any])
def get_competitorpricemonitor_metrics():
    """Calculate summary statistical KPIs for CompetitorPriceMonitor collection."""
    svc = CompetitorPriceMonitorService()
    return svc.calculate_aggregate_metrics()

# ==================== MarginFloorThreshold Endpoints ====================
@router.get("/marginfloorthresholds", response_model=List[Dict[str, Any]])
def list_marginfloorthresholds(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MarginFloorThreshold records with pagination and filtering."""
    svc = MarginFloorThresholdService()
    items = svc.list_marginfloorthresholds(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/marginfloorthresholds/{item_id}", response_model=Dict[str, Any])
def get_marginfloorthreshold_by_id(item_id: int):
    """Retrieve detailed record for MarginFloorThreshold by ID."""
    svc = MarginFloorThresholdService()
    item = svc.get_marginfloorthreshold_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MarginFloorThreshold with ID {item_id} not found")
    return item.to_dict()

@router.post("/marginfloorthresholds", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_marginfloorthreshold(payload: MarginFloorThresholdCreateSchema):
    """Create new MarginFloorThreshold instance in enterprise repository."""
    svc = MarginFloorThresholdService()
    try:
        item = svc.create_marginfloorthreshold(
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

@router.put("/marginfloorthresholds/{item_id}", response_model=Dict[str, Any])
def update_marginfloorthreshold(item_id: int, payload: MarginFloorThresholdUpdateSchema):
    """Update existing MarginFloorThreshold record fields."""
    svc = MarginFloorThresholdService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_marginfloorthreshold(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MarginFloorThreshold with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/marginfloorthresholds/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_marginfloorthreshold(item_id: int, hard: bool = Query(False)):
    """Delete MarginFloorThreshold record (soft-delete by default)."""
    svc = MarginFloorThresholdService()
    ok = svc.delete_marginfloorthreshold(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MarginFloorThreshold with ID {item_id} not found")
    return None

@router.get("/marginfloorthresholds/analytics/metrics", response_model=Dict[str, Any])
def get_marginfloorthreshold_metrics():
    """Calculate summary statistical KPIs for MarginFloorThreshold collection."""
    svc = MarginFloorThresholdService()
    return svc.calculate_aggregate_metrics()

# ==================== CurrencyExchangeRateRule Endpoints ====================
@router.get("/currencyexchangeraterules", response_model=List[Dict[str, Any]])
def list_currencyexchangeraterules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CurrencyExchangeRateRule records with pagination and filtering."""
    svc = CurrencyExchangeRateRuleService()
    items = svc.list_currencyexchangeraterules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/currencyexchangeraterules/{item_id}", response_model=Dict[str, Any])
def get_currencyexchangeraterule_by_id(item_id: int):
    """Retrieve detailed record for CurrencyExchangeRateRule by ID."""
    svc = CurrencyExchangeRateRuleService()
    item = svc.get_currencyexchangeraterule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CurrencyExchangeRateRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/currencyexchangeraterules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_currencyexchangeraterule(payload: CurrencyExchangeRateRuleCreateSchema):
    """Create new CurrencyExchangeRateRule instance in enterprise repository."""
    svc = CurrencyExchangeRateRuleService()
    try:
        item = svc.create_currencyexchangeraterule(
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

@router.put("/currencyexchangeraterules/{item_id}", response_model=Dict[str, Any])
def update_currencyexchangeraterule(item_id: int, payload: CurrencyExchangeRateRuleUpdateSchema):
    """Update existing CurrencyExchangeRateRule record fields."""
    svc = CurrencyExchangeRateRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_currencyexchangeraterule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CurrencyExchangeRateRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/currencyexchangeraterules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_currencyexchangeraterule(item_id: int, hard: bool = Query(False)):
    """Delete CurrencyExchangeRateRule record (soft-delete by default)."""
    svc = CurrencyExchangeRateRuleService()
    ok = svc.delete_currencyexchangeraterule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CurrencyExchangeRateRule with ID {item_id} not found")
    return None

@router.get("/currencyexchangeraterules/analytics/metrics", response_model=Dict[str, Any])
def get_currencyexchangeraterule_metrics():
    """Calculate summary statistical KPIs for CurrencyExchangeRateRule collection."""
    svc = CurrencyExchangeRateRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== DynamicSurgeMultiplier Endpoints ====================
@router.get("/dynamicsurgemultipliers", response_model=List[Dict[str, Any]])
def list_dynamicsurgemultipliers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DynamicSurgeMultiplier records with pagination and filtering."""
    svc = DynamicSurgeMultiplierService()
    items = svc.list_dynamicsurgemultipliers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dynamicsurgemultipliers/{item_id}", response_model=Dict[str, Any])
def get_dynamicsurgemultiplier_by_id(item_id: int):
    """Retrieve detailed record for DynamicSurgeMultiplier by ID."""
    svc = DynamicSurgeMultiplierService()
    item = svc.get_dynamicsurgemultiplier_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DynamicSurgeMultiplier with ID {item_id} not found")
    return item.to_dict()

@router.post("/dynamicsurgemultipliers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dynamicsurgemultiplier(payload: DynamicSurgeMultiplierCreateSchema):
    """Create new DynamicSurgeMultiplier instance in enterprise repository."""
    svc = DynamicSurgeMultiplierService()
    try:
        item = svc.create_dynamicsurgemultiplier(
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

@router.put("/dynamicsurgemultipliers/{item_id}", response_model=Dict[str, Any])
def update_dynamicsurgemultiplier(item_id: int, payload: DynamicSurgeMultiplierUpdateSchema):
    """Update existing DynamicSurgeMultiplier record fields."""
    svc = DynamicSurgeMultiplierService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dynamicsurgemultiplier(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DynamicSurgeMultiplier with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dynamicsurgemultipliers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dynamicsurgemultiplier(item_id: int, hard: bool = Query(False)):
    """Delete DynamicSurgeMultiplier record (soft-delete by default)."""
    svc = DynamicSurgeMultiplierService()
    ok = svc.delete_dynamicsurgemultiplier(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DynamicSurgeMultiplier with ID {item_id} not found")
    return None

@router.get("/dynamicsurgemultipliers/analytics/metrics", response_model=Dict[str, Any])
def get_dynamicsurgemultiplier_metrics():
    """Calculate summary statistical KPIs for DynamicSurgeMultiplier collection."""
    svc = DynamicSurgeMultiplierService()
    return svc.calculate_aggregate_metrics()

# ==================== BundlePackageRule Endpoints ====================
@router.get("/bundlepackagerules", response_model=List[Dict[str, Any]])
def list_bundlepackagerules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BundlePackageRule records with pagination and filtering."""
    svc = BundlePackageRuleService()
    items = svc.list_bundlepackagerules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bundlepackagerules/{item_id}", response_model=Dict[str, Any])
def get_bundlepackagerule_by_id(item_id: int):
    """Retrieve detailed record for BundlePackageRule by ID."""
    svc = BundlePackageRuleService()
    item = svc.get_bundlepackagerule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BundlePackageRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/bundlepackagerules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bundlepackagerule(payload: BundlePackageRuleCreateSchema):
    """Create new BundlePackageRule instance in enterprise repository."""
    svc = BundlePackageRuleService()
    try:
        item = svc.create_bundlepackagerule(
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

@router.put("/bundlepackagerules/{item_id}", response_model=Dict[str, Any])
def update_bundlepackagerule(item_id: int, payload: BundlePackageRuleUpdateSchema):
    """Update existing BundlePackageRule record fields."""
    svc = BundlePackageRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bundlepackagerule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BundlePackageRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bundlepackagerules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bundlepackagerule(item_id: int, hard: bool = Query(False)):
    """Delete BundlePackageRule record (soft-delete by default)."""
    svc = BundlePackageRuleService()
    ok = svc.delete_bundlepackagerule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BundlePackageRule with ID {item_id} not found")
    return None

@router.get("/bundlepackagerules/analytics/metrics", response_model=Dict[str, Any])
def get_bundlepackagerule_metrics():
    """Calculate summary statistical KPIs for BundlePackageRule collection."""
    svc = BundlePackageRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== ChannelPriceOverride Endpoints ====================
@router.get("/channelpriceoverrides", response_model=List[Dict[str, Any]])
def list_channelpriceoverrides(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChannelPriceOverride records with pagination and filtering."""
    svc = ChannelPriceOverrideService()
    items = svc.list_channelpriceoverrides(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/channelpriceoverrides/{item_id}", response_model=Dict[str, Any])
def get_channelpriceoverride_by_id(item_id: int):
    """Retrieve detailed record for ChannelPriceOverride by ID."""
    svc = ChannelPriceOverrideService()
    item = svc.get_channelpriceoverride_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChannelPriceOverride with ID {item_id} not found")
    return item.to_dict()

@router.post("/channelpriceoverrides", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_channelpriceoverride(payload: ChannelPriceOverrideCreateSchema):
    """Create new ChannelPriceOverride instance in enterprise repository."""
    svc = ChannelPriceOverrideService()
    try:
        item = svc.create_channelpriceoverride(
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

@router.put("/channelpriceoverrides/{item_id}", response_model=Dict[str, Any])
def update_channelpriceoverride(item_id: int, payload: ChannelPriceOverrideUpdateSchema):
    """Update existing ChannelPriceOverride record fields."""
    svc = ChannelPriceOverrideService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_channelpriceoverride(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChannelPriceOverride with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/channelpriceoverrides/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_channelpriceoverride(item_id: int, hard: bool = Query(False)):
    """Delete ChannelPriceOverride record (soft-delete by default)."""
    svc = ChannelPriceOverrideService()
    ok = svc.delete_channelpriceoverride(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChannelPriceOverride with ID {item_id} not found")
    return None

@router.get("/channelpriceoverrides/analytics/metrics", response_model=Dict[str, Any])
def get_channelpriceoverride_metrics():
    """Calculate summary statistical KPIs for ChannelPriceOverride collection."""
    svc = ChannelPriceOverrideService()
    return svc.calculate_aggregate_metrics()

# ==================== PriceChangeApproval Endpoints ====================
@router.get("/pricechangeapprovals", response_model=List[Dict[str, Any]])
def list_pricechangeapprovals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PriceChangeApproval records with pagination and filtering."""
    svc = PriceChangeApprovalService()
    items = svc.list_pricechangeapprovals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/pricechangeapprovals/{item_id}", response_model=Dict[str, Any])
def get_pricechangeapproval_by_id(item_id: int):
    """Retrieve detailed record for PriceChangeApproval by ID."""
    svc = PriceChangeApprovalService()
    item = svc.get_pricechangeapproval_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PriceChangeApproval with ID {item_id} not found")
    return item.to_dict()

@router.post("/pricechangeapprovals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_pricechangeapproval(payload: PriceChangeApprovalCreateSchema):
    """Create new PriceChangeApproval instance in enterprise repository."""
    svc = PriceChangeApprovalService()
    try:
        item = svc.create_pricechangeapproval(
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

@router.put("/pricechangeapprovals/{item_id}", response_model=Dict[str, Any])
def update_pricechangeapproval(item_id: int, payload: PriceChangeApprovalUpdateSchema):
    """Update existing PriceChangeApproval record fields."""
    svc = PriceChangeApprovalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_pricechangeapproval(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PriceChangeApproval with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/pricechangeapprovals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pricechangeapproval(item_id: int, hard: bool = Query(False)):
    """Delete PriceChangeApproval record (soft-delete by default)."""
    svc = PriceChangeApprovalService()
    ok = svc.delete_pricechangeapproval(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PriceChangeApproval with ID {item_id} not found")
    return None

@router.get("/pricechangeapprovals/analytics/metrics", response_model=Dict[str, Any])
def get_pricechangeapproval_metrics():
    """Calculate summary statistical KPIs for PriceChangeApproval collection."""
    svc = PriceChangeApprovalService()
    return svc.calculate_aggregate_metrics()

# ==================== PromotionalPerformance Endpoints ====================
@router.get("/promotionalperformances", response_model=List[Dict[str, Any]])
def list_promotionalperformances(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PromotionalPerformance records with pagination and filtering."""
    svc = PromotionalPerformanceService()
    items = svc.list_promotionalperformances(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/promotionalperformances/{item_id}", response_model=Dict[str, Any])
def get_promotionalperformance_by_id(item_id: int):
    """Retrieve detailed record for PromotionalPerformance by ID."""
    svc = PromotionalPerformanceService()
    item = svc.get_promotionalperformance_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PromotionalPerformance with ID {item_id} not found")
    return item.to_dict()

@router.post("/promotionalperformances", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_promotionalperformance(payload: PromotionalPerformanceCreateSchema):
    """Create new PromotionalPerformance instance in enterprise repository."""
    svc = PromotionalPerformanceService()
    try:
        item = svc.create_promotionalperformance(
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

@router.put("/promotionalperformances/{item_id}", response_model=Dict[str, Any])
def update_promotionalperformance(item_id: int, payload: PromotionalPerformanceUpdateSchema):
    """Update existing PromotionalPerformance record fields."""
    svc = PromotionalPerformanceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_promotionalperformance(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PromotionalPerformance with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/promotionalperformances/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotionalperformance(item_id: int, hard: bool = Query(False)):
    """Delete PromotionalPerformance record (soft-delete by default)."""
    svc = PromotionalPerformanceService()
    ok = svc.delete_promotionalperformance(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PromotionalPerformance with ID {item_id} not found")
    return None

@router.get("/promotionalperformances/analytics/metrics", response_model=Dict[str, Any])
def get_promotionalperformance_metrics():
    """Calculate summary statistical KPIs for PromotionalPerformance collection."""
    svc = PromotionalPerformanceService()
    return svc.calculate_aggregate_metrics()

# ==================== MarkdownSchedule Endpoints ====================
@router.get("/markdownschedules", response_model=List[Dict[str, Any]])
def list_markdownschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MarkdownSchedule records with pagination and filtering."""
    svc = MarkdownScheduleService()
    items = svc.list_markdownschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/markdownschedules/{item_id}", response_model=Dict[str, Any])
def get_markdownschedule_by_id(item_id: int):
    """Retrieve detailed record for MarkdownSchedule by ID."""
    svc = MarkdownScheduleService()
    item = svc.get_markdownschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MarkdownSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/markdownschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_markdownschedule(payload: MarkdownScheduleCreateSchema):
    """Create new MarkdownSchedule instance in enterprise repository."""
    svc = MarkdownScheduleService()
    try:
        item = svc.create_markdownschedule(
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

@router.put("/markdownschedules/{item_id}", response_model=Dict[str, Any])
def update_markdownschedule(item_id: int, payload: MarkdownScheduleUpdateSchema):
    """Update existing MarkdownSchedule record fields."""
    svc = MarkdownScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_markdownschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MarkdownSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/markdownschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_markdownschedule(item_id: int, hard: bool = Query(False)):
    """Delete MarkdownSchedule record (soft-delete by default)."""
    svc = MarkdownScheduleService()
    ok = svc.delete_markdownschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MarkdownSchedule with ID {item_id} not found")
    return None

@router.get("/markdownschedules/analytics/metrics", response_model=Dict[str, Any])
def get_markdownschedule_metrics():
    """Calculate summary statistical KPIs for MarkdownSchedule collection."""
    svc = MarkdownScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== LoyaltyPointsRule Endpoints ====================
@router.get("/loyaltypointsrules", response_model=List[Dict[str, Any]])
def list_loyaltypointsrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LoyaltyPointsRule records with pagination and filtering."""
    svc = LoyaltyPointsRuleService()
    items = svc.list_loyaltypointsrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/loyaltypointsrules/{item_id}", response_model=Dict[str, Any])
def get_loyaltypointsrule_by_id(item_id: int):
    """Retrieve detailed record for LoyaltyPointsRule by ID."""
    svc = LoyaltyPointsRuleService()
    item = svc.get_loyaltypointsrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LoyaltyPointsRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/loyaltypointsrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_loyaltypointsrule(payload: LoyaltyPointsRuleCreateSchema):
    """Create new LoyaltyPointsRule instance in enterprise repository."""
    svc = LoyaltyPointsRuleService()
    try:
        item = svc.create_loyaltypointsrule(
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

@router.put("/loyaltypointsrules/{item_id}", response_model=Dict[str, Any])
def update_loyaltypointsrule(item_id: int, payload: LoyaltyPointsRuleUpdateSchema):
    """Update existing LoyaltyPointsRule record fields."""
    svc = LoyaltyPointsRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_loyaltypointsrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LoyaltyPointsRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/loyaltypointsrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loyaltypointsrule(item_id: int, hard: bool = Query(False)):
    """Delete LoyaltyPointsRule record (soft-delete by default)."""
    svc = LoyaltyPointsRuleService()
    ok = svc.delete_loyaltypointsrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LoyaltyPointsRule with ID {item_id} not found")
    return None

@router.get("/loyaltypointsrules/analytics/metrics", response_model=Dict[str, Any])
def get_loyaltypointsrule_metrics():
    """Calculate summary statistical KPIs for LoyaltyPointsRule collection."""
    svc = LoyaltyPointsRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== PriceExceptionAudit Endpoints ====================
@router.get("/priceexceptionaudits", response_model=List[Dict[str, Any]])
def list_priceexceptionaudits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PriceExceptionAudit records with pagination and filtering."""
    svc = PriceExceptionAuditService()
    items = svc.list_priceexceptionaudits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/priceexceptionaudits/{item_id}", response_model=Dict[str, Any])
def get_priceexceptionaudit_by_id(item_id: int):
    """Retrieve detailed record for PriceExceptionAudit by ID."""
    svc = PriceExceptionAuditService()
    item = svc.get_priceexceptionaudit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PriceExceptionAudit with ID {item_id} not found")
    return item.to_dict()

@router.post("/priceexceptionaudits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_priceexceptionaudit(payload: PriceExceptionAuditCreateSchema):
    """Create new PriceExceptionAudit instance in enterprise repository."""
    svc = PriceExceptionAuditService()
    try:
        item = svc.create_priceexceptionaudit(
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

@router.put("/priceexceptionaudits/{item_id}", response_model=Dict[str, Any])
def update_priceexceptionaudit(item_id: int, payload: PriceExceptionAuditUpdateSchema):
    """Update existing PriceExceptionAudit record fields."""
    svc = PriceExceptionAuditService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_priceexceptionaudit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PriceExceptionAudit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/priceexceptionaudits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_priceexceptionaudit(item_id: int, hard: bool = Query(False)):
    """Delete PriceExceptionAudit record (soft-delete by default)."""
    svc = PriceExceptionAuditService()
    ok = svc.delete_priceexceptionaudit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PriceExceptionAudit with ID {item_id} not found")
    return None

@router.get("/priceexceptionaudits/analytics/metrics", response_model=Dict[str, Any])
def get_priceexceptionaudit_metrics():
    """Calculate summary statistical KPIs for PriceExceptionAudit collection."""
    svc = PriceExceptionAuditService()
    return svc.calculate_aggregate_metrics()

