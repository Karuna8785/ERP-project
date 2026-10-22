"""
Sales & Operations Planning (S&OP) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    DemandForecastPlanService,
    SupplyConstraintModelService,
    SafetyStockThresholdService,
    ProductionCapacityLimitService,
    LeadTimeVariabilityService,
    MaterialRequirementPlanService,
    DistributionPlanService,
    StockAllocationRuleService,
    SupplierCommitmentService,
    ForecastAccuracyMetricService,
    InventoryBufferZoneService,
    MasterProductionScheduleService,
    BottleneckWorkstationService,
    ScenarioComparisonService,
    ExpeditedShipmentOrderService,
    ExecutiveSOPConsensusService,
)
from .schemas import (
    DemandForecastPlanCreateSchema, DemandForecastPlanUpdateSchema, DemandForecastPlanResponseSchema,
    SupplyConstraintModelCreateSchema, SupplyConstraintModelUpdateSchema, SupplyConstraintModelResponseSchema,
    SafetyStockThresholdCreateSchema, SafetyStockThresholdUpdateSchema, SafetyStockThresholdResponseSchema,
    ProductionCapacityLimitCreateSchema, ProductionCapacityLimitUpdateSchema, ProductionCapacityLimitResponseSchema,
    LeadTimeVariabilityCreateSchema, LeadTimeVariabilityUpdateSchema, LeadTimeVariabilityResponseSchema,
    MaterialRequirementPlanCreateSchema, MaterialRequirementPlanUpdateSchema, MaterialRequirementPlanResponseSchema,
    DistributionPlanCreateSchema, DistributionPlanUpdateSchema, DistributionPlanResponseSchema,
    StockAllocationRuleCreateSchema, StockAllocationRuleUpdateSchema, StockAllocationRuleResponseSchema,
    SupplierCommitmentCreateSchema, SupplierCommitmentUpdateSchema, SupplierCommitmentResponseSchema,
    ForecastAccuracyMetricCreateSchema, ForecastAccuracyMetricUpdateSchema, ForecastAccuracyMetricResponseSchema,
    InventoryBufferZoneCreateSchema, InventoryBufferZoneUpdateSchema, InventoryBufferZoneResponseSchema,
    MasterProductionScheduleCreateSchema, MasterProductionScheduleUpdateSchema, MasterProductionScheduleResponseSchema,
    BottleneckWorkstationCreateSchema, BottleneckWorkstationUpdateSchema, BottleneckWorkstationResponseSchema,
    ScenarioComparisonCreateSchema, ScenarioComparisonUpdateSchema, ScenarioComparisonResponseSchema,
    ExpeditedShipmentOrderCreateSchema, ExpeditedShipmentOrderUpdateSchema, ExpeditedShipmentOrderResponseSchema,
    ExecutiveSOPConsensusCreateSchema, ExecutiveSOPConsensusUpdateSchema, ExecutiveSOPConsensusResponseSchema,
)

router = APIRouter(prefix="/supply_chain_planning", tags=["Sales & Operations Planning (S&OP)"])

# ==================== DemandForecastPlan Endpoints ====================
@router.get("/demandforecastplans", response_model=List[Dict[str, Any]])
def list_demandforecastplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DemandForecastPlan records with pagination and filtering."""
    svc = DemandForecastPlanService()
    items = svc.list_demandforecastplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/demandforecastplans/{item_id}", response_model=Dict[str, Any])
def get_demandforecastplan_by_id(item_id: int):
    """Retrieve detailed record for DemandForecastPlan by ID."""
    svc = DemandForecastPlanService()
    item = svc.get_demandforecastplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DemandForecastPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/demandforecastplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_demandforecastplan(payload: DemandForecastPlanCreateSchema):
    """Create new DemandForecastPlan instance in enterprise repository."""
    svc = DemandForecastPlanService()
    try:
        item = svc.create_demandforecastplan(
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

@router.put("/demandforecastplans/{item_id}", response_model=Dict[str, Any])
def update_demandforecastplan(item_id: int, payload: DemandForecastPlanUpdateSchema):
    """Update existing DemandForecastPlan record fields."""
    svc = DemandForecastPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_demandforecastplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DemandForecastPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/demandforecastplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_demandforecastplan(item_id: int, hard: bool = Query(False)):
    """Delete DemandForecastPlan record (soft-delete by default)."""
    svc = DemandForecastPlanService()
    ok = svc.delete_demandforecastplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DemandForecastPlan with ID {item_id} not found")
    return None

@router.get("/demandforecastplans/analytics/metrics", response_model=Dict[str, Any])
def get_demandforecastplan_metrics():
    """Calculate summary statistical KPIs for DemandForecastPlan collection."""
    svc = DemandForecastPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplyConstraintModel Endpoints ====================
@router.get("/supplyconstraintmodels", response_model=List[Dict[str, Any]])
def list_supplyconstraintmodels(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplyConstraintModel records with pagination and filtering."""
    svc = SupplyConstraintModelService()
    items = svc.list_supplyconstraintmodels(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supplyconstraintmodels/{item_id}", response_model=Dict[str, Any])
def get_supplyconstraintmodel_by_id(item_id: int):
    """Retrieve detailed record for SupplyConstraintModel by ID."""
    svc = SupplyConstraintModelService()
    item = svc.get_supplyconstraintmodel_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplyConstraintModel with ID {item_id} not found")
    return item.to_dict()

@router.post("/supplyconstraintmodels", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supplyconstraintmodel(payload: SupplyConstraintModelCreateSchema):
    """Create new SupplyConstraintModel instance in enterprise repository."""
    svc = SupplyConstraintModelService()
    try:
        item = svc.create_supplyconstraintmodel(
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

@router.put("/supplyconstraintmodels/{item_id}", response_model=Dict[str, Any])
def update_supplyconstraintmodel(item_id: int, payload: SupplyConstraintModelUpdateSchema):
    """Update existing SupplyConstraintModel record fields."""
    svc = SupplyConstraintModelService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supplyconstraintmodel(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplyConstraintModel with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supplyconstraintmodels/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplyconstraintmodel(item_id: int, hard: bool = Query(False)):
    """Delete SupplyConstraintModel record (soft-delete by default)."""
    svc = SupplyConstraintModelService()
    ok = svc.delete_supplyconstraintmodel(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplyConstraintModel with ID {item_id} not found")
    return None

@router.get("/supplyconstraintmodels/analytics/metrics", response_model=Dict[str, Any])
def get_supplyconstraintmodel_metrics():
    """Calculate summary statistical KPIs for SupplyConstraintModel collection."""
    svc = SupplyConstraintModelService()
    return svc.calculate_aggregate_metrics()

# ==================== SafetyStockThreshold Endpoints ====================
@router.get("/safetystockthresholds", response_model=List[Dict[str, Any]])
def list_safetystockthresholds(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SafetyStockThreshold records with pagination and filtering."""
    svc = SafetyStockThresholdService()
    items = svc.list_safetystockthresholds(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/safetystockthresholds/{item_id}", response_model=Dict[str, Any])
def get_safetystockthreshold_by_id(item_id: int):
    """Retrieve detailed record for SafetyStockThreshold by ID."""
    svc = SafetyStockThresholdService()
    item = svc.get_safetystockthreshold_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SafetyStockThreshold with ID {item_id} not found")
    return item.to_dict()

@router.post("/safetystockthresholds", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_safetystockthreshold(payload: SafetyStockThresholdCreateSchema):
    """Create new SafetyStockThreshold instance in enterprise repository."""
    svc = SafetyStockThresholdService()
    try:
        item = svc.create_safetystockthreshold(
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

@router.put("/safetystockthresholds/{item_id}", response_model=Dict[str, Any])
def update_safetystockthreshold(item_id: int, payload: SafetyStockThresholdUpdateSchema):
    """Update existing SafetyStockThreshold record fields."""
    svc = SafetyStockThresholdService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_safetystockthreshold(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SafetyStockThreshold with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/safetystockthresholds/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_safetystockthreshold(item_id: int, hard: bool = Query(False)):
    """Delete SafetyStockThreshold record (soft-delete by default)."""
    svc = SafetyStockThresholdService()
    ok = svc.delete_safetystockthreshold(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SafetyStockThreshold with ID {item_id} not found")
    return None

@router.get("/safetystockthresholds/analytics/metrics", response_model=Dict[str, Any])
def get_safetystockthreshold_metrics():
    """Calculate summary statistical KPIs for SafetyStockThreshold collection."""
    svc = SafetyStockThresholdService()
    return svc.calculate_aggregate_metrics()

# ==================== ProductionCapacityLimit Endpoints ====================
@router.get("/productioncapacitylimits", response_model=List[Dict[str, Any]])
def list_productioncapacitylimits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProductionCapacityLimit records with pagination and filtering."""
    svc = ProductionCapacityLimitService()
    items = svc.list_productioncapacitylimits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/productioncapacitylimits/{item_id}", response_model=Dict[str, Any])
def get_productioncapacitylimit_by_id(item_id: int):
    """Retrieve detailed record for ProductionCapacityLimit by ID."""
    svc = ProductionCapacityLimitService()
    item = svc.get_productioncapacitylimit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProductionCapacityLimit with ID {item_id} not found")
    return item.to_dict()

@router.post("/productioncapacitylimits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_productioncapacitylimit(payload: ProductionCapacityLimitCreateSchema):
    """Create new ProductionCapacityLimit instance in enterprise repository."""
    svc = ProductionCapacityLimitService()
    try:
        item = svc.create_productioncapacitylimit(
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

@router.put("/productioncapacitylimits/{item_id}", response_model=Dict[str, Any])
def update_productioncapacitylimit(item_id: int, payload: ProductionCapacityLimitUpdateSchema):
    """Update existing ProductionCapacityLimit record fields."""
    svc = ProductionCapacityLimitService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_productioncapacitylimit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProductionCapacityLimit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/productioncapacitylimits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_productioncapacitylimit(item_id: int, hard: bool = Query(False)):
    """Delete ProductionCapacityLimit record (soft-delete by default)."""
    svc = ProductionCapacityLimitService()
    ok = svc.delete_productioncapacitylimit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProductionCapacityLimit with ID {item_id} not found")
    return None

@router.get("/productioncapacitylimits/analytics/metrics", response_model=Dict[str, Any])
def get_productioncapacitylimit_metrics():
    """Calculate summary statistical KPIs for ProductionCapacityLimit collection."""
    svc = ProductionCapacityLimitService()
    return svc.calculate_aggregate_metrics()

# ==================== LeadTimeVariability Endpoints ====================
@router.get("/leadtimevariabilitys", response_model=List[Dict[str, Any]])
def list_leadtimevariabilitys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeadTimeVariability records with pagination and filtering."""
    svc = LeadTimeVariabilityService()
    items = svc.list_leadtimevariabilitys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leadtimevariabilitys/{item_id}", response_model=Dict[str, Any])
def get_leadtimevariability_by_id(item_id: int):
    """Retrieve detailed record for LeadTimeVariability by ID."""
    svc = LeadTimeVariabilityService()
    item = svc.get_leadtimevariability_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeadTimeVariability with ID {item_id} not found")
    return item.to_dict()

@router.post("/leadtimevariabilitys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leadtimevariability(payload: LeadTimeVariabilityCreateSchema):
    """Create new LeadTimeVariability instance in enterprise repository."""
    svc = LeadTimeVariabilityService()
    try:
        item = svc.create_leadtimevariability(
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

@router.put("/leadtimevariabilitys/{item_id}", response_model=Dict[str, Any])
def update_leadtimevariability(item_id: int, payload: LeadTimeVariabilityUpdateSchema):
    """Update existing LeadTimeVariability record fields."""
    svc = LeadTimeVariabilityService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leadtimevariability(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeadTimeVariability with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leadtimevariabilitys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leadtimevariability(item_id: int, hard: bool = Query(False)):
    """Delete LeadTimeVariability record (soft-delete by default)."""
    svc = LeadTimeVariabilityService()
    ok = svc.delete_leadtimevariability(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeadTimeVariability with ID {item_id} not found")
    return None

@router.get("/leadtimevariabilitys/analytics/metrics", response_model=Dict[str, Any])
def get_leadtimevariability_metrics():
    """Calculate summary statistical KPIs for LeadTimeVariability collection."""
    svc = LeadTimeVariabilityService()
    return svc.calculate_aggregate_metrics()

# ==================== MaterialRequirementPlan Endpoints ====================
@router.get("/materialrequirementplans", response_model=List[Dict[str, Any]])
def list_materialrequirementplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaterialRequirementPlan records with pagination and filtering."""
    svc = MaterialRequirementPlanService()
    items = svc.list_materialrequirementplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/materialrequirementplans/{item_id}", response_model=Dict[str, Any])
def get_materialrequirementplan_by_id(item_id: int):
    """Retrieve detailed record for MaterialRequirementPlan by ID."""
    svc = MaterialRequirementPlanService()
    item = svc.get_materialrequirementplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaterialRequirementPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/materialrequirementplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_materialrequirementplan(payload: MaterialRequirementPlanCreateSchema):
    """Create new MaterialRequirementPlan instance in enterprise repository."""
    svc = MaterialRequirementPlanService()
    try:
        item = svc.create_materialrequirementplan(
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

@router.put("/materialrequirementplans/{item_id}", response_model=Dict[str, Any])
def update_materialrequirementplan(item_id: int, payload: MaterialRequirementPlanUpdateSchema):
    """Update existing MaterialRequirementPlan record fields."""
    svc = MaterialRequirementPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_materialrequirementplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaterialRequirementPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/materialrequirementplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_materialrequirementplan(item_id: int, hard: bool = Query(False)):
    """Delete MaterialRequirementPlan record (soft-delete by default)."""
    svc = MaterialRequirementPlanService()
    ok = svc.delete_materialrequirementplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaterialRequirementPlan with ID {item_id} not found")
    return None

@router.get("/materialrequirementplans/analytics/metrics", response_model=Dict[str, Any])
def get_materialrequirementplan_metrics():
    """Calculate summary statistical KPIs for MaterialRequirementPlan collection."""
    svc = MaterialRequirementPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== DistributionPlan Endpoints ====================
@router.get("/distributionplans", response_model=List[Dict[str, Any]])
def list_distributionplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DistributionPlan records with pagination and filtering."""
    svc = DistributionPlanService()
    items = svc.list_distributionplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/distributionplans/{item_id}", response_model=Dict[str, Any])
def get_distributionplan_by_id(item_id: int):
    """Retrieve detailed record for DistributionPlan by ID."""
    svc = DistributionPlanService()
    item = svc.get_distributionplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DistributionPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/distributionplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_distributionplan(payload: DistributionPlanCreateSchema):
    """Create new DistributionPlan instance in enterprise repository."""
    svc = DistributionPlanService()
    try:
        item = svc.create_distributionplan(
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

@router.put("/distributionplans/{item_id}", response_model=Dict[str, Any])
def update_distributionplan(item_id: int, payload: DistributionPlanUpdateSchema):
    """Update existing DistributionPlan record fields."""
    svc = DistributionPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_distributionplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DistributionPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/distributionplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_distributionplan(item_id: int, hard: bool = Query(False)):
    """Delete DistributionPlan record (soft-delete by default)."""
    svc = DistributionPlanService()
    ok = svc.delete_distributionplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DistributionPlan with ID {item_id} not found")
    return None

@router.get("/distributionplans/analytics/metrics", response_model=Dict[str, Any])
def get_distributionplan_metrics():
    """Calculate summary statistical KPIs for DistributionPlan collection."""
    svc = DistributionPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== StockAllocationRule Endpoints ====================
@router.get("/stockallocationrules", response_model=List[Dict[str, Any]])
def list_stockallocationrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StockAllocationRule records with pagination and filtering."""
    svc = StockAllocationRuleService()
    items = svc.list_stockallocationrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/stockallocationrules/{item_id}", response_model=Dict[str, Any])
def get_stockallocationrule_by_id(item_id: int):
    """Retrieve detailed record for StockAllocationRule by ID."""
    svc = StockAllocationRuleService()
    item = svc.get_stockallocationrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StockAllocationRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/stockallocationrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_stockallocationrule(payload: StockAllocationRuleCreateSchema):
    """Create new StockAllocationRule instance in enterprise repository."""
    svc = StockAllocationRuleService()
    try:
        item = svc.create_stockallocationrule(
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

@router.put("/stockallocationrules/{item_id}", response_model=Dict[str, Any])
def update_stockallocationrule(item_id: int, payload: StockAllocationRuleUpdateSchema):
    """Update existing StockAllocationRule record fields."""
    svc = StockAllocationRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_stockallocationrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StockAllocationRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/stockallocationrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stockallocationrule(item_id: int, hard: bool = Query(False)):
    """Delete StockAllocationRule record (soft-delete by default)."""
    svc = StockAllocationRuleService()
    ok = svc.delete_stockallocationrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StockAllocationRule with ID {item_id} not found")
    return None

@router.get("/stockallocationrules/analytics/metrics", response_model=Dict[str, Any])
def get_stockallocationrule_metrics():
    """Calculate summary statistical KPIs for StockAllocationRule collection."""
    svc = StockAllocationRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierCommitment Endpoints ====================
@router.get("/suppliercommitments", response_model=List[Dict[str, Any]])
def list_suppliercommitments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierCommitment records with pagination and filtering."""
    svc = SupplierCommitmentService()
    items = svc.list_suppliercommitments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/suppliercommitments/{item_id}", response_model=Dict[str, Any])
def get_suppliercommitment_by_id(item_id: int):
    """Retrieve detailed record for SupplierCommitment by ID."""
    svc = SupplierCommitmentService()
    item = svc.get_suppliercommitment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierCommitment with ID {item_id} not found")
    return item.to_dict()

@router.post("/suppliercommitments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_suppliercommitment(payload: SupplierCommitmentCreateSchema):
    """Create new SupplierCommitment instance in enterprise repository."""
    svc = SupplierCommitmentService()
    try:
        item = svc.create_suppliercommitment(
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

@router.put("/suppliercommitments/{item_id}", response_model=Dict[str, Any])
def update_suppliercommitment(item_id: int, payload: SupplierCommitmentUpdateSchema):
    """Update existing SupplierCommitment record fields."""
    svc = SupplierCommitmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_suppliercommitment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierCommitment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/suppliercommitments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_suppliercommitment(item_id: int, hard: bool = Query(False)):
    """Delete SupplierCommitment record (soft-delete by default)."""
    svc = SupplierCommitmentService()
    ok = svc.delete_suppliercommitment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierCommitment with ID {item_id} not found")
    return None

@router.get("/suppliercommitments/analytics/metrics", response_model=Dict[str, Any])
def get_suppliercommitment_metrics():
    """Calculate summary statistical KPIs for SupplierCommitment collection."""
    svc = SupplierCommitmentService()
    return svc.calculate_aggregate_metrics()

# ==================== ForecastAccuracyMetric Endpoints ====================
@router.get("/forecastaccuracymetrics", response_model=List[Dict[str, Any]])
def list_forecastaccuracymetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ForecastAccuracyMetric records with pagination and filtering."""
    svc = ForecastAccuracyMetricService()
    items = svc.list_forecastaccuracymetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/forecastaccuracymetrics/{item_id}", response_model=Dict[str, Any])
def get_forecastaccuracymetric_by_id(item_id: int):
    """Retrieve detailed record for ForecastAccuracyMetric by ID."""
    svc = ForecastAccuracyMetricService()
    item = svc.get_forecastaccuracymetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ForecastAccuracyMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/forecastaccuracymetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_forecastaccuracymetric(payload: ForecastAccuracyMetricCreateSchema):
    """Create new ForecastAccuracyMetric instance in enterprise repository."""
    svc = ForecastAccuracyMetricService()
    try:
        item = svc.create_forecastaccuracymetric(
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

@router.put("/forecastaccuracymetrics/{item_id}", response_model=Dict[str, Any])
def update_forecastaccuracymetric(item_id: int, payload: ForecastAccuracyMetricUpdateSchema):
    """Update existing ForecastAccuracyMetric record fields."""
    svc = ForecastAccuracyMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_forecastaccuracymetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ForecastAccuracyMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/forecastaccuracymetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_forecastaccuracymetric(item_id: int, hard: bool = Query(False)):
    """Delete ForecastAccuracyMetric record (soft-delete by default)."""
    svc = ForecastAccuracyMetricService()
    ok = svc.delete_forecastaccuracymetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ForecastAccuracyMetric with ID {item_id} not found")
    return None

@router.get("/forecastaccuracymetrics/analytics/metrics", response_model=Dict[str, Any])
def get_forecastaccuracymetric_metrics():
    """Calculate summary statistical KPIs for ForecastAccuracyMetric collection."""
    svc = ForecastAccuracyMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== InventoryBufferZone Endpoints ====================
@router.get("/inventorybufferzones", response_model=List[Dict[str, Any]])
def list_inventorybufferzones(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InventoryBufferZone records with pagination and filtering."""
    svc = InventoryBufferZoneService()
    items = svc.list_inventorybufferzones(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inventorybufferzones/{item_id}", response_model=Dict[str, Any])
def get_inventorybufferzone_by_id(item_id: int):
    """Retrieve detailed record for InventoryBufferZone by ID."""
    svc = InventoryBufferZoneService()
    item = svc.get_inventorybufferzone_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InventoryBufferZone with ID {item_id} not found")
    return item.to_dict()

@router.post("/inventorybufferzones", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inventorybufferzone(payload: InventoryBufferZoneCreateSchema):
    """Create new InventoryBufferZone instance in enterprise repository."""
    svc = InventoryBufferZoneService()
    try:
        item = svc.create_inventorybufferzone(
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

@router.put("/inventorybufferzones/{item_id}", response_model=Dict[str, Any])
def update_inventorybufferzone(item_id: int, payload: InventoryBufferZoneUpdateSchema):
    """Update existing InventoryBufferZone record fields."""
    svc = InventoryBufferZoneService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inventorybufferzone(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InventoryBufferZone with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inventorybufferzones/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inventorybufferzone(item_id: int, hard: bool = Query(False)):
    """Delete InventoryBufferZone record (soft-delete by default)."""
    svc = InventoryBufferZoneService()
    ok = svc.delete_inventorybufferzone(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InventoryBufferZone with ID {item_id} not found")
    return None

@router.get("/inventorybufferzones/analytics/metrics", response_model=Dict[str, Any])
def get_inventorybufferzone_metrics():
    """Calculate summary statistical KPIs for InventoryBufferZone collection."""
    svc = InventoryBufferZoneService()
    return svc.calculate_aggregate_metrics()

# ==================== MasterProductionSchedule Endpoints ====================
@router.get("/masterproductionschedules", response_model=List[Dict[str, Any]])
def list_masterproductionschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MasterProductionSchedule records with pagination and filtering."""
    svc = MasterProductionScheduleService()
    items = svc.list_masterproductionschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/masterproductionschedules/{item_id}", response_model=Dict[str, Any])
def get_masterproductionschedule_by_id(item_id: int):
    """Retrieve detailed record for MasterProductionSchedule by ID."""
    svc = MasterProductionScheduleService()
    item = svc.get_masterproductionschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MasterProductionSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/masterproductionschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_masterproductionschedule(payload: MasterProductionScheduleCreateSchema):
    """Create new MasterProductionSchedule instance in enterprise repository."""
    svc = MasterProductionScheduleService()
    try:
        item = svc.create_masterproductionschedule(
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

@router.put("/masterproductionschedules/{item_id}", response_model=Dict[str, Any])
def update_masterproductionschedule(item_id: int, payload: MasterProductionScheduleUpdateSchema):
    """Update existing MasterProductionSchedule record fields."""
    svc = MasterProductionScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_masterproductionschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MasterProductionSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/masterproductionschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_masterproductionschedule(item_id: int, hard: bool = Query(False)):
    """Delete MasterProductionSchedule record (soft-delete by default)."""
    svc = MasterProductionScheduleService()
    ok = svc.delete_masterproductionschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MasterProductionSchedule with ID {item_id} not found")
    return None

@router.get("/masterproductionschedules/analytics/metrics", response_model=Dict[str, Any])
def get_masterproductionschedule_metrics():
    """Calculate summary statistical KPIs for MasterProductionSchedule collection."""
    svc = MasterProductionScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== BottleneckWorkstation Endpoints ====================
@router.get("/bottleneckworkstations", response_model=List[Dict[str, Any]])
def list_bottleneckworkstations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BottleneckWorkstation records with pagination and filtering."""
    svc = BottleneckWorkstationService()
    items = svc.list_bottleneckworkstations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bottleneckworkstations/{item_id}", response_model=Dict[str, Any])
def get_bottleneckworkstation_by_id(item_id: int):
    """Retrieve detailed record for BottleneckWorkstation by ID."""
    svc = BottleneckWorkstationService()
    item = svc.get_bottleneckworkstation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BottleneckWorkstation with ID {item_id} not found")
    return item.to_dict()

@router.post("/bottleneckworkstations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bottleneckworkstation(payload: BottleneckWorkstationCreateSchema):
    """Create new BottleneckWorkstation instance in enterprise repository."""
    svc = BottleneckWorkstationService()
    try:
        item = svc.create_bottleneckworkstation(
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

@router.put("/bottleneckworkstations/{item_id}", response_model=Dict[str, Any])
def update_bottleneckworkstation(item_id: int, payload: BottleneckWorkstationUpdateSchema):
    """Update existing BottleneckWorkstation record fields."""
    svc = BottleneckWorkstationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bottleneckworkstation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BottleneckWorkstation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bottleneckworkstations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bottleneckworkstation(item_id: int, hard: bool = Query(False)):
    """Delete BottleneckWorkstation record (soft-delete by default)."""
    svc = BottleneckWorkstationService()
    ok = svc.delete_bottleneckworkstation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BottleneckWorkstation with ID {item_id} not found")
    return None

@router.get("/bottleneckworkstations/analytics/metrics", response_model=Dict[str, Any])
def get_bottleneckworkstation_metrics():
    """Calculate summary statistical KPIs for BottleneckWorkstation collection."""
    svc = BottleneckWorkstationService()
    return svc.calculate_aggregate_metrics()

# ==================== ScenarioComparison Endpoints ====================
@router.get("/scenariocomparisons", response_model=List[Dict[str, Any]])
def list_scenariocomparisons(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ScenarioComparison records with pagination and filtering."""
    svc = ScenarioComparisonService()
    items = svc.list_scenariocomparisons(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/scenariocomparisons/{item_id}", response_model=Dict[str, Any])
def get_scenariocomparison_by_id(item_id: int):
    """Retrieve detailed record for ScenarioComparison by ID."""
    svc = ScenarioComparisonService()
    item = svc.get_scenariocomparison_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ScenarioComparison with ID {item_id} not found")
    return item.to_dict()

@router.post("/scenariocomparisons", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_scenariocomparison(payload: ScenarioComparisonCreateSchema):
    """Create new ScenarioComparison instance in enterprise repository."""
    svc = ScenarioComparisonService()
    try:
        item = svc.create_scenariocomparison(
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

@router.put("/scenariocomparisons/{item_id}", response_model=Dict[str, Any])
def update_scenariocomparison(item_id: int, payload: ScenarioComparisonUpdateSchema):
    """Update existing ScenarioComparison record fields."""
    svc = ScenarioComparisonService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_scenariocomparison(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ScenarioComparison with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/scenariocomparisons/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scenariocomparison(item_id: int, hard: bool = Query(False)):
    """Delete ScenarioComparison record (soft-delete by default)."""
    svc = ScenarioComparisonService()
    ok = svc.delete_scenariocomparison(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ScenarioComparison with ID {item_id} not found")
    return None

@router.get("/scenariocomparisons/analytics/metrics", response_model=Dict[str, Any])
def get_scenariocomparison_metrics():
    """Calculate summary statistical KPIs for ScenarioComparison collection."""
    svc = ScenarioComparisonService()
    return svc.calculate_aggregate_metrics()

# ==================== ExpeditedShipmentOrder Endpoints ====================
@router.get("/expeditedshipmentorders", response_model=List[Dict[str, Any]])
def list_expeditedshipmentorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExpeditedShipmentOrder records with pagination and filtering."""
    svc = ExpeditedShipmentOrderService()
    items = svc.list_expeditedshipmentorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/expeditedshipmentorders/{item_id}", response_model=Dict[str, Any])
def get_expeditedshipmentorder_by_id(item_id: int):
    """Retrieve detailed record for ExpeditedShipmentOrder by ID."""
    svc = ExpeditedShipmentOrderService()
    item = svc.get_expeditedshipmentorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExpeditedShipmentOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/expeditedshipmentorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_expeditedshipmentorder(payload: ExpeditedShipmentOrderCreateSchema):
    """Create new ExpeditedShipmentOrder instance in enterprise repository."""
    svc = ExpeditedShipmentOrderService()
    try:
        item = svc.create_expeditedshipmentorder(
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

@router.put("/expeditedshipmentorders/{item_id}", response_model=Dict[str, Any])
def update_expeditedshipmentorder(item_id: int, payload: ExpeditedShipmentOrderUpdateSchema):
    """Update existing ExpeditedShipmentOrder record fields."""
    svc = ExpeditedShipmentOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_expeditedshipmentorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExpeditedShipmentOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/expeditedshipmentorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expeditedshipmentorder(item_id: int, hard: bool = Query(False)):
    """Delete ExpeditedShipmentOrder record (soft-delete by default)."""
    svc = ExpeditedShipmentOrderService()
    ok = svc.delete_expeditedshipmentorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExpeditedShipmentOrder with ID {item_id} not found")
    return None

@router.get("/expeditedshipmentorders/analytics/metrics", response_model=Dict[str, Any])
def get_expeditedshipmentorder_metrics():
    """Calculate summary statistical KPIs for ExpeditedShipmentOrder collection."""
    svc = ExpeditedShipmentOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutiveSOPConsensus Endpoints ====================
@router.get("/executivesopconsensuss", response_model=List[Dict[str, Any]])
def list_executivesopconsensuss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutiveSOPConsensus records with pagination and filtering."""
    svc = ExecutiveSOPConsensusService()
    items = svc.list_executivesopconsensuss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executivesopconsensuss/{item_id}", response_model=Dict[str, Any])
def get_executivesopconsensus_by_id(item_id: int):
    """Retrieve detailed record for ExecutiveSOPConsensus by ID."""
    svc = ExecutiveSOPConsensusService()
    item = svc.get_executivesopconsensus_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutiveSOPConsensus with ID {item_id} not found")
    return item.to_dict()

@router.post("/executivesopconsensuss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executivesopconsensus(payload: ExecutiveSOPConsensusCreateSchema):
    """Create new ExecutiveSOPConsensus instance in enterprise repository."""
    svc = ExecutiveSOPConsensusService()
    try:
        item = svc.create_executivesopconsensus(
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

@router.put("/executivesopconsensuss/{item_id}", response_model=Dict[str, Any])
def update_executivesopconsensus(item_id: int, payload: ExecutiveSOPConsensusUpdateSchema):
    """Update existing ExecutiveSOPConsensus record fields."""
    svc = ExecutiveSOPConsensusService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executivesopconsensus(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutiveSOPConsensus with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executivesopconsensuss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executivesopconsensus(item_id: int, hard: bool = Query(False)):
    """Delete ExecutiveSOPConsensus record (soft-delete by default)."""
    svc = ExecutiveSOPConsensusService()
    ok = svc.delete_executivesopconsensus(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutiveSOPConsensus with ID {item_id} not found")
    return None

@router.get("/executivesopconsensuss/analytics/metrics", response_model=Dict[str, Any])
def get_executivesopconsensus_metrics():
    """Calculate summary statistical KPIs for ExecutiveSOPConsensus collection."""
    svc = ExecutiveSOPConsensusService()
    return svc.calculate_aggregate_metrics()

