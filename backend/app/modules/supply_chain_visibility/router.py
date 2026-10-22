"""
Real-time IoT Telemetry & Supply Chain Visibility - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    IoTSensorTelemetryPingService,
    ColdChainTempLoggerService,
    RFIDPalletScanRecordService,
    GeofenceTransitEventService,
    ShipmentShockSensorLogService,
    ContainerSealStatusService,
    SmartContractEscrowEventService,
    CarrierLocationWaypointService,
    DwellTimeExceedNoticeService,
    PredictiveETAEstimateService,
    CarbonEmissionWaypointService,
    CustomsClearanceMilestoneService,
    TamperEvidentIncidentService,
    WeatherDisruptionAlertService,
    MultimodalHandoverNoteService,
    TrackAndTraceAuditLogService,
)
from .schemas import (
    IoTSensorTelemetryPingCreateSchema, IoTSensorTelemetryPingUpdateSchema, IoTSensorTelemetryPingResponseSchema,
    ColdChainTempLoggerCreateSchema, ColdChainTempLoggerUpdateSchema, ColdChainTempLoggerResponseSchema,
    RFIDPalletScanRecordCreateSchema, RFIDPalletScanRecordUpdateSchema, RFIDPalletScanRecordResponseSchema,
    GeofenceTransitEventCreateSchema, GeofenceTransitEventUpdateSchema, GeofenceTransitEventResponseSchema,
    ShipmentShockSensorLogCreateSchema, ShipmentShockSensorLogUpdateSchema, ShipmentShockSensorLogResponseSchema,
    ContainerSealStatusCreateSchema, ContainerSealStatusUpdateSchema, ContainerSealStatusResponseSchema,
    SmartContractEscrowEventCreateSchema, SmartContractEscrowEventUpdateSchema, SmartContractEscrowEventResponseSchema,
    CarrierLocationWaypointCreateSchema, CarrierLocationWaypointUpdateSchema, CarrierLocationWaypointResponseSchema,
    DwellTimeExceedNoticeCreateSchema, DwellTimeExceedNoticeUpdateSchema, DwellTimeExceedNoticeResponseSchema,
    PredictiveETAEstimateCreateSchema, PredictiveETAEstimateUpdateSchema, PredictiveETAEstimateResponseSchema,
    CarbonEmissionWaypointCreateSchema, CarbonEmissionWaypointUpdateSchema, CarbonEmissionWaypointResponseSchema,
    CustomsClearanceMilestoneCreateSchema, CustomsClearanceMilestoneUpdateSchema, CustomsClearanceMilestoneResponseSchema,
    TamperEvidentIncidentCreateSchema, TamperEvidentIncidentUpdateSchema, TamperEvidentIncidentResponseSchema,
    WeatherDisruptionAlertCreateSchema, WeatherDisruptionAlertUpdateSchema, WeatherDisruptionAlertResponseSchema,
    MultimodalHandoverNoteCreateSchema, MultimodalHandoverNoteUpdateSchema, MultimodalHandoverNoteResponseSchema,
    TrackAndTraceAuditLogCreateSchema, TrackAndTraceAuditLogUpdateSchema, TrackAndTraceAuditLogResponseSchema,
)

router = APIRouter(prefix="/supply_chain_visibility", tags=["Real-time IoT Telemetry & Supply Chain Visibility"])

# ==================== IoTSensorTelemetryPing Endpoints ====================
@router.get("/iotsensortelemetrypings", response_model=List[Dict[str, Any]])
def list_iotsensortelemetrypings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IoTSensorTelemetryPing records with pagination and filtering."""
    svc = IoTSensorTelemetryPingService()
    items = svc.list_iotsensortelemetrypings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/iotsensortelemetrypings/{item_id}", response_model=Dict[str, Any])
def get_iotsensortelemetryping_by_id(item_id: int):
    """Retrieve detailed record for IoTSensorTelemetryPing by ID."""
    svc = IoTSensorTelemetryPingService()
    item = svc.get_iotsensortelemetryping_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IoTSensorTelemetryPing with ID {item_id} not found")
    return item.to_dict()

@router.post("/iotsensortelemetrypings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_iotsensortelemetryping(payload: IoTSensorTelemetryPingCreateSchema):
    """Create new IoTSensorTelemetryPing instance in enterprise repository."""
    svc = IoTSensorTelemetryPingService()
    try:
        item = svc.create_iotsensortelemetryping(
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

@router.put("/iotsensortelemetrypings/{item_id}", response_model=Dict[str, Any])
def update_iotsensortelemetryping(item_id: int, payload: IoTSensorTelemetryPingUpdateSchema):
    """Update existing IoTSensorTelemetryPing record fields."""
    svc = IoTSensorTelemetryPingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_iotsensortelemetryping(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IoTSensorTelemetryPing with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/iotsensortelemetrypings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_iotsensortelemetryping(item_id: int, hard: bool = Query(False)):
    """Delete IoTSensorTelemetryPing record (soft-delete by default)."""
    svc = IoTSensorTelemetryPingService()
    ok = svc.delete_iotsensortelemetryping(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IoTSensorTelemetryPing with ID {item_id} not found")
    return None

@router.get("/iotsensortelemetrypings/analytics/metrics", response_model=Dict[str, Any])
def get_iotsensortelemetryping_metrics():
    """Calculate summary statistical KPIs for IoTSensorTelemetryPing collection."""
    svc = IoTSensorTelemetryPingService()
    return svc.calculate_aggregate_metrics()

# ==================== ColdChainTempLogger Endpoints ====================
@router.get("/coldchaintemploggers", response_model=List[Dict[str, Any]])
def list_coldchaintemploggers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ColdChainTempLogger records with pagination and filtering."""
    svc = ColdChainTempLoggerService()
    items = svc.list_coldchaintemploggers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/coldchaintemploggers/{item_id}", response_model=Dict[str, Any])
def get_coldchaintemplogger_by_id(item_id: int):
    """Retrieve detailed record for ColdChainTempLogger by ID."""
    svc = ColdChainTempLoggerService()
    item = svc.get_coldchaintemplogger_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ColdChainTempLogger with ID {item_id} not found")
    return item.to_dict()

@router.post("/coldchaintemploggers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_coldchaintemplogger(payload: ColdChainTempLoggerCreateSchema):
    """Create new ColdChainTempLogger instance in enterprise repository."""
    svc = ColdChainTempLoggerService()
    try:
        item = svc.create_coldchaintemplogger(
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

@router.put("/coldchaintemploggers/{item_id}", response_model=Dict[str, Any])
def update_coldchaintemplogger(item_id: int, payload: ColdChainTempLoggerUpdateSchema):
    """Update existing ColdChainTempLogger record fields."""
    svc = ColdChainTempLoggerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_coldchaintemplogger(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ColdChainTempLogger with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/coldchaintemploggers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_coldchaintemplogger(item_id: int, hard: bool = Query(False)):
    """Delete ColdChainTempLogger record (soft-delete by default)."""
    svc = ColdChainTempLoggerService()
    ok = svc.delete_coldchaintemplogger(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ColdChainTempLogger with ID {item_id} not found")
    return None

@router.get("/coldchaintemploggers/analytics/metrics", response_model=Dict[str, Any])
def get_coldchaintemplogger_metrics():
    """Calculate summary statistical KPIs for ColdChainTempLogger collection."""
    svc = ColdChainTempLoggerService()
    return svc.calculate_aggregate_metrics()

# ==================== RFIDPalletScanRecord Endpoints ====================
@router.get("/rfidpalletscanrecords", response_model=List[Dict[str, Any]])
def list_rfidpalletscanrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RFIDPalletScanRecord records with pagination and filtering."""
    svc = RFIDPalletScanRecordService()
    items = svc.list_rfidpalletscanrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/rfidpalletscanrecords/{item_id}", response_model=Dict[str, Any])
def get_rfidpalletscanrecord_by_id(item_id: int):
    """Retrieve detailed record for RFIDPalletScanRecord by ID."""
    svc = RFIDPalletScanRecordService()
    item = svc.get_rfidpalletscanrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RFIDPalletScanRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/rfidpalletscanrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_rfidpalletscanrecord(payload: RFIDPalletScanRecordCreateSchema):
    """Create new RFIDPalletScanRecord instance in enterprise repository."""
    svc = RFIDPalletScanRecordService()
    try:
        item = svc.create_rfidpalletscanrecord(
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

@router.put("/rfidpalletscanrecords/{item_id}", response_model=Dict[str, Any])
def update_rfidpalletscanrecord(item_id: int, payload: RFIDPalletScanRecordUpdateSchema):
    """Update existing RFIDPalletScanRecord record fields."""
    svc = RFIDPalletScanRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_rfidpalletscanrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RFIDPalletScanRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/rfidpalletscanrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rfidpalletscanrecord(item_id: int, hard: bool = Query(False)):
    """Delete RFIDPalletScanRecord record (soft-delete by default)."""
    svc = RFIDPalletScanRecordService()
    ok = svc.delete_rfidpalletscanrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RFIDPalletScanRecord with ID {item_id} not found")
    return None

@router.get("/rfidpalletscanrecords/analytics/metrics", response_model=Dict[str, Any])
def get_rfidpalletscanrecord_metrics():
    """Calculate summary statistical KPIs for RFIDPalletScanRecord collection."""
    svc = RFIDPalletScanRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== GeofenceTransitEvent Endpoints ====================
@router.get("/geofencetransitevents", response_model=List[Dict[str, Any]])
def list_geofencetransitevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GeofenceTransitEvent records with pagination and filtering."""
    svc = GeofenceTransitEventService()
    items = svc.list_geofencetransitevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/geofencetransitevents/{item_id}", response_model=Dict[str, Any])
def get_geofencetransitevent_by_id(item_id: int):
    """Retrieve detailed record for GeofenceTransitEvent by ID."""
    svc = GeofenceTransitEventService()
    item = svc.get_geofencetransitevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GeofenceTransitEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/geofencetransitevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_geofencetransitevent(payload: GeofenceTransitEventCreateSchema):
    """Create new GeofenceTransitEvent instance in enterprise repository."""
    svc = GeofenceTransitEventService()
    try:
        item = svc.create_geofencetransitevent(
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

@router.put("/geofencetransitevents/{item_id}", response_model=Dict[str, Any])
def update_geofencetransitevent(item_id: int, payload: GeofenceTransitEventUpdateSchema):
    """Update existing GeofenceTransitEvent record fields."""
    svc = GeofenceTransitEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_geofencetransitevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GeofenceTransitEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/geofencetransitevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_geofencetransitevent(item_id: int, hard: bool = Query(False)):
    """Delete GeofenceTransitEvent record (soft-delete by default)."""
    svc = GeofenceTransitEventService()
    ok = svc.delete_geofencetransitevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GeofenceTransitEvent with ID {item_id} not found")
    return None

@router.get("/geofencetransitevents/analytics/metrics", response_model=Dict[str, Any])
def get_geofencetransitevent_metrics():
    """Calculate summary statistical KPIs for GeofenceTransitEvent collection."""
    svc = GeofenceTransitEventService()
    return svc.calculate_aggregate_metrics()

# ==================== ShipmentShockSensorLog Endpoints ====================
@router.get("/shipmentshocksensorlogs", response_model=List[Dict[str, Any]])
def list_shipmentshocksensorlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShipmentShockSensorLog records with pagination and filtering."""
    svc = ShipmentShockSensorLogService()
    items = svc.list_shipmentshocksensorlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shipmentshocksensorlogs/{item_id}", response_model=Dict[str, Any])
def get_shipmentshocksensorlog_by_id(item_id: int):
    """Retrieve detailed record for ShipmentShockSensorLog by ID."""
    svc = ShipmentShockSensorLogService()
    item = svc.get_shipmentshocksensorlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShipmentShockSensorLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/shipmentshocksensorlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shipmentshocksensorlog(payload: ShipmentShockSensorLogCreateSchema):
    """Create new ShipmentShockSensorLog instance in enterprise repository."""
    svc = ShipmentShockSensorLogService()
    try:
        item = svc.create_shipmentshocksensorlog(
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

@router.put("/shipmentshocksensorlogs/{item_id}", response_model=Dict[str, Any])
def update_shipmentshocksensorlog(item_id: int, payload: ShipmentShockSensorLogUpdateSchema):
    """Update existing ShipmentShockSensorLog record fields."""
    svc = ShipmentShockSensorLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shipmentshocksensorlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShipmentShockSensorLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shipmentshocksensorlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shipmentshocksensorlog(item_id: int, hard: bool = Query(False)):
    """Delete ShipmentShockSensorLog record (soft-delete by default)."""
    svc = ShipmentShockSensorLogService()
    ok = svc.delete_shipmentshocksensorlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShipmentShockSensorLog with ID {item_id} not found")
    return None

@router.get("/shipmentshocksensorlogs/analytics/metrics", response_model=Dict[str, Any])
def get_shipmentshocksensorlog_metrics():
    """Calculate summary statistical KPIs for ShipmentShockSensorLog collection."""
    svc = ShipmentShockSensorLogService()
    return svc.calculate_aggregate_metrics()

# ==================== ContainerSealStatus Endpoints ====================
@router.get("/containersealstatuss", response_model=List[Dict[str, Any]])
def list_containersealstatuss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContainerSealStatus records with pagination and filtering."""
    svc = ContainerSealStatusService()
    items = svc.list_containersealstatuss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/containersealstatuss/{item_id}", response_model=Dict[str, Any])
def get_containersealstatus_by_id(item_id: int):
    """Retrieve detailed record for ContainerSealStatus by ID."""
    svc = ContainerSealStatusService()
    item = svc.get_containersealstatus_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContainerSealStatus with ID {item_id} not found")
    return item.to_dict()

@router.post("/containersealstatuss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_containersealstatus(payload: ContainerSealStatusCreateSchema):
    """Create new ContainerSealStatus instance in enterprise repository."""
    svc = ContainerSealStatusService()
    try:
        item = svc.create_containersealstatus(
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

@router.put("/containersealstatuss/{item_id}", response_model=Dict[str, Any])
def update_containersealstatus(item_id: int, payload: ContainerSealStatusUpdateSchema):
    """Update existing ContainerSealStatus record fields."""
    svc = ContainerSealStatusService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_containersealstatus(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContainerSealStatus with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/containersealstatuss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_containersealstatus(item_id: int, hard: bool = Query(False)):
    """Delete ContainerSealStatus record (soft-delete by default)."""
    svc = ContainerSealStatusService()
    ok = svc.delete_containersealstatus(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContainerSealStatus with ID {item_id} not found")
    return None

@router.get("/containersealstatuss/analytics/metrics", response_model=Dict[str, Any])
def get_containersealstatus_metrics():
    """Calculate summary statistical KPIs for ContainerSealStatus collection."""
    svc = ContainerSealStatusService()
    return svc.calculate_aggregate_metrics()

# ==================== SmartContractEscrowEvent Endpoints ====================
@router.get("/smartcontractescrowevents", response_model=List[Dict[str, Any]])
def list_smartcontractescrowevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SmartContractEscrowEvent records with pagination and filtering."""
    svc = SmartContractEscrowEventService()
    items = svc.list_smartcontractescrowevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/smartcontractescrowevents/{item_id}", response_model=Dict[str, Any])
def get_smartcontractescrowevent_by_id(item_id: int):
    """Retrieve detailed record for SmartContractEscrowEvent by ID."""
    svc = SmartContractEscrowEventService()
    item = svc.get_smartcontractescrowevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SmartContractEscrowEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/smartcontractescrowevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_smartcontractescrowevent(payload: SmartContractEscrowEventCreateSchema):
    """Create new SmartContractEscrowEvent instance in enterprise repository."""
    svc = SmartContractEscrowEventService()
    try:
        item = svc.create_smartcontractescrowevent(
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

@router.put("/smartcontractescrowevents/{item_id}", response_model=Dict[str, Any])
def update_smartcontractescrowevent(item_id: int, payload: SmartContractEscrowEventUpdateSchema):
    """Update existing SmartContractEscrowEvent record fields."""
    svc = SmartContractEscrowEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_smartcontractescrowevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SmartContractEscrowEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/smartcontractescrowevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_smartcontractescrowevent(item_id: int, hard: bool = Query(False)):
    """Delete SmartContractEscrowEvent record (soft-delete by default)."""
    svc = SmartContractEscrowEventService()
    ok = svc.delete_smartcontractescrowevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SmartContractEscrowEvent with ID {item_id} not found")
    return None

@router.get("/smartcontractescrowevents/analytics/metrics", response_model=Dict[str, Any])
def get_smartcontractescrowevent_metrics():
    """Calculate summary statistical KPIs for SmartContractEscrowEvent collection."""
    svc = SmartContractEscrowEventService()
    return svc.calculate_aggregate_metrics()

# ==================== CarrierLocationWaypoint Endpoints ====================
@router.get("/carrierlocationwaypoints", response_model=List[Dict[str, Any]])
def list_carrierlocationwaypoints(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CarrierLocationWaypoint records with pagination and filtering."""
    svc = CarrierLocationWaypointService()
    items = svc.list_carrierlocationwaypoints(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/carrierlocationwaypoints/{item_id}", response_model=Dict[str, Any])
def get_carrierlocationwaypoint_by_id(item_id: int):
    """Retrieve detailed record for CarrierLocationWaypoint by ID."""
    svc = CarrierLocationWaypointService()
    item = svc.get_carrierlocationwaypoint_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CarrierLocationWaypoint with ID {item_id} not found")
    return item.to_dict()

@router.post("/carrierlocationwaypoints", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_carrierlocationwaypoint(payload: CarrierLocationWaypointCreateSchema):
    """Create new CarrierLocationWaypoint instance in enterprise repository."""
    svc = CarrierLocationWaypointService()
    try:
        item = svc.create_carrierlocationwaypoint(
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

@router.put("/carrierlocationwaypoints/{item_id}", response_model=Dict[str, Any])
def update_carrierlocationwaypoint(item_id: int, payload: CarrierLocationWaypointUpdateSchema):
    """Update existing CarrierLocationWaypoint record fields."""
    svc = CarrierLocationWaypointService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_carrierlocationwaypoint(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CarrierLocationWaypoint with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/carrierlocationwaypoints/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrierlocationwaypoint(item_id: int, hard: bool = Query(False)):
    """Delete CarrierLocationWaypoint record (soft-delete by default)."""
    svc = CarrierLocationWaypointService()
    ok = svc.delete_carrierlocationwaypoint(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CarrierLocationWaypoint with ID {item_id} not found")
    return None

@router.get("/carrierlocationwaypoints/analytics/metrics", response_model=Dict[str, Any])
def get_carrierlocationwaypoint_metrics():
    """Calculate summary statistical KPIs for CarrierLocationWaypoint collection."""
    svc = CarrierLocationWaypointService()
    return svc.calculate_aggregate_metrics()

# ==================== DwellTimeExceedNotice Endpoints ====================
@router.get("/dwelltimeexceednotices", response_model=List[Dict[str, Any]])
def list_dwelltimeexceednotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DwellTimeExceedNotice records with pagination and filtering."""
    svc = DwellTimeExceedNoticeService()
    items = svc.list_dwelltimeexceednotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dwelltimeexceednotices/{item_id}", response_model=Dict[str, Any])
def get_dwelltimeexceednotice_by_id(item_id: int):
    """Retrieve detailed record for DwellTimeExceedNotice by ID."""
    svc = DwellTimeExceedNoticeService()
    item = svc.get_dwelltimeexceednotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DwellTimeExceedNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/dwelltimeexceednotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dwelltimeexceednotice(payload: DwellTimeExceedNoticeCreateSchema):
    """Create new DwellTimeExceedNotice instance in enterprise repository."""
    svc = DwellTimeExceedNoticeService()
    try:
        item = svc.create_dwelltimeexceednotice(
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

@router.put("/dwelltimeexceednotices/{item_id}", response_model=Dict[str, Any])
def update_dwelltimeexceednotice(item_id: int, payload: DwellTimeExceedNoticeUpdateSchema):
    """Update existing DwellTimeExceedNotice record fields."""
    svc = DwellTimeExceedNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dwelltimeexceednotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DwellTimeExceedNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dwelltimeexceednotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dwelltimeexceednotice(item_id: int, hard: bool = Query(False)):
    """Delete DwellTimeExceedNotice record (soft-delete by default)."""
    svc = DwellTimeExceedNoticeService()
    ok = svc.delete_dwelltimeexceednotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DwellTimeExceedNotice with ID {item_id} not found")
    return None

@router.get("/dwelltimeexceednotices/analytics/metrics", response_model=Dict[str, Any])
def get_dwelltimeexceednotice_metrics():
    """Calculate summary statistical KPIs for DwellTimeExceedNotice collection."""
    svc = DwellTimeExceedNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== PredictiveETAEstimate Endpoints ====================
@router.get("/predictiveetaestimates", response_model=List[Dict[str, Any]])
def list_predictiveetaestimates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PredictiveETAEstimate records with pagination and filtering."""
    svc = PredictiveETAEstimateService()
    items = svc.list_predictiveetaestimates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/predictiveetaestimates/{item_id}", response_model=Dict[str, Any])
def get_predictiveetaestimate_by_id(item_id: int):
    """Retrieve detailed record for PredictiveETAEstimate by ID."""
    svc = PredictiveETAEstimateService()
    item = svc.get_predictiveetaestimate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PredictiveETAEstimate with ID {item_id} not found")
    return item.to_dict()

@router.post("/predictiveetaestimates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_predictiveetaestimate(payload: PredictiveETAEstimateCreateSchema):
    """Create new PredictiveETAEstimate instance in enterprise repository."""
    svc = PredictiveETAEstimateService()
    try:
        item = svc.create_predictiveetaestimate(
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

@router.put("/predictiveetaestimates/{item_id}", response_model=Dict[str, Any])
def update_predictiveetaestimate(item_id: int, payload: PredictiveETAEstimateUpdateSchema):
    """Update existing PredictiveETAEstimate record fields."""
    svc = PredictiveETAEstimateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_predictiveetaestimate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PredictiveETAEstimate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/predictiveetaestimates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_predictiveetaestimate(item_id: int, hard: bool = Query(False)):
    """Delete PredictiveETAEstimate record (soft-delete by default)."""
    svc = PredictiveETAEstimateService()
    ok = svc.delete_predictiveetaestimate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PredictiveETAEstimate with ID {item_id} not found")
    return None

@router.get("/predictiveetaestimates/analytics/metrics", response_model=Dict[str, Any])
def get_predictiveetaestimate_metrics():
    """Calculate summary statistical KPIs for PredictiveETAEstimate collection."""
    svc = PredictiveETAEstimateService()
    return svc.calculate_aggregate_metrics()

# ==================== CarbonEmissionWaypoint Endpoints ====================
@router.get("/carbonemissionwaypoints", response_model=List[Dict[str, Any]])
def list_carbonemissionwaypoints(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CarbonEmissionWaypoint records with pagination and filtering."""
    svc = CarbonEmissionWaypointService()
    items = svc.list_carbonemissionwaypoints(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/carbonemissionwaypoints/{item_id}", response_model=Dict[str, Any])
def get_carbonemissionwaypoint_by_id(item_id: int):
    """Retrieve detailed record for CarbonEmissionWaypoint by ID."""
    svc = CarbonEmissionWaypointService()
    item = svc.get_carbonemissionwaypoint_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CarbonEmissionWaypoint with ID {item_id} not found")
    return item.to_dict()

@router.post("/carbonemissionwaypoints", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_carbonemissionwaypoint(payload: CarbonEmissionWaypointCreateSchema):
    """Create new CarbonEmissionWaypoint instance in enterprise repository."""
    svc = CarbonEmissionWaypointService()
    try:
        item = svc.create_carbonemissionwaypoint(
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

@router.put("/carbonemissionwaypoints/{item_id}", response_model=Dict[str, Any])
def update_carbonemissionwaypoint(item_id: int, payload: CarbonEmissionWaypointUpdateSchema):
    """Update existing CarbonEmissionWaypoint record fields."""
    svc = CarbonEmissionWaypointService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_carbonemissionwaypoint(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CarbonEmissionWaypoint with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/carbonemissionwaypoints/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carbonemissionwaypoint(item_id: int, hard: bool = Query(False)):
    """Delete CarbonEmissionWaypoint record (soft-delete by default)."""
    svc = CarbonEmissionWaypointService()
    ok = svc.delete_carbonemissionwaypoint(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CarbonEmissionWaypoint with ID {item_id} not found")
    return None

@router.get("/carbonemissionwaypoints/analytics/metrics", response_model=Dict[str, Any])
def get_carbonemissionwaypoint_metrics():
    """Calculate summary statistical KPIs for CarbonEmissionWaypoint collection."""
    svc = CarbonEmissionWaypointService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomsClearanceMilestone Endpoints ====================
@router.get("/customsclearancemilestones", response_model=List[Dict[str, Any]])
def list_customsclearancemilestones(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomsClearanceMilestone records with pagination and filtering."""
    svc = CustomsClearanceMilestoneService()
    items = svc.list_customsclearancemilestones(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customsclearancemilestones/{item_id}", response_model=Dict[str, Any])
def get_customsclearancemilestone_by_id(item_id: int):
    """Retrieve detailed record for CustomsClearanceMilestone by ID."""
    svc = CustomsClearanceMilestoneService()
    item = svc.get_customsclearancemilestone_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomsClearanceMilestone with ID {item_id} not found")
    return item.to_dict()

@router.post("/customsclearancemilestones", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customsclearancemilestone(payload: CustomsClearanceMilestoneCreateSchema):
    """Create new CustomsClearanceMilestone instance in enterprise repository."""
    svc = CustomsClearanceMilestoneService()
    try:
        item = svc.create_customsclearancemilestone(
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

@router.put("/customsclearancemilestones/{item_id}", response_model=Dict[str, Any])
def update_customsclearancemilestone(item_id: int, payload: CustomsClearanceMilestoneUpdateSchema):
    """Update existing CustomsClearanceMilestone record fields."""
    svc = CustomsClearanceMilestoneService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customsclearancemilestone(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomsClearanceMilestone with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customsclearancemilestones/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customsclearancemilestone(item_id: int, hard: bool = Query(False)):
    """Delete CustomsClearanceMilestone record (soft-delete by default)."""
    svc = CustomsClearanceMilestoneService()
    ok = svc.delete_customsclearancemilestone(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomsClearanceMilestone with ID {item_id} not found")
    return None

@router.get("/customsclearancemilestones/analytics/metrics", response_model=Dict[str, Any])
def get_customsclearancemilestone_metrics():
    """Calculate summary statistical KPIs for CustomsClearanceMilestone collection."""
    svc = CustomsClearanceMilestoneService()
    return svc.calculate_aggregate_metrics()

# ==================== TamperEvidentIncident Endpoints ====================
@router.get("/tamperevidentincidents", response_model=List[Dict[str, Any]])
def list_tamperevidentincidents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TamperEvidentIncident records with pagination and filtering."""
    svc = TamperEvidentIncidentService()
    items = svc.list_tamperevidentincidents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tamperevidentincidents/{item_id}", response_model=Dict[str, Any])
def get_tamperevidentincident_by_id(item_id: int):
    """Retrieve detailed record for TamperEvidentIncident by ID."""
    svc = TamperEvidentIncidentService()
    item = svc.get_tamperevidentincident_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TamperEvidentIncident with ID {item_id} not found")
    return item.to_dict()

@router.post("/tamperevidentincidents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tamperevidentincident(payload: TamperEvidentIncidentCreateSchema):
    """Create new TamperEvidentIncident instance in enterprise repository."""
    svc = TamperEvidentIncidentService()
    try:
        item = svc.create_tamperevidentincident(
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

@router.put("/tamperevidentincidents/{item_id}", response_model=Dict[str, Any])
def update_tamperevidentincident(item_id: int, payload: TamperEvidentIncidentUpdateSchema):
    """Update existing TamperEvidentIncident record fields."""
    svc = TamperEvidentIncidentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tamperevidentincident(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TamperEvidentIncident with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tamperevidentincidents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tamperevidentincident(item_id: int, hard: bool = Query(False)):
    """Delete TamperEvidentIncident record (soft-delete by default)."""
    svc = TamperEvidentIncidentService()
    ok = svc.delete_tamperevidentincident(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TamperEvidentIncident with ID {item_id} not found")
    return None

@router.get("/tamperevidentincidents/analytics/metrics", response_model=Dict[str, Any])
def get_tamperevidentincident_metrics():
    """Calculate summary statistical KPIs for TamperEvidentIncident collection."""
    svc = TamperEvidentIncidentService()
    return svc.calculate_aggregate_metrics()

# ==================== WeatherDisruptionAlert Endpoints ====================
@router.get("/weatherdisruptionalerts", response_model=List[Dict[str, Any]])
def list_weatherdisruptionalerts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WeatherDisruptionAlert records with pagination and filtering."""
    svc = WeatherDisruptionAlertService()
    items = svc.list_weatherdisruptionalerts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/weatherdisruptionalerts/{item_id}", response_model=Dict[str, Any])
def get_weatherdisruptionalert_by_id(item_id: int):
    """Retrieve detailed record for WeatherDisruptionAlert by ID."""
    svc = WeatherDisruptionAlertService()
    item = svc.get_weatherdisruptionalert_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WeatherDisruptionAlert with ID {item_id} not found")
    return item.to_dict()

@router.post("/weatherdisruptionalerts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_weatherdisruptionalert(payload: WeatherDisruptionAlertCreateSchema):
    """Create new WeatherDisruptionAlert instance in enterprise repository."""
    svc = WeatherDisruptionAlertService()
    try:
        item = svc.create_weatherdisruptionalert(
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

@router.put("/weatherdisruptionalerts/{item_id}", response_model=Dict[str, Any])
def update_weatherdisruptionalert(item_id: int, payload: WeatherDisruptionAlertUpdateSchema):
    """Update existing WeatherDisruptionAlert record fields."""
    svc = WeatherDisruptionAlertService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_weatherdisruptionalert(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WeatherDisruptionAlert with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/weatherdisruptionalerts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_weatherdisruptionalert(item_id: int, hard: bool = Query(False)):
    """Delete WeatherDisruptionAlert record (soft-delete by default)."""
    svc = WeatherDisruptionAlertService()
    ok = svc.delete_weatherdisruptionalert(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WeatherDisruptionAlert with ID {item_id} not found")
    return None

@router.get("/weatherdisruptionalerts/analytics/metrics", response_model=Dict[str, Any])
def get_weatherdisruptionalert_metrics():
    """Calculate summary statistical KPIs for WeatherDisruptionAlert collection."""
    svc = WeatherDisruptionAlertService()
    return svc.calculate_aggregate_metrics()

# ==================== MultimodalHandoverNote Endpoints ====================
@router.get("/multimodalhandovernotes", response_model=List[Dict[str, Any]])
def list_multimodalhandovernotes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MultimodalHandoverNote records with pagination and filtering."""
    svc = MultimodalHandoverNoteService()
    items = svc.list_multimodalhandovernotes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/multimodalhandovernotes/{item_id}", response_model=Dict[str, Any])
def get_multimodalhandovernote_by_id(item_id: int):
    """Retrieve detailed record for MultimodalHandoverNote by ID."""
    svc = MultimodalHandoverNoteService()
    item = svc.get_multimodalhandovernote_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MultimodalHandoverNote with ID {item_id} not found")
    return item.to_dict()

@router.post("/multimodalhandovernotes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_multimodalhandovernote(payload: MultimodalHandoverNoteCreateSchema):
    """Create new MultimodalHandoverNote instance in enterprise repository."""
    svc = MultimodalHandoverNoteService()
    try:
        item = svc.create_multimodalhandovernote(
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

@router.put("/multimodalhandovernotes/{item_id}", response_model=Dict[str, Any])
def update_multimodalhandovernote(item_id: int, payload: MultimodalHandoverNoteUpdateSchema):
    """Update existing MultimodalHandoverNote record fields."""
    svc = MultimodalHandoverNoteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_multimodalhandovernote(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MultimodalHandoverNote with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/multimodalhandovernotes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_multimodalhandovernote(item_id: int, hard: bool = Query(False)):
    """Delete MultimodalHandoverNote record (soft-delete by default)."""
    svc = MultimodalHandoverNoteService()
    ok = svc.delete_multimodalhandovernote(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MultimodalHandoverNote with ID {item_id} not found")
    return None

@router.get("/multimodalhandovernotes/analytics/metrics", response_model=Dict[str, Any])
def get_multimodalhandovernote_metrics():
    """Calculate summary statistical KPIs for MultimodalHandoverNote collection."""
    svc = MultimodalHandoverNoteService()
    return svc.calculate_aggregate_metrics()

# ==================== TrackAndTraceAuditLog Endpoints ====================
@router.get("/trackandtraceauditlogs", response_model=List[Dict[str, Any]])
def list_trackandtraceauditlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TrackAndTraceAuditLog records with pagination and filtering."""
    svc = TrackAndTraceAuditLogService()
    items = svc.list_trackandtraceauditlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/trackandtraceauditlogs/{item_id}", response_model=Dict[str, Any])
def get_trackandtraceauditlog_by_id(item_id: int):
    """Retrieve detailed record for TrackAndTraceAuditLog by ID."""
    svc = TrackAndTraceAuditLogService()
    item = svc.get_trackandtraceauditlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TrackAndTraceAuditLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/trackandtraceauditlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_trackandtraceauditlog(payload: TrackAndTraceAuditLogCreateSchema):
    """Create new TrackAndTraceAuditLog instance in enterprise repository."""
    svc = TrackAndTraceAuditLogService()
    try:
        item = svc.create_trackandtraceauditlog(
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

@router.put("/trackandtraceauditlogs/{item_id}", response_model=Dict[str, Any])
def update_trackandtraceauditlog(item_id: int, payload: TrackAndTraceAuditLogUpdateSchema):
    """Update existing TrackAndTraceAuditLog record fields."""
    svc = TrackAndTraceAuditLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_trackandtraceauditlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TrackAndTraceAuditLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/trackandtraceauditlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trackandtraceauditlog(item_id: int, hard: bool = Query(False)):
    """Delete TrackAndTraceAuditLog record (soft-delete by default)."""
    svc = TrackAndTraceAuditLogService()
    ok = svc.delete_trackandtraceauditlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TrackAndTraceAuditLog with ID {item_id} not found")
    return None

@router.get("/trackandtraceauditlogs/analytics/metrics", response_model=Dict[str, Any])
def get_trackandtraceauditlog_metrics():
    """Calculate summary statistical KPIs for TrackAndTraceAuditLog collection."""
    svc = TrackAndTraceAuditLogService()
    return svc.calculate_aggregate_metrics()

