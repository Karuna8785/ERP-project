"""
Supply Chain & Fleet Logistics - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ShipmentService,
    CarrierService,
    RouteService,
    VehicleService,
    DriverService,
    DeliveryStopService,
    FreightBillService,
    WaybillService,
    ContainerService,
    DispatchOrderService,
    FuelLogService,
    TollReceiptService,
    MaintenanceLogService,
    GPSPingService,
    DockScheduleService,
    CustomsDocService,
)
from .schemas import (
    ShipmentCreateSchema, ShipmentUpdateSchema, ShipmentResponseSchema,
    CarrierCreateSchema, CarrierUpdateSchema, CarrierResponseSchema,
    RouteCreateSchema, RouteUpdateSchema, RouteResponseSchema,
    VehicleCreateSchema, VehicleUpdateSchema, VehicleResponseSchema,
    DriverCreateSchema, DriverUpdateSchema, DriverResponseSchema,
    DeliveryStopCreateSchema, DeliveryStopUpdateSchema, DeliveryStopResponseSchema,
    FreightBillCreateSchema, FreightBillUpdateSchema, FreightBillResponseSchema,
    WaybillCreateSchema, WaybillUpdateSchema, WaybillResponseSchema,
    ContainerCreateSchema, ContainerUpdateSchema, ContainerResponseSchema,
    DispatchOrderCreateSchema, DispatchOrderUpdateSchema, DispatchOrderResponseSchema,
    FuelLogCreateSchema, FuelLogUpdateSchema, FuelLogResponseSchema,
    TollReceiptCreateSchema, TollReceiptUpdateSchema, TollReceiptResponseSchema,
    MaintenanceLogCreateSchema, MaintenanceLogUpdateSchema, MaintenanceLogResponseSchema,
    GPSPingCreateSchema, GPSPingUpdateSchema, GPSPingResponseSchema,
    DockScheduleCreateSchema, DockScheduleUpdateSchema, DockScheduleResponseSchema,
    CustomsDocCreateSchema, CustomsDocUpdateSchema, CustomsDocResponseSchema,
)

router = APIRouter(prefix="/logistics", tags=["Supply Chain & Fleet Logistics"])

# ==================== Shipment Endpoints ====================
@router.get("/shipments", response_model=List[Dict[str, Any]])
def list_shipments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Shipment records with pagination and filtering."""
    svc = ShipmentService()
    items = svc.list_shipments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shipments/{item_id}", response_model=Dict[str, Any])
def get_shipment_by_id(item_id: int):
    """Retrieve detailed record for Shipment by ID."""
    svc = ShipmentService()
    item = svc.get_shipment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Shipment with ID {item_id} not found")
    return item.to_dict()

@router.post("/shipments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shipment(payload: ShipmentCreateSchema):
    """Create new Shipment instance in enterprise repository."""
    svc = ShipmentService()
    try:
        item = svc.create_shipment(
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

@router.put("/shipments/{item_id}", response_model=Dict[str, Any])
def update_shipment(item_id: int, payload: ShipmentUpdateSchema):
    """Update existing Shipment record fields."""
    svc = ShipmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shipment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Shipment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shipments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shipment(item_id: int, hard: bool = Query(False)):
    """Delete Shipment record (soft-delete by default)."""
    svc = ShipmentService()
    ok = svc.delete_shipment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Shipment with ID {item_id} not found")
    return None

@router.get("/shipments/analytics/metrics", response_model=Dict[str, Any])
def get_shipment_metrics():
    """Calculate summary statistical KPIs for Shipment collection."""
    svc = ShipmentService()
    return svc.calculate_aggregate_metrics()

# ==================== Carrier Endpoints ====================
@router.get("/carriers", response_model=List[Dict[str, Any]])
def list_carriers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Carrier records with pagination and filtering."""
    svc = CarrierService()
    items = svc.list_carriers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/carriers/{item_id}", response_model=Dict[str, Any])
def get_carrier_by_id(item_id: int):
    """Retrieve detailed record for Carrier by ID."""
    svc = CarrierService()
    item = svc.get_carrier_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Carrier with ID {item_id} not found")
    return item.to_dict()

@router.post("/carriers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_carrier(payload: CarrierCreateSchema):
    """Create new Carrier instance in enterprise repository."""
    svc = CarrierService()
    try:
        item = svc.create_carrier(
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

@router.put("/carriers/{item_id}", response_model=Dict[str, Any])
def update_carrier(item_id: int, payload: CarrierUpdateSchema):
    """Update existing Carrier record fields."""
    svc = CarrierService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_carrier(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Carrier with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/carriers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrier(item_id: int, hard: bool = Query(False)):
    """Delete Carrier record (soft-delete by default)."""
    svc = CarrierService()
    ok = svc.delete_carrier(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Carrier with ID {item_id} not found")
    return None

@router.get("/carriers/analytics/metrics", response_model=Dict[str, Any])
def get_carrier_metrics():
    """Calculate summary statistical KPIs for Carrier collection."""
    svc = CarrierService()
    return svc.calculate_aggregate_metrics()

# ==================== Route Endpoints ====================
@router.get("/routes", response_model=List[Dict[str, Any]])
def list_routes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Route records with pagination and filtering."""
    svc = RouteService()
    items = svc.list_routes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/routes/{item_id}", response_model=Dict[str, Any])
def get_route_by_id(item_id: int):
    """Retrieve detailed record for Route by ID."""
    svc = RouteService()
    item = svc.get_route_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Route with ID {item_id} not found")
    return item.to_dict()

@router.post("/routes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_route(payload: RouteCreateSchema):
    """Create new Route instance in enterprise repository."""
    svc = RouteService()
    try:
        item = svc.create_route(
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

@router.put("/routes/{item_id}", response_model=Dict[str, Any])
def update_route(item_id: int, payload: RouteUpdateSchema):
    """Update existing Route record fields."""
    svc = RouteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_route(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Route with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/routes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_route(item_id: int, hard: bool = Query(False)):
    """Delete Route record (soft-delete by default)."""
    svc = RouteService()
    ok = svc.delete_route(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Route with ID {item_id} not found")
    return None

@router.get("/routes/analytics/metrics", response_model=Dict[str, Any])
def get_route_metrics():
    """Calculate summary statistical KPIs for Route collection."""
    svc = RouteService()
    return svc.calculate_aggregate_metrics()

# ==================== Vehicle Endpoints ====================
@router.get("/vehicles", response_model=List[Dict[str, Any]])
def list_vehicles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Vehicle records with pagination and filtering."""
    svc = VehicleService()
    items = svc.list_vehicles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vehicles/{item_id}", response_model=Dict[str, Any])
def get_vehicle_by_id(item_id: int):
    """Retrieve detailed record for Vehicle by ID."""
    svc = VehicleService()
    item = svc.get_vehicle_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Vehicle with ID {item_id} not found")
    return item.to_dict()

@router.post("/vehicles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vehicle(payload: VehicleCreateSchema):
    """Create new Vehicle instance in enterprise repository."""
    svc = VehicleService()
    try:
        item = svc.create_vehicle(
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

@router.put("/vehicles/{item_id}", response_model=Dict[str, Any])
def update_vehicle(item_id: int, payload: VehicleUpdateSchema):
    """Update existing Vehicle record fields."""
    svc = VehicleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vehicle(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Vehicle with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vehicles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(item_id: int, hard: bool = Query(False)):
    """Delete Vehicle record (soft-delete by default)."""
    svc = VehicleService()
    ok = svc.delete_vehicle(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Vehicle with ID {item_id} not found")
    return None

@router.get("/vehicles/analytics/metrics", response_model=Dict[str, Any])
def get_vehicle_metrics():
    """Calculate summary statistical KPIs for Vehicle collection."""
    svc = VehicleService()
    return svc.calculate_aggregate_metrics()

# ==================== Driver Endpoints ====================
@router.get("/drivers", response_model=List[Dict[str, Any]])
def list_drivers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Driver records with pagination and filtering."""
    svc = DriverService()
    items = svc.list_drivers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/drivers/{item_id}", response_model=Dict[str, Any])
def get_driver_by_id(item_id: int):
    """Retrieve detailed record for Driver by ID."""
    svc = DriverService()
    item = svc.get_driver_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Driver with ID {item_id} not found")
    return item.to_dict()

@router.post("/drivers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_driver(payload: DriverCreateSchema):
    """Create new Driver instance in enterprise repository."""
    svc = DriverService()
    try:
        item = svc.create_driver(
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

@router.put("/drivers/{item_id}", response_model=Dict[str, Any])
def update_driver(item_id: int, payload: DriverUpdateSchema):
    """Update existing Driver record fields."""
    svc = DriverService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_driver(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Driver with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/drivers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_driver(item_id: int, hard: bool = Query(False)):
    """Delete Driver record (soft-delete by default)."""
    svc = DriverService()
    ok = svc.delete_driver(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Driver with ID {item_id} not found")
    return None

@router.get("/drivers/analytics/metrics", response_model=Dict[str, Any])
def get_driver_metrics():
    """Calculate summary statistical KPIs for Driver collection."""
    svc = DriverService()
    return svc.calculate_aggregate_metrics()

# ==================== DeliveryStop Endpoints ====================
@router.get("/deliverystops", response_model=List[Dict[str, Any]])
def list_deliverystops(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeliveryStop records with pagination and filtering."""
    svc = DeliveryStopService()
    items = svc.list_deliverystops(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/deliverystops/{item_id}", response_model=Dict[str, Any])
def get_deliverystop_by_id(item_id: int):
    """Retrieve detailed record for DeliveryStop by ID."""
    svc = DeliveryStopService()
    item = svc.get_deliverystop_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeliveryStop with ID {item_id} not found")
    return item.to_dict()

@router.post("/deliverystops", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_deliverystop(payload: DeliveryStopCreateSchema):
    """Create new DeliveryStop instance in enterprise repository."""
    svc = DeliveryStopService()
    try:
        item = svc.create_deliverystop(
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

@router.put("/deliverystops/{item_id}", response_model=Dict[str, Any])
def update_deliverystop(item_id: int, payload: DeliveryStopUpdateSchema):
    """Update existing DeliveryStop record fields."""
    svc = DeliveryStopService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_deliverystop(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeliveryStop with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/deliverystops/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deliverystop(item_id: int, hard: bool = Query(False)):
    """Delete DeliveryStop record (soft-delete by default)."""
    svc = DeliveryStopService()
    ok = svc.delete_deliverystop(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeliveryStop with ID {item_id} not found")
    return None

@router.get("/deliverystops/analytics/metrics", response_model=Dict[str, Any])
def get_deliverystop_metrics():
    """Calculate summary statistical KPIs for DeliveryStop collection."""
    svc = DeliveryStopService()
    return svc.calculate_aggregate_metrics()

# ==================== FreightBill Endpoints ====================
@router.get("/freightbills", response_model=List[Dict[str, Any]])
def list_freightbills(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FreightBill records with pagination and filtering."""
    svc = FreightBillService()
    items = svc.list_freightbills(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/freightbills/{item_id}", response_model=Dict[str, Any])
def get_freightbill_by_id(item_id: int):
    """Retrieve detailed record for FreightBill by ID."""
    svc = FreightBillService()
    item = svc.get_freightbill_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FreightBill with ID {item_id} not found")
    return item.to_dict()

@router.post("/freightbills", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_freightbill(payload: FreightBillCreateSchema):
    """Create new FreightBill instance in enterprise repository."""
    svc = FreightBillService()
    try:
        item = svc.create_freightbill(
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

@router.put("/freightbills/{item_id}", response_model=Dict[str, Any])
def update_freightbill(item_id: int, payload: FreightBillUpdateSchema):
    """Update existing FreightBill record fields."""
    svc = FreightBillService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_freightbill(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FreightBill with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/freightbills/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_freightbill(item_id: int, hard: bool = Query(False)):
    """Delete FreightBill record (soft-delete by default)."""
    svc = FreightBillService()
    ok = svc.delete_freightbill(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FreightBill with ID {item_id} not found")
    return None

@router.get("/freightbills/analytics/metrics", response_model=Dict[str, Any])
def get_freightbill_metrics():
    """Calculate summary statistical KPIs for FreightBill collection."""
    svc = FreightBillService()
    return svc.calculate_aggregate_metrics()

# ==================== Waybill Endpoints ====================
@router.get("/waybills", response_model=List[Dict[str, Any]])
def list_waybills(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Waybill records with pagination and filtering."""
    svc = WaybillService()
    items = svc.list_waybills(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/waybills/{item_id}", response_model=Dict[str, Any])
def get_waybill_by_id(item_id: int):
    """Retrieve detailed record for Waybill by ID."""
    svc = WaybillService()
    item = svc.get_waybill_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Waybill with ID {item_id} not found")
    return item.to_dict()

@router.post("/waybills", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_waybill(payload: WaybillCreateSchema):
    """Create new Waybill instance in enterprise repository."""
    svc = WaybillService()
    try:
        item = svc.create_waybill(
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

@router.put("/waybills/{item_id}", response_model=Dict[str, Any])
def update_waybill(item_id: int, payload: WaybillUpdateSchema):
    """Update existing Waybill record fields."""
    svc = WaybillService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_waybill(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Waybill with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/waybills/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_waybill(item_id: int, hard: bool = Query(False)):
    """Delete Waybill record (soft-delete by default)."""
    svc = WaybillService()
    ok = svc.delete_waybill(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Waybill with ID {item_id} not found")
    return None

@router.get("/waybills/analytics/metrics", response_model=Dict[str, Any])
def get_waybill_metrics():
    """Calculate summary statistical KPIs for Waybill collection."""
    svc = WaybillService()
    return svc.calculate_aggregate_metrics()

# ==================== Container Endpoints ====================
@router.get("/containers", response_model=List[Dict[str, Any]])
def list_containers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Container records with pagination and filtering."""
    svc = ContainerService()
    items = svc.list_containers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/containers/{item_id}", response_model=Dict[str, Any])
def get_container_by_id(item_id: int):
    """Retrieve detailed record for Container by ID."""
    svc = ContainerService()
    item = svc.get_container_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Container with ID {item_id} not found")
    return item.to_dict()

@router.post("/containers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_container(payload: ContainerCreateSchema):
    """Create new Container instance in enterprise repository."""
    svc = ContainerService()
    try:
        item = svc.create_container(
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

@router.put("/containers/{item_id}", response_model=Dict[str, Any])
def update_container(item_id: int, payload: ContainerUpdateSchema):
    """Update existing Container record fields."""
    svc = ContainerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_container(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Container with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/containers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_container(item_id: int, hard: bool = Query(False)):
    """Delete Container record (soft-delete by default)."""
    svc = ContainerService()
    ok = svc.delete_container(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Container with ID {item_id} not found")
    return None

@router.get("/containers/analytics/metrics", response_model=Dict[str, Any])
def get_container_metrics():
    """Calculate summary statistical KPIs for Container collection."""
    svc = ContainerService()
    return svc.calculate_aggregate_metrics()

# ==================== DispatchOrder Endpoints ====================
@router.get("/dispatchorders", response_model=List[Dict[str, Any]])
def list_dispatchorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DispatchOrder records with pagination and filtering."""
    svc = DispatchOrderService()
    items = svc.list_dispatchorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dispatchorders/{item_id}", response_model=Dict[str, Any])
def get_dispatchorder_by_id(item_id: int):
    """Retrieve detailed record for DispatchOrder by ID."""
    svc = DispatchOrderService()
    item = svc.get_dispatchorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DispatchOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/dispatchorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dispatchorder(payload: DispatchOrderCreateSchema):
    """Create new DispatchOrder instance in enterprise repository."""
    svc = DispatchOrderService()
    try:
        item = svc.create_dispatchorder(
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

@router.put("/dispatchorders/{item_id}", response_model=Dict[str, Any])
def update_dispatchorder(item_id: int, payload: DispatchOrderUpdateSchema):
    """Update existing DispatchOrder record fields."""
    svc = DispatchOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dispatchorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DispatchOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dispatchorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dispatchorder(item_id: int, hard: bool = Query(False)):
    """Delete DispatchOrder record (soft-delete by default)."""
    svc = DispatchOrderService()
    ok = svc.delete_dispatchorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DispatchOrder with ID {item_id} not found")
    return None

@router.get("/dispatchorders/analytics/metrics", response_model=Dict[str, Any])
def get_dispatchorder_metrics():
    """Calculate summary statistical KPIs for DispatchOrder collection."""
    svc = DispatchOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== FuelLog Endpoints ====================
@router.get("/fuellogs", response_model=List[Dict[str, Any]])
def list_fuellogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FuelLog records with pagination and filtering."""
    svc = FuelLogService()
    items = svc.list_fuellogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fuellogs/{item_id}", response_model=Dict[str, Any])
def get_fuellog_by_id(item_id: int):
    """Retrieve detailed record for FuelLog by ID."""
    svc = FuelLogService()
    item = svc.get_fuellog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FuelLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/fuellogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fuellog(payload: FuelLogCreateSchema):
    """Create new FuelLog instance in enterprise repository."""
    svc = FuelLogService()
    try:
        item = svc.create_fuellog(
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

@router.put("/fuellogs/{item_id}", response_model=Dict[str, Any])
def update_fuellog(item_id: int, payload: FuelLogUpdateSchema):
    """Update existing FuelLog record fields."""
    svc = FuelLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fuellog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FuelLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fuellogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fuellog(item_id: int, hard: bool = Query(False)):
    """Delete FuelLog record (soft-delete by default)."""
    svc = FuelLogService()
    ok = svc.delete_fuellog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FuelLog with ID {item_id} not found")
    return None

@router.get("/fuellogs/analytics/metrics", response_model=Dict[str, Any])
def get_fuellog_metrics():
    """Calculate summary statistical KPIs for FuelLog collection."""
    svc = FuelLogService()
    return svc.calculate_aggregate_metrics()

# ==================== TollReceipt Endpoints ====================
@router.get("/tollreceipts", response_model=List[Dict[str, Any]])
def list_tollreceipts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TollReceipt records with pagination and filtering."""
    svc = TollReceiptService()
    items = svc.list_tollreceipts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tollreceipts/{item_id}", response_model=Dict[str, Any])
def get_tollreceipt_by_id(item_id: int):
    """Retrieve detailed record for TollReceipt by ID."""
    svc = TollReceiptService()
    item = svc.get_tollreceipt_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TollReceipt with ID {item_id} not found")
    return item.to_dict()

@router.post("/tollreceipts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tollreceipt(payload: TollReceiptCreateSchema):
    """Create new TollReceipt instance in enterprise repository."""
    svc = TollReceiptService()
    try:
        item = svc.create_tollreceipt(
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

@router.put("/tollreceipts/{item_id}", response_model=Dict[str, Any])
def update_tollreceipt(item_id: int, payload: TollReceiptUpdateSchema):
    """Update existing TollReceipt record fields."""
    svc = TollReceiptService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tollreceipt(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TollReceipt with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tollreceipts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tollreceipt(item_id: int, hard: bool = Query(False)):
    """Delete TollReceipt record (soft-delete by default)."""
    svc = TollReceiptService()
    ok = svc.delete_tollreceipt(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TollReceipt with ID {item_id} not found")
    return None

@router.get("/tollreceipts/analytics/metrics", response_model=Dict[str, Any])
def get_tollreceipt_metrics():
    """Calculate summary statistical KPIs for TollReceipt collection."""
    svc = TollReceiptService()
    return svc.calculate_aggregate_metrics()

# ==================== MaintenanceLog Endpoints ====================
@router.get("/maintenancelogs", response_model=List[Dict[str, Any]])
def list_maintenancelogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaintenanceLog records with pagination and filtering."""
    svc = MaintenanceLogService()
    items = svc.list_maintenancelogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/maintenancelogs/{item_id}", response_model=Dict[str, Any])
def get_maintenancelog_by_id(item_id: int):
    """Retrieve detailed record for MaintenanceLog by ID."""
    svc = MaintenanceLogService()
    item = svc.get_maintenancelog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaintenanceLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/maintenancelogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_maintenancelog(payload: MaintenanceLogCreateSchema):
    """Create new MaintenanceLog instance in enterprise repository."""
    svc = MaintenanceLogService()
    try:
        item = svc.create_maintenancelog(
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

@router.put("/maintenancelogs/{item_id}", response_model=Dict[str, Any])
def update_maintenancelog(item_id: int, payload: MaintenanceLogUpdateSchema):
    """Update existing MaintenanceLog record fields."""
    svc = MaintenanceLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_maintenancelog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaintenanceLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/maintenancelogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenancelog(item_id: int, hard: bool = Query(False)):
    """Delete MaintenanceLog record (soft-delete by default)."""
    svc = MaintenanceLogService()
    ok = svc.delete_maintenancelog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaintenanceLog with ID {item_id} not found")
    return None

@router.get("/maintenancelogs/analytics/metrics", response_model=Dict[str, Any])
def get_maintenancelog_metrics():
    """Calculate summary statistical KPIs for MaintenanceLog collection."""
    svc = MaintenanceLogService()
    return svc.calculate_aggregate_metrics()

# ==================== GPSPing Endpoints ====================
@router.get("/gpspings", response_model=List[Dict[str, Any]])
def list_gpspings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GPSPing records with pagination and filtering."""
    svc = GPSPingService()
    items = svc.list_gpspings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/gpspings/{item_id}", response_model=Dict[str, Any])
def get_gpsping_by_id(item_id: int):
    """Retrieve detailed record for GPSPing by ID."""
    svc = GPSPingService()
    item = svc.get_gpsping_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GPSPing with ID {item_id} not found")
    return item.to_dict()

@router.post("/gpspings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_gpsping(payload: GPSPingCreateSchema):
    """Create new GPSPing instance in enterprise repository."""
    svc = GPSPingService()
    try:
        item = svc.create_gpsping(
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

@router.put("/gpspings/{item_id}", response_model=Dict[str, Any])
def update_gpsping(item_id: int, payload: GPSPingUpdateSchema):
    """Update existing GPSPing record fields."""
    svc = GPSPingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_gpsping(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GPSPing with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/gpspings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gpsping(item_id: int, hard: bool = Query(False)):
    """Delete GPSPing record (soft-delete by default)."""
    svc = GPSPingService()
    ok = svc.delete_gpsping(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GPSPing with ID {item_id} not found")
    return None

@router.get("/gpspings/analytics/metrics", response_model=Dict[str, Any])
def get_gpsping_metrics():
    """Calculate summary statistical KPIs for GPSPing collection."""
    svc = GPSPingService()
    return svc.calculate_aggregate_metrics()

# ==================== DockSchedule Endpoints ====================
@router.get("/dockschedules", response_model=List[Dict[str, Any]])
def list_dockschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DockSchedule records with pagination and filtering."""
    svc = DockScheduleService()
    items = svc.list_dockschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dockschedules/{item_id}", response_model=Dict[str, Any])
def get_dockschedule_by_id(item_id: int):
    """Retrieve detailed record for DockSchedule by ID."""
    svc = DockScheduleService()
    item = svc.get_dockschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DockSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/dockschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dockschedule(payload: DockScheduleCreateSchema):
    """Create new DockSchedule instance in enterprise repository."""
    svc = DockScheduleService()
    try:
        item = svc.create_dockschedule(
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

@router.put("/dockschedules/{item_id}", response_model=Dict[str, Any])
def update_dockschedule(item_id: int, payload: DockScheduleUpdateSchema):
    """Update existing DockSchedule record fields."""
    svc = DockScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dockschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DockSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dockschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dockschedule(item_id: int, hard: bool = Query(False)):
    """Delete DockSchedule record (soft-delete by default)."""
    svc = DockScheduleService()
    ok = svc.delete_dockschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DockSchedule with ID {item_id} not found")
    return None

@router.get("/dockschedules/analytics/metrics", response_model=Dict[str, Any])
def get_dockschedule_metrics():
    """Calculate summary statistical KPIs for DockSchedule collection."""
    svc = DockScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomsDoc Endpoints ====================
@router.get("/customsdocs", response_model=List[Dict[str, Any]])
def list_customsdocs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomsDoc records with pagination and filtering."""
    svc = CustomsDocService()
    items = svc.list_customsdocs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customsdocs/{item_id}", response_model=Dict[str, Any])
def get_customsdoc_by_id(item_id: int):
    """Retrieve detailed record for CustomsDoc by ID."""
    svc = CustomsDocService()
    item = svc.get_customsdoc_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomsDoc with ID {item_id} not found")
    return item.to_dict()

@router.post("/customsdocs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customsdoc(payload: CustomsDocCreateSchema):
    """Create new CustomsDoc instance in enterprise repository."""
    svc = CustomsDocService()
    try:
        item = svc.create_customsdoc(
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

@router.put("/customsdocs/{item_id}", response_model=Dict[str, Any])
def update_customsdoc(item_id: int, payload: CustomsDocUpdateSchema):
    """Update existing CustomsDoc record fields."""
    svc = CustomsDocService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customsdoc(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomsDoc with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customsdocs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customsdoc(item_id: int, hard: bool = Query(False)):
    """Delete CustomsDoc record (soft-delete by default)."""
    svc = CustomsDocService()
    ok = svc.delete_customsdoc(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomsDoc with ID {item_id} not found")
    return None

@router.get("/customsdocs/analytics/metrics", response_model=Dict[str, Any])
def get_customsdoc_metrics():
    """Calculate summary statistical KPIs for CustomsDoc collection."""
    svc = CustomsDocService()
    return svc.calculate_aggregate_metrics()

