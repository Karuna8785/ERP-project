"""
Automated Inventory Replenishment & Min-Max - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ReplenishmentPolicyService,
    EconomicOrderQuantityService,
    ReorderPointRuleService,
    SafetyStockCalculationService,
    VelocityClassificationABCService,
    SupplierLeadTimeProfileService,
    TransferReplenishmentOrderService,
    StockoutAlertNoticeService,
    ExcessInventoryFlagService,
    SeasonalDemandFactorService,
    BufferStockReserveService,
    VendorManagedInventoryService,
    BackorderPriorityQueueService,
    MultiEchelonNetworkService,
    ReplenishmentRunLogService,
    ServiceLevelGoalService,
)
from .schemas import (
    ReplenishmentPolicyCreateSchema, ReplenishmentPolicyUpdateSchema, ReplenishmentPolicyResponseSchema,
    EconomicOrderQuantityCreateSchema, EconomicOrderQuantityUpdateSchema, EconomicOrderQuantityResponseSchema,
    ReorderPointRuleCreateSchema, ReorderPointRuleUpdateSchema, ReorderPointRuleResponseSchema,
    SafetyStockCalculationCreateSchema, SafetyStockCalculationUpdateSchema, SafetyStockCalculationResponseSchema,
    VelocityClassificationABCCreateSchema, VelocityClassificationABCUpdateSchema, VelocityClassificationABCResponseSchema,
    SupplierLeadTimeProfileCreateSchema, SupplierLeadTimeProfileUpdateSchema, SupplierLeadTimeProfileResponseSchema,
    TransferReplenishmentOrderCreateSchema, TransferReplenishmentOrderUpdateSchema, TransferReplenishmentOrderResponseSchema,
    StockoutAlertNoticeCreateSchema, StockoutAlertNoticeUpdateSchema, StockoutAlertNoticeResponseSchema,
    ExcessInventoryFlagCreateSchema, ExcessInventoryFlagUpdateSchema, ExcessInventoryFlagResponseSchema,
    SeasonalDemandFactorCreateSchema, SeasonalDemandFactorUpdateSchema, SeasonalDemandFactorResponseSchema,
    BufferStockReserveCreateSchema, BufferStockReserveUpdateSchema, BufferStockReserveResponseSchema,
    VendorManagedInventoryCreateSchema, VendorManagedInventoryUpdateSchema, VendorManagedInventoryResponseSchema,
    BackorderPriorityQueueCreateSchema, BackorderPriorityQueueUpdateSchema, BackorderPriorityQueueResponseSchema,
    MultiEchelonNetworkCreateSchema, MultiEchelonNetworkUpdateSchema, MultiEchelonNetworkResponseSchema,
    ReplenishmentRunLogCreateSchema, ReplenishmentRunLogUpdateSchema, ReplenishmentRunLogResponseSchema,
    ServiceLevelGoalCreateSchema, ServiceLevelGoalUpdateSchema, ServiceLevelGoalResponseSchema,
)

router = APIRouter(prefix="/inventory_replenishment", tags=["Automated Inventory Replenishment & Min-Max"])

# ==================== ReplenishmentPolicy Endpoints ====================
@router.get("/replenishmentpolicys", response_model=List[Dict[str, Any]])
def list_replenishmentpolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReplenishmentPolicy records with pagination and filtering."""
    svc = ReplenishmentPolicyService()
    items = svc.list_replenishmentpolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/replenishmentpolicys/{item_id}", response_model=Dict[str, Any])
def get_replenishmentpolicy_by_id(item_id: int):
    """Retrieve detailed record for ReplenishmentPolicy by ID."""
    svc = ReplenishmentPolicyService()
    item = svc.get_replenishmentpolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReplenishmentPolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/replenishmentpolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_replenishmentpolicy(payload: ReplenishmentPolicyCreateSchema):
    """Create new ReplenishmentPolicy instance in enterprise repository."""
    svc = ReplenishmentPolicyService()
    try:
        item = svc.create_replenishmentpolicy(
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

@router.put("/replenishmentpolicys/{item_id}", response_model=Dict[str, Any])
def update_replenishmentpolicy(item_id: int, payload: ReplenishmentPolicyUpdateSchema):
    """Update existing ReplenishmentPolicy record fields."""
    svc = ReplenishmentPolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_replenishmentpolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReplenishmentPolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/replenishmentpolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_replenishmentpolicy(item_id: int, hard: bool = Query(False)):
    """Delete ReplenishmentPolicy record (soft-delete by default)."""
    svc = ReplenishmentPolicyService()
    ok = svc.delete_replenishmentpolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReplenishmentPolicy with ID {item_id} not found")
    return None

@router.get("/replenishmentpolicys/analytics/metrics", response_model=Dict[str, Any])
def get_replenishmentpolicy_metrics():
    """Calculate summary statistical KPIs for ReplenishmentPolicy collection."""
    svc = ReplenishmentPolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== EconomicOrderQuantity Endpoints ====================
@router.get("/economicorderquantitys", response_model=List[Dict[str, Any]])
def list_economicorderquantitys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EconomicOrderQuantity records with pagination and filtering."""
    svc = EconomicOrderQuantityService()
    items = svc.list_economicorderquantitys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/economicorderquantitys/{item_id}", response_model=Dict[str, Any])
def get_economicorderquantity_by_id(item_id: int):
    """Retrieve detailed record for EconomicOrderQuantity by ID."""
    svc = EconomicOrderQuantityService()
    item = svc.get_economicorderquantity_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EconomicOrderQuantity with ID {item_id} not found")
    return item.to_dict()

@router.post("/economicorderquantitys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_economicorderquantity(payload: EconomicOrderQuantityCreateSchema):
    """Create new EconomicOrderQuantity instance in enterprise repository."""
    svc = EconomicOrderQuantityService()
    try:
        item = svc.create_economicorderquantity(
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

@router.put("/economicorderquantitys/{item_id}", response_model=Dict[str, Any])
def update_economicorderquantity(item_id: int, payload: EconomicOrderQuantityUpdateSchema):
    """Update existing EconomicOrderQuantity record fields."""
    svc = EconomicOrderQuantityService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_economicorderquantity(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EconomicOrderQuantity with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/economicorderquantitys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_economicorderquantity(item_id: int, hard: bool = Query(False)):
    """Delete EconomicOrderQuantity record (soft-delete by default)."""
    svc = EconomicOrderQuantityService()
    ok = svc.delete_economicorderquantity(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EconomicOrderQuantity with ID {item_id} not found")
    return None

@router.get("/economicorderquantitys/analytics/metrics", response_model=Dict[str, Any])
def get_economicorderquantity_metrics():
    """Calculate summary statistical KPIs for EconomicOrderQuantity collection."""
    svc = EconomicOrderQuantityService()
    return svc.calculate_aggregate_metrics()

# ==================== ReorderPointRule Endpoints ====================
@router.get("/reorderpointrules", response_model=List[Dict[str, Any]])
def list_reorderpointrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReorderPointRule records with pagination and filtering."""
    svc = ReorderPointRuleService()
    items = svc.list_reorderpointrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/reorderpointrules/{item_id}", response_model=Dict[str, Any])
def get_reorderpointrule_by_id(item_id: int):
    """Retrieve detailed record for ReorderPointRule by ID."""
    svc = ReorderPointRuleService()
    item = svc.get_reorderpointrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReorderPointRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/reorderpointrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_reorderpointrule(payload: ReorderPointRuleCreateSchema):
    """Create new ReorderPointRule instance in enterprise repository."""
    svc = ReorderPointRuleService()
    try:
        item = svc.create_reorderpointrule(
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

@router.put("/reorderpointrules/{item_id}", response_model=Dict[str, Any])
def update_reorderpointrule(item_id: int, payload: ReorderPointRuleUpdateSchema):
    """Update existing ReorderPointRule record fields."""
    svc = ReorderPointRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_reorderpointrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReorderPointRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/reorderpointrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reorderpointrule(item_id: int, hard: bool = Query(False)):
    """Delete ReorderPointRule record (soft-delete by default)."""
    svc = ReorderPointRuleService()
    ok = svc.delete_reorderpointrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReorderPointRule with ID {item_id} not found")
    return None

@router.get("/reorderpointrules/analytics/metrics", response_model=Dict[str, Any])
def get_reorderpointrule_metrics():
    """Calculate summary statistical KPIs for ReorderPointRule collection."""
    svc = ReorderPointRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== SafetyStockCalculation Endpoints ====================
@router.get("/safetystockcalculations", response_model=List[Dict[str, Any]])
def list_safetystockcalculations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SafetyStockCalculation records with pagination and filtering."""
    svc = SafetyStockCalculationService()
    items = svc.list_safetystockcalculations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/safetystockcalculations/{item_id}", response_model=Dict[str, Any])
def get_safetystockcalculation_by_id(item_id: int):
    """Retrieve detailed record for SafetyStockCalculation by ID."""
    svc = SafetyStockCalculationService()
    item = svc.get_safetystockcalculation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SafetyStockCalculation with ID {item_id} not found")
    return item.to_dict()

@router.post("/safetystockcalculations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_safetystockcalculation(payload: SafetyStockCalculationCreateSchema):
    """Create new SafetyStockCalculation instance in enterprise repository."""
    svc = SafetyStockCalculationService()
    try:
        item = svc.create_safetystockcalculation(
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

@router.put("/safetystockcalculations/{item_id}", response_model=Dict[str, Any])
def update_safetystockcalculation(item_id: int, payload: SafetyStockCalculationUpdateSchema):
    """Update existing SafetyStockCalculation record fields."""
    svc = SafetyStockCalculationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_safetystockcalculation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SafetyStockCalculation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/safetystockcalculations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_safetystockcalculation(item_id: int, hard: bool = Query(False)):
    """Delete SafetyStockCalculation record (soft-delete by default)."""
    svc = SafetyStockCalculationService()
    ok = svc.delete_safetystockcalculation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SafetyStockCalculation with ID {item_id} not found")
    return None

@router.get("/safetystockcalculations/analytics/metrics", response_model=Dict[str, Any])
def get_safetystockcalculation_metrics():
    """Calculate summary statistical KPIs for SafetyStockCalculation collection."""
    svc = SafetyStockCalculationService()
    return svc.calculate_aggregate_metrics()

# ==================== VelocityClassificationABC Endpoints ====================
@router.get("/velocityclassificationabcs", response_model=List[Dict[str, Any]])
def list_velocityclassificationabcs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VelocityClassificationABC records with pagination and filtering."""
    svc = VelocityClassificationABCService()
    items = svc.list_velocityclassificationabcs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/velocityclassificationabcs/{item_id}", response_model=Dict[str, Any])
def get_velocityclassificationabc_by_id(item_id: int):
    """Retrieve detailed record for VelocityClassificationABC by ID."""
    svc = VelocityClassificationABCService()
    item = svc.get_velocityclassificationabc_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VelocityClassificationABC with ID {item_id} not found")
    return item.to_dict()

@router.post("/velocityclassificationabcs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_velocityclassificationabc(payload: VelocityClassificationABCCreateSchema):
    """Create new VelocityClassificationABC instance in enterprise repository."""
    svc = VelocityClassificationABCService()
    try:
        item = svc.create_velocityclassificationabc(
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

@router.put("/velocityclassificationabcs/{item_id}", response_model=Dict[str, Any])
def update_velocityclassificationabc(item_id: int, payload: VelocityClassificationABCUpdateSchema):
    """Update existing VelocityClassificationABC record fields."""
    svc = VelocityClassificationABCService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_velocityclassificationabc(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VelocityClassificationABC with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/velocityclassificationabcs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_velocityclassificationabc(item_id: int, hard: bool = Query(False)):
    """Delete VelocityClassificationABC record (soft-delete by default)."""
    svc = VelocityClassificationABCService()
    ok = svc.delete_velocityclassificationabc(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VelocityClassificationABC with ID {item_id} not found")
    return None

@router.get("/velocityclassificationabcs/analytics/metrics", response_model=Dict[str, Any])
def get_velocityclassificationabc_metrics():
    """Calculate summary statistical KPIs for VelocityClassificationABC collection."""
    svc = VelocityClassificationABCService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierLeadTimeProfile Endpoints ====================
@router.get("/supplierleadtimeprofiles", response_model=List[Dict[str, Any]])
def list_supplierleadtimeprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierLeadTimeProfile records with pagination and filtering."""
    svc = SupplierLeadTimeProfileService()
    items = svc.list_supplierleadtimeprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supplierleadtimeprofiles/{item_id}", response_model=Dict[str, Any])
def get_supplierleadtimeprofile_by_id(item_id: int):
    """Retrieve detailed record for SupplierLeadTimeProfile by ID."""
    svc = SupplierLeadTimeProfileService()
    item = svc.get_supplierleadtimeprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierLeadTimeProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/supplierleadtimeprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supplierleadtimeprofile(payload: SupplierLeadTimeProfileCreateSchema):
    """Create new SupplierLeadTimeProfile instance in enterprise repository."""
    svc = SupplierLeadTimeProfileService()
    try:
        item = svc.create_supplierleadtimeprofile(
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

@router.put("/supplierleadtimeprofiles/{item_id}", response_model=Dict[str, Any])
def update_supplierleadtimeprofile(item_id: int, payload: SupplierLeadTimeProfileUpdateSchema):
    """Update existing SupplierLeadTimeProfile record fields."""
    svc = SupplierLeadTimeProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supplierleadtimeprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierLeadTimeProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supplierleadtimeprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplierleadtimeprofile(item_id: int, hard: bool = Query(False)):
    """Delete SupplierLeadTimeProfile record (soft-delete by default)."""
    svc = SupplierLeadTimeProfileService()
    ok = svc.delete_supplierleadtimeprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierLeadTimeProfile with ID {item_id} not found")
    return None

@router.get("/supplierleadtimeprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_supplierleadtimeprofile_metrics():
    """Calculate summary statistical KPIs for SupplierLeadTimeProfile collection."""
    svc = SupplierLeadTimeProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== TransferReplenishmentOrder Endpoints ====================
@router.get("/transferreplenishmentorders", response_model=List[Dict[str, Any]])
def list_transferreplenishmentorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TransferReplenishmentOrder records with pagination and filtering."""
    svc = TransferReplenishmentOrderService()
    items = svc.list_transferreplenishmentorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/transferreplenishmentorders/{item_id}", response_model=Dict[str, Any])
def get_transferreplenishmentorder_by_id(item_id: int):
    """Retrieve detailed record for TransferReplenishmentOrder by ID."""
    svc = TransferReplenishmentOrderService()
    item = svc.get_transferreplenishmentorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TransferReplenishmentOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/transferreplenishmentorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_transferreplenishmentorder(payload: TransferReplenishmentOrderCreateSchema):
    """Create new TransferReplenishmentOrder instance in enterprise repository."""
    svc = TransferReplenishmentOrderService()
    try:
        item = svc.create_transferreplenishmentorder(
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

@router.put("/transferreplenishmentorders/{item_id}", response_model=Dict[str, Any])
def update_transferreplenishmentorder(item_id: int, payload: TransferReplenishmentOrderUpdateSchema):
    """Update existing TransferReplenishmentOrder record fields."""
    svc = TransferReplenishmentOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_transferreplenishmentorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TransferReplenishmentOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/transferreplenishmentorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transferreplenishmentorder(item_id: int, hard: bool = Query(False)):
    """Delete TransferReplenishmentOrder record (soft-delete by default)."""
    svc = TransferReplenishmentOrderService()
    ok = svc.delete_transferreplenishmentorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TransferReplenishmentOrder with ID {item_id} not found")
    return None

@router.get("/transferreplenishmentorders/analytics/metrics", response_model=Dict[str, Any])
def get_transferreplenishmentorder_metrics():
    """Calculate summary statistical KPIs for TransferReplenishmentOrder collection."""
    svc = TransferReplenishmentOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== StockoutAlertNotice Endpoints ====================
@router.get("/stockoutalertnotices", response_model=List[Dict[str, Any]])
def list_stockoutalertnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StockoutAlertNotice records with pagination and filtering."""
    svc = StockoutAlertNoticeService()
    items = svc.list_stockoutalertnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/stockoutalertnotices/{item_id}", response_model=Dict[str, Any])
def get_stockoutalertnotice_by_id(item_id: int):
    """Retrieve detailed record for StockoutAlertNotice by ID."""
    svc = StockoutAlertNoticeService()
    item = svc.get_stockoutalertnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StockoutAlertNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/stockoutalertnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_stockoutalertnotice(payload: StockoutAlertNoticeCreateSchema):
    """Create new StockoutAlertNotice instance in enterprise repository."""
    svc = StockoutAlertNoticeService()
    try:
        item = svc.create_stockoutalertnotice(
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

@router.put("/stockoutalertnotices/{item_id}", response_model=Dict[str, Any])
def update_stockoutalertnotice(item_id: int, payload: StockoutAlertNoticeUpdateSchema):
    """Update existing StockoutAlertNotice record fields."""
    svc = StockoutAlertNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_stockoutalertnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StockoutAlertNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/stockoutalertnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stockoutalertnotice(item_id: int, hard: bool = Query(False)):
    """Delete StockoutAlertNotice record (soft-delete by default)."""
    svc = StockoutAlertNoticeService()
    ok = svc.delete_stockoutalertnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StockoutAlertNotice with ID {item_id} not found")
    return None

@router.get("/stockoutalertnotices/analytics/metrics", response_model=Dict[str, Any])
def get_stockoutalertnotice_metrics():
    """Calculate summary statistical KPIs for StockoutAlertNotice collection."""
    svc = StockoutAlertNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== ExcessInventoryFlag Endpoints ====================
@router.get("/excessinventoryflags", response_model=List[Dict[str, Any]])
def list_excessinventoryflags(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExcessInventoryFlag records with pagination and filtering."""
    svc = ExcessInventoryFlagService()
    items = svc.list_excessinventoryflags(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/excessinventoryflags/{item_id}", response_model=Dict[str, Any])
def get_excessinventoryflag_by_id(item_id: int):
    """Retrieve detailed record for ExcessInventoryFlag by ID."""
    svc = ExcessInventoryFlagService()
    item = svc.get_excessinventoryflag_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExcessInventoryFlag with ID {item_id} not found")
    return item.to_dict()

@router.post("/excessinventoryflags", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_excessinventoryflag(payload: ExcessInventoryFlagCreateSchema):
    """Create new ExcessInventoryFlag instance in enterprise repository."""
    svc = ExcessInventoryFlagService()
    try:
        item = svc.create_excessinventoryflag(
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

@router.put("/excessinventoryflags/{item_id}", response_model=Dict[str, Any])
def update_excessinventoryflag(item_id: int, payload: ExcessInventoryFlagUpdateSchema):
    """Update existing ExcessInventoryFlag record fields."""
    svc = ExcessInventoryFlagService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_excessinventoryflag(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExcessInventoryFlag with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/excessinventoryflags/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_excessinventoryflag(item_id: int, hard: bool = Query(False)):
    """Delete ExcessInventoryFlag record (soft-delete by default)."""
    svc = ExcessInventoryFlagService()
    ok = svc.delete_excessinventoryflag(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExcessInventoryFlag with ID {item_id} not found")
    return None

@router.get("/excessinventoryflags/analytics/metrics", response_model=Dict[str, Any])
def get_excessinventoryflag_metrics():
    """Calculate summary statistical KPIs for ExcessInventoryFlag collection."""
    svc = ExcessInventoryFlagService()
    return svc.calculate_aggregate_metrics()

# ==================== SeasonalDemandFactor Endpoints ====================
@router.get("/seasonaldemandfactors", response_model=List[Dict[str, Any]])
def list_seasonaldemandfactors(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SeasonalDemandFactor records with pagination and filtering."""
    svc = SeasonalDemandFactorService()
    items = svc.list_seasonaldemandfactors(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/seasonaldemandfactors/{item_id}", response_model=Dict[str, Any])
def get_seasonaldemandfactor_by_id(item_id: int):
    """Retrieve detailed record for SeasonalDemandFactor by ID."""
    svc = SeasonalDemandFactorService()
    item = svc.get_seasonaldemandfactor_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SeasonalDemandFactor with ID {item_id} not found")
    return item.to_dict()

@router.post("/seasonaldemandfactors", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_seasonaldemandfactor(payload: SeasonalDemandFactorCreateSchema):
    """Create new SeasonalDemandFactor instance in enterprise repository."""
    svc = SeasonalDemandFactorService()
    try:
        item = svc.create_seasonaldemandfactor(
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

@router.put("/seasonaldemandfactors/{item_id}", response_model=Dict[str, Any])
def update_seasonaldemandfactor(item_id: int, payload: SeasonalDemandFactorUpdateSchema):
    """Update existing SeasonalDemandFactor record fields."""
    svc = SeasonalDemandFactorService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_seasonaldemandfactor(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SeasonalDemandFactor with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/seasonaldemandfactors/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_seasonaldemandfactor(item_id: int, hard: bool = Query(False)):
    """Delete SeasonalDemandFactor record (soft-delete by default)."""
    svc = SeasonalDemandFactorService()
    ok = svc.delete_seasonaldemandfactor(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SeasonalDemandFactor with ID {item_id} not found")
    return None

@router.get("/seasonaldemandfactors/analytics/metrics", response_model=Dict[str, Any])
def get_seasonaldemandfactor_metrics():
    """Calculate summary statistical KPIs for SeasonalDemandFactor collection."""
    svc = SeasonalDemandFactorService()
    return svc.calculate_aggregate_metrics()

# ==================== BufferStockReserve Endpoints ====================
@router.get("/bufferstockreserves", response_model=List[Dict[str, Any]])
def list_bufferstockreserves(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BufferStockReserve records with pagination and filtering."""
    svc = BufferStockReserveService()
    items = svc.list_bufferstockreserves(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bufferstockreserves/{item_id}", response_model=Dict[str, Any])
def get_bufferstockreserve_by_id(item_id: int):
    """Retrieve detailed record for BufferStockReserve by ID."""
    svc = BufferStockReserveService()
    item = svc.get_bufferstockreserve_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BufferStockReserve with ID {item_id} not found")
    return item.to_dict()

@router.post("/bufferstockreserves", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bufferstockreserve(payload: BufferStockReserveCreateSchema):
    """Create new BufferStockReserve instance in enterprise repository."""
    svc = BufferStockReserveService()
    try:
        item = svc.create_bufferstockreserve(
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

@router.put("/bufferstockreserves/{item_id}", response_model=Dict[str, Any])
def update_bufferstockreserve(item_id: int, payload: BufferStockReserveUpdateSchema):
    """Update existing BufferStockReserve record fields."""
    svc = BufferStockReserveService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bufferstockreserve(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BufferStockReserve with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bufferstockreserves/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bufferstockreserve(item_id: int, hard: bool = Query(False)):
    """Delete BufferStockReserve record (soft-delete by default)."""
    svc = BufferStockReserveService()
    ok = svc.delete_bufferstockreserve(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BufferStockReserve with ID {item_id} not found")
    return None

@router.get("/bufferstockreserves/analytics/metrics", response_model=Dict[str, Any])
def get_bufferstockreserve_metrics():
    """Calculate summary statistical KPIs for BufferStockReserve collection."""
    svc = BufferStockReserveService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorManagedInventory Endpoints ====================
@router.get("/vendormanagedinventorys", response_model=List[Dict[str, Any]])
def list_vendormanagedinventorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorManagedInventory records with pagination and filtering."""
    svc = VendorManagedInventoryService()
    items = svc.list_vendormanagedinventorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendormanagedinventorys/{item_id}", response_model=Dict[str, Any])
def get_vendormanagedinventory_by_id(item_id: int):
    """Retrieve detailed record for VendorManagedInventory by ID."""
    svc = VendorManagedInventoryService()
    item = svc.get_vendormanagedinventory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorManagedInventory with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendormanagedinventorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendormanagedinventory(payload: VendorManagedInventoryCreateSchema):
    """Create new VendorManagedInventory instance in enterprise repository."""
    svc = VendorManagedInventoryService()
    try:
        item = svc.create_vendormanagedinventory(
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

@router.put("/vendormanagedinventorys/{item_id}", response_model=Dict[str, Any])
def update_vendormanagedinventory(item_id: int, payload: VendorManagedInventoryUpdateSchema):
    """Update existing VendorManagedInventory record fields."""
    svc = VendorManagedInventoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendormanagedinventory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorManagedInventory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendormanagedinventorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendormanagedinventory(item_id: int, hard: bool = Query(False)):
    """Delete VendorManagedInventory record (soft-delete by default)."""
    svc = VendorManagedInventoryService()
    ok = svc.delete_vendormanagedinventory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorManagedInventory with ID {item_id} not found")
    return None

@router.get("/vendormanagedinventorys/analytics/metrics", response_model=Dict[str, Any])
def get_vendormanagedinventory_metrics():
    """Calculate summary statistical KPIs for VendorManagedInventory collection."""
    svc = VendorManagedInventoryService()
    return svc.calculate_aggregate_metrics()

# ==================== BackorderPriorityQueue Endpoints ====================
@router.get("/backorderpriorityqueues", response_model=List[Dict[str, Any]])
def list_backorderpriorityqueues(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BackorderPriorityQueue records with pagination and filtering."""
    svc = BackorderPriorityQueueService()
    items = svc.list_backorderpriorityqueues(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/backorderpriorityqueues/{item_id}", response_model=Dict[str, Any])
def get_backorderpriorityqueue_by_id(item_id: int):
    """Retrieve detailed record for BackorderPriorityQueue by ID."""
    svc = BackorderPriorityQueueService()
    item = svc.get_backorderpriorityqueue_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BackorderPriorityQueue with ID {item_id} not found")
    return item.to_dict()

@router.post("/backorderpriorityqueues", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_backorderpriorityqueue(payload: BackorderPriorityQueueCreateSchema):
    """Create new BackorderPriorityQueue instance in enterprise repository."""
    svc = BackorderPriorityQueueService()
    try:
        item = svc.create_backorderpriorityqueue(
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

@router.put("/backorderpriorityqueues/{item_id}", response_model=Dict[str, Any])
def update_backorderpriorityqueue(item_id: int, payload: BackorderPriorityQueueUpdateSchema):
    """Update existing BackorderPriorityQueue record fields."""
    svc = BackorderPriorityQueueService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_backorderpriorityqueue(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BackorderPriorityQueue with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/backorderpriorityqueues/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_backorderpriorityqueue(item_id: int, hard: bool = Query(False)):
    """Delete BackorderPriorityQueue record (soft-delete by default)."""
    svc = BackorderPriorityQueueService()
    ok = svc.delete_backorderpriorityqueue(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BackorderPriorityQueue with ID {item_id} not found")
    return None

@router.get("/backorderpriorityqueues/analytics/metrics", response_model=Dict[str, Any])
def get_backorderpriorityqueue_metrics():
    """Calculate summary statistical KPIs for BackorderPriorityQueue collection."""
    svc = BackorderPriorityQueueService()
    return svc.calculate_aggregate_metrics()

# ==================== MultiEchelonNetwork Endpoints ====================
@router.get("/multiechelonnetworks", response_model=List[Dict[str, Any]])
def list_multiechelonnetworks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MultiEchelonNetwork records with pagination and filtering."""
    svc = MultiEchelonNetworkService()
    items = svc.list_multiechelonnetworks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/multiechelonnetworks/{item_id}", response_model=Dict[str, Any])
def get_multiechelonnetwork_by_id(item_id: int):
    """Retrieve detailed record for MultiEchelonNetwork by ID."""
    svc = MultiEchelonNetworkService()
    item = svc.get_multiechelonnetwork_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MultiEchelonNetwork with ID {item_id} not found")
    return item.to_dict()

@router.post("/multiechelonnetworks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_multiechelonnetwork(payload: MultiEchelonNetworkCreateSchema):
    """Create new MultiEchelonNetwork instance in enterprise repository."""
    svc = MultiEchelonNetworkService()
    try:
        item = svc.create_multiechelonnetwork(
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

@router.put("/multiechelonnetworks/{item_id}", response_model=Dict[str, Any])
def update_multiechelonnetwork(item_id: int, payload: MultiEchelonNetworkUpdateSchema):
    """Update existing MultiEchelonNetwork record fields."""
    svc = MultiEchelonNetworkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_multiechelonnetwork(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MultiEchelonNetwork with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/multiechelonnetworks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_multiechelonnetwork(item_id: int, hard: bool = Query(False)):
    """Delete MultiEchelonNetwork record (soft-delete by default)."""
    svc = MultiEchelonNetworkService()
    ok = svc.delete_multiechelonnetwork(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MultiEchelonNetwork with ID {item_id} not found")
    return None

@router.get("/multiechelonnetworks/analytics/metrics", response_model=Dict[str, Any])
def get_multiechelonnetwork_metrics():
    """Calculate summary statistical KPIs for MultiEchelonNetwork collection."""
    svc = MultiEchelonNetworkService()
    return svc.calculate_aggregate_metrics()

# ==================== ReplenishmentRunLog Endpoints ====================
@router.get("/replenishmentrunlogs", response_model=List[Dict[str, Any]])
def list_replenishmentrunlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReplenishmentRunLog records with pagination and filtering."""
    svc = ReplenishmentRunLogService()
    items = svc.list_replenishmentrunlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/replenishmentrunlogs/{item_id}", response_model=Dict[str, Any])
def get_replenishmentrunlog_by_id(item_id: int):
    """Retrieve detailed record for ReplenishmentRunLog by ID."""
    svc = ReplenishmentRunLogService()
    item = svc.get_replenishmentrunlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReplenishmentRunLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/replenishmentrunlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_replenishmentrunlog(payload: ReplenishmentRunLogCreateSchema):
    """Create new ReplenishmentRunLog instance in enterprise repository."""
    svc = ReplenishmentRunLogService()
    try:
        item = svc.create_replenishmentrunlog(
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

@router.put("/replenishmentrunlogs/{item_id}", response_model=Dict[str, Any])
def update_replenishmentrunlog(item_id: int, payload: ReplenishmentRunLogUpdateSchema):
    """Update existing ReplenishmentRunLog record fields."""
    svc = ReplenishmentRunLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_replenishmentrunlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReplenishmentRunLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/replenishmentrunlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_replenishmentrunlog(item_id: int, hard: bool = Query(False)):
    """Delete ReplenishmentRunLog record (soft-delete by default)."""
    svc = ReplenishmentRunLogService()
    ok = svc.delete_replenishmentrunlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReplenishmentRunLog with ID {item_id} not found")
    return None

@router.get("/replenishmentrunlogs/analytics/metrics", response_model=Dict[str, Any])
def get_replenishmentrunlog_metrics():
    """Calculate summary statistical KPIs for ReplenishmentRunLog collection."""
    svc = ReplenishmentRunLogService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceLevelGoal Endpoints ====================
@router.get("/servicelevelgoals", response_model=List[Dict[str, Any]])
def list_servicelevelgoals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceLevelGoal records with pagination and filtering."""
    svc = ServiceLevelGoalService()
    items = svc.list_servicelevelgoals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicelevelgoals/{item_id}", response_model=Dict[str, Any])
def get_servicelevelgoal_by_id(item_id: int):
    """Retrieve detailed record for ServiceLevelGoal by ID."""
    svc = ServiceLevelGoalService()
    item = svc.get_servicelevelgoal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceLevelGoal with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicelevelgoals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicelevelgoal(payload: ServiceLevelGoalCreateSchema):
    """Create new ServiceLevelGoal instance in enterprise repository."""
    svc = ServiceLevelGoalService()
    try:
        item = svc.create_servicelevelgoal(
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

@router.put("/servicelevelgoals/{item_id}", response_model=Dict[str, Any])
def update_servicelevelgoal(item_id: int, payload: ServiceLevelGoalUpdateSchema):
    """Update existing ServiceLevelGoal record fields."""
    svc = ServiceLevelGoalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicelevelgoal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceLevelGoal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicelevelgoals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicelevelgoal(item_id: int, hard: bool = Query(False)):
    """Delete ServiceLevelGoal record (soft-delete by default)."""
    svc = ServiceLevelGoalService()
    ok = svc.delete_servicelevelgoal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceLevelGoal with ID {item_id} not found")
    return None

@router.get("/servicelevelgoals/analytics/metrics", response_model=Dict[str, Any])
def get_servicelevelgoal_metrics():
    """Calculate summary statistical KPIs for ServiceLevelGoal collection."""
    svc = ServiceLevelGoalService()
    return svc.calculate_aggregate_metrics()

