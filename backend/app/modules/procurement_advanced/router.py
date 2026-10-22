"""
Strategic Procurement & Sourcing - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    SourcingRequestService,
    VendorQuoteService,
    BidComparisonService,
    ContractAgreementService,
    PurchaseRequisitionService,
    BlanketPOService,
    VendorScorecardService,
    SpendCategoryService,
    ProcurementPolicyService,
    CatalogItemService,
    SupplierTierService,
    RebateProgramService,
    FreightRateAgreementService,
    ImportPermitService,
    PurchaseReturnService,
    PaymentScheduleService,
)
from .schemas import (
    SourcingRequestCreateSchema, SourcingRequestUpdateSchema, SourcingRequestResponseSchema,
    VendorQuoteCreateSchema, VendorQuoteUpdateSchema, VendorQuoteResponseSchema,
    BidComparisonCreateSchema, BidComparisonUpdateSchema, BidComparisonResponseSchema,
    ContractAgreementCreateSchema, ContractAgreementUpdateSchema, ContractAgreementResponseSchema,
    PurchaseRequisitionCreateSchema, PurchaseRequisitionUpdateSchema, PurchaseRequisitionResponseSchema,
    BlanketPOCreateSchema, BlanketPOUpdateSchema, BlanketPOResponseSchema,
    VendorScorecardCreateSchema, VendorScorecardUpdateSchema, VendorScorecardResponseSchema,
    SpendCategoryCreateSchema, SpendCategoryUpdateSchema, SpendCategoryResponseSchema,
    ProcurementPolicyCreateSchema, ProcurementPolicyUpdateSchema, ProcurementPolicyResponseSchema,
    CatalogItemCreateSchema, CatalogItemUpdateSchema, CatalogItemResponseSchema,
    SupplierTierCreateSchema, SupplierTierUpdateSchema, SupplierTierResponseSchema,
    RebateProgramCreateSchema, RebateProgramUpdateSchema, RebateProgramResponseSchema,
    FreightRateAgreementCreateSchema, FreightRateAgreementUpdateSchema, FreightRateAgreementResponseSchema,
    ImportPermitCreateSchema, ImportPermitUpdateSchema, ImportPermitResponseSchema,
    PurchaseReturnCreateSchema, PurchaseReturnUpdateSchema, PurchaseReturnResponseSchema,
    PaymentScheduleCreateSchema, PaymentScheduleUpdateSchema, PaymentScheduleResponseSchema,
)

router = APIRouter(prefix="/procurement_advanced", tags=["Strategic Procurement & Sourcing"])

# ==================== SourcingRequest Endpoints ====================
@router.get("/sourcingrequests", response_model=List[Dict[str, Any]])
def list_sourcingrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SourcingRequest records with pagination and filtering."""
    svc = SourcingRequestService()
    items = svc.list_sourcingrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sourcingrequests/{item_id}", response_model=Dict[str, Any])
def get_sourcingrequest_by_id(item_id: int):
    """Retrieve detailed record for SourcingRequest by ID."""
    svc = SourcingRequestService()
    item = svc.get_sourcingrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SourcingRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/sourcingrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sourcingrequest(payload: SourcingRequestCreateSchema):
    """Create new SourcingRequest instance in enterprise repository."""
    svc = SourcingRequestService()
    try:
        item = svc.create_sourcingrequest(
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

@router.put("/sourcingrequests/{item_id}", response_model=Dict[str, Any])
def update_sourcingrequest(item_id: int, payload: SourcingRequestUpdateSchema):
    """Update existing SourcingRequest record fields."""
    svc = SourcingRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sourcingrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SourcingRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sourcingrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sourcingrequest(item_id: int, hard: bool = Query(False)):
    """Delete SourcingRequest record (soft-delete by default)."""
    svc = SourcingRequestService()
    ok = svc.delete_sourcingrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SourcingRequest with ID {item_id} not found")
    return None

@router.get("/sourcingrequests/analytics/metrics", response_model=Dict[str, Any])
def get_sourcingrequest_metrics():
    """Calculate summary statistical KPIs for SourcingRequest collection."""
    svc = SourcingRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorQuote Endpoints ====================
@router.get("/vendorquotes", response_model=List[Dict[str, Any]])
def list_vendorquotes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorQuote records with pagination and filtering."""
    svc = VendorQuoteService()
    items = svc.list_vendorquotes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorquotes/{item_id}", response_model=Dict[str, Any])
def get_vendorquote_by_id(item_id: int):
    """Retrieve detailed record for VendorQuote by ID."""
    svc = VendorQuoteService()
    item = svc.get_vendorquote_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorQuote with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorquotes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorquote(payload: VendorQuoteCreateSchema):
    """Create new VendorQuote instance in enterprise repository."""
    svc = VendorQuoteService()
    try:
        item = svc.create_vendorquote(
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

@router.put("/vendorquotes/{item_id}", response_model=Dict[str, Any])
def update_vendorquote(item_id: int, payload: VendorQuoteUpdateSchema):
    """Update existing VendorQuote record fields."""
    svc = VendorQuoteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorquote(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorQuote with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorquotes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorquote(item_id: int, hard: bool = Query(False)):
    """Delete VendorQuote record (soft-delete by default)."""
    svc = VendorQuoteService()
    ok = svc.delete_vendorquote(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorQuote with ID {item_id} not found")
    return None

@router.get("/vendorquotes/analytics/metrics", response_model=Dict[str, Any])
def get_vendorquote_metrics():
    """Calculate summary statistical KPIs for VendorQuote collection."""
    svc = VendorQuoteService()
    return svc.calculate_aggregate_metrics()

# ==================== BidComparison Endpoints ====================
@router.get("/bidcomparisons", response_model=List[Dict[str, Any]])
def list_bidcomparisons(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BidComparison records with pagination and filtering."""
    svc = BidComparisonService()
    items = svc.list_bidcomparisons(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bidcomparisons/{item_id}", response_model=Dict[str, Any])
def get_bidcomparison_by_id(item_id: int):
    """Retrieve detailed record for BidComparison by ID."""
    svc = BidComparisonService()
    item = svc.get_bidcomparison_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BidComparison with ID {item_id} not found")
    return item.to_dict()

@router.post("/bidcomparisons", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bidcomparison(payload: BidComparisonCreateSchema):
    """Create new BidComparison instance in enterprise repository."""
    svc = BidComparisonService()
    try:
        item = svc.create_bidcomparison(
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

@router.put("/bidcomparisons/{item_id}", response_model=Dict[str, Any])
def update_bidcomparison(item_id: int, payload: BidComparisonUpdateSchema):
    """Update existing BidComparison record fields."""
    svc = BidComparisonService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bidcomparison(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BidComparison with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bidcomparisons/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bidcomparison(item_id: int, hard: bool = Query(False)):
    """Delete BidComparison record (soft-delete by default)."""
    svc = BidComparisonService()
    ok = svc.delete_bidcomparison(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BidComparison with ID {item_id} not found")
    return None

@router.get("/bidcomparisons/analytics/metrics", response_model=Dict[str, Any])
def get_bidcomparison_metrics():
    """Calculate summary statistical KPIs for BidComparison collection."""
    svc = BidComparisonService()
    return svc.calculate_aggregate_metrics()

# ==================== ContractAgreement Endpoints ====================
@router.get("/contractagreements", response_model=List[Dict[str, Any]])
def list_contractagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContractAgreement records with pagination and filtering."""
    svc = ContractAgreementService()
    items = svc.list_contractagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/contractagreements/{item_id}", response_model=Dict[str, Any])
def get_contractagreement_by_id(item_id: int):
    """Retrieve detailed record for ContractAgreement by ID."""
    svc = ContractAgreementService()
    item = svc.get_contractagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContractAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/contractagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_contractagreement(payload: ContractAgreementCreateSchema):
    """Create new ContractAgreement instance in enterprise repository."""
    svc = ContractAgreementService()
    try:
        item = svc.create_contractagreement(
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

@router.put("/contractagreements/{item_id}", response_model=Dict[str, Any])
def update_contractagreement(item_id: int, payload: ContractAgreementUpdateSchema):
    """Update existing ContractAgreement record fields."""
    svc = ContractAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_contractagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContractAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/contractagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contractagreement(item_id: int, hard: bool = Query(False)):
    """Delete ContractAgreement record (soft-delete by default)."""
    svc = ContractAgreementService()
    ok = svc.delete_contractagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContractAgreement with ID {item_id} not found")
    return None

@router.get("/contractagreements/analytics/metrics", response_model=Dict[str, Any])
def get_contractagreement_metrics():
    """Calculate summary statistical KPIs for ContractAgreement collection."""
    svc = ContractAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== PurchaseRequisition Endpoints ====================
@router.get("/purchaserequisitions", response_model=List[Dict[str, Any]])
def list_purchaserequisitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PurchaseRequisition records with pagination and filtering."""
    svc = PurchaseRequisitionService()
    items = svc.list_purchaserequisitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/purchaserequisitions/{item_id}", response_model=Dict[str, Any])
def get_purchaserequisition_by_id(item_id: int):
    """Retrieve detailed record for PurchaseRequisition by ID."""
    svc = PurchaseRequisitionService()
    item = svc.get_purchaserequisition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PurchaseRequisition with ID {item_id} not found")
    return item.to_dict()

@router.post("/purchaserequisitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_purchaserequisition(payload: PurchaseRequisitionCreateSchema):
    """Create new PurchaseRequisition instance in enterprise repository."""
    svc = PurchaseRequisitionService()
    try:
        item = svc.create_purchaserequisition(
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

@router.put("/purchaserequisitions/{item_id}", response_model=Dict[str, Any])
def update_purchaserequisition(item_id: int, payload: PurchaseRequisitionUpdateSchema):
    """Update existing PurchaseRequisition record fields."""
    svc = PurchaseRequisitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_purchaserequisition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PurchaseRequisition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/purchaserequisitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_purchaserequisition(item_id: int, hard: bool = Query(False)):
    """Delete PurchaseRequisition record (soft-delete by default)."""
    svc = PurchaseRequisitionService()
    ok = svc.delete_purchaserequisition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PurchaseRequisition with ID {item_id} not found")
    return None

@router.get("/purchaserequisitions/analytics/metrics", response_model=Dict[str, Any])
def get_purchaserequisition_metrics():
    """Calculate summary statistical KPIs for PurchaseRequisition collection."""
    svc = PurchaseRequisitionService()
    return svc.calculate_aggregate_metrics()

# ==================== BlanketPO Endpoints ====================
@router.get("/blanketpos", response_model=List[Dict[str, Any]])
def list_blanketpos(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BlanketPO records with pagination and filtering."""
    svc = BlanketPOService()
    items = svc.list_blanketpos(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/blanketpos/{item_id}", response_model=Dict[str, Any])
def get_blanketpo_by_id(item_id: int):
    """Retrieve detailed record for BlanketPO by ID."""
    svc = BlanketPOService()
    item = svc.get_blanketpo_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BlanketPO with ID {item_id} not found")
    return item.to_dict()

@router.post("/blanketpos", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_blanketpo(payload: BlanketPOCreateSchema):
    """Create new BlanketPO instance in enterprise repository."""
    svc = BlanketPOService()
    try:
        item = svc.create_blanketpo(
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

@router.put("/blanketpos/{item_id}", response_model=Dict[str, Any])
def update_blanketpo(item_id: int, payload: BlanketPOUpdateSchema):
    """Update existing BlanketPO record fields."""
    svc = BlanketPOService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_blanketpo(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BlanketPO with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/blanketpos/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blanketpo(item_id: int, hard: bool = Query(False)):
    """Delete BlanketPO record (soft-delete by default)."""
    svc = BlanketPOService()
    ok = svc.delete_blanketpo(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BlanketPO with ID {item_id} not found")
    return None

@router.get("/blanketpos/analytics/metrics", response_model=Dict[str, Any])
def get_blanketpo_metrics():
    """Calculate summary statistical KPIs for BlanketPO collection."""
    svc = BlanketPOService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorScorecard Endpoints ====================
@router.get("/vendorscorecards", response_model=List[Dict[str, Any]])
def list_vendorscorecards(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorScorecard records with pagination and filtering."""
    svc = VendorScorecardService()
    items = svc.list_vendorscorecards(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorscorecards/{item_id}", response_model=Dict[str, Any])
def get_vendorscorecard_by_id(item_id: int):
    """Retrieve detailed record for VendorScorecard by ID."""
    svc = VendorScorecardService()
    item = svc.get_vendorscorecard_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorScorecard with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorscorecards", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorscorecard(payload: VendorScorecardCreateSchema):
    """Create new VendorScorecard instance in enterprise repository."""
    svc = VendorScorecardService()
    try:
        item = svc.create_vendorscorecard(
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

@router.put("/vendorscorecards/{item_id}", response_model=Dict[str, Any])
def update_vendorscorecard(item_id: int, payload: VendorScorecardUpdateSchema):
    """Update existing VendorScorecard record fields."""
    svc = VendorScorecardService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorscorecard(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorScorecard with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorscorecards/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorscorecard(item_id: int, hard: bool = Query(False)):
    """Delete VendorScorecard record (soft-delete by default)."""
    svc = VendorScorecardService()
    ok = svc.delete_vendorscorecard(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorScorecard with ID {item_id} not found")
    return None

@router.get("/vendorscorecards/analytics/metrics", response_model=Dict[str, Any])
def get_vendorscorecard_metrics():
    """Calculate summary statistical KPIs for VendorScorecard collection."""
    svc = VendorScorecardService()
    return svc.calculate_aggregate_metrics()

# ==================== SpendCategory Endpoints ====================
@router.get("/spendcategorys", response_model=List[Dict[str, Any]])
def list_spendcategorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SpendCategory records with pagination and filtering."""
    svc = SpendCategoryService()
    items = svc.list_spendcategorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/spendcategorys/{item_id}", response_model=Dict[str, Any])
def get_spendcategory_by_id(item_id: int):
    """Retrieve detailed record for SpendCategory by ID."""
    svc = SpendCategoryService()
    item = svc.get_spendcategory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SpendCategory with ID {item_id} not found")
    return item.to_dict()

@router.post("/spendcategorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_spendcategory(payload: SpendCategoryCreateSchema):
    """Create new SpendCategory instance in enterprise repository."""
    svc = SpendCategoryService()
    try:
        item = svc.create_spendcategory(
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

@router.put("/spendcategorys/{item_id}", response_model=Dict[str, Any])
def update_spendcategory(item_id: int, payload: SpendCategoryUpdateSchema):
    """Update existing SpendCategory record fields."""
    svc = SpendCategoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_spendcategory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SpendCategory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/spendcategorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_spendcategory(item_id: int, hard: bool = Query(False)):
    """Delete SpendCategory record (soft-delete by default)."""
    svc = SpendCategoryService()
    ok = svc.delete_spendcategory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SpendCategory with ID {item_id} not found")
    return None

@router.get("/spendcategorys/analytics/metrics", response_model=Dict[str, Any])
def get_spendcategory_metrics():
    """Calculate summary statistical KPIs for SpendCategory collection."""
    svc = SpendCategoryService()
    return svc.calculate_aggregate_metrics()

# ==================== ProcurementPolicy Endpoints ====================
@router.get("/procurementpolicys", response_model=List[Dict[str, Any]])
def list_procurementpolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProcurementPolicy records with pagination and filtering."""
    svc = ProcurementPolicyService()
    items = svc.list_procurementpolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/procurementpolicys/{item_id}", response_model=Dict[str, Any])
def get_procurementpolicy_by_id(item_id: int):
    """Retrieve detailed record for ProcurementPolicy by ID."""
    svc = ProcurementPolicyService()
    item = svc.get_procurementpolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProcurementPolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/procurementpolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_procurementpolicy(payload: ProcurementPolicyCreateSchema):
    """Create new ProcurementPolicy instance in enterprise repository."""
    svc = ProcurementPolicyService()
    try:
        item = svc.create_procurementpolicy(
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

@router.put("/procurementpolicys/{item_id}", response_model=Dict[str, Any])
def update_procurementpolicy(item_id: int, payload: ProcurementPolicyUpdateSchema):
    """Update existing ProcurementPolicy record fields."""
    svc = ProcurementPolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_procurementpolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProcurementPolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/procurementpolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_procurementpolicy(item_id: int, hard: bool = Query(False)):
    """Delete ProcurementPolicy record (soft-delete by default)."""
    svc = ProcurementPolicyService()
    ok = svc.delete_procurementpolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProcurementPolicy with ID {item_id} not found")
    return None

@router.get("/procurementpolicys/analytics/metrics", response_model=Dict[str, Any])
def get_procurementpolicy_metrics():
    """Calculate summary statistical KPIs for ProcurementPolicy collection."""
    svc = ProcurementPolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== CatalogItem Endpoints ====================
@router.get("/catalogitems", response_model=List[Dict[str, Any]])
def list_catalogitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CatalogItem records with pagination and filtering."""
    svc = CatalogItemService()
    items = svc.list_catalogitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/catalogitems/{item_id}", response_model=Dict[str, Any])
def get_catalogitem_by_id(item_id: int):
    """Retrieve detailed record for CatalogItem by ID."""
    svc = CatalogItemService()
    item = svc.get_catalogitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CatalogItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/catalogitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_catalogitem(payload: CatalogItemCreateSchema):
    """Create new CatalogItem instance in enterprise repository."""
    svc = CatalogItemService()
    try:
        item = svc.create_catalogitem(
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

@router.put("/catalogitems/{item_id}", response_model=Dict[str, Any])
def update_catalogitem(item_id: int, payload: CatalogItemUpdateSchema):
    """Update existing CatalogItem record fields."""
    svc = CatalogItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_catalogitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CatalogItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/catalogitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_catalogitem(item_id: int, hard: bool = Query(False)):
    """Delete CatalogItem record (soft-delete by default)."""
    svc = CatalogItemService()
    ok = svc.delete_catalogitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CatalogItem with ID {item_id} not found")
    return None

@router.get("/catalogitems/analytics/metrics", response_model=Dict[str, Any])
def get_catalogitem_metrics():
    """Calculate summary statistical KPIs for CatalogItem collection."""
    svc = CatalogItemService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierTier Endpoints ====================
@router.get("/suppliertiers", response_model=List[Dict[str, Any]])
def list_suppliertiers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierTier records with pagination and filtering."""
    svc = SupplierTierService()
    items = svc.list_suppliertiers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/suppliertiers/{item_id}", response_model=Dict[str, Any])
def get_suppliertier_by_id(item_id: int):
    """Retrieve detailed record for SupplierTier by ID."""
    svc = SupplierTierService()
    item = svc.get_suppliertier_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierTier with ID {item_id} not found")
    return item.to_dict()

@router.post("/suppliertiers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_suppliertier(payload: SupplierTierCreateSchema):
    """Create new SupplierTier instance in enterprise repository."""
    svc = SupplierTierService()
    try:
        item = svc.create_suppliertier(
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

@router.put("/suppliertiers/{item_id}", response_model=Dict[str, Any])
def update_suppliertier(item_id: int, payload: SupplierTierUpdateSchema):
    """Update existing SupplierTier record fields."""
    svc = SupplierTierService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_suppliertier(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierTier with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/suppliertiers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_suppliertier(item_id: int, hard: bool = Query(False)):
    """Delete SupplierTier record (soft-delete by default)."""
    svc = SupplierTierService()
    ok = svc.delete_suppliertier(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierTier with ID {item_id} not found")
    return None

@router.get("/suppliertiers/analytics/metrics", response_model=Dict[str, Any])
def get_suppliertier_metrics():
    """Calculate summary statistical KPIs for SupplierTier collection."""
    svc = SupplierTierService()
    return svc.calculate_aggregate_metrics()

# ==================== RebateProgram Endpoints ====================
@router.get("/rebateprograms", response_model=List[Dict[str, Any]])
def list_rebateprograms(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RebateProgram records with pagination and filtering."""
    svc = RebateProgramService()
    items = svc.list_rebateprograms(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/rebateprograms/{item_id}", response_model=Dict[str, Any])
def get_rebateprogram_by_id(item_id: int):
    """Retrieve detailed record for RebateProgram by ID."""
    svc = RebateProgramService()
    item = svc.get_rebateprogram_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RebateProgram with ID {item_id} not found")
    return item.to_dict()

@router.post("/rebateprograms", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_rebateprogram(payload: RebateProgramCreateSchema):
    """Create new RebateProgram instance in enterprise repository."""
    svc = RebateProgramService()
    try:
        item = svc.create_rebateprogram(
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

@router.put("/rebateprograms/{item_id}", response_model=Dict[str, Any])
def update_rebateprogram(item_id: int, payload: RebateProgramUpdateSchema):
    """Update existing RebateProgram record fields."""
    svc = RebateProgramService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_rebateprogram(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RebateProgram with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/rebateprograms/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rebateprogram(item_id: int, hard: bool = Query(False)):
    """Delete RebateProgram record (soft-delete by default)."""
    svc = RebateProgramService()
    ok = svc.delete_rebateprogram(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RebateProgram with ID {item_id} not found")
    return None

@router.get("/rebateprograms/analytics/metrics", response_model=Dict[str, Any])
def get_rebateprogram_metrics():
    """Calculate summary statistical KPIs for RebateProgram collection."""
    svc = RebateProgramService()
    return svc.calculate_aggregate_metrics()

# ==================== FreightRateAgreement Endpoints ====================
@router.get("/freightrateagreements", response_model=List[Dict[str, Any]])
def list_freightrateagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FreightRateAgreement records with pagination and filtering."""
    svc = FreightRateAgreementService()
    items = svc.list_freightrateagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/freightrateagreements/{item_id}", response_model=Dict[str, Any])
def get_freightrateagreement_by_id(item_id: int):
    """Retrieve detailed record for FreightRateAgreement by ID."""
    svc = FreightRateAgreementService()
    item = svc.get_freightrateagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FreightRateAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/freightrateagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_freightrateagreement(payload: FreightRateAgreementCreateSchema):
    """Create new FreightRateAgreement instance in enterprise repository."""
    svc = FreightRateAgreementService()
    try:
        item = svc.create_freightrateagreement(
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

@router.put("/freightrateagreements/{item_id}", response_model=Dict[str, Any])
def update_freightrateagreement(item_id: int, payload: FreightRateAgreementUpdateSchema):
    """Update existing FreightRateAgreement record fields."""
    svc = FreightRateAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_freightrateagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FreightRateAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/freightrateagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_freightrateagreement(item_id: int, hard: bool = Query(False)):
    """Delete FreightRateAgreement record (soft-delete by default)."""
    svc = FreightRateAgreementService()
    ok = svc.delete_freightrateagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FreightRateAgreement with ID {item_id} not found")
    return None

@router.get("/freightrateagreements/analytics/metrics", response_model=Dict[str, Any])
def get_freightrateagreement_metrics():
    """Calculate summary statistical KPIs for FreightRateAgreement collection."""
    svc = FreightRateAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== ImportPermit Endpoints ====================
@router.get("/importpermits", response_model=List[Dict[str, Any]])
def list_importpermits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ImportPermit records with pagination and filtering."""
    svc = ImportPermitService()
    items = svc.list_importpermits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/importpermits/{item_id}", response_model=Dict[str, Any])
def get_importpermit_by_id(item_id: int):
    """Retrieve detailed record for ImportPermit by ID."""
    svc = ImportPermitService()
    item = svc.get_importpermit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ImportPermit with ID {item_id} not found")
    return item.to_dict()

@router.post("/importpermits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_importpermit(payload: ImportPermitCreateSchema):
    """Create new ImportPermit instance in enterprise repository."""
    svc = ImportPermitService()
    try:
        item = svc.create_importpermit(
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

@router.put("/importpermits/{item_id}", response_model=Dict[str, Any])
def update_importpermit(item_id: int, payload: ImportPermitUpdateSchema):
    """Update existing ImportPermit record fields."""
    svc = ImportPermitService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_importpermit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ImportPermit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/importpermits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_importpermit(item_id: int, hard: bool = Query(False)):
    """Delete ImportPermit record (soft-delete by default)."""
    svc = ImportPermitService()
    ok = svc.delete_importpermit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ImportPermit with ID {item_id} not found")
    return None

@router.get("/importpermits/analytics/metrics", response_model=Dict[str, Any])
def get_importpermit_metrics():
    """Calculate summary statistical KPIs for ImportPermit collection."""
    svc = ImportPermitService()
    return svc.calculate_aggregate_metrics()

# ==================== PurchaseReturn Endpoints ====================
@router.get("/purchasereturns", response_model=List[Dict[str, Any]])
def list_purchasereturns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PurchaseReturn records with pagination and filtering."""
    svc = PurchaseReturnService()
    items = svc.list_purchasereturns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/purchasereturns/{item_id}", response_model=Dict[str, Any])
def get_purchasereturn_by_id(item_id: int):
    """Retrieve detailed record for PurchaseReturn by ID."""
    svc = PurchaseReturnService()
    item = svc.get_purchasereturn_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PurchaseReturn with ID {item_id} not found")
    return item.to_dict()

@router.post("/purchasereturns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_purchasereturn(payload: PurchaseReturnCreateSchema):
    """Create new PurchaseReturn instance in enterprise repository."""
    svc = PurchaseReturnService()
    try:
        item = svc.create_purchasereturn(
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

@router.put("/purchasereturns/{item_id}", response_model=Dict[str, Any])
def update_purchasereturn(item_id: int, payload: PurchaseReturnUpdateSchema):
    """Update existing PurchaseReturn record fields."""
    svc = PurchaseReturnService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_purchasereturn(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PurchaseReturn with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/purchasereturns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_purchasereturn(item_id: int, hard: bool = Query(False)):
    """Delete PurchaseReturn record (soft-delete by default)."""
    svc = PurchaseReturnService()
    ok = svc.delete_purchasereturn(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PurchaseReturn with ID {item_id} not found")
    return None

@router.get("/purchasereturns/analytics/metrics", response_model=Dict[str, Any])
def get_purchasereturn_metrics():
    """Calculate summary statistical KPIs for PurchaseReturn collection."""
    svc = PurchaseReturnService()
    return svc.calculate_aggregate_metrics()

# ==================== PaymentSchedule Endpoints ====================
@router.get("/paymentschedules", response_model=List[Dict[str, Any]])
def list_paymentschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PaymentSchedule records with pagination and filtering."""
    svc = PaymentScheduleService()
    items = svc.list_paymentschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/paymentschedules/{item_id}", response_model=Dict[str, Any])
def get_paymentschedule_by_id(item_id: int):
    """Retrieve detailed record for PaymentSchedule by ID."""
    svc = PaymentScheduleService()
    item = svc.get_paymentschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PaymentSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/paymentschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_paymentschedule(payload: PaymentScheduleCreateSchema):
    """Create new PaymentSchedule instance in enterprise repository."""
    svc = PaymentScheduleService()
    try:
        item = svc.create_paymentschedule(
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

@router.put("/paymentschedules/{item_id}", response_model=Dict[str, Any])
def update_paymentschedule(item_id: int, payload: PaymentScheduleUpdateSchema):
    """Update existing PaymentSchedule record fields."""
    svc = PaymentScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_paymentschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PaymentSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/paymentschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_paymentschedule(item_id: int, hard: bool = Query(False)):
    """Delete PaymentSchedule record (soft-delete by default)."""
    svc = PaymentScheduleService()
    ok = svc.delete_paymentschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PaymentSchedule with ID {item_id} not found")
    return None

@router.get("/paymentschedules/analytics/metrics", response_model=Dict[str, Any])
def get_paymentschedule_metrics():
    """Calculate summary statistical KPIs for PaymentSchedule collection."""
    svc = PaymentScheduleService()
    return svc.calculate_aggregate_metrics()

