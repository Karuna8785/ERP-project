"""
Subscription Billing & Revenue Recognition - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    SubscriptionPlanService,
    CustomerSubscriptionService,
    BillingIntervalScheduleService,
    MeteredUsageEventService,
    InvoiceChargeItemService,
    DiscountCouponService,
    PaymentMethodProfileService,
    DunningSequenceService,
    RevenueContractASC606Service,
    PerformanceObligationService,
    DeferredRevenueAmortizationService,
    CreditBalanceAdjustmentService,
    ChurnNoticeService,
    UsageTierTieringService,
    TaxJurisdictionRuleService,
    BillingReconciliationService,
)
from .schemas import (
    SubscriptionPlanCreateSchema, SubscriptionPlanUpdateSchema, SubscriptionPlanResponseSchema,
    CustomerSubscriptionCreateSchema, CustomerSubscriptionUpdateSchema, CustomerSubscriptionResponseSchema,
    BillingIntervalScheduleCreateSchema, BillingIntervalScheduleUpdateSchema, BillingIntervalScheduleResponseSchema,
    MeteredUsageEventCreateSchema, MeteredUsageEventUpdateSchema, MeteredUsageEventResponseSchema,
    InvoiceChargeItemCreateSchema, InvoiceChargeItemUpdateSchema, InvoiceChargeItemResponseSchema,
    DiscountCouponCreateSchema, DiscountCouponUpdateSchema, DiscountCouponResponseSchema,
    PaymentMethodProfileCreateSchema, PaymentMethodProfileUpdateSchema, PaymentMethodProfileResponseSchema,
    DunningSequenceCreateSchema, DunningSequenceUpdateSchema, DunningSequenceResponseSchema,
    RevenueContractASC606CreateSchema, RevenueContractASC606UpdateSchema, RevenueContractASC606ResponseSchema,
    PerformanceObligationCreateSchema, PerformanceObligationUpdateSchema, PerformanceObligationResponseSchema,
    DeferredRevenueAmortizationCreateSchema, DeferredRevenueAmortizationUpdateSchema, DeferredRevenueAmortizationResponseSchema,
    CreditBalanceAdjustmentCreateSchema, CreditBalanceAdjustmentUpdateSchema, CreditBalanceAdjustmentResponseSchema,
    ChurnNoticeCreateSchema, ChurnNoticeUpdateSchema, ChurnNoticeResponseSchema,
    UsageTierTieringCreateSchema, UsageTierTieringUpdateSchema, UsageTierTieringResponseSchema,
    TaxJurisdictionRuleCreateSchema, TaxJurisdictionRuleUpdateSchema, TaxJurisdictionRuleResponseSchema,
    BillingReconciliationCreateSchema, BillingReconciliationUpdateSchema, BillingReconciliationResponseSchema,
)

router = APIRouter(prefix="/billing_subscriptions", tags=["Subscription Billing & Revenue Recognition"])

# ==================== SubscriptionPlan Endpoints ====================
@router.get("/subscriptionplans", response_model=List[Dict[str, Any]])
def list_subscriptionplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SubscriptionPlan records with pagination and filtering."""
    svc = SubscriptionPlanService()
    items = svc.list_subscriptionplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/subscriptionplans/{item_id}", response_model=Dict[str, Any])
def get_subscriptionplan_by_id(item_id: int):
    """Retrieve detailed record for SubscriptionPlan by ID."""
    svc = SubscriptionPlanService()
    item = svc.get_subscriptionplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SubscriptionPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/subscriptionplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_subscriptionplan(payload: SubscriptionPlanCreateSchema):
    """Create new SubscriptionPlan instance in enterprise repository."""
    svc = SubscriptionPlanService()
    try:
        item = svc.create_subscriptionplan(
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

@router.put("/subscriptionplans/{item_id}", response_model=Dict[str, Any])
def update_subscriptionplan(item_id: int, payload: SubscriptionPlanUpdateSchema):
    """Update existing SubscriptionPlan record fields."""
    svc = SubscriptionPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_subscriptionplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SubscriptionPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/subscriptionplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subscriptionplan(item_id: int, hard: bool = Query(False)):
    """Delete SubscriptionPlan record (soft-delete by default)."""
    svc = SubscriptionPlanService()
    ok = svc.delete_subscriptionplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SubscriptionPlan with ID {item_id} not found")
    return None

@router.get("/subscriptionplans/analytics/metrics", response_model=Dict[str, Any])
def get_subscriptionplan_metrics():
    """Calculate summary statistical KPIs for SubscriptionPlan collection."""
    svc = SubscriptionPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerSubscription Endpoints ====================
@router.get("/customersubscriptions", response_model=List[Dict[str, Any]])
def list_customersubscriptions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerSubscription records with pagination and filtering."""
    svc = CustomerSubscriptionService()
    items = svc.list_customersubscriptions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customersubscriptions/{item_id}", response_model=Dict[str, Any])
def get_customersubscription_by_id(item_id: int):
    """Retrieve detailed record for CustomerSubscription by ID."""
    svc = CustomerSubscriptionService()
    item = svc.get_customersubscription_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerSubscription with ID {item_id} not found")
    return item.to_dict()

@router.post("/customersubscriptions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customersubscription(payload: CustomerSubscriptionCreateSchema):
    """Create new CustomerSubscription instance in enterprise repository."""
    svc = CustomerSubscriptionService()
    try:
        item = svc.create_customersubscription(
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

@router.put("/customersubscriptions/{item_id}", response_model=Dict[str, Any])
def update_customersubscription(item_id: int, payload: CustomerSubscriptionUpdateSchema):
    """Update existing CustomerSubscription record fields."""
    svc = CustomerSubscriptionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customersubscription(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerSubscription with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customersubscriptions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customersubscription(item_id: int, hard: bool = Query(False)):
    """Delete CustomerSubscription record (soft-delete by default)."""
    svc = CustomerSubscriptionService()
    ok = svc.delete_customersubscription(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerSubscription with ID {item_id} not found")
    return None

@router.get("/customersubscriptions/analytics/metrics", response_model=Dict[str, Any])
def get_customersubscription_metrics():
    """Calculate summary statistical KPIs for CustomerSubscription collection."""
    svc = CustomerSubscriptionService()
    return svc.calculate_aggregate_metrics()

# ==================== BillingIntervalSchedule Endpoints ====================
@router.get("/billingintervalschedules", response_model=List[Dict[str, Any]])
def list_billingintervalschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BillingIntervalSchedule records with pagination and filtering."""
    svc = BillingIntervalScheduleService()
    items = svc.list_billingintervalschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/billingintervalschedules/{item_id}", response_model=Dict[str, Any])
def get_billingintervalschedule_by_id(item_id: int):
    """Retrieve detailed record for BillingIntervalSchedule by ID."""
    svc = BillingIntervalScheduleService()
    item = svc.get_billingintervalschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BillingIntervalSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/billingintervalschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_billingintervalschedule(payload: BillingIntervalScheduleCreateSchema):
    """Create new BillingIntervalSchedule instance in enterprise repository."""
    svc = BillingIntervalScheduleService()
    try:
        item = svc.create_billingintervalschedule(
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

@router.put("/billingintervalschedules/{item_id}", response_model=Dict[str, Any])
def update_billingintervalschedule(item_id: int, payload: BillingIntervalScheduleUpdateSchema):
    """Update existing BillingIntervalSchedule record fields."""
    svc = BillingIntervalScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_billingintervalschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BillingIntervalSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/billingintervalschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_billingintervalschedule(item_id: int, hard: bool = Query(False)):
    """Delete BillingIntervalSchedule record (soft-delete by default)."""
    svc = BillingIntervalScheduleService()
    ok = svc.delete_billingintervalschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BillingIntervalSchedule with ID {item_id} not found")
    return None

@router.get("/billingintervalschedules/analytics/metrics", response_model=Dict[str, Any])
def get_billingintervalschedule_metrics():
    """Calculate summary statistical KPIs for BillingIntervalSchedule collection."""
    svc = BillingIntervalScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== MeteredUsageEvent Endpoints ====================
@router.get("/meteredusageevents", response_model=List[Dict[str, Any]])
def list_meteredusageevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MeteredUsageEvent records with pagination and filtering."""
    svc = MeteredUsageEventService()
    items = svc.list_meteredusageevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/meteredusageevents/{item_id}", response_model=Dict[str, Any])
def get_meteredusageevent_by_id(item_id: int):
    """Retrieve detailed record for MeteredUsageEvent by ID."""
    svc = MeteredUsageEventService()
    item = svc.get_meteredusageevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MeteredUsageEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/meteredusageevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_meteredusageevent(payload: MeteredUsageEventCreateSchema):
    """Create new MeteredUsageEvent instance in enterprise repository."""
    svc = MeteredUsageEventService()
    try:
        item = svc.create_meteredusageevent(
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

@router.put("/meteredusageevents/{item_id}", response_model=Dict[str, Any])
def update_meteredusageevent(item_id: int, payload: MeteredUsageEventUpdateSchema):
    """Update existing MeteredUsageEvent record fields."""
    svc = MeteredUsageEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_meteredusageevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MeteredUsageEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/meteredusageevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meteredusageevent(item_id: int, hard: bool = Query(False)):
    """Delete MeteredUsageEvent record (soft-delete by default)."""
    svc = MeteredUsageEventService()
    ok = svc.delete_meteredusageevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MeteredUsageEvent with ID {item_id} not found")
    return None

@router.get("/meteredusageevents/analytics/metrics", response_model=Dict[str, Any])
def get_meteredusageevent_metrics():
    """Calculate summary statistical KPIs for MeteredUsageEvent collection."""
    svc = MeteredUsageEventService()
    return svc.calculate_aggregate_metrics()

# ==================== InvoiceChargeItem Endpoints ====================
@router.get("/invoicechargeitems", response_model=List[Dict[str, Any]])
def list_invoicechargeitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InvoiceChargeItem records with pagination and filtering."""
    svc = InvoiceChargeItemService()
    items = svc.list_invoicechargeitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/invoicechargeitems/{item_id}", response_model=Dict[str, Any])
def get_invoicechargeitem_by_id(item_id: int):
    """Retrieve detailed record for InvoiceChargeItem by ID."""
    svc = InvoiceChargeItemService()
    item = svc.get_invoicechargeitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InvoiceChargeItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/invoicechargeitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_invoicechargeitem(payload: InvoiceChargeItemCreateSchema):
    """Create new InvoiceChargeItem instance in enterprise repository."""
    svc = InvoiceChargeItemService()
    try:
        item = svc.create_invoicechargeitem(
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

@router.put("/invoicechargeitems/{item_id}", response_model=Dict[str, Any])
def update_invoicechargeitem(item_id: int, payload: InvoiceChargeItemUpdateSchema):
    """Update existing InvoiceChargeItem record fields."""
    svc = InvoiceChargeItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_invoicechargeitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InvoiceChargeItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/invoicechargeitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoicechargeitem(item_id: int, hard: bool = Query(False)):
    """Delete InvoiceChargeItem record (soft-delete by default)."""
    svc = InvoiceChargeItemService()
    ok = svc.delete_invoicechargeitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InvoiceChargeItem with ID {item_id} not found")
    return None

@router.get("/invoicechargeitems/analytics/metrics", response_model=Dict[str, Any])
def get_invoicechargeitem_metrics():
    """Calculate summary statistical KPIs for InvoiceChargeItem collection."""
    svc = InvoiceChargeItemService()
    return svc.calculate_aggregate_metrics()

# ==================== DiscountCoupon Endpoints ====================
@router.get("/discountcoupons", response_model=List[Dict[str, Any]])
def list_discountcoupons(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DiscountCoupon records with pagination and filtering."""
    svc = DiscountCouponService()
    items = svc.list_discountcoupons(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/discountcoupons/{item_id}", response_model=Dict[str, Any])
def get_discountcoupon_by_id(item_id: int):
    """Retrieve detailed record for DiscountCoupon by ID."""
    svc = DiscountCouponService()
    item = svc.get_discountcoupon_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DiscountCoupon with ID {item_id} not found")
    return item.to_dict()

@router.post("/discountcoupons", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_discountcoupon(payload: DiscountCouponCreateSchema):
    """Create new DiscountCoupon instance in enterprise repository."""
    svc = DiscountCouponService()
    try:
        item = svc.create_discountcoupon(
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

@router.put("/discountcoupons/{item_id}", response_model=Dict[str, Any])
def update_discountcoupon(item_id: int, payload: DiscountCouponUpdateSchema):
    """Update existing DiscountCoupon record fields."""
    svc = DiscountCouponService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_discountcoupon(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DiscountCoupon with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/discountcoupons/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_discountcoupon(item_id: int, hard: bool = Query(False)):
    """Delete DiscountCoupon record (soft-delete by default)."""
    svc = DiscountCouponService()
    ok = svc.delete_discountcoupon(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DiscountCoupon with ID {item_id} not found")
    return None

@router.get("/discountcoupons/analytics/metrics", response_model=Dict[str, Any])
def get_discountcoupon_metrics():
    """Calculate summary statistical KPIs for DiscountCoupon collection."""
    svc = DiscountCouponService()
    return svc.calculate_aggregate_metrics()

# ==================== PaymentMethodProfile Endpoints ====================
@router.get("/paymentmethodprofiles", response_model=List[Dict[str, Any]])
def list_paymentmethodprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PaymentMethodProfile records with pagination and filtering."""
    svc = PaymentMethodProfileService()
    items = svc.list_paymentmethodprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/paymentmethodprofiles/{item_id}", response_model=Dict[str, Any])
def get_paymentmethodprofile_by_id(item_id: int):
    """Retrieve detailed record for PaymentMethodProfile by ID."""
    svc = PaymentMethodProfileService()
    item = svc.get_paymentmethodprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PaymentMethodProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/paymentmethodprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_paymentmethodprofile(payload: PaymentMethodProfileCreateSchema):
    """Create new PaymentMethodProfile instance in enterprise repository."""
    svc = PaymentMethodProfileService()
    try:
        item = svc.create_paymentmethodprofile(
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

@router.put("/paymentmethodprofiles/{item_id}", response_model=Dict[str, Any])
def update_paymentmethodprofile(item_id: int, payload: PaymentMethodProfileUpdateSchema):
    """Update existing PaymentMethodProfile record fields."""
    svc = PaymentMethodProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_paymentmethodprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PaymentMethodProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/paymentmethodprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_paymentmethodprofile(item_id: int, hard: bool = Query(False)):
    """Delete PaymentMethodProfile record (soft-delete by default)."""
    svc = PaymentMethodProfileService()
    ok = svc.delete_paymentmethodprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PaymentMethodProfile with ID {item_id} not found")
    return None

@router.get("/paymentmethodprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_paymentmethodprofile_metrics():
    """Calculate summary statistical KPIs for PaymentMethodProfile collection."""
    svc = PaymentMethodProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== DunningSequence Endpoints ====================
@router.get("/dunningsequences", response_model=List[Dict[str, Any]])
def list_dunningsequences(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DunningSequence records with pagination and filtering."""
    svc = DunningSequenceService()
    items = svc.list_dunningsequences(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dunningsequences/{item_id}", response_model=Dict[str, Any])
def get_dunningsequence_by_id(item_id: int):
    """Retrieve detailed record for DunningSequence by ID."""
    svc = DunningSequenceService()
    item = svc.get_dunningsequence_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DunningSequence with ID {item_id} not found")
    return item.to_dict()

@router.post("/dunningsequences", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dunningsequence(payload: DunningSequenceCreateSchema):
    """Create new DunningSequence instance in enterprise repository."""
    svc = DunningSequenceService()
    try:
        item = svc.create_dunningsequence(
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

@router.put("/dunningsequences/{item_id}", response_model=Dict[str, Any])
def update_dunningsequence(item_id: int, payload: DunningSequenceUpdateSchema):
    """Update existing DunningSequence record fields."""
    svc = DunningSequenceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dunningsequence(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DunningSequence with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dunningsequences/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dunningsequence(item_id: int, hard: bool = Query(False)):
    """Delete DunningSequence record (soft-delete by default)."""
    svc = DunningSequenceService()
    ok = svc.delete_dunningsequence(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DunningSequence with ID {item_id} not found")
    return None

@router.get("/dunningsequences/analytics/metrics", response_model=Dict[str, Any])
def get_dunningsequence_metrics():
    """Calculate summary statistical KPIs for DunningSequence collection."""
    svc = DunningSequenceService()
    return svc.calculate_aggregate_metrics()

# ==================== RevenueContractASC606 Endpoints ====================
@router.get("/revenuecontractasc606s", response_model=List[Dict[str, Any]])
def list_revenuecontractasc606s(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RevenueContractASC606 records with pagination and filtering."""
    svc = RevenueContractASC606Service()
    items = svc.list_revenuecontractasc606s(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/revenuecontractasc606s/{item_id}", response_model=Dict[str, Any])
def get_revenuecontractasc606_by_id(item_id: int):
    """Retrieve detailed record for RevenueContractASC606 by ID."""
    svc = RevenueContractASC606Service()
    item = svc.get_revenuecontractasc606_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RevenueContractASC606 with ID {item_id} not found")
    return item.to_dict()

@router.post("/revenuecontractasc606s", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_revenuecontractasc606(payload: RevenueContractASC606CreateSchema):
    """Create new RevenueContractASC606 instance in enterprise repository."""
    svc = RevenueContractASC606Service()
    try:
        item = svc.create_revenuecontractasc606(
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

@router.put("/revenuecontractasc606s/{item_id}", response_model=Dict[str, Any])
def update_revenuecontractasc606(item_id: int, payload: RevenueContractASC606UpdateSchema):
    """Update existing RevenueContractASC606 record fields."""
    svc = RevenueContractASC606Service()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_revenuecontractasc606(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RevenueContractASC606 with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/revenuecontractasc606s/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_revenuecontractasc606(item_id: int, hard: bool = Query(False)):
    """Delete RevenueContractASC606 record (soft-delete by default)."""
    svc = RevenueContractASC606Service()
    ok = svc.delete_revenuecontractasc606(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RevenueContractASC606 with ID {item_id} not found")
    return None

@router.get("/revenuecontractasc606s/analytics/metrics", response_model=Dict[str, Any])
def get_revenuecontractasc606_metrics():
    """Calculate summary statistical KPIs for RevenueContractASC606 collection."""
    svc = RevenueContractASC606Service()
    return svc.calculate_aggregate_metrics()

# ==================== PerformanceObligation Endpoints ====================
@router.get("/performanceobligations", response_model=List[Dict[str, Any]])
def list_performanceobligations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PerformanceObligation records with pagination and filtering."""
    svc = PerformanceObligationService()
    items = svc.list_performanceobligations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/performanceobligations/{item_id}", response_model=Dict[str, Any])
def get_performanceobligation_by_id(item_id: int):
    """Retrieve detailed record for PerformanceObligation by ID."""
    svc = PerformanceObligationService()
    item = svc.get_performanceobligation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PerformanceObligation with ID {item_id} not found")
    return item.to_dict()

@router.post("/performanceobligations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_performanceobligation(payload: PerformanceObligationCreateSchema):
    """Create new PerformanceObligation instance in enterprise repository."""
    svc = PerformanceObligationService()
    try:
        item = svc.create_performanceobligation(
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

@router.put("/performanceobligations/{item_id}", response_model=Dict[str, Any])
def update_performanceobligation(item_id: int, payload: PerformanceObligationUpdateSchema):
    """Update existing PerformanceObligation record fields."""
    svc = PerformanceObligationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_performanceobligation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PerformanceObligation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/performanceobligations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_performanceobligation(item_id: int, hard: bool = Query(False)):
    """Delete PerformanceObligation record (soft-delete by default)."""
    svc = PerformanceObligationService()
    ok = svc.delete_performanceobligation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PerformanceObligation with ID {item_id} not found")
    return None

@router.get("/performanceobligations/analytics/metrics", response_model=Dict[str, Any])
def get_performanceobligation_metrics():
    """Calculate summary statistical KPIs for PerformanceObligation collection."""
    svc = PerformanceObligationService()
    return svc.calculate_aggregate_metrics()

# ==================== DeferredRevenueAmortization Endpoints ====================
@router.get("/deferredrevenueamortizations", response_model=List[Dict[str, Any]])
def list_deferredrevenueamortizations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeferredRevenueAmortization records with pagination and filtering."""
    svc = DeferredRevenueAmortizationService()
    items = svc.list_deferredrevenueamortizations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/deferredrevenueamortizations/{item_id}", response_model=Dict[str, Any])
def get_deferredrevenueamortization_by_id(item_id: int):
    """Retrieve detailed record for DeferredRevenueAmortization by ID."""
    svc = DeferredRevenueAmortizationService()
    item = svc.get_deferredrevenueamortization_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeferredRevenueAmortization with ID {item_id} not found")
    return item.to_dict()

@router.post("/deferredrevenueamortizations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_deferredrevenueamortization(payload: DeferredRevenueAmortizationCreateSchema):
    """Create new DeferredRevenueAmortization instance in enterprise repository."""
    svc = DeferredRevenueAmortizationService()
    try:
        item = svc.create_deferredrevenueamortization(
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

@router.put("/deferredrevenueamortizations/{item_id}", response_model=Dict[str, Any])
def update_deferredrevenueamortization(item_id: int, payload: DeferredRevenueAmortizationUpdateSchema):
    """Update existing DeferredRevenueAmortization record fields."""
    svc = DeferredRevenueAmortizationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_deferredrevenueamortization(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeferredRevenueAmortization with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/deferredrevenueamortizations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deferredrevenueamortization(item_id: int, hard: bool = Query(False)):
    """Delete DeferredRevenueAmortization record (soft-delete by default)."""
    svc = DeferredRevenueAmortizationService()
    ok = svc.delete_deferredrevenueamortization(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeferredRevenueAmortization with ID {item_id} not found")
    return None

@router.get("/deferredrevenueamortizations/analytics/metrics", response_model=Dict[str, Any])
def get_deferredrevenueamortization_metrics():
    """Calculate summary statistical KPIs for DeferredRevenueAmortization collection."""
    svc = DeferredRevenueAmortizationService()
    return svc.calculate_aggregate_metrics()

# ==================== CreditBalanceAdjustment Endpoints ====================
@router.get("/creditbalanceadjustments", response_model=List[Dict[str, Any]])
def list_creditbalanceadjustments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CreditBalanceAdjustment records with pagination and filtering."""
    svc = CreditBalanceAdjustmentService()
    items = svc.list_creditbalanceadjustments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/creditbalanceadjustments/{item_id}", response_model=Dict[str, Any])
def get_creditbalanceadjustment_by_id(item_id: int):
    """Retrieve detailed record for CreditBalanceAdjustment by ID."""
    svc = CreditBalanceAdjustmentService()
    item = svc.get_creditbalanceadjustment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CreditBalanceAdjustment with ID {item_id} not found")
    return item.to_dict()

@router.post("/creditbalanceadjustments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_creditbalanceadjustment(payload: CreditBalanceAdjustmentCreateSchema):
    """Create new CreditBalanceAdjustment instance in enterprise repository."""
    svc = CreditBalanceAdjustmentService()
    try:
        item = svc.create_creditbalanceadjustment(
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

@router.put("/creditbalanceadjustments/{item_id}", response_model=Dict[str, Any])
def update_creditbalanceadjustment(item_id: int, payload: CreditBalanceAdjustmentUpdateSchema):
    """Update existing CreditBalanceAdjustment record fields."""
    svc = CreditBalanceAdjustmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_creditbalanceadjustment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CreditBalanceAdjustment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/creditbalanceadjustments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_creditbalanceadjustment(item_id: int, hard: bool = Query(False)):
    """Delete CreditBalanceAdjustment record (soft-delete by default)."""
    svc = CreditBalanceAdjustmentService()
    ok = svc.delete_creditbalanceadjustment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CreditBalanceAdjustment with ID {item_id} not found")
    return None

@router.get("/creditbalanceadjustments/analytics/metrics", response_model=Dict[str, Any])
def get_creditbalanceadjustment_metrics():
    """Calculate summary statistical KPIs for CreditBalanceAdjustment collection."""
    svc = CreditBalanceAdjustmentService()
    return svc.calculate_aggregate_metrics()

# ==================== ChurnNotice Endpoints ====================
@router.get("/churnnotices", response_model=List[Dict[str, Any]])
def list_churnnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChurnNotice records with pagination and filtering."""
    svc = ChurnNoticeService()
    items = svc.list_churnnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/churnnotices/{item_id}", response_model=Dict[str, Any])
def get_churnnotice_by_id(item_id: int):
    """Retrieve detailed record for ChurnNotice by ID."""
    svc = ChurnNoticeService()
    item = svc.get_churnnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChurnNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/churnnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_churnnotice(payload: ChurnNoticeCreateSchema):
    """Create new ChurnNotice instance in enterprise repository."""
    svc = ChurnNoticeService()
    try:
        item = svc.create_churnnotice(
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

@router.put("/churnnotices/{item_id}", response_model=Dict[str, Any])
def update_churnnotice(item_id: int, payload: ChurnNoticeUpdateSchema):
    """Update existing ChurnNotice record fields."""
    svc = ChurnNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_churnnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChurnNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/churnnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_churnnotice(item_id: int, hard: bool = Query(False)):
    """Delete ChurnNotice record (soft-delete by default)."""
    svc = ChurnNoticeService()
    ok = svc.delete_churnnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChurnNotice with ID {item_id} not found")
    return None

@router.get("/churnnotices/analytics/metrics", response_model=Dict[str, Any])
def get_churnnotice_metrics():
    """Calculate summary statistical KPIs for ChurnNotice collection."""
    svc = ChurnNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== UsageTierTiering Endpoints ====================
@router.get("/usagetiertierings", response_model=List[Dict[str, Any]])
def list_usagetiertierings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UsageTierTiering records with pagination and filtering."""
    svc = UsageTierTieringService()
    items = svc.list_usagetiertierings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/usagetiertierings/{item_id}", response_model=Dict[str, Any])
def get_usagetiertiering_by_id(item_id: int):
    """Retrieve detailed record for UsageTierTiering by ID."""
    svc = UsageTierTieringService()
    item = svc.get_usagetiertiering_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UsageTierTiering with ID {item_id} not found")
    return item.to_dict()

@router.post("/usagetiertierings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_usagetiertiering(payload: UsageTierTieringCreateSchema):
    """Create new UsageTierTiering instance in enterprise repository."""
    svc = UsageTierTieringService()
    try:
        item = svc.create_usagetiertiering(
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

@router.put("/usagetiertierings/{item_id}", response_model=Dict[str, Any])
def update_usagetiertiering(item_id: int, payload: UsageTierTieringUpdateSchema):
    """Update existing UsageTierTiering record fields."""
    svc = UsageTierTieringService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_usagetiertiering(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UsageTierTiering with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/usagetiertierings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_usagetiertiering(item_id: int, hard: bool = Query(False)):
    """Delete UsageTierTiering record (soft-delete by default)."""
    svc = UsageTierTieringService()
    ok = svc.delete_usagetiertiering(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UsageTierTiering with ID {item_id} not found")
    return None

@router.get("/usagetiertierings/analytics/metrics", response_model=Dict[str, Any])
def get_usagetiertiering_metrics():
    """Calculate summary statistical KPIs for UsageTierTiering collection."""
    svc = UsageTierTieringService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxJurisdictionRule Endpoints ====================
@router.get("/taxjurisdictionrules", response_model=List[Dict[str, Any]])
def list_taxjurisdictionrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxJurisdictionRule records with pagination and filtering."""
    svc = TaxJurisdictionRuleService()
    items = svc.list_taxjurisdictionrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxjurisdictionrules/{item_id}", response_model=Dict[str, Any])
def get_taxjurisdictionrule_by_id(item_id: int):
    """Retrieve detailed record for TaxJurisdictionRule by ID."""
    svc = TaxJurisdictionRuleService()
    item = svc.get_taxjurisdictionrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxJurisdictionRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxjurisdictionrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxjurisdictionrule(payload: TaxJurisdictionRuleCreateSchema):
    """Create new TaxJurisdictionRule instance in enterprise repository."""
    svc = TaxJurisdictionRuleService()
    try:
        item = svc.create_taxjurisdictionrule(
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

@router.put("/taxjurisdictionrules/{item_id}", response_model=Dict[str, Any])
def update_taxjurisdictionrule(item_id: int, payload: TaxJurisdictionRuleUpdateSchema):
    """Update existing TaxJurisdictionRule record fields."""
    svc = TaxJurisdictionRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxjurisdictionrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxJurisdictionRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxjurisdictionrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxjurisdictionrule(item_id: int, hard: bool = Query(False)):
    """Delete TaxJurisdictionRule record (soft-delete by default)."""
    svc = TaxJurisdictionRuleService()
    ok = svc.delete_taxjurisdictionrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxJurisdictionRule with ID {item_id} not found")
    return None

@router.get("/taxjurisdictionrules/analytics/metrics", response_model=Dict[str, Any])
def get_taxjurisdictionrule_metrics():
    """Calculate summary statistical KPIs for TaxJurisdictionRule collection."""
    svc = TaxJurisdictionRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== BillingReconciliation Endpoints ====================
@router.get("/billingreconciliations", response_model=List[Dict[str, Any]])
def list_billingreconciliations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BillingReconciliation records with pagination and filtering."""
    svc = BillingReconciliationService()
    items = svc.list_billingreconciliations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/billingreconciliations/{item_id}", response_model=Dict[str, Any])
def get_billingreconciliation_by_id(item_id: int):
    """Retrieve detailed record for BillingReconciliation by ID."""
    svc = BillingReconciliationService()
    item = svc.get_billingreconciliation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BillingReconciliation with ID {item_id} not found")
    return item.to_dict()

@router.post("/billingreconciliations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_billingreconciliation(payload: BillingReconciliationCreateSchema):
    """Create new BillingReconciliation instance in enterprise repository."""
    svc = BillingReconciliationService()
    try:
        item = svc.create_billingreconciliation(
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

@router.put("/billingreconciliations/{item_id}", response_model=Dict[str, Any])
def update_billingreconciliation(item_id: int, payload: BillingReconciliationUpdateSchema):
    """Update existing BillingReconciliation record fields."""
    svc = BillingReconciliationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_billingreconciliation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BillingReconciliation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/billingreconciliations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_billingreconciliation(item_id: int, hard: bool = Query(False)):
    """Delete BillingReconciliation record (soft-delete by default)."""
    svc = BillingReconciliationService()
    ok = svc.delete_billingreconciliation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BillingReconciliation with ID {item_id} not found")
    return None

@router.get("/billingreconciliations/analytics/metrics", response_model=Dict[str, Any])
def get_billingreconciliation_metrics():
    """Calculate summary statistical KPIs for BillingReconciliation collection."""
    svc = BillingReconciliationService()
    return svc.calculate_aggregate_metrics()

