"""
Executive Business Intelligence & OLAP - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    DataCubeService,
    MetricDefinitionService,
    DimensionFilterService,
    DashboardWidgetService,
    CohortAnalysisService,
    ForecastModelService,
    AnomalyAlertService,
    ExecutiveKPIService,
    ReportScheduleService,
    UserRetentionService,
    LTVProjectionService,
    InventoryTurnoverService,
    SalesAttainmentService,
    FinancialSpreadService,
    BenchmarkComparisonService,
    ExportJobService,
)
from .schemas import (
    DataCubeCreateSchema, DataCubeUpdateSchema, DataCubeResponseSchema,
    MetricDefinitionCreateSchema, MetricDefinitionUpdateSchema, MetricDefinitionResponseSchema,
    DimensionFilterCreateSchema, DimensionFilterUpdateSchema, DimensionFilterResponseSchema,
    DashboardWidgetCreateSchema, DashboardWidgetUpdateSchema, DashboardWidgetResponseSchema,
    CohortAnalysisCreateSchema, CohortAnalysisUpdateSchema, CohortAnalysisResponseSchema,
    ForecastModelCreateSchema, ForecastModelUpdateSchema, ForecastModelResponseSchema,
    AnomalyAlertCreateSchema, AnomalyAlertUpdateSchema, AnomalyAlertResponseSchema,
    ExecutiveKPICreateSchema, ExecutiveKPIUpdateSchema, ExecutiveKPIResponseSchema,
    ReportScheduleCreateSchema, ReportScheduleUpdateSchema, ReportScheduleResponseSchema,
    UserRetentionCreateSchema, UserRetentionUpdateSchema, UserRetentionResponseSchema,
    LTVProjectionCreateSchema, LTVProjectionUpdateSchema, LTVProjectionResponseSchema,
    InventoryTurnoverCreateSchema, InventoryTurnoverUpdateSchema, InventoryTurnoverResponseSchema,
    SalesAttainmentCreateSchema, SalesAttainmentUpdateSchema, SalesAttainmentResponseSchema,
    FinancialSpreadCreateSchema, FinancialSpreadUpdateSchema, FinancialSpreadResponseSchema,
    BenchmarkComparisonCreateSchema, BenchmarkComparisonUpdateSchema, BenchmarkComparisonResponseSchema,
    ExportJobCreateSchema, ExportJobUpdateSchema, ExportJobResponseSchema,
)

router = APIRouter(prefix="/analytics", tags=["Executive Business Intelligence & OLAP"])

# ==================== DataCube Endpoints ====================
@router.get("/datacubes", response_model=List[Dict[str, Any]])
def list_datacubes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataCube records with pagination and filtering."""
    svc = DataCubeService()
    items = svc.list_datacubes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/datacubes/{item_id}", response_model=Dict[str, Any])
def get_datacube_by_id(item_id: int):
    """Retrieve detailed record for DataCube by ID."""
    svc = DataCubeService()
    item = svc.get_datacube_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataCube with ID {item_id} not found")
    return item.to_dict()

@router.post("/datacubes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_datacube(payload: DataCubeCreateSchema):
    """Create new DataCube instance in enterprise repository."""
    svc = DataCubeService()
    try:
        item = svc.create_datacube(
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

@router.put("/datacubes/{item_id}", response_model=Dict[str, Any])
def update_datacube(item_id: int, payload: DataCubeUpdateSchema):
    """Update existing DataCube record fields."""
    svc = DataCubeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_datacube(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataCube with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/datacubes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_datacube(item_id: int, hard: bool = Query(False)):
    """Delete DataCube record (soft-delete by default)."""
    svc = DataCubeService()
    ok = svc.delete_datacube(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataCube with ID {item_id} not found")
    return None

@router.get("/datacubes/analytics/metrics", response_model=Dict[str, Any])
def get_datacube_metrics():
    """Calculate summary statistical KPIs for DataCube collection."""
    svc = DataCubeService()
    return svc.calculate_aggregate_metrics()

# ==================== MetricDefinition Endpoints ====================
@router.get("/metricdefinitions", response_model=List[Dict[str, Any]])
def list_metricdefinitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MetricDefinition records with pagination and filtering."""
    svc = MetricDefinitionService()
    items = svc.list_metricdefinitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/metricdefinitions/{item_id}", response_model=Dict[str, Any])
def get_metricdefinition_by_id(item_id: int):
    """Retrieve detailed record for MetricDefinition by ID."""
    svc = MetricDefinitionService()
    item = svc.get_metricdefinition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MetricDefinition with ID {item_id} not found")
    return item.to_dict()

@router.post("/metricdefinitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_metricdefinition(payload: MetricDefinitionCreateSchema):
    """Create new MetricDefinition instance in enterprise repository."""
    svc = MetricDefinitionService()
    try:
        item = svc.create_metricdefinition(
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

@router.put("/metricdefinitions/{item_id}", response_model=Dict[str, Any])
def update_metricdefinition(item_id: int, payload: MetricDefinitionUpdateSchema):
    """Update existing MetricDefinition record fields."""
    svc = MetricDefinitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_metricdefinition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MetricDefinition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/metricdefinitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_metricdefinition(item_id: int, hard: bool = Query(False)):
    """Delete MetricDefinition record (soft-delete by default)."""
    svc = MetricDefinitionService()
    ok = svc.delete_metricdefinition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MetricDefinition with ID {item_id} not found")
    return None

@router.get("/metricdefinitions/analytics/metrics", response_model=Dict[str, Any])
def get_metricdefinition_metrics():
    """Calculate summary statistical KPIs for MetricDefinition collection."""
    svc = MetricDefinitionService()
    return svc.calculate_aggregate_metrics()

# ==================== DimensionFilter Endpoints ====================
@router.get("/dimensionfilters", response_model=List[Dict[str, Any]])
def list_dimensionfilters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DimensionFilter records with pagination and filtering."""
    svc = DimensionFilterService()
    items = svc.list_dimensionfilters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dimensionfilters/{item_id}", response_model=Dict[str, Any])
def get_dimensionfilter_by_id(item_id: int):
    """Retrieve detailed record for DimensionFilter by ID."""
    svc = DimensionFilterService()
    item = svc.get_dimensionfilter_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DimensionFilter with ID {item_id} not found")
    return item.to_dict()

@router.post("/dimensionfilters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dimensionfilter(payload: DimensionFilterCreateSchema):
    """Create new DimensionFilter instance in enterprise repository."""
    svc = DimensionFilterService()
    try:
        item = svc.create_dimensionfilter(
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

@router.put("/dimensionfilters/{item_id}", response_model=Dict[str, Any])
def update_dimensionfilter(item_id: int, payload: DimensionFilterUpdateSchema):
    """Update existing DimensionFilter record fields."""
    svc = DimensionFilterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dimensionfilter(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DimensionFilter with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dimensionfilters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dimensionfilter(item_id: int, hard: bool = Query(False)):
    """Delete DimensionFilter record (soft-delete by default)."""
    svc = DimensionFilterService()
    ok = svc.delete_dimensionfilter(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DimensionFilter with ID {item_id} not found")
    return None

@router.get("/dimensionfilters/analytics/metrics", response_model=Dict[str, Any])
def get_dimensionfilter_metrics():
    """Calculate summary statistical KPIs for DimensionFilter collection."""
    svc = DimensionFilterService()
    return svc.calculate_aggregate_metrics()

# ==================== DashboardWidget Endpoints ====================
@router.get("/dashboardwidgets", response_model=List[Dict[str, Any]])
def list_dashboardwidgets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DashboardWidget records with pagination and filtering."""
    svc = DashboardWidgetService()
    items = svc.list_dashboardwidgets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dashboardwidgets/{item_id}", response_model=Dict[str, Any])
def get_dashboardwidget_by_id(item_id: int):
    """Retrieve detailed record for DashboardWidget by ID."""
    svc = DashboardWidgetService()
    item = svc.get_dashboardwidget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DashboardWidget with ID {item_id} not found")
    return item.to_dict()

@router.post("/dashboardwidgets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dashboardwidget(payload: DashboardWidgetCreateSchema):
    """Create new DashboardWidget instance in enterprise repository."""
    svc = DashboardWidgetService()
    try:
        item = svc.create_dashboardwidget(
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

@router.put("/dashboardwidgets/{item_id}", response_model=Dict[str, Any])
def update_dashboardwidget(item_id: int, payload: DashboardWidgetUpdateSchema):
    """Update existing DashboardWidget record fields."""
    svc = DashboardWidgetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dashboardwidget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DashboardWidget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dashboardwidgets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dashboardwidget(item_id: int, hard: bool = Query(False)):
    """Delete DashboardWidget record (soft-delete by default)."""
    svc = DashboardWidgetService()
    ok = svc.delete_dashboardwidget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DashboardWidget with ID {item_id} not found")
    return None

@router.get("/dashboardwidgets/analytics/metrics", response_model=Dict[str, Any])
def get_dashboardwidget_metrics():
    """Calculate summary statistical KPIs for DashboardWidget collection."""
    svc = DashboardWidgetService()
    return svc.calculate_aggregate_metrics()

# ==================== CohortAnalysis Endpoints ====================
@router.get("/cohortanalysiss", response_model=List[Dict[str, Any]])
def list_cohortanalysiss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CohortAnalysis records with pagination and filtering."""
    svc = CohortAnalysisService()
    items = svc.list_cohortanalysiss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cohortanalysiss/{item_id}", response_model=Dict[str, Any])
def get_cohortanalysis_by_id(item_id: int):
    """Retrieve detailed record for CohortAnalysis by ID."""
    svc = CohortAnalysisService()
    item = svc.get_cohortanalysis_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CohortAnalysis with ID {item_id} not found")
    return item.to_dict()

@router.post("/cohortanalysiss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cohortanalysis(payload: CohortAnalysisCreateSchema):
    """Create new CohortAnalysis instance in enterprise repository."""
    svc = CohortAnalysisService()
    try:
        item = svc.create_cohortanalysis(
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

@router.put("/cohortanalysiss/{item_id}", response_model=Dict[str, Any])
def update_cohortanalysis(item_id: int, payload: CohortAnalysisUpdateSchema):
    """Update existing CohortAnalysis record fields."""
    svc = CohortAnalysisService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cohortanalysis(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CohortAnalysis with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cohortanalysiss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cohortanalysis(item_id: int, hard: bool = Query(False)):
    """Delete CohortAnalysis record (soft-delete by default)."""
    svc = CohortAnalysisService()
    ok = svc.delete_cohortanalysis(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CohortAnalysis with ID {item_id} not found")
    return None

@router.get("/cohortanalysiss/analytics/metrics", response_model=Dict[str, Any])
def get_cohortanalysis_metrics():
    """Calculate summary statistical KPIs for CohortAnalysis collection."""
    svc = CohortAnalysisService()
    return svc.calculate_aggregate_metrics()

# ==================== ForecastModel Endpoints ====================
@router.get("/forecastmodels", response_model=List[Dict[str, Any]])
def list_forecastmodels(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ForecastModel records with pagination and filtering."""
    svc = ForecastModelService()
    items = svc.list_forecastmodels(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/forecastmodels/{item_id}", response_model=Dict[str, Any])
def get_forecastmodel_by_id(item_id: int):
    """Retrieve detailed record for ForecastModel by ID."""
    svc = ForecastModelService()
    item = svc.get_forecastmodel_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ForecastModel with ID {item_id} not found")
    return item.to_dict()

@router.post("/forecastmodels", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_forecastmodel(payload: ForecastModelCreateSchema):
    """Create new ForecastModel instance in enterprise repository."""
    svc = ForecastModelService()
    try:
        item = svc.create_forecastmodel(
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

@router.put("/forecastmodels/{item_id}", response_model=Dict[str, Any])
def update_forecastmodel(item_id: int, payload: ForecastModelUpdateSchema):
    """Update existing ForecastModel record fields."""
    svc = ForecastModelService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_forecastmodel(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ForecastModel with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/forecastmodels/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_forecastmodel(item_id: int, hard: bool = Query(False)):
    """Delete ForecastModel record (soft-delete by default)."""
    svc = ForecastModelService()
    ok = svc.delete_forecastmodel(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ForecastModel with ID {item_id} not found")
    return None

@router.get("/forecastmodels/analytics/metrics", response_model=Dict[str, Any])
def get_forecastmodel_metrics():
    """Calculate summary statistical KPIs for ForecastModel collection."""
    svc = ForecastModelService()
    return svc.calculate_aggregate_metrics()

# ==================== AnomalyAlert Endpoints ====================
@router.get("/anomalyalerts", response_model=List[Dict[str, Any]])
def list_anomalyalerts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AnomalyAlert records with pagination and filtering."""
    svc = AnomalyAlertService()
    items = svc.list_anomalyalerts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/anomalyalerts/{item_id}", response_model=Dict[str, Any])
def get_anomalyalert_by_id(item_id: int):
    """Retrieve detailed record for AnomalyAlert by ID."""
    svc = AnomalyAlertService()
    item = svc.get_anomalyalert_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AnomalyAlert with ID {item_id} not found")
    return item.to_dict()

@router.post("/anomalyalerts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_anomalyalert(payload: AnomalyAlertCreateSchema):
    """Create new AnomalyAlert instance in enterprise repository."""
    svc = AnomalyAlertService()
    try:
        item = svc.create_anomalyalert(
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

@router.put("/anomalyalerts/{item_id}", response_model=Dict[str, Any])
def update_anomalyalert(item_id: int, payload: AnomalyAlertUpdateSchema):
    """Update existing AnomalyAlert record fields."""
    svc = AnomalyAlertService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_anomalyalert(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AnomalyAlert with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/anomalyalerts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_anomalyalert(item_id: int, hard: bool = Query(False)):
    """Delete AnomalyAlert record (soft-delete by default)."""
    svc = AnomalyAlertService()
    ok = svc.delete_anomalyalert(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AnomalyAlert with ID {item_id} not found")
    return None

@router.get("/anomalyalerts/analytics/metrics", response_model=Dict[str, Any])
def get_anomalyalert_metrics():
    """Calculate summary statistical KPIs for AnomalyAlert collection."""
    svc = AnomalyAlertService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutiveKPI Endpoints ====================
@router.get("/executivekpis", response_model=List[Dict[str, Any]])
def list_executivekpis(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutiveKPI records with pagination and filtering."""
    svc = ExecutiveKPIService()
    items = svc.list_executivekpis(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executivekpis/{item_id}", response_model=Dict[str, Any])
def get_executivekpi_by_id(item_id: int):
    """Retrieve detailed record for ExecutiveKPI by ID."""
    svc = ExecutiveKPIService()
    item = svc.get_executivekpi_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutiveKPI with ID {item_id} not found")
    return item.to_dict()

@router.post("/executivekpis", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executivekpi(payload: ExecutiveKPICreateSchema):
    """Create new ExecutiveKPI instance in enterprise repository."""
    svc = ExecutiveKPIService()
    try:
        item = svc.create_executivekpi(
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

@router.put("/executivekpis/{item_id}", response_model=Dict[str, Any])
def update_executivekpi(item_id: int, payload: ExecutiveKPIUpdateSchema):
    """Update existing ExecutiveKPI record fields."""
    svc = ExecutiveKPIService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executivekpi(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutiveKPI with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executivekpis/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executivekpi(item_id: int, hard: bool = Query(False)):
    """Delete ExecutiveKPI record (soft-delete by default)."""
    svc = ExecutiveKPIService()
    ok = svc.delete_executivekpi(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutiveKPI with ID {item_id} not found")
    return None

@router.get("/executivekpis/analytics/metrics", response_model=Dict[str, Any])
def get_executivekpi_metrics():
    """Calculate summary statistical KPIs for ExecutiveKPI collection."""
    svc = ExecutiveKPIService()
    return svc.calculate_aggregate_metrics()

# ==================== ReportSchedule Endpoints ====================
@router.get("/reportschedules", response_model=List[Dict[str, Any]])
def list_reportschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReportSchedule records with pagination and filtering."""
    svc = ReportScheduleService()
    items = svc.list_reportschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/reportschedules/{item_id}", response_model=Dict[str, Any])
def get_reportschedule_by_id(item_id: int):
    """Retrieve detailed record for ReportSchedule by ID."""
    svc = ReportScheduleService()
    item = svc.get_reportschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReportSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/reportschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_reportschedule(payload: ReportScheduleCreateSchema):
    """Create new ReportSchedule instance in enterprise repository."""
    svc = ReportScheduleService()
    try:
        item = svc.create_reportschedule(
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

@router.put("/reportschedules/{item_id}", response_model=Dict[str, Any])
def update_reportschedule(item_id: int, payload: ReportScheduleUpdateSchema):
    """Update existing ReportSchedule record fields."""
    svc = ReportScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_reportschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReportSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/reportschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reportschedule(item_id: int, hard: bool = Query(False)):
    """Delete ReportSchedule record (soft-delete by default)."""
    svc = ReportScheduleService()
    ok = svc.delete_reportschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReportSchedule with ID {item_id} not found")
    return None

@router.get("/reportschedules/analytics/metrics", response_model=Dict[str, Any])
def get_reportschedule_metrics():
    """Calculate summary statistical KPIs for ReportSchedule collection."""
    svc = ReportScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== UserRetention Endpoints ====================
@router.get("/userretentions", response_model=List[Dict[str, Any]])
def list_userretentions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UserRetention records with pagination and filtering."""
    svc = UserRetentionService()
    items = svc.list_userretentions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/userretentions/{item_id}", response_model=Dict[str, Any])
def get_userretention_by_id(item_id: int):
    """Retrieve detailed record for UserRetention by ID."""
    svc = UserRetentionService()
    item = svc.get_userretention_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UserRetention with ID {item_id} not found")
    return item.to_dict()

@router.post("/userretentions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_userretention(payload: UserRetentionCreateSchema):
    """Create new UserRetention instance in enterprise repository."""
    svc = UserRetentionService()
    try:
        item = svc.create_userretention(
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

@router.put("/userretentions/{item_id}", response_model=Dict[str, Any])
def update_userretention(item_id: int, payload: UserRetentionUpdateSchema):
    """Update existing UserRetention record fields."""
    svc = UserRetentionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_userretention(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UserRetention with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/userretentions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_userretention(item_id: int, hard: bool = Query(False)):
    """Delete UserRetention record (soft-delete by default)."""
    svc = UserRetentionService()
    ok = svc.delete_userretention(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UserRetention with ID {item_id} not found")
    return None

@router.get("/userretentions/analytics/metrics", response_model=Dict[str, Any])
def get_userretention_metrics():
    """Calculate summary statistical KPIs for UserRetention collection."""
    svc = UserRetentionService()
    return svc.calculate_aggregate_metrics()

# ==================== LTVProjection Endpoints ====================
@router.get("/ltvprojections", response_model=List[Dict[str, Any]])
def list_ltvprojections(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LTVProjection records with pagination and filtering."""
    svc = LTVProjectionService()
    items = svc.list_ltvprojections(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ltvprojections/{item_id}", response_model=Dict[str, Any])
def get_ltvprojection_by_id(item_id: int):
    """Retrieve detailed record for LTVProjection by ID."""
    svc = LTVProjectionService()
    item = svc.get_ltvprojection_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LTVProjection with ID {item_id} not found")
    return item.to_dict()

@router.post("/ltvprojections", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ltvprojection(payload: LTVProjectionCreateSchema):
    """Create new LTVProjection instance in enterprise repository."""
    svc = LTVProjectionService()
    try:
        item = svc.create_ltvprojection(
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

@router.put("/ltvprojections/{item_id}", response_model=Dict[str, Any])
def update_ltvprojection(item_id: int, payload: LTVProjectionUpdateSchema):
    """Update existing LTVProjection record fields."""
    svc = LTVProjectionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ltvprojection(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LTVProjection with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ltvprojections/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ltvprojection(item_id: int, hard: bool = Query(False)):
    """Delete LTVProjection record (soft-delete by default)."""
    svc = LTVProjectionService()
    ok = svc.delete_ltvprojection(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LTVProjection with ID {item_id} not found")
    return None

@router.get("/ltvprojections/analytics/metrics", response_model=Dict[str, Any])
def get_ltvprojection_metrics():
    """Calculate summary statistical KPIs for LTVProjection collection."""
    svc = LTVProjectionService()
    return svc.calculate_aggregate_metrics()

# ==================== InventoryTurnover Endpoints ====================
@router.get("/inventoryturnovers", response_model=List[Dict[str, Any]])
def list_inventoryturnovers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InventoryTurnover records with pagination and filtering."""
    svc = InventoryTurnoverService()
    items = svc.list_inventoryturnovers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inventoryturnovers/{item_id}", response_model=Dict[str, Any])
def get_inventoryturnover_by_id(item_id: int):
    """Retrieve detailed record for InventoryTurnover by ID."""
    svc = InventoryTurnoverService()
    item = svc.get_inventoryturnover_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InventoryTurnover with ID {item_id} not found")
    return item.to_dict()

@router.post("/inventoryturnovers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inventoryturnover(payload: InventoryTurnoverCreateSchema):
    """Create new InventoryTurnover instance in enterprise repository."""
    svc = InventoryTurnoverService()
    try:
        item = svc.create_inventoryturnover(
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

@router.put("/inventoryturnovers/{item_id}", response_model=Dict[str, Any])
def update_inventoryturnover(item_id: int, payload: InventoryTurnoverUpdateSchema):
    """Update existing InventoryTurnover record fields."""
    svc = InventoryTurnoverService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inventoryturnover(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InventoryTurnover with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inventoryturnovers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inventoryturnover(item_id: int, hard: bool = Query(False)):
    """Delete InventoryTurnover record (soft-delete by default)."""
    svc = InventoryTurnoverService()
    ok = svc.delete_inventoryturnover(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InventoryTurnover with ID {item_id} not found")
    return None

@router.get("/inventoryturnovers/analytics/metrics", response_model=Dict[str, Any])
def get_inventoryturnover_metrics():
    """Calculate summary statistical KPIs for InventoryTurnover collection."""
    svc = InventoryTurnoverService()
    return svc.calculate_aggregate_metrics()

# ==================== SalesAttainment Endpoints ====================
@router.get("/salesattainments", response_model=List[Dict[str, Any]])
def list_salesattainments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SalesAttainment records with pagination and filtering."""
    svc = SalesAttainmentService()
    items = svc.list_salesattainments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/salesattainments/{item_id}", response_model=Dict[str, Any])
def get_salesattainment_by_id(item_id: int):
    """Retrieve detailed record for SalesAttainment by ID."""
    svc = SalesAttainmentService()
    item = svc.get_salesattainment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SalesAttainment with ID {item_id} not found")
    return item.to_dict()

@router.post("/salesattainments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_salesattainment(payload: SalesAttainmentCreateSchema):
    """Create new SalesAttainment instance in enterprise repository."""
    svc = SalesAttainmentService()
    try:
        item = svc.create_salesattainment(
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

@router.put("/salesattainments/{item_id}", response_model=Dict[str, Any])
def update_salesattainment(item_id: int, payload: SalesAttainmentUpdateSchema):
    """Update existing SalesAttainment record fields."""
    svc = SalesAttainmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_salesattainment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SalesAttainment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/salesattainments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_salesattainment(item_id: int, hard: bool = Query(False)):
    """Delete SalesAttainment record (soft-delete by default)."""
    svc = SalesAttainmentService()
    ok = svc.delete_salesattainment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SalesAttainment with ID {item_id} not found")
    return None

@router.get("/salesattainments/analytics/metrics", response_model=Dict[str, Any])
def get_salesattainment_metrics():
    """Calculate summary statistical KPIs for SalesAttainment collection."""
    svc = SalesAttainmentService()
    return svc.calculate_aggregate_metrics()

# ==================== FinancialSpread Endpoints ====================
@router.get("/financialspreads", response_model=List[Dict[str, Any]])
def list_financialspreads(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FinancialSpread records with pagination and filtering."""
    svc = FinancialSpreadService()
    items = svc.list_financialspreads(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/financialspreads/{item_id}", response_model=Dict[str, Any])
def get_financialspread_by_id(item_id: int):
    """Retrieve detailed record for FinancialSpread by ID."""
    svc = FinancialSpreadService()
    item = svc.get_financialspread_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FinancialSpread with ID {item_id} not found")
    return item.to_dict()

@router.post("/financialspreads", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_financialspread(payload: FinancialSpreadCreateSchema):
    """Create new FinancialSpread instance in enterprise repository."""
    svc = FinancialSpreadService()
    try:
        item = svc.create_financialspread(
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

@router.put("/financialspreads/{item_id}", response_model=Dict[str, Any])
def update_financialspread(item_id: int, payload: FinancialSpreadUpdateSchema):
    """Update existing FinancialSpread record fields."""
    svc = FinancialSpreadService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_financialspread(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FinancialSpread with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/financialspreads/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_financialspread(item_id: int, hard: bool = Query(False)):
    """Delete FinancialSpread record (soft-delete by default)."""
    svc = FinancialSpreadService()
    ok = svc.delete_financialspread(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FinancialSpread with ID {item_id} not found")
    return None

@router.get("/financialspreads/analytics/metrics", response_model=Dict[str, Any])
def get_financialspread_metrics():
    """Calculate summary statistical KPIs for FinancialSpread collection."""
    svc = FinancialSpreadService()
    return svc.calculate_aggregate_metrics()

# ==================== BenchmarkComparison Endpoints ====================
@router.get("/benchmarkcomparisons", response_model=List[Dict[str, Any]])
def list_benchmarkcomparisons(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BenchmarkComparison records with pagination and filtering."""
    svc = BenchmarkComparisonService()
    items = svc.list_benchmarkcomparisons(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/benchmarkcomparisons/{item_id}", response_model=Dict[str, Any])
def get_benchmarkcomparison_by_id(item_id: int):
    """Retrieve detailed record for BenchmarkComparison by ID."""
    svc = BenchmarkComparisonService()
    item = svc.get_benchmarkcomparison_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BenchmarkComparison with ID {item_id} not found")
    return item.to_dict()

@router.post("/benchmarkcomparisons", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_benchmarkcomparison(payload: BenchmarkComparisonCreateSchema):
    """Create new BenchmarkComparison instance in enterprise repository."""
    svc = BenchmarkComparisonService()
    try:
        item = svc.create_benchmarkcomparison(
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

@router.put("/benchmarkcomparisons/{item_id}", response_model=Dict[str, Any])
def update_benchmarkcomparison(item_id: int, payload: BenchmarkComparisonUpdateSchema):
    """Update existing BenchmarkComparison record fields."""
    svc = BenchmarkComparisonService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_benchmarkcomparison(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BenchmarkComparison with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/benchmarkcomparisons/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_benchmarkcomparison(item_id: int, hard: bool = Query(False)):
    """Delete BenchmarkComparison record (soft-delete by default)."""
    svc = BenchmarkComparisonService()
    ok = svc.delete_benchmarkcomparison(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BenchmarkComparison with ID {item_id} not found")
    return None

@router.get("/benchmarkcomparisons/analytics/metrics", response_model=Dict[str, Any])
def get_benchmarkcomparison_metrics():
    """Calculate summary statistical KPIs for BenchmarkComparison collection."""
    svc = BenchmarkComparisonService()
    return svc.calculate_aggregate_metrics()

# ==================== ExportJob Endpoints ====================
@router.get("/exportjobs", response_model=List[Dict[str, Any]])
def list_exportjobs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExportJob records with pagination and filtering."""
    svc = ExportJobService()
    items = svc.list_exportjobs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/exportjobs/{item_id}", response_model=Dict[str, Any])
def get_exportjob_by_id(item_id: int):
    """Retrieve detailed record for ExportJob by ID."""
    svc = ExportJobService()
    item = svc.get_exportjob_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExportJob with ID {item_id} not found")
    return item.to_dict()

@router.post("/exportjobs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_exportjob(payload: ExportJobCreateSchema):
    """Create new ExportJob instance in enterprise repository."""
    svc = ExportJobService()
    try:
        item = svc.create_exportjob(
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

@router.put("/exportjobs/{item_id}", response_model=Dict[str, Any])
def update_exportjob(item_id: int, payload: ExportJobUpdateSchema):
    """Update existing ExportJob record fields."""
    svc = ExportJobService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_exportjob(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExportJob with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/exportjobs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exportjob(item_id: int, hard: bool = Query(False)):
    """Delete ExportJob record (soft-delete by default)."""
    svc = ExportJobService()
    ok = svc.delete_exportjob(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExportJob with ID {item_id} not found")
    return None

@router.get("/exportjobs/analytics/metrics", response_model=Dict[str, Any])
def get_exportjob_metrics():
    """Calculate summary statistical KPIs for ExportJob collection."""
    svc = ExportJobService()
    return svc.calculate_aggregate_metrics()

