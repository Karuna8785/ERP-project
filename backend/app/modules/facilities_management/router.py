"""
Facilities & Corporate Real Estate - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    FacilityBuildingService,
    OfficeFloorWingService,
    RoomDeskAllocationService,
    HVACControlScheduleService,
    PhysicalBadgeAccessLogService,
    SecurityVisitorPassService,
    JanitorialTaskLogService,
    LeaseSpaceContractService,
    EmergencyEvacuationPlanService,
    UtilityMeterRecordService,
    ParkingSlotAllocationService,
    AssetTagLocationService,
    IncidentHazardNoticeService,
    MailroomPackageLogService,
    CateringRequestOrderService,
    FacilityExpenseChargeService,
)
from .schemas import (
    FacilityBuildingCreateSchema, FacilityBuildingUpdateSchema, FacilityBuildingResponseSchema,
    OfficeFloorWingCreateSchema, OfficeFloorWingUpdateSchema, OfficeFloorWingResponseSchema,
    RoomDeskAllocationCreateSchema, RoomDeskAllocationUpdateSchema, RoomDeskAllocationResponseSchema,
    HVACControlScheduleCreateSchema, HVACControlScheduleUpdateSchema, HVACControlScheduleResponseSchema,
    PhysicalBadgeAccessLogCreateSchema, PhysicalBadgeAccessLogUpdateSchema, PhysicalBadgeAccessLogResponseSchema,
    SecurityVisitorPassCreateSchema, SecurityVisitorPassUpdateSchema, SecurityVisitorPassResponseSchema,
    JanitorialTaskLogCreateSchema, JanitorialTaskLogUpdateSchema, JanitorialTaskLogResponseSchema,
    LeaseSpaceContractCreateSchema, LeaseSpaceContractUpdateSchema, LeaseSpaceContractResponseSchema,
    EmergencyEvacuationPlanCreateSchema, EmergencyEvacuationPlanUpdateSchema, EmergencyEvacuationPlanResponseSchema,
    UtilityMeterRecordCreateSchema, UtilityMeterRecordUpdateSchema, UtilityMeterRecordResponseSchema,
    ParkingSlotAllocationCreateSchema, ParkingSlotAllocationUpdateSchema, ParkingSlotAllocationResponseSchema,
    AssetTagLocationCreateSchema, AssetTagLocationUpdateSchema, AssetTagLocationResponseSchema,
    IncidentHazardNoticeCreateSchema, IncidentHazardNoticeUpdateSchema, IncidentHazardNoticeResponseSchema,
    MailroomPackageLogCreateSchema, MailroomPackageLogUpdateSchema, MailroomPackageLogResponseSchema,
    CateringRequestOrderCreateSchema, CateringRequestOrderUpdateSchema, CateringRequestOrderResponseSchema,
    FacilityExpenseChargeCreateSchema, FacilityExpenseChargeUpdateSchema, FacilityExpenseChargeResponseSchema,
)

router = APIRouter(prefix="/facilities_management", tags=["Facilities & Corporate Real Estate"])

# ==================== FacilityBuilding Endpoints ====================
@router.get("/facilitybuildings", response_model=List[Dict[str, Any]])
def list_facilitybuildings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FacilityBuilding records with pagination and filtering."""
    svc = FacilityBuildingService()
    items = svc.list_facilitybuildings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/facilitybuildings/{item_id}", response_model=Dict[str, Any])
def get_facilitybuilding_by_id(item_id: int):
    """Retrieve detailed record for FacilityBuilding by ID."""
    svc = FacilityBuildingService()
    item = svc.get_facilitybuilding_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FacilityBuilding with ID {item_id} not found")
    return item.to_dict()

@router.post("/facilitybuildings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_facilitybuilding(payload: FacilityBuildingCreateSchema):
    """Create new FacilityBuilding instance in enterprise repository."""
    svc = FacilityBuildingService()
    try:
        item = svc.create_facilitybuilding(
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

@router.put("/facilitybuildings/{item_id}", response_model=Dict[str, Any])
def update_facilitybuilding(item_id: int, payload: FacilityBuildingUpdateSchema):
    """Update existing FacilityBuilding record fields."""
    svc = FacilityBuildingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_facilitybuilding(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FacilityBuilding with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/facilitybuildings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_facilitybuilding(item_id: int, hard: bool = Query(False)):
    """Delete FacilityBuilding record (soft-delete by default)."""
    svc = FacilityBuildingService()
    ok = svc.delete_facilitybuilding(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FacilityBuilding with ID {item_id} not found")
    return None

@router.get("/facilitybuildings/analytics/metrics", response_model=Dict[str, Any])
def get_facilitybuilding_metrics():
    """Calculate summary statistical KPIs for FacilityBuilding collection."""
    svc = FacilityBuildingService()
    return svc.calculate_aggregate_metrics()

# ==================== OfficeFloorWing Endpoints ====================
@router.get("/officefloorwings", response_model=List[Dict[str, Any]])
def list_officefloorwings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OfficeFloorWing records with pagination and filtering."""
    svc = OfficeFloorWingService()
    items = svc.list_officefloorwings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/officefloorwings/{item_id}", response_model=Dict[str, Any])
def get_officefloorwing_by_id(item_id: int):
    """Retrieve detailed record for OfficeFloorWing by ID."""
    svc = OfficeFloorWingService()
    item = svc.get_officefloorwing_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OfficeFloorWing with ID {item_id} not found")
    return item.to_dict()

@router.post("/officefloorwings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_officefloorwing(payload: OfficeFloorWingCreateSchema):
    """Create new OfficeFloorWing instance in enterprise repository."""
    svc = OfficeFloorWingService()
    try:
        item = svc.create_officefloorwing(
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

@router.put("/officefloorwings/{item_id}", response_model=Dict[str, Any])
def update_officefloorwing(item_id: int, payload: OfficeFloorWingUpdateSchema):
    """Update existing OfficeFloorWing record fields."""
    svc = OfficeFloorWingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_officefloorwing(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OfficeFloorWing with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/officefloorwings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_officefloorwing(item_id: int, hard: bool = Query(False)):
    """Delete OfficeFloorWing record (soft-delete by default)."""
    svc = OfficeFloorWingService()
    ok = svc.delete_officefloorwing(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OfficeFloorWing with ID {item_id} not found")
    return None

@router.get("/officefloorwings/analytics/metrics", response_model=Dict[str, Any])
def get_officefloorwing_metrics():
    """Calculate summary statistical KPIs for OfficeFloorWing collection."""
    svc = OfficeFloorWingService()
    return svc.calculate_aggregate_metrics()

# ==================== RoomDeskAllocation Endpoints ====================
@router.get("/roomdeskallocations", response_model=List[Dict[str, Any]])
def list_roomdeskallocations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RoomDeskAllocation records with pagination and filtering."""
    svc = RoomDeskAllocationService()
    items = svc.list_roomdeskallocations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/roomdeskallocations/{item_id}", response_model=Dict[str, Any])
def get_roomdeskallocation_by_id(item_id: int):
    """Retrieve detailed record for RoomDeskAllocation by ID."""
    svc = RoomDeskAllocationService()
    item = svc.get_roomdeskallocation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RoomDeskAllocation with ID {item_id} not found")
    return item.to_dict()

@router.post("/roomdeskallocations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_roomdeskallocation(payload: RoomDeskAllocationCreateSchema):
    """Create new RoomDeskAllocation instance in enterprise repository."""
    svc = RoomDeskAllocationService()
    try:
        item = svc.create_roomdeskallocation(
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

@router.put("/roomdeskallocations/{item_id}", response_model=Dict[str, Any])
def update_roomdeskallocation(item_id: int, payload: RoomDeskAllocationUpdateSchema):
    """Update existing RoomDeskAllocation record fields."""
    svc = RoomDeskAllocationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_roomdeskallocation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RoomDeskAllocation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/roomdeskallocations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_roomdeskallocation(item_id: int, hard: bool = Query(False)):
    """Delete RoomDeskAllocation record (soft-delete by default)."""
    svc = RoomDeskAllocationService()
    ok = svc.delete_roomdeskallocation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RoomDeskAllocation with ID {item_id} not found")
    return None

@router.get("/roomdeskallocations/analytics/metrics", response_model=Dict[str, Any])
def get_roomdeskallocation_metrics():
    """Calculate summary statistical KPIs for RoomDeskAllocation collection."""
    svc = RoomDeskAllocationService()
    return svc.calculate_aggregate_metrics()

# ==================== HVACControlSchedule Endpoints ====================
@router.get("/hvaccontrolschedules", response_model=List[Dict[str, Any]])
def list_hvaccontrolschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HVACControlSchedule records with pagination and filtering."""
    svc = HVACControlScheduleService()
    items = svc.list_hvaccontrolschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hvaccontrolschedules/{item_id}", response_model=Dict[str, Any])
def get_hvaccontrolschedule_by_id(item_id: int):
    """Retrieve detailed record for HVACControlSchedule by ID."""
    svc = HVACControlScheduleService()
    item = svc.get_hvaccontrolschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HVACControlSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/hvaccontrolschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hvaccontrolschedule(payload: HVACControlScheduleCreateSchema):
    """Create new HVACControlSchedule instance in enterprise repository."""
    svc = HVACControlScheduleService()
    try:
        item = svc.create_hvaccontrolschedule(
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

@router.put("/hvaccontrolschedules/{item_id}", response_model=Dict[str, Any])
def update_hvaccontrolschedule(item_id: int, payload: HVACControlScheduleUpdateSchema):
    """Update existing HVACControlSchedule record fields."""
    svc = HVACControlScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hvaccontrolschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HVACControlSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hvaccontrolschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hvaccontrolschedule(item_id: int, hard: bool = Query(False)):
    """Delete HVACControlSchedule record (soft-delete by default)."""
    svc = HVACControlScheduleService()
    ok = svc.delete_hvaccontrolschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HVACControlSchedule with ID {item_id} not found")
    return None

@router.get("/hvaccontrolschedules/analytics/metrics", response_model=Dict[str, Any])
def get_hvaccontrolschedule_metrics():
    """Calculate summary statistical KPIs for HVACControlSchedule collection."""
    svc = HVACControlScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== PhysicalBadgeAccessLog Endpoints ====================
@router.get("/physicalbadgeaccesslogs", response_model=List[Dict[str, Any]])
def list_physicalbadgeaccesslogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PhysicalBadgeAccessLog records with pagination and filtering."""
    svc = PhysicalBadgeAccessLogService()
    items = svc.list_physicalbadgeaccesslogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/physicalbadgeaccesslogs/{item_id}", response_model=Dict[str, Any])
def get_physicalbadgeaccesslog_by_id(item_id: int):
    """Retrieve detailed record for PhysicalBadgeAccessLog by ID."""
    svc = PhysicalBadgeAccessLogService()
    item = svc.get_physicalbadgeaccesslog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PhysicalBadgeAccessLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/physicalbadgeaccesslogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_physicalbadgeaccesslog(payload: PhysicalBadgeAccessLogCreateSchema):
    """Create new PhysicalBadgeAccessLog instance in enterprise repository."""
    svc = PhysicalBadgeAccessLogService()
    try:
        item = svc.create_physicalbadgeaccesslog(
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

@router.put("/physicalbadgeaccesslogs/{item_id}", response_model=Dict[str, Any])
def update_physicalbadgeaccesslog(item_id: int, payload: PhysicalBadgeAccessLogUpdateSchema):
    """Update existing PhysicalBadgeAccessLog record fields."""
    svc = PhysicalBadgeAccessLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_physicalbadgeaccesslog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PhysicalBadgeAccessLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/physicalbadgeaccesslogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_physicalbadgeaccesslog(item_id: int, hard: bool = Query(False)):
    """Delete PhysicalBadgeAccessLog record (soft-delete by default)."""
    svc = PhysicalBadgeAccessLogService()
    ok = svc.delete_physicalbadgeaccesslog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PhysicalBadgeAccessLog with ID {item_id} not found")
    return None

@router.get("/physicalbadgeaccesslogs/analytics/metrics", response_model=Dict[str, Any])
def get_physicalbadgeaccesslog_metrics():
    """Calculate summary statistical KPIs for PhysicalBadgeAccessLog collection."""
    svc = PhysicalBadgeAccessLogService()
    return svc.calculate_aggregate_metrics()

# ==================== SecurityVisitorPass Endpoints ====================
@router.get("/securityvisitorpasss", response_model=List[Dict[str, Any]])
def list_securityvisitorpasss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SecurityVisitorPass records with pagination and filtering."""
    svc = SecurityVisitorPassService()
    items = svc.list_securityvisitorpasss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/securityvisitorpasss/{item_id}", response_model=Dict[str, Any])
def get_securityvisitorpass_by_id(item_id: int):
    """Retrieve detailed record for SecurityVisitorPass by ID."""
    svc = SecurityVisitorPassService()
    item = svc.get_securityvisitorpass_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SecurityVisitorPass with ID {item_id} not found")
    return item.to_dict()

@router.post("/securityvisitorpasss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_securityvisitorpass(payload: SecurityVisitorPassCreateSchema):
    """Create new SecurityVisitorPass instance in enterprise repository."""
    svc = SecurityVisitorPassService()
    try:
        item = svc.create_securityvisitorpass(
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

@router.put("/securityvisitorpasss/{item_id}", response_model=Dict[str, Any])
def update_securityvisitorpass(item_id: int, payload: SecurityVisitorPassUpdateSchema):
    """Update existing SecurityVisitorPass record fields."""
    svc = SecurityVisitorPassService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_securityvisitorpass(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SecurityVisitorPass with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/securityvisitorpasss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_securityvisitorpass(item_id: int, hard: bool = Query(False)):
    """Delete SecurityVisitorPass record (soft-delete by default)."""
    svc = SecurityVisitorPassService()
    ok = svc.delete_securityvisitorpass(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SecurityVisitorPass with ID {item_id} not found")
    return None

@router.get("/securityvisitorpasss/analytics/metrics", response_model=Dict[str, Any])
def get_securityvisitorpass_metrics():
    """Calculate summary statistical KPIs for SecurityVisitorPass collection."""
    svc = SecurityVisitorPassService()
    return svc.calculate_aggregate_metrics()

# ==================== JanitorialTaskLog Endpoints ====================
@router.get("/janitorialtasklogs", response_model=List[Dict[str, Any]])
def list_janitorialtasklogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List JanitorialTaskLog records with pagination and filtering."""
    svc = JanitorialTaskLogService()
    items = svc.list_janitorialtasklogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/janitorialtasklogs/{item_id}", response_model=Dict[str, Any])
def get_janitorialtasklog_by_id(item_id: int):
    """Retrieve detailed record for JanitorialTaskLog by ID."""
    svc = JanitorialTaskLogService()
    item = svc.get_janitorialtasklog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"JanitorialTaskLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/janitorialtasklogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_janitorialtasklog(payload: JanitorialTaskLogCreateSchema):
    """Create new JanitorialTaskLog instance in enterprise repository."""
    svc = JanitorialTaskLogService()
    try:
        item = svc.create_janitorialtasklog(
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

@router.put("/janitorialtasklogs/{item_id}", response_model=Dict[str, Any])
def update_janitorialtasklog(item_id: int, payload: JanitorialTaskLogUpdateSchema):
    """Update existing JanitorialTaskLog record fields."""
    svc = JanitorialTaskLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_janitorialtasklog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"JanitorialTaskLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/janitorialtasklogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_janitorialtasklog(item_id: int, hard: bool = Query(False)):
    """Delete JanitorialTaskLog record (soft-delete by default)."""
    svc = JanitorialTaskLogService()
    ok = svc.delete_janitorialtasklog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"JanitorialTaskLog with ID {item_id} not found")
    return None

@router.get("/janitorialtasklogs/analytics/metrics", response_model=Dict[str, Any])
def get_janitorialtasklog_metrics():
    """Calculate summary statistical KPIs for JanitorialTaskLog collection."""
    svc = JanitorialTaskLogService()
    return svc.calculate_aggregate_metrics()

# ==================== LeaseSpaceContract Endpoints ====================
@router.get("/leasespacecontracts", response_model=List[Dict[str, Any]])
def list_leasespacecontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeaseSpaceContract records with pagination and filtering."""
    svc = LeaseSpaceContractService()
    items = svc.list_leasespacecontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leasespacecontracts/{item_id}", response_model=Dict[str, Any])
def get_leasespacecontract_by_id(item_id: int):
    """Retrieve detailed record for LeaseSpaceContract by ID."""
    svc = LeaseSpaceContractService()
    item = svc.get_leasespacecontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeaseSpaceContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/leasespacecontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leasespacecontract(payload: LeaseSpaceContractCreateSchema):
    """Create new LeaseSpaceContract instance in enterprise repository."""
    svc = LeaseSpaceContractService()
    try:
        item = svc.create_leasespacecontract(
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

@router.put("/leasespacecontracts/{item_id}", response_model=Dict[str, Any])
def update_leasespacecontract(item_id: int, payload: LeaseSpaceContractUpdateSchema):
    """Update existing LeaseSpaceContract record fields."""
    svc = LeaseSpaceContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leasespacecontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeaseSpaceContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leasespacecontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leasespacecontract(item_id: int, hard: bool = Query(False)):
    """Delete LeaseSpaceContract record (soft-delete by default)."""
    svc = LeaseSpaceContractService()
    ok = svc.delete_leasespacecontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeaseSpaceContract with ID {item_id} not found")
    return None

@router.get("/leasespacecontracts/analytics/metrics", response_model=Dict[str, Any])
def get_leasespacecontract_metrics():
    """Calculate summary statistical KPIs for LeaseSpaceContract collection."""
    svc = LeaseSpaceContractService()
    return svc.calculate_aggregate_metrics()

# ==================== EmergencyEvacuationPlan Endpoints ====================
@router.get("/emergencyevacuationplans", response_model=List[Dict[str, Any]])
def list_emergencyevacuationplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmergencyEvacuationPlan records with pagination and filtering."""
    svc = EmergencyEvacuationPlanService()
    items = svc.list_emergencyevacuationplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/emergencyevacuationplans/{item_id}", response_model=Dict[str, Any])
def get_emergencyevacuationplan_by_id(item_id: int):
    """Retrieve detailed record for EmergencyEvacuationPlan by ID."""
    svc = EmergencyEvacuationPlanService()
    item = svc.get_emergencyevacuationplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmergencyEvacuationPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/emergencyevacuationplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_emergencyevacuationplan(payload: EmergencyEvacuationPlanCreateSchema):
    """Create new EmergencyEvacuationPlan instance in enterprise repository."""
    svc = EmergencyEvacuationPlanService()
    try:
        item = svc.create_emergencyevacuationplan(
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

@router.put("/emergencyevacuationplans/{item_id}", response_model=Dict[str, Any])
def update_emergencyevacuationplan(item_id: int, payload: EmergencyEvacuationPlanUpdateSchema):
    """Update existing EmergencyEvacuationPlan record fields."""
    svc = EmergencyEvacuationPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_emergencyevacuationplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmergencyEvacuationPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/emergencyevacuationplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_emergencyevacuationplan(item_id: int, hard: bool = Query(False)):
    """Delete EmergencyEvacuationPlan record (soft-delete by default)."""
    svc = EmergencyEvacuationPlanService()
    ok = svc.delete_emergencyevacuationplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmergencyEvacuationPlan with ID {item_id} not found")
    return None

@router.get("/emergencyevacuationplans/analytics/metrics", response_model=Dict[str, Any])
def get_emergencyevacuationplan_metrics():
    """Calculate summary statistical KPIs for EmergencyEvacuationPlan collection."""
    svc = EmergencyEvacuationPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== UtilityMeterRecord Endpoints ====================
@router.get("/utilitymeterrecords", response_model=List[Dict[str, Any]])
def list_utilitymeterrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UtilityMeterRecord records with pagination and filtering."""
    svc = UtilityMeterRecordService()
    items = svc.list_utilitymeterrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/utilitymeterrecords/{item_id}", response_model=Dict[str, Any])
def get_utilitymeterrecord_by_id(item_id: int):
    """Retrieve detailed record for UtilityMeterRecord by ID."""
    svc = UtilityMeterRecordService()
    item = svc.get_utilitymeterrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UtilityMeterRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/utilitymeterrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_utilitymeterrecord(payload: UtilityMeterRecordCreateSchema):
    """Create new UtilityMeterRecord instance in enterprise repository."""
    svc = UtilityMeterRecordService()
    try:
        item = svc.create_utilitymeterrecord(
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

@router.put("/utilitymeterrecords/{item_id}", response_model=Dict[str, Any])
def update_utilitymeterrecord(item_id: int, payload: UtilityMeterRecordUpdateSchema):
    """Update existing UtilityMeterRecord record fields."""
    svc = UtilityMeterRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_utilitymeterrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UtilityMeterRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/utilitymeterrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_utilitymeterrecord(item_id: int, hard: bool = Query(False)):
    """Delete UtilityMeterRecord record (soft-delete by default)."""
    svc = UtilityMeterRecordService()
    ok = svc.delete_utilitymeterrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UtilityMeterRecord with ID {item_id} not found")
    return None

@router.get("/utilitymeterrecords/analytics/metrics", response_model=Dict[str, Any])
def get_utilitymeterrecord_metrics():
    """Calculate summary statistical KPIs for UtilityMeterRecord collection."""
    svc = UtilityMeterRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== ParkingSlotAllocation Endpoints ====================
@router.get("/parkingslotallocations", response_model=List[Dict[str, Any]])
def list_parkingslotallocations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ParkingSlotAllocation records with pagination and filtering."""
    svc = ParkingSlotAllocationService()
    items = svc.list_parkingslotallocations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/parkingslotallocations/{item_id}", response_model=Dict[str, Any])
def get_parkingslotallocation_by_id(item_id: int):
    """Retrieve detailed record for ParkingSlotAllocation by ID."""
    svc = ParkingSlotAllocationService()
    item = svc.get_parkingslotallocation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ParkingSlotAllocation with ID {item_id} not found")
    return item.to_dict()

@router.post("/parkingslotallocations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_parkingslotallocation(payload: ParkingSlotAllocationCreateSchema):
    """Create new ParkingSlotAllocation instance in enterprise repository."""
    svc = ParkingSlotAllocationService()
    try:
        item = svc.create_parkingslotallocation(
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

@router.put("/parkingslotallocations/{item_id}", response_model=Dict[str, Any])
def update_parkingslotallocation(item_id: int, payload: ParkingSlotAllocationUpdateSchema):
    """Update existing ParkingSlotAllocation record fields."""
    svc = ParkingSlotAllocationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_parkingslotallocation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ParkingSlotAllocation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/parkingslotallocations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_parkingslotallocation(item_id: int, hard: bool = Query(False)):
    """Delete ParkingSlotAllocation record (soft-delete by default)."""
    svc = ParkingSlotAllocationService()
    ok = svc.delete_parkingslotallocation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ParkingSlotAllocation with ID {item_id} not found")
    return None

@router.get("/parkingslotallocations/analytics/metrics", response_model=Dict[str, Any])
def get_parkingslotallocation_metrics():
    """Calculate summary statistical KPIs for ParkingSlotAllocation collection."""
    svc = ParkingSlotAllocationService()
    return svc.calculate_aggregate_metrics()

# ==================== AssetTagLocation Endpoints ====================
@router.get("/assettaglocations", response_model=List[Dict[str, Any]])
def list_assettaglocations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetTagLocation records with pagination and filtering."""
    svc = AssetTagLocationService()
    items = svc.list_assettaglocations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assettaglocations/{item_id}", response_model=Dict[str, Any])
def get_assettaglocation_by_id(item_id: int):
    """Retrieve detailed record for AssetTagLocation by ID."""
    svc = AssetTagLocationService()
    item = svc.get_assettaglocation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetTagLocation with ID {item_id} not found")
    return item.to_dict()

@router.post("/assettaglocations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assettaglocation(payload: AssetTagLocationCreateSchema):
    """Create new AssetTagLocation instance in enterprise repository."""
    svc = AssetTagLocationService()
    try:
        item = svc.create_assettaglocation(
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

@router.put("/assettaglocations/{item_id}", response_model=Dict[str, Any])
def update_assettaglocation(item_id: int, payload: AssetTagLocationUpdateSchema):
    """Update existing AssetTagLocation record fields."""
    svc = AssetTagLocationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assettaglocation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetTagLocation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assettaglocations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assettaglocation(item_id: int, hard: bool = Query(False)):
    """Delete AssetTagLocation record (soft-delete by default)."""
    svc = AssetTagLocationService()
    ok = svc.delete_assettaglocation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetTagLocation with ID {item_id} not found")
    return None

@router.get("/assettaglocations/analytics/metrics", response_model=Dict[str, Any])
def get_assettaglocation_metrics():
    """Calculate summary statistical KPIs for AssetTagLocation collection."""
    svc = AssetTagLocationService()
    return svc.calculate_aggregate_metrics()

# ==================== IncidentHazardNotice Endpoints ====================
@router.get("/incidenthazardnotices", response_model=List[Dict[str, Any]])
def list_incidenthazardnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IncidentHazardNotice records with pagination and filtering."""
    svc = IncidentHazardNoticeService()
    items = svc.list_incidenthazardnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/incidenthazardnotices/{item_id}", response_model=Dict[str, Any])
def get_incidenthazardnotice_by_id(item_id: int):
    """Retrieve detailed record for IncidentHazardNotice by ID."""
    svc = IncidentHazardNoticeService()
    item = svc.get_incidenthazardnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IncidentHazardNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/incidenthazardnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_incidenthazardnotice(payload: IncidentHazardNoticeCreateSchema):
    """Create new IncidentHazardNotice instance in enterprise repository."""
    svc = IncidentHazardNoticeService()
    try:
        item = svc.create_incidenthazardnotice(
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

@router.put("/incidenthazardnotices/{item_id}", response_model=Dict[str, Any])
def update_incidenthazardnotice(item_id: int, payload: IncidentHazardNoticeUpdateSchema):
    """Update existing IncidentHazardNotice record fields."""
    svc = IncidentHazardNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_incidenthazardnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IncidentHazardNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/incidenthazardnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incidenthazardnotice(item_id: int, hard: bool = Query(False)):
    """Delete IncidentHazardNotice record (soft-delete by default)."""
    svc = IncidentHazardNoticeService()
    ok = svc.delete_incidenthazardnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IncidentHazardNotice with ID {item_id} not found")
    return None

@router.get("/incidenthazardnotices/analytics/metrics", response_model=Dict[str, Any])
def get_incidenthazardnotice_metrics():
    """Calculate summary statistical KPIs for IncidentHazardNotice collection."""
    svc = IncidentHazardNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== MailroomPackageLog Endpoints ====================
@router.get("/mailroompackagelogs", response_model=List[Dict[str, Any]])
def list_mailroompackagelogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MailroomPackageLog records with pagination and filtering."""
    svc = MailroomPackageLogService()
    items = svc.list_mailroompackagelogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/mailroompackagelogs/{item_id}", response_model=Dict[str, Any])
def get_mailroompackagelog_by_id(item_id: int):
    """Retrieve detailed record for MailroomPackageLog by ID."""
    svc = MailroomPackageLogService()
    item = svc.get_mailroompackagelog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MailroomPackageLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/mailroompackagelogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_mailroompackagelog(payload: MailroomPackageLogCreateSchema):
    """Create new MailroomPackageLog instance in enterprise repository."""
    svc = MailroomPackageLogService()
    try:
        item = svc.create_mailroompackagelog(
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

@router.put("/mailroompackagelogs/{item_id}", response_model=Dict[str, Any])
def update_mailroompackagelog(item_id: int, payload: MailroomPackageLogUpdateSchema):
    """Update existing MailroomPackageLog record fields."""
    svc = MailroomPackageLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_mailroompackagelog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MailroomPackageLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/mailroompackagelogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mailroompackagelog(item_id: int, hard: bool = Query(False)):
    """Delete MailroomPackageLog record (soft-delete by default)."""
    svc = MailroomPackageLogService()
    ok = svc.delete_mailroompackagelog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MailroomPackageLog with ID {item_id} not found")
    return None

@router.get("/mailroompackagelogs/analytics/metrics", response_model=Dict[str, Any])
def get_mailroompackagelog_metrics():
    """Calculate summary statistical KPIs for MailroomPackageLog collection."""
    svc = MailroomPackageLogService()
    return svc.calculate_aggregate_metrics()

# ==================== CateringRequestOrder Endpoints ====================
@router.get("/cateringrequestorders", response_model=List[Dict[str, Any]])
def list_cateringrequestorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CateringRequestOrder records with pagination and filtering."""
    svc = CateringRequestOrderService()
    items = svc.list_cateringrequestorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cateringrequestorders/{item_id}", response_model=Dict[str, Any])
def get_cateringrequestorder_by_id(item_id: int):
    """Retrieve detailed record for CateringRequestOrder by ID."""
    svc = CateringRequestOrderService()
    item = svc.get_cateringrequestorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CateringRequestOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/cateringrequestorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cateringrequestorder(payload: CateringRequestOrderCreateSchema):
    """Create new CateringRequestOrder instance in enterprise repository."""
    svc = CateringRequestOrderService()
    try:
        item = svc.create_cateringrequestorder(
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

@router.put("/cateringrequestorders/{item_id}", response_model=Dict[str, Any])
def update_cateringrequestorder(item_id: int, payload: CateringRequestOrderUpdateSchema):
    """Update existing CateringRequestOrder record fields."""
    svc = CateringRequestOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cateringrequestorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CateringRequestOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cateringrequestorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cateringrequestorder(item_id: int, hard: bool = Query(False)):
    """Delete CateringRequestOrder record (soft-delete by default)."""
    svc = CateringRequestOrderService()
    ok = svc.delete_cateringrequestorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CateringRequestOrder with ID {item_id} not found")
    return None

@router.get("/cateringrequestorders/analytics/metrics", response_model=Dict[str, Any])
def get_cateringrequestorder_metrics():
    """Calculate summary statistical KPIs for CateringRequestOrder collection."""
    svc = CateringRequestOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== FacilityExpenseCharge Endpoints ====================
@router.get("/facilityexpensecharges", response_model=List[Dict[str, Any]])
def list_facilityexpensecharges(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FacilityExpenseCharge records with pagination and filtering."""
    svc = FacilityExpenseChargeService()
    items = svc.list_facilityexpensecharges(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/facilityexpensecharges/{item_id}", response_model=Dict[str, Any])
def get_facilityexpensecharge_by_id(item_id: int):
    """Retrieve detailed record for FacilityExpenseCharge by ID."""
    svc = FacilityExpenseChargeService()
    item = svc.get_facilityexpensecharge_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FacilityExpenseCharge with ID {item_id} not found")
    return item.to_dict()

@router.post("/facilityexpensecharges", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_facilityexpensecharge(payload: FacilityExpenseChargeCreateSchema):
    """Create new FacilityExpenseCharge instance in enterprise repository."""
    svc = FacilityExpenseChargeService()
    try:
        item = svc.create_facilityexpensecharge(
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

@router.put("/facilityexpensecharges/{item_id}", response_model=Dict[str, Any])
def update_facilityexpensecharge(item_id: int, payload: FacilityExpenseChargeUpdateSchema):
    """Update existing FacilityExpenseCharge record fields."""
    svc = FacilityExpenseChargeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_facilityexpensecharge(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FacilityExpenseCharge with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/facilityexpensecharges/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_facilityexpensecharge(item_id: int, hard: bool = Query(False)):
    """Delete FacilityExpenseCharge record (soft-delete by default)."""
    svc = FacilityExpenseChargeService()
    ok = svc.delete_facilityexpensecharge(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FacilityExpenseCharge with ID {item_id} not found")
    return None

@router.get("/facilityexpensecharges/analytics/metrics", response_model=Dict[str, Any])
def get_facilityexpensecharge_metrics():
    """Calculate summary statistical KPIs for FacilityExpenseCharge collection."""
    svc = FacilityExpenseChargeService()
    return svc.calculate_aggregate_metrics()

