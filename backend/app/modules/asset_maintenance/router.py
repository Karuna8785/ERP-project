"""
Industrial Plant & CMMS Asset Maintenance - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    MaintenanceWorkOrderService,
    PreventivePlanService,
    AssetMeterReadingService,
    EquipmentFailureLogService,
    SparePartInventoryService,
    MaintenanceTechnicianService,
    ToolCalibrationLogService,
    DowntimeIncidentService,
    LubricationRouteService,
    SafetyWorkPermitService,
    VibrationAnalysisService,
    ThermalInspectionService,
    WorkOrderFeedbackService,
    VendorServiceContractService,
    EquipmentBillOfMaterialService,
    MaintenanceKPIService,
)
from .schemas import (
    MaintenanceWorkOrderCreateSchema, MaintenanceWorkOrderUpdateSchema, MaintenanceWorkOrderResponseSchema,
    PreventivePlanCreateSchema, PreventivePlanUpdateSchema, PreventivePlanResponseSchema,
    AssetMeterReadingCreateSchema, AssetMeterReadingUpdateSchema, AssetMeterReadingResponseSchema,
    EquipmentFailureLogCreateSchema, EquipmentFailureLogUpdateSchema, EquipmentFailureLogResponseSchema,
    SparePartInventoryCreateSchema, SparePartInventoryUpdateSchema, SparePartInventoryResponseSchema,
    MaintenanceTechnicianCreateSchema, MaintenanceTechnicianUpdateSchema, MaintenanceTechnicianResponseSchema,
    ToolCalibrationLogCreateSchema, ToolCalibrationLogUpdateSchema, ToolCalibrationLogResponseSchema,
    DowntimeIncidentCreateSchema, DowntimeIncidentUpdateSchema, DowntimeIncidentResponseSchema,
    LubricationRouteCreateSchema, LubricationRouteUpdateSchema, LubricationRouteResponseSchema,
    SafetyWorkPermitCreateSchema, SafetyWorkPermitUpdateSchema, SafetyWorkPermitResponseSchema,
    VibrationAnalysisCreateSchema, VibrationAnalysisUpdateSchema, VibrationAnalysisResponseSchema,
    ThermalInspectionCreateSchema, ThermalInspectionUpdateSchema, ThermalInspectionResponseSchema,
    WorkOrderFeedbackCreateSchema, WorkOrderFeedbackUpdateSchema, WorkOrderFeedbackResponseSchema,
    VendorServiceContractCreateSchema, VendorServiceContractUpdateSchema, VendorServiceContractResponseSchema,
    EquipmentBillOfMaterialCreateSchema, EquipmentBillOfMaterialUpdateSchema, EquipmentBillOfMaterialResponseSchema,
    MaintenanceKPICreateSchema, MaintenanceKPIUpdateSchema, MaintenanceKPIResponseSchema,
)

router = APIRouter(prefix="/asset_maintenance", tags=["Industrial Plant & CMMS Asset Maintenance"])

# ==================== MaintenanceWorkOrder Endpoints ====================
@router.get("/maintenanceworkorders", response_model=List[Dict[str, Any]])
def list_maintenanceworkorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaintenanceWorkOrder records with pagination and filtering."""
    svc = MaintenanceWorkOrderService()
    items = svc.list_maintenanceworkorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/maintenanceworkorders/{item_id}", response_model=Dict[str, Any])
def get_maintenanceworkorder_by_id(item_id: int):
    """Retrieve detailed record for MaintenanceWorkOrder by ID."""
    svc = MaintenanceWorkOrderService()
    item = svc.get_maintenanceworkorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaintenanceWorkOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/maintenanceworkorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_maintenanceworkorder(payload: MaintenanceWorkOrderCreateSchema):
    """Create new MaintenanceWorkOrder instance in enterprise repository."""
    svc = MaintenanceWorkOrderService()
    try:
        item = svc.create_maintenanceworkorder(
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

@router.put("/maintenanceworkorders/{item_id}", response_model=Dict[str, Any])
def update_maintenanceworkorder(item_id: int, payload: MaintenanceWorkOrderUpdateSchema):
    """Update existing MaintenanceWorkOrder record fields."""
    svc = MaintenanceWorkOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_maintenanceworkorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaintenanceWorkOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/maintenanceworkorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenanceworkorder(item_id: int, hard: bool = Query(False)):
    """Delete MaintenanceWorkOrder record (soft-delete by default)."""
    svc = MaintenanceWorkOrderService()
    ok = svc.delete_maintenanceworkorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaintenanceWorkOrder with ID {item_id} not found")
    return None

@router.get("/maintenanceworkorders/analytics/metrics", response_model=Dict[str, Any])
def get_maintenanceworkorder_metrics():
    """Calculate summary statistical KPIs for MaintenanceWorkOrder collection."""
    svc = MaintenanceWorkOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== PreventivePlan Endpoints ====================
@router.get("/preventiveplans", response_model=List[Dict[str, Any]])
def list_preventiveplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PreventivePlan records with pagination and filtering."""
    svc = PreventivePlanService()
    items = svc.list_preventiveplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/preventiveplans/{item_id}", response_model=Dict[str, Any])
def get_preventiveplan_by_id(item_id: int):
    """Retrieve detailed record for PreventivePlan by ID."""
    svc = PreventivePlanService()
    item = svc.get_preventiveplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PreventivePlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/preventiveplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_preventiveplan(payload: PreventivePlanCreateSchema):
    """Create new PreventivePlan instance in enterprise repository."""
    svc = PreventivePlanService()
    try:
        item = svc.create_preventiveplan(
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

@router.put("/preventiveplans/{item_id}", response_model=Dict[str, Any])
def update_preventiveplan(item_id: int, payload: PreventivePlanUpdateSchema):
    """Update existing PreventivePlan record fields."""
    svc = PreventivePlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_preventiveplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PreventivePlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/preventiveplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_preventiveplan(item_id: int, hard: bool = Query(False)):
    """Delete PreventivePlan record (soft-delete by default)."""
    svc = PreventivePlanService()
    ok = svc.delete_preventiveplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PreventivePlan with ID {item_id} not found")
    return None

@router.get("/preventiveplans/analytics/metrics", response_model=Dict[str, Any])
def get_preventiveplan_metrics():
    """Calculate summary statistical KPIs for PreventivePlan collection."""
    svc = PreventivePlanService()
    return svc.calculate_aggregate_metrics()

# ==================== AssetMeterReading Endpoints ====================
@router.get("/assetmeterreadings", response_model=List[Dict[str, Any]])
def list_assetmeterreadings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetMeterReading records with pagination and filtering."""
    svc = AssetMeterReadingService()
    items = svc.list_assetmeterreadings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assetmeterreadings/{item_id}", response_model=Dict[str, Any])
def get_assetmeterreading_by_id(item_id: int):
    """Retrieve detailed record for AssetMeterReading by ID."""
    svc = AssetMeterReadingService()
    item = svc.get_assetmeterreading_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetMeterReading with ID {item_id} not found")
    return item.to_dict()

@router.post("/assetmeterreadings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assetmeterreading(payload: AssetMeterReadingCreateSchema):
    """Create new AssetMeterReading instance in enterprise repository."""
    svc = AssetMeterReadingService()
    try:
        item = svc.create_assetmeterreading(
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

@router.put("/assetmeterreadings/{item_id}", response_model=Dict[str, Any])
def update_assetmeterreading(item_id: int, payload: AssetMeterReadingUpdateSchema):
    """Update existing AssetMeterReading record fields."""
    svc = AssetMeterReadingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assetmeterreading(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetMeterReading with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assetmeterreadings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assetmeterreading(item_id: int, hard: bool = Query(False)):
    """Delete AssetMeterReading record (soft-delete by default)."""
    svc = AssetMeterReadingService()
    ok = svc.delete_assetmeterreading(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetMeterReading with ID {item_id} not found")
    return None

@router.get("/assetmeterreadings/analytics/metrics", response_model=Dict[str, Any])
def get_assetmeterreading_metrics():
    """Calculate summary statistical KPIs for AssetMeterReading collection."""
    svc = AssetMeterReadingService()
    return svc.calculate_aggregate_metrics()

# ==================== EquipmentFailureLog Endpoints ====================
@router.get("/equipmentfailurelogs", response_model=List[Dict[str, Any]])
def list_equipmentfailurelogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EquipmentFailureLog records with pagination and filtering."""
    svc = EquipmentFailureLogService()
    items = svc.list_equipmentfailurelogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/equipmentfailurelogs/{item_id}", response_model=Dict[str, Any])
def get_equipmentfailurelog_by_id(item_id: int):
    """Retrieve detailed record for EquipmentFailureLog by ID."""
    svc = EquipmentFailureLogService()
    item = svc.get_equipmentfailurelog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EquipmentFailureLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/equipmentfailurelogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_equipmentfailurelog(payload: EquipmentFailureLogCreateSchema):
    """Create new EquipmentFailureLog instance in enterprise repository."""
    svc = EquipmentFailureLogService()
    try:
        item = svc.create_equipmentfailurelog(
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

@router.put("/equipmentfailurelogs/{item_id}", response_model=Dict[str, Any])
def update_equipmentfailurelog(item_id: int, payload: EquipmentFailureLogUpdateSchema):
    """Update existing EquipmentFailureLog record fields."""
    svc = EquipmentFailureLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_equipmentfailurelog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EquipmentFailureLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/equipmentfailurelogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equipmentfailurelog(item_id: int, hard: bool = Query(False)):
    """Delete EquipmentFailureLog record (soft-delete by default)."""
    svc = EquipmentFailureLogService()
    ok = svc.delete_equipmentfailurelog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EquipmentFailureLog with ID {item_id} not found")
    return None

@router.get("/equipmentfailurelogs/analytics/metrics", response_model=Dict[str, Any])
def get_equipmentfailurelog_metrics():
    """Calculate summary statistical KPIs for EquipmentFailureLog collection."""
    svc = EquipmentFailureLogService()
    return svc.calculate_aggregate_metrics()

# ==================== SparePartInventory Endpoints ====================
@router.get("/sparepartinventorys", response_model=List[Dict[str, Any]])
def list_sparepartinventorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SparePartInventory records with pagination and filtering."""
    svc = SparePartInventoryService()
    items = svc.list_sparepartinventorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sparepartinventorys/{item_id}", response_model=Dict[str, Any])
def get_sparepartinventory_by_id(item_id: int):
    """Retrieve detailed record for SparePartInventory by ID."""
    svc = SparePartInventoryService()
    item = svc.get_sparepartinventory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SparePartInventory with ID {item_id} not found")
    return item.to_dict()

@router.post("/sparepartinventorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sparepartinventory(payload: SparePartInventoryCreateSchema):
    """Create new SparePartInventory instance in enterprise repository."""
    svc = SparePartInventoryService()
    try:
        item = svc.create_sparepartinventory(
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

@router.put("/sparepartinventorys/{item_id}", response_model=Dict[str, Any])
def update_sparepartinventory(item_id: int, payload: SparePartInventoryUpdateSchema):
    """Update existing SparePartInventory record fields."""
    svc = SparePartInventoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sparepartinventory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SparePartInventory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sparepartinventorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sparepartinventory(item_id: int, hard: bool = Query(False)):
    """Delete SparePartInventory record (soft-delete by default)."""
    svc = SparePartInventoryService()
    ok = svc.delete_sparepartinventory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SparePartInventory with ID {item_id} not found")
    return None

@router.get("/sparepartinventorys/analytics/metrics", response_model=Dict[str, Any])
def get_sparepartinventory_metrics():
    """Calculate summary statistical KPIs for SparePartInventory collection."""
    svc = SparePartInventoryService()
    return svc.calculate_aggregate_metrics()

# ==================== MaintenanceTechnician Endpoints ====================
@router.get("/maintenancetechnicians", response_model=List[Dict[str, Any]])
def list_maintenancetechnicians(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaintenanceTechnician records with pagination and filtering."""
    svc = MaintenanceTechnicianService()
    items = svc.list_maintenancetechnicians(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/maintenancetechnicians/{item_id}", response_model=Dict[str, Any])
def get_maintenancetechnician_by_id(item_id: int):
    """Retrieve detailed record for MaintenanceTechnician by ID."""
    svc = MaintenanceTechnicianService()
    item = svc.get_maintenancetechnician_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaintenanceTechnician with ID {item_id} not found")
    return item.to_dict()

@router.post("/maintenancetechnicians", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_maintenancetechnician(payload: MaintenanceTechnicianCreateSchema):
    """Create new MaintenanceTechnician instance in enterprise repository."""
    svc = MaintenanceTechnicianService()
    try:
        item = svc.create_maintenancetechnician(
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

@router.put("/maintenancetechnicians/{item_id}", response_model=Dict[str, Any])
def update_maintenancetechnician(item_id: int, payload: MaintenanceTechnicianUpdateSchema):
    """Update existing MaintenanceTechnician record fields."""
    svc = MaintenanceTechnicianService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_maintenancetechnician(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaintenanceTechnician with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/maintenancetechnicians/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenancetechnician(item_id: int, hard: bool = Query(False)):
    """Delete MaintenanceTechnician record (soft-delete by default)."""
    svc = MaintenanceTechnicianService()
    ok = svc.delete_maintenancetechnician(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaintenanceTechnician with ID {item_id} not found")
    return None

@router.get("/maintenancetechnicians/analytics/metrics", response_model=Dict[str, Any])
def get_maintenancetechnician_metrics():
    """Calculate summary statistical KPIs for MaintenanceTechnician collection."""
    svc = MaintenanceTechnicianService()
    return svc.calculate_aggregate_metrics()

# ==================== ToolCalibrationLog Endpoints ====================
@router.get("/toolcalibrationlogs", response_model=List[Dict[str, Any]])
def list_toolcalibrationlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ToolCalibrationLog records with pagination and filtering."""
    svc = ToolCalibrationLogService()
    items = svc.list_toolcalibrationlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/toolcalibrationlogs/{item_id}", response_model=Dict[str, Any])
def get_toolcalibrationlog_by_id(item_id: int):
    """Retrieve detailed record for ToolCalibrationLog by ID."""
    svc = ToolCalibrationLogService()
    item = svc.get_toolcalibrationlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ToolCalibrationLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/toolcalibrationlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_toolcalibrationlog(payload: ToolCalibrationLogCreateSchema):
    """Create new ToolCalibrationLog instance in enterprise repository."""
    svc = ToolCalibrationLogService()
    try:
        item = svc.create_toolcalibrationlog(
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

@router.put("/toolcalibrationlogs/{item_id}", response_model=Dict[str, Any])
def update_toolcalibrationlog(item_id: int, payload: ToolCalibrationLogUpdateSchema):
    """Update existing ToolCalibrationLog record fields."""
    svc = ToolCalibrationLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_toolcalibrationlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ToolCalibrationLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/toolcalibrationlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_toolcalibrationlog(item_id: int, hard: bool = Query(False)):
    """Delete ToolCalibrationLog record (soft-delete by default)."""
    svc = ToolCalibrationLogService()
    ok = svc.delete_toolcalibrationlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ToolCalibrationLog with ID {item_id} not found")
    return None

@router.get("/toolcalibrationlogs/analytics/metrics", response_model=Dict[str, Any])
def get_toolcalibrationlog_metrics():
    """Calculate summary statistical KPIs for ToolCalibrationLog collection."""
    svc = ToolCalibrationLogService()
    return svc.calculate_aggregate_metrics()

# ==================== DowntimeIncident Endpoints ====================
@router.get("/downtimeincidents", response_model=List[Dict[str, Any]])
def list_downtimeincidents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DowntimeIncident records with pagination and filtering."""
    svc = DowntimeIncidentService()
    items = svc.list_downtimeincidents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/downtimeincidents/{item_id}", response_model=Dict[str, Any])
def get_downtimeincident_by_id(item_id: int):
    """Retrieve detailed record for DowntimeIncident by ID."""
    svc = DowntimeIncidentService()
    item = svc.get_downtimeincident_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DowntimeIncident with ID {item_id} not found")
    return item.to_dict()

@router.post("/downtimeincidents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_downtimeincident(payload: DowntimeIncidentCreateSchema):
    """Create new DowntimeIncident instance in enterprise repository."""
    svc = DowntimeIncidentService()
    try:
        item = svc.create_downtimeincident(
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

@router.put("/downtimeincidents/{item_id}", response_model=Dict[str, Any])
def update_downtimeincident(item_id: int, payload: DowntimeIncidentUpdateSchema):
    """Update existing DowntimeIncident record fields."""
    svc = DowntimeIncidentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_downtimeincident(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DowntimeIncident with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/downtimeincidents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_downtimeincident(item_id: int, hard: bool = Query(False)):
    """Delete DowntimeIncident record (soft-delete by default)."""
    svc = DowntimeIncidentService()
    ok = svc.delete_downtimeincident(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DowntimeIncident with ID {item_id} not found")
    return None

@router.get("/downtimeincidents/analytics/metrics", response_model=Dict[str, Any])
def get_downtimeincident_metrics():
    """Calculate summary statistical KPIs for DowntimeIncident collection."""
    svc = DowntimeIncidentService()
    return svc.calculate_aggregate_metrics()

# ==================== LubricationRoute Endpoints ====================
@router.get("/lubricationroutes", response_model=List[Dict[str, Any]])
def list_lubricationroutes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LubricationRoute records with pagination and filtering."""
    svc = LubricationRouteService()
    items = svc.list_lubricationroutes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/lubricationroutes/{item_id}", response_model=Dict[str, Any])
def get_lubricationroute_by_id(item_id: int):
    """Retrieve detailed record for LubricationRoute by ID."""
    svc = LubricationRouteService()
    item = svc.get_lubricationroute_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LubricationRoute with ID {item_id} not found")
    return item.to_dict()

@router.post("/lubricationroutes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_lubricationroute(payload: LubricationRouteCreateSchema):
    """Create new LubricationRoute instance in enterprise repository."""
    svc = LubricationRouteService()
    try:
        item = svc.create_lubricationroute(
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

@router.put("/lubricationroutes/{item_id}", response_model=Dict[str, Any])
def update_lubricationroute(item_id: int, payload: LubricationRouteUpdateSchema):
    """Update existing LubricationRoute record fields."""
    svc = LubricationRouteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_lubricationroute(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LubricationRoute with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/lubricationroutes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lubricationroute(item_id: int, hard: bool = Query(False)):
    """Delete LubricationRoute record (soft-delete by default)."""
    svc = LubricationRouteService()
    ok = svc.delete_lubricationroute(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LubricationRoute with ID {item_id} not found")
    return None

@router.get("/lubricationroutes/analytics/metrics", response_model=Dict[str, Any])
def get_lubricationroute_metrics():
    """Calculate summary statistical KPIs for LubricationRoute collection."""
    svc = LubricationRouteService()
    return svc.calculate_aggregate_metrics()

# ==================== SafetyWorkPermit Endpoints ====================
@router.get("/safetyworkpermits", response_model=List[Dict[str, Any]])
def list_safetyworkpermits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SafetyWorkPermit records with pagination and filtering."""
    svc = SafetyWorkPermitService()
    items = svc.list_safetyworkpermits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/safetyworkpermits/{item_id}", response_model=Dict[str, Any])
def get_safetyworkpermit_by_id(item_id: int):
    """Retrieve detailed record for SafetyWorkPermit by ID."""
    svc = SafetyWorkPermitService()
    item = svc.get_safetyworkpermit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SafetyWorkPermit with ID {item_id} not found")
    return item.to_dict()

@router.post("/safetyworkpermits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_safetyworkpermit(payload: SafetyWorkPermitCreateSchema):
    """Create new SafetyWorkPermit instance in enterprise repository."""
    svc = SafetyWorkPermitService()
    try:
        item = svc.create_safetyworkpermit(
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

@router.put("/safetyworkpermits/{item_id}", response_model=Dict[str, Any])
def update_safetyworkpermit(item_id: int, payload: SafetyWorkPermitUpdateSchema):
    """Update existing SafetyWorkPermit record fields."""
    svc = SafetyWorkPermitService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_safetyworkpermit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SafetyWorkPermit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/safetyworkpermits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_safetyworkpermit(item_id: int, hard: bool = Query(False)):
    """Delete SafetyWorkPermit record (soft-delete by default)."""
    svc = SafetyWorkPermitService()
    ok = svc.delete_safetyworkpermit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SafetyWorkPermit with ID {item_id} not found")
    return None

@router.get("/safetyworkpermits/analytics/metrics", response_model=Dict[str, Any])
def get_safetyworkpermit_metrics():
    """Calculate summary statistical KPIs for SafetyWorkPermit collection."""
    svc = SafetyWorkPermitService()
    return svc.calculate_aggregate_metrics()

# ==================== VibrationAnalysis Endpoints ====================
@router.get("/vibrationanalysiss", response_model=List[Dict[str, Any]])
def list_vibrationanalysiss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VibrationAnalysis records with pagination and filtering."""
    svc = VibrationAnalysisService()
    items = svc.list_vibrationanalysiss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vibrationanalysiss/{item_id}", response_model=Dict[str, Any])
def get_vibrationanalysis_by_id(item_id: int):
    """Retrieve detailed record for VibrationAnalysis by ID."""
    svc = VibrationAnalysisService()
    item = svc.get_vibrationanalysis_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VibrationAnalysis with ID {item_id} not found")
    return item.to_dict()

@router.post("/vibrationanalysiss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vibrationanalysis(payload: VibrationAnalysisCreateSchema):
    """Create new VibrationAnalysis instance in enterprise repository."""
    svc = VibrationAnalysisService()
    try:
        item = svc.create_vibrationanalysis(
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

@router.put("/vibrationanalysiss/{item_id}", response_model=Dict[str, Any])
def update_vibrationanalysis(item_id: int, payload: VibrationAnalysisUpdateSchema):
    """Update existing VibrationAnalysis record fields."""
    svc = VibrationAnalysisService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vibrationanalysis(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VibrationAnalysis with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vibrationanalysiss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vibrationanalysis(item_id: int, hard: bool = Query(False)):
    """Delete VibrationAnalysis record (soft-delete by default)."""
    svc = VibrationAnalysisService()
    ok = svc.delete_vibrationanalysis(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VibrationAnalysis with ID {item_id} not found")
    return None

@router.get("/vibrationanalysiss/analytics/metrics", response_model=Dict[str, Any])
def get_vibrationanalysis_metrics():
    """Calculate summary statistical KPIs for VibrationAnalysis collection."""
    svc = VibrationAnalysisService()
    return svc.calculate_aggregate_metrics()

# ==================== ThermalInspection Endpoints ====================
@router.get("/thermalinspections", response_model=List[Dict[str, Any]])
def list_thermalinspections(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ThermalInspection records with pagination and filtering."""
    svc = ThermalInspectionService()
    items = svc.list_thermalinspections(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/thermalinspections/{item_id}", response_model=Dict[str, Any])
def get_thermalinspection_by_id(item_id: int):
    """Retrieve detailed record for ThermalInspection by ID."""
    svc = ThermalInspectionService()
    item = svc.get_thermalinspection_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ThermalInspection with ID {item_id} not found")
    return item.to_dict()

@router.post("/thermalinspections", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_thermalinspection(payload: ThermalInspectionCreateSchema):
    """Create new ThermalInspection instance in enterprise repository."""
    svc = ThermalInspectionService()
    try:
        item = svc.create_thermalinspection(
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

@router.put("/thermalinspections/{item_id}", response_model=Dict[str, Any])
def update_thermalinspection(item_id: int, payload: ThermalInspectionUpdateSchema):
    """Update existing ThermalInspection record fields."""
    svc = ThermalInspectionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_thermalinspection(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ThermalInspection with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/thermalinspections/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_thermalinspection(item_id: int, hard: bool = Query(False)):
    """Delete ThermalInspection record (soft-delete by default)."""
    svc = ThermalInspectionService()
    ok = svc.delete_thermalinspection(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ThermalInspection with ID {item_id} not found")
    return None

@router.get("/thermalinspections/analytics/metrics", response_model=Dict[str, Any])
def get_thermalinspection_metrics():
    """Calculate summary statistical KPIs for ThermalInspection collection."""
    svc = ThermalInspectionService()
    return svc.calculate_aggregate_metrics()

# ==================== WorkOrderFeedback Endpoints ====================
@router.get("/workorderfeedbacks", response_model=List[Dict[str, Any]])
def list_workorderfeedbacks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WorkOrderFeedback records with pagination and filtering."""
    svc = WorkOrderFeedbackService()
    items = svc.list_workorderfeedbacks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/workorderfeedbacks/{item_id}", response_model=Dict[str, Any])
def get_workorderfeedback_by_id(item_id: int):
    """Retrieve detailed record for WorkOrderFeedback by ID."""
    svc = WorkOrderFeedbackService()
    item = svc.get_workorderfeedback_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WorkOrderFeedback with ID {item_id} not found")
    return item.to_dict()

@router.post("/workorderfeedbacks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_workorderfeedback(payload: WorkOrderFeedbackCreateSchema):
    """Create new WorkOrderFeedback instance in enterprise repository."""
    svc = WorkOrderFeedbackService()
    try:
        item = svc.create_workorderfeedback(
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

@router.put("/workorderfeedbacks/{item_id}", response_model=Dict[str, Any])
def update_workorderfeedback(item_id: int, payload: WorkOrderFeedbackUpdateSchema):
    """Update existing WorkOrderFeedback record fields."""
    svc = WorkOrderFeedbackService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_workorderfeedback(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WorkOrderFeedback with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/workorderfeedbacks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workorderfeedback(item_id: int, hard: bool = Query(False)):
    """Delete WorkOrderFeedback record (soft-delete by default)."""
    svc = WorkOrderFeedbackService()
    ok = svc.delete_workorderfeedback(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WorkOrderFeedback with ID {item_id} not found")
    return None

@router.get("/workorderfeedbacks/analytics/metrics", response_model=Dict[str, Any])
def get_workorderfeedback_metrics():
    """Calculate summary statistical KPIs for WorkOrderFeedback collection."""
    svc = WorkOrderFeedbackService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorServiceContract Endpoints ====================
@router.get("/vendorservicecontracts", response_model=List[Dict[str, Any]])
def list_vendorservicecontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorServiceContract records with pagination and filtering."""
    svc = VendorServiceContractService()
    items = svc.list_vendorservicecontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorservicecontracts/{item_id}", response_model=Dict[str, Any])
def get_vendorservicecontract_by_id(item_id: int):
    """Retrieve detailed record for VendorServiceContract by ID."""
    svc = VendorServiceContractService()
    item = svc.get_vendorservicecontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorServiceContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorservicecontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorservicecontract(payload: VendorServiceContractCreateSchema):
    """Create new VendorServiceContract instance in enterprise repository."""
    svc = VendorServiceContractService()
    try:
        item = svc.create_vendorservicecontract(
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

@router.put("/vendorservicecontracts/{item_id}", response_model=Dict[str, Any])
def update_vendorservicecontract(item_id: int, payload: VendorServiceContractUpdateSchema):
    """Update existing VendorServiceContract record fields."""
    svc = VendorServiceContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorservicecontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorServiceContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorservicecontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorservicecontract(item_id: int, hard: bool = Query(False)):
    """Delete VendorServiceContract record (soft-delete by default)."""
    svc = VendorServiceContractService()
    ok = svc.delete_vendorservicecontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorServiceContract with ID {item_id} not found")
    return None

@router.get("/vendorservicecontracts/analytics/metrics", response_model=Dict[str, Any])
def get_vendorservicecontract_metrics():
    """Calculate summary statistical KPIs for VendorServiceContract collection."""
    svc = VendorServiceContractService()
    return svc.calculate_aggregate_metrics()

# ==================== EquipmentBillOfMaterial Endpoints ====================
@router.get("/equipmentbillofmaterials", response_model=List[Dict[str, Any]])
def list_equipmentbillofmaterials(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EquipmentBillOfMaterial records with pagination and filtering."""
    svc = EquipmentBillOfMaterialService()
    items = svc.list_equipmentbillofmaterials(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/equipmentbillofmaterials/{item_id}", response_model=Dict[str, Any])
def get_equipmentbillofmaterial_by_id(item_id: int):
    """Retrieve detailed record for EquipmentBillOfMaterial by ID."""
    svc = EquipmentBillOfMaterialService()
    item = svc.get_equipmentbillofmaterial_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EquipmentBillOfMaterial with ID {item_id} not found")
    return item.to_dict()

@router.post("/equipmentbillofmaterials", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_equipmentbillofmaterial(payload: EquipmentBillOfMaterialCreateSchema):
    """Create new EquipmentBillOfMaterial instance in enterprise repository."""
    svc = EquipmentBillOfMaterialService()
    try:
        item = svc.create_equipmentbillofmaterial(
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

@router.put("/equipmentbillofmaterials/{item_id}", response_model=Dict[str, Any])
def update_equipmentbillofmaterial(item_id: int, payload: EquipmentBillOfMaterialUpdateSchema):
    """Update existing EquipmentBillOfMaterial record fields."""
    svc = EquipmentBillOfMaterialService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_equipmentbillofmaterial(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EquipmentBillOfMaterial with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/equipmentbillofmaterials/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equipmentbillofmaterial(item_id: int, hard: bool = Query(False)):
    """Delete EquipmentBillOfMaterial record (soft-delete by default)."""
    svc = EquipmentBillOfMaterialService()
    ok = svc.delete_equipmentbillofmaterial(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EquipmentBillOfMaterial with ID {item_id} not found")
    return None

@router.get("/equipmentbillofmaterials/analytics/metrics", response_model=Dict[str, Any])
def get_equipmentbillofmaterial_metrics():
    """Calculate summary statistical KPIs for EquipmentBillOfMaterial collection."""
    svc = EquipmentBillOfMaterialService()
    return svc.calculate_aggregate_metrics()

# ==================== MaintenanceKPI Endpoints ====================
@router.get("/maintenancekpis", response_model=List[Dict[str, Any]])
def list_maintenancekpis(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaintenanceKPI records with pagination and filtering."""
    svc = MaintenanceKPIService()
    items = svc.list_maintenancekpis(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/maintenancekpis/{item_id}", response_model=Dict[str, Any])
def get_maintenancekpi_by_id(item_id: int):
    """Retrieve detailed record for MaintenanceKPI by ID."""
    svc = MaintenanceKPIService()
    item = svc.get_maintenancekpi_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaintenanceKPI with ID {item_id} not found")
    return item.to_dict()

@router.post("/maintenancekpis", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_maintenancekpi(payload: MaintenanceKPICreateSchema):
    """Create new MaintenanceKPI instance in enterprise repository."""
    svc = MaintenanceKPIService()
    try:
        item = svc.create_maintenancekpi(
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

@router.put("/maintenancekpis/{item_id}", response_model=Dict[str, Any])
def update_maintenancekpi(item_id: int, payload: MaintenanceKPIUpdateSchema):
    """Update existing MaintenanceKPI record fields."""
    svc = MaintenanceKPIService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_maintenancekpi(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaintenanceKPI with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/maintenancekpis/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenancekpi(item_id: int, hard: bool = Query(False)):
    """Delete MaintenanceKPI record (soft-delete by default)."""
    svc = MaintenanceKPIService()
    ok = svc.delete_maintenancekpi(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaintenanceKPI with ID {item_id} not found")
    return None

@router.get("/maintenancekpis/analytics/metrics", response_model=Dict[str, Any])
def get_maintenancekpi_metrics():
    """Calculate summary statistical KPIs for MaintenanceKPI collection."""
    svc = MaintenanceKPIService()
    return svc.calculate_aggregate_metrics()

