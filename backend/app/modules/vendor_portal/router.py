"""
Supplier Collaboration & Vendor Portal - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    VendorPortalUserService,
    SupplierCompanyProfileService,
    POAcknowledgementService,
    AdvanceShippingNoticeService,
    SupplierInvoiceSubmissionService,
    DebitNoteClaimService,
    PaymentStatusQueryService,
    QualityRejectionFeedbackService,
    VendorDocumentSubmissionService,
    ComplianceCheckAcknowledgementService,
    SupplierScorecardViewService,
    RFQResponseBidService,
    CataloguePriceUpdateService,
    VendorContactDirectoryService,
    SupplierAnnouncementNoticeService,
    BankDetailVerificationService,
)
from .schemas import (
    VendorPortalUserCreateSchema, VendorPortalUserUpdateSchema, VendorPortalUserResponseSchema,
    SupplierCompanyProfileCreateSchema, SupplierCompanyProfileUpdateSchema, SupplierCompanyProfileResponseSchema,
    POAcknowledgementCreateSchema, POAcknowledgementUpdateSchema, POAcknowledgementResponseSchema,
    AdvanceShippingNoticeCreateSchema, AdvanceShippingNoticeUpdateSchema, AdvanceShippingNoticeResponseSchema,
    SupplierInvoiceSubmissionCreateSchema, SupplierInvoiceSubmissionUpdateSchema, SupplierInvoiceSubmissionResponseSchema,
    DebitNoteClaimCreateSchema, DebitNoteClaimUpdateSchema, DebitNoteClaimResponseSchema,
    PaymentStatusQueryCreateSchema, PaymentStatusQueryUpdateSchema, PaymentStatusQueryResponseSchema,
    QualityRejectionFeedbackCreateSchema, QualityRejectionFeedbackUpdateSchema, QualityRejectionFeedbackResponseSchema,
    VendorDocumentSubmissionCreateSchema, VendorDocumentSubmissionUpdateSchema, VendorDocumentSubmissionResponseSchema,
    ComplianceCheckAcknowledgementCreateSchema, ComplianceCheckAcknowledgementUpdateSchema, ComplianceCheckAcknowledgementResponseSchema,
    SupplierScorecardViewCreateSchema, SupplierScorecardViewUpdateSchema, SupplierScorecardViewResponseSchema,
    RFQResponseBidCreateSchema, RFQResponseBidUpdateSchema, RFQResponseBidResponseSchema,
    CataloguePriceUpdateCreateSchema, CataloguePriceUpdateUpdateSchema, CataloguePriceUpdateResponseSchema,
    VendorContactDirectoryCreateSchema, VendorContactDirectoryUpdateSchema, VendorContactDirectoryResponseSchema,
    SupplierAnnouncementNoticeCreateSchema, SupplierAnnouncementNoticeUpdateSchema, SupplierAnnouncementNoticeResponseSchema,
    BankDetailVerificationCreateSchema, BankDetailVerificationUpdateSchema, BankDetailVerificationResponseSchema,
)

router = APIRouter(prefix="/vendor_portal", tags=["Supplier Collaboration & Vendor Portal"])

# ==================== VendorPortalUser Endpoints ====================
@router.get("/vendorportalusers", response_model=List[Dict[str, Any]])
def list_vendorportalusers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorPortalUser records with pagination and filtering."""
    svc = VendorPortalUserService()
    items = svc.list_vendorportalusers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorportalusers/{item_id}", response_model=Dict[str, Any])
def get_vendorportaluser_by_id(item_id: int):
    """Retrieve detailed record for VendorPortalUser by ID."""
    svc = VendorPortalUserService()
    item = svc.get_vendorportaluser_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorPortalUser with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorportalusers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorportaluser(payload: VendorPortalUserCreateSchema):
    """Create new VendorPortalUser instance in enterprise repository."""
    svc = VendorPortalUserService()
    try:
        item = svc.create_vendorportaluser(
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

@router.put("/vendorportalusers/{item_id}", response_model=Dict[str, Any])
def update_vendorportaluser(item_id: int, payload: VendorPortalUserUpdateSchema):
    """Update existing VendorPortalUser record fields."""
    svc = VendorPortalUserService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorportaluser(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorPortalUser with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorportalusers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorportaluser(item_id: int, hard: bool = Query(False)):
    """Delete VendorPortalUser record (soft-delete by default)."""
    svc = VendorPortalUserService()
    ok = svc.delete_vendorportaluser(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorPortalUser with ID {item_id} not found")
    return None

@router.get("/vendorportalusers/analytics/metrics", response_model=Dict[str, Any])
def get_vendorportaluser_metrics():
    """Calculate summary statistical KPIs for VendorPortalUser collection."""
    svc = VendorPortalUserService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierCompanyProfile Endpoints ====================
@router.get("/suppliercompanyprofiles", response_model=List[Dict[str, Any]])
def list_suppliercompanyprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierCompanyProfile records with pagination and filtering."""
    svc = SupplierCompanyProfileService()
    items = svc.list_suppliercompanyprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/suppliercompanyprofiles/{item_id}", response_model=Dict[str, Any])
def get_suppliercompanyprofile_by_id(item_id: int):
    """Retrieve detailed record for SupplierCompanyProfile by ID."""
    svc = SupplierCompanyProfileService()
    item = svc.get_suppliercompanyprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierCompanyProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/suppliercompanyprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_suppliercompanyprofile(payload: SupplierCompanyProfileCreateSchema):
    """Create new SupplierCompanyProfile instance in enterprise repository."""
    svc = SupplierCompanyProfileService()
    try:
        item = svc.create_suppliercompanyprofile(
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

@router.put("/suppliercompanyprofiles/{item_id}", response_model=Dict[str, Any])
def update_suppliercompanyprofile(item_id: int, payload: SupplierCompanyProfileUpdateSchema):
    """Update existing SupplierCompanyProfile record fields."""
    svc = SupplierCompanyProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_suppliercompanyprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierCompanyProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/suppliercompanyprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_suppliercompanyprofile(item_id: int, hard: bool = Query(False)):
    """Delete SupplierCompanyProfile record (soft-delete by default)."""
    svc = SupplierCompanyProfileService()
    ok = svc.delete_suppliercompanyprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierCompanyProfile with ID {item_id} not found")
    return None

@router.get("/suppliercompanyprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_suppliercompanyprofile_metrics():
    """Calculate summary statistical KPIs for SupplierCompanyProfile collection."""
    svc = SupplierCompanyProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== POAcknowledgement Endpoints ====================
@router.get("/poacknowledgements", response_model=List[Dict[str, Any]])
def list_poacknowledgements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List POAcknowledgement records with pagination and filtering."""
    svc = POAcknowledgementService()
    items = svc.list_poacknowledgements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/poacknowledgements/{item_id}", response_model=Dict[str, Any])
def get_poacknowledgement_by_id(item_id: int):
    """Retrieve detailed record for POAcknowledgement by ID."""
    svc = POAcknowledgementService()
    item = svc.get_poacknowledgement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"POAcknowledgement with ID {item_id} not found")
    return item.to_dict()

@router.post("/poacknowledgements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_poacknowledgement(payload: POAcknowledgementCreateSchema):
    """Create new POAcknowledgement instance in enterprise repository."""
    svc = POAcknowledgementService()
    try:
        item = svc.create_poacknowledgement(
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

@router.put("/poacknowledgements/{item_id}", response_model=Dict[str, Any])
def update_poacknowledgement(item_id: int, payload: POAcknowledgementUpdateSchema):
    """Update existing POAcknowledgement record fields."""
    svc = POAcknowledgementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_poacknowledgement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"POAcknowledgement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/poacknowledgements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_poacknowledgement(item_id: int, hard: bool = Query(False)):
    """Delete POAcknowledgement record (soft-delete by default)."""
    svc = POAcknowledgementService()
    ok = svc.delete_poacknowledgement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"POAcknowledgement with ID {item_id} not found")
    return None

@router.get("/poacknowledgements/analytics/metrics", response_model=Dict[str, Any])
def get_poacknowledgement_metrics():
    """Calculate summary statistical KPIs for POAcknowledgement collection."""
    svc = POAcknowledgementService()
    return svc.calculate_aggregate_metrics()

# ==================== AdvanceShippingNotice Endpoints ====================
@router.get("/advanceshippingnotices", response_model=List[Dict[str, Any]])
def list_advanceshippingnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AdvanceShippingNotice records with pagination and filtering."""
    svc = AdvanceShippingNoticeService()
    items = svc.list_advanceshippingnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/advanceshippingnotices/{item_id}", response_model=Dict[str, Any])
def get_advanceshippingnotice_by_id(item_id: int):
    """Retrieve detailed record for AdvanceShippingNotice by ID."""
    svc = AdvanceShippingNoticeService()
    item = svc.get_advanceshippingnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AdvanceShippingNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/advanceshippingnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_advanceshippingnotice(payload: AdvanceShippingNoticeCreateSchema):
    """Create new AdvanceShippingNotice instance in enterprise repository."""
    svc = AdvanceShippingNoticeService()
    try:
        item = svc.create_advanceshippingnotice(
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

@router.put("/advanceshippingnotices/{item_id}", response_model=Dict[str, Any])
def update_advanceshippingnotice(item_id: int, payload: AdvanceShippingNoticeUpdateSchema):
    """Update existing AdvanceShippingNotice record fields."""
    svc = AdvanceShippingNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_advanceshippingnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AdvanceShippingNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/advanceshippingnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_advanceshippingnotice(item_id: int, hard: bool = Query(False)):
    """Delete AdvanceShippingNotice record (soft-delete by default)."""
    svc = AdvanceShippingNoticeService()
    ok = svc.delete_advanceshippingnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AdvanceShippingNotice with ID {item_id} not found")
    return None

@router.get("/advanceshippingnotices/analytics/metrics", response_model=Dict[str, Any])
def get_advanceshippingnotice_metrics():
    """Calculate summary statistical KPIs for AdvanceShippingNotice collection."""
    svc = AdvanceShippingNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierInvoiceSubmission Endpoints ====================
@router.get("/supplierinvoicesubmissions", response_model=List[Dict[str, Any]])
def list_supplierinvoicesubmissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierInvoiceSubmission records with pagination and filtering."""
    svc = SupplierInvoiceSubmissionService()
    items = svc.list_supplierinvoicesubmissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supplierinvoicesubmissions/{item_id}", response_model=Dict[str, Any])
def get_supplierinvoicesubmission_by_id(item_id: int):
    """Retrieve detailed record for SupplierInvoiceSubmission by ID."""
    svc = SupplierInvoiceSubmissionService()
    item = svc.get_supplierinvoicesubmission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierInvoiceSubmission with ID {item_id} not found")
    return item.to_dict()

@router.post("/supplierinvoicesubmissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supplierinvoicesubmission(payload: SupplierInvoiceSubmissionCreateSchema):
    """Create new SupplierInvoiceSubmission instance in enterprise repository."""
    svc = SupplierInvoiceSubmissionService()
    try:
        item = svc.create_supplierinvoicesubmission(
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

@router.put("/supplierinvoicesubmissions/{item_id}", response_model=Dict[str, Any])
def update_supplierinvoicesubmission(item_id: int, payload: SupplierInvoiceSubmissionUpdateSchema):
    """Update existing SupplierInvoiceSubmission record fields."""
    svc = SupplierInvoiceSubmissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supplierinvoicesubmission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierInvoiceSubmission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supplierinvoicesubmissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplierinvoicesubmission(item_id: int, hard: bool = Query(False)):
    """Delete SupplierInvoiceSubmission record (soft-delete by default)."""
    svc = SupplierInvoiceSubmissionService()
    ok = svc.delete_supplierinvoicesubmission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierInvoiceSubmission with ID {item_id} not found")
    return None

@router.get("/supplierinvoicesubmissions/analytics/metrics", response_model=Dict[str, Any])
def get_supplierinvoicesubmission_metrics():
    """Calculate summary statistical KPIs for SupplierInvoiceSubmission collection."""
    svc = SupplierInvoiceSubmissionService()
    return svc.calculate_aggregate_metrics()

# ==================== DebitNoteClaim Endpoints ====================
@router.get("/debitnoteclaims", response_model=List[Dict[str, Any]])
def list_debitnoteclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DebitNoteClaim records with pagination and filtering."""
    svc = DebitNoteClaimService()
    items = svc.list_debitnoteclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/debitnoteclaims/{item_id}", response_model=Dict[str, Any])
def get_debitnoteclaim_by_id(item_id: int):
    """Retrieve detailed record for DebitNoteClaim by ID."""
    svc = DebitNoteClaimService()
    item = svc.get_debitnoteclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DebitNoteClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/debitnoteclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_debitnoteclaim(payload: DebitNoteClaimCreateSchema):
    """Create new DebitNoteClaim instance in enterprise repository."""
    svc = DebitNoteClaimService()
    try:
        item = svc.create_debitnoteclaim(
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

@router.put("/debitnoteclaims/{item_id}", response_model=Dict[str, Any])
def update_debitnoteclaim(item_id: int, payload: DebitNoteClaimUpdateSchema):
    """Update existing DebitNoteClaim record fields."""
    svc = DebitNoteClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_debitnoteclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DebitNoteClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/debitnoteclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_debitnoteclaim(item_id: int, hard: bool = Query(False)):
    """Delete DebitNoteClaim record (soft-delete by default)."""
    svc = DebitNoteClaimService()
    ok = svc.delete_debitnoteclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DebitNoteClaim with ID {item_id} not found")
    return None

@router.get("/debitnoteclaims/analytics/metrics", response_model=Dict[str, Any])
def get_debitnoteclaim_metrics():
    """Calculate summary statistical KPIs for DebitNoteClaim collection."""
    svc = DebitNoteClaimService()
    return svc.calculate_aggregate_metrics()

# ==================== PaymentStatusQuery Endpoints ====================
@router.get("/paymentstatusquerys", response_model=List[Dict[str, Any]])
def list_paymentstatusquerys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PaymentStatusQuery records with pagination and filtering."""
    svc = PaymentStatusQueryService()
    items = svc.list_paymentstatusquerys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/paymentstatusquerys/{item_id}", response_model=Dict[str, Any])
def get_paymentstatusquery_by_id(item_id: int):
    """Retrieve detailed record for PaymentStatusQuery by ID."""
    svc = PaymentStatusQueryService()
    item = svc.get_paymentstatusquery_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PaymentStatusQuery with ID {item_id} not found")
    return item.to_dict()

@router.post("/paymentstatusquerys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_paymentstatusquery(payload: PaymentStatusQueryCreateSchema):
    """Create new PaymentStatusQuery instance in enterprise repository."""
    svc = PaymentStatusQueryService()
    try:
        item = svc.create_paymentstatusquery(
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

@router.put("/paymentstatusquerys/{item_id}", response_model=Dict[str, Any])
def update_paymentstatusquery(item_id: int, payload: PaymentStatusQueryUpdateSchema):
    """Update existing PaymentStatusQuery record fields."""
    svc = PaymentStatusQueryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_paymentstatusquery(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PaymentStatusQuery with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/paymentstatusquerys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_paymentstatusquery(item_id: int, hard: bool = Query(False)):
    """Delete PaymentStatusQuery record (soft-delete by default)."""
    svc = PaymentStatusQueryService()
    ok = svc.delete_paymentstatusquery(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PaymentStatusQuery with ID {item_id} not found")
    return None

@router.get("/paymentstatusquerys/analytics/metrics", response_model=Dict[str, Any])
def get_paymentstatusquery_metrics():
    """Calculate summary statistical KPIs for PaymentStatusQuery collection."""
    svc = PaymentStatusQueryService()
    return svc.calculate_aggregate_metrics()

# ==================== QualityRejectionFeedback Endpoints ====================
@router.get("/qualityrejectionfeedbacks", response_model=List[Dict[str, Any]])
def list_qualityrejectionfeedbacks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List QualityRejectionFeedback records with pagination and filtering."""
    svc = QualityRejectionFeedbackService()
    items = svc.list_qualityrejectionfeedbacks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/qualityrejectionfeedbacks/{item_id}", response_model=Dict[str, Any])
def get_qualityrejectionfeedback_by_id(item_id: int):
    """Retrieve detailed record for QualityRejectionFeedback by ID."""
    svc = QualityRejectionFeedbackService()
    item = svc.get_qualityrejectionfeedback_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"QualityRejectionFeedback with ID {item_id} not found")
    return item.to_dict()

@router.post("/qualityrejectionfeedbacks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_qualityrejectionfeedback(payload: QualityRejectionFeedbackCreateSchema):
    """Create new QualityRejectionFeedback instance in enterprise repository."""
    svc = QualityRejectionFeedbackService()
    try:
        item = svc.create_qualityrejectionfeedback(
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

@router.put("/qualityrejectionfeedbacks/{item_id}", response_model=Dict[str, Any])
def update_qualityrejectionfeedback(item_id: int, payload: QualityRejectionFeedbackUpdateSchema):
    """Update existing QualityRejectionFeedback record fields."""
    svc = QualityRejectionFeedbackService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_qualityrejectionfeedback(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"QualityRejectionFeedback with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/qualityrejectionfeedbacks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_qualityrejectionfeedback(item_id: int, hard: bool = Query(False)):
    """Delete QualityRejectionFeedback record (soft-delete by default)."""
    svc = QualityRejectionFeedbackService()
    ok = svc.delete_qualityrejectionfeedback(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"QualityRejectionFeedback with ID {item_id} not found")
    return None

@router.get("/qualityrejectionfeedbacks/analytics/metrics", response_model=Dict[str, Any])
def get_qualityrejectionfeedback_metrics():
    """Calculate summary statistical KPIs for QualityRejectionFeedback collection."""
    svc = QualityRejectionFeedbackService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorDocumentSubmission Endpoints ====================
@router.get("/vendordocumentsubmissions", response_model=List[Dict[str, Any]])
def list_vendordocumentsubmissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorDocumentSubmission records with pagination and filtering."""
    svc = VendorDocumentSubmissionService()
    items = svc.list_vendordocumentsubmissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendordocumentsubmissions/{item_id}", response_model=Dict[str, Any])
def get_vendordocumentsubmission_by_id(item_id: int):
    """Retrieve detailed record for VendorDocumentSubmission by ID."""
    svc = VendorDocumentSubmissionService()
    item = svc.get_vendordocumentsubmission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorDocumentSubmission with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendordocumentsubmissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendordocumentsubmission(payload: VendorDocumentSubmissionCreateSchema):
    """Create new VendorDocumentSubmission instance in enterprise repository."""
    svc = VendorDocumentSubmissionService()
    try:
        item = svc.create_vendordocumentsubmission(
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

@router.put("/vendordocumentsubmissions/{item_id}", response_model=Dict[str, Any])
def update_vendordocumentsubmission(item_id: int, payload: VendorDocumentSubmissionUpdateSchema):
    """Update existing VendorDocumentSubmission record fields."""
    svc = VendorDocumentSubmissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendordocumentsubmission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorDocumentSubmission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendordocumentsubmissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendordocumentsubmission(item_id: int, hard: bool = Query(False)):
    """Delete VendorDocumentSubmission record (soft-delete by default)."""
    svc = VendorDocumentSubmissionService()
    ok = svc.delete_vendordocumentsubmission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorDocumentSubmission with ID {item_id} not found")
    return None

@router.get("/vendordocumentsubmissions/analytics/metrics", response_model=Dict[str, Any])
def get_vendordocumentsubmission_metrics():
    """Calculate summary statistical KPIs for VendorDocumentSubmission collection."""
    svc = VendorDocumentSubmissionService()
    return svc.calculate_aggregate_metrics()

# ==================== ComplianceCheckAcknowledgement Endpoints ====================
@router.get("/compliancecheckacknowledgements", response_model=List[Dict[str, Any]])
def list_compliancecheckacknowledgements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ComplianceCheckAcknowledgement records with pagination and filtering."""
    svc = ComplianceCheckAcknowledgementService()
    items = svc.list_compliancecheckacknowledgements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/compliancecheckacknowledgements/{item_id}", response_model=Dict[str, Any])
def get_compliancecheckacknowledgement_by_id(item_id: int):
    """Retrieve detailed record for ComplianceCheckAcknowledgement by ID."""
    svc = ComplianceCheckAcknowledgementService()
    item = svc.get_compliancecheckacknowledgement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ComplianceCheckAcknowledgement with ID {item_id} not found")
    return item.to_dict()

@router.post("/compliancecheckacknowledgements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_compliancecheckacknowledgement(payload: ComplianceCheckAcknowledgementCreateSchema):
    """Create new ComplianceCheckAcknowledgement instance in enterprise repository."""
    svc = ComplianceCheckAcknowledgementService()
    try:
        item = svc.create_compliancecheckacknowledgement(
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

@router.put("/compliancecheckacknowledgements/{item_id}", response_model=Dict[str, Any])
def update_compliancecheckacknowledgement(item_id: int, payload: ComplianceCheckAcknowledgementUpdateSchema):
    """Update existing ComplianceCheckAcknowledgement record fields."""
    svc = ComplianceCheckAcknowledgementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_compliancecheckacknowledgement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ComplianceCheckAcknowledgement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/compliancecheckacknowledgements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_compliancecheckacknowledgement(item_id: int, hard: bool = Query(False)):
    """Delete ComplianceCheckAcknowledgement record (soft-delete by default)."""
    svc = ComplianceCheckAcknowledgementService()
    ok = svc.delete_compliancecheckacknowledgement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ComplianceCheckAcknowledgement with ID {item_id} not found")
    return None

@router.get("/compliancecheckacknowledgements/analytics/metrics", response_model=Dict[str, Any])
def get_compliancecheckacknowledgement_metrics():
    """Calculate summary statistical KPIs for ComplianceCheckAcknowledgement collection."""
    svc = ComplianceCheckAcknowledgementService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierScorecardView Endpoints ====================
@router.get("/supplierscorecardviews", response_model=List[Dict[str, Any]])
def list_supplierscorecardviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierScorecardView records with pagination and filtering."""
    svc = SupplierScorecardViewService()
    items = svc.list_supplierscorecardviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supplierscorecardviews/{item_id}", response_model=Dict[str, Any])
def get_supplierscorecardview_by_id(item_id: int):
    """Retrieve detailed record for SupplierScorecardView by ID."""
    svc = SupplierScorecardViewService()
    item = svc.get_supplierscorecardview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierScorecardView with ID {item_id} not found")
    return item.to_dict()

@router.post("/supplierscorecardviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supplierscorecardview(payload: SupplierScorecardViewCreateSchema):
    """Create new SupplierScorecardView instance in enterprise repository."""
    svc = SupplierScorecardViewService()
    try:
        item = svc.create_supplierscorecardview(
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

@router.put("/supplierscorecardviews/{item_id}", response_model=Dict[str, Any])
def update_supplierscorecardview(item_id: int, payload: SupplierScorecardViewUpdateSchema):
    """Update existing SupplierScorecardView record fields."""
    svc = SupplierScorecardViewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supplierscorecardview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierScorecardView with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supplierscorecardviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplierscorecardview(item_id: int, hard: bool = Query(False)):
    """Delete SupplierScorecardView record (soft-delete by default)."""
    svc = SupplierScorecardViewService()
    ok = svc.delete_supplierscorecardview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierScorecardView with ID {item_id} not found")
    return None

@router.get("/supplierscorecardviews/analytics/metrics", response_model=Dict[str, Any])
def get_supplierscorecardview_metrics():
    """Calculate summary statistical KPIs for SupplierScorecardView collection."""
    svc = SupplierScorecardViewService()
    return svc.calculate_aggregate_metrics()

# ==================== RFQResponseBid Endpoints ====================
@router.get("/rfqresponsebids", response_model=List[Dict[str, Any]])
def list_rfqresponsebids(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RFQResponseBid records with pagination and filtering."""
    svc = RFQResponseBidService()
    items = svc.list_rfqresponsebids(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/rfqresponsebids/{item_id}", response_model=Dict[str, Any])
def get_rfqresponsebid_by_id(item_id: int):
    """Retrieve detailed record for RFQResponseBid by ID."""
    svc = RFQResponseBidService()
    item = svc.get_rfqresponsebid_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RFQResponseBid with ID {item_id} not found")
    return item.to_dict()

@router.post("/rfqresponsebids", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_rfqresponsebid(payload: RFQResponseBidCreateSchema):
    """Create new RFQResponseBid instance in enterprise repository."""
    svc = RFQResponseBidService()
    try:
        item = svc.create_rfqresponsebid(
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

@router.put("/rfqresponsebids/{item_id}", response_model=Dict[str, Any])
def update_rfqresponsebid(item_id: int, payload: RFQResponseBidUpdateSchema):
    """Update existing RFQResponseBid record fields."""
    svc = RFQResponseBidService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_rfqresponsebid(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RFQResponseBid with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/rfqresponsebids/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rfqresponsebid(item_id: int, hard: bool = Query(False)):
    """Delete RFQResponseBid record (soft-delete by default)."""
    svc = RFQResponseBidService()
    ok = svc.delete_rfqresponsebid(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RFQResponseBid with ID {item_id} not found")
    return None

@router.get("/rfqresponsebids/analytics/metrics", response_model=Dict[str, Any])
def get_rfqresponsebid_metrics():
    """Calculate summary statistical KPIs for RFQResponseBid collection."""
    svc = RFQResponseBidService()
    return svc.calculate_aggregate_metrics()

# ==================== CataloguePriceUpdate Endpoints ====================
@router.get("/cataloguepriceupdates", response_model=List[Dict[str, Any]])
def list_cataloguepriceupdates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CataloguePriceUpdate records with pagination and filtering."""
    svc = CataloguePriceUpdateService()
    items = svc.list_cataloguepriceupdates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cataloguepriceupdates/{item_id}", response_model=Dict[str, Any])
def get_cataloguepriceupdate_by_id(item_id: int):
    """Retrieve detailed record for CataloguePriceUpdate by ID."""
    svc = CataloguePriceUpdateService()
    item = svc.get_cataloguepriceupdate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CataloguePriceUpdate with ID {item_id} not found")
    return item.to_dict()

@router.post("/cataloguepriceupdates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cataloguepriceupdate(payload: CataloguePriceUpdateCreateSchema):
    """Create new CataloguePriceUpdate instance in enterprise repository."""
    svc = CataloguePriceUpdateService()
    try:
        item = svc.create_cataloguepriceupdate(
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

@router.put("/cataloguepriceupdates/{item_id}", response_model=Dict[str, Any])
def update_cataloguepriceupdate(item_id: int, payload: CataloguePriceUpdateUpdateSchema):
    """Update existing CataloguePriceUpdate record fields."""
    svc = CataloguePriceUpdateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cataloguepriceupdate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CataloguePriceUpdate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cataloguepriceupdates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cataloguepriceupdate(item_id: int, hard: bool = Query(False)):
    """Delete CataloguePriceUpdate record (soft-delete by default)."""
    svc = CataloguePriceUpdateService()
    ok = svc.delete_cataloguepriceupdate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CataloguePriceUpdate with ID {item_id} not found")
    return None

@router.get("/cataloguepriceupdates/analytics/metrics", response_model=Dict[str, Any])
def get_cataloguepriceupdate_metrics():
    """Calculate summary statistical KPIs for CataloguePriceUpdate collection."""
    svc = CataloguePriceUpdateService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorContactDirectory Endpoints ====================
@router.get("/vendorcontactdirectorys", response_model=List[Dict[str, Any]])
def list_vendorcontactdirectorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorContactDirectory records with pagination and filtering."""
    svc = VendorContactDirectoryService()
    items = svc.list_vendorcontactdirectorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorcontactdirectorys/{item_id}", response_model=Dict[str, Any])
def get_vendorcontactdirectory_by_id(item_id: int):
    """Retrieve detailed record for VendorContactDirectory by ID."""
    svc = VendorContactDirectoryService()
    item = svc.get_vendorcontactdirectory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorContactDirectory with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorcontactdirectorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorcontactdirectory(payload: VendorContactDirectoryCreateSchema):
    """Create new VendorContactDirectory instance in enterprise repository."""
    svc = VendorContactDirectoryService()
    try:
        item = svc.create_vendorcontactdirectory(
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

@router.put("/vendorcontactdirectorys/{item_id}", response_model=Dict[str, Any])
def update_vendorcontactdirectory(item_id: int, payload: VendorContactDirectoryUpdateSchema):
    """Update existing VendorContactDirectory record fields."""
    svc = VendorContactDirectoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorcontactdirectory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorContactDirectory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorcontactdirectorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorcontactdirectory(item_id: int, hard: bool = Query(False)):
    """Delete VendorContactDirectory record (soft-delete by default)."""
    svc = VendorContactDirectoryService()
    ok = svc.delete_vendorcontactdirectory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorContactDirectory with ID {item_id} not found")
    return None

@router.get("/vendorcontactdirectorys/analytics/metrics", response_model=Dict[str, Any])
def get_vendorcontactdirectory_metrics():
    """Calculate summary statistical KPIs for VendorContactDirectory collection."""
    svc = VendorContactDirectoryService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierAnnouncementNotice Endpoints ====================
@router.get("/supplierannouncementnotices", response_model=List[Dict[str, Any]])
def list_supplierannouncementnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierAnnouncementNotice records with pagination and filtering."""
    svc = SupplierAnnouncementNoticeService()
    items = svc.list_supplierannouncementnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supplierannouncementnotices/{item_id}", response_model=Dict[str, Any])
def get_supplierannouncementnotice_by_id(item_id: int):
    """Retrieve detailed record for SupplierAnnouncementNotice by ID."""
    svc = SupplierAnnouncementNoticeService()
    item = svc.get_supplierannouncementnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierAnnouncementNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/supplierannouncementnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supplierannouncementnotice(payload: SupplierAnnouncementNoticeCreateSchema):
    """Create new SupplierAnnouncementNotice instance in enterprise repository."""
    svc = SupplierAnnouncementNoticeService()
    try:
        item = svc.create_supplierannouncementnotice(
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

@router.put("/supplierannouncementnotices/{item_id}", response_model=Dict[str, Any])
def update_supplierannouncementnotice(item_id: int, payload: SupplierAnnouncementNoticeUpdateSchema):
    """Update existing SupplierAnnouncementNotice record fields."""
    svc = SupplierAnnouncementNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supplierannouncementnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierAnnouncementNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supplierannouncementnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplierannouncementnotice(item_id: int, hard: bool = Query(False)):
    """Delete SupplierAnnouncementNotice record (soft-delete by default)."""
    svc = SupplierAnnouncementNoticeService()
    ok = svc.delete_supplierannouncementnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierAnnouncementNotice with ID {item_id} not found")
    return None

@router.get("/supplierannouncementnotices/analytics/metrics", response_model=Dict[str, Any])
def get_supplierannouncementnotice_metrics():
    """Calculate summary statistical KPIs for SupplierAnnouncementNotice collection."""
    svc = SupplierAnnouncementNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== BankDetailVerification Endpoints ====================
@router.get("/bankdetailverifications", response_model=List[Dict[str, Any]])
def list_bankdetailverifications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BankDetailVerification records with pagination and filtering."""
    svc = BankDetailVerificationService()
    items = svc.list_bankdetailverifications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bankdetailverifications/{item_id}", response_model=Dict[str, Any])
def get_bankdetailverification_by_id(item_id: int):
    """Retrieve detailed record for BankDetailVerification by ID."""
    svc = BankDetailVerificationService()
    item = svc.get_bankdetailverification_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BankDetailVerification with ID {item_id} not found")
    return item.to_dict()

@router.post("/bankdetailverifications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bankdetailverification(payload: BankDetailVerificationCreateSchema):
    """Create new BankDetailVerification instance in enterprise repository."""
    svc = BankDetailVerificationService()
    try:
        item = svc.create_bankdetailverification(
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

@router.put("/bankdetailverifications/{item_id}", response_model=Dict[str, Any])
def update_bankdetailverification(item_id: int, payload: BankDetailVerificationUpdateSchema):
    """Update existing BankDetailVerification record fields."""
    svc = BankDetailVerificationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bankdetailverification(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BankDetailVerification with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bankdetailverifications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bankdetailverification(item_id: int, hard: bool = Query(False)):
    """Delete BankDetailVerification record (soft-delete by default)."""
    svc = BankDetailVerificationService()
    ok = svc.delete_bankdetailverification(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BankDetailVerification with ID {item_id} not found")
    return None

@router.get("/bankdetailverifications/analytics/metrics", response_model=Dict[str, Any])
def get_bankdetailverification_metrics():
    """Calculate summary statistical KPIs for BankDetailVerification collection."""
    svc = BankDetailVerificationService()
    return svc.calculate_aggregate_metrics()

