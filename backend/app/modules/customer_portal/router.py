"""
Customer Self-Service & Commerce Portal - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    CustomerPortalAccountService,
    SelfServiceOrderService,
    PortalInvoiceViewService,
    StatementOfAccountRequestService,
    OnlinePaymentTransactionService,
    SupportTicketSubmissionService,
    ProductCatalogBrowserService,
    SavedOrderTemplateService,
    PriceQuoteRequestService,
    ShipmentTrackingLookupService,
    DocumentDownloadHistoryService,
    ReturnRMARequestService,
    FeedbackReviewSubmissionService,
    LoyaltyRewardRedemptionService,
    AccountManagerContactService,
    SubscriptionSelfManagementService,
)
from .schemas import (
    CustomerPortalAccountCreateSchema, CustomerPortalAccountUpdateSchema, CustomerPortalAccountResponseSchema,
    SelfServiceOrderCreateSchema, SelfServiceOrderUpdateSchema, SelfServiceOrderResponseSchema,
    PortalInvoiceViewCreateSchema, PortalInvoiceViewUpdateSchema, PortalInvoiceViewResponseSchema,
    StatementOfAccountRequestCreateSchema, StatementOfAccountRequestUpdateSchema, StatementOfAccountRequestResponseSchema,
    OnlinePaymentTransactionCreateSchema, OnlinePaymentTransactionUpdateSchema, OnlinePaymentTransactionResponseSchema,
    SupportTicketSubmissionCreateSchema, SupportTicketSubmissionUpdateSchema, SupportTicketSubmissionResponseSchema,
    ProductCatalogBrowserCreateSchema, ProductCatalogBrowserUpdateSchema, ProductCatalogBrowserResponseSchema,
    SavedOrderTemplateCreateSchema, SavedOrderTemplateUpdateSchema, SavedOrderTemplateResponseSchema,
    PriceQuoteRequestCreateSchema, PriceQuoteRequestUpdateSchema, PriceQuoteRequestResponseSchema,
    ShipmentTrackingLookupCreateSchema, ShipmentTrackingLookupUpdateSchema, ShipmentTrackingLookupResponseSchema,
    DocumentDownloadHistoryCreateSchema, DocumentDownloadHistoryUpdateSchema, DocumentDownloadHistoryResponseSchema,
    ReturnRMARequestCreateSchema, ReturnRMARequestUpdateSchema, ReturnRMARequestResponseSchema,
    FeedbackReviewSubmissionCreateSchema, FeedbackReviewSubmissionUpdateSchema, FeedbackReviewSubmissionResponseSchema,
    LoyaltyRewardRedemptionCreateSchema, LoyaltyRewardRedemptionUpdateSchema, LoyaltyRewardRedemptionResponseSchema,
    AccountManagerContactCreateSchema, AccountManagerContactUpdateSchema, AccountManagerContactResponseSchema,
    SubscriptionSelfManagementCreateSchema, SubscriptionSelfManagementUpdateSchema, SubscriptionSelfManagementResponseSchema,
)

router = APIRouter(prefix="/customer_portal", tags=["Customer Self-Service & Commerce Portal"])

# ==================== CustomerPortalAccount Endpoints ====================
@router.get("/customerportalaccounts", response_model=List[Dict[str, Any]])
def list_customerportalaccounts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerPortalAccount records with pagination and filtering."""
    svc = CustomerPortalAccountService()
    items = svc.list_customerportalaccounts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerportalaccounts/{item_id}", response_model=Dict[str, Any])
def get_customerportalaccount_by_id(item_id: int):
    """Retrieve detailed record for CustomerPortalAccount by ID."""
    svc = CustomerPortalAccountService()
    item = svc.get_customerportalaccount_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerPortalAccount with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerportalaccounts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerportalaccount(payload: CustomerPortalAccountCreateSchema):
    """Create new CustomerPortalAccount instance in enterprise repository."""
    svc = CustomerPortalAccountService()
    try:
        item = svc.create_customerportalaccount(
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

@router.put("/customerportalaccounts/{item_id}", response_model=Dict[str, Any])
def update_customerportalaccount(item_id: int, payload: CustomerPortalAccountUpdateSchema):
    """Update existing CustomerPortalAccount record fields."""
    svc = CustomerPortalAccountService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerportalaccount(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerPortalAccount with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerportalaccounts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerportalaccount(item_id: int, hard: bool = Query(False)):
    """Delete CustomerPortalAccount record (soft-delete by default)."""
    svc = CustomerPortalAccountService()
    ok = svc.delete_customerportalaccount(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerPortalAccount with ID {item_id} not found")
    return None

@router.get("/customerportalaccounts/analytics/metrics", response_model=Dict[str, Any])
def get_customerportalaccount_metrics():
    """Calculate summary statistical KPIs for CustomerPortalAccount collection."""
    svc = CustomerPortalAccountService()
    return svc.calculate_aggregate_metrics()

# ==================== SelfServiceOrder Endpoints ====================
@router.get("/selfserviceorders", response_model=List[Dict[str, Any]])
def list_selfserviceorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SelfServiceOrder records with pagination and filtering."""
    svc = SelfServiceOrderService()
    items = svc.list_selfserviceorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/selfserviceorders/{item_id}", response_model=Dict[str, Any])
def get_selfserviceorder_by_id(item_id: int):
    """Retrieve detailed record for SelfServiceOrder by ID."""
    svc = SelfServiceOrderService()
    item = svc.get_selfserviceorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SelfServiceOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/selfserviceorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_selfserviceorder(payload: SelfServiceOrderCreateSchema):
    """Create new SelfServiceOrder instance in enterprise repository."""
    svc = SelfServiceOrderService()
    try:
        item = svc.create_selfserviceorder(
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

@router.put("/selfserviceorders/{item_id}", response_model=Dict[str, Any])
def update_selfserviceorder(item_id: int, payload: SelfServiceOrderUpdateSchema):
    """Update existing SelfServiceOrder record fields."""
    svc = SelfServiceOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_selfserviceorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SelfServiceOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/selfserviceorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_selfserviceorder(item_id: int, hard: bool = Query(False)):
    """Delete SelfServiceOrder record (soft-delete by default)."""
    svc = SelfServiceOrderService()
    ok = svc.delete_selfserviceorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SelfServiceOrder with ID {item_id} not found")
    return None

@router.get("/selfserviceorders/analytics/metrics", response_model=Dict[str, Any])
def get_selfserviceorder_metrics():
    """Calculate summary statistical KPIs for SelfServiceOrder collection."""
    svc = SelfServiceOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== PortalInvoiceView Endpoints ====================
@router.get("/portalinvoiceviews", response_model=List[Dict[str, Any]])
def list_portalinvoiceviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PortalInvoiceView records with pagination and filtering."""
    svc = PortalInvoiceViewService()
    items = svc.list_portalinvoiceviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/portalinvoiceviews/{item_id}", response_model=Dict[str, Any])
def get_portalinvoiceview_by_id(item_id: int):
    """Retrieve detailed record for PortalInvoiceView by ID."""
    svc = PortalInvoiceViewService()
    item = svc.get_portalinvoiceview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PortalInvoiceView with ID {item_id} not found")
    return item.to_dict()

@router.post("/portalinvoiceviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_portalinvoiceview(payload: PortalInvoiceViewCreateSchema):
    """Create new PortalInvoiceView instance in enterprise repository."""
    svc = PortalInvoiceViewService()
    try:
        item = svc.create_portalinvoiceview(
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

@router.put("/portalinvoiceviews/{item_id}", response_model=Dict[str, Any])
def update_portalinvoiceview(item_id: int, payload: PortalInvoiceViewUpdateSchema):
    """Update existing PortalInvoiceView record fields."""
    svc = PortalInvoiceViewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_portalinvoiceview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PortalInvoiceView with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/portalinvoiceviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_portalinvoiceview(item_id: int, hard: bool = Query(False)):
    """Delete PortalInvoiceView record (soft-delete by default)."""
    svc = PortalInvoiceViewService()
    ok = svc.delete_portalinvoiceview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PortalInvoiceView with ID {item_id} not found")
    return None

@router.get("/portalinvoiceviews/analytics/metrics", response_model=Dict[str, Any])
def get_portalinvoiceview_metrics():
    """Calculate summary statistical KPIs for PortalInvoiceView collection."""
    svc = PortalInvoiceViewService()
    return svc.calculate_aggregate_metrics()

# ==================== StatementOfAccountRequest Endpoints ====================
@router.get("/statementofaccountrequests", response_model=List[Dict[str, Any]])
def list_statementofaccountrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StatementOfAccountRequest records with pagination and filtering."""
    svc = StatementOfAccountRequestService()
    items = svc.list_statementofaccountrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/statementofaccountrequests/{item_id}", response_model=Dict[str, Any])
def get_statementofaccountrequest_by_id(item_id: int):
    """Retrieve detailed record for StatementOfAccountRequest by ID."""
    svc = StatementOfAccountRequestService()
    item = svc.get_statementofaccountrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StatementOfAccountRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/statementofaccountrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_statementofaccountrequest(payload: StatementOfAccountRequestCreateSchema):
    """Create new StatementOfAccountRequest instance in enterprise repository."""
    svc = StatementOfAccountRequestService()
    try:
        item = svc.create_statementofaccountrequest(
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

@router.put("/statementofaccountrequests/{item_id}", response_model=Dict[str, Any])
def update_statementofaccountrequest(item_id: int, payload: StatementOfAccountRequestUpdateSchema):
    """Update existing StatementOfAccountRequest record fields."""
    svc = StatementOfAccountRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_statementofaccountrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StatementOfAccountRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/statementofaccountrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_statementofaccountrequest(item_id: int, hard: bool = Query(False)):
    """Delete StatementOfAccountRequest record (soft-delete by default)."""
    svc = StatementOfAccountRequestService()
    ok = svc.delete_statementofaccountrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StatementOfAccountRequest with ID {item_id} not found")
    return None

@router.get("/statementofaccountrequests/analytics/metrics", response_model=Dict[str, Any])
def get_statementofaccountrequest_metrics():
    """Calculate summary statistical KPIs for StatementOfAccountRequest collection."""
    svc = StatementOfAccountRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== OnlinePaymentTransaction Endpoints ====================
@router.get("/onlinepaymenttransactions", response_model=List[Dict[str, Any]])
def list_onlinepaymenttransactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OnlinePaymentTransaction records with pagination and filtering."""
    svc = OnlinePaymentTransactionService()
    items = svc.list_onlinepaymenttransactions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/onlinepaymenttransactions/{item_id}", response_model=Dict[str, Any])
def get_onlinepaymenttransaction_by_id(item_id: int):
    """Retrieve detailed record for OnlinePaymentTransaction by ID."""
    svc = OnlinePaymentTransactionService()
    item = svc.get_onlinepaymenttransaction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OnlinePaymentTransaction with ID {item_id} not found")
    return item.to_dict()

@router.post("/onlinepaymenttransactions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_onlinepaymenttransaction(payload: OnlinePaymentTransactionCreateSchema):
    """Create new OnlinePaymentTransaction instance in enterprise repository."""
    svc = OnlinePaymentTransactionService()
    try:
        item = svc.create_onlinepaymenttransaction(
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

@router.put("/onlinepaymenttransactions/{item_id}", response_model=Dict[str, Any])
def update_onlinepaymenttransaction(item_id: int, payload: OnlinePaymentTransactionUpdateSchema):
    """Update existing OnlinePaymentTransaction record fields."""
    svc = OnlinePaymentTransactionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_onlinepaymenttransaction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OnlinePaymentTransaction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/onlinepaymenttransactions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_onlinepaymenttransaction(item_id: int, hard: bool = Query(False)):
    """Delete OnlinePaymentTransaction record (soft-delete by default)."""
    svc = OnlinePaymentTransactionService()
    ok = svc.delete_onlinepaymenttransaction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OnlinePaymentTransaction with ID {item_id} not found")
    return None

@router.get("/onlinepaymenttransactions/analytics/metrics", response_model=Dict[str, Any])
def get_onlinepaymenttransaction_metrics():
    """Calculate summary statistical KPIs for OnlinePaymentTransaction collection."""
    svc = OnlinePaymentTransactionService()
    return svc.calculate_aggregate_metrics()

# ==================== SupportTicketSubmission Endpoints ====================
@router.get("/supportticketsubmissions", response_model=List[Dict[str, Any]])
def list_supportticketsubmissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupportTicketSubmission records with pagination and filtering."""
    svc = SupportTicketSubmissionService()
    items = svc.list_supportticketsubmissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supportticketsubmissions/{item_id}", response_model=Dict[str, Any])
def get_supportticketsubmission_by_id(item_id: int):
    """Retrieve detailed record for SupportTicketSubmission by ID."""
    svc = SupportTicketSubmissionService()
    item = svc.get_supportticketsubmission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupportTicketSubmission with ID {item_id} not found")
    return item.to_dict()

@router.post("/supportticketsubmissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supportticketsubmission(payload: SupportTicketSubmissionCreateSchema):
    """Create new SupportTicketSubmission instance in enterprise repository."""
    svc = SupportTicketSubmissionService()
    try:
        item = svc.create_supportticketsubmission(
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

@router.put("/supportticketsubmissions/{item_id}", response_model=Dict[str, Any])
def update_supportticketsubmission(item_id: int, payload: SupportTicketSubmissionUpdateSchema):
    """Update existing SupportTicketSubmission record fields."""
    svc = SupportTicketSubmissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supportticketsubmission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupportTicketSubmission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supportticketsubmissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supportticketsubmission(item_id: int, hard: bool = Query(False)):
    """Delete SupportTicketSubmission record (soft-delete by default)."""
    svc = SupportTicketSubmissionService()
    ok = svc.delete_supportticketsubmission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupportTicketSubmission with ID {item_id} not found")
    return None

@router.get("/supportticketsubmissions/analytics/metrics", response_model=Dict[str, Any])
def get_supportticketsubmission_metrics():
    """Calculate summary statistical KPIs for SupportTicketSubmission collection."""
    svc = SupportTicketSubmissionService()
    return svc.calculate_aggregate_metrics()

# ==================== ProductCatalogBrowser Endpoints ====================
@router.get("/productcatalogbrowsers", response_model=List[Dict[str, Any]])
def list_productcatalogbrowsers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProductCatalogBrowser records with pagination and filtering."""
    svc = ProductCatalogBrowserService()
    items = svc.list_productcatalogbrowsers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/productcatalogbrowsers/{item_id}", response_model=Dict[str, Any])
def get_productcatalogbrowser_by_id(item_id: int):
    """Retrieve detailed record for ProductCatalogBrowser by ID."""
    svc = ProductCatalogBrowserService()
    item = svc.get_productcatalogbrowser_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProductCatalogBrowser with ID {item_id} not found")
    return item.to_dict()

@router.post("/productcatalogbrowsers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_productcatalogbrowser(payload: ProductCatalogBrowserCreateSchema):
    """Create new ProductCatalogBrowser instance in enterprise repository."""
    svc = ProductCatalogBrowserService()
    try:
        item = svc.create_productcatalogbrowser(
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

@router.put("/productcatalogbrowsers/{item_id}", response_model=Dict[str, Any])
def update_productcatalogbrowser(item_id: int, payload: ProductCatalogBrowserUpdateSchema):
    """Update existing ProductCatalogBrowser record fields."""
    svc = ProductCatalogBrowserService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_productcatalogbrowser(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProductCatalogBrowser with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/productcatalogbrowsers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_productcatalogbrowser(item_id: int, hard: bool = Query(False)):
    """Delete ProductCatalogBrowser record (soft-delete by default)."""
    svc = ProductCatalogBrowserService()
    ok = svc.delete_productcatalogbrowser(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProductCatalogBrowser with ID {item_id} not found")
    return None

@router.get("/productcatalogbrowsers/analytics/metrics", response_model=Dict[str, Any])
def get_productcatalogbrowser_metrics():
    """Calculate summary statistical KPIs for ProductCatalogBrowser collection."""
    svc = ProductCatalogBrowserService()
    return svc.calculate_aggregate_metrics()

# ==================== SavedOrderTemplate Endpoints ====================
@router.get("/savedordertemplates", response_model=List[Dict[str, Any]])
def list_savedordertemplates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SavedOrderTemplate records with pagination and filtering."""
    svc = SavedOrderTemplateService()
    items = svc.list_savedordertemplates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/savedordertemplates/{item_id}", response_model=Dict[str, Any])
def get_savedordertemplate_by_id(item_id: int):
    """Retrieve detailed record for SavedOrderTemplate by ID."""
    svc = SavedOrderTemplateService()
    item = svc.get_savedordertemplate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SavedOrderTemplate with ID {item_id} not found")
    return item.to_dict()

@router.post("/savedordertemplates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_savedordertemplate(payload: SavedOrderTemplateCreateSchema):
    """Create new SavedOrderTemplate instance in enterprise repository."""
    svc = SavedOrderTemplateService()
    try:
        item = svc.create_savedordertemplate(
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

@router.put("/savedordertemplates/{item_id}", response_model=Dict[str, Any])
def update_savedordertemplate(item_id: int, payload: SavedOrderTemplateUpdateSchema):
    """Update existing SavedOrderTemplate record fields."""
    svc = SavedOrderTemplateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_savedordertemplate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SavedOrderTemplate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/savedordertemplates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_savedordertemplate(item_id: int, hard: bool = Query(False)):
    """Delete SavedOrderTemplate record (soft-delete by default)."""
    svc = SavedOrderTemplateService()
    ok = svc.delete_savedordertemplate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SavedOrderTemplate with ID {item_id} not found")
    return None

@router.get("/savedordertemplates/analytics/metrics", response_model=Dict[str, Any])
def get_savedordertemplate_metrics():
    """Calculate summary statistical KPIs for SavedOrderTemplate collection."""
    svc = SavedOrderTemplateService()
    return svc.calculate_aggregate_metrics()

# ==================== PriceQuoteRequest Endpoints ====================
@router.get("/pricequoterequests", response_model=List[Dict[str, Any]])
def list_pricequoterequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PriceQuoteRequest records with pagination and filtering."""
    svc = PriceQuoteRequestService()
    items = svc.list_pricequoterequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/pricequoterequests/{item_id}", response_model=Dict[str, Any])
def get_pricequoterequest_by_id(item_id: int):
    """Retrieve detailed record for PriceQuoteRequest by ID."""
    svc = PriceQuoteRequestService()
    item = svc.get_pricequoterequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PriceQuoteRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/pricequoterequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_pricequoterequest(payload: PriceQuoteRequestCreateSchema):
    """Create new PriceQuoteRequest instance in enterprise repository."""
    svc = PriceQuoteRequestService()
    try:
        item = svc.create_pricequoterequest(
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

@router.put("/pricequoterequests/{item_id}", response_model=Dict[str, Any])
def update_pricequoterequest(item_id: int, payload: PriceQuoteRequestUpdateSchema):
    """Update existing PriceQuoteRequest record fields."""
    svc = PriceQuoteRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_pricequoterequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PriceQuoteRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/pricequoterequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pricequoterequest(item_id: int, hard: bool = Query(False)):
    """Delete PriceQuoteRequest record (soft-delete by default)."""
    svc = PriceQuoteRequestService()
    ok = svc.delete_pricequoterequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PriceQuoteRequest with ID {item_id} not found")
    return None

@router.get("/pricequoterequests/analytics/metrics", response_model=Dict[str, Any])
def get_pricequoterequest_metrics():
    """Calculate summary statistical KPIs for PriceQuoteRequest collection."""
    svc = PriceQuoteRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== ShipmentTrackingLookup Endpoints ====================
@router.get("/shipmenttrackinglookups", response_model=List[Dict[str, Any]])
def list_shipmenttrackinglookups(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShipmentTrackingLookup records with pagination and filtering."""
    svc = ShipmentTrackingLookupService()
    items = svc.list_shipmenttrackinglookups(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shipmenttrackinglookups/{item_id}", response_model=Dict[str, Any])
def get_shipmenttrackinglookup_by_id(item_id: int):
    """Retrieve detailed record for ShipmentTrackingLookup by ID."""
    svc = ShipmentTrackingLookupService()
    item = svc.get_shipmenttrackinglookup_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShipmentTrackingLookup with ID {item_id} not found")
    return item.to_dict()

@router.post("/shipmenttrackinglookups", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shipmenttrackinglookup(payload: ShipmentTrackingLookupCreateSchema):
    """Create new ShipmentTrackingLookup instance in enterprise repository."""
    svc = ShipmentTrackingLookupService()
    try:
        item = svc.create_shipmenttrackinglookup(
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

@router.put("/shipmenttrackinglookups/{item_id}", response_model=Dict[str, Any])
def update_shipmenttrackinglookup(item_id: int, payload: ShipmentTrackingLookupUpdateSchema):
    """Update existing ShipmentTrackingLookup record fields."""
    svc = ShipmentTrackingLookupService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shipmenttrackinglookup(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShipmentTrackingLookup with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shipmenttrackinglookups/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shipmenttrackinglookup(item_id: int, hard: bool = Query(False)):
    """Delete ShipmentTrackingLookup record (soft-delete by default)."""
    svc = ShipmentTrackingLookupService()
    ok = svc.delete_shipmenttrackinglookup(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShipmentTrackingLookup with ID {item_id} not found")
    return None

@router.get("/shipmenttrackinglookups/analytics/metrics", response_model=Dict[str, Any])
def get_shipmenttrackinglookup_metrics():
    """Calculate summary statistical KPIs for ShipmentTrackingLookup collection."""
    svc = ShipmentTrackingLookupService()
    return svc.calculate_aggregate_metrics()

# ==================== DocumentDownloadHistory Endpoints ====================
@router.get("/documentdownloadhistorys", response_model=List[Dict[str, Any]])
def list_documentdownloadhistorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentDownloadHistory records with pagination and filtering."""
    svc = DocumentDownloadHistoryService()
    items = svc.list_documentdownloadhistorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documentdownloadhistorys/{item_id}", response_model=Dict[str, Any])
def get_documentdownloadhistory_by_id(item_id: int):
    """Retrieve detailed record for DocumentDownloadHistory by ID."""
    svc = DocumentDownloadHistoryService()
    item = svc.get_documentdownloadhistory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentDownloadHistory with ID {item_id} not found")
    return item.to_dict()

@router.post("/documentdownloadhistorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documentdownloadhistory(payload: DocumentDownloadHistoryCreateSchema):
    """Create new DocumentDownloadHistory instance in enterprise repository."""
    svc = DocumentDownloadHistoryService()
    try:
        item = svc.create_documentdownloadhistory(
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

@router.put("/documentdownloadhistorys/{item_id}", response_model=Dict[str, Any])
def update_documentdownloadhistory(item_id: int, payload: DocumentDownloadHistoryUpdateSchema):
    """Update existing DocumentDownloadHistory record fields."""
    svc = DocumentDownloadHistoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documentdownloadhistory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentDownloadHistory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documentdownloadhistorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documentdownloadhistory(item_id: int, hard: bool = Query(False)):
    """Delete DocumentDownloadHistory record (soft-delete by default)."""
    svc = DocumentDownloadHistoryService()
    ok = svc.delete_documentdownloadhistory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentDownloadHistory with ID {item_id} not found")
    return None

@router.get("/documentdownloadhistorys/analytics/metrics", response_model=Dict[str, Any])
def get_documentdownloadhistory_metrics():
    """Calculate summary statistical KPIs for DocumentDownloadHistory collection."""
    svc = DocumentDownloadHistoryService()
    return svc.calculate_aggregate_metrics()

# ==================== ReturnRMARequest Endpoints ====================
@router.get("/returnrmarequests", response_model=List[Dict[str, Any]])
def list_returnrmarequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReturnRMARequest records with pagination and filtering."""
    svc = ReturnRMARequestService()
    items = svc.list_returnrmarequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/returnrmarequests/{item_id}", response_model=Dict[str, Any])
def get_returnrmarequest_by_id(item_id: int):
    """Retrieve detailed record for ReturnRMARequest by ID."""
    svc = ReturnRMARequestService()
    item = svc.get_returnrmarequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReturnRMARequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/returnrmarequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_returnrmarequest(payload: ReturnRMARequestCreateSchema):
    """Create new ReturnRMARequest instance in enterprise repository."""
    svc = ReturnRMARequestService()
    try:
        item = svc.create_returnrmarequest(
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

@router.put("/returnrmarequests/{item_id}", response_model=Dict[str, Any])
def update_returnrmarequest(item_id: int, payload: ReturnRMARequestUpdateSchema):
    """Update existing ReturnRMARequest record fields."""
    svc = ReturnRMARequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_returnrmarequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReturnRMARequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/returnrmarequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_returnrmarequest(item_id: int, hard: bool = Query(False)):
    """Delete ReturnRMARequest record (soft-delete by default)."""
    svc = ReturnRMARequestService()
    ok = svc.delete_returnrmarequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReturnRMARequest with ID {item_id} not found")
    return None

@router.get("/returnrmarequests/analytics/metrics", response_model=Dict[str, Any])
def get_returnrmarequest_metrics():
    """Calculate summary statistical KPIs for ReturnRMARequest collection."""
    svc = ReturnRMARequestService()
    return svc.calculate_aggregate_metrics()

# ==================== FeedbackReviewSubmission Endpoints ====================
@router.get("/feedbackreviewsubmissions", response_model=List[Dict[str, Any]])
def list_feedbackreviewsubmissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FeedbackReviewSubmission records with pagination and filtering."""
    svc = FeedbackReviewSubmissionService()
    items = svc.list_feedbackreviewsubmissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/feedbackreviewsubmissions/{item_id}", response_model=Dict[str, Any])
def get_feedbackreviewsubmission_by_id(item_id: int):
    """Retrieve detailed record for FeedbackReviewSubmission by ID."""
    svc = FeedbackReviewSubmissionService()
    item = svc.get_feedbackreviewsubmission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FeedbackReviewSubmission with ID {item_id} not found")
    return item.to_dict()

@router.post("/feedbackreviewsubmissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_feedbackreviewsubmission(payload: FeedbackReviewSubmissionCreateSchema):
    """Create new FeedbackReviewSubmission instance in enterprise repository."""
    svc = FeedbackReviewSubmissionService()
    try:
        item = svc.create_feedbackreviewsubmission(
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

@router.put("/feedbackreviewsubmissions/{item_id}", response_model=Dict[str, Any])
def update_feedbackreviewsubmission(item_id: int, payload: FeedbackReviewSubmissionUpdateSchema):
    """Update existing FeedbackReviewSubmission record fields."""
    svc = FeedbackReviewSubmissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_feedbackreviewsubmission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FeedbackReviewSubmission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/feedbackreviewsubmissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feedbackreviewsubmission(item_id: int, hard: bool = Query(False)):
    """Delete FeedbackReviewSubmission record (soft-delete by default)."""
    svc = FeedbackReviewSubmissionService()
    ok = svc.delete_feedbackreviewsubmission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FeedbackReviewSubmission with ID {item_id} not found")
    return None

@router.get("/feedbackreviewsubmissions/analytics/metrics", response_model=Dict[str, Any])
def get_feedbackreviewsubmission_metrics():
    """Calculate summary statistical KPIs for FeedbackReviewSubmission collection."""
    svc = FeedbackReviewSubmissionService()
    return svc.calculate_aggregate_metrics()

# ==================== LoyaltyRewardRedemption Endpoints ====================
@router.get("/loyaltyrewardredemptions", response_model=List[Dict[str, Any]])
def list_loyaltyrewardredemptions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LoyaltyRewardRedemption records with pagination and filtering."""
    svc = LoyaltyRewardRedemptionService()
    items = svc.list_loyaltyrewardredemptions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/loyaltyrewardredemptions/{item_id}", response_model=Dict[str, Any])
def get_loyaltyrewardredemption_by_id(item_id: int):
    """Retrieve detailed record for LoyaltyRewardRedemption by ID."""
    svc = LoyaltyRewardRedemptionService()
    item = svc.get_loyaltyrewardredemption_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LoyaltyRewardRedemption with ID {item_id} not found")
    return item.to_dict()

@router.post("/loyaltyrewardredemptions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_loyaltyrewardredemption(payload: LoyaltyRewardRedemptionCreateSchema):
    """Create new LoyaltyRewardRedemption instance in enterprise repository."""
    svc = LoyaltyRewardRedemptionService()
    try:
        item = svc.create_loyaltyrewardredemption(
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

@router.put("/loyaltyrewardredemptions/{item_id}", response_model=Dict[str, Any])
def update_loyaltyrewardredemption(item_id: int, payload: LoyaltyRewardRedemptionUpdateSchema):
    """Update existing LoyaltyRewardRedemption record fields."""
    svc = LoyaltyRewardRedemptionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_loyaltyrewardredemption(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LoyaltyRewardRedemption with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/loyaltyrewardredemptions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loyaltyrewardredemption(item_id: int, hard: bool = Query(False)):
    """Delete LoyaltyRewardRedemption record (soft-delete by default)."""
    svc = LoyaltyRewardRedemptionService()
    ok = svc.delete_loyaltyrewardredemption(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LoyaltyRewardRedemption with ID {item_id} not found")
    return None

@router.get("/loyaltyrewardredemptions/analytics/metrics", response_model=Dict[str, Any])
def get_loyaltyrewardredemption_metrics():
    """Calculate summary statistical KPIs for LoyaltyRewardRedemption collection."""
    svc = LoyaltyRewardRedemptionService()
    return svc.calculate_aggregate_metrics()

# ==================== AccountManagerContact Endpoints ====================
@router.get("/accountmanagercontacts", response_model=List[Dict[str, Any]])
def list_accountmanagercontacts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AccountManagerContact records with pagination and filtering."""
    svc = AccountManagerContactService()
    items = svc.list_accountmanagercontacts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/accountmanagercontacts/{item_id}", response_model=Dict[str, Any])
def get_accountmanagercontact_by_id(item_id: int):
    """Retrieve detailed record for AccountManagerContact by ID."""
    svc = AccountManagerContactService()
    item = svc.get_accountmanagercontact_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AccountManagerContact with ID {item_id} not found")
    return item.to_dict()

@router.post("/accountmanagercontacts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_accountmanagercontact(payload: AccountManagerContactCreateSchema):
    """Create new AccountManagerContact instance in enterprise repository."""
    svc = AccountManagerContactService()
    try:
        item = svc.create_accountmanagercontact(
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

@router.put("/accountmanagercontacts/{item_id}", response_model=Dict[str, Any])
def update_accountmanagercontact(item_id: int, payload: AccountManagerContactUpdateSchema):
    """Update existing AccountManagerContact record fields."""
    svc = AccountManagerContactService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_accountmanagercontact(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AccountManagerContact with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/accountmanagercontacts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accountmanagercontact(item_id: int, hard: bool = Query(False)):
    """Delete AccountManagerContact record (soft-delete by default)."""
    svc = AccountManagerContactService()
    ok = svc.delete_accountmanagercontact(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AccountManagerContact with ID {item_id} not found")
    return None

@router.get("/accountmanagercontacts/analytics/metrics", response_model=Dict[str, Any])
def get_accountmanagercontact_metrics():
    """Calculate summary statistical KPIs for AccountManagerContact collection."""
    svc = AccountManagerContactService()
    return svc.calculate_aggregate_metrics()

# ==================== SubscriptionSelfManagement Endpoints ====================
@router.get("/subscriptionselfmanagements", response_model=List[Dict[str, Any]])
def list_subscriptionselfmanagements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SubscriptionSelfManagement records with pagination and filtering."""
    svc = SubscriptionSelfManagementService()
    items = svc.list_subscriptionselfmanagements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/subscriptionselfmanagements/{item_id}", response_model=Dict[str, Any])
def get_subscriptionselfmanagement_by_id(item_id: int):
    """Retrieve detailed record for SubscriptionSelfManagement by ID."""
    svc = SubscriptionSelfManagementService()
    item = svc.get_subscriptionselfmanagement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SubscriptionSelfManagement with ID {item_id} not found")
    return item.to_dict()

@router.post("/subscriptionselfmanagements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_subscriptionselfmanagement(payload: SubscriptionSelfManagementCreateSchema):
    """Create new SubscriptionSelfManagement instance in enterprise repository."""
    svc = SubscriptionSelfManagementService()
    try:
        item = svc.create_subscriptionselfmanagement(
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

@router.put("/subscriptionselfmanagements/{item_id}", response_model=Dict[str, Any])
def update_subscriptionselfmanagement(item_id: int, payload: SubscriptionSelfManagementUpdateSchema):
    """Update existing SubscriptionSelfManagement record fields."""
    svc = SubscriptionSelfManagementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_subscriptionselfmanagement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SubscriptionSelfManagement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/subscriptionselfmanagements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subscriptionselfmanagement(item_id: int, hard: bool = Query(False)):
    """Delete SubscriptionSelfManagement record (soft-delete by default)."""
    svc = SubscriptionSelfManagementService()
    ok = svc.delete_subscriptionselfmanagement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SubscriptionSelfManagement with ID {item_id} not found")
    return None

@router.get("/subscriptionselfmanagements/analytics/metrics", response_model=Dict[str, Any])
def get_subscriptionselfmanagement_metrics():
    """Calculate summary statistical KPIs for SubscriptionSelfManagement collection."""
    svc = SubscriptionSelfManagementService()
    return svc.calculate_aggregate_metrics()

