"""
Omnichannel Point-of-Sale (POS) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    POSRegisterService,
    POSTransactionService,
    CashDrawerService,
    TenderSplitService,
    GiftCardService,
    CouponVoucherService,
    PromotionRuleService,
    ReturnExchangeService,
    TerminalSessionService,
    ZReportService,
    OfflineReceiptService,
    HardwareDeviceService,
    PriceOverrideService,
    CustomerLoyaltyService,
    LayawayOrderService,
    StockReservationService,
)
from .schemas import (
    POSRegisterCreateSchema, POSRegisterUpdateSchema, POSRegisterResponseSchema,
    POSTransactionCreateSchema, POSTransactionUpdateSchema, POSTransactionResponseSchema,
    CashDrawerCreateSchema, CashDrawerUpdateSchema, CashDrawerResponseSchema,
    TenderSplitCreateSchema, TenderSplitUpdateSchema, TenderSplitResponseSchema,
    GiftCardCreateSchema, GiftCardUpdateSchema, GiftCardResponseSchema,
    CouponVoucherCreateSchema, CouponVoucherUpdateSchema, CouponVoucherResponseSchema,
    PromotionRuleCreateSchema, PromotionRuleUpdateSchema, PromotionRuleResponseSchema,
    ReturnExchangeCreateSchema, ReturnExchangeUpdateSchema, ReturnExchangeResponseSchema,
    TerminalSessionCreateSchema, TerminalSessionUpdateSchema, TerminalSessionResponseSchema,
    ZReportCreateSchema, ZReportUpdateSchema, ZReportResponseSchema,
    OfflineReceiptCreateSchema, OfflineReceiptUpdateSchema, OfflineReceiptResponseSchema,
    HardwareDeviceCreateSchema, HardwareDeviceUpdateSchema, HardwareDeviceResponseSchema,
    PriceOverrideCreateSchema, PriceOverrideUpdateSchema, PriceOverrideResponseSchema,
    CustomerLoyaltyCreateSchema, CustomerLoyaltyUpdateSchema, CustomerLoyaltyResponseSchema,
    LayawayOrderCreateSchema, LayawayOrderUpdateSchema, LayawayOrderResponseSchema,
    StockReservationCreateSchema, StockReservationUpdateSchema, StockReservationResponseSchema,
)

router = APIRouter(prefix="/pos", tags=["Omnichannel Point-of-Sale (POS)"])

# ==================== POSRegister Endpoints ====================
@router.get("/posregisters", response_model=List[Dict[str, Any]])
def list_posregisters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List POSRegister records with pagination and filtering."""
    svc = POSRegisterService()
    items = svc.list_posregisters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/posregisters/{item_id}", response_model=Dict[str, Any])
def get_posregister_by_id(item_id: int):
    """Retrieve detailed record for POSRegister by ID."""
    svc = POSRegisterService()
    item = svc.get_posregister_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"POSRegister with ID {item_id} not found")
    return item.to_dict()

@router.post("/posregisters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_posregister(payload: POSRegisterCreateSchema):
    """Create new POSRegister instance in enterprise repository."""
    svc = POSRegisterService()
    try:
        item = svc.create_posregister(
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

@router.put("/posregisters/{item_id}", response_model=Dict[str, Any])
def update_posregister(item_id: int, payload: POSRegisterUpdateSchema):
    """Update existing POSRegister record fields."""
    svc = POSRegisterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_posregister(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"POSRegister with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/posregisters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posregister(item_id: int, hard: bool = Query(False)):
    """Delete POSRegister record (soft-delete by default)."""
    svc = POSRegisterService()
    ok = svc.delete_posregister(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"POSRegister with ID {item_id} not found")
    return None

@router.get("/posregisters/analytics/metrics", response_model=Dict[str, Any])
def get_posregister_metrics():
    """Calculate summary statistical KPIs for POSRegister collection."""
    svc = POSRegisterService()
    return svc.calculate_aggregate_metrics()

# ==================== POSTransaction Endpoints ====================
@router.get("/postransactions", response_model=List[Dict[str, Any]])
def list_postransactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List POSTransaction records with pagination and filtering."""
    svc = POSTransactionService()
    items = svc.list_postransactions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/postransactions/{item_id}", response_model=Dict[str, Any])
def get_postransaction_by_id(item_id: int):
    """Retrieve detailed record for POSTransaction by ID."""
    svc = POSTransactionService()
    item = svc.get_postransaction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"POSTransaction with ID {item_id} not found")
    return item.to_dict()

@router.post("/postransactions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_postransaction(payload: POSTransactionCreateSchema):
    """Create new POSTransaction instance in enterprise repository."""
    svc = POSTransactionService()
    try:
        item = svc.create_postransaction(
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

@router.put("/postransactions/{item_id}", response_model=Dict[str, Any])
def update_postransaction(item_id: int, payload: POSTransactionUpdateSchema):
    """Update existing POSTransaction record fields."""
    svc = POSTransactionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_postransaction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"POSTransaction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/postransactions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_postransaction(item_id: int, hard: bool = Query(False)):
    """Delete POSTransaction record (soft-delete by default)."""
    svc = POSTransactionService()
    ok = svc.delete_postransaction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"POSTransaction with ID {item_id} not found")
    return None

@router.get("/postransactions/analytics/metrics", response_model=Dict[str, Any])
def get_postransaction_metrics():
    """Calculate summary statistical KPIs for POSTransaction collection."""
    svc = POSTransactionService()
    return svc.calculate_aggregate_metrics()

# ==================== CashDrawer Endpoints ====================
@router.get("/cashdrawers", response_model=List[Dict[str, Any]])
def list_cashdrawers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CashDrawer records with pagination and filtering."""
    svc = CashDrawerService()
    items = svc.list_cashdrawers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cashdrawers/{item_id}", response_model=Dict[str, Any])
def get_cashdrawer_by_id(item_id: int):
    """Retrieve detailed record for CashDrawer by ID."""
    svc = CashDrawerService()
    item = svc.get_cashdrawer_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CashDrawer with ID {item_id} not found")
    return item.to_dict()

@router.post("/cashdrawers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cashdrawer(payload: CashDrawerCreateSchema):
    """Create new CashDrawer instance in enterprise repository."""
    svc = CashDrawerService()
    try:
        item = svc.create_cashdrawer(
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

@router.put("/cashdrawers/{item_id}", response_model=Dict[str, Any])
def update_cashdrawer(item_id: int, payload: CashDrawerUpdateSchema):
    """Update existing CashDrawer record fields."""
    svc = CashDrawerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cashdrawer(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CashDrawer with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cashdrawers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cashdrawer(item_id: int, hard: bool = Query(False)):
    """Delete CashDrawer record (soft-delete by default)."""
    svc = CashDrawerService()
    ok = svc.delete_cashdrawer(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CashDrawer with ID {item_id} not found")
    return None

@router.get("/cashdrawers/analytics/metrics", response_model=Dict[str, Any])
def get_cashdrawer_metrics():
    """Calculate summary statistical KPIs for CashDrawer collection."""
    svc = CashDrawerService()
    return svc.calculate_aggregate_metrics()

# ==================== TenderSplit Endpoints ====================
@router.get("/tendersplits", response_model=List[Dict[str, Any]])
def list_tendersplits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TenderSplit records with pagination and filtering."""
    svc = TenderSplitService()
    items = svc.list_tendersplits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tendersplits/{item_id}", response_model=Dict[str, Any])
def get_tendersplit_by_id(item_id: int):
    """Retrieve detailed record for TenderSplit by ID."""
    svc = TenderSplitService()
    item = svc.get_tendersplit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TenderSplit with ID {item_id} not found")
    return item.to_dict()

@router.post("/tendersplits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tendersplit(payload: TenderSplitCreateSchema):
    """Create new TenderSplit instance in enterprise repository."""
    svc = TenderSplitService()
    try:
        item = svc.create_tendersplit(
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

@router.put("/tendersplits/{item_id}", response_model=Dict[str, Any])
def update_tendersplit(item_id: int, payload: TenderSplitUpdateSchema):
    """Update existing TenderSplit record fields."""
    svc = TenderSplitService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tendersplit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TenderSplit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tendersplits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tendersplit(item_id: int, hard: bool = Query(False)):
    """Delete TenderSplit record (soft-delete by default)."""
    svc = TenderSplitService()
    ok = svc.delete_tendersplit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TenderSplit with ID {item_id} not found")
    return None

@router.get("/tendersplits/analytics/metrics", response_model=Dict[str, Any])
def get_tendersplit_metrics():
    """Calculate summary statistical KPIs for TenderSplit collection."""
    svc = TenderSplitService()
    return svc.calculate_aggregate_metrics()

# ==================== GiftCard Endpoints ====================
@router.get("/giftcards", response_model=List[Dict[str, Any]])
def list_giftcards(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GiftCard records with pagination and filtering."""
    svc = GiftCardService()
    items = svc.list_giftcards(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/giftcards/{item_id}", response_model=Dict[str, Any])
def get_giftcard_by_id(item_id: int):
    """Retrieve detailed record for GiftCard by ID."""
    svc = GiftCardService()
    item = svc.get_giftcard_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GiftCard with ID {item_id} not found")
    return item.to_dict()

@router.post("/giftcards", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_giftcard(payload: GiftCardCreateSchema):
    """Create new GiftCard instance in enterprise repository."""
    svc = GiftCardService()
    try:
        item = svc.create_giftcard(
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

@router.put("/giftcards/{item_id}", response_model=Dict[str, Any])
def update_giftcard(item_id: int, payload: GiftCardUpdateSchema):
    """Update existing GiftCard record fields."""
    svc = GiftCardService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_giftcard(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GiftCard with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/giftcards/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_giftcard(item_id: int, hard: bool = Query(False)):
    """Delete GiftCard record (soft-delete by default)."""
    svc = GiftCardService()
    ok = svc.delete_giftcard(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GiftCard with ID {item_id} not found")
    return None

@router.get("/giftcards/analytics/metrics", response_model=Dict[str, Any])
def get_giftcard_metrics():
    """Calculate summary statistical KPIs for GiftCard collection."""
    svc = GiftCardService()
    return svc.calculate_aggregate_metrics()

# ==================== CouponVoucher Endpoints ====================
@router.get("/couponvouchers", response_model=List[Dict[str, Any]])
def list_couponvouchers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CouponVoucher records with pagination and filtering."""
    svc = CouponVoucherService()
    items = svc.list_couponvouchers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/couponvouchers/{item_id}", response_model=Dict[str, Any])
def get_couponvoucher_by_id(item_id: int):
    """Retrieve detailed record for CouponVoucher by ID."""
    svc = CouponVoucherService()
    item = svc.get_couponvoucher_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CouponVoucher with ID {item_id} not found")
    return item.to_dict()

@router.post("/couponvouchers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_couponvoucher(payload: CouponVoucherCreateSchema):
    """Create new CouponVoucher instance in enterprise repository."""
    svc = CouponVoucherService()
    try:
        item = svc.create_couponvoucher(
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

@router.put("/couponvouchers/{item_id}", response_model=Dict[str, Any])
def update_couponvoucher(item_id: int, payload: CouponVoucherUpdateSchema):
    """Update existing CouponVoucher record fields."""
    svc = CouponVoucherService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_couponvoucher(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CouponVoucher with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/couponvouchers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_couponvoucher(item_id: int, hard: bool = Query(False)):
    """Delete CouponVoucher record (soft-delete by default)."""
    svc = CouponVoucherService()
    ok = svc.delete_couponvoucher(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CouponVoucher with ID {item_id} not found")
    return None

@router.get("/couponvouchers/analytics/metrics", response_model=Dict[str, Any])
def get_couponvoucher_metrics():
    """Calculate summary statistical KPIs for CouponVoucher collection."""
    svc = CouponVoucherService()
    return svc.calculate_aggregate_metrics()

# ==================== PromotionRule Endpoints ====================
@router.get("/promotionrules", response_model=List[Dict[str, Any]])
def list_promotionrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PromotionRule records with pagination and filtering."""
    svc = PromotionRuleService()
    items = svc.list_promotionrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/promotionrules/{item_id}", response_model=Dict[str, Any])
def get_promotionrule_by_id(item_id: int):
    """Retrieve detailed record for PromotionRule by ID."""
    svc = PromotionRuleService()
    item = svc.get_promotionrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PromotionRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/promotionrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_promotionrule(payload: PromotionRuleCreateSchema):
    """Create new PromotionRule instance in enterprise repository."""
    svc = PromotionRuleService()
    try:
        item = svc.create_promotionrule(
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

@router.put("/promotionrules/{item_id}", response_model=Dict[str, Any])
def update_promotionrule(item_id: int, payload: PromotionRuleUpdateSchema):
    """Update existing PromotionRule record fields."""
    svc = PromotionRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_promotionrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PromotionRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/promotionrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotionrule(item_id: int, hard: bool = Query(False)):
    """Delete PromotionRule record (soft-delete by default)."""
    svc = PromotionRuleService()
    ok = svc.delete_promotionrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PromotionRule with ID {item_id} not found")
    return None

@router.get("/promotionrules/analytics/metrics", response_model=Dict[str, Any])
def get_promotionrule_metrics():
    """Calculate summary statistical KPIs for PromotionRule collection."""
    svc = PromotionRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== ReturnExchange Endpoints ====================
@router.get("/returnexchanges", response_model=List[Dict[str, Any]])
def list_returnexchanges(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReturnExchange records with pagination and filtering."""
    svc = ReturnExchangeService()
    items = svc.list_returnexchanges(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/returnexchanges/{item_id}", response_model=Dict[str, Any])
def get_returnexchange_by_id(item_id: int):
    """Retrieve detailed record for ReturnExchange by ID."""
    svc = ReturnExchangeService()
    item = svc.get_returnexchange_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReturnExchange with ID {item_id} not found")
    return item.to_dict()

@router.post("/returnexchanges", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_returnexchange(payload: ReturnExchangeCreateSchema):
    """Create new ReturnExchange instance in enterprise repository."""
    svc = ReturnExchangeService()
    try:
        item = svc.create_returnexchange(
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

@router.put("/returnexchanges/{item_id}", response_model=Dict[str, Any])
def update_returnexchange(item_id: int, payload: ReturnExchangeUpdateSchema):
    """Update existing ReturnExchange record fields."""
    svc = ReturnExchangeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_returnexchange(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReturnExchange with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/returnexchanges/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_returnexchange(item_id: int, hard: bool = Query(False)):
    """Delete ReturnExchange record (soft-delete by default)."""
    svc = ReturnExchangeService()
    ok = svc.delete_returnexchange(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReturnExchange with ID {item_id} not found")
    return None

@router.get("/returnexchanges/analytics/metrics", response_model=Dict[str, Any])
def get_returnexchange_metrics():
    """Calculate summary statistical KPIs for ReturnExchange collection."""
    svc = ReturnExchangeService()
    return svc.calculate_aggregate_metrics()

# ==================== TerminalSession Endpoints ====================
@router.get("/terminalsessions", response_model=List[Dict[str, Any]])
def list_terminalsessions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TerminalSession records with pagination and filtering."""
    svc = TerminalSessionService()
    items = svc.list_terminalsessions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/terminalsessions/{item_id}", response_model=Dict[str, Any])
def get_terminalsession_by_id(item_id: int):
    """Retrieve detailed record for TerminalSession by ID."""
    svc = TerminalSessionService()
    item = svc.get_terminalsession_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TerminalSession with ID {item_id} not found")
    return item.to_dict()

@router.post("/terminalsessions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_terminalsession(payload: TerminalSessionCreateSchema):
    """Create new TerminalSession instance in enterprise repository."""
    svc = TerminalSessionService()
    try:
        item = svc.create_terminalsession(
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

@router.put("/terminalsessions/{item_id}", response_model=Dict[str, Any])
def update_terminalsession(item_id: int, payload: TerminalSessionUpdateSchema):
    """Update existing TerminalSession record fields."""
    svc = TerminalSessionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_terminalsession(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TerminalSession with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/terminalsessions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_terminalsession(item_id: int, hard: bool = Query(False)):
    """Delete TerminalSession record (soft-delete by default)."""
    svc = TerminalSessionService()
    ok = svc.delete_terminalsession(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TerminalSession with ID {item_id} not found")
    return None

@router.get("/terminalsessions/analytics/metrics", response_model=Dict[str, Any])
def get_terminalsession_metrics():
    """Calculate summary statistical KPIs for TerminalSession collection."""
    svc = TerminalSessionService()
    return svc.calculate_aggregate_metrics()

# ==================== ZReport Endpoints ====================
@router.get("/zreports", response_model=List[Dict[str, Any]])
def list_zreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ZReport records with pagination and filtering."""
    svc = ZReportService()
    items = svc.list_zreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/zreports/{item_id}", response_model=Dict[str, Any])
def get_zreport_by_id(item_id: int):
    """Retrieve detailed record for ZReport by ID."""
    svc = ZReportService()
    item = svc.get_zreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ZReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/zreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_zreport(payload: ZReportCreateSchema):
    """Create new ZReport instance in enterprise repository."""
    svc = ZReportService()
    try:
        item = svc.create_zreport(
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

@router.put("/zreports/{item_id}", response_model=Dict[str, Any])
def update_zreport(item_id: int, payload: ZReportUpdateSchema):
    """Update existing ZReport record fields."""
    svc = ZReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_zreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ZReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/zreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_zreport(item_id: int, hard: bool = Query(False)):
    """Delete ZReport record (soft-delete by default)."""
    svc = ZReportService()
    ok = svc.delete_zreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ZReport with ID {item_id} not found")
    return None

@router.get("/zreports/analytics/metrics", response_model=Dict[str, Any])
def get_zreport_metrics():
    """Calculate summary statistical KPIs for ZReport collection."""
    svc = ZReportService()
    return svc.calculate_aggregate_metrics()

# ==================== OfflineReceipt Endpoints ====================
@router.get("/offlinereceipts", response_model=List[Dict[str, Any]])
def list_offlinereceipts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OfflineReceipt records with pagination and filtering."""
    svc = OfflineReceiptService()
    items = svc.list_offlinereceipts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/offlinereceipts/{item_id}", response_model=Dict[str, Any])
def get_offlinereceipt_by_id(item_id: int):
    """Retrieve detailed record for OfflineReceipt by ID."""
    svc = OfflineReceiptService()
    item = svc.get_offlinereceipt_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OfflineReceipt with ID {item_id} not found")
    return item.to_dict()

@router.post("/offlinereceipts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_offlinereceipt(payload: OfflineReceiptCreateSchema):
    """Create new OfflineReceipt instance in enterprise repository."""
    svc = OfflineReceiptService()
    try:
        item = svc.create_offlinereceipt(
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

@router.put("/offlinereceipts/{item_id}", response_model=Dict[str, Any])
def update_offlinereceipt(item_id: int, payload: OfflineReceiptUpdateSchema):
    """Update existing OfflineReceipt record fields."""
    svc = OfflineReceiptService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_offlinereceipt(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OfflineReceipt with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/offlinereceipts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_offlinereceipt(item_id: int, hard: bool = Query(False)):
    """Delete OfflineReceipt record (soft-delete by default)."""
    svc = OfflineReceiptService()
    ok = svc.delete_offlinereceipt(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OfflineReceipt with ID {item_id} not found")
    return None

@router.get("/offlinereceipts/analytics/metrics", response_model=Dict[str, Any])
def get_offlinereceipt_metrics():
    """Calculate summary statistical KPIs for OfflineReceipt collection."""
    svc = OfflineReceiptService()
    return svc.calculate_aggregate_metrics()

# ==================== HardwareDevice Endpoints ====================
@router.get("/hardwaredevices", response_model=List[Dict[str, Any]])
def list_hardwaredevices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HardwareDevice records with pagination and filtering."""
    svc = HardwareDeviceService()
    items = svc.list_hardwaredevices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hardwaredevices/{item_id}", response_model=Dict[str, Any])
def get_hardwaredevice_by_id(item_id: int):
    """Retrieve detailed record for HardwareDevice by ID."""
    svc = HardwareDeviceService()
    item = svc.get_hardwaredevice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HardwareDevice with ID {item_id} not found")
    return item.to_dict()

@router.post("/hardwaredevices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hardwaredevice(payload: HardwareDeviceCreateSchema):
    """Create new HardwareDevice instance in enterprise repository."""
    svc = HardwareDeviceService()
    try:
        item = svc.create_hardwaredevice(
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

@router.put("/hardwaredevices/{item_id}", response_model=Dict[str, Any])
def update_hardwaredevice(item_id: int, payload: HardwareDeviceUpdateSchema):
    """Update existing HardwareDevice record fields."""
    svc = HardwareDeviceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hardwaredevice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HardwareDevice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hardwaredevices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hardwaredevice(item_id: int, hard: bool = Query(False)):
    """Delete HardwareDevice record (soft-delete by default)."""
    svc = HardwareDeviceService()
    ok = svc.delete_hardwaredevice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HardwareDevice with ID {item_id} not found")
    return None

@router.get("/hardwaredevices/analytics/metrics", response_model=Dict[str, Any])
def get_hardwaredevice_metrics():
    """Calculate summary statistical KPIs for HardwareDevice collection."""
    svc = HardwareDeviceService()
    return svc.calculate_aggregate_metrics()

# ==================== PriceOverride Endpoints ====================
@router.get("/priceoverrides", response_model=List[Dict[str, Any]])
def list_priceoverrides(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PriceOverride records with pagination and filtering."""
    svc = PriceOverrideService()
    items = svc.list_priceoverrides(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/priceoverrides/{item_id}", response_model=Dict[str, Any])
def get_priceoverride_by_id(item_id: int):
    """Retrieve detailed record for PriceOverride by ID."""
    svc = PriceOverrideService()
    item = svc.get_priceoverride_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PriceOverride with ID {item_id} not found")
    return item.to_dict()

@router.post("/priceoverrides", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_priceoverride(payload: PriceOverrideCreateSchema):
    """Create new PriceOverride instance in enterprise repository."""
    svc = PriceOverrideService()
    try:
        item = svc.create_priceoverride(
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

@router.put("/priceoverrides/{item_id}", response_model=Dict[str, Any])
def update_priceoverride(item_id: int, payload: PriceOverrideUpdateSchema):
    """Update existing PriceOverride record fields."""
    svc = PriceOverrideService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_priceoverride(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PriceOverride with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/priceoverrides/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_priceoverride(item_id: int, hard: bool = Query(False)):
    """Delete PriceOverride record (soft-delete by default)."""
    svc = PriceOverrideService()
    ok = svc.delete_priceoverride(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PriceOverride with ID {item_id} not found")
    return None

@router.get("/priceoverrides/analytics/metrics", response_model=Dict[str, Any])
def get_priceoverride_metrics():
    """Calculate summary statistical KPIs for PriceOverride collection."""
    svc = PriceOverrideService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerLoyalty Endpoints ====================
@router.get("/customerloyaltys", response_model=List[Dict[str, Any]])
def list_customerloyaltys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerLoyalty records with pagination and filtering."""
    svc = CustomerLoyaltyService()
    items = svc.list_customerloyaltys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerloyaltys/{item_id}", response_model=Dict[str, Any])
def get_customerloyalty_by_id(item_id: int):
    """Retrieve detailed record for CustomerLoyalty by ID."""
    svc = CustomerLoyaltyService()
    item = svc.get_customerloyalty_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerLoyalty with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerloyaltys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerloyalty(payload: CustomerLoyaltyCreateSchema):
    """Create new CustomerLoyalty instance in enterprise repository."""
    svc = CustomerLoyaltyService()
    try:
        item = svc.create_customerloyalty(
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

@router.put("/customerloyaltys/{item_id}", response_model=Dict[str, Any])
def update_customerloyalty(item_id: int, payload: CustomerLoyaltyUpdateSchema):
    """Update existing CustomerLoyalty record fields."""
    svc = CustomerLoyaltyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerloyalty(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerLoyalty with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerloyaltys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerloyalty(item_id: int, hard: bool = Query(False)):
    """Delete CustomerLoyalty record (soft-delete by default)."""
    svc = CustomerLoyaltyService()
    ok = svc.delete_customerloyalty(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerLoyalty with ID {item_id} not found")
    return None

@router.get("/customerloyaltys/analytics/metrics", response_model=Dict[str, Any])
def get_customerloyalty_metrics():
    """Calculate summary statistical KPIs for CustomerLoyalty collection."""
    svc = CustomerLoyaltyService()
    return svc.calculate_aggregate_metrics()

# ==================== LayawayOrder Endpoints ====================
@router.get("/layawayorders", response_model=List[Dict[str, Any]])
def list_layawayorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LayawayOrder records with pagination and filtering."""
    svc = LayawayOrderService()
    items = svc.list_layawayorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/layawayorders/{item_id}", response_model=Dict[str, Any])
def get_layawayorder_by_id(item_id: int):
    """Retrieve detailed record for LayawayOrder by ID."""
    svc = LayawayOrderService()
    item = svc.get_layawayorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LayawayOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/layawayorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_layawayorder(payload: LayawayOrderCreateSchema):
    """Create new LayawayOrder instance in enterprise repository."""
    svc = LayawayOrderService()
    try:
        item = svc.create_layawayorder(
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

@router.put("/layawayorders/{item_id}", response_model=Dict[str, Any])
def update_layawayorder(item_id: int, payload: LayawayOrderUpdateSchema):
    """Update existing LayawayOrder record fields."""
    svc = LayawayOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_layawayorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LayawayOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/layawayorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_layawayorder(item_id: int, hard: bool = Query(False)):
    """Delete LayawayOrder record (soft-delete by default)."""
    svc = LayawayOrderService()
    ok = svc.delete_layawayorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LayawayOrder with ID {item_id} not found")
    return None

@router.get("/layawayorders/analytics/metrics", response_model=Dict[str, Any])
def get_layawayorder_metrics():
    """Calculate summary statistical KPIs for LayawayOrder collection."""
    svc = LayawayOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== StockReservation Endpoints ====================
@router.get("/stockreservations", response_model=List[Dict[str, Any]])
def list_stockreservations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StockReservation records with pagination and filtering."""
    svc = StockReservationService()
    items = svc.list_stockreservations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/stockreservations/{item_id}", response_model=Dict[str, Any])
def get_stockreservation_by_id(item_id: int):
    """Retrieve detailed record for StockReservation by ID."""
    svc = StockReservationService()
    item = svc.get_stockreservation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StockReservation with ID {item_id} not found")
    return item.to_dict()

@router.post("/stockreservations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_stockreservation(payload: StockReservationCreateSchema):
    """Create new StockReservation instance in enterprise repository."""
    svc = StockReservationService()
    try:
        item = svc.create_stockreservation(
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

@router.put("/stockreservations/{item_id}", response_model=Dict[str, Any])
def update_stockreservation(item_id: int, payload: StockReservationUpdateSchema):
    """Update existing StockReservation record fields."""
    svc = StockReservationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_stockreservation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StockReservation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/stockreservations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stockreservation(item_id: int, hard: bool = Query(False)):
    """Delete StockReservation record (soft-delete by default)."""
    svc = StockReservationService()
    ok = svc.delete_stockreservation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StockReservation with ID {item_id} not found")
    return None

@router.get("/stockreservations/analytics/metrics", response_model=Dict[str, Any])
def get_stockreservation_metrics():
    """Calculate summary statistical KPIs for StockReservation collection."""
    svc = StockReservationService()
    return svc.calculate_aggregate_metrics()

