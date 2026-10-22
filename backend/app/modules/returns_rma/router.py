"""
Reverse Logistics & Customer Returns (RMA) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ReturnMerchandiseAuthService,
    ReceivingInspectionQAService,
    RestockingFeeRuleService,
    CustomerRefundCreditNoteService,
    QuarantineDispositionService,
    WarrantyVerificationService,
    RefurbishmentWorkOrderService,
    ScrapAuthorizationService,
    CarrierReturnWaybillService,
    CustomerReturnReasonService,
    ReplacementShipmentService,
    ReturnAnalyticsMetricService,
    VendorChargebackClaimService,
    PackagingConditionLogService,
    ReturnPolicyRuleService,
    DepotRepairStatusService,
)
from .schemas import (
    ReturnMerchandiseAuthCreateSchema, ReturnMerchandiseAuthUpdateSchema, ReturnMerchandiseAuthResponseSchema,
    ReceivingInspectionQACreateSchema, ReceivingInspectionQAUpdateSchema, ReceivingInspectionQAResponseSchema,
    RestockingFeeRuleCreateSchema, RestockingFeeRuleUpdateSchema, RestockingFeeRuleResponseSchema,
    CustomerRefundCreditNoteCreateSchema, CustomerRefundCreditNoteUpdateSchema, CustomerRefundCreditNoteResponseSchema,
    QuarantineDispositionCreateSchema, QuarantineDispositionUpdateSchema, QuarantineDispositionResponseSchema,
    WarrantyVerificationCreateSchema, WarrantyVerificationUpdateSchema, WarrantyVerificationResponseSchema,
    RefurbishmentWorkOrderCreateSchema, RefurbishmentWorkOrderUpdateSchema, RefurbishmentWorkOrderResponseSchema,
    ScrapAuthorizationCreateSchema, ScrapAuthorizationUpdateSchema, ScrapAuthorizationResponseSchema,
    CarrierReturnWaybillCreateSchema, CarrierReturnWaybillUpdateSchema, CarrierReturnWaybillResponseSchema,
    CustomerReturnReasonCreateSchema, CustomerReturnReasonUpdateSchema, CustomerReturnReasonResponseSchema,
    ReplacementShipmentCreateSchema, ReplacementShipmentUpdateSchema, ReplacementShipmentResponseSchema,
    ReturnAnalyticsMetricCreateSchema, ReturnAnalyticsMetricUpdateSchema, ReturnAnalyticsMetricResponseSchema,
    VendorChargebackClaimCreateSchema, VendorChargebackClaimUpdateSchema, VendorChargebackClaimResponseSchema,
    PackagingConditionLogCreateSchema, PackagingConditionLogUpdateSchema, PackagingConditionLogResponseSchema,
    ReturnPolicyRuleCreateSchema, ReturnPolicyRuleUpdateSchema, ReturnPolicyRuleResponseSchema,
    DepotRepairStatusCreateSchema, DepotRepairStatusUpdateSchema, DepotRepairStatusResponseSchema,
)

router = APIRouter(prefix="/returns_rma", tags=["Reverse Logistics & Customer Returns (RMA)"])

# ==================== ReturnMerchandiseAuth Endpoints ====================
@router.get("/returnmerchandiseauths", response_model=List[Dict[str, Any]])
def list_returnmerchandiseauths(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReturnMerchandiseAuth records with pagination and filtering."""
    svc = ReturnMerchandiseAuthService()
    items = svc.list_returnmerchandiseauths(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/returnmerchandiseauths/{item_id}", response_model=Dict[str, Any])
def get_returnmerchandiseauth_by_id(item_id: int):
    """Retrieve detailed record for ReturnMerchandiseAuth by ID."""
    svc = ReturnMerchandiseAuthService()
    item = svc.get_returnmerchandiseauth_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReturnMerchandiseAuth with ID {item_id} not found")
    return item.to_dict()

@router.post("/returnmerchandiseauths", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_returnmerchandiseauth(payload: ReturnMerchandiseAuthCreateSchema):
    """Create new ReturnMerchandiseAuth instance in enterprise repository."""
    svc = ReturnMerchandiseAuthService()
    try:
        item = svc.create_returnmerchandiseauth(
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

@router.put("/returnmerchandiseauths/{item_id}", response_model=Dict[str, Any])
def update_returnmerchandiseauth(item_id: int, payload: ReturnMerchandiseAuthUpdateSchema):
    """Update existing ReturnMerchandiseAuth record fields."""
    svc = ReturnMerchandiseAuthService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_returnmerchandiseauth(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReturnMerchandiseAuth with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/returnmerchandiseauths/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_returnmerchandiseauth(item_id: int, hard: bool = Query(False)):
    """Delete ReturnMerchandiseAuth record (soft-delete by default)."""
    svc = ReturnMerchandiseAuthService()
    ok = svc.delete_returnmerchandiseauth(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReturnMerchandiseAuth with ID {item_id} not found")
    return None

@router.get("/returnmerchandiseauths/analytics/metrics", response_model=Dict[str, Any])
def get_returnmerchandiseauth_metrics():
    """Calculate summary statistical KPIs for ReturnMerchandiseAuth collection."""
    svc = ReturnMerchandiseAuthService()
    return svc.calculate_aggregate_metrics()

# ==================== ReceivingInspectionQA Endpoints ====================
@router.get("/receivinginspectionqas", response_model=List[Dict[str, Any]])
def list_receivinginspectionqas(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReceivingInspectionQA records with pagination and filtering."""
    svc = ReceivingInspectionQAService()
    items = svc.list_receivinginspectionqas(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/receivinginspectionqas/{item_id}", response_model=Dict[str, Any])
def get_receivinginspectionqa_by_id(item_id: int):
    """Retrieve detailed record for ReceivingInspectionQA by ID."""
    svc = ReceivingInspectionQAService()
    item = svc.get_receivinginspectionqa_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReceivingInspectionQA with ID {item_id} not found")
    return item.to_dict()

@router.post("/receivinginspectionqas", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_receivinginspectionqa(payload: ReceivingInspectionQACreateSchema):
    """Create new ReceivingInspectionQA instance in enterprise repository."""
    svc = ReceivingInspectionQAService()
    try:
        item = svc.create_receivinginspectionqa(
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

@router.put("/receivinginspectionqas/{item_id}", response_model=Dict[str, Any])
def update_receivinginspectionqa(item_id: int, payload: ReceivingInspectionQAUpdateSchema):
    """Update existing ReceivingInspectionQA record fields."""
    svc = ReceivingInspectionQAService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_receivinginspectionqa(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReceivingInspectionQA with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/receivinginspectionqas/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_receivinginspectionqa(item_id: int, hard: bool = Query(False)):
    """Delete ReceivingInspectionQA record (soft-delete by default)."""
    svc = ReceivingInspectionQAService()
    ok = svc.delete_receivinginspectionqa(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReceivingInspectionQA with ID {item_id} not found")
    return None

@router.get("/receivinginspectionqas/analytics/metrics", response_model=Dict[str, Any])
def get_receivinginspectionqa_metrics():
    """Calculate summary statistical KPIs for ReceivingInspectionQA collection."""
    svc = ReceivingInspectionQAService()
    return svc.calculate_aggregate_metrics()

# ==================== RestockingFeeRule Endpoints ====================
@router.get("/restockingfeerules", response_model=List[Dict[str, Any]])
def list_restockingfeerules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RestockingFeeRule records with pagination and filtering."""
    svc = RestockingFeeRuleService()
    items = svc.list_restockingfeerules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/restockingfeerules/{item_id}", response_model=Dict[str, Any])
def get_restockingfeerule_by_id(item_id: int):
    """Retrieve detailed record for RestockingFeeRule by ID."""
    svc = RestockingFeeRuleService()
    item = svc.get_restockingfeerule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RestockingFeeRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/restockingfeerules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_restockingfeerule(payload: RestockingFeeRuleCreateSchema):
    """Create new RestockingFeeRule instance in enterprise repository."""
    svc = RestockingFeeRuleService()
    try:
        item = svc.create_restockingfeerule(
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

@router.put("/restockingfeerules/{item_id}", response_model=Dict[str, Any])
def update_restockingfeerule(item_id: int, payload: RestockingFeeRuleUpdateSchema):
    """Update existing RestockingFeeRule record fields."""
    svc = RestockingFeeRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_restockingfeerule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RestockingFeeRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/restockingfeerules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_restockingfeerule(item_id: int, hard: bool = Query(False)):
    """Delete RestockingFeeRule record (soft-delete by default)."""
    svc = RestockingFeeRuleService()
    ok = svc.delete_restockingfeerule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RestockingFeeRule with ID {item_id} not found")
    return None

@router.get("/restockingfeerules/analytics/metrics", response_model=Dict[str, Any])
def get_restockingfeerule_metrics():
    """Calculate summary statistical KPIs for RestockingFeeRule collection."""
    svc = RestockingFeeRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerRefundCreditNote Endpoints ====================
@router.get("/customerrefundcreditnotes", response_model=List[Dict[str, Any]])
def list_customerrefundcreditnotes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerRefundCreditNote records with pagination and filtering."""
    svc = CustomerRefundCreditNoteService()
    items = svc.list_customerrefundcreditnotes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerrefundcreditnotes/{item_id}", response_model=Dict[str, Any])
def get_customerrefundcreditnote_by_id(item_id: int):
    """Retrieve detailed record for CustomerRefundCreditNote by ID."""
    svc = CustomerRefundCreditNoteService()
    item = svc.get_customerrefundcreditnote_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerRefundCreditNote with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerrefundcreditnotes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerrefundcreditnote(payload: CustomerRefundCreditNoteCreateSchema):
    """Create new CustomerRefundCreditNote instance in enterprise repository."""
    svc = CustomerRefundCreditNoteService()
    try:
        item = svc.create_customerrefundcreditnote(
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

@router.put("/customerrefundcreditnotes/{item_id}", response_model=Dict[str, Any])
def update_customerrefundcreditnote(item_id: int, payload: CustomerRefundCreditNoteUpdateSchema):
    """Update existing CustomerRefundCreditNote record fields."""
    svc = CustomerRefundCreditNoteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerrefundcreditnote(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerRefundCreditNote with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerrefundcreditnotes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerrefundcreditnote(item_id: int, hard: bool = Query(False)):
    """Delete CustomerRefundCreditNote record (soft-delete by default)."""
    svc = CustomerRefundCreditNoteService()
    ok = svc.delete_customerrefundcreditnote(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerRefundCreditNote with ID {item_id} not found")
    return None

@router.get("/customerrefundcreditnotes/analytics/metrics", response_model=Dict[str, Any])
def get_customerrefundcreditnote_metrics():
    """Calculate summary statistical KPIs for CustomerRefundCreditNote collection."""
    svc = CustomerRefundCreditNoteService()
    return svc.calculate_aggregate_metrics()

# ==================== QuarantineDisposition Endpoints ====================
@router.get("/quarantinedispositions", response_model=List[Dict[str, Any]])
def list_quarantinedispositions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List QuarantineDisposition records with pagination and filtering."""
    svc = QuarantineDispositionService()
    items = svc.list_quarantinedispositions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/quarantinedispositions/{item_id}", response_model=Dict[str, Any])
def get_quarantinedisposition_by_id(item_id: int):
    """Retrieve detailed record for QuarantineDisposition by ID."""
    svc = QuarantineDispositionService()
    item = svc.get_quarantinedisposition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"QuarantineDisposition with ID {item_id} not found")
    return item.to_dict()

@router.post("/quarantinedispositions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_quarantinedisposition(payload: QuarantineDispositionCreateSchema):
    """Create new QuarantineDisposition instance in enterprise repository."""
    svc = QuarantineDispositionService()
    try:
        item = svc.create_quarantinedisposition(
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

@router.put("/quarantinedispositions/{item_id}", response_model=Dict[str, Any])
def update_quarantinedisposition(item_id: int, payload: QuarantineDispositionUpdateSchema):
    """Update existing QuarantineDisposition record fields."""
    svc = QuarantineDispositionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_quarantinedisposition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"QuarantineDisposition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/quarantinedispositions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quarantinedisposition(item_id: int, hard: bool = Query(False)):
    """Delete QuarantineDisposition record (soft-delete by default)."""
    svc = QuarantineDispositionService()
    ok = svc.delete_quarantinedisposition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"QuarantineDisposition with ID {item_id} not found")
    return None

@router.get("/quarantinedispositions/analytics/metrics", response_model=Dict[str, Any])
def get_quarantinedisposition_metrics():
    """Calculate summary statistical KPIs for QuarantineDisposition collection."""
    svc = QuarantineDispositionService()
    return svc.calculate_aggregate_metrics()

# ==================== WarrantyVerification Endpoints ====================
@router.get("/warrantyverifications", response_model=List[Dict[str, Any]])
def list_warrantyverifications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WarrantyVerification records with pagination and filtering."""
    svc = WarrantyVerificationService()
    items = svc.list_warrantyverifications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/warrantyverifications/{item_id}", response_model=Dict[str, Any])
def get_warrantyverification_by_id(item_id: int):
    """Retrieve detailed record for WarrantyVerification by ID."""
    svc = WarrantyVerificationService()
    item = svc.get_warrantyverification_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WarrantyVerification with ID {item_id} not found")
    return item.to_dict()

@router.post("/warrantyverifications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_warrantyverification(payload: WarrantyVerificationCreateSchema):
    """Create new WarrantyVerification instance in enterprise repository."""
    svc = WarrantyVerificationService()
    try:
        item = svc.create_warrantyverification(
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

@router.put("/warrantyverifications/{item_id}", response_model=Dict[str, Any])
def update_warrantyverification(item_id: int, payload: WarrantyVerificationUpdateSchema):
    """Update existing WarrantyVerification record fields."""
    svc = WarrantyVerificationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_warrantyverification(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WarrantyVerification with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/warrantyverifications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warrantyverification(item_id: int, hard: bool = Query(False)):
    """Delete WarrantyVerification record (soft-delete by default)."""
    svc = WarrantyVerificationService()
    ok = svc.delete_warrantyverification(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WarrantyVerification with ID {item_id} not found")
    return None

@router.get("/warrantyverifications/analytics/metrics", response_model=Dict[str, Any])
def get_warrantyverification_metrics():
    """Calculate summary statistical KPIs for WarrantyVerification collection."""
    svc = WarrantyVerificationService()
    return svc.calculate_aggregate_metrics()

# ==================== RefurbishmentWorkOrder Endpoints ====================
@router.get("/refurbishmentworkorders", response_model=List[Dict[str, Any]])
def list_refurbishmentworkorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RefurbishmentWorkOrder records with pagination and filtering."""
    svc = RefurbishmentWorkOrderService()
    items = svc.list_refurbishmentworkorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/refurbishmentworkorders/{item_id}", response_model=Dict[str, Any])
def get_refurbishmentworkorder_by_id(item_id: int):
    """Retrieve detailed record for RefurbishmentWorkOrder by ID."""
    svc = RefurbishmentWorkOrderService()
    item = svc.get_refurbishmentworkorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RefurbishmentWorkOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/refurbishmentworkorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_refurbishmentworkorder(payload: RefurbishmentWorkOrderCreateSchema):
    """Create new RefurbishmentWorkOrder instance in enterprise repository."""
    svc = RefurbishmentWorkOrderService()
    try:
        item = svc.create_refurbishmentworkorder(
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

@router.put("/refurbishmentworkorders/{item_id}", response_model=Dict[str, Any])
def update_refurbishmentworkorder(item_id: int, payload: RefurbishmentWorkOrderUpdateSchema):
    """Update existing RefurbishmentWorkOrder record fields."""
    svc = RefurbishmentWorkOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_refurbishmentworkorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RefurbishmentWorkOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/refurbishmentworkorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_refurbishmentworkorder(item_id: int, hard: bool = Query(False)):
    """Delete RefurbishmentWorkOrder record (soft-delete by default)."""
    svc = RefurbishmentWorkOrderService()
    ok = svc.delete_refurbishmentworkorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RefurbishmentWorkOrder with ID {item_id} not found")
    return None

@router.get("/refurbishmentworkorders/analytics/metrics", response_model=Dict[str, Any])
def get_refurbishmentworkorder_metrics():
    """Calculate summary statistical KPIs for RefurbishmentWorkOrder collection."""
    svc = RefurbishmentWorkOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== ScrapAuthorization Endpoints ====================
@router.get("/scrapauthorizations", response_model=List[Dict[str, Any]])
def list_scrapauthorizations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ScrapAuthorization records with pagination and filtering."""
    svc = ScrapAuthorizationService()
    items = svc.list_scrapauthorizations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/scrapauthorizations/{item_id}", response_model=Dict[str, Any])
def get_scrapauthorization_by_id(item_id: int):
    """Retrieve detailed record for ScrapAuthorization by ID."""
    svc = ScrapAuthorizationService()
    item = svc.get_scrapauthorization_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ScrapAuthorization with ID {item_id} not found")
    return item.to_dict()

@router.post("/scrapauthorizations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_scrapauthorization(payload: ScrapAuthorizationCreateSchema):
    """Create new ScrapAuthorization instance in enterprise repository."""
    svc = ScrapAuthorizationService()
    try:
        item = svc.create_scrapauthorization(
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

@router.put("/scrapauthorizations/{item_id}", response_model=Dict[str, Any])
def update_scrapauthorization(item_id: int, payload: ScrapAuthorizationUpdateSchema):
    """Update existing ScrapAuthorization record fields."""
    svc = ScrapAuthorizationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_scrapauthorization(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ScrapAuthorization with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/scrapauthorizations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scrapauthorization(item_id: int, hard: bool = Query(False)):
    """Delete ScrapAuthorization record (soft-delete by default)."""
    svc = ScrapAuthorizationService()
    ok = svc.delete_scrapauthorization(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ScrapAuthorization with ID {item_id} not found")
    return None

@router.get("/scrapauthorizations/analytics/metrics", response_model=Dict[str, Any])
def get_scrapauthorization_metrics():
    """Calculate summary statistical KPIs for ScrapAuthorization collection."""
    svc = ScrapAuthorizationService()
    return svc.calculate_aggregate_metrics()

# ==================== CarrierReturnWaybill Endpoints ====================
@router.get("/carrierreturnwaybills", response_model=List[Dict[str, Any]])
def list_carrierreturnwaybills(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CarrierReturnWaybill records with pagination and filtering."""
    svc = CarrierReturnWaybillService()
    items = svc.list_carrierreturnwaybills(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/carrierreturnwaybills/{item_id}", response_model=Dict[str, Any])
def get_carrierreturnwaybill_by_id(item_id: int):
    """Retrieve detailed record for CarrierReturnWaybill by ID."""
    svc = CarrierReturnWaybillService()
    item = svc.get_carrierreturnwaybill_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CarrierReturnWaybill with ID {item_id} not found")
    return item.to_dict()

@router.post("/carrierreturnwaybills", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_carrierreturnwaybill(payload: CarrierReturnWaybillCreateSchema):
    """Create new CarrierReturnWaybill instance in enterprise repository."""
    svc = CarrierReturnWaybillService()
    try:
        item = svc.create_carrierreturnwaybill(
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

@router.put("/carrierreturnwaybills/{item_id}", response_model=Dict[str, Any])
def update_carrierreturnwaybill(item_id: int, payload: CarrierReturnWaybillUpdateSchema):
    """Update existing CarrierReturnWaybill record fields."""
    svc = CarrierReturnWaybillService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_carrierreturnwaybill(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CarrierReturnWaybill with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/carrierreturnwaybills/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrierreturnwaybill(item_id: int, hard: bool = Query(False)):
    """Delete CarrierReturnWaybill record (soft-delete by default)."""
    svc = CarrierReturnWaybillService()
    ok = svc.delete_carrierreturnwaybill(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CarrierReturnWaybill with ID {item_id} not found")
    return None

@router.get("/carrierreturnwaybills/analytics/metrics", response_model=Dict[str, Any])
def get_carrierreturnwaybill_metrics():
    """Calculate summary statistical KPIs for CarrierReturnWaybill collection."""
    svc = CarrierReturnWaybillService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerReturnReason Endpoints ====================
@router.get("/customerreturnreasons", response_model=List[Dict[str, Any]])
def list_customerreturnreasons(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerReturnReason records with pagination and filtering."""
    svc = CustomerReturnReasonService()
    items = svc.list_customerreturnreasons(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerreturnreasons/{item_id}", response_model=Dict[str, Any])
def get_customerreturnreason_by_id(item_id: int):
    """Retrieve detailed record for CustomerReturnReason by ID."""
    svc = CustomerReturnReasonService()
    item = svc.get_customerreturnreason_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerReturnReason with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerreturnreasons", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerreturnreason(payload: CustomerReturnReasonCreateSchema):
    """Create new CustomerReturnReason instance in enterprise repository."""
    svc = CustomerReturnReasonService()
    try:
        item = svc.create_customerreturnreason(
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

@router.put("/customerreturnreasons/{item_id}", response_model=Dict[str, Any])
def update_customerreturnreason(item_id: int, payload: CustomerReturnReasonUpdateSchema):
    """Update existing CustomerReturnReason record fields."""
    svc = CustomerReturnReasonService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerreturnreason(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerReturnReason with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerreturnreasons/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerreturnreason(item_id: int, hard: bool = Query(False)):
    """Delete CustomerReturnReason record (soft-delete by default)."""
    svc = CustomerReturnReasonService()
    ok = svc.delete_customerreturnreason(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerReturnReason with ID {item_id} not found")
    return None

@router.get("/customerreturnreasons/analytics/metrics", response_model=Dict[str, Any])
def get_customerreturnreason_metrics():
    """Calculate summary statistical KPIs for CustomerReturnReason collection."""
    svc = CustomerReturnReasonService()
    return svc.calculate_aggregate_metrics()

# ==================== ReplacementShipment Endpoints ====================
@router.get("/replacementshipments", response_model=List[Dict[str, Any]])
def list_replacementshipments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReplacementShipment records with pagination and filtering."""
    svc = ReplacementShipmentService()
    items = svc.list_replacementshipments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/replacementshipments/{item_id}", response_model=Dict[str, Any])
def get_replacementshipment_by_id(item_id: int):
    """Retrieve detailed record for ReplacementShipment by ID."""
    svc = ReplacementShipmentService()
    item = svc.get_replacementshipment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReplacementShipment with ID {item_id} not found")
    return item.to_dict()

@router.post("/replacementshipments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_replacementshipment(payload: ReplacementShipmentCreateSchema):
    """Create new ReplacementShipment instance in enterprise repository."""
    svc = ReplacementShipmentService()
    try:
        item = svc.create_replacementshipment(
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

@router.put("/replacementshipments/{item_id}", response_model=Dict[str, Any])
def update_replacementshipment(item_id: int, payload: ReplacementShipmentUpdateSchema):
    """Update existing ReplacementShipment record fields."""
    svc = ReplacementShipmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_replacementshipment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReplacementShipment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/replacementshipments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_replacementshipment(item_id: int, hard: bool = Query(False)):
    """Delete ReplacementShipment record (soft-delete by default)."""
    svc = ReplacementShipmentService()
    ok = svc.delete_replacementshipment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReplacementShipment with ID {item_id} not found")
    return None

@router.get("/replacementshipments/analytics/metrics", response_model=Dict[str, Any])
def get_replacementshipment_metrics():
    """Calculate summary statistical KPIs for ReplacementShipment collection."""
    svc = ReplacementShipmentService()
    return svc.calculate_aggregate_metrics()

# ==================== ReturnAnalyticsMetric Endpoints ====================
@router.get("/returnanalyticsmetrics", response_model=List[Dict[str, Any]])
def list_returnanalyticsmetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReturnAnalyticsMetric records with pagination and filtering."""
    svc = ReturnAnalyticsMetricService()
    items = svc.list_returnanalyticsmetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/returnanalyticsmetrics/{item_id}", response_model=Dict[str, Any])
def get_returnanalyticsmetric_by_id(item_id: int):
    """Retrieve detailed record for ReturnAnalyticsMetric by ID."""
    svc = ReturnAnalyticsMetricService()
    item = svc.get_returnanalyticsmetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReturnAnalyticsMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/returnanalyticsmetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_returnanalyticsmetric(payload: ReturnAnalyticsMetricCreateSchema):
    """Create new ReturnAnalyticsMetric instance in enterprise repository."""
    svc = ReturnAnalyticsMetricService()
    try:
        item = svc.create_returnanalyticsmetric(
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

@router.put("/returnanalyticsmetrics/{item_id}", response_model=Dict[str, Any])
def update_returnanalyticsmetric(item_id: int, payload: ReturnAnalyticsMetricUpdateSchema):
    """Update existing ReturnAnalyticsMetric record fields."""
    svc = ReturnAnalyticsMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_returnanalyticsmetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReturnAnalyticsMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/returnanalyticsmetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_returnanalyticsmetric(item_id: int, hard: bool = Query(False)):
    """Delete ReturnAnalyticsMetric record (soft-delete by default)."""
    svc = ReturnAnalyticsMetricService()
    ok = svc.delete_returnanalyticsmetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReturnAnalyticsMetric with ID {item_id} not found")
    return None

@router.get("/returnanalyticsmetrics/analytics/metrics", response_model=Dict[str, Any])
def get_returnanalyticsmetric_metrics():
    """Calculate summary statistical KPIs for ReturnAnalyticsMetric collection."""
    svc = ReturnAnalyticsMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorChargebackClaim Endpoints ====================
@router.get("/vendorchargebackclaims", response_model=List[Dict[str, Any]])
def list_vendorchargebackclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorChargebackClaim records with pagination and filtering."""
    svc = VendorChargebackClaimService()
    items = svc.list_vendorchargebackclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorchargebackclaims/{item_id}", response_model=Dict[str, Any])
def get_vendorchargebackclaim_by_id(item_id: int):
    """Retrieve detailed record for VendorChargebackClaim by ID."""
    svc = VendorChargebackClaimService()
    item = svc.get_vendorchargebackclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorChargebackClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorchargebackclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorchargebackclaim(payload: VendorChargebackClaimCreateSchema):
    """Create new VendorChargebackClaim instance in enterprise repository."""
    svc = VendorChargebackClaimService()
    try:
        item = svc.create_vendorchargebackclaim(
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

@router.put("/vendorchargebackclaims/{item_id}", response_model=Dict[str, Any])
def update_vendorchargebackclaim(item_id: int, payload: VendorChargebackClaimUpdateSchema):
    """Update existing VendorChargebackClaim record fields."""
    svc = VendorChargebackClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorchargebackclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorChargebackClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorchargebackclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorchargebackclaim(item_id: int, hard: bool = Query(False)):
    """Delete VendorChargebackClaim record (soft-delete by default)."""
    svc = VendorChargebackClaimService()
    ok = svc.delete_vendorchargebackclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorChargebackClaim with ID {item_id} not found")
    return None

@router.get("/vendorchargebackclaims/analytics/metrics", response_model=Dict[str, Any])
def get_vendorchargebackclaim_metrics():
    """Calculate summary statistical KPIs for VendorChargebackClaim collection."""
    svc = VendorChargebackClaimService()
    return svc.calculate_aggregate_metrics()

# ==================== PackagingConditionLog Endpoints ====================
@router.get("/packagingconditionlogs", response_model=List[Dict[str, Any]])
def list_packagingconditionlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PackagingConditionLog records with pagination and filtering."""
    svc = PackagingConditionLogService()
    items = svc.list_packagingconditionlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/packagingconditionlogs/{item_id}", response_model=Dict[str, Any])
def get_packagingconditionlog_by_id(item_id: int):
    """Retrieve detailed record for PackagingConditionLog by ID."""
    svc = PackagingConditionLogService()
    item = svc.get_packagingconditionlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PackagingConditionLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/packagingconditionlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_packagingconditionlog(payload: PackagingConditionLogCreateSchema):
    """Create new PackagingConditionLog instance in enterprise repository."""
    svc = PackagingConditionLogService()
    try:
        item = svc.create_packagingconditionlog(
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

@router.put("/packagingconditionlogs/{item_id}", response_model=Dict[str, Any])
def update_packagingconditionlog(item_id: int, payload: PackagingConditionLogUpdateSchema):
    """Update existing PackagingConditionLog record fields."""
    svc = PackagingConditionLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_packagingconditionlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PackagingConditionLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/packagingconditionlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_packagingconditionlog(item_id: int, hard: bool = Query(False)):
    """Delete PackagingConditionLog record (soft-delete by default)."""
    svc = PackagingConditionLogService()
    ok = svc.delete_packagingconditionlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PackagingConditionLog with ID {item_id} not found")
    return None

@router.get("/packagingconditionlogs/analytics/metrics", response_model=Dict[str, Any])
def get_packagingconditionlog_metrics():
    """Calculate summary statistical KPIs for PackagingConditionLog collection."""
    svc = PackagingConditionLogService()
    return svc.calculate_aggregate_metrics()

# ==================== ReturnPolicyRule Endpoints ====================
@router.get("/returnpolicyrules", response_model=List[Dict[str, Any]])
def list_returnpolicyrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReturnPolicyRule records with pagination and filtering."""
    svc = ReturnPolicyRuleService()
    items = svc.list_returnpolicyrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/returnpolicyrules/{item_id}", response_model=Dict[str, Any])
def get_returnpolicyrule_by_id(item_id: int):
    """Retrieve detailed record for ReturnPolicyRule by ID."""
    svc = ReturnPolicyRuleService()
    item = svc.get_returnpolicyrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReturnPolicyRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/returnpolicyrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_returnpolicyrule(payload: ReturnPolicyRuleCreateSchema):
    """Create new ReturnPolicyRule instance in enterprise repository."""
    svc = ReturnPolicyRuleService()
    try:
        item = svc.create_returnpolicyrule(
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

@router.put("/returnpolicyrules/{item_id}", response_model=Dict[str, Any])
def update_returnpolicyrule(item_id: int, payload: ReturnPolicyRuleUpdateSchema):
    """Update existing ReturnPolicyRule record fields."""
    svc = ReturnPolicyRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_returnpolicyrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReturnPolicyRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/returnpolicyrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_returnpolicyrule(item_id: int, hard: bool = Query(False)):
    """Delete ReturnPolicyRule record (soft-delete by default)."""
    svc = ReturnPolicyRuleService()
    ok = svc.delete_returnpolicyrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReturnPolicyRule with ID {item_id} not found")
    return None

@router.get("/returnpolicyrules/analytics/metrics", response_model=Dict[str, Any])
def get_returnpolicyrule_metrics():
    """Calculate summary statistical KPIs for ReturnPolicyRule collection."""
    svc = ReturnPolicyRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== DepotRepairStatus Endpoints ====================
@router.get("/depotrepairstatuss", response_model=List[Dict[str, Any]])
def list_depotrepairstatuss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DepotRepairStatus records with pagination and filtering."""
    svc = DepotRepairStatusService()
    items = svc.list_depotrepairstatuss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/depotrepairstatuss/{item_id}", response_model=Dict[str, Any])
def get_depotrepairstatus_by_id(item_id: int):
    """Retrieve detailed record for DepotRepairStatus by ID."""
    svc = DepotRepairStatusService()
    item = svc.get_depotrepairstatus_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DepotRepairStatus with ID {item_id} not found")
    return item.to_dict()

@router.post("/depotrepairstatuss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_depotrepairstatus(payload: DepotRepairStatusCreateSchema):
    """Create new DepotRepairStatus instance in enterprise repository."""
    svc = DepotRepairStatusService()
    try:
        item = svc.create_depotrepairstatus(
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

@router.put("/depotrepairstatuss/{item_id}", response_model=Dict[str, Any])
def update_depotrepairstatus(item_id: int, payload: DepotRepairStatusUpdateSchema):
    """Update existing DepotRepairStatus record fields."""
    svc = DepotRepairStatusService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_depotrepairstatus(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DepotRepairStatus with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/depotrepairstatuss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_depotrepairstatus(item_id: int, hard: bool = Query(False)):
    """Delete DepotRepairStatus record (soft-delete by default)."""
    svc = DepotRepairStatusService()
    ok = svc.delete_depotrepairstatus(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DepotRepairStatus with ID {item_id} not found")
    return None

@router.get("/depotrepairstatuss/analytics/metrics", response_model=Dict[str, Any])
def get_depotrepairstatus_metrics():
    """Calculate summary statistical KPIs for DepotRepairStatus collection."""
    svc = DepotRepairStatusService()
    return svc.calculate_aggregate_metrics()

