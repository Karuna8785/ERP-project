"""
Time, Attendance & Workforce Scheduling - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    BiometricClockPunchService,
    ShiftRosterScheduleService,
    AttendanceDailyRecordService,
    OvertimePreApprovalService,
    BreakTimeIntervalService,
    PublicHolidayCalendarService,
    CompOffEntitlementService,
    TimesheetCorrectionService,
    LateArrivalInfractionService,
    RemoteWorkDeclarationService,
    ShiftSwapRequestService,
    OnCallRosterDutyService,
    GeofenceClockInZoneService,
    StatutoryWorkingHoursService,
    ShiftAllowanceCreditService,
    TimecardSignoffService,
)
from .schemas import (
    BiometricClockPunchCreateSchema, BiometricClockPunchUpdateSchema, BiometricClockPunchResponseSchema,
    ShiftRosterScheduleCreateSchema, ShiftRosterScheduleUpdateSchema, ShiftRosterScheduleResponseSchema,
    AttendanceDailyRecordCreateSchema, AttendanceDailyRecordUpdateSchema, AttendanceDailyRecordResponseSchema,
    OvertimePreApprovalCreateSchema, OvertimePreApprovalUpdateSchema, OvertimePreApprovalResponseSchema,
    BreakTimeIntervalCreateSchema, BreakTimeIntervalUpdateSchema, BreakTimeIntervalResponseSchema,
    PublicHolidayCalendarCreateSchema, PublicHolidayCalendarUpdateSchema, PublicHolidayCalendarResponseSchema,
    CompOffEntitlementCreateSchema, CompOffEntitlementUpdateSchema, CompOffEntitlementResponseSchema,
    TimesheetCorrectionCreateSchema, TimesheetCorrectionUpdateSchema, TimesheetCorrectionResponseSchema,
    LateArrivalInfractionCreateSchema, LateArrivalInfractionUpdateSchema, LateArrivalInfractionResponseSchema,
    RemoteWorkDeclarationCreateSchema, RemoteWorkDeclarationUpdateSchema, RemoteWorkDeclarationResponseSchema,
    ShiftSwapRequestCreateSchema, ShiftSwapRequestUpdateSchema, ShiftSwapRequestResponseSchema,
    OnCallRosterDutyCreateSchema, OnCallRosterDutyUpdateSchema, OnCallRosterDutyResponseSchema,
    GeofenceClockInZoneCreateSchema, GeofenceClockInZoneUpdateSchema, GeofenceClockInZoneResponseSchema,
    StatutoryWorkingHoursCreateSchema, StatutoryWorkingHoursUpdateSchema, StatutoryWorkingHoursResponseSchema,
    ShiftAllowanceCreditCreateSchema, ShiftAllowanceCreditUpdateSchema, ShiftAllowanceCreditResponseSchema,
    TimecardSignoffCreateSchema, TimecardSignoffUpdateSchema, TimecardSignoffResponseSchema,
)

router = APIRouter(prefix="/time_attendance", tags=["Time, Attendance & Workforce Scheduling"])

# ==================== BiometricClockPunch Endpoints ====================
@router.get("/biometricclockpunchs", response_model=List[Dict[str, Any]])
def list_biometricclockpunchs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BiometricClockPunch records with pagination and filtering."""
    svc = BiometricClockPunchService()
    items = svc.list_biometricclockpunchs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/biometricclockpunchs/{item_id}", response_model=Dict[str, Any])
def get_biometricclockpunch_by_id(item_id: int):
    """Retrieve detailed record for BiometricClockPunch by ID."""
    svc = BiometricClockPunchService()
    item = svc.get_biometricclockpunch_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BiometricClockPunch with ID {item_id} not found")
    return item.to_dict()

@router.post("/biometricclockpunchs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_biometricclockpunch(payload: BiometricClockPunchCreateSchema):
    """Create new BiometricClockPunch instance in enterprise repository."""
    svc = BiometricClockPunchService()
    try:
        item = svc.create_biometricclockpunch(
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

@router.put("/biometricclockpunchs/{item_id}", response_model=Dict[str, Any])
def update_biometricclockpunch(item_id: int, payload: BiometricClockPunchUpdateSchema):
    """Update existing BiometricClockPunch record fields."""
    svc = BiometricClockPunchService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_biometricclockpunch(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BiometricClockPunch with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/biometricclockpunchs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_biometricclockpunch(item_id: int, hard: bool = Query(False)):
    """Delete BiometricClockPunch record (soft-delete by default)."""
    svc = BiometricClockPunchService()
    ok = svc.delete_biometricclockpunch(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BiometricClockPunch with ID {item_id} not found")
    return None

@router.get("/biometricclockpunchs/analytics/metrics", response_model=Dict[str, Any])
def get_biometricclockpunch_metrics():
    """Calculate summary statistical KPIs for BiometricClockPunch collection."""
    svc = BiometricClockPunchService()
    return svc.calculate_aggregate_metrics()

# ==================== ShiftRosterSchedule Endpoints ====================
@router.get("/shiftrosterschedules", response_model=List[Dict[str, Any]])
def list_shiftrosterschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShiftRosterSchedule records with pagination and filtering."""
    svc = ShiftRosterScheduleService()
    items = svc.list_shiftrosterschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shiftrosterschedules/{item_id}", response_model=Dict[str, Any])
def get_shiftrosterschedule_by_id(item_id: int):
    """Retrieve detailed record for ShiftRosterSchedule by ID."""
    svc = ShiftRosterScheduleService()
    item = svc.get_shiftrosterschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShiftRosterSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/shiftrosterschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shiftrosterschedule(payload: ShiftRosterScheduleCreateSchema):
    """Create new ShiftRosterSchedule instance in enterprise repository."""
    svc = ShiftRosterScheduleService()
    try:
        item = svc.create_shiftrosterschedule(
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

@router.put("/shiftrosterschedules/{item_id}", response_model=Dict[str, Any])
def update_shiftrosterschedule(item_id: int, payload: ShiftRosterScheduleUpdateSchema):
    """Update existing ShiftRosterSchedule record fields."""
    svc = ShiftRosterScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shiftrosterschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShiftRosterSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shiftrosterschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shiftrosterschedule(item_id: int, hard: bool = Query(False)):
    """Delete ShiftRosterSchedule record (soft-delete by default)."""
    svc = ShiftRosterScheduleService()
    ok = svc.delete_shiftrosterschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShiftRosterSchedule with ID {item_id} not found")
    return None

@router.get("/shiftrosterschedules/analytics/metrics", response_model=Dict[str, Any])
def get_shiftrosterschedule_metrics():
    """Calculate summary statistical KPIs for ShiftRosterSchedule collection."""
    svc = ShiftRosterScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== AttendanceDailyRecord Endpoints ====================
@router.get("/attendancedailyrecords", response_model=List[Dict[str, Any]])
def list_attendancedailyrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AttendanceDailyRecord records with pagination and filtering."""
    svc = AttendanceDailyRecordService()
    items = svc.list_attendancedailyrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/attendancedailyrecords/{item_id}", response_model=Dict[str, Any])
def get_attendancedailyrecord_by_id(item_id: int):
    """Retrieve detailed record for AttendanceDailyRecord by ID."""
    svc = AttendanceDailyRecordService()
    item = svc.get_attendancedailyrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AttendanceDailyRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/attendancedailyrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_attendancedailyrecord(payload: AttendanceDailyRecordCreateSchema):
    """Create new AttendanceDailyRecord instance in enterprise repository."""
    svc = AttendanceDailyRecordService()
    try:
        item = svc.create_attendancedailyrecord(
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

@router.put("/attendancedailyrecords/{item_id}", response_model=Dict[str, Any])
def update_attendancedailyrecord(item_id: int, payload: AttendanceDailyRecordUpdateSchema):
    """Update existing AttendanceDailyRecord record fields."""
    svc = AttendanceDailyRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_attendancedailyrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AttendanceDailyRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/attendancedailyrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attendancedailyrecord(item_id: int, hard: bool = Query(False)):
    """Delete AttendanceDailyRecord record (soft-delete by default)."""
    svc = AttendanceDailyRecordService()
    ok = svc.delete_attendancedailyrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AttendanceDailyRecord with ID {item_id} not found")
    return None

@router.get("/attendancedailyrecords/analytics/metrics", response_model=Dict[str, Any])
def get_attendancedailyrecord_metrics():
    """Calculate summary statistical KPIs for AttendanceDailyRecord collection."""
    svc = AttendanceDailyRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== OvertimePreApproval Endpoints ====================
@router.get("/overtimepreapprovals", response_model=List[Dict[str, Any]])
def list_overtimepreapprovals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OvertimePreApproval records with pagination and filtering."""
    svc = OvertimePreApprovalService()
    items = svc.list_overtimepreapprovals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/overtimepreapprovals/{item_id}", response_model=Dict[str, Any])
def get_overtimepreapproval_by_id(item_id: int):
    """Retrieve detailed record for OvertimePreApproval by ID."""
    svc = OvertimePreApprovalService()
    item = svc.get_overtimepreapproval_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OvertimePreApproval with ID {item_id} not found")
    return item.to_dict()

@router.post("/overtimepreapprovals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_overtimepreapproval(payload: OvertimePreApprovalCreateSchema):
    """Create new OvertimePreApproval instance in enterprise repository."""
    svc = OvertimePreApprovalService()
    try:
        item = svc.create_overtimepreapproval(
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

@router.put("/overtimepreapprovals/{item_id}", response_model=Dict[str, Any])
def update_overtimepreapproval(item_id: int, payload: OvertimePreApprovalUpdateSchema):
    """Update existing OvertimePreApproval record fields."""
    svc = OvertimePreApprovalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_overtimepreapproval(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OvertimePreApproval with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/overtimepreapprovals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_overtimepreapproval(item_id: int, hard: bool = Query(False)):
    """Delete OvertimePreApproval record (soft-delete by default)."""
    svc = OvertimePreApprovalService()
    ok = svc.delete_overtimepreapproval(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OvertimePreApproval with ID {item_id} not found")
    return None

@router.get("/overtimepreapprovals/analytics/metrics", response_model=Dict[str, Any])
def get_overtimepreapproval_metrics():
    """Calculate summary statistical KPIs for OvertimePreApproval collection."""
    svc = OvertimePreApprovalService()
    return svc.calculate_aggregate_metrics()

# ==================== BreakTimeInterval Endpoints ====================
@router.get("/breaktimeintervals", response_model=List[Dict[str, Any]])
def list_breaktimeintervals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BreakTimeInterval records with pagination and filtering."""
    svc = BreakTimeIntervalService()
    items = svc.list_breaktimeintervals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/breaktimeintervals/{item_id}", response_model=Dict[str, Any])
def get_breaktimeinterval_by_id(item_id: int):
    """Retrieve detailed record for BreakTimeInterval by ID."""
    svc = BreakTimeIntervalService()
    item = svc.get_breaktimeinterval_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BreakTimeInterval with ID {item_id} not found")
    return item.to_dict()

@router.post("/breaktimeintervals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_breaktimeinterval(payload: BreakTimeIntervalCreateSchema):
    """Create new BreakTimeInterval instance in enterprise repository."""
    svc = BreakTimeIntervalService()
    try:
        item = svc.create_breaktimeinterval(
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

@router.put("/breaktimeintervals/{item_id}", response_model=Dict[str, Any])
def update_breaktimeinterval(item_id: int, payload: BreakTimeIntervalUpdateSchema):
    """Update existing BreakTimeInterval record fields."""
    svc = BreakTimeIntervalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_breaktimeinterval(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BreakTimeInterval with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/breaktimeintervals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_breaktimeinterval(item_id: int, hard: bool = Query(False)):
    """Delete BreakTimeInterval record (soft-delete by default)."""
    svc = BreakTimeIntervalService()
    ok = svc.delete_breaktimeinterval(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BreakTimeInterval with ID {item_id} not found")
    return None

@router.get("/breaktimeintervals/analytics/metrics", response_model=Dict[str, Any])
def get_breaktimeinterval_metrics():
    """Calculate summary statistical KPIs for BreakTimeInterval collection."""
    svc = BreakTimeIntervalService()
    return svc.calculate_aggregate_metrics()

# ==================== PublicHolidayCalendar Endpoints ====================
@router.get("/publicholidaycalendars", response_model=List[Dict[str, Any]])
def list_publicholidaycalendars(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PublicHolidayCalendar records with pagination and filtering."""
    svc = PublicHolidayCalendarService()
    items = svc.list_publicholidaycalendars(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/publicholidaycalendars/{item_id}", response_model=Dict[str, Any])
def get_publicholidaycalendar_by_id(item_id: int):
    """Retrieve detailed record for PublicHolidayCalendar by ID."""
    svc = PublicHolidayCalendarService()
    item = svc.get_publicholidaycalendar_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PublicHolidayCalendar with ID {item_id} not found")
    return item.to_dict()

@router.post("/publicholidaycalendars", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_publicholidaycalendar(payload: PublicHolidayCalendarCreateSchema):
    """Create new PublicHolidayCalendar instance in enterprise repository."""
    svc = PublicHolidayCalendarService()
    try:
        item = svc.create_publicholidaycalendar(
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

@router.put("/publicholidaycalendars/{item_id}", response_model=Dict[str, Any])
def update_publicholidaycalendar(item_id: int, payload: PublicHolidayCalendarUpdateSchema):
    """Update existing PublicHolidayCalendar record fields."""
    svc = PublicHolidayCalendarService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_publicholidaycalendar(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PublicHolidayCalendar with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/publicholidaycalendars/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_publicholidaycalendar(item_id: int, hard: bool = Query(False)):
    """Delete PublicHolidayCalendar record (soft-delete by default)."""
    svc = PublicHolidayCalendarService()
    ok = svc.delete_publicholidaycalendar(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PublicHolidayCalendar with ID {item_id} not found")
    return None

@router.get("/publicholidaycalendars/analytics/metrics", response_model=Dict[str, Any])
def get_publicholidaycalendar_metrics():
    """Calculate summary statistical KPIs for PublicHolidayCalendar collection."""
    svc = PublicHolidayCalendarService()
    return svc.calculate_aggregate_metrics()

# ==================== CompOffEntitlement Endpoints ====================
@router.get("/compoffentitlements", response_model=List[Dict[str, Any]])
def list_compoffentitlements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CompOffEntitlement records with pagination and filtering."""
    svc = CompOffEntitlementService()
    items = svc.list_compoffentitlements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/compoffentitlements/{item_id}", response_model=Dict[str, Any])
def get_compoffentitlement_by_id(item_id: int):
    """Retrieve detailed record for CompOffEntitlement by ID."""
    svc = CompOffEntitlementService()
    item = svc.get_compoffentitlement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CompOffEntitlement with ID {item_id} not found")
    return item.to_dict()

@router.post("/compoffentitlements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_compoffentitlement(payload: CompOffEntitlementCreateSchema):
    """Create new CompOffEntitlement instance in enterprise repository."""
    svc = CompOffEntitlementService()
    try:
        item = svc.create_compoffentitlement(
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

@router.put("/compoffentitlements/{item_id}", response_model=Dict[str, Any])
def update_compoffentitlement(item_id: int, payload: CompOffEntitlementUpdateSchema):
    """Update existing CompOffEntitlement record fields."""
    svc = CompOffEntitlementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_compoffentitlement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CompOffEntitlement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/compoffentitlements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_compoffentitlement(item_id: int, hard: bool = Query(False)):
    """Delete CompOffEntitlement record (soft-delete by default)."""
    svc = CompOffEntitlementService()
    ok = svc.delete_compoffentitlement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CompOffEntitlement with ID {item_id} not found")
    return None

@router.get("/compoffentitlements/analytics/metrics", response_model=Dict[str, Any])
def get_compoffentitlement_metrics():
    """Calculate summary statistical KPIs for CompOffEntitlement collection."""
    svc = CompOffEntitlementService()
    return svc.calculate_aggregate_metrics()

# ==================== TimesheetCorrection Endpoints ====================
@router.get("/timesheetcorrections", response_model=List[Dict[str, Any]])
def list_timesheetcorrections(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TimesheetCorrection records with pagination and filtering."""
    svc = TimesheetCorrectionService()
    items = svc.list_timesheetcorrections(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/timesheetcorrections/{item_id}", response_model=Dict[str, Any])
def get_timesheetcorrection_by_id(item_id: int):
    """Retrieve detailed record for TimesheetCorrection by ID."""
    svc = TimesheetCorrectionService()
    item = svc.get_timesheetcorrection_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TimesheetCorrection with ID {item_id} not found")
    return item.to_dict()

@router.post("/timesheetcorrections", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_timesheetcorrection(payload: TimesheetCorrectionCreateSchema):
    """Create new TimesheetCorrection instance in enterprise repository."""
    svc = TimesheetCorrectionService()
    try:
        item = svc.create_timesheetcorrection(
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

@router.put("/timesheetcorrections/{item_id}", response_model=Dict[str, Any])
def update_timesheetcorrection(item_id: int, payload: TimesheetCorrectionUpdateSchema):
    """Update existing TimesheetCorrection record fields."""
    svc = TimesheetCorrectionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_timesheetcorrection(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TimesheetCorrection with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/timesheetcorrections/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_timesheetcorrection(item_id: int, hard: bool = Query(False)):
    """Delete TimesheetCorrection record (soft-delete by default)."""
    svc = TimesheetCorrectionService()
    ok = svc.delete_timesheetcorrection(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TimesheetCorrection with ID {item_id} not found")
    return None

@router.get("/timesheetcorrections/analytics/metrics", response_model=Dict[str, Any])
def get_timesheetcorrection_metrics():
    """Calculate summary statistical KPIs for TimesheetCorrection collection."""
    svc = TimesheetCorrectionService()
    return svc.calculate_aggregate_metrics()

# ==================== LateArrivalInfraction Endpoints ====================
@router.get("/latearrivalinfractions", response_model=List[Dict[str, Any]])
def list_latearrivalinfractions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LateArrivalInfraction records with pagination and filtering."""
    svc = LateArrivalInfractionService()
    items = svc.list_latearrivalinfractions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/latearrivalinfractions/{item_id}", response_model=Dict[str, Any])
def get_latearrivalinfraction_by_id(item_id: int):
    """Retrieve detailed record for LateArrivalInfraction by ID."""
    svc = LateArrivalInfractionService()
    item = svc.get_latearrivalinfraction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LateArrivalInfraction with ID {item_id} not found")
    return item.to_dict()

@router.post("/latearrivalinfractions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_latearrivalinfraction(payload: LateArrivalInfractionCreateSchema):
    """Create new LateArrivalInfraction instance in enterprise repository."""
    svc = LateArrivalInfractionService()
    try:
        item = svc.create_latearrivalinfraction(
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

@router.put("/latearrivalinfractions/{item_id}", response_model=Dict[str, Any])
def update_latearrivalinfraction(item_id: int, payload: LateArrivalInfractionUpdateSchema):
    """Update existing LateArrivalInfraction record fields."""
    svc = LateArrivalInfractionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_latearrivalinfraction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LateArrivalInfraction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/latearrivalinfractions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_latearrivalinfraction(item_id: int, hard: bool = Query(False)):
    """Delete LateArrivalInfraction record (soft-delete by default)."""
    svc = LateArrivalInfractionService()
    ok = svc.delete_latearrivalinfraction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LateArrivalInfraction with ID {item_id} not found")
    return None

@router.get("/latearrivalinfractions/analytics/metrics", response_model=Dict[str, Any])
def get_latearrivalinfraction_metrics():
    """Calculate summary statistical KPIs for LateArrivalInfraction collection."""
    svc = LateArrivalInfractionService()
    return svc.calculate_aggregate_metrics()

# ==================== RemoteWorkDeclaration Endpoints ====================
@router.get("/remoteworkdeclarations", response_model=List[Dict[str, Any]])
def list_remoteworkdeclarations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RemoteWorkDeclaration records with pagination and filtering."""
    svc = RemoteWorkDeclarationService()
    items = svc.list_remoteworkdeclarations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/remoteworkdeclarations/{item_id}", response_model=Dict[str, Any])
def get_remoteworkdeclaration_by_id(item_id: int):
    """Retrieve detailed record for RemoteWorkDeclaration by ID."""
    svc = RemoteWorkDeclarationService()
    item = svc.get_remoteworkdeclaration_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RemoteWorkDeclaration with ID {item_id} not found")
    return item.to_dict()

@router.post("/remoteworkdeclarations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_remoteworkdeclaration(payload: RemoteWorkDeclarationCreateSchema):
    """Create new RemoteWorkDeclaration instance in enterprise repository."""
    svc = RemoteWorkDeclarationService()
    try:
        item = svc.create_remoteworkdeclaration(
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

@router.put("/remoteworkdeclarations/{item_id}", response_model=Dict[str, Any])
def update_remoteworkdeclaration(item_id: int, payload: RemoteWorkDeclarationUpdateSchema):
    """Update existing RemoteWorkDeclaration record fields."""
    svc = RemoteWorkDeclarationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_remoteworkdeclaration(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RemoteWorkDeclaration with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/remoteworkdeclarations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_remoteworkdeclaration(item_id: int, hard: bool = Query(False)):
    """Delete RemoteWorkDeclaration record (soft-delete by default)."""
    svc = RemoteWorkDeclarationService()
    ok = svc.delete_remoteworkdeclaration(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RemoteWorkDeclaration with ID {item_id} not found")
    return None

@router.get("/remoteworkdeclarations/analytics/metrics", response_model=Dict[str, Any])
def get_remoteworkdeclaration_metrics():
    """Calculate summary statistical KPIs for RemoteWorkDeclaration collection."""
    svc = RemoteWorkDeclarationService()
    return svc.calculate_aggregate_metrics()

# ==================== ShiftSwapRequest Endpoints ====================
@router.get("/shiftswaprequests", response_model=List[Dict[str, Any]])
def list_shiftswaprequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShiftSwapRequest records with pagination and filtering."""
    svc = ShiftSwapRequestService()
    items = svc.list_shiftswaprequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shiftswaprequests/{item_id}", response_model=Dict[str, Any])
def get_shiftswaprequest_by_id(item_id: int):
    """Retrieve detailed record for ShiftSwapRequest by ID."""
    svc = ShiftSwapRequestService()
    item = svc.get_shiftswaprequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShiftSwapRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/shiftswaprequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shiftswaprequest(payload: ShiftSwapRequestCreateSchema):
    """Create new ShiftSwapRequest instance in enterprise repository."""
    svc = ShiftSwapRequestService()
    try:
        item = svc.create_shiftswaprequest(
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

@router.put("/shiftswaprequests/{item_id}", response_model=Dict[str, Any])
def update_shiftswaprequest(item_id: int, payload: ShiftSwapRequestUpdateSchema):
    """Update existing ShiftSwapRequest record fields."""
    svc = ShiftSwapRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shiftswaprequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShiftSwapRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shiftswaprequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shiftswaprequest(item_id: int, hard: bool = Query(False)):
    """Delete ShiftSwapRequest record (soft-delete by default)."""
    svc = ShiftSwapRequestService()
    ok = svc.delete_shiftswaprequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShiftSwapRequest with ID {item_id} not found")
    return None

@router.get("/shiftswaprequests/analytics/metrics", response_model=Dict[str, Any])
def get_shiftswaprequest_metrics():
    """Calculate summary statistical KPIs for ShiftSwapRequest collection."""
    svc = ShiftSwapRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== OnCallRosterDuty Endpoints ====================
@router.get("/oncallrosterdutys", response_model=List[Dict[str, Any]])
def list_oncallrosterdutys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OnCallRosterDuty records with pagination and filtering."""
    svc = OnCallRosterDutyService()
    items = svc.list_oncallrosterdutys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/oncallrosterdutys/{item_id}", response_model=Dict[str, Any])
def get_oncallrosterduty_by_id(item_id: int):
    """Retrieve detailed record for OnCallRosterDuty by ID."""
    svc = OnCallRosterDutyService()
    item = svc.get_oncallrosterduty_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OnCallRosterDuty with ID {item_id} not found")
    return item.to_dict()

@router.post("/oncallrosterdutys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_oncallrosterduty(payload: OnCallRosterDutyCreateSchema):
    """Create new OnCallRosterDuty instance in enterprise repository."""
    svc = OnCallRosterDutyService()
    try:
        item = svc.create_oncallrosterduty(
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

@router.put("/oncallrosterdutys/{item_id}", response_model=Dict[str, Any])
def update_oncallrosterduty(item_id: int, payload: OnCallRosterDutyUpdateSchema):
    """Update existing OnCallRosterDuty record fields."""
    svc = OnCallRosterDutyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_oncallrosterduty(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OnCallRosterDuty with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/oncallrosterdutys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_oncallrosterduty(item_id: int, hard: bool = Query(False)):
    """Delete OnCallRosterDuty record (soft-delete by default)."""
    svc = OnCallRosterDutyService()
    ok = svc.delete_oncallrosterduty(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OnCallRosterDuty with ID {item_id} not found")
    return None

@router.get("/oncallrosterdutys/analytics/metrics", response_model=Dict[str, Any])
def get_oncallrosterduty_metrics():
    """Calculate summary statistical KPIs for OnCallRosterDuty collection."""
    svc = OnCallRosterDutyService()
    return svc.calculate_aggregate_metrics()

# ==================== GeofenceClockInZone Endpoints ====================
@router.get("/geofenceclockinzones", response_model=List[Dict[str, Any]])
def list_geofenceclockinzones(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GeofenceClockInZone records with pagination and filtering."""
    svc = GeofenceClockInZoneService()
    items = svc.list_geofenceclockinzones(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/geofenceclockinzones/{item_id}", response_model=Dict[str, Any])
def get_geofenceclockinzone_by_id(item_id: int):
    """Retrieve detailed record for GeofenceClockInZone by ID."""
    svc = GeofenceClockInZoneService()
    item = svc.get_geofenceclockinzone_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GeofenceClockInZone with ID {item_id} not found")
    return item.to_dict()

@router.post("/geofenceclockinzones", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_geofenceclockinzone(payload: GeofenceClockInZoneCreateSchema):
    """Create new GeofenceClockInZone instance in enterprise repository."""
    svc = GeofenceClockInZoneService()
    try:
        item = svc.create_geofenceclockinzone(
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

@router.put("/geofenceclockinzones/{item_id}", response_model=Dict[str, Any])
def update_geofenceclockinzone(item_id: int, payload: GeofenceClockInZoneUpdateSchema):
    """Update existing GeofenceClockInZone record fields."""
    svc = GeofenceClockInZoneService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_geofenceclockinzone(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GeofenceClockInZone with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/geofenceclockinzones/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_geofenceclockinzone(item_id: int, hard: bool = Query(False)):
    """Delete GeofenceClockInZone record (soft-delete by default)."""
    svc = GeofenceClockInZoneService()
    ok = svc.delete_geofenceclockinzone(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GeofenceClockInZone with ID {item_id} not found")
    return None

@router.get("/geofenceclockinzones/analytics/metrics", response_model=Dict[str, Any])
def get_geofenceclockinzone_metrics():
    """Calculate summary statistical KPIs for GeofenceClockInZone collection."""
    svc = GeofenceClockInZoneService()
    return svc.calculate_aggregate_metrics()

# ==================== StatutoryWorkingHours Endpoints ====================
@router.get("/statutoryworkinghourss", response_model=List[Dict[str, Any]])
def list_statutoryworkinghourss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StatutoryWorkingHours records with pagination and filtering."""
    svc = StatutoryWorkingHoursService()
    items = svc.list_statutoryworkinghourss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/statutoryworkinghourss/{item_id}", response_model=Dict[str, Any])
def get_statutoryworkinghours_by_id(item_id: int):
    """Retrieve detailed record for StatutoryWorkingHours by ID."""
    svc = StatutoryWorkingHoursService()
    item = svc.get_statutoryworkinghours_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StatutoryWorkingHours with ID {item_id} not found")
    return item.to_dict()

@router.post("/statutoryworkinghourss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_statutoryworkinghours(payload: StatutoryWorkingHoursCreateSchema):
    """Create new StatutoryWorkingHours instance in enterprise repository."""
    svc = StatutoryWorkingHoursService()
    try:
        item = svc.create_statutoryworkinghours(
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

@router.put("/statutoryworkinghourss/{item_id}", response_model=Dict[str, Any])
def update_statutoryworkinghours(item_id: int, payload: StatutoryWorkingHoursUpdateSchema):
    """Update existing StatutoryWorkingHours record fields."""
    svc = StatutoryWorkingHoursService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_statutoryworkinghours(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StatutoryWorkingHours with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/statutoryworkinghourss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_statutoryworkinghours(item_id: int, hard: bool = Query(False)):
    """Delete StatutoryWorkingHours record (soft-delete by default)."""
    svc = StatutoryWorkingHoursService()
    ok = svc.delete_statutoryworkinghours(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StatutoryWorkingHours with ID {item_id} not found")
    return None

@router.get("/statutoryworkinghourss/analytics/metrics", response_model=Dict[str, Any])
def get_statutoryworkinghours_metrics():
    """Calculate summary statistical KPIs for StatutoryWorkingHours collection."""
    svc = StatutoryWorkingHoursService()
    return svc.calculate_aggregate_metrics()

# ==================== ShiftAllowanceCredit Endpoints ====================
@router.get("/shiftallowancecredits", response_model=List[Dict[str, Any]])
def list_shiftallowancecredits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShiftAllowanceCredit records with pagination and filtering."""
    svc = ShiftAllowanceCreditService()
    items = svc.list_shiftallowancecredits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shiftallowancecredits/{item_id}", response_model=Dict[str, Any])
def get_shiftallowancecredit_by_id(item_id: int):
    """Retrieve detailed record for ShiftAllowanceCredit by ID."""
    svc = ShiftAllowanceCreditService()
    item = svc.get_shiftallowancecredit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShiftAllowanceCredit with ID {item_id} not found")
    return item.to_dict()

@router.post("/shiftallowancecredits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shiftallowancecredit(payload: ShiftAllowanceCreditCreateSchema):
    """Create new ShiftAllowanceCredit instance in enterprise repository."""
    svc = ShiftAllowanceCreditService()
    try:
        item = svc.create_shiftallowancecredit(
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

@router.put("/shiftallowancecredits/{item_id}", response_model=Dict[str, Any])
def update_shiftallowancecredit(item_id: int, payload: ShiftAllowanceCreditUpdateSchema):
    """Update existing ShiftAllowanceCredit record fields."""
    svc = ShiftAllowanceCreditService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shiftallowancecredit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShiftAllowanceCredit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shiftallowancecredits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shiftallowancecredit(item_id: int, hard: bool = Query(False)):
    """Delete ShiftAllowanceCredit record (soft-delete by default)."""
    svc = ShiftAllowanceCreditService()
    ok = svc.delete_shiftallowancecredit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShiftAllowanceCredit with ID {item_id} not found")
    return None

@router.get("/shiftallowancecredits/analytics/metrics", response_model=Dict[str, Any])
def get_shiftallowancecredit_metrics():
    """Calculate summary statistical KPIs for ShiftAllowanceCredit collection."""
    svc = ShiftAllowanceCreditService()
    return svc.calculate_aggregate_metrics()

# ==================== TimecardSignoff Endpoints ====================
@router.get("/timecardsignoffs", response_model=List[Dict[str, Any]])
def list_timecardsignoffs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TimecardSignoff records with pagination and filtering."""
    svc = TimecardSignoffService()
    items = svc.list_timecardsignoffs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/timecardsignoffs/{item_id}", response_model=Dict[str, Any])
def get_timecardsignoff_by_id(item_id: int):
    """Retrieve detailed record for TimecardSignoff by ID."""
    svc = TimecardSignoffService()
    item = svc.get_timecardsignoff_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TimecardSignoff with ID {item_id} not found")
    return item.to_dict()

@router.post("/timecardsignoffs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_timecardsignoff(payload: TimecardSignoffCreateSchema):
    """Create new TimecardSignoff instance in enterprise repository."""
    svc = TimecardSignoffService()
    try:
        item = svc.create_timecardsignoff(
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

@router.put("/timecardsignoffs/{item_id}", response_model=Dict[str, Any])
def update_timecardsignoff(item_id: int, payload: TimecardSignoffUpdateSchema):
    """Update existing TimecardSignoff record fields."""
    svc = TimecardSignoffService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_timecardsignoff(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TimecardSignoff with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/timecardsignoffs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_timecardsignoff(item_id: int, hard: bool = Query(False)):
    """Delete TimecardSignoff record (soft-delete by default)."""
    svc = TimecardSignoffService()
    ok = svc.delete_timecardsignoff(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TimecardSignoff with ID {item_id} not found")
    return None

@router.get("/timecardsignoffs/analytics/metrics", response_model=Dict[str, Any])
def get_timecardsignoff_metrics():
    """Calculate summary statistical KPIs for TimecardSignoff collection."""
    svc = TimecardSignoffService()
    return svc.calculate_aggregate_metrics()

