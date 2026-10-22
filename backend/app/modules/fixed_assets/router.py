"""
Enterprise Fixed Asset Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    AssetMasterService,
    AssetCategoryService,
    DepreciationScheduleService,
    DepreciationRunService,
    AssetRevaluationService,
    AssetImpairmentService,
    MaintenanceScheduleService,
    WorkOrderAssetService,
    AssetDisposalService,
    AssetTransferLogService,
    PhysicalVerificationService,
    WarrantyAgreementService,
    InsurancePolicyService,
    LeaseScheduleService,
    ComponentAssetService,
    DisposalProceedsService,
)
from .schemas import (
    AssetMasterCreateSchema, AssetMasterUpdateSchema, AssetMasterResponseSchema,
    AssetCategoryCreateSchema, AssetCategoryUpdateSchema, AssetCategoryResponseSchema,
    DepreciationScheduleCreateSchema, DepreciationScheduleUpdateSchema, DepreciationScheduleResponseSchema,
    DepreciationRunCreateSchema, DepreciationRunUpdateSchema, DepreciationRunResponseSchema,
    AssetRevaluationCreateSchema, AssetRevaluationUpdateSchema, AssetRevaluationResponseSchema,
    AssetImpairmentCreateSchema, AssetImpairmentUpdateSchema, AssetImpairmentResponseSchema,
    MaintenanceScheduleCreateSchema, MaintenanceScheduleUpdateSchema, MaintenanceScheduleResponseSchema,
    WorkOrderAssetCreateSchema, WorkOrderAssetUpdateSchema, WorkOrderAssetResponseSchema,
    AssetDisposalCreateSchema, AssetDisposalUpdateSchema, AssetDisposalResponseSchema,
    AssetTransferLogCreateSchema, AssetTransferLogUpdateSchema, AssetTransferLogResponseSchema,
    PhysicalVerificationCreateSchema, PhysicalVerificationUpdateSchema, PhysicalVerificationResponseSchema,
    WarrantyAgreementCreateSchema, WarrantyAgreementUpdateSchema, WarrantyAgreementResponseSchema,
    InsurancePolicyCreateSchema, InsurancePolicyUpdateSchema, InsurancePolicyResponseSchema,
    LeaseScheduleCreateSchema, LeaseScheduleUpdateSchema, LeaseScheduleResponseSchema,
    ComponentAssetCreateSchema, ComponentAssetUpdateSchema, ComponentAssetResponseSchema,
    DisposalProceedsCreateSchema, DisposalProceedsUpdateSchema, DisposalProceedsResponseSchema,
)

router = APIRouter(prefix="/fixed_assets", tags=["Enterprise Fixed Asset Management"])

# ==================== AssetMaster Endpoints ====================
@router.get("/assetmasters", response_model=List[Dict[str, Any]])
def list_assetmasters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetMaster records with pagination and filtering."""
    svc = AssetMasterService()
    items = svc.list_assetmasters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assetmasters/{item_id}", response_model=Dict[str, Any])
def get_assetmaster_by_id(item_id: int):
    """Retrieve detailed record for AssetMaster by ID."""
    svc = AssetMasterService()
    item = svc.get_assetmaster_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetMaster with ID {item_id} not found")
    return item.to_dict()

@router.post("/assetmasters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assetmaster(payload: AssetMasterCreateSchema):
    """Create new AssetMaster instance in enterprise repository."""
    svc = AssetMasterService()
    try:
        item = svc.create_assetmaster(
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

@router.put("/assetmasters/{item_id}", response_model=Dict[str, Any])
def update_assetmaster(item_id: int, payload: AssetMasterUpdateSchema):
    """Update existing AssetMaster record fields."""
    svc = AssetMasterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assetmaster(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetMaster with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assetmasters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assetmaster(item_id: int, hard: bool = Query(False)):
    """Delete AssetMaster record (soft-delete by default)."""
    svc = AssetMasterService()
    ok = svc.delete_assetmaster(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetMaster with ID {item_id} not found")
    return None

@router.get("/assetmasters/analytics/metrics", response_model=Dict[str, Any])
def get_assetmaster_metrics():
    """Calculate summary statistical KPIs for AssetMaster collection."""
    svc = AssetMasterService()
    return svc.calculate_aggregate_metrics()

# ==================== AssetCategory Endpoints ====================
@router.get("/assetcategorys", response_model=List[Dict[str, Any]])
def list_assetcategorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetCategory records with pagination and filtering."""
    svc = AssetCategoryService()
    items = svc.list_assetcategorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assetcategorys/{item_id}", response_model=Dict[str, Any])
def get_assetcategory_by_id(item_id: int):
    """Retrieve detailed record for AssetCategory by ID."""
    svc = AssetCategoryService()
    item = svc.get_assetcategory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetCategory with ID {item_id} not found")
    return item.to_dict()

@router.post("/assetcategorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assetcategory(payload: AssetCategoryCreateSchema):
    """Create new AssetCategory instance in enterprise repository."""
    svc = AssetCategoryService()
    try:
        item = svc.create_assetcategory(
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

@router.put("/assetcategorys/{item_id}", response_model=Dict[str, Any])
def update_assetcategory(item_id: int, payload: AssetCategoryUpdateSchema):
    """Update existing AssetCategory record fields."""
    svc = AssetCategoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assetcategory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetCategory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assetcategorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assetcategory(item_id: int, hard: bool = Query(False)):
    """Delete AssetCategory record (soft-delete by default)."""
    svc = AssetCategoryService()
    ok = svc.delete_assetcategory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetCategory with ID {item_id} not found")
    return None

@router.get("/assetcategorys/analytics/metrics", response_model=Dict[str, Any])
def get_assetcategory_metrics():
    """Calculate summary statistical KPIs for AssetCategory collection."""
    svc = AssetCategoryService()
    return svc.calculate_aggregate_metrics()

# ==================== DepreciationSchedule Endpoints ====================
@router.get("/depreciationschedules", response_model=List[Dict[str, Any]])
def list_depreciationschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DepreciationSchedule records with pagination and filtering."""
    svc = DepreciationScheduleService()
    items = svc.list_depreciationschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/depreciationschedules/{item_id}", response_model=Dict[str, Any])
def get_depreciationschedule_by_id(item_id: int):
    """Retrieve detailed record for DepreciationSchedule by ID."""
    svc = DepreciationScheduleService()
    item = svc.get_depreciationschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DepreciationSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/depreciationschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_depreciationschedule(payload: DepreciationScheduleCreateSchema):
    """Create new DepreciationSchedule instance in enterprise repository."""
    svc = DepreciationScheduleService()
    try:
        item = svc.create_depreciationschedule(
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

@router.put("/depreciationschedules/{item_id}", response_model=Dict[str, Any])
def update_depreciationschedule(item_id: int, payload: DepreciationScheduleUpdateSchema):
    """Update existing DepreciationSchedule record fields."""
    svc = DepreciationScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_depreciationschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DepreciationSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/depreciationschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_depreciationschedule(item_id: int, hard: bool = Query(False)):
    """Delete DepreciationSchedule record (soft-delete by default)."""
    svc = DepreciationScheduleService()
    ok = svc.delete_depreciationschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DepreciationSchedule with ID {item_id} not found")
    return None

@router.get("/depreciationschedules/analytics/metrics", response_model=Dict[str, Any])
def get_depreciationschedule_metrics():
    """Calculate summary statistical KPIs for DepreciationSchedule collection."""
    svc = DepreciationScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== DepreciationRun Endpoints ====================
@router.get("/depreciationruns", response_model=List[Dict[str, Any]])
def list_depreciationruns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DepreciationRun records with pagination and filtering."""
    svc = DepreciationRunService()
    items = svc.list_depreciationruns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/depreciationruns/{item_id}", response_model=Dict[str, Any])
def get_depreciationrun_by_id(item_id: int):
    """Retrieve detailed record for DepreciationRun by ID."""
    svc = DepreciationRunService()
    item = svc.get_depreciationrun_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DepreciationRun with ID {item_id} not found")
    return item.to_dict()

@router.post("/depreciationruns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_depreciationrun(payload: DepreciationRunCreateSchema):
    """Create new DepreciationRun instance in enterprise repository."""
    svc = DepreciationRunService()
    try:
        item = svc.create_depreciationrun(
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

@router.put("/depreciationruns/{item_id}", response_model=Dict[str, Any])
def update_depreciationrun(item_id: int, payload: DepreciationRunUpdateSchema):
    """Update existing DepreciationRun record fields."""
    svc = DepreciationRunService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_depreciationrun(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DepreciationRun with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/depreciationruns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_depreciationrun(item_id: int, hard: bool = Query(False)):
    """Delete DepreciationRun record (soft-delete by default)."""
    svc = DepreciationRunService()
    ok = svc.delete_depreciationrun(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DepreciationRun with ID {item_id} not found")
    return None

@router.get("/depreciationruns/analytics/metrics", response_model=Dict[str, Any])
def get_depreciationrun_metrics():
    """Calculate summary statistical KPIs for DepreciationRun collection."""
    svc = DepreciationRunService()
    return svc.calculate_aggregate_metrics()

# ==================== AssetRevaluation Endpoints ====================
@router.get("/assetrevaluations", response_model=List[Dict[str, Any]])
def list_assetrevaluations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetRevaluation records with pagination and filtering."""
    svc = AssetRevaluationService()
    items = svc.list_assetrevaluations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assetrevaluations/{item_id}", response_model=Dict[str, Any])
def get_assetrevaluation_by_id(item_id: int):
    """Retrieve detailed record for AssetRevaluation by ID."""
    svc = AssetRevaluationService()
    item = svc.get_assetrevaluation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetRevaluation with ID {item_id} not found")
    return item.to_dict()

@router.post("/assetrevaluations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assetrevaluation(payload: AssetRevaluationCreateSchema):
    """Create new AssetRevaluation instance in enterprise repository."""
    svc = AssetRevaluationService()
    try:
        item = svc.create_assetrevaluation(
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

@router.put("/assetrevaluations/{item_id}", response_model=Dict[str, Any])
def update_assetrevaluation(item_id: int, payload: AssetRevaluationUpdateSchema):
    """Update existing AssetRevaluation record fields."""
    svc = AssetRevaluationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assetrevaluation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetRevaluation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assetrevaluations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assetrevaluation(item_id: int, hard: bool = Query(False)):
    """Delete AssetRevaluation record (soft-delete by default)."""
    svc = AssetRevaluationService()
    ok = svc.delete_assetrevaluation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetRevaluation with ID {item_id} not found")
    return None

@router.get("/assetrevaluations/analytics/metrics", response_model=Dict[str, Any])
def get_assetrevaluation_metrics():
    """Calculate summary statistical KPIs for AssetRevaluation collection."""
    svc = AssetRevaluationService()
    return svc.calculate_aggregate_metrics()

# ==================== AssetImpairment Endpoints ====================
@router.get("/assetimpairments", response_model=List[Dict[str, Any]])
def list_assetimpairments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetImpairment records with pagination and filtering."""
    svc = AssetImpairmentService()
    items = svc.list_assetimpairments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assetimpairments/{item_id}", response_model=Dict[str, Any])
def get_assetimpairment_by_id(item_id: int):
    """Retrieve detailed record for AssetImpairment by ID."""
    svc = AssetImpairmentService()
    item = svc.get_assetimpairment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetImpairment with ID {item_id} not found")
    return item.to_dict()

@router.post("/assetimpairments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assetimpairment(payload: AssetImpairmentCreateSchema):
    """Create new AssetImpairment instance in enterprise repository."""
    svc = AssetImpairmentService()
    try:
        item = svc.create_assetimpairment(
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

@router.put("/assetimpairments/{item_id}", response_model=Dict[str, Any])
def update_assetimpairment(item_id: int, payload: AssetImpairmentUpdateSchema):
    """Update existing AssetImpairment record fields."""
    svc = AssetImpairmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assetimpairment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetImpairment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assetimpairments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assetimpairment(item_id: int, hard: bool = Query(False)):
    """Delete AssetImpairment record (soft-delete by default)."""
    svc = AssetImpairmentService()
    ok = svc.delete_assetimpairment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetImpairment with ID {item_id} not found")
    return None

@router.get("/assetimpairments/analytics/metrics", response_model=Dict[str, Any])
def get_assetimpairment_metrics():
    """Calculate summary statistical KPIs for AssetImpairment collection."""
    svc = AssetImpairmentService()
    return svc.calculate_aggregate_metrics()

# ==================== MaintenanceSchedule Endpoints ====================
@router.get("/maintenanceschedules", response_model=List[Dict[str, Any]])
def list_maintenanceschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaintenanceSchedule records with pagination and filtering."""
    svc = MaintenanceScheduleService()
    items = svc.list_maintenanceschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/maintenanceschedules/{item_id}", response_model=Dict[str, Any])
def get_maintenanceschedule_by_id(item_id: int):
    """Retrieve detailed record for MaintenanceSchedule by ID."""
    svc = MaintenanceScheduleService()
    item = svc.get_maintenanceschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaintenanceSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/maintenanceschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_maintenanceschedule(payload: MaintenanceScheduleCreateSchema):
    """Create new MaintenanceSchedule instance in enterprise repository."""
    svc = MaintenanceScheduleService()
    try:
        item = svc.create_maintenanceschedule(
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

@router.put("/maintenanceschedules/{item_id}", response_model=Dict[str, Any])
def update_maintenanceschedule(item_id: int, payload: MaintenanceScheduleUpdateSchema):
    """Update existing MaintenanceSchedule record fields."""
    svc = MaintenanceScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_maintenanceschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaintenanceSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/maintenanceschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenanceschedule(item_id: int, hard: bool = Query(False)):
    """Delete MaintenanceSchedule record (soft-delete by default)."""
    svc = MaintenanceScheduleService()
    ok = svc.delete_maintenanceschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaintenanceSchedule with ID {item_id} not found")
    return None

@router.get("/maintenanceschedules/analytics/metrics", response_model=Dict[str, Any])
def get_maintenanceschedule_metrics():
    """Calculate summary statistical KPIs for MaintenanceSchedule collection."""
    svc = MaintenanceScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== WorkOrderAsset Endpoints ====================
@router.get("/workorderassets", response_model=List[Dict[str, Any]])
def list_workorderassets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WorkOrderAsset records with pagination and filtering."""
    svc = WorkOrderAssetService()
    items = svc.list_workorderassets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/workorderassets/{item_id}", response_model=Dict[str, Any])
def get_workorderasset_by_id(item_id: int):
    """Retrieve detailed record for WorkOrderAsset by ID."""
    svc = WorkOrderAssetService()
    item = svc.get_workorderasset_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WorkOrderAsset with ID {item_id} not found")
    return item.to_dict()

@router.post("/workorderassets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_workorderasset(payload: WorkOrderAssetCreateSchema):
    """Create new WorkOrderAsset instance in enterprise repository."""
    svc = WorkOrderAssetService()
    try:
        item = svc.create_workorderasset(
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

@router.put("/workorderassets/{item_id}", response_model=Dict[str, Any])
def update_workorderasset(item_id: int, payload: WorkOrderAssetUpdateSchema):
    """Update existing WorkOrderAsset record fields."""
    svc = WorkOrderAssetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_workorderasset(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WorkOrderAsset with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/workorderassets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workorderasset(item_id: int, hard: bool = Query(False)):
    """Delete WorkOrderAsset record (soft-delete by default)."""
    svc = WorkOrderAssetService()
    ok = svc.delete_workorderasset(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WorkOrderAsset with ID {item_id} not found")
    return None

@router.get("/workorderassets/analytics/metrics", response_model=Dict[str, Any])
def get_workorderasset_metrics():
    """Calculate summary statistical KPIs for WorkOrderAsset collection."""
    svc = WorkOrderAssetService()
    return svc.calculate_aggregate_metrics()

# ==================== AssetDisposal Endpoints ====================
@router.get("/assetdisposals", response_model=List[Dict[str, Any]])
def list_assetdisposals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetDisposal records with pagination and filtering."""
    svc = AssetDisposalService()
    items = svc.list_assetdisposals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assetdisposals/{item_id}", response_model=Dict[str, Any])
def get_assetdisposal_by_id(item_id: int):
    """Retrieve detailed record for AssetDisposal by ID."""
    svc = AssetDisposalService()
    item = svc.get_assetdisposal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetDisposal with ID {item_id} not found")
    return item.to_dict()

@router.post("/assetdisposals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assetdisposal(payload: AssetDisposalCreateSchema):
    """Create new AssetDisposal instance in enterprise repository."""
    svc = AssetDisposalService()
    try:
        item = svc.create_assetdisposal(
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

@router.put("/assetdisposals/{item_id}", response_model=Dict[str, Any])
def update_assetdisposal(item_id: int, payload: AssetDisposalUpdateSchema):
    """Update existing AssetDisposal record fields."""
    svc = AssetDisposalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assetdisposal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetDisposal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assetdisposals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assetdisposal(item_id: int, hard: bool = Query(False)):
    """Delete AssetDisposal record (soft-delete by default)."""
    svc = AssetDisposalService()
    ok = svc.delete_assetdisposal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetDisposal with ID {item_id} not found")
    return None

@router.get("/assetdisposals/analytics/metrics", response_model=Dict[str, Any])
def get_assetdisposal_metrics():
    """Calculate summary statistical KPIs for AssetDisposal collection."""
    svc = AssetDisposalService()
    return svc.calculate_aggregate_metrics()

# ==================== AssetTransferLog Endpoints ====================
@router.get("/assettransferlogs", response_model=List[Dict[str, Any]])
def list_assettransferlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AssetTransferLog records with pagination and filtering."""
    svc = AssetTransferLogService()
    items = svc.list_assettransferlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/assettransferlogs/{item_id}", response_model=Dict[str, Any])
def get_assettransferlog_by_id(item_id: int):
    """Retrieve detailed record for AssetTransferLog by ID."""
    svc = AssetTransferLogService()
    item = svc.get_assettransferlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AssetTransferLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/assettransferlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_assettransferlog(payload: AssetTransferLogCreateSchema):
    """Create new AssetTransferLog instance in enterprise repository."""
    svc = AssetTransferLogService()
    try:
        item = svc.create_assettransferlog(
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

@router.put("/assettransferlogs/{item_id}", response_model=Dict[str, Any])
def update_assettransferlog(item_id: int, payload: AssetTransferLogUpdateSchema):
    """Update existing AssetTransferLog record fields."""
    svc = AssetTransferLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_assettransferlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AssetTransferLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/assettransferlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assettransferlog(item_id: int, hard: bool = Query(False)):
    """Delete AssetTransferLog record (soft-delete by default)."""
    svc = AssetTransferLogService()
    ok = svc.delete_assettransferlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AssetTransferLog with ID {item_id} not found")
    return None

@router.get("/assettransferlogs/analytics/metrics", response_model=Dict[str, Any])
def get_assettransferlog_metrics():
    """Calculate summary statistical KPIs for AssetTransferLog collection."""
    svc = AssetTransferLogService()
    return svc.calculate_aggregate_metrics()

# ==================== PhysicalVerification Endpoints ====================
@router.get("/physicalverifications", response_model=List[Dict[str, Any]])
def list_physicalverifications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PhysicalVerification records with pagination and filtering."""
    svc = PhysicalVerificationService()
    items = svc.list_physicalverifications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/physicalverifications/{item_id}", response_model=Dict[str, Any])
def get_physicalverification_by_id(item_id: int):
    """Retrieve detailed record for PhysicalVerification by ID."""
    svc = PhysicalVerificationService()
    item = svc.get_physicalverification_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PhysicalVerification with ID {item_id} not found")
    return item.to_dict()

@router.post("/physicalverifications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_physicalverification(payload: PhysicalVerificationCreateSchema):
    """Create new PhysicalVerification instance in enterprise repository."""
    svc = PhysicalVerificationService()
    try:
        item = svc.create_physicalverification(
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

@router.put("/physicalverifications/{item_id}", response_model=Dict[str, Any])
def update_physicalverification(item_id: int, payload: PhysicalVerificationUpdateSchema):
    """Update existing PhysicalVerification record fields."""
    svc = PhysicalVerificationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_physicalverification(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PhysicalVerification with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/physicalverifications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_physicalverification(item_id: int, hard: bool = Query(False)):
    """Delete PhysicalVerification record (soft-delete by default)."""
    svc = PhysicalVerificationService()
    ok = svc.delete_physicalverification(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PhysicalVerification with ID {item_id} not found")
    return None

@router.get("/physicalverifications/analytics/metrics", response_model=Dict[str, Any])
def get_physicalverification_metrics():
    """Calculate summary statistical KPIs for PhysicalVerification collection."""
    svc = PhysicalVerificationService()
    return svc.calculate_aggregate_metrics()

# ==================== WarrantyAgreement Endpoints ====================
@router.get("/warrantyagreements", response_model=List[Dict[str, Any]])
def list_warrantyagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WarrantyAgreement records with pagination and filtering."""
    svc = WarrantyAgreementService()
    items = svc.list_warrantyagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/warrantyagreements/{item_id}", response_model=Dict[str, Any])
def get_warrantyagreement_by_id(item_id: int):
    """Retrieve detailed record for WarrantyAgreement by ID."""
    svc = WarrantyAgreementService()
    item = svc.get_warrantyagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WarrantyAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/warrantyagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_warrantyagreement(payload: WarrantyAgreementCreateSchema):
    """Create new WarrantyAgreement instance in enterprise repository."""
    svc = WarrantyAgreementService()
    try:
        item = svc.create_warrantyagreement(
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

@router.put("/warrantyagreements/{item_id}", response_model=Dict[str, Any])
def update_warrantyagreement(item_id: int, payload: WarrantyAgreementUpdateSchema):
    """Update existing WarrantyAgreement record fields."""
    svc = WarrantyAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_warrantyagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WarrantyAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/warrantyagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warrantyagreement(item_id: int, hard: bool = Query(False)):
    """Delete WarrantyAgreement record (soft-delete by default)."""
    svc = WarrantyAgreementService()
    ok = svc.delete_warrantyagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WarrantyAgreement with ID {item_id} not found")
    return None

@router.get("/warrantyagreements/analytics/metrics", response_model=Dict[str, Any])
def get_warrantyagreement_metrics():
    """Calculate summary statistical KPIs for WarrantyAgreement collection."""
    svc = WarrantyAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== InsurancePolicy Endpoints ====================
@router.get("/insurancepolicys", response_model=List[Dict[str, Any]])
def list_insurancepolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InsurancePolicy records with pagination and filtering."""
    svc = InsurancePolicyService()
    items = svc.list_insurancepolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/insurancepolicys/{item_id}", response_model=Dict[str, Any])
def get_insurancepolicy_by_id(item_id: int):
    """Retrieve detailed record for InsurancePolicy by ID."""
    svc = InsurancePolicyService()
    item = svc.get_insurancepolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InsurancePolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/insurancepolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_insurancepolicy(payload: InsurancePolicyCreateSchema):
    """Create new InsurancePolicy instance in enterprise repository."""
    svc = InsurancePolicyService()
    try:
        item = svc.create_insurancepolicy(
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

@router.put("/insurancepolicys/{item_id}", response_model=Dict[str, Any])
def update_insurancepolicy(item_id: int, payload: InsurancePolicyUpdateSchema):
    """Update existing InsurancePolicy record fields."""
    svc = InsurancePolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_insurancepolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InsurancePolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/insurancepolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurancepolicy(item_id: int, hard: bool = Query(False)):
    """Delete InsurancePolicy record (soft-delete by default)."""
    svc = InsurancePolicyService()
    ok = svc.delete_insurancepolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InsurancePolicy with ID {item_id} not found")
    return None

@router.get("/insurancepolicys/analytics/metrics", response_model=Dict[str, Any])
def get_insurancepolicy_metrics():
    """Calculate summary statistical KPIs for InsurancePolicy collection."""
    svc = InsurancePolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== LeaseSchedule Endpoints ====================
@router.get("/leaseschedules", response_model=List[Dict[str, Any]])
def list_leaseschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeaseSchedule records with pagination and filtering."""
    svc = LeaseScheduleService()
    items = svc.list_leaseschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leaseschedules/{item_id}", response_model=Dict[str, Any])
def get_leaseschedule_by_id(item_id: int):
    """Retrieve detailed record for LeaseSchedule by ID."""
    svc = LeaseScheduleService()
    item = svc.get_leaseschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeaseSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/leaseschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leaseschedule(payload: LeaseScheduleCreateSchema):
    """Create new LeaseSchedule instance in enterprise repository."""
    svc = LeaseScheduleService()
    try:
        item = svc.create_leaseschedule(
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

@router.put("/leaseschedules/{item_id}", response_model=Dict[str, Any])
def update_leaseschedule(item_id: int, payload: LeaseScheduleUpdateSchema):
    """Update existing LeaseSchedule record fields."""
    svc = LeaseScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leaseschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeaseSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leaseschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leaseschedule(item_id: int, hard: bool = Query(False)):
    """Delete LeaseSchedule record (soft-delete by default)."""
    svc = LeaseScheduleService()
    ok = svc.delete_leaseschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeaseSchedule with ID {item_id} not found")
    return None

@router.get("/leaseschedules/analytics/metrics", response_model=Dict[str, Any])
def get_leaseschedule_metrics():
    """Calculate summary statistical KPIs for LeaseSchedule collection."""
    svc = LeaseScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== ComponentAsset Endpoints ====================
@router.get("/componentassets", response_model=List[Dict[str, Any]])
def list_componentassets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ComponentAsset records with pagination and filtering."""
    svc = ComponentAssetService()
    items = svc.list_componentassets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/componentassets/{item_id}", response_model=Dict[str, Any])
def get_componentasset_by_id(item_id: int):
    """Retrieve detailed record for ComponentAsset by ID."""
    svc = ComponentAssetService()
    item = svc.get_componentasset_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ComponentAsset with ID {item_id} not found")
    return item.to_dict()

@router.post("/componentassets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_componentasset(payload: ComponentAssetCreateSchema):
    """Create new ComponentAsset instance in enterprise repository."""
    svc = ComponentAssetService()
    try:
        item = svc.create_componentasset(
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

@router.put("/componentassets/{item_id}", response_model=Dict[str, Any])
def update_componentasset(item_id: int, payload: ComponentAssetUpdateSchema):
    """Update existing ComponentAsset record fields."""
    svc = ComponentAssetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_componentasset(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ComponentAsset with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/componentassets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_componentasset(item_id: int, hard: bool = Query(False)):
    """Delete ComponentAsset record (soft-delete by default)."""
    svc = ComponentAssetService()
    ok = svc.delete_componentasset(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ComponentAsset with ID {item_id} not found")
    return None

@router.get("/componentassets/analytics/metrics", response_model=Dict[str, Any])
def get_componentasset_metrics():
    """Calculate summary statistical KPIs for ComponentAsset collection."""
    svc = ComponentAssetService()
    return svc.calculate_aggregate_metrics()

# ==================== DisposalProceeds Endpoints ====================
@router.get("/disposalproceedss", response_model=List[Dict[str, Any]])
def list_disposalproceedss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DisposalProceeds records with pagination and filtering."""
    svc = DisposalProceedsService()
    items = svc.list_disposalproceedss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/disposalproceedss/{item_id}", response_model=Dict[str, Any])
def get_disposalproceeds_by_id(item_id: int):
    """Retrieve detailed record for DisposalProceeds by ID."""
    svc = DisposalProceedsService()
    item = svc.get_disposalproceeds_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DisposalProceeds with ID {item_id} not found")
    return item.to_dict()

@router.post("/disposalproceedss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_disposalproceeds(payload: DisposalProceedsCreateSchema):
    """Create new DisposalProceeds instance in enterprise repository."""
    svc = DisposalProceedsService()
    try:
        item = svc.create_disposalproceeds(
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

@router.put("/disposalproceedss/{item_id}", response_model=Dict[str, Any])
def update_disposalproceeds(item_id: int, payload: DisposalProceedsUpdateSchema):
    """Update existing DisposalProceeds record fields."""
    svc = DisposalProceedsService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_disposalproceeds(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DisposalProceeds with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/disposalproceedss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_disposalproceeds(item_id: int, hard: bool = Query(False)):
    """Delete DisposalProceeds record (soft-delete by default)."""
    svc = DisposalProceedsService()
    ok = svc.delete_disposalproceeds(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DisposalProceeds with ID {item_id} not found")
    return None

@router.get("/disposalproceedss/analytics/metrics", response_model=Dict[str, Any])
def get_disposalproceeds_metrics():
    """Calculate summary statistical KPIs for DisposalProceeds collection."""
    svc = DisposalProceedsService()
    return svc.calculate_aggregate_metrics()

