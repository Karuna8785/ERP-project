"""
Corporate Travel & Expense Reimbursement - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    TravelAuthorizationRequestService,
    FlightReservationBookingService,
    HotelAccommodationRecordService,
    ExpenseReportVoucherService,
    PerDiemAllowanceRateService,
    CorporateCreditCardFeedService,
    ReceiptOCRScanService,
    MileageReimbursementService,
    TravelPolicyRuleService,
    ForeignCurrencyReceiptService,
    CashAdvanceRequestService,
    ExpenseApprovalFlowService,
    NonReimbursableItemService,
    TravelRiskAssessmentService,
    PreferredVendorHotelService,
    SpendAuditAnomalyService,
)
from .schemas import (
    TravelAuthorizationRequestCreateSchema, TravelAuthorizationRequestUpdateSchema, TravelAuthorizationRequestResponseSchema,
    FlightReservationBookingCreateSchema, FlightReservationBookingUpdateSchema, FlightReservationBookingResponseSchema,
    HotelAccommodationRecordCreateSchema, HotelAccommodationRecordUpdateSchema, HotelAccommodationRecordResponseSchema,
    ExpenseReportVoucherCreateSchema, ExpenseReportVoucherUpdateSchema, ExpenseReportVoucherResponseSchema,
    PerDiemAllowanceRateCreateSchema, PerDiemAllowanceRateUpdateSchema, PerDiemAllowanceRateResponseSchema,
    CorporateCreditCardFeedCreateSchema, CorporateCreditCardFeedUpdateSchema, CorporateCreditCardFeedResponseSchema,
    ReceiptOCRScanCreateSchema, ReceiptOCRScanUpdateSchema, ReceiptOCRScanResponseSchema,
    MileageReimbursementCreateSchema, MileageReimbursementUpdateSchema, MileageReimbursementResponseSchema,
    TravelPolicyRuleCreateSchema, TravelPolicyRuleUpdateSchema, TravelPolicyRuleResponseSchema,
    ForeignCurrencyReceiptCreateSchema, ForeignCurrencyReceiptUpdateSchema, ForeignCurrencyReceiptResponseSchema,
    CashAdvanceRequestCreateSchema, CashAdvanceRequestUpdateSchema, CashAdvanceRequestResponseSchema,
    ExpenseApprovalFlowCreateSchema, ExpenseApprovalFlowUpdateSchema, ExpenseApprovalFlowResponseSchema,
    NonReimbursableItemCreateSchema, NonReimbursableItemUpdateSchema, NonReimbursableItemResponseSchema,
    TravelRiskAssessmentCreateSchema, TravelRiskAssessmentUpdateSchema, TravelRiskAssessmentResponseSchema,
    PreferredVendorHotelCreateSchema, PreferredVendorHotelUpdateSchema, PreferredVendorHotelResponseSchema,
    SpendAuditAnomalyCreateSchema, SpendAuditAnomalyUpdateSchema, SpendAuditAnomalyResponseSchema,
)

router = APIRouter(prefix="/travel_expense", tags=["Corporate Travel & Expense Reimbursement"])

# ==================== TravelAuthorizationRequest Endpoints ====================
@router.get("/travelauthorizationrequests", response_model=List[Dict[str, Any]])
def list_travelauthorizationrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TravelAuthorizationRequest records with pagination and filtering."""
    svc = TravelAuthorizationRequestService()
    items = svc.list_travelauthorizationrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/travelauthorizationrequests/{item_id}", response_model=Dict[str, Any])
def get_travelauthorizationrequest_by_id(item_id: int):
    """Retrieve detailed record for TravelAuthorizationRequest by ID."""
    svc = TravelAuthorizationRequestService()
    item = svc.get_travelauthorizationrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TravelAuthorizationRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/travelauthorizationrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_travelauthorizationrequest(payload: TravelAuthorizationRequestCreateSchema):
    """Create new TravelAuthorizationRequest instance in enterprise repository."""
    svc = TravelAuthorizationRequestService()
    try:
        item = svc.create_travelauthorizationrequest(
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

@router.put("/travelauthorizationrequests/{item_id}", response_model=Dict[str, Any])
def update_travelauthorizationrequest(item_id: int, payload: TravelAuthorizationRequestUpdateSchema):
    """Update existing TravelAuthorizationRequest record fields."""
    svc = TravelAuthorizationRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_travelauthorizationrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TravelAuthorizationRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/travelauthorizationrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_travelauthorizationrequest(item_id: int, hard: bool = Query(False)):
    """Delete TravelAuthorizationRequest record (soft-delete by default)."""
    svc = TravelAuthorizationRequestService()
    ok = svc.delete_travelauthorizationrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TravelAuthorizationRequest with ID {item_id} not found")
    return None

@router.get("/travelauthorizationrequests/analytics/metrics", response_model=Dict[str, Any])
def get_travelauthorizationrequest_metrics():
    """Calculate summary statistical KPIs for TravelAuthorizationRequest collection."""
    svc = TravelAuthorizationRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== FlightReservationBooking Endpoints ====================
@router.get("/flightreservationbookings", response_model=List[Dict[str, Any]])
def list_flightreservationbookings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FlightReservationBooking records with pagination and filtering."""
    svc = FlightReservationBookingService()
    items = svc.list_flightreservationbookings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/flightreservationbookings/{item_id}", response_model=Dict[str, Any])
def get_flightreservationbooking_by_id(item_id: int):
    """Retrieve detailed record for FlightReservationBooking by ID."""
    svc = FlightReservationBookingService()
    item = svc.get_flightreservationbooking_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FlightReservationBooking with ID {item_id} not found")
    return item.to_dict()

@router.post("/flightreservationbookings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_flightreservationbooking(payload: FlightReservationBookingCreateSchema):
    """Create new FlightReservationBooking instance in enterprise repository."""
    svc = FlightReservationBookingService()
    try:
        item = svc.create_flightreservationbooking(
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

@router.put("/flightreservationbookings/{item_id}", response_model=Dict[str, Any])
def update_flightreservationbooking(item_id: int, payload: FlightReservationBookingUpdateSchema):
    """Update existing FlightReservationBooking record fields."""
    svc = FlightReservationBookingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_flightreservationbooking(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FlightReservationBooking with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/flightreservationbookings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_flightreservationbooking(item_id: int, hard: bool = Query(False)):
    """Delete FlightReservationBooking record (soft-delete by default)."""
    svc = FlightReservationBookingService()
    ok = svc.delete_flightreservationbooking(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FlightReservationBooking with ID {item_id} not found")
    return None

@router.get("/flightreservationbookings/analytics/metrics", response_model=Dict[str, Any])
def get_flightreservationbooking_metrics():
    """Calculate summary statistical KPIs for FlightReservationBooking collection."""
    svc = FlightReservationBookingService()
    return svc.calculate_aggregate_metrics()

# ==================== HotelAccommodationRecord Endpoints ====================
@router.get("/hotelaccommodationrecords", response_model=List[Dict[str, Any]])
def list_hotelaccommodationrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HotelAccommodationRecord records with pagination and filtering."""
    svc = HotelAccommodationRecordService()
    items = svc.list_hotelaccommodationrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hotelaccommodationrecords/{item_id}", response_model=Dict[str, Any])
def get_hotelaccommodationrecord_by_id(item_id: int):
    """Retrieve detailed record for HotelAccommodationRecord by ID."""
    svc = HotelAccommodationRecordService()
    item = svc.get_hotelaccommodationrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HotelAccommodationRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/hotelaccommodationrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hotelaccommodationrecord(payload: HotelAccommodationRecordCreateSchema):
    """Create new HotelAccommodationRecord instance in enterprise repository."""
    svc = HotelAccommodationRecordService()
    try:
        item = svc.create_hotelaccommodationrecord(
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

@router.put("/hotelaccommodationrecords/{item_id}", response_model=Dict[str, Any])
def update_hotelaccommodationrecord(item_id: int, payload: HotelAccommodationRecordUpdateSchema):
    """Update existing HotelAccommodationRecord record fields."""
    svc = HotelAccommodationRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hotelaccommodationrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HotelAccommodationRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hotelaccommodationrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hotelaccommodationrecord(item_id: int, hard: bool = Query(False)):
    """Delete HotelAccommodationRecord record (soft-delete by default)."""
    svc = HotelAccommodationRecordService()
    ok = svc.delete_hotelaccommodationrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HotelAccommodationRecord with ID {item_id} not found")
    return None

@router.get("/hotelaccommodationrecords/analytics/metrics", response_model=Dict[str, Any])
def get_hotelaccommodationrecord_metrics():
    """Calculate summary statistical KPIs for HotelAccommodationRecord collection."""
    svc = HotelAccommodationRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== ExpenseReportVoucher Endpoints ====================
@router.get("/expensereportvouchers", response_model=List[Dict[str, Any]])
def list_expensereportvouchers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExpenseReportVoucher records with pagination and filtering."""
    svc = ExpenseReportVoucherService()
    items = svc.list_expensereportvouchers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/expensereportvouchers/{item_id}", response_model=Dict[str, Any])
def get_expensereportvoucher_by_id(item_id: int):
    """Retrieve detailed record for ExpenseReportVoucher by ID."""
    svc = ExpenseReportVoucherService()
    item = svc.get_expensereportvoucher_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExpenseReportVoucher with ID {item_id} not found")
    return item.to_dict()

@router.post("/expensereportvouchers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_expensereportvoucher(payload: ExpenseReportVoucherCreateSchema):
    """Create new ExpenseReportVoucher instance in enterprise repository."""
    svc = ExpenseReportVoucherService()
    try:
        item = svc.create_expensereportvoucher(
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

@router.put("/expensereportvouchers/{item_id}", response_model=Dict[str, Any])
def update_expensereportvoucher(item_id: int, payload: ExpenseReportVoucherUpdateSchema):
    """Update existing ExpenseReportVoucher record fields."""
    svc = ExpenseReportVoucherService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_expensereportvoucher(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExpenseReportVoucher with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/expensereportvouchers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expensereportvoucher(item_id: int, hard: bool = Query(False)):
    """Delete ExpenseReportVoucher record (soft-delete by default)."""
    svc = ExpenseReportVoucherService()
    ok = svc.delete_expensereportvoucher(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExpenseReportVoucher with ID {item_id} not found")
    return None

@router.get("/expensereportvouchers/analytics/metrics", response_model=Dict[str, Any])
def get_expensereportvoucher_metrics():
    """Calculate summary statistical KPIs for ExpenseReportVoucher collection."""
    svc = ExpenseReportVoucherService()
    return svc.calculate_aggregate_metrics()

# ==================== PerDiemAllowanceRate Endpoints ====================
@router.get("/perdiemallowancerates", response_model=List[Dict[str, Any]])
def list_perdiemallowancerates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PerDiemAllowanceRate records with pagination and filtering."""
    svc = PerDiemAllowanceRateService()
    items = svc.list_perdiemallowancerates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/perdiemallowancerates/{item_id}", response_model=Dict[str, Any])
def get_perdiemallowancerate_by_id(item_id: int):
    """Retrieve detailed record for PerDiemAllowanceRate by ID."""
    svc = PerDiemAllowanceRateService()
    item = svc.get_perdiemallowancerate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PerDiemAllowanceRate with ID {item_id} not found")
    return item.to_dict()

@router.post("/perdiemallowancerates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_perdiemallowancerate(payload: PerDiemAllowanceRateCreateSchema):
    """Create new PerDiemAllowanceRate instance in enterprise repository."""
    svc = PerDiemAllowanceRateService()
    try:
        item = svc.create_perdiemallowancerate(
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

@router.put("/perdiemallowancerates/{item_id}", response_model=Dict[str, Any])
def update_perdiemallowancerate(item_id: int, payload: PerDiemAllowanceRateUpdateSchema):
    """Update existing PerDiemAllowanceRate record fields."""
    svc = PerDiemAllowanceRateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_perdiemallowancerate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PerDiemAllowanceRate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/perdiemallowancerates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_perdiemallowancerate(item_id: int, hard: bool = Query(False)):
    """Delete PerDiemAllowanceRate record (soft-delete by default)."""
    svc = PerDiemAllowanceRateService()
    ok = svc.delete_perdiemallowancerate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PerDiemAllowanceRate with ID {item_id} not found")
    return None

@router.get("/perdiemallowancerates/analytics/metrics", response_model=Dict[str, Any])
def get_perdiemallowancerate_metrics():
    """Calculate summary statistical KPIs for PerDiemAllowanceRate collection."""
    svc = PerDiemAllowanceRateService()
    return svc.calculate_aggregate_metrics()

# ==================== CorporateCreditCardFeed Endpoints ====================
@router.get("/corporatecreditcardfeeds", response_model=List[Dict[str, Any]])
def list_corporatecreditcardfeeds(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CorporateCreditCardFeed records with pagination and filtering."""
    svc = CorporateCreditCardFeedService()
    items = svc.list_corporatecreditcardfeeds(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/corporatecreditcardfeeds/{item_id}", response_model=Dict[str, Any])
def get_corporatecreditcardfeed_by_id(item_id: int):
    """Retrieve detailed record for CorporateCreditCardFeed by ID."""
    svc = CorporateCreditCardFeedService()
    item = svc.get_corporatecreditcardfeed_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CorporateCreditCardFeed with ID {item_id} not found")
    return item.to_dict()

@router.post("/corporatecreditcardfeeds", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_corporatecreditcardfeed(payload: CorporateCreditCardFeedCreateSchema):
    """Create new CorporateCreditCardFeed instance in enterprise repository."""
    svc = CorporateCreditCardFeedService()
    try:
        item = svc.create_corporatecreditcardfeed(
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

@router.put("/corporatecreditcardfeeds/{item_id}", response_model=Dict[str, Any])
def update_corporatecreditcardfeed(item_id: int, payload: CorporateCreditCardFeedUpdateSchema):
    """Update existing CorporateCreditCardFeed record fields."""
    svc = CorporateCreditCardFeedService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_corporatecreditcardfeed(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CorporateCreditCardFeed with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/corporatecreditcardfeeds/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_corporatecreditcardfeed(item_id: int, hard: bool = Query(False)):
    """Delete CorporateCreditCardFeed record (soft-delete by default)."""
    svc = CorporateCreditCardFeedService()
    ok = svc.delete_corporatecreditcardfeed(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CorporateCreditCardFeed with ID {item_id} not found")
    return None

@router.get("/corporatecreditcardfeeds/analytics/metrics", response_model=Dict[str, Any])
def get_corporatecreditcardfeed_metrics():
    """Calculate summary statistical KPIs for CorporateCreditCardFeed collection."""
    svc = CorporateCreditCardFeedService()
    return svc.calculate_aggregate_metrics()

# ==================== ReceiptOCRScan Endpoints ====================
@router.get("/receiptocrscans", response_model=List[Dict[str, Any]])
def list_receiptocrscans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReceiptOCRScan records with pagination and filtering."""
    svc = ReceiptOCRScanService()
    items = svc.list_receiptocrscans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/receiptocrscans/{item_id}", response_model=Dict[str, Any])
def get_receiptocrscan_by_id(item_id: int):
    """Retrieve detailed record for ReceiptOCRScan by ID."""
    svc = ReceiptOCRScanService()
    item = svc.get_receiptocrscan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReceiptOCRScan with ID {item_id} not found")
    return item.to_dict()

@router.post("/receiptocrscans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_receiptocrscan(payload: ReceiptOCRScanCreateSchema):
    """Create new ReceiptOCRScan instance in enterprise repository."""
    svc = ReceiptOCRScanService()
    try:
        item = svc.create_receiptocrscan(
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

@router.put("/receiptocrscans/{item_id}", response_model=Dict[str, Any])
def update_receiptocrscan(item_id: int, payload: ReceiptOCRScanUpdateSchema):
    """Update existing ReceiptOCRScan record fields."""
    svc = ReceiptOCRScanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_receiptocrscan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReceiptOCRScan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/receiptocrscans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_receiptocrscan(item_id: int, hard: bool = Query(False)):
    """Delete ReceiptOCRScan record (soft-delete by default)."""
    svc = ReceiptOCRScanService()
    ok = svc.delete_receiptocrscan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReceiptOCRScan with ID {item_id} not found")
    return None

@router.get("/receiptocrscans/analytics/metrics", response_model=Dict[str, Any])
def get_receiptocrscan_metrics():
    """Calculate summary statistical KPIs for ReceiptOCRScan collection."""
    svc = ReceiptOCRScanService()
    return svc.calculate_aggregate_metrics()

# ==================== MileageReimbursement Endpoints ====================
@router.get("/mileagereimbursements", response_model=List[Dict[str, Any]])
def list_mileagereimbursements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MileageReimbursement records with pagination and filtering."""
    svc = MileageReimbursementService()
    items = svc.list_mileagereimbursements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/mileagereimbursements/{item_id}", response_model=Dict[str, Any])
def get_mileagereimbursement_by_id(item_id: int):
    """Retrieve detailed record for MileageReimbursement by ID."""
    svc = MileageReimbursementService()
    item = svc.get_mileagereimbursement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MileageReimbursement with ID {item_id} not found")
    return item.to_dict()

@router.post("/mileagereimbursements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_mileagereimbursement(payload: MileageReimbursementCreateSchema):
    """Create new MileageReimbursement instance in enterprise repository."""
    svc = MileageReimbursementService()
    try:
        item = svc.create_mileagereimbursement(
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

@router.put("/mileagereimbursements/{item_id}", response_model=Dict[str, Any])
def update_mileagereimbursement(item_id: int, payload: MileageReimbursementUpdateSchema):
    """Update existing MileageReimbursement record fields."""
    svc = MileageReimbursementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_mileagereimbursement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MileageReimbursement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/mileagereimbursements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mileagereimbursement(item_id: int, hard: bool = Query(False)):
    """Delete MileageReimbursement record (soft-delete by default)."""
    svc = MileageReimbursementService()
    ok = svc.delete_mileagereimbursement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MileageReimbursement with ID {item_id} not found")
    return None

@router.get("/mileagereimbursements/analytics/metrics", response_model=Dict[str, Any])
def get_mileagereimbursement_metrics():
    """Calculate summary statistical KPIs for MileageReimbursement collection."""
    svc = MileageReimbursementService()
    return svc.calculate_aggregate_metrics()

# ==================== TravelPolicyRule Endpoints ====================
@router.get("/travelpolicyrules", response_model=List[Dict[str, Any]])
def list_travelpolicyrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TravelPolicyRule records with pagination and filtering."""
    svc = TravelPolicyRuleService()
    items = svc.list_travelpolicyrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/travelpolicyrules/{item_id}", response_model=Dict[str, Any])
def get_travelpolicyrule_by_id(item_id: int):
    """Retrieve detailed record for TravelPolicyRule by ID."""
    svc = TravelPolicyRuleService()
    item = svc.get_travelpolicyrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TravelPolicyRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/travelpolicyrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_travelpolicyrule(payload: TravelPolicyRuleCreateSchema):
    """Create new TravelPolicyRule instance in enterprise repository."""
    svc = TravelPolicyRuleService()
    try:
        item = svc.create_travelpolicyrule(
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

@router.put("/travelpolicyrules/{item_id}", response_model=Dict[str, Any])
def update_travelpolicyrule(item_id: int, payload: TravelPolicyRuleUpdateSchema):
    """Update existing TravelPolicyRule record fields."""
    svc = TravelPolicyRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_travelpolicyrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TravelPolicyRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/travelpolicyrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_travelpolicyrule(item_id: int, hard: bool = Query(False)):
    """Delete TravelPolicyRule record (soft-delete by default)."""
    svc = TravelPolicyRuleService()
    ok = svc.delete_travelpolicyrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TravelPolicyRule with ID {item_id} not found")
    return None

@router.get("/travelpolicyrules/analytics/metrics", response_model=Dict[str, Any])
def get_travelpolicyrule_metrics():
    """Calculate summary statistical KPIs for TravelPolicyRule collection."""
    svc = TravelPolicyRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== ForeignCurrencyReceipt Endpoints ====================
@router.get("/foreigncurrencyreceipts", response_model=List[Dict[str, Any]])
def list_foreigncurrencyreceipts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ForeignCurrencyReceipt records with pagination and filtering."""
    svc = ForeignCurrencyReceiptService()
    items = svc.list_foreigncurrencyreceipts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/foreigncurrencyreceipts/{item_id}", response_model=Dict[str, Any])
def get_foreigncurrencyreceipt_by_id(item_id: int):
    """Retrieve detailed record for ForeignCurrencyReceipt by ID."""
    svc = ForeignCurrencyReceiptService()
    item = svc.get_foreigncurrencyreceipt_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ForeignCurrencyReceipt with ID {item_id} not found")
    return item.to_dict()

@router.post("/foreigncurrencyreceipts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_foreigncurrencyreceipt(payload: ForeignCurrencyReceiptCreateSchema):
    """Create new ForeignCurrencyReceipt instance in enterprise repository."""
    svc = ForeignCurrencyReceiptService()
    try:
        item = svc.create_foreigncurrencyreceipt(
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

@router.put("/foreigncurrencyreceipts/{item_id}", response_model=Dict[str, Any])
def update_foreigncurrencyreceipt(item_id: int, payload: ForeignCurrencyReceiptUpdateSchema):
    """Update existing ForeignCurrencyReceipt record fields."""
    svc = ForeignCurrencyReceiptService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_foreigncurrencyreceipt(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ForeignCurrencyReceipt with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/foreigncurrencyreceipts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_foreigncurrencyreceipt(item_id: int, hard: bool = Query(False)):
    """Delete ForeignCurrencyReceipt record (soft-delete by default)."""
    svc = ForeignCurrencyReceiptService()
    ok = svc.delete_foreigncurrencyreceipt(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ForeignCurrencyReceipt with ID {item_id} not found")
    return None

@router.get("/foreigncurrencyreceipts/analytics/metrics", response_model=Dict[str, Any])
def get_foreigncurrencyreceipt_metrics():
    """Calculate summary statistical KPIs for ForeignCurrencyReceipt collection."""
    svc = ForeignCurrencyReceiptService()
    return svc.calculate_aggregate_metrics()

# ==================== CashAdvanceRequest Endpoints ====================
@router.get("/cashadvancerequests", response_model=List[Dict[str, Any]])
def list_cashadvancerequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CashAdvanceRequest records with pagination and filtering."""
    svc = CashAdvanceRequestService()
    items = svc.list_cashadvancerequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cashadvancerequests/{item_id}", response_model=Dict[str, Any])
def get_cashadvancerequest_by_id(item_id: int):
    """Retrieve detailed record for CashAdvanceRequest by ID."""
    svc = CashAdvanceRequestService()
    item = svc.get_cashadvancerequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CashAdvanceRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/cashadvancerequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cashadvancerequest(payload: CashAdvanceRequestCreateSchema):
    """Create new CashAdvanceRequest instance in enterprise repository."""
    svc = CashAdvanceRequestService()
    try:
        item = svc.create_cashadvancerequest(
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

@router.put("/cashadvancerequests/{item_id}", response_model=Dict[str, Any])
def update_cashadvancerequest(item_id: int, payload: CashAdvanceRequestUpdateSchema):
    """Update existing CashAdvanceRequest record fields."""
    svc = CashAdvanceRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cashadvancerequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CashAdvanceRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cashadvancerequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cashadvancerequest(item_id: int, hard: bool = Query(False)):
    """Delete CashAdvanceRequest record (soft-delete by default)."""
    svc = CashAdvanceRequestService()
    ok = svc.delete_cashadvancerequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CashAdvanceRequest with ID {item_id} not found")
    return None

@router.get("/cashadvancerequests/analytics/metrics", response_model=Dict[str, Any])
def get_cashadvancerequest_metrics():
    """Calculate summary statistical KPIs for CashAdvanceRequest collection."""
    svc = CashAdvanceRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== ExpenseApprovalFlow Endpoints ====================
@router.get("/expenseapprovalflows", response_model=List[Dict[str, Any]])
def list_expenseapprovalflows(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExpenseApprovalFlow records with pagination and filtering."""
    svc = ExpenseApprovalFlowService()
    items = svc.list_expenseapprovalflows(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/expenseapprovalflows/{item_id}", response_model=Dict[str, Any])
def get_expenseapprovalflow_by_id(item_id: int):
    """Retrieve detailed record for ExpenseApprovalFlow by ID."""
    svc = ExpenseApprovalFlowService()
    item = svc.get_expenseapprovalflow_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExpenseApprovalFlow with ID {item_id} not found")
    return item.to_dict()

@router.post("/expenseapprovalflows", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_expenseapprovalflow(payload: ExpenseApprovalFlowCreateSchema):
    """Create new ExpenseApprovalFlow instance in enterprise repository."""
    svc = ExpenseApprovalFlowService()
    try:
        item = svc.create_expenseapprovalflow(
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

@router.put("/expenseapprovalflows/{item_id}", response_model=Dict[str, Any])
def update_expenseapprovalflow(item_id: int, payload: ExpenseApprovalFlowUpdateSchema):
    """Update existing ExpenseApprovalFlow record fields."""
    svc = ExpenseApprovalFlowService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_expenseapprovalflow(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExpenseApprovalFlow with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/expenseapprovalflows/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expenseapprovalflow(item_id: int, hard: bool = Query(False)):
    """Delete ExpenseApprovalFlow record (soft-delete by default)."""
    svc = ExpenseApprovalFlowService()
    ok = svc.delete_expenseapprovalflow(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExpenseApprovalFlow with ID {item_id} not found")
    return None

@router.get("/expenseapprovalflows/analytics/metrics", response_model=Dict[str, Any])
def get_expenseapprovalflow_metrics():
    """Calculate summary statistical KPIs for ExpenseApprovalFlow collection."""
    svc = ExpenseApprovalFlowService()
    return svc.calculate_aggregate_metrics()

# ==================== NonReimbursableItem Endpoints ====================
@router.get("/nonreimbursableitems", response_model=List[Dict[str, Any]])
def list_nonreimbursableitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List NonReimbursableItem records with pagination and filtering."""
    svc = NonReimbursableItemService()
    items = svc.list_nonreimbursableitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/nonreimbursableitems/{item_id}", response_model=Dict[str, Any])
def get_nonreimbursableitem_by_id(item_id: int):
    """Retrieve detailed record for NonReimbursableItem by ID."""
    svc = NonReimbursableItemService()
    item = svc.get_nonreimbursableitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"NonReimbursableItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/nonreimbursableitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_nonreimbursableitem(payload: NonReimbursableItemCreateSchema):
    """Create new NonReimbursableItem instance in enterprise repository."""
    svc = NonReimbursableItemService()
    try:
        item = svc.create_nonreimbursableitem(
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

@router.put("/nonreimbursableitems/{item_id}", response_model=Dict[str, Any])
def update_nonreimbursableitem(item_id: int, payload: NonReimbursableItemUpdateSchema):
    """Update existing NonReimbursableItem record fields."""
    svc = NonReimbursableItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_nonreimbursableitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"NonReimbursableItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/nonreimbursableitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nonreimbursableitem(item_id: int, hard: bool = Query(False)):
    """Delete NonReimbursableItem record (soft-delete by default)."""
    svc = NonReimbursableItemService()
    ok = svc.delete_nonreimbursableitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"NonReimbursableItem with ID {item_id} not found")
    return None

@router.get("/nonreimbursableitems/analytics/metrics", response_model=Dict[str, Any])
def get_nonreimbursableitem_metrics():
    """Calculate summary statistical KPIs for NonReimbursableItem collection."""
    svc = NonReimbursableItemService()
    return svc.calculate_aggregate_metrics()

# ==================== TravelRiskAssessment Endpoints ====================
@router.get("/travelriskassessments", response_model=List[Dict[str, Any]])
def list_travelriskassessments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TravelRiskAssessment records with pagination and filtering."""
    svc = TravelRiskAssessmentService()
    items = svc.list_travelriskassessments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/travelriskassessments/{item_id}", response_model=Dict[str, Any])
def get_travelriskassessment_by_id(item_id: int):
    """Retrieve detailed record for TravelRiskAssessment by ID."""
    svc = TravelRiskAssessmentService()
    item = svc.get_travelriskassessment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TravelRiskAssessment with ID {item_id} not found")
    return item.to_dict()

@router.post("/travelriskassessments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_travelriskassessment(payload: TravelRiskAssessmentCreateSchema):
    """Create new TravelRiskAssessment instance in enterprise repository."""
    svc = TravelRiskAssessmentService()
    try:
        item = svc.create_travelriskassessment(
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

@router.put("/travelriskassessments/{item_id}", response_model=Dict[str, Any])
def update_travelriskassessment(item_id: int, payload: TravelRiskAssessmentUpdateSchema):
    """Update existing TravelRiskAssessment record fields."""
    svc = TravelRiskAssessmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_travelriskassessment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TravelRiskAssessment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/travelriskassessments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_travelriskassessment(item_id: int, hard: bool = Query(False)):
    """Delete TravelRiskAssessment record (soft-delete by default)."""
    svc = TravelRiskAssessmentService()
    ok = svc.delete_travelriskassessment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TravelRiskAssessment with ID {item_id} not found")
    return None

@router.get("/travelriskassessments/analytics/metrics", response_model=Dict[str, Any])
def get_travelriskassessment_metrics():
    """Calculate summary statistical KPIs for TravelRiskAssessment collection."""
    svc = TravelRiskAssessmentService()
    return svc.calculate_aggregate_metrics()

# ==================== PreferredVendorHotel Endpoints ====================
@router.get("/preferredvendorhotels", response_model=List[Dict[str, Any]])
def list_preferredvendorhotels(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PreferredVendorHotel records with pagination and filtering."""
    svc = PreferredVendorHotelService()
    items = svc.list_preferredvendorhotels(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/preferredvendorhotels/{item_id}", response_model=Dict[str, Any])
def get_preferredvendorhotel_by_id(item_id: int):
    """Retrieve detailed record for PreferredVendorHotel by ID."""
    svc = PreferredVendorHotelService()
    item = svc.get_preferredvendorhotel_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PreferredVendorHotel with ID {item_id} not found")
    return item.to_dict()

@router.post("/preferredvendorhotels", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_preferredvendorhotel(payload: PreferredVendorHotelCreateSchema):
    """Create new PreferredVendorHotel instance in enterprise repository."""
    svc = PreferredVendorHotelService()
    try:
        item = svc.create_preferredvendorhotel(
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

@router.put("/preferredvendorhotels/{item_id}", response_model=Dict[str, Any])
def update_preferredvendorhotel(item_id: int, payload: PreferredVendorHotelUpdateSchema):
    """Update existing PreferredVendorHotel record fields."""
    svc = PreferredVendorHotelService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_preferredvendorhotel(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PreferredVendorHotel with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/preferredvendorhotels/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_preferredvendorhotel(item_id: int, hard: bool = Query(False)):
    """Delete PreferredVendorHotel record (soft-delete by default)."""
    svc = PreferredVendorHotelService()
    ok = svc.delete_preferredvendorhotel(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PreferredVendorHotel with ID {item_id} not found")
    return None

@router.get("/preferredvendorhotels/analytics/metrics", response_model=Dict[str, Any])
def get_preferredvendorhotel_metrics():
    """Calculate summary statistical KPIs for PreferredVendorHotel collection."""
    svc = PreferredVendorHotelService()
    return svc.calculate_aggregate_metrics()

# ==================== SpendAuditAnomaly Endpoints ====================
@router.get("/spendauditanomalys", response_model=List[Dict[str, Any]])
def list_spendauditanomalys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SpendAuditAnomaly records with pagination and filtering."""
    svc = SpendAuditAnomalyService()
    items = svc.list_spendauditanomalys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/spendauditanomalys/{item_id}", response_model=Dict[str, Any])
def get_spendauditanomaly_by_id(item_id: int):
    """Retrieve detailed record for SpendAuditAnomaly by ID."""
    svc = SpendAuditAnomalyService()
    item = svc.get_spendauditanomaly_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SpendAuditAnomaly with ID {item_id} not found")
    return item.to_dict()

@router.post("/spendauditanomalys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_spendauditanomaly(payload: SpendAuditAnomalyCreateSchema):
    """Create new SpendAuditAnomaly instance in enterprise repository."""
    svc = SpendAuditAnomalyService()
    try:
        item = svc.create_spendauditanomaly(
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

@router.put("/spendauditanomalys/{item_id}", response_model=Dict[str, Any])
def update_spendauditanomaly(item_id: int, payload: SpendAuditAnomalyUpdateSchema):
    """Update existing SpendAuditAnomaly record fields."""
    svc = SpendAuditAnomalyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_spendauditanomaly(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SpendAuditAnomaly with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/spendauditanomalys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_spendauditanomaly(item_id: int, hard: bool = Query(False)):
    """Delete SpendAuditAnomaly record (soft-delete by default)."""
    svc = SpendAuditAnomalyService()
    ok = svc.delete_spendauditanomaly(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SpendAuditAnomaly with ID {item_id} not found")
    return None

@router.get("/spendauditanomalys/analytics/metrics", response_model=Dict[str, Any])
def get_spendauditanomaly_metrics():
    """Calculate summary statistical KPIs for SpendAuditAnomaly collection."""
    svc = SpendAuditAnomalyService()
    return svc.calculate_aggregate_metrics()

