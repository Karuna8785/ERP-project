"""
Manufacturing Resource Planning (MRP II) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    WorkOrderService,
    BillOfMaterialService,
    OperationService,
    WorkCenterService,
    RoutingService,
    ProductionScheduleService,
    ScrapRecordService,
    QualityCheckService,
    MachineDowntimeService,
    ToolingAssetService,
    MaterialRequisitionService,
    ECOService,
    StandardCostService,
    AssemblyLineService,
    ShiftOutputService,
    WIPStockService,
)
from .schemas import (
    WorkOrderCreateSchema, WorkOrderUpdateSchema, WorkOrderResponseSchema,
    BillOfMaterialCreateSchema, BillOfMaterialUpdateSchema, BillOfMaterialResponseSchema,
    OperationCreateSchema, OperationUpdateSchema, OperationResponseSchema,
    WorkCenterCreateSchema, WorkCenterUpdateSchema, WorkCenterResponseSchema,
    RoutingCreateSchema, RoutingUpdateSchema, RoutingResponseSchema,
    ProductionScheduleCreateSchema, ProductionScheduleUpdateSchema, ProductionScheduleResponseSchema,
    ScrapRecordCreateSchema, ScrapRecordUpdateSchema, ScrapRecordResponseSchema,
    QualityCheckCreateSchema, QualityCheckUpdateSchema, QualityCheckResponseSchema,
    MachineDowntimeCreateSchema, MachineDowntimeUpdateSchema, MachineDowntimeResponseSchema,
    ToolingAssetCreateSchema, ToolingAssetUpdateSchema, ToolingAssetResponseSchema,
    MaterialRequisitionCreateSchema, MaterialRequisitionUpdateSchema, MaterialRequisitionResponseSchema,
    ECOCreateSchema, ECOUpdateSchema, ECOResponseSchema,
    StandardCostCreateSchema, StandardCostUpdateSchema, StandardCostResponseSchema,
    AssemblyLineCreateSchema, AssemblyLineUpdateSchema, AssemblyLineResponseSchema,
    ShiftOutputCreateSchema, ShiftOutputUpdateSchema, ShiftOutputResponseSchema,
    WIPStockCreateSchema, WIPStockUpdateSchema, WIPStockResponseSchema,
)

router = APIRouter(prefix="/manufacturing", tags=["Manufacturing Resource Planning (MRP II)"])

# ==================== WorkOrder Endpoints ====================
@router.get("/workorders", response_model=List[Dict[str, Any]])
def list_workorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WorkOrder records with pagination and filtering."""
    svc = WorkOrderService()
    items = svc.list_workorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/workorders/{item_id}", response_model=Dict[str, Any])
def get_workorder_by_id(item_id: int):
    """Retrieve detailed record for WorkOrder by ID."""
    svc = WorkOrderService()
    item = svc.get_workorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WorkOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/workorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_workorder(payload: WorkOrderCreateSchema):
    """Create new WorkOrder instance in enterprise repository."""
    svc = WorkOrderService()
    try:
        item = svc.create_workorder(
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

@router.put("/workorders/{item_id}", response_model=Dict[str, Any])
def update_workorder(item_id: int, payload: WorkOrderUpdateSchema):
    """Update existing WorkOrder record fields."""
    svc = WorkOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_workorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WorkOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/workorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workorder(item_id: int, hard: bool = Query(False)):
    """Delete WorkOrder record (soft-delete by default)."""
    svc = WorkOrderService()
    ok = svc.delete_workorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WorkOrder with ID {item_id} not found")
    return None

@router.get("/workorders/analytics/metrics", response_model=Dict[str, Any])
def get_workorder_metrics():
    """Calculate summary statistical KPIs for WorkOrder collection."""
    svc = WorkOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== BillOfMaterial Endpoints ====================
@router.get("/billofmaterials", response_model=List[Dict[str, Any]])
def list_billofmaterials(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BillOfMaterial records with pagination and filtering."""
    svc = BillOfMaterialService()
    items = svc.list_billofmaterials(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/billofmaterials/{item_id}", response_model=Dict[str, Any])
def get_billofmaterial_by_id(item_id: int):
    """Retrieve detailed record for BillOfMaterial by ID."""
    svc = BillOfMaterialService()
    item = svc.get_billofmaterial_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BillOfMaterial with ID {item_id} not found")
    return item.to_dict()

@router.post("/billofmaterials", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_billofmaterial(payload: BillOfMaterialCreateSchema):
    """Create new BillOfMaterial instance in enterprise repository."""
    svc = BillOfMaterialService()
    try:
        item = svc.create_billofmaterial(
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

@router.put("/billofmaterials/{item_id}", response_model=Dict[str, Any])
def update_billofmaterial(item_id: int, payload: BillOfMaterialUpdateSchema):
    """Update existing BillOfMaterial record fields."""
    svc = BillOfMaterialService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_billofmaterial(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BillOfMaterial with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/billofmaterials/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_billofmaterial(item_id: int, hard: bool = Query(False)):
    """Delete BillOfMaterial record (soft-delete by default)."""
    svc = BillOfMaterialService()
    ok = svc.delete_billofmaterial(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BillOfMaterial with ID {item_id} not found")
    return None

@router.get("/billofmaterials/analytics/metrics", response_model=Dict[str, Any])
def get_billofmaterial_metrics():
    """Calculate summary statistical KPIs for BillOfMaterial collection."""
    svc = BillOfMaterialService()
    return svc.calculate_aggregate_metrics()

# ==================== Operation Endpoints ====================
@router.get("/operations", response_model=List[Dict[str, Any]])
def list_operations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Operation records with pagination and filtering."""
    svc = OperationService()
    items = svc.list_operations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/operations/{item_id}", response_model=Dict[str, Any])
def get_operation_by_id(item_id: int):
    """Retrieve detailed record for Operation by ID."""
    svc = OperationService()
    item = svc.get_operation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Operation with ID {item_id} not found")
    return item.to_dict()

@router.post("/operations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_operation(payload: OperationCreateSchema):
    """Create new Operation instance in enterprise repository."""
    svc = OperationService()
    try:
        item = svc.create_operation(
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

@router.put("/operations/{item_id}", response_model=Dict[str, Any])
def update_operation(item_id: int, payload: OperationUpdateSchema):
    """Update existing Operation record fields."""
    svc = OperationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_operation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Operation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/operations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_operation(item_id: int, hard: bool = Query(False)):
    """Delete Operation record (soft-delete by default)."""
    svc = OperationService()
    ok = svc.delete_operation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Operation with ID {item_id} not found")
    return None

@router.get("/operations/analytics/metrics", response_model=Dict[str, Any])
def get_operation_metrics():
    """Calculate summary statistical KPIs for Operation collection."""
    svc = OperationService()
    return svc.calculate_aggregate_metrics()

# ==================== WorkCenter Endpoints ====================
@router.get("/workcenters", response_model=List[Dict[str, Any]])
def list_workcenters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WorkCenter records with pagination and filtering."""
    svc = WorkCenterService()
    items = svc.list_workcenters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/workcenters/{item_id}", response_model=Dict[str, Any])
def get_workcenter_by_id(item_id: int):
    """Retrieve detailed record for WorkCenter by ID."""
    svc = WorkCenterService()
    item = svc.get_workcenter_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WorkCenter with ID {item_id} not found")
    return item.to_dict()

@router.post("/workcenters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_workcenter(payload: WorkCenterCreateSchema):
    """Create new WorkCenter instance in enterprise repository."""
    svc = WorkCenterService()
    try:
        item = svc.create_workcenter(
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

@router.put("/workcenters/{item_id}", response_model=Dict[str, Any])
def update_workcenter(item_id: int, payload: WorkCenterUpdateSchema):
    """Update existing WorkCenter record fields."""
    svc = WorkCenterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_workcenter(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WorkCenter with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/workcenters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workcenter(item_id: int, hard: bool = Query(False)):
    """Delete WorkCenter record (soft-delete by default)."""
    svc = WorkCenterService()
    ok = svc.delete_workcenter(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WorkCenter with ID {item_id} not found")
    return None

@router.get("/workcenters/analytics/metrics", response_model=Dict[str, Any])
def get_workcenter_metrics():
    """Calculate summary statistical KPIs for WorkCenter collection."""
    svc = WorkCenterService()
    return svc.calculate_aggregate_metrics()

# ==================== Routing Endpoints ====================
@router.get("/routings", response_model=List[Dict[str, Any]])
def list_routings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List Routing records with pagination and filtering."""
    svc = RoutingService()
    items = svc.list_routings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/routings/{item_id}", response_model=Dict[str, Any])
def get_routing_by_id(item_id: int):
    """Retrieve detailed record for Routing by ID."""
    svc = RoutingService()
    item = svc.get_routing_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Routing with ID {item_id} not found")
    return item.to_dict()

@router.post("/routings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_routing(payload: RoutingCreateSchema):
    """Create new Routing instance in enterprise repository."""
    svc = RoutingService()
    try:
        item = svc.create_routing(
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

@router.put("/routings/{item_id}", response_model=Dict[str, Any])
def update_routing(item_id: int, payload: RoutingUpdateSchema):
    """Update existing Routing record fields."""
    svc = RoutingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_routing(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Routing with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/routings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_routing(item_id: int, hard: bool = Query(False)):
    """Delete Routing record (soft-delete by default)."""
    svc = RoutingService()
    ok = svc.delete_routing(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Routing with ID {item_id} not found")
    return None

@router.get("/routings/analytics/metrics", response_model=Dict[str, Any])
def get_routing_metrics():
    """Calculate summary statistical KPIs for Routing collection."""
    svc = RoutingService()
    return svc.calculate_aggregate_metrics()

# ==================== ProductionSchedule Endpoints ====================
@router.get("/productionschedules", response_model=List[Dict[str, Any]])
def list_productionschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProductionSchedule records with pagination and filtering."""
    svc = ProductionScheduleService()
    items = svc.list_productionschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/productionschedules/{item_id}", response_model=Dict[str, Any])
def get_productionschedule_by_id(item_id: int):
    """Retrieve detailed record for ProductionSchedule by ID."""
    svc = ProductionScheduleService()
    item = svc.get_productionschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProductionSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/productionschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_productionschedule(payload: ProductionScheduleCreateSchema):
    """Create new ProductionSchedule instance in enterprise repository."""
    svc = ProductionScheduleService()
    try:
        item = svc.create_productionschedule(
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

@router.put("/productionschedules/{item_id}", response_model=Dict[str, Any])
def update_productionschedule(item_id: int, payload: ProductionScheduleUpdateSchema):
    """Update existing ProductionSchedule record fields."""
    svc = ProductionScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_productionschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProductionSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/productionschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_productionschedule(item_id: int, hard: bool = Query(False)):
    """Delete ProductionSchedule record (soft-delete by default)."""
    svc = ProductionScheduleService()
    ok = svc.delete_productionschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProductionSchedule with ID {item_id} not found")
    return None

@router.get("/productionschedules/analytics/metrics", response_model=Dict[str, Any])
def get_productionschedule_metrics():
    """Calculate summary statistical KPIs for ProductionSchedule collection."""
    svc = ProductionScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== ScrapRecord Endpoints ====================
@router.get("/scraprecords", response_model=List[Dict[str, Any]])
def list_scraprecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ScrapRecord records with pagination and filtering."""
    svc = ScrapRecordService()
    items = svc.list_scraprecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/scraprecords/{item_id}", response_model=Dict[str, Any])
def get_scraprecord_by_id(item_id: int):
    """Retrieve detailed record for ScrapRecord by ID."""
    svc = ScrapRecordService()
    item = svc.get_scraprecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ScrapRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/scraprecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_scraprecord(payload: ScrapRecordCreateSchema):
    """Create new ScrapRecord instance in enterprise repository."""
    svc = ScrapRecordService()
    try:
        item = svc.create_scraprecord(
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

@router.put("/scraprecords/{item_id}", response_model=Dict[str, Any])
def update_scraprecord(item_id: int, payload: ScrapRecordUpdateSchema):
    """Update existing ScrapRecord record fields."""
    svc = ScrapRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_scraprecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ScrapRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/scraprecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scraprecord(item_id: int, hard: bool = Query(False)):
    """Delete ScrapRecord record (soft-delete by default)."""
    svc = ScrapRecordService()
    ok = svc.delete_scraprecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ScrapRecord with ID {item_id} not found")
    return None

@router.get("/scraprecords/analytics/metrics", response_model=Dict[str, Any])
def get_scraprecord_metrics():
    """Calculate summary statistical KPIs for ScrapRecord collection."""
    svc = ScrapRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== QualityCheck Endpoints ====================
@router.get("/qualitychecks", response_model=List[Dict[str, Any]])
def list_qualitychecks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List QualityCheck records with pagination and filtering."""
    svc = QualityCheckService()
    items = svc.list_qualitychecks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/qualitychecks/{item_id}", response_model=Dict[str, Any])
def get_qualitycheck_by_id(item_id: int):
    """Retrieve detailed record for QualityCheck by ID."""
    svc = QualityCheckService()
    item = svc.get_qualitycheck_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"QualityCheck with ID {item_id} not found")
    return item.to_dict()

@router.post("/qualitychecks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_qualitycheck(payload: QualityCheckCreateSchema):
    """Create new QualityCheck instance in enterprise repository."""
    svc = QualityCheckService()
    try:
        item = svc.create_qualitycheck(
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

@router.put("/qualitychecks/{item_id}", response_model=Dict[str, Any])
def update_qualitycheck(item_id: int, payload: QualityCheckUpdateSchema):
    """Update existing QualityCheck record fields."""
    svc = QualityCheckService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_qualitycheck(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"QualityCheck with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/qualitychecks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_qualitycheck(item_id: int, hard: bool = Query(False)):
    """Delete QualityCheck record (soft-delete by default)."""
    svc = QualityCheckService()
    ok = svc.delete_qualitycheck(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"QualityCheck with ID {item_id} not found")
    return None

@router.get("/qualitychecks/analytics/metrics", response_model=Dict[str, Any])
def get_qualitycheck_metrics():
    """Calculate summary statistical KPIs for QualityCheck collection."""
    svc = QualityCheckService()
    return svc.calculate_aggregate_metrics()

# ==================== MachineDowntime Endpoints ====================
@router.get("/machinedowntimes", response_model=List[Dict[str, Any]])
def list_machinedowntimes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MachineDowntime records with pagination and filtering."""
    svc = MachineDowntimeService()
    items = svc.list_machinedowntimes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/machinedowntimes/{item_id}", response_model=Dict[str, Any])
def get_machinedowntime_by_id(item_id: int):
    """Retrieve detailed record for MachineDowntime by ID."""
    svc = MachineDowntimeService()
    item = svc.get_machinedowntime_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MachineDowntime with ID {item_id} not found")
    return item.to_dict()

@router.post("/machinedowntimes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_machinedowntime(payload: MachineDowntimeCreateSchema):
    """Create new MachineDowntime instance in enterprise repository."""
    svc = MachineDowntimeService()
    try:
        item = svc.create_machinedowntime(
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

@router.put("/machinedowntimes/{item_id}", response_model=Dict[str, Any])
def update_machinedowntime(item_id: int, payload: MachineDowntimeUpdateSchema):
    """Update existing MachineDowntime record fields."""
    svc = MachineDowntimeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_machinedowntime(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MachineDowntime with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/machinedowntimes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_machinedowntime(item_id: int, hard: bool = Query(False)):
    """Delete MachineDowntime record (soft-delete by default)."""
    svc = MachineDowntimeService()
    ok = svc.delete_machinedowntime(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MachineDowntime with ID {item_id} not found")
    return None

@router.get("/machinedowntimes/analytics/metrics", response_model=Dict[str, Any])
def get_machinedowntime_metrics():
    """Calculate summary statistical KPIs for MachineDowntime collection."""
    svc = MachineDowntimeService()
    return svc.calculate_aggregate_metrics()

# ==================== ToolingAsset Endpoints ====================
@router.get("/toolingassets", response_model=List[Dict[str, Any]])
def list_toolingassets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ToolingAsset records with pagination and filtering."""
    svc = ToolingAssetService()
    items = svc.list_toolingassets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/toolingassets/{item_id}", response_model=Dict[str, Any])
def get_toolingasset_by_id(item_id: int):
    """Retrieve detailed record for ToolingAsset by ID."""
    svc = ToolingAssetService()
    item = svc.get_toolingasset_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ToolingAsset with ID {item_id} not found")
    return item.to_dict()

@router.post("/toolingassets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_toolingasset(payload: ToolingAssetCreateSchema):
    """Create new ToolingAsset instance in enterprise repository."""
    svc = ToolingAssetService()
    try:
        item = svc.create_toolingasset(
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

@router.put("/toolingassets/{item_id}", response_model=Dict[str, Any])
def update_toolingasset(item_id: int, payload: ToolingAssetUpdateSchema):
    """Update existing ToolingAsset record fields."""
    svc = ToolingAssetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_toolingasset(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ToolingAsset with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/toolingassets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_toolingasset(item_id: int, hard: bool = Query(False)):
    """Delete ToolingAsset record (soft-delete by default)."""
    svc = ToolingAssetService()
    ok = svc.delete_toolingasset(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ToolingAsset with ID {item_id} not found")
    return None

@router.get("/toolingassets/analytics/metrics", response_model=Dict[str, Any])
def get_toolingasset_metrics():
    """Calculate summary statistical KPIs for ToolingAsset collection."""
    svc = ToolingAssetService()
    return svc.calculate_aggregate_metrics()

# ==================== MaterialRequisition Endpoints ====================
@router.get("/materialrequisitions", response_model=List[Dict[str, Any]])
def list_materialrequisitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaterialRequisition records with pagination and filtering."""
    svc = MaterialRequisitionService()
    items = svc.list_materialrequisitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/materialrequisitions/{item_id}", response_model=Dict[str, Any])
def get_materialrequisition_by_id(item_id: int):
    """Retrieve detailed record for MaterialRequisition by ID."""
    svc = MaterialRequisitionService()
    item = svc.get_materialrequisition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaterialRequisition with ID {item_id} not found")
    return item.to_dict()

@router.post("/materialrequisitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_materialrequisition(payload: MaterialRequisitionCreateSchema):
    """Create new MaterialRequisition instance in enterprise repository."""
    svc = MaterialRequisitionService()
    try:
        item = svc.create_materialrequisition(
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

@router.put("/materialrequisitions/{item_id}", response_model=Dict[str, Any])
def update_materialrequisition(item_id: int, payload: MaterialRequisitionUpdateSchema):
    """Update existing MaterialRequisition record fields."""
    svc = MaterialRequisitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_materialrequisition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaterialRequisition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/materialrequisitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_materialrequisition(item_id: int, hard: bool = Query(False)):
    """Delete MaterialRequisition record (soft-delete by default)."""
    svc = MaterialRequisitionService()
    ok = svc.delete_materialrequisition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaterialRequisition with ID {item_id} not found")
    return None

@router.get("/materialrequisitions/analytics/metrics", response_model=Dict[str, Any])
def get_materialrequisition_metrics():
    """Calculate summary statistical KPIs for MaterialRequisition collection."""
    svc = MaterialRequisitionService()
    return svc.calculate_aggregate_metrics()

# ==================== ECO Endpoints ====================
@router.get("/ecos", response_model=List[Dict[str, Any]])
def list_ecos(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ECO records with pagination and filtering."""
    svc = ECOService()
    items = svc.list_ecos(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ecos/{item_id}", response_model=Dict[str, Any])
def get_eco_by_id(item_id: int):
    """Retrieve detailed record for ECO by ID."""
    svc = ECOService()
    item = svc.get_eco_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ECO with ID {item_id} not found")
    return item.to_dict()

@router.post("/ecos", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_eco(payload: ECOCreateSchema):
    """Create new ECO instance in enterprise repository."""
    svc = ECOService()
    try:
        item = svc.create_eco(
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

@router.put("/ecos/{item_id}", response_model=Dict[str, Any])
def update_eco(item_id: int, payload: ECOUpdateSchema):
    """Update existing ECO record fields."""
    svc = ECOService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_eco(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ECO with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ecos/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_eco(item_id: int, hard: bool = Query(False)):
    """Delete ECO record (soft-delete by default)."""
    svc = ECOService()
    ok = svc.delete_eco(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ECO with ID {item_id} not found")
    return None

@router.get("/ecos/analytics/metrics", response_model=Dict[str, Any])
def get_eco_metrics():
    """Calculate summary statistical KPIs for ECO collection."""
    svc = ECOService()
    return svc.calculate_aggregate_metrics()

# ==================== StandardCost Endpoints ====================
@router.get("/standardcosts", response_model=List[Dict[str, Any]])
def list_standardcosts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StandardCost records with pagination and filtering."""
    svc = StandardCostService()
    items = svc.list_standardcosts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/standardcosts/{item_id}", response_model=Dict[str, Any])
def get_standardcost_by_id(item_id: int):
    """Retrieve detailed record for StandardCost by ID."""
    svc = StandardCostService()
    item = svc.get_standardcost_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StandardCost with ID {item_id} not found")
    return item.to_dict()

@router.post("/standardcosts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_standardcost(payload: StandardCostCreateSchema):
    """Create new StandardCost instance in enterprise repository."""
    svc = StandardCostService()
    try:
        item = svc.create_standardcost(
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

@router.put("/standardcosts/{item_id}", response_model=Dict[str, Any])
def update_standardcost(item_id: int, payload: StandardCostUpdateSchema):
    """Update existing StandardCost record fields."""
    svc = StandardCostService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_standardcost(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StandardCost with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/standardcosts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_standardcost(item_id: int, hard: bool = Query(False)):
    """Delete StandardCost record (soft-delete by default)."""
    svc = StandardCostService()
    ok = svc.delete_standardcost(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StandardCost with ID {item_id} not found")
    return None

@router.get("/standardcosts/analytics/metrics", response_model=Dict[str, Any])
def get_standardcost_metrics():
    """Calculate summary statistical KPIs for StandardCost collection."""
    svc = StandardCostService()
    return svc.calculate_aggregate_metrics()

# ==================== AssemblyLine Endpoints ====================
@router.get("/assemblylines", response_model=List[Dict[str, Any]])
def list_assemblylines(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssemblyLine records with pagination and filtering."""
    svc = AssemblyLineService()
    items = svc.list_assemblylines(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assemblylines/{item_id}", response_model=Dict[str, Any])
def get_assemblyline_by_id(item_id: int):
    """Retrieve detailed record for AssemblyLine by ID."""
    svc = AssemblyLineService()
    item = svc.get_assemblyline_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssemblyLine with ID {item_id} not found")
    return item.to_dict()

@router.post("/assemblylines", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assemblyline(payload: AssemblyLineCreateSchema):
    """Create new AssemblyLine instance in enterprise repository."""
    svc = AssemblyLineService()
    try:
        item = svc.create_assemblyline(
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

@router.put("/assemblylines/{item_id}", response_model=Dict[str, Any])
def update_assemblyline(item_id: int, payload: AssemblyLineUpdateSchema):
    """Update existing AssemblyLine record fields."""
    svc = AssemblyLineService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assemblyline(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssemblyLine with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assemblylines/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assemblyline(item_id: int, hard: bool = Query(False)):
    """Delete AssemblyLine record (soft-delete by default)."""
    svc = AssemblyLineService()
    ok = svc.delete_assemblyline(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssemblyLine with ID {item_id} not found")
    return None

@router.get("/assemblylines/analytics/metrics", response_model=Dict[str, Any])
def get_assemblyline_metrics():
    """Calculate summary statistical KPIs for AssemblyLine collection."""
    svc = AssemblyLineService()
    return svc.calculate_aggregate_metrics()

# ==================== ShiftOutput Endpoints ====================
@router.get("/shiftoutputs", response_model=List[Dict[str, Any]])
def list_shiftoutputs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShiftOutput records with pagination and filtering."""
    svc = ShiftOutputService()
    items = svc.list_shiftoutputs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shiftoutputs/{item_id}", response_model=Dict[str, Any])
def get_shiftoutput_by_id(item_id: int):
    """Retrieve detailed record for ShiftOutput by ID."""
    svc = ShiftOutputService()
    item = svc.get_shiftoutput_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShiftOutput with ID {item_id} not found")
    return item.to_dict()

@router.post("/shiftoutputs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shiftoutput(payload: ShiftOutputCreateSchema):
    """Create new ShiftOutput instance in enterprise repository."""
    svc = ShiftOutputService()
    try:
        item = svc.create_shiftoutput(
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

@router.put("/shiftoutputs/{item_id}", response_model=Dict[str, Any])
def update_shiftoutput(item_id: int, payload: ShiftOutputUpdateSchema):
    """Update existing ShiftOutput record fields."""
    svc = ShiftOutputService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shiftoutput(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShiftOutput with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shiftoutputs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shiftoutput(item_id: int, hard: bool = Query(False)):
    """Delete ShiftOutput record (soft-delete by default)."""
    svc = ShiftOutputService()
    ok = svc.delete_shiftoutput(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShiftOutput with ID {item_id} not found")
    return None

@router.get("/shiftoutputs/analytics/metrics", response_model=Dict[str, Any])
def get_shiftoutput_metrics():
    """Calculate summary statistical KPIs for ShiftOutput collection."""
    svc = ShiftOutputService()
    return svc.calculate_aggregate_metrics()

# ==================== WIPStock Endpoints ====================
@router.get("/wipstocks", response_model=List[Dict[str, Any]])
def list_wipstocks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WIPStock records with pagination and filtering."""
    svc = WIPStockService()
    items = svc.list_wipstocks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/wipstocks/{item_id}", response_model=Dict[str, Any])
def get_wipstock_by_id(item_id: int):
    """Retrieve detailed record for WIPStock by ID."""
    svc = WIPStockService()
    item = svc.get_wipstock_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WIPStock with ID {item_id} not found")
    return item.to_dict()

@router.post("/wipstocks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_wipstock(payload: WIPStockCreateSchema):
    """Create new WIPStock instance in enterprise repository."""
    svc = WIPStockService()
    try:
        item = svc.create_wipstock(
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

@router.put("/wipstocks/{item_id}", response_model=Dict[str, Any])
def update_wipstock(item_id: int, payload: WIPStockUpdateSchema):
    """Update existing WIPStock record fields."""
    svc = WIPStockService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_wipstock(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WIPStock with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/wipstocks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wipstock(item_id: int, hard: bool = Query(False)):
    """Delete WIPStock record (soft-delete by default)."""
    svc = WIPStockService()
    ok = svc.delete_wipstock(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WIPStock with ID {item_id} not found")
    return None

@router.get("/wipstocks/analytics/metrics", response_model=Dict[str, Any])
def get_wipstock_metrics():
    """Calculate summary statistical KPIs for WIPStock collection."""
    svc = WIPStockService()
    return svc.calculate_aggregate_metrics()

