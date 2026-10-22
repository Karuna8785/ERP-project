"""
Fleet Telematics & Route Optimization - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    FleetVehicleService,
    DriverProfileService,
    VehicleTelematicsLogService,
    OdometerReadingService,
    FuelConsumptionLogService,
    FleetServiceScheduleService,
    RepairWorkOrderService,
    TireWearLogService,
    InspectionPreTripService,
    RouteOptimizationRunService,
    GeofenceZoneService,
    SpeedingViolationService,
    AccidentReportService,
    FleetInsuranceClaimService,
    PermitLicenseRenewalService,
    DepotStationService,
)
from .schemas import (
    FleetVehicleCreateSchema, FleetVehicleUpdateSchema, FleetVehicleResponseSchema,
    DriverProfileCreateSchema, DriverProfileUpdateSchema, DriverProfileResponseSchema,
    VehicleTelematicsLogCreateSchema, VehicleTelematicsLogUpdateSchema, VehicleTelematicsLogResponseSchema,
    OdometerReadingCreateSchema, OdometerReadingUpdateSchema, OdometerReadingResponseSchema,
    FuelConsumptionLogCreateSchema, FuelConsumptionLogUpdateSchema, FuelConsumptionLogResponseSchema,
    FleetServiceScheduleCreateSchema, FleetServiceScheduleUpdateSchema, FleetServiceScheduleResponseSchema,
    RepairWorkOrderCreateSchema, RepairWorkOrderUpdateSchema, RepairWorkOrderResponseSchema,
    TireWearLogCreateSchema, TireWearLogUpdateSchema, TireWearLogResponseSchema,
    InspectionPreTripCreateSchema, InspectionPreTripUpdateSchema, InspectionPreTripResponseSchema,
    RouteOptimizationRunCreateSchema, RouteOptimizationRunUpdateSchema, RouteOptimizationRunResponseSchema,
    GeofenceZoneCreateSchema, GeofenceZoneUpdateSchema, GeofenceZoneResponseSchema,
    SpeedingViolationCreateSchema, SpeedingViolationUpdateSchema, SpeedingViolationResponseSchema,
    AccidentReportCreateSchema, AccidentReportUpdateSchema, AccidentReportResponseSchema,
    FleetInsuranceClaimCreateSchema, FleetInsuranceClaimUpdateSchema, FleetInsuranceClaimResponseSchema,
    PermitLicenseRenewalCreateSchema, PermitLicenseRenewalUpdateSchema, PermitLicenseRenewalResponseSchema,
    DepotStationCreateSchema, DepotStationUpdateSchema, DepotStationResponseSchema,
)

router = APIRouter(prefix="/fleet_management", tags=["Fleet Telematics & Route Optimization"])

# ==================== FleetVehicle Endpoints ====================
@router.get("/fleetvehicles", response_model=List[Dict[str, Any]])
def list_fleetvehicles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FleetVehicle records with pagination and filtering."""
    svc = FleetVehicleService()
    items = svc.list_fleetvehicles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fleetvehicles/{item_id}", response_model=Dict[str, Any])
def get_fleetvehicle_by_id(item_id: int):
    """Retrieve detailed record for FleetVehicle by ID."""
    svc = FleetVehicleService()
    item = svc.get_fleetvehicle_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FleetVehicle with ID {item_id} not found")
    return item.to_dict()

@router.post("/fleetvehicles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fleetvehicle(payload: FleetVehicleCreateSchema):
    """Create new FleetVehicle instance in enterprise repository."""
    svc = FleetVehicleService()
    try:
        item = svc.create_fleetvehicle(
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

@router.put("/fleetvehicles/{item_id}", response_model=Dict[str, Any])
def update_fleetvehicle(item_id: int, payload: FleetVehicleUpdateSchema):
    """Update existing FleetVehicle record fields."""
    svc = FleetVehicleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fleetvehicle(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FleetVehicle with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fleetvehicles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fleetvehicle(item_id: int, hard: bool = Query(False)):
    """Delete FleetVehicle record (soft-delete by default)."""
    svc = FleetVehicleService()
    ok = svc.delete_fleetvehicle(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FleetVehicle with ID {item_id} not found")
    return None

@router.get("/fleetvehicles/analytics/metrics", response_model=Dict[str, Any])
def get_fleetvehicle_metrics():
    """Calculate summary statistical KPIs for FleetVehicle collection."""
    svc = FleetVehicleService()
    return svc.calculate_aggregate_metrics()

# ==================== DriverProfile Endpoints ====================
@router.get("/driverprofiles", response_model=List[Dict[str, Any]])
def list_driverprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DriverProfile records with pagination and filtering."""
    svc = DriverProfileService()
    items = svc.list_driverprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/driverprofiles/{item_id}", response_model=Dict[str, Any])
def get_driverprofile_by_id(item_id: int):
    """Retrieve detailed record for DriverProfile by ID."""
    svc = DriverProfileService()
    item = svc.get_driverprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DriverProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/driverprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_driverprofile(payload: DriverProfileCreateSchema):
    """Create new DriverProfile instance in enterprise repository."""
    svc = DriverProfileService()
    try:
        item = svc.create_driverprofile(
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

@router.put("/driverprofiles/{item_id}", response_model=Dict[str, Any])
def update_driverprofile(item_id: int, payload: DriverProfileUpdateSchema):
    """Update existing DriverProfile record fields."""
    svc = DriverProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_driverprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DriverProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/driverprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_driverprofile(item_id: int, hard: bool = Query(False)):
    """Delete DriverProfile record (soft-delete by default)."""
    svc = DriverProfileService()
    ok = svc.delete_driverprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DriverProfile with ID {item_id} not found")
    return None

@router.get("/driverprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_driverprofile_metrics():
    """Calculate summary statistical KPIs for DriverProfile collection."""
    svc = DriverProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== VehicleTelematicsLog Endpoints ====================
@router.get("/vehicletelematicslogs", response_model=List[Dict[str, Any]])
def list_vehicletelematicslogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VehicleTelematicsLog records with pagination and filtering."""
    svc = VehicleTelematicsLogService()
    items = svc.list_vehicletelematicslogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vehicletelematicslogs/{item_id}", response_model=Dict[str, Any])
def get_vehicletelematicslog_by_id(item_id: int):
    """Retrieve detailed record for VehicleTelematicsLog by ID."""
    svc = VehicleTelematicsLogService()
    item = svc.get_vehicletelematicslog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VehicleTelematicsLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/vehicletelematicslogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vehicletelematicslog(payload: VehicleTelematicsLogCreateSchema):
    """Create new VehicleTelematicsLog instance in enterprise repository."""
    svc = VehicleTelematicsLogService()
    try:
        item = svc.create_vehicletelematicslog(
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

@router.put("/vehicletelematicslogs/{item_id}", response_model=Dict[str, Any])
def update_vehicletelematicslog(item_id: int, payload: VehicleTelematicsLogUpdateSchema):
    """Update existing VehicleTelematicsLog record fields."""
    svc = VehicleTelematicsLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vehicletelematicslog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VehicleTelematicsLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vehicletelematicslogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicletelematicslog(item_id: int, hard: bool = Query(False)):
    """Delete VehicleTelematicsLog record (soft-delete by default)."""
    svc = VehicleTelematicsLogService()
    ok = svc.delete_vehicletelematicslog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VehicleTelematicsLog with ID {item_id} not found")
    return None

@router.get("/vehicletelematicslogs/analytics/metrics", response_model=Dict[str, Any])
def get_vehicletelematicslog_metrics():
    """Calculate summary statistical KPIs for VehicleTelematicsLog collection."""
    svc = VehicleTelematicsLogService()
    return svc.calculate_aggregate_metrics()

# ==================== OdometerReading Endpoints ====================
@router.get("/odometerreadings", response_model=List[Dict[str, Any]])
def list_odometerreadings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OdometerReading records with pagination and filtering."""
    svc = OdometerReadingService()
    items = svc.list_odometerreadings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/odometerreadings/{item_id}", response_model=Dict[str, Any])
def get_odometerreading_by_id(item_id: int):
    """Retrieve detailed record for OdometerReading by ID."""
    svc = OdometerReadingService()
    item = svc.get_odometerreading_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OdometerReading with ID {item_id} not found")
    return item.to_dict()

@router.post("/odometerreadings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_odometerreading(payload: OdometerReadingCreateSchema):
    """Create new OdometerReading instance in enterprise repository."""
    svc = OdometerReadingService()
    try:
        item = svc.create_odometerreading(
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

@router.put("/odometerreadings/{item_id}", response_model=Dict[str, Any])
def update_odometerreading(item_id: int, payload: OdometerReadingUpdateSchema):
    """Update existing OdometerReading record fields."""
    svc = OdometerReadingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_odometerreading(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OdometerReading with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/odometerreadings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_odometerreading(item_id: int, hard: bool = Query(False)):
    """Delete OdometerReading record (soft-delete by default)."""
    svc = OdometerReadingService()
    ok = svc.delete_odometerreading(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OdometerReading with ID {item_id} not found")
    return None

@router.get("/odometerreadings/analytics/metrics", response_model=Dict[str, Any])
def get_odometerreading_metrics():
    """Calculate summary statistical KPIs for OdometerReading collection."""
    svc = OdometerReadingService()
    return svc.calculate_aggregate_metrics()

# ==================== FuelConsumptionLog Endpoints ====================
@router.get("/fuelconsumptionlogs", response_model=List[Dict[str, Any]])
def list_fuelconsumptionlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FuelConsumptionLog records with pagination and filtering."""
    svc = FuelConsumptionLogService()
    items = svc.list_fuelconsumptionlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fuelconsumptionlogs/{item_id}", response_model=Dict[str, Any])
def get_fuelconsumptionlog_by_id(item_id: int):
    """Retrieve detailed record for FuelConsumptionLog by ID."""
    svc = FuelConsumptionLogService()
    item = svc.get_fuelconsumptionlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FuelConsumptionLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/fuelconsumptionlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fuelconsumptionlog(payload: FuelConsumptionLogCreateSchema):
    """Create new FuelConsumptionLog instance in enterprise repository."""
    svc = FuelConsumptionLogService()
    try:
        item = svc.create_fuelconsumptionlog(
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

@router.put("/fuelconsumptionlogs/{item_id}", response_model=Dict[str, Any])
def update_fuelconsumptionlog(item_id: int, payload: FuelConsumptionLogUpdateSchema):
    """Update existing FuelConsumptionLog record fields."""
    svc = FuelConsumptionLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fuelconsumptionlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FuelConsumptionLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fuelconsumptionlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fuelconsumptionlog(item_id: int, hard: bool = Query(False)):
    """Delete FuelConsumptionLog record (soft-delete by default)."""
    svc = FuelConsumptionLogService()
    ok = svc.delete_fuelconsumptionlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FuelConsumptionLog with ID {item_id} not found")
    return None

@router.get("/fuelconsumptionlogs/analytics/metrics", response_model=Dict[str, Any])
def get_fuelconsumptionlog_metrics():
    """Calculate summary statistical KPIs for FuelConsumptionLog collection."""
    svc = FuelConsumptionLogService()
    return svc.calculate_aggregate_metrics()

# ==================== FleetServiceSchedule Endpoints ====================
@router.get("/fleetserviceschedules", response_model=List[Dict[str, Any]])
def list_fleetserviceschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FleetServiceSchedule records with pagination and filtering."""
    svc = FleetServiceScheduleService()
    items = svc.list_fleetserviceschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fleetserviceschedules/{item_id}", response_model=Dict[str, Any])
def get_fleetserviceschedule_by_id(item_id: int):
    """Retrieve detailed record for FleetServiceSchedule by ID."""
    svc = FleetServiceScheduleService()
    item = svc.get_fleetserviceschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FleetServiceSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/fleetserviceschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fleetserviceschedule(payload: FleetServiceScheduleCreateSchema):
    """Create new FleetServiceSchedule instance in enterprise repository."""
    svc = FleetServiceScheduleService()
    try:
        item = svc.create_fleetserviceschedule(
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

@router.put("/fleetserviceschedules/{item_id}", response_model=Dict[str, Any])
def update_fleetserviceschedule(item_id: int, payload: FleetServiceScheduleUpdateSchema):
    """Update existing FleetServiceSchedule record fields."""
    svc = FleetServiceScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fleetserviceschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FleetServiceSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fleetserviceschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fleetserviceschedule(item_id: int, hard: bool = Query(False)):
    """Delete FleetServiceSchedule record (soft-delete by default)."""
    svc = FleetServiceScheduleService()
    ok = svc.delete_fleetserviceschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FleetServiceSchedule with ID {item_id} not found")
    return None

@router.get("/fleetserviceschedules/analytics/metrics", response_model=Dict[str, Any])
def get_fleetserviceschedule_metrics():
    """Calculate summary statistical KPIs for FleetServiceSchedule collection."""
    svc = FleetServiceScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== RepairWorkOrder Endpoints ====================
@router.get("/repairworkorders", response_model=List[Dict[str, Any]])
def list_repairworkorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RepairWorkOrder records with pagination and filtering."""
    svc = RepairWorkOrderService()
    items = svc.list_repairworkorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/repairworkorders/{item_id}", response_model=Dict[str, Any])
def get_repairworkorder_by_id(item_id: int):
    """Retrieve detailed record for RepairWorkOrder by ID."""
    svc = RepairWorkOrderService()
    item = svc.get_repairworkorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RepairWorkOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/repairworkorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_repairworkorder(payload: RepairWorkOrderCreateSchema):
    """Create new RepairWorkOrder instance in enterprise repository."""
    svc = RepairWorkOrderService()
    try:
        item = svc.create_repairworkorder(
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

@router.put("/repairworkorders/{item_id}", response_model=Dict[str, Any])
def update_repairworkorder(item_id: int, payload: RepairWorkOrderUpdateSchema):
    """Update existing RepairWorkOrder record fields."""
    svc = RepairWorkOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_repairworkorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RepairWorkOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/repairworkorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_repairworkorder(item_id: int, hard: bool = Query(False)):
    """Delete RepairWorkOrder record (soft-delete by default)."""
    svc = RepairWorkOrderService()
    ok = svc.delete_repairworkorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RepairWorkOrder with ID {item_id} not found")
    return None

@router.get("/repairworkorders/analytics/metrics", response_model=Dict[str, Any])
def get_repairworkorder_metrics():
    """Calculate summary statistical KPIs for RepairWorkOrder collection."""
    svc = RepairWorkOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== TireWearLog Endpoints ====================
@router.get("/tirewearlogs", response_model=List[Dict[str, Any]])
def list_tirewearlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TireWearLog records with pagination and filtering."""
    svc = TireWearLogService()
    items = svc.list_tirewearlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tirewearlogs/{item_id}", response_model=Dict[str, Any])
def get_tirewearlog_by_id(item_id: int):
    """Retrieve detailed record for TireWearLog by ID."""
    svc = TireWearLogService()
    item = svc.get_tirewearlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TireWearLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/tirewearlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tirewearlog(payload: TireWearLogCreateSchema):
    """Create new TireWearLog instance in enterprise repository."""
    svc = TireWearLogService()
    try:
        item = svc.create_tirewearlog(
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

@router.put("/tirewearlogs/{item_id}", response_model=Dict[str, Any])
def update_tirewearlog(item_id: int, payload: TireWearLogUpdateSchema):
    """Update existing TireWearLog record fields."""
    svc = TireWearLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tirewearlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TireWearLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tirewearlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tirewearlog(item_id: int, hard: bool = Query(False)):
    """Delete TireWearLog record (soft-delete by default)."""
    svc = TireWearLogService()
    ok = svc.delete_tirewearlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TireWearLog with ID {item_id} not found")
    return None

@router.get("/tirewearlogs/analytics/metrics", response_model=Dict[str, Any])
def get_tirewearlog_metrics():
    """Calculate summary statistical KPIs for TireWearLog collection."""
    svc = TireWearLogService()
    return svc.calculate_aggregate_metrics()

# ==================== InspectionPreTrip Endpoints ====================
@router.get("/inspectionpretrips", response_model=List[Dict[str, Any]])
def list_inspectionpretrips(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InspectionPreTrip records with pagination and filtering."""
    svc = InspectionPreTripService()
    items = svc.list_inspectionpretrips(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inspectionpretrips/{item_id}", response_model=Dict[str, Any])
def get_inspectionpretrip_by_id(item_id: int):
    """Retrieve detailed record for InspectionPreTrip by ID."""
    svc = InspectionPreTripService()
    item = svc.get_inspectionpretrip_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InspectionPreTrip with ID {item_id} not found")
    return item.to_dict()

@router.post("/inspectionpretrips", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inspectionpretrip(payload: InspectionPreTripCreateSchema):
    """Create new InspectionPreTrip instance in enterprise repository."""
    svc = InspectionPreTripService()
    try:
        item = svc.create_inspectionpretrip(
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

@router.put("/inspectionpretrips/{item_id}", response_model=Dict[str, Any])
def update_inspectionpretrip(item_id: int, payload: InspectionPreTripUpdateSchema):
    """Update existing InspectionPreTrip record fields."""
    svc = InspectionPreTripService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inspectionpretrip(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InspectionPreTrip with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inspectionpretrips/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inspectionpretrip(item_id: int, hard: bool = Query(False)):
    """Delete InspectionPreTrip record (soft-delete by default)."""
    svc = InspectionPreTripService()
    ok = svc.delete_inspectionpretrip(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InspectionPreTrip with ID {item_id} not found")
    return None

@router.get("/inspectionpretrips/analytics/metrics", response_model=Dict[str, Any])
def get_inspectionpretrip_metrics():
    """Calculate summary statistical KPIs for InspectionPreTrip collection."""
    svc = InspectionPreTripService()
    return svc.calculate_aggregate_metrics()

# ==================== RouteOptimizationRun Endpoints ====================
@router.get("/routeoptimizationruns", response_model=List[Dict[str, Any]])
def list_routeoptimizationruns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RouteOptimizationRun records with pagination and filtering."""
    svc = RouteOptimizationRunService()
    items = svc.list_routeoptimizationruns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/routeoptimizationruns/{item_id}", response_model=Dict[str, Any])
def get_routeoptimizationrun_by_id(item_id: int):
    """Retrieve detailed record for RouteOptimizationRun by ID."""
    svc = RouteOptimizationRunService()
    item = svc.get_routeoptimizationrun_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RouteOptimizationRun with ID {item_id} not found")
    return item.to_dict()

@router.post("/routeoptimizationruns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_routeoptimizationrun(payload: RouteOptimizationRunCreateSchema):
    """Create new RouteOptimizationRun instance in enterprise repository."""
    svc = RouteOptimizationRunService()
    try:
        item = svc.create_routeoptimizationrun(
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

@router.put("/routeoptimizationruns/{item_id}", response_model=Dict[str, Any])
def update_routeoptimizationrun(item_id: int, payload: RouteOptimizationRunUpdateSchema):
    """Update existing RouteOptimizationRun record fields."""
    svc = RouteOptimizationRunService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_routeoptimizationrun(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RouteOptimizationRun with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/routeoptimizationruns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_routeoptimizationrun(item_id: int, hard: bool = Query(False)):
    """Delete RouteOptimizationRun record (soft-delete by default)."""
    svc = RouteOptimizationRunService()
    ok = svc.delete_routeoptimizationrun(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RouteOptimizationRun with ID {item_id} not found")
    return None

@router.get("/routeoptimizationruns/analytics/metrics", response_model=Dict[str, Any])
def get_routeoptimizationrun_metrics():
    """Calculate summary statistical KPIs for RouteOptimizationRun collection."""
    svc = RouteOptimizationRunService()
    return svc.calculate_aggregate_metrics()

# ==================== GeofenceZone Endpoints ====================
@router.get("/geofencezones", response_model=List[Dict[str, Any]])
def list_geofencezones(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GeofenceZone records with pagination and filtering."""
    svc = GeofenceZoneService()
    items = svc.list_geofencezones(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/geofencezones/{item_id}", response_model=Dict[str, Any])
def get_geofencezone_by_id(item_id: int):
    """Retrieve detailed record for GeofenceZone by ID."""
    svc = GeofenceZoneService()
    item = svc.get_geofencezone_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GeofenceZone with ID {item_id} not found")
    return item.to_dict()

@router.post("/geofencezones", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_geofencezone(payload: GeofenceZoneCreateSchema):
    """Create new GeofenceZone instance in enterprise repository."""
    svc = GeofenceZoneService()
    try:
        item = svc.create_geofencezone(
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

@router.put("/geofencezones/{item_id}", response_model=Dict[str, Any])
def update_geofencezone(item_id: int, payload: GeofenceZoneUpdateSchema):
    """Update existing GeofenceZone record fields."""
    svc = GeofenceZoneService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_geofencezone(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GeofenceZone with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/geofencezones/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_geofencezone(item_id: int, hard: bool = Query(False)):
    """Delete GeofenceZone record (soft-delete by default)."""
    svc = GeofenceZoneService()
    ok = svc.delete_geofencezone(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GeofenceZone with ID {item_id} not found")
    return None

@router.get("/geofencezones/analytics/metrics", response_model=Dict[str, Any])
def get_geofencezone_metrics():
    """Calculate summary statistical KPIs for GeofenceZone collection."""
    svc = GeofenceZoneService()
    return svc.calculate_aggregate_metrics()

# ==================== SpeedingViolation Endpoints ====================
@router.get("/speedingviolations", response_model=List[Dict[str, Any]])
def list_speedingviolations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SpeedingViolation records with pagination and filtering."""
    svc = SpeedingViolationService()
    items = svc.list_speedingviolations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/speedingviolations/{item_id}", response_model=Dict[str, Any])
def get_speedingviolation_by_id(item_id: int):
    """Retrieve detailed record for SpeedingViolation by ID."""
    svc = SpeedingViolationService()
    item = svc.get_speedingviolation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SpeedingViolation with ID {item_id} not found")
    return item.to_dict()

@router.post("/speedingviolations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_speedingviolation(payload: SpeedingViolationCreateSchema):
    """Create new SpeedingViolation instance in enterprise repository."""
    svc = SpeedingViolationService()
    try:
        item = svc.create_speedingviolation(
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

@router.put("/speedingviolations/{item_id}", response_model=Dict[str, Any])
def update_speedingviolation(item_id: int, payload: SpeedingViolationUpdateSchema):
    """Update existing SpeedingViolation record fields."""
    svc = SpeedingViolationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_speedingviolation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SpeedingViolation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/speedingviolations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_speedingviolation(item_id: int, hard: bool = Query(False)):
    """Delete SpeedingViolation record (soft-delete by default)."""
    svc = SpeedingViolationService()
    ok = svc.delete_speedingviolation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SpeedingViolation with ID {item_id} not found")
    return None

@router.get("/speedingviolations/analytics/metrics", response_model=Dict[str, Any])
def get_speedingviolation_metrics():
    """Calculate summary statistical KPIs for SpeedingViolation collection."""
    svc = SpeedingViolationService()
    return svc.calculate_aggregate_metrics()

# ==================== AccidentReport Endpoints ====================
@router.get("/accidentreports", response_model=List[Dict[str, Any]])
def list_accidentreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AccidentReport records with pagination and filtering."""
    svc = AccidentReportService()
    items = svc.list_accidentreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/accidentreports/{item_id}", response_model=Dict[str, Any])
def get_accidentreport_by_id(item_id: int):
    """Retrieve detailed record for AccidentReport by ID."""
    svc = AccidentReportService()
    item = svc.get_accidentreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AccidentReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/accidentreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_accidentreport(payload: AccidentReportCreateSchema):
    """Create new AccidentReport instance in enterprise repository."""
    svc = AccidentReportService()
    try:
        item = svc.create_accidentreport(
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

@router.put("/accidentreports/{item_id}", response_model=Dict[str, Any])
def update_accidentreport(item_id: int, payload: AccidentReportUpdateSchema):
    """Update existing AccidentReport record fields."""
    svc = AccidentReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_accidentreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AccidentReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/accidentreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accidentreport(item_id: int, hard: bool = Query(False)):
    """Delete AccidentReport record (soft-delete by default)."""
    svc = AccidentReportService()
    ok = svc.delete_accidentreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AccidentReport with ID {item_id} not found")
    return None

@router.get("/accidentreports/analytics/metrics", response_model=Dict[str, Any])
def get_accidentreport_metrics():
    """Calculate summary statistical KPIs for AccidentReport collection."""
    svc = AccidentReportService()
    return svc.calculate_aggregate_metrics()

# ==================== FleetInsuranceClaim Endpoints ====================
@router.get("/fleetinsuranceclaims", response_model=List[Dict[str, Any]])
def list_fleetinsuranceclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FleetInsuranceClaim records with pagination and filtering."""
    svc = FleetInsuranceClaimService()
    items = svc.list_fleetinsuranceclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fleetinsuranceclaims/{item_id}", response_model=Dict[str, Any])
def get_fleetinsuranceclaim_by_id(item_id: int):
    """Retrieve detailed record for FleetInsuranceClaim by ID."""
    svc = FleetInsuranceClaimService()
    item = svc.get_fleetinsuranceclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FleetInsuranceClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/fleetinsuranceclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fleetinsuranceclaim(payload: FleetInsuranceClaimCreateSchema):
    """Create new FleetInsuranceClaim instance in enterprise repository."""
    svc = FleetInsuranceClaimService()
    try:
        item = svc.create_fleetinsuranceclaim(
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

@router.put("/fleetinsuranceclaims/{item_id}", response_model=Dict[str, Any])
def update_fleetinsuranceclaim(item_id: int, payload: FleetInsuranceClaimUpdateSchema):
    """Update existing FleetInsuranceClaim record fields."""
    svc = FleetInsuranceClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fleetinsuranceclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FleetInsuranceClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fleetinsuranceclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fleetinsuranceclaim(item_id: int, hard: bool = Query(False)):
    """Delete FleetInsuranceClaim record (soft-delete by default)."""
    svc = FleetInsuranceClaimService()
    ok = svc.delete_fleetinsuranceclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FleetInsuranceClaim with ID {item_id} not found")
    return None

@router.get("/fleetinsuranceclaims/analytics/metrics", response_model=Dict[str, Any])
def get_fleetinsuranceclaim_metrics():
    """Calculate summary statistical KPIs for FleetInsuranceClaim collection."""
    svc = FleetInsuranceClaimService()
    return svc.calculate_aggregate_metrics()

# ==================== PermitLicenseRenewal Endpoints ====================
@router.get("/permitlicenserenewals", response_model=List[Dict[str, Any]])
def list_permitlicenserenewals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PermitLicenseRenewal records with pagination and filtering."""
    svc = PermitLicenseRenewalService()
    items = svc.list_permitlicenserenewals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/permitlicenserenewals/{item_id}", response_model=Dict[str, Any])
def get_permitlicenserenewal_by_id(item_id: int):
    """Retrieve detailed record for PermitLicenseRenewal by ID."""
    svc = PermitLicenseRenewalService()
    item = svc.get_permitlicenserenewal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PermitLicenseRenewal with ID {item_id} not found")
    return item.to_dict()

@router.post("/permitlicenserenewals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_permitlicenserenewal(payload: PermitLicenseRenewalCreateSchema):
    """Create new PermitLicenseRenewal instance in enterprise repository."""
    svc = PermitLicenseRenewalService()
    try:
        item = svc.create_permitlicenserenewal(
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

@router.put("/permitlicenserenewals/{item_id}", response_model=Dict[str, Any])
def update_permitlicenserenewal(item_id: int, payload: PermitLicenseRenewalUpdateSchema):
    """Update existing PermitLicenseRenewal record fields."""
    svc = PermitLicenseRenewalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_permitlicenserenewal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PermitLicenseRenewal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/permitlicenserenewals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_permitlicenserenewal(item_id: int, hard: bool = Query(False)):
    """Delete PermitLicenseRenewal record (soft-delete by default)."""
    svc = PermitLicenseRenewalService()
    ok = svc.delete_permitlicenserenewal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PermitLicenseRenewal with ID {item_id} not found")
    return None

@router.get("/permitlicenserenewals/analytics/metrics", response_model=Dict[str, Any])
def get_permitlicenserenewal_metrics():
    """Calculate summary statistical KPIs for PermitLicenseRenewal collection."""
    svc = PermitLicenseRenewalService()
    return svc.calculate_aggregate_metrics()

# ==================== DepotStation Endpoints ====================
@router.get("/depotstations", response_model=List[Dict[str, Any]])
def list_depotstations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DepotStation records with pagination and filtering."""
    svc = DepotStationService()
    items = svc.list_depotstations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/depotstations/{item_id}", response_model=Dict[str, Any])
def get_depotstation_by_id(item_id: int):
    """Retrieve detailed record for DepotStation by ID."""
    svc = DepotStationService()
    item = svc.get_depotstation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DepotStation with ID {item_id} not found")
    return item.to_dict()

@router.post("/depotstations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_depotstation(payload: DepotStationCreateSchema):
    """Create new DepotStation instance in enterprise repository."""
    svc = DepotStationService()
    try:
        item = svc.create_depotstation(
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

@router.put("/depotstations/{item_id}", response_model=Dict[str, Any])
def update_depotstation(item_id: int, payload: DepotStationUpdateSchema):
    """Update existing DepotStation record fields."""
    svc = DepotStationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_depotstation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DepotStation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/depotstations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_depotstation(item_id: int, hard: bool = Query(False)):
    """Delete DepotStation record (soft-delete by default)."""
    svc = DepotStationService()
    ok = svc.delete_depotstation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DepotStation with ID {item_id} not found")
    return None

@router.get("/depotstations/analytics/metrics", response_model=Dict[str, Any])
def get_depotstation_metrics():
    """Calculate summary statistical KPIs for DepotStation collection."""
    svc = DepotStationService()
    return svc.calculate_aggregate_metrics()

