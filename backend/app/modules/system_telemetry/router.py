"""
Distributed Telemetry & APM Observability - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ServiceHealthCheckProbeService,
    APMMetricTimeseriesService,
    DistributedTraceSpanService,
    ErrorCrashReportService,
    LatencySLOBudgetService,
    ServerNodeTelemetryService,
    DatabasePoolMetricService,
    MemoryHeapSnapshotService,
    AlertEscalationRuleService,
    IncidentPostMortemService,
    LogStreamingSinkService,
    SyntheticsMonitorJobService,
    CapacityPlanningTrendService,
    DeploymentReleaseMarkerService,
    TelemetryDashboardWidgetService,
    AnomalyDetectionAlertService,
)
from .schemas import (
    ServiceHealthCheckProbeCreateSchema, ServiceHealthCheckProbeUpdateSchema, ServiceHealthCheckProbeResponseSchema,
    APMMetricTimeseriesCreateSchema, APMMetricTimeseriesUpdateSchema, APMMetricTimeseriesResponseSchema,
    DistributedTraceSpanCreateSchema, DistributedTraceSpanUpdateSchema, DistributedTraceSpanResponseSchema,
    ErrorCrashReportCreateSchema, ErrorCrashReportUpdateSchema, ErrorCrashReportResponseSchema,
    LatencySLOBudgetCreateSchema, LatencySLOBudgetUpdateSchema, LatencySLOBudgetResponseSchema,
    ServerNodeTelemetryCreateSchema, ServerNodeTelemetryUpdateSchema, ServerNodeTelemetryResponseSchema,
    DatabasePoolMetricCreateSchema, DatabasePoolMetricUpdateSchema, DatabasePoolMetricResponseSchema,
    MemoryHeapSnapshotCreateSchema, MemoryHeapSnapshotUpdateSchema, MemoryHeapSnapshotResponseSchema,
    AlertEscalationRuleCreateSchema, AlertEscalationRuleUpdateSchema, AlertEscalationRuleResponseSchema,
    IncidentPostMortemCreateSchema, IncidentPostMortemUpdateSchema, IncidentPostMortemResponseSchema,
    LogStreamingSinkCreateSchema, LogStreamingSinkUpdateSchema, LogStreamingSinkResponseSchema,
    SyntheticsMonitorJobCreateSchema, SyntheticsMonitorJobUpdateSchema, SyntheticsMonitorJobResponseSchema,
    CapacityPlanningTrendCreateSchema, CapacityPlanningTrendUpdateSchema, CapacityPlanningTrendResponseSchema,
    DeploymentReleaseMarkerCreateSchema, DeploymentReleaseMarkerUpdateSchema, DeploymentReleaseMarkerResponseSchema,
    TelemetryDashboardWidgetCreateSchema, TelemetryDashboardWidgetUpdateSchema, TelemetryDashboardWidgetResponseSchema,
    AnomalyDetectionAlertCreateSchema, AnomalyDetectionAlertUpdateSchema, AnomalyDetectionAlertResponseSchema,
)

router = APIRouter(prefix="/system_telemetry", tags=["Distributed Telemetry & APM Observability"])

# ==================== ServiceHealthCheckProbe Endpoints ====================
@router.get("/servicehealthcheckprobes", response_model=List[Dict[str, Any]])
def list_servicehealthcheckprobes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceHealthCheckProbe records with pagination and filtering."""
    svc = ServiceHealthCheckProbeService()
    items = svc.list_servicehealthcheckprobes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicehealthcheckprobes/{item_id}", response_model=Dict[str, Any])
def get_servicehealthcheckprobe_by_id(item_id: int):
    """Retrieve detailed record for ServiceHealthCheckProbe by ID."""
    svc = ServiceHealthCheckProbeService()
    item = svc.get_servicehealthcheckprobe_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceHealthCheckProbe with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicehealthcheckprobes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicehealthcheckprobe(payload: ServiceHealthCheckProbeCreateSchema):
    """Create new ServiceHealthCheckProbe instance in enterprise repository."""
    svc = ServiceHealthCheckProbeService()
    try:
        item = svc.create_servicehealthcheckprobe(
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

@router.put("/servicehealthcheckprobes/{item_id}", response_model=Dict[str, Any])
def update_servicehealthcheckprobe(item_id: int, payload: ServiceHealthCheckProbeUpdateSchema):
    """Update existing ServiceHealthCheckProbe record fields."""
    svc = ServiceHealthCheckProbeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicehealthcheckprobe(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceHealthCheckProbe with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicehealthcheckprobes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicehealthcheckprobe(item_id: int, hard: bool = Query(False)):
    """Delete ServiceHealthCheckProbe record (soft-delete by default)."""
    svc = ServiceHealthCheckProbeService()
    ok = svc.delete_servicehealthcheckprobe(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceHealthCheckProbe with ID {item_id} not found")
    return None

@router.get("/servicehealthcheckprobes/analytics/metrics", response_model=Dict[str, Any])
def get_servicehealthcheckprobe_metrics():
    """Calculate summary statistical KPIs for ServiceHealthCheckProbe collection."""
    svc = ServiceHealthCheckProbeService()
    return svc.calculate_aggregate_metrics()

# ==================== APMMetricTimeseries Endpoints ====================
@router.get("/apmmetrictimeseriess", response_model=List[Dict[str, Any]])
def list_apmmetrictimeseriess(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List APMMetricTimeseries records with pagination and filtering."""
    svc = APMMetricTimeseriesService()
    items = svc.list_apmmetrictimeseriess(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/apmmetrictimeseriess/{item_id}", response_model=Dict[str, Any])
def get_apmmetrictimeseries_by_id(item_id: int):
    """Retrieve detailed record for APMMetricTimeseries by ID."""
    svc = APMMetricTimeseriesService()
    item = svc.get_apmmetrictimeseries_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"APMMetricTimeseries with ID {item_id} not found")
    return item.to_dict()

@router.post("/apmmetrictimeseriess", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_apmmetrictimeseries(payload: APMMetricTimeseriesCreateSchema):
    """Create new APMMetricTimeseries instance in enterprise repository."""
    svc = APMMetricTimeseriesService()
    try:
        item = svc.create_apmmetrictimeseries(
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

@router.put("/apmmetrictimeseriess/{item_id}", response_model=Dict[str, Any])
def update_apmmetrictimeseries(item_id: int, payload: APMMetricTimeseriesUpdateSchema):
    """Update existing APMMetricTimeseries record fields."""
    svc = APMMetricTimeseriesService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_apmmetrictimeseries(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"APMMetricTimeseries with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/apmmetrictimeseriess/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_apmmetrictimeseries(item_id: int, hard: bool = Query(False)):
    """Delete APMMetricTimeseries record (soft-delete by default)."""
    svc = APMMetricTimeseriesService()
    ok = svc.delete_apmmetrictimeseries(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"APMMetricTimeseries with ID {item_id} not found")
    return None

@router.get("/apmmetrictimeseriess/analytics/metrics", response_model=Dict[str, Any])
def get_apmmetrictimeseries_metrics():
    """Calculate summary statistical KPIs for APMMetricTimeseries collection."""
    svc = APMMetricTimeseriesService()
    return svc.calculate_aggregate_metrics()

# ==================== DistributedTraceSpan Endpoints ====================
@router.get("/distributedtracespans", response_model=List[Dict[str, Any]])
def list_distributedtracespans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DistributedTraceSpan records with pagination and filtering."""
    svc = DistributedTraceSpanService()
    items = svc.list_distributedtracespans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/distributedtracespans/{item_id}", response_model=Dict[str, Any])
def get_distributedtracespan_by_id(item_id: int):
    """Retrieve detailed record for DistributedTraceSpan by ID."""
    svc = DistributedTraceSpanService()
    item = svc.get_distributedtracespan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DistributedTraceSpan with ID {item_id} not found")
    return item.to_dict()

@router.post("/distributedtracespans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_distributedtracespan(payload: DistributedTraceSpanCreateSchema):
    """Create new DistributedTraceSpan instance in enterprise repository."""
    svc = DistributedTraceSpanService()
    try:
        item = svc.create_distributedtracespan(
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

@router.put("/distributedtracespans/{item_id}", response_model=Dict[str, Any])
def update_distributedtracespan(item_id: int, payload: DistributedTraceSpanUpdateSchema):
    """Update existing DistributedTraceSpan record fields."""
    svc = DistributedTraceSpanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_distributedtracespan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DistributedTraceSpan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/distributedtracespans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_distributedtracespan(item_id: int, hard: bool = Query(False)):
    """Delete DistributedTraceSpan record (soft-delete by default)."""
    svc = DistributedTraceSpanService()
    ok = svc.delete_distributedtracespan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DistributedTraceSpan with ID {item_id} not found")
    return None

@router.get("/distributedtracespans/analytics/metrics", response_model=Dict[str, Any])
def get_distributedtracespan_metrics():
    """Calculate summary statistical KPIs for DistributedTraceSpan collection."""
    svc = DistributedTraceSpanService()
    return svc.calculate_aggregate_metrics()

# ==================== ErrorCrashReport Endpoints ====================
@router.get("/errorcrashreports", response_model=List[Dict[str, Any]])
def list_errorcrashreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ErrorCrashReport records with pagination and filtering."""
    svc = ErrorCrashReportService()
    items = svc.list_errorcrashreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/errorcrashreports/{item_id}", response_model=Dict[str, Any])
def get_errorcrashreport_by_id(item_id: int):
    """Retrieve detailed record for ErrorCrashReport by ID."""
    svc = ErrorCrashReportService()
    item = svc.get_errorcrashreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ErrorCrashReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/errorcrashreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_errorcrashreport(payload: ErrorCrashReportCreateSchema):
    """Create new ErrorCrashReport instance in enterprise repository."""
    svc = ErrorCrashReportService()
    try:
        item = svc.create_errorcrashreport(
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

@router.put("/errorcrashreports/{item_id}", response_model=Dict[str, Any])
def update_errorcrashreport(item_id: int, payload: ErrorCrashReportUpdateSchema):
    """Update existing ErrorCrashReport record fields."""
    svc = ErrorCrashReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_errorcrashreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ErrorCrashReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/errorcrashreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_errorcrashreport(item_id: int, hard: bool = Query(False)):
    """Delete ErrorCrashReport record (soft-delete by default)."""
    svc = ErrorCrashReportService()
    ok = svc.delete_errorcrashreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ErrorCrashReport with ID {item_id} not found")
    return None

@router.get("/errorcrashreports/analytics/metrics", response_model=Dict[str, Any])
def get_errorcrashreport_metrics():
    """Calculate summary statistical KPIs for ErrorCrashReport collection."""
    svc = ErrorCrashReportService()
    return svc.calculate_aggregate_metrics()

# ==================== LatencySLOBudget Endpoints ====================
@router.get("/latencyslobudgets", response_model=List[Dict[str, Any]])
def list_latencyslobudgets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LatencySLOBudget records with pagination and filtering."""
    svc = LatencySLOBudgetService()
    items = svc.list_latencyslobudgets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/latencyslobudgets/{item_id}", response_model=Dict[str, Any])
def get_latencyslobudget_by_id(item_id: int):
    """Retrieve detailed record for LatencySLOBudget by ID."""
    svc = LatencySLOBudgetService()
    item = svc.get_latencyslobudget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LatencySLOBudget with ID {item_id} not found")
    return item.to_dict()

@router.post("/latencyslobudgets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_latencyslobudget(payload: LatencySLOBudgetCreateSchema):
    """Create new LatencySLOBudget instance in enterprise repository."""
    svc = LatencySLOBudgetService()
    try:
        item = svc.create_latencyslobudget(
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

@router.put("/latencyslobudgets/{item_id}", response_model=Dict[str, Any])
def update_latencyslobudget(item_id: int, payload: LatencySLOBudgetUpdateSchema):
    """Update existing LatencySLOBudget record fields."""
    svc = LatencySLOBudgetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_latencyslobudget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LatencySLOBudget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/latencyslobudgets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_latencyslobudget(item_id: int, hard: bool = Query(False)):
    """Delete LatencySLOBudget record (soft-delete by default)."""
    svc = LatencySLOBudgetService()
    ok = svc.delete_latencyslobudget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LatencySLOBudget with ID {item_id} not found")
    return None

@router.get("/latencyslobudgets/analytics/metrics", response_model=Dict[str, Any])
def get_latencyslobudget_metrics():
    """Calculate summary statistical KPIs for LatencySLOBudget collection."""
    svc = LatencySLOBudgetService()
    return svc.calculate_aggregate_metrics()

# ==================== ServerNodeTelemetry Endpoints ====================
@router.get("/servernodetelemetrys", response_model=List[Dict[str, Any]])
def list_servernodetelemetrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServerNodeTelemetry records with pagination and filtering."""
    svc = ServerNodeTelemetryService()
    items = svc.list_servernodetelemetrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servernodetelemetrys/{item_id}", response_model=Dict[str, Any])
def get_servernodetelemetry_by_id(item_id: int):
    """Retrieve detailed record for ServerNodeTelemetry by ID."""
    svc = ServerNodeTelemetryService()
    item = svc.get_servernodetelemetry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServerNodeTelemetry with ID {item_id} not found")
    return item.to_dict()

@router.post("/servernodetelemetrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servernodetelemetry(payload: ServerNodeTelemetryCreateSchema):
    """Create new ServerNodeTelemetry instance in enterprise repository."""
    svc = ServerNodeTelemetryService()
    try:
        item = svc.create_servernodetelemetry(
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

@router.put("/servernodetelemetrys/{item_id}", response_model=Dict[str, Any])
def update_servernodetelemetry(item_id: int, payload: ServerNodeTelemetryUpdateSchema):
    """Update existing ServerNodeTelemetry record fields."""
    svc = ServerNodeTelemetryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servernodetelemetry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServerNodeTelemetry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servernodetelemetrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servernodetelemetry(item_id: int, hard: bool = Query(False)):
    """Delete ServerNodeTelemetry record (soft-delete by default)."""
    svc = ServerNodeTelemetryService()
    ok = svc.delete_servernodetelemetry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServerNodeTelemetry with ID {item_id} not found")
    return None

@router.get("/servernodetelemetrys/analytics/metrics", response_model=Dict[str, Any])
def get_servernodetelemetry_metrics():
    """Calculate summary statistical KPIs for ServerNodeTelemetry collection."""
    svc = ServerNodeTelemetryService()
    return svc.calculate_aggregate_metrics()

# ==================== DatabasePoolMetric Endpoints ====================
@router.get("/databasepoolmetrics", response_model=List[Dict[str, Any]])
def list_databasepoolmetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DatabasePoolMetric records with pagination and filtering."""
    svc = DatabasePoolMetricService()
    items = svc.list_databasepoolmetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/databasepoolmetrics/{item_id}", response_model=Dict[str, Any])
def get_databasepoolmetric_by_id(item_id: int):
    """Retrieve detailed record for DatabasePoolMetric by ID."""
    svc = DatabasePoolMetricService()
    item = svc.get_databasepoolmetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DatabasePoolMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/databasepoolmetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_databasepoolmetric(payload: DatabasePoolMetricCreateSchema):
    """Create new DatabasePoolMetric instance in enterprise repository."""
    svc = DatabasePoolMetricService()
    try:
        item = svc.create_databasepoolmetric(
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

@router.put("/databasepoolmetrics/{item_id}", response_model=Dict[str, Any])
def update_databasepoolmetric(item_id: int, payload: DatabasePoolMetricUpdateSchema):
    """Update existing DatabasePoolMetric record fields."""
    svc = DatabasePoolMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_databasepoolmetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DatabasePoolMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/databasepoolmetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_databasepoolmetric(item_id: int, hard: bool = Query(False)):
    """Delete DatabasePoolMetric record (soft-delete by default)."""
    svc = DatabasePoolMetricService()
    ok = svc.delete_databasepoolmetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DatabasePoolMetric with ID {item_id} not found")
    return None

@router.get("/databasepoolmetrics/analytics/metrics", response_model=Dict[str, Any])
def get_databasepoolmetric_metrics():
    """Calculate summary statistical KPIs for DatabasePoolMetric collection."""
    svc = DatabasePoolMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== MemoryHeapSnapshot Endpoints ====================
@router.get("/memoryheapsnapshots", response_model=List[Dict[str, Any]])
def list_memoryheapsnapshots(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MemoryHeapSnapshot records with pagination and filtering."""
    svc = MemoryHeapSnapshotService()
    items = svc.list_memoryheapsnapshots(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/memoryheapsnapshots/{item_id}", response_model=Dict[str, Any])
def get_memoryheapsnapshot_by_id(item_id: int):
    """Retrieve detailed record for MemoryHeapSnapshot by ID."""
    svc = MemoryHeapSnapshotService()
    item = svc.get_memoryheapsnapshot_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MemoryHeapSnapshot with ID {item_id} not found")
    return item.to_dict()

@router.post("/memoryheapsnapshots", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_memoryheapsnapshot(payload: MemoryHeapSnapshotCreateSchema):
    """Create new MemoryHeapSnapshot instance in enterprise repository."""
    svc = MemoryHeapSnapshotService()
    try:
        item = svc.create_memoryheapsnapshot(
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

@router.put("/memoryheapsnapshots/{item_id}", response_model=Dict[str, Any])
def update_memoryheapsnapshot(item_id: int, payload: MemoryHeapSnapshotUpdateSchema):
    """Update existing MemoryHeapSnapshot record fields."""
    svc = MemoryHeapSnapshotService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_memoryheapsnapshot(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MemoryHeapSnapshot with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/memoryheapsnapshots/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_memoryheapsnapshot(item_id: int, hard: bool = Query(False)):
    """Delete MemoryHeapSnapshot record (soft-delete by default)."""
    svc = MemoryHeapSnapshotService()
    ok = svc.delete_memoryheapsnapshot(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MemoryHeapSnapshot with ID {item_id} not found")
    return None

@router.get("/memoryheapsnapshots/analytics/metrics", response_model=Dict[str, Any])
def get_memoryheapsnapshot_metrics():
    """Calculate summary statistical KPIs for MemoryHeapSnapshot collection."""
    svc = MemoryHeapSnapshotService()
    return svc.calculate_aggregate_metrics()

# ==================== AlertEscalationRule Endpoints ====================
@router.get("/alertescalationrules", response_model=List[Dict[str, Any]])
def list_alertescalationrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AlertEscalationRule records with pagination and filtering."""
    svc = AlertEscalationRuleService()
    items = svc.list_alertescalationrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/alertescalationrules/{item_id}", response_model=Dict[str, Any])
def get_alertescalationrule_by_id(item_id: int):
    """Retrieve detailed record for AlertEscalationRule by ID."""
    svc = AlertEscalationRuleService()
    item = svc.get_alertescalationrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AlertEscalationRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/alertescalationrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_alertescalationrule(payload: AlertEscalationRuleCreateSchema):
    """Create new AlertEscalationRule instance in enterprise repository."""
    svc = AlertEscalationRuleService()
    try:
        item = svc.create_alertescalationrule(
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

@router.put("/alertescalationrules/{item_id}", response_model=Dict[str, Any])
def update_alertescalationrule(item_id: int, payload: AlertEscalationRuleUpdateSchema):
    """Update existing AlertEscalationRule record fields."""
    svc = AlertEscalationRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_alertescalationrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AlertEscalationRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/alertescalationrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_alertescalationrule(item_id: int, hard: bool = Query(False)):
    """Delete AlertEscalationRule record (soft-delete by default)."""
    svc = AlertEscalationRuleService()
    ok = svc.delete_alertescalationrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AlertEscalationRule with ID {item_id} not found")
    return None

@router.get("/alertescalationrules/analytics/metrics", response_model=Dict[str, Any])
def get_alertescalationrule_metrics():
    """Calculate summary statistical KPIs for AlertEscalationRule collection."""
    svc = AlertEscalationRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== IncidentPostMortem Endpoints ====================
@router.get("/incidentpostmortems", response_model=List[Dict[str, Any]])
def list_incidentpostmortems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IncidentPostMortem records with pagination and filtering."""
    svc = IncidentPostMortemService()
    items = svc.list_incidentpostmortems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/incidentpostmortems/{item_id}", response_model=Dict[str, Any])
def get_incidentpostmortem_by_id(item_id: int):
    """Retrieve detailed record for IncidentPostMortem by ID."""
    svc = IncidentPostMortemService()
    item = svc.get_incidentpostmortem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IncidentPostMortem with ID {item_id} not found")
    return item.to_dict()

@router.post("/incidentpostmortems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_incidentpostmortem(payload: IncidentPostMortemCreateSchema):
    """Create new IncidentPostMortem instance in enterprise repository."""
    svc = IncidentPostMortemService()
    try:
        item = svc.create_incidentpostmortem(
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

@router.put("/incidentpostmortems/{item_id}", response_model=Dict[str, Any])
def update_incidentpostmortem(item_id: int, payload: IncidentPostMortemUpdateSchema):
    """Update existing IncidentPostMortem record fields."""
    svc = IncidentPostMortemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_incidentpostmortem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IncidentPostMortem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/incidentpostmortems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incidentpostmortem(item_id: int, hard: bool = Query(False)):
    """Delete IncidentPostMortem record (soft-delete by default)."""
    svc = IncidentPostMortemService()
    ok = svc.delete_incidentpostmortem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IncidentPostMortem with ID {item_id} not found")
    return None

@router.get("/incidentpostmortems/analytics/metrics", response_model=Dict[str, Any])
def get_incidentpostmortem_metrics():
    """Calculate summary statistical KPIs for IncidentPostMortem collection."""
    svc = IncidentPostMortemService()
    return svc.calculate_aggregate_metrics()

# ==================== LogStreamingSink Endpoints ====================
@router.get("/logstreamingsinks", response_model=List[Dict[str, Any]])
def list_logstreamingsinks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LogStreamingSink records with pagination and filtering."""
    svc = LogStreamingSinkService()
    items = svc.list_logstreamingsinks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/logstreamingsinks/{item_id}", response_model=Dict[str, Any])
def get_logstreamingsink_by_id(item_id: int):
    """Retrieve detailed record for LogStreamingSink by ID."""
    svc = LogStreamingSinkService()
    item = svc.get_logstreamingsink_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LogStreamingSink with ID {item_id} not found")
    return item.to_dict()

@router.post("/logstreamingsinks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_logstreamingsink(payload: LogStreamingSinkCreateSchema):
    """Create new LogStreamingSink instance in enterprise repository."""
    svc = LogStreamingSinkService()
    try:
        item = svc.create_logstreamingsink(
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

@router.put("/logstreamingsinks/{item_id}", response_model=Dict[str, Any])
def update_logstreamingsink(item_id: int, payload: LogStreamingSinkUpdateSchema):
    """Update existing LogStreamingSink record fields."""
    svc = LogStreamingSinkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_logstreamingsink(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LogStreamingSink with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/logstreamingsinks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_logstreamingsink(item_id: int, hard: bool = Query(False)):
    """Delete LogStreamingSink record (soft-delete by default)."""
    svc = LogStreamingSinkService()
    ok = svc.delete_logstreamingsink(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LogStreamingSink with ID {item_id} not found")
    return None

@router.get("/logstreamingsinks/analytics/metrics", response_model=Dict[str, Any])
def get_logstreamingsink_metrics():
    """Calculate summary statistical KPIs for LogStreamingSink collection."""
    svc = LogStreamingSinkService()
    return svc.calculate_aggregate_metrics()

# ==================== SyntheticsMonitorJob Endpoints ====================
@router.get("/syntheticsmonitorjobs", response_model=List[Dict[str, Any]])
def list_syntheticsmonitorjobs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SyntheticsMonitorJob records with pagination and filtering."""
    svc = SyntheticsMonitorJobService()
    items = svc.list_syntheticsmonitorjobs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/syntheticsmonitorjobs/{item_id}", response_model=Dict[str, Any])
def get_syntheticsmonitorjob_by_id(item_id: int):
    """Retrieve detailed record for SyntheticsMonitorJob by ID."""
    svc = SyntheticsMonitorJobService()
    item = svc.get_syntheticsmonitorjob_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SyntheticsMonitorJob with ID {item_id} not found")
    return item.to_dict()

@router.post("/syntheticsmonitorjobs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_syntheticsmonitorjob(payload: SyntheticsMonitorJobCreateSchema):
    """Create new SyntheticsMonitorJob instance in enterprise repository."""
    svc = SyntheticsMonitorJobService()
    try:
        item = svc.create_syntheticsmonitorjob(
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

@router.put("/syntheticsmonitorjobs/{item_id}", response_model=Dict[str, Any])
def update_syntheticsmonitorjob(item_id: int, payload: SyntheticsMonitorJobUpdateSchema):
    """Update existing SyntheticsMonitorJob record fields."""
    svc = SyntheticsMonitorJobService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_syntheticsmonitorjob(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SyntheticsMonitorJob with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/syntheticsmonitorjobs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_syntheticsmonitorjob(item_id: int, hard: bool = Query(False)):
    """Delete SyntheticsMonitorJob record (soft-delete by default)."""
    svc = SyntheticsMonitorJobService()
    ok = svc.delete_syntheticsmonitorjob(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SyntheticsMonitorJob with ID {item_id} not found")
    return None

@router.get("/syntheticsmonitorjobs/analytics/metrics", response_model=Dict[str, Any])
def get_syntheticsmonitorjob_metrics():
    """Calculate summary statistical KPIs for SyntheticsMonitorJob collection."""
    svc = SyntheticsMonitorJobService()
    return svc.calculate_aggregate_metrics()

# ==================== CapacityPlanningTrend Endpoints ====================
@router.get("/capacityplanningtrends", response_model=List[Dict[str, Any]])
def list_capacityplanningtrends(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CapacityPlanningTrend records with pagination and filtering."""
    svc = CapacityPlanningTrendService()
    items = svc.list_capacityplanningtrends(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/capacityplanningtrends/{item_id}", response_model=Dict[str, Any])
def get_capacityplanningtrend_by_id(item_id: int):
    """Retrieve detailed record for CapacityPlanningTrend by ID."""
    svc = CapacityPlanningTrendService()
    item = svc.get_capacityplanningtrend_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CapacityPlanningTrend with ID {item_id} not found")
    return item.to_dict()

@router.post("/capacityplanningtrends", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_capacityplanningtrend(payload: CapacityPlanningTrendCreateSchema):
    """Create new CapacityPlanningTrend instance in enterprise repository."""
    svc = CapacityPlanningTrendService()
    try:
        item = svc.create_capacityplanningtrend(
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

@router.put("/capacityplanningtrends/{item_id}", response_model=Dict[str, Any])
def update_capacityplanningtrend(item_id: int, payload: CapacityPlanningTrendUpdateSchema):
    """Update existing CapacityPlanningTrend record fields."""
    svc = CapacityPlanningTrendService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_capacityplanningtrend(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CapacityPlanningTrend with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/capacityplanningtrends/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_capacityplanningtrend(item_id: int, hard: bool = Query(False)):
    """Delete CapacityPlanningTrend record (soft-delete by default)."""
    svc = CapacityPlanningTrendService()
    ok = svc.delete_capacityplanningtrend(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CapacityPlanningTrend with ID {item_id} not found")
    return None

@router.get("/capacityplanningtrends/analytics/metrics", response_model=Dict[str, Any])
def get_capacityplanningtrend_metrics():
    """Calculate summary statistical KPIs for CapacityPlanningTrend collection."""
    svc = CapacityPlanningTrendService()
    return svc.calculate_aggregate_metrics()

# ==================== DeploymentReleaseMarker Endpoints ====================
@router.get("/deploymentreleasemarkers", response_model=List[Dict[str, Any]])
def list_deploymentreleasemarkers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeploymentReleaseMarker records with pagination and filtering."""
    svc = DeploymentReleaseMarkerService()
    items = svc.list_deploymentreleasemarkers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/deploymentreleasemarkers/{item_id}", response_model=Dict[str, Any])
def get_deploymentreleasemarker_by_id(item_id: int):
    """Retrieve detailed record for DeploymentReleaseMarker by ID."""
    svc = DeploymentReleaseMarkerService()
    item = svc.get_deploymentreleasemarker_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeploymentReleaseMarker with ID {item_id} not found")
    return item.to_dict()

@router.post("/deploymentreleasemarkers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_deploymentreleasemarker(payload: DeploymentReleaseMarkerCreateSchema):
    """Create new DeploymentReleaseMarker instance in enterprise repository."""
    svc = DeploymentReleaseMarkerService()
    try:
        item = svc.create_deploymentreleasemarker(
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

@router.put("/deploymentreleasemarkers/{item_id}", response_model=Dict[str, Any])
def update_deploymentreleasemarker(item_id: int, payload: DeploymentReleaseMarkerUpdateSchema):
    """Update existing DeploymentReleaseMarker record fields."""
    svc = DeploymentReleaseMarkerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_deploymentreleasemarker(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeploymentReleaseMarker with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/deploymentreleasemarkers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deploymentreleasemarker(item_id: int, hard: bool = Query(False)):
    """Delete DeploymentReleaseMarker record (soft-delete by default)."""
    svc = DeploymentReleaseMarkerService()
    ok = svc.delete_deploymentreleasemarker(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeploymentReleaseMarker with ID {item_id} not found")
    return None

@router.get("/deploymentreleasemarkers/analytics/metrics", response_model=Dict[str, Any])
def get_deploymentreleasemarker_metrics():
    """Calculate summary statistical KPIs for DeploymentReleaseMarker collection."""
    svc = DeploymentReleaseMarkerService()
    return svc.calculate_aggregate_metrics()

# ==================== TelemetryDashboardWidget Endpoints ====================
@router.get("/telemetrydashboardwidgets", response_model=List[Dict[str, Any]])
def list_telemetrydashboardwidgets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TelemetryDashboardWidget records with pagination and filtering."""
    svc = TelemetryDashboardWidgetService()
    items = svc.list_telemetrydashboardwidgets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/telemetrydashboardwidgets/{item_id}", response_model=Dict[str, Any])
def get_telemetrydashboardwidget_by_id(item_id: int):
    """Retrieve detailed record for TelemetryDashboardWidget by ID."""
    svc = TelemetryDashboardWidgetService()
    item = svc.get_telemetrydashboardwidget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TelemetryDashboardWidget with ID {item_id} not found")
    return item.to_dict()

@router.post("/telemetrydashboardwidgets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_telemetrydashboardwidget(payload: TelemetryDashboardWidgetCreateSchema):
    """Create new TelemetryDashboardWidget instance in enterprise repository."""
    svc = TelemetryDashboardWidgetService()
    try:
        item = svc.create_telemetrydashboardwidget(
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

@router.put("/telemetrydashboardwidgets/{item_id}", response_model=Dict[str, Any])
def update_telemetrydashboardwidget(item_id: int, payload: TelemetryDashboardWidgetUpdateSchema):
    """Update existing TelemetryDashboardWidget record fields."""
    svc = TelemetryDashboardWidgetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_telemetrydashboardwidget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TelemetryDashboardWidget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/telemetrydashboardwidgets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_telemetrydashboardwidget(item_id: int, hard: bool = Query(False)):
    """Delete TelemetryDashboardWidget record (soft-delete by default)."""
    svc = TelemetryDashboardWidgetService()
    ok = svc.delete_telemetrydashboardwidget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TelemetryDashboardWidget with ID {item_id} not found")
    return None

@router.get("/telemetrydashboardwidgets/analytics/metrics", response_model=Dict[str, Any])
def get_telemetrydashboardwidget_metrics():
    """Calculate summary statistical KPIs for TelemetryDashboardWidget collection."""
    svc = TelemetryDashboardWidgetService()
    return svc.calculate_aggregate_metrics()

# ==================== AnomalyDetectionAlert Endpoints ====================
@router.get("/anomalydetectionalerts", response_model=List[Dict[str, Any]])
def list_anomalydetectionalerts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AnomalyDetectionAlert records with pagination and filtering."""
    svc = AnomalyDetectionAlertService()
    items = svc.list_anomalydetectionalerts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/anomalydetectionalerts/{item_id}", response_model=Dict[str, Any])
def get_anomalydetectionalert_by_id(item_id: int):
    """Retrieve detailed record for AnomalyDetectionAlert by ID."""
    svc = AnomalyDetectionAlertService()
    item = svc.get_anomalydetectionalert_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AnomalyDetectionAlert with ID {item_id} not found")
    return item.to_dict()

@router.post("/anomalydetectionalerts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_anomalydetectionalert(payload: AnomalyDetectionAlertCreateSchema):
    """Create new AnomalyDetectionAlert instance in enterprise repository."""
    svc = AnomalyDetectionAlertService()
    try:
        item = svc.create_anomalydetectionalert(
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

@router.put("/anomalydetectionalerts/{item_id}", response_model=Dict[str, Any])
def update_anomalydetectionalert(item_id: int, payload: AnomalyDetectionAlertUpdateSchema):
    """Update existing AnomalyDetectionAlert record fields."""
    svc = AnomalyDetectionAlertService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_anomalydetectionalert(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AnomalyDetectionAlert with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/anomalydetectionalerts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_anomalydetectionalert(item_id: int, hard: bool = Query(False)):
    """Delete AnomalyDetectionAlert record (soft-delete by default)."""
    svc = AnomalyDetectionAlertService()
    ok = svc.delete_anomalydetectionalert(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AnomalyDetectionAlert with ID {item_id} not found")
    return None

@router.get("/anomalydetectionalerts/analytics/metrics", response_model=Dict[str, Any])
def get_anomalydetectionalert_metrics():
    """Calculate summary statistical KPIs for AnomalyDetectionAlert collection."""
    svc = AnomalyDetectionAlertService()
    return svc.calculate_aggregate_metrics()

