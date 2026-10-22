"""
Advanced Warehouse Management (WMS) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    WarehouseZoneService,
    StorageAisleService,
    RackBinLocationService,
    StockPalletService,
    WavePickingPlanService,
    PutawayTaskService,
    CycleCountSheetService,
    BinTransferOrderService,
    CrossDockRouteService,
    LPNTagService,
    PackagingStationService,
    DockDoorAssignmentService,
    KittingOrderService,
    DeKittingJobService,
    HazardClassificationService,
    TempLogRecordService,
)
from .schemas import (
    WarehouseZoneCreateSchema, WarehouseZoneUpdateSchema, WarehouseZoneResponseSchema,
    StorageAisleCreateSchema, StorageAisleUpdateSchema, StorageAisleResponseSchema,
    RackBinLocationCreateSchema, RackBinLocationUpdateSchema, RackBinLocationResponseSchema,
    StockPalletCreateSchema, StockPalletUpdateSchema, StockPalletResponseSchema,
    WavePickingPlanCreateSchema, WavePickingPlanUpdateSchema, WavePickingPlanResponseSchema,
    PutawayTaskCreateSchema, PutawayTaskUpdateSchema, PutawayTaskResponseSchema,
    CycleCountSheetCreateSchema, CycleCountSheetUpdateSchema, CycleCountSheetResponseSchema,
    BinTransferOrderCreateSchema, BinTransferOrderUpdateSchema, BinTransferOrderResponseSchema,
    CrossDockRouteCreateSchema, CrossDockRouteUpdateSchema, CrossDockRouteResponseSchema,
    LPNTagCreateSchema, LPNTagUpdateSchema, LPNTagResponseSchema,
    PackagingStationCreateSchema, PackagingStationUpdateSchema, PackagingStationResponseSchema,
    DockDoorAssignmentCreateSchema, DockDoorAssignmentUpdateSchema, DockDoorAssignmentResponseSchema,
    KittingOrderCreateSchema, KittingOrderUpdateSchema, KittingOrderResponseSchema,
    DeKittingJobCreateSchema, DeKittingJobUpdateSchema, DeKittingJobResponseSchema,
    HazardClassificationCreateSchema, HazardClassificationUpdateSchema, HazardClassificationResponseSchema,
    TempLogRecordCreateSchema, TempLogRecordUpdateSchema, TempLogRecordResponseSchema,
)

router = APIRouter(prefix="/warehouse_management", tags=["Advanced Warehouse Management (WMS)"])

# ==================== WarehouseZone Endpoints ====================
@router.get("/warehousezones", response_model=List[Dict[str, Any]])
def list_warehousezones(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WarehouseZone records with pagination and filtering."""
    svc = WarehouseZoneService()
    items = svc.list_warehousezones(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/warehousezones/{item_id}", response_model=Dict[str, Any])
def get_warehousezone_by_id(item_id: int):
    """Retrieve detailed record for WarehouseZone by ID."""
    svc = WarehouseZoneService()
    item = svc.get_warehousezone_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WarehouseZone with ID {item_id} not found")
    return item.to_dict()

@router.post("/warehousezones", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_warehousezone(payload: WarehouseZoneCreateSchema):
    """Create new WarehouseZone instance in enterprise repository."""
    svc = WarehouseZoneService()
    try:
        item = svc.create_warehousezone(
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

@router.put("/warehousezones/{item_id}", response_model=Dict[str, Any])
def update_warehousezone(item_id: int, payload: WarehouseZoneUpdateSchema):
    """Update existing WarehouseZone record fields."""
    svc = WarehouseZoneService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_warehousezone(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WarehouseZone with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/warehousezones/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warehousezone(item_id: int, hard: bool = Query(False)):
    """Delete WarehouseZone record (soft-delete by default)."""
    svc = WarehouseZoneService()
    ok = svc.delete_warehousezone(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WarehouseZone with ID {item_id} not found")
    return None

@router.get("/warehousezones/analytics/metrics", response_model=Dict[str, Any])
def get_warehousezone_metrics():
    """Calculate summary statistical KPIs for WarehouseZone collection."""
    svc = WarehouseZoneService()
    return svc.calculate_aggregate_metrics()

# ==================== StorageAisle Endpoints ====================
@router.get("/storageaisles", response_model=List[Dict[str, Any]])
def list_storageaisles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StorageAisle records with pagination and filtering."""
    svc = StorageAisleService()
    items = svc.list_storageaisles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/storageaisles/{item_id}", response_model=Dict[str, Any])
def get_storageaisle_by_id(item_id: int):
    """Retrieve detailed record for StorageAisle by ID."""
    svc = StorageAisleService()
    item = svc.get_storageaisle_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StorageAisle with ID {item_id} not found")
    return item.to_dict()

@router.post("/storageaisles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_storageaisle(payload: StorageAisleCreateSchema):
    """Create new StorageAisle instance in enterprise repository."""
    svc = StorageAisleService()
    try:
        item = svc.create_storageaisle(
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

@router.put("/storageaisles/{item_id}", response_model=Dict[str, Any])
def update_storageaisle(item_id: int, payload: StorageAisleUpdateSchema):
    """Update existing StorageAisle record fields."""
    svc = StorageAisleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_storageaisle(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StorageAisle with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/storageaisles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_storageaisle(item_id: int, hard: bool = Query(False)):
    """Delete StorageAisle record (soft-delete by default)."""
    svc = StorageAisleService()
    ok = svc.delete_storageaisle(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StorageAisle with ID {item_id} not found")
    return None

@router.get("/storageaisles/analytics/metrics", response_model=Dict[str, Any])
def get_storageaisle_metrics():
    """Calculate summary statistical KPIs for StorageAisle collection."""
    svc = StorageAisleService()
    return svc.calculate_aggregate_metrics()

# ==================== RackBinLocation Endpoints ====================
@router.get("/rackbinlocations", response_model=List[Dict[str, Any]])
def list_rackbinlocations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RackBinLocation records with pagination and filtering."""
    svc = RackBinLocationService()
    items = svc.list_rackbinlocations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/rackbinlocations/{item_id}", response_model=Dict[str, Any])
def get_rackbinlocation_by_id(item_id: int):
    """Retrieve detailed record for RackBinLocation by ID."""
    svc = RackBinLocationService()
    item = svc.get_rackbinlocation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RackBinLocation with ID {item_id} not found")
    return item.to_dict()

@router.post("/rackbinlocations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_rackbinlocation(payload: RackBinLocationCreateSchema):
    """Create new RackBinLocation instance in enterprise repository."""
    svc = RackBinLocationService()
    try:
        item = svc.create_rackbinlocation(
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

@router.put("/rackbinlocations/{item_id}", response_model=Dict[str, Any])
def update_rackbinlocation(item_id: int, payload: RackBinLocationUpdateSchema):
    """Update existing RackBinLocation record fields."""
    svc = RackBinLocationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_rackbinlocation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RackBinLocation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/rackbinlocations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rackbinlocation(item_id: int, hard: bool = Query(False)):
    """Delete RackBinLocation record (soft-delete by default)."""
    svc = RackBinLocationService()
    ok = svc.delete_rackbinlocation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RackBinLocation with ID {item_id} not found")
    return None

@router.get("/rackbinlocations/analytics/metrics", response_model=Dict[str, Any])
def get_rackbinlocation_metrics():
    """Calculate summary statistical KPIs for RackBinLocation collection."""
    svc = RackBinLocationService()
    return svc.calculate_aggregate_metrics()

# ==================== StockPallet Endpoints ====================
@router.get("/stockpallets", response_model=List[Dict[str, Any]])
def list_stockpallets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StockPallet records with pagination and filtering."""
    svc = StockPalletService()
    items = svc.list_stockpallets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/stockpallets/{item_id}", response_model=Dict[str, Any])
def get_stockpallet_by_id(item_id: int):
    """Retrieve detailed record for StockPallet by ID."""
    svc = StockPalletService()
    item = svc.get_stockpallet_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StockPallet with ID {item_id} not found")
    return item.to_dict()

@router.post("/stockpallets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_stockpallet(payload: StockPalletCreateSchema):
    """Create new StockPallet instance in enterprise repository."""
    svc = StockPalletService()
    try:
        item = svc.create_stockpallet(
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

@router.put("/stockpallets/{item_id}", response_model=Dict[str, Any])
def update_stockpallet(item_id: int, payload: StockPalletUpdateSchema):
    """Update existing StockPallet record fields."""
    svc = StockPalletService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_stockpallet(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StockPallet with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/stockpallets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stockpallet(item_id: int, hard: bool = Query(False)):
    """Delete StockPallet record (soft-delete by default)."""
    svc = StockPalletService()
    ok = svc.delete_stockpallet(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StockPallet with ID {item_id} not found")
    return None

@router.get("/stockpallets/analytics/metrics", response_model=Dict[str, Any])
def get_stockpallet_metrics():
    """Calculate summary statistical KPIs for StockPallet collection."""
    svc = StockPalletService()
    return svc.calculate_aggregate_metrics()

# ==================== WavePickingPlan Endpoints ====================
@router.get("/wavepickingplans", response_model=List[Dict[str, Any]])
def list_wavepickingplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WavePickingPlan records with pagination and filtering."""
    svc = WavePickingPlanService()
    items = svc.list_wavepickingplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/wavepickingplans/{item_id}", response_model=Dict[str, Any])
def get_wavepickingplan_by_id(item_id: int):
    """Retrieve detailed record for WavePickingPlan by ID."""
    svc = WavePickingPlanService()
    item = svc.get_wavepickingplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WavePickingPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/wavepickingplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_wavepickingplan(payload: WavePickingPlanCreateSchema):
    """Create new WavePickingPlan instance in enterprise repository."""
    svc = WavePickingPlanService()
    try:
        item = svc.create_wavepickingplan(
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

@router.put("/wavepickingplans/{item_id}", response_model=Dict[str, Any])
def update_wavepickingplan(item_id: int, payload: WavePickingPlanUpdateSchema):
    """Update existing WavePickingPlan record fields."""
    svc = WavePickingPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_wavepickingplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WavePickingPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/wavepickingplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wavepickingplan(item_id: int, hard: bool = Query(False)):
    """Delete WavePickingPlan record (soft-delete by default)."""
    svc = WavePickingPlanService()
    ok = svc.delete_wavepickingplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WavePickingPlan with ID {item_id} not found")
    return None

@router.get("/wavepickingplans/analytics/metrics", response_model=Dict[str, Any])
def get_wavepickingplan_metrics():
    """Calculate summary statistical KPIs for WavePickingPlan collection."""
    svc = WavePickingPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== PutawayTask Endpoints ====================
@router.get("/putawaytasks", response_model=List[Dict[str, Any]])
def list_putawaytasks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PutawayTask records with pagination and filtering."""
    svc = PutawayTaskService()
    items = svc.list_putawaytasks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/putawaytasks/{item_id}", response_model=Dict[str, Any])
def get_putawaytask_by_id(item_id: int):
    """Retrieve detailed record for PutawayTask by ID."""
    svc = PutawayTaskService()
    item = svc.get_putawaytask_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PutawayTask with ID {item_id} not found")
    return item.to_dict()

@router.post("/putawaytasks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_putawaytask(payload: PutawayTaskCreateSchema):
    """Create new PutawayTask instance in enterprise repository."""
    svc = PutawayTaskService()
    try:
        item = svc.create_putawaytask(
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

@router.put("/putawaytasks/{item_id}", response_model=Dict[str, Any])
def update_putawaytask(item_id: int, payload: PutawayTaskUpdateSchema):
    """Update existing PutawayTask record fields."""
    svc = PutawayTaskService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_putawaytask(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PutawayTask with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/putawaytasks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_putawaytask(item_id: int, hard: bool = Query(False)):
    """Delete PutawayTask record (soft-delete by default)."""
    svc = PutawayTaskService()
    ok = svc.delete_putawaytask(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PutawayTask with ID {item_id} not found")
    return None

@router.get("/putawaytasks/analytics/metrics", response_model=Dict[str, Any])
def get_putawaytask_metrics():
    """Calculate summary statistical KPIs for PutawayTask collection."""
    svc = PutawayTaskService()
    return svc.calculate_aggregate_metrics()

# ==================== CycleCountSheet Endpoints ====================
@router.get("/cyclecountsheets", response_model=List[Dict[str, Any]])
def list_cyclecountsheets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CycleCountSheet records with pagination and filtering."""
    svc = CycleCountSheetService()
    items = svc.list_cyclecountsheets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cyclecountsheets/{item_id}", response_model=Dict[str, Any])
def get_cyclecountsheet_by_id(item_id: int):
    """Retrieve detailed record for CycleCountSheet by ID."""
    svc = CycleCountSheetService()
    item = svc.get_cyclecountsheet_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CycleCountSheet with ID {item_id} not found")
    return item.to_dict()

@router.post("/cyclecountsheets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cyclecountsheet(payload: CycleCountSheetCreateSchema):
    """Create new CycleCountSheet instance in enterprise repository."""
    svc = CycleCountSheetService()
    try:
        item = svc.create_cyclecountsheet(
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

@router.put("/cyclecountsheets/{item_id}", response_model=Dict[str, Any])
def update_cyclecountsheet(item_id: int, payload: CycleCountSheetUpdateSchema):
    """Update existing CycleCountSheet record fields."""
    svc = CycleCountSheetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cyclecountsheet(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CycleCountSheet with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cyclecountsheets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cyclecountsheet(item_id: int, hard: bool = Query(False)):
    """Delete CycleCountSheet record (soft-delete by default)."""
    svc = CycleCountSheetService()
    ok = svc.delete_cyclecountsheet(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CycleCountSheet with ID {item_id} not found")
    return None

@router.get("/cyclecountsheets/analytics/metrics", response_model=Dict[str, Any])
def get_cyclecountsheet_metrics():
    """Calculate summary statistical KPIs for CycleCountSheet collection."""
    svc = CycleCountSheetService()
    return svc.calculate_aggregate_metrics()

# ==================== BinTransferOrder Endpoints ====================
@router.get("/bintransferorders", response_model=List[Dict[str, Any]])
def list_bintransferorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BinTransferOrder records with pagination and filtering."""
    svc = BinTransferOrderService()
    items = svc.list_bintransferorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bintransferorders/{item_id}", response_model=Dict[str, Any])
def get_bintransferorder_by_id(item_id: int):
    """Retrieve detailed record for BinTransferOrder by ID."""
    svc = BinTransferOrderService()
    item = svc.get_bintransferorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BinTransferOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/bintransferorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bintransferorder(payload: BinTransferOrderCreateSchema):
    """Create new BinTransferOrder instance in enterprise repository."""
    svc = BinTransferOrderService()
    try:
        item = svc.create_bintransferorder(
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

@router.put("/bintransferorders/{item_id}", response_model=Dict[str, Any])
def update_bintransferorder(item_id: int, payload: BinTransferOrderUpdateSchema):
    """Update existing BinTransferOrder record fields."""
    svc = BinTransferOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bintransferorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BinTransferOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bintransferorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bintransferorder(item_id: int, hard: bool = Query(False)):
    """Delete BinTransferOrder record (soft-delete by default)."""
    svc = BinTransferOrderService()
    ok = svc.delete_bintransferorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BinTransferOrder with ID {item_id} not found")
    return None

@router.get("/bintransferorders/analytics/metrics", response_model=Dict[str, Any])
def get_bintransferorder_metrics():
    """Calculate summary statistical KPIs for BinTransferOrder collection."""
    svc = BinTransferOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== CrossDockRoute Endpoints ====================
@router.get("/crossdockroutes", response_model=List[Dict[str, Any]])
def list_crossdockroutes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CrossDockRoute records with pagination and filtering."""
    svc = CrossDockRouteService()
    items = svc.list_crossdockroutes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/crossdockroutes/{item_id}", response_model=Dict[str, Any])
def get_crossdockroute_by_id(item_id: int):
    """Retrieve detailed record for CrossDockRoute by ID."""
    svc = CrossDockRouteService()
    item = svc.get_crossdockroute_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CrossDockRoute with ID {item_id} not found")
    return item.to_dict()

@router.post("/crossdockroutes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_crossdockroute(payload: CrossDockRouteCreateSchema):
    """Create new CrossDockRoute instance in enterprise repository."""
    svc = CrossDockRouteService()
    try:
        item = svc.create_crossdockroute(
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

@router.put("/crossdockroutes/{item_id}", response_model=Dict[str, Any])
def update_crossdockroute(item_id: int, payload: CrossDockRouteUpdateSchema):
    """Update existing CrossDockRoute record fields."""
    svc = CrossDockRouteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_crossdockroute(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CrossDockRoute with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/crossdockroutes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_crossdockroute(item_id: int, hard: bool = Query(False)):
    """Delete CrossDockRoute record (soft-delete by default)."""
    svc = CrossDockRouteService()
    ok = svc.delete_crossdockroute(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CrossDockRoute with ID {item_id} not found")
    return None

@router.get("/crossdockroutes/analytics/metrics", response_model=Dict[str, Any])
def get_crossdockroute_metrics():
    """Calculate summary statistical KPIs for CrossDockRoute collection."""
    svc = CrossDockRouteService()
    return svc.calculate_aggregate_metrics()

# ==================== LPNTag Endpoints ====================
@router.get("/lpntags", response_model=List[Dict[str, Any]])
def list_lpntags(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LPNTag records with pagination and filtering."""
    svc = LPNTagService()
    items = svc.list_lpntags(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/lpntags/{item_id}", response_model=Dict[str, Any])
def get_lpntag_by_id(item_id: int):
    """Retrieve detailed record for LPNTag by ID."""
    svc = LPNTagService()
    item = svc.get_lpntag_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LPNTag with ID {item_id} not found")
    return item.to_dict()

@router.post("/lpntags", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_lpntag(payload: LPNTagCreateSchema):
    """Create new LPNTag instance in enterprise repository."""
    svc = LPNTagService()
    try:
        item = svc.create_lpntag(
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

@router.put("/lpntags/{item_id}", response_model=Dict[str, Any])
def update_lpntag(item_id: int, payload: LPNTagUpdateSchema):
    """Update existing LPNTag record fields."""
    svc = LPNTagService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_lpntag(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LPNTag with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/lpntags/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lpntag(item_id: int, hard: bool = Query(False)):
    """Delete LPNTag record (soft-delete by default)."""
    svc = LPNTagService()
    ok = svc.delete_lpntag(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LPNTag with ID {item_id} not found")
    return None

@router.get("/lpntags/analytics/metrics", response_model=Dict[str, Any])
def get_lpntag_metrics():
    """Calculate summary statistical KPIs for LPNTag collection."""
    svc = LPNTagService()
    return svc.calculate_aggregate_metrics()

# ==================== PackagingStation Endpoints ====================
@router.get("/packagingstations", response_model=List[Dict[str, Any]])
def list_packagingstations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PackagingStation records with pagination and filtering."""
    svc = PackagingStationService()
    items = svc.list_packagingstations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/packagingstations/{item_id}", response_model=Dict[str, Any])
def get_packagingstation_by_id(item_id: int):
    """Retrieve detailed record for PackagingStation by ID."""
    svc = PackagingStationService()
    item = svc.get_packagingstation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PackagingStation with ID {item_id} not found")
    return item.to_dict()

@router.post("/packagingstations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_packagingstation(payload: PackagingStationCreateSchema):
    """Create new PackagingStation instance in enterprise repository."""
    svc = PackagingStationService()
    try:
        item = svc.create_packagingstation(
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

@router.put("/packagingstations/{item_id}", response_model=Dict[str, Any])
def update_packagingstation(item_id: int, payload: PackagingStationUpdateSchema):
    """Update existing PackagingStation record fields."""
    svc = PackagingStationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_packagingstation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PackagingStation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/packagingstations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_packagingstation(item_id: int, hard: bool = Query(False)):
    """Delete PackagingStation record (soft-delete by default)."""
    svc = PackagingStationService()
    ok = svc.delete_packagingstation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PackagingStation with ID {item_id} not found")
    return None

@router.get("/packagingstations/analytics/metrics", response_model=Dict[str, Any])
def get_packagingstation_metrics():
    """Calculate summary statistical KPIs for PackagingStation collection."""
    svc = PackagingStationService()
    return svc.calculate_aggregate_metrics()

# ==================== DockDoorAssignment Endpoints ====================
@router.get("/dockdoorassignments", response_model=List[Dict[str, Any]])
def list_dockdoorassignments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DockDoorAssignment records with pagination and filtering."""
    svc = DockDoorAssignmentService()
    items = svc.list_dockdoorassignments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dockdoorassignments/{item_id}", response_model=Dict[str, Any])
def get_dockdoorassignment_by_id(item_id: int):
    """Retrieve detailed record for DockDoorAssignment by ID."""
    svc = DockDoorAssignmentService()
    item = svc.get_dockdoorassignment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DockDoorAssignment with ID {item_id} not found")
    return item.to_dict()

@router.post("/dockdoorassignments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dockdoorassignment(payload: DockDoorAssignmentCreateSchema):
    """Create new DockDoorAssignment instance in enterprise repository."""
    svc = DockDoorAssignmentService()
    try:
        item = svc.create_dockdoorassignment(
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

@router.put("/dockdoorassignments/{item_id}", response_model=Dict[str, Any])
def update_dockdoorassignment(item_id: int, payload: DockDoorAssignmentUpdateSchema):
    """Update existing DockDoorAssignment record fields."""
    svc = DockDoorAssignmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dockdoorassignment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DockDoorAssignment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dockdoorassignments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dockdoorassignment(item_id: int, hard: bool = Query(False)):
    """Delete DockDoorAssignment record (soft-delete by default)."""
    svc = DockDoorAssignmentService()
    ok = svc.delete_dockdoorassignment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DockDoorAssignment with ID {item_id} not found")
    return None

@router.get("/dockdoorassignments/analytics/metrics", response_model=Dict[str, Any])
def get_dockdoorassignment_metrics():
    """Calculate summary statistical KPIs for DockDoorAssignment collection."""
    svc = DockDoorAssignmentService()
    return svc.calculate_aggregate_metrics()

# ==================== KittingOrder Endpoints ====================
@router.get("/kittingorders", response_model=List[Dict[str, Any]])
def list_kittingorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List KittingOrder records with pagination and filtering."""
    svc = KittingOrderService()
    items = svc.list_kittingorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/kittingorders/{item_id}", response_model=Dict[str, Any])
def get_kittingorder_by_id(item_id: int):
    """Retrieve detailed record for KittingOrder by ID."""
    svc = KittingOrderService()
    item = svc.get_kittingorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"KittingOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/kittingorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_kittingorder(payload: KittingOrderCreateSchema):
    """Create new KittingOrder instance in enterprise repository."""
    svc = KittingOrderService()
    try:
        item = svc.create_kittingorder(
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

@router.put("/kittingorders/{item_id}", response_model=Dict[str, Any])
def update_kittingorder(item_id: int, payload: KittingOrderUpdateSchema):
    """Update existing KittingOrder record fields."""
    svc = KittingOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_kittingorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"KittingOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/kittingorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_kittingorder(item_id: int, hard: bool = Query(False)):
    """Delete KittingOrder record (soft-delete by default)."""
    svc = KittingOrderService()
    ok = svc.delete_kittingorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"KittingOrder with ID {item_id} not found")
    return None

@router.get("/kittingorders/analytics/metrics", response_model=Dict[str, Any])
def get_kittingorder_metrics():
    """Calculate summary statistical KPIs for KittingOrder collection."""
    svc = KittingOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== DeKittingJob Endpoints ====================
@router.get("/dekittingjobs", response_model=List[Dict[str, Any]])
def list_dekittingjobs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeKittingJob records with pagination and filtering."""
    svc = DeKittingJobService()
    items = svc.list_dekittingjobs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dekittingjobs/{item_id}", response_model=Dict[str, Any])
def get_dekittingjob_by_id(item_id: int):
    """Retrieve detailed record for DeKittingJob by ID."""
    svc = DeKittingJobService()
    item = svc.get_dekittingjob_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeKittingJob with ID {item_id} not found")
    return item.to_dict()

@router.post("/dekittingjobs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dekittingjob(payload: DeKittingJobCreateSchema):
    """Create new DeKittingJob instance in enterprise repository."""
    svc = DeKittingJobService()
    try:
        item = svc.create_dekittingjob(
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

@router.put("/dekittingjobs/{item_id}", response_model=Dict[str, Any])
def update_dekittingjob(item_id: int, payload: DeKittingJobUpdateSchema):
    """Update existing DeKittingJob record fields."""
    svc = DeKittingJobService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dekittingjob(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeKittingJob with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dekittingjobs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dekittingjob(item_id: int, hard: bool = Query(False)):
    """Delete DeKittingJob record (soft-delete by default)."""
    svc = DeKittingJobService()
    ok = svc.delete_dekittingjob(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeKittingJob with ID {item_id} not found")
    return None

@router.get("/dekittingjobs/analytics/metrics", response_model=Dict[str, Any])
def get_dekittingjob_metrics():
    """Calculate summary statistical KPIs for DeKittingJob collection."""
    svc = DeKittingJobService()
    return svc.calculate_aggregate_metrics()

# ==================== HazardClassification Endpoints ====================
@router.get("/hazardclassifications", response_model=List[Dict[str, Any]])
def list_hazardclassifications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HazardClassification records with pagination and filtering."""
    svc = HazardClassificationService()
    items = svc.list_hazardclassifications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hazardclassifications/{item_id}", response_model=Dict[str, Any])
def get_hazardclassification_by_id(item_id: int):
    """Retrieve detailed record for HazardClassification by ID."""
    svc = HazardClassificationService()
    item = svc.get_hazardclassification_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HazardClassification with ID {item_id} not found")
    return item.to_dict()

@router.post("/hazardclassifications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hazardclassification(payload: HazardClassificationCreateSchema):
    """Create new HazardClassification instance in enterprise repository."""
    svc = HazardClassificationService()
    try:
        item = svc.create_hazardclassification(
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

@router.put("/hazardclassifications/{item_id}", response_model=Dict[str, Any])
def update_hazardclassification(item_id: int, payload: HazardClassificationUpdateSchema):
    """Update existing HazardClassification record fields."""
    svc = HazardClassificationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hazardclassification(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HazardClassification with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hazardclassifications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hazardclassification(item_id: int, hard: bool = Query(False)):
    """Delete HazardClassification record (soft-delete by default)."""
    svc = HazardClassificationService()
    ok = svc.delete_hazardclassification(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HazardClassification with ID {item_id} not found")
    return None

@router.get("/hazardclassifications/analytics/metrics", response_model=Dict[str, Any])
def get_hazardclassification_metrics():
    """Calculate summary statistical KPIs for HazardClassification collection."""
    svc = HazardClassificationService()
    return svc.calculate_aggregate_metrics()

# ==================== TempLogRecord Endpoints ====================
@router.get("/templogrecords", response_model=List[Dict[str, Any]])
def list_templogrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TempLogRecord records with pagination and filtering."""
    svc = TempLogRecordService()
    items = svc.list_templogrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/templogrecords/{item_id}", response_model=Dict[str, Any])
def get_templogrecord_by_id(item_id: int):
    """Retrieve detailed record for TempLogRecord by ID."""
    svc = TempLogRecordService()
    item = svc.get_templogrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TempLogRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/templogrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_templogrecord(payload: TempLogRecordCreateSchema):
    """Create new TempLogRecord instance in enterprise repository."""
    svc = TempLogRecordService()
    try:
        item = svc.create_templogrecord(
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

@router.put("/templogrecords/{item_id}", response_model=Dict[str, Any])
def update_templogrecord(item_id: int, payload: TempLogRecordUpdateSchema):
    """Update existing TempLogRecord record fields."""
    svc = TempLogRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_templogrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TempLogRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/templogrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_templogrecord(item_id: int, hard: bool = Query(False)):
    """Delete TempLogRecord record (soft-delete by default)."""
    svc = TempLogRecordService()
    ok = svc.delete_templogrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TempLogRecord with ID {item_id} not found")
    return None

@router.get("/templogrecords/analytics/metrics", response_model=Dict[str, Any])
def get_templogrecord_metrics():
    """Calculate summary statistical KPIs for TempLogRecord collection."""
    svc = TempLogRecordService()
    return svc.calculate_aggregate_metrics()

