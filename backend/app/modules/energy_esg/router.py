"""
Corporate Sustainability & ESG Energy Tracking - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    EnergyMeterLogService,
    CarbonEmissionRecordService,
    RenewableCreditService,
    WaterConsumptionLogService,
    WasteDisposalManifestService,
    HazardousMaterialTrackService,
    ESGComplianceMetricService,
    SustainabilityInitiativeService,
    GreenhouseGasScope1Service,
    GreenhouseGasScope2Service,
    GreenhouseGasScope3Service,
    EnergyAuditReportService,
    VendorESGScorecardService,
    RegulatoryCarbonFilingService,
    OffsetCertificateService,
    CommunityImpactProjectService,
)
from .schemas import (
    EnergyMeterLogCreateSchema, EnergyMeterLogUpdateSchema, EnergyMeterLogResponseSchema,
    CarbonEmissionRecordCreateSchema, CarbonEmissionRecordUpdateSchema, CarbonEmissionRecordResponseSchema,
    RenewableCreditCreateSchema, RenewableCreditUpdateSchema, RenewableCreditResponseSchema,
    WaterConsumptionLogCreateSchema, WaterConsumptionLogUpdateSchema, WaterConsumptionLogResponseSchema,
    WasteDisposalManifestCreateSchema, WasteDisposalManifestUpdateSchema, WasteDisposalManifestResponseSchema,
    HazardousMaterialTrackCreateSchema, HazardousMaterialTrackUpdateSchema, HazardousMaterialTrackResponseSchema,
    ESGComplianceMetricCreateSchema, ESGComplianceMetricUpdateSchema, ESGComplianceMetricResponseSchema,
    SustainabilityInitiativeCreateSchema, SustainabilityInitiativeUpdateSchema, SustainabilityInitiativeResponseSchema,
    GreenhouseGasScope1CreateSchema, GreenhouseGasScope1UpdateSchema, GreenhouseGasScope1ResponseSchema,
    GreenhouseGasScope2CreateSchema, GreenhouseGasScope2UpdateSchema, GreenhouseGasScope2ResponseSchema,
    GreenhouseGasScope3CreateSchema, GreenhouseGasScope3UpdateSchema, GreenhouseGasScope3ResponseSchema,
    EnergyAuditReportCreateSchema, EnergyAuditReportUpdateSchema, EnergyAuditReportResponseSchema,
    VendorESGScorecardCreateSchema, VendorESGScorecardUpdateSchema, VendorESGScorecardResponseSchema,
    RegulatoryCarbonFilingCreateSchema, RegulatoryCarbonFilingUpdateSchema, RegulatoryCarbonFilingResponseSchema,
    OffsetCertificateCreateSchema, OffsetCertificateUpdateSchema, OffsetCertificateResponseSchema,
    CommunityImpactProjectCreateSchema, CommunityImpactProjectUpdateSchema, CommunityImpactProjectResponseSchema,
)

router = APIRouter(prefix="/energy_esg", tags=["Corporate Sustainability & ESG Energy Tracking"])

# ==================== EnergyMeterLog Endpoints ====================
@router.get("/energymeterlogs", response_model=List[Dict[str, Any]])
def list_energymeterlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EnergyMeterLog records with pagination and filtering."""
    svc = EnergyMeterLogService()
    items = svc.list_energymeterlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/energymeterlogs/{item_id}", response_model=Dict[str, Any])
def get_energymeterlog_by_id(item_id: int):
    """Retrieve detailed record for EnergyMeterLog by ID."""
    svc = EnergyMeterLogService()
    item = svc.get_energymeterlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EnergyMeterLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/energymeterlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_energymeterlog(payload: EnergyMeterLogCreateSchema):
    """Create new EnergyMeterLog instance in enterprise repository."""
    svc = EnergyMeterLogService()
    try:
        item = svc.create_energymeterlog(
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

@router.put("/energymeterlogs/{item_id}", response_model=Dict[str, Any])
def update_energymeterlog(item_id: int, payload: EnergyMeterLogUpdateSchema):
    """Update existing EnergyMeterLog record fields."""
    svc = EnergyMeterLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_energymeterlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EnergyMeterLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/energymeterlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_energymeterlog(item_id: int, hard: bool = Query(False)):
    """Delete EnergyMeterLog record (soft-delete by default)."""
    svc = EnergyMeterLogService()
    ok = svc.delete_energymeterlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EnergyMeterLog with ID {item_id} not found")
    return None

@router.get("/energymeterlogs/analytics/metrics", response_model=Dict[str, Any])
def get_energymeterlog_metrics():
    """Calculate summary statistical KPIs for EnergyMeterLog collection."""
    svc = EnergyMeterLogService()
    return svc.calculate_aggregate_metrics()

# ==================== CarbonEmissionRecord Endpoints ====================
@router.get("/carbonemissionrecords", response_model=List[Dict[str, Any]])
def list_carbonemissionrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CarbonEmissionRecord records with pagination and filtering."""
    svc = CarbonEmissionRecordService()
    items = svc.list_carbonemissionrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/carbonemissionrecords/{item_id}", response_model=Dict[str, Any])
def get_carbonemissionrecord_by_id(item_id: int):
    """Retrieve detailed record for CarbonEmissionRecord by ID."""
    svc = CarbonEmissionRecordService()
    item = svc.get_carbonemissionrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CarbonEmissionRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/carbonemissionrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_carbonemissionrecord(payload: CarbonEmissionRecordCreateSchema):
    """Create new CarbonEmissionRecord instance in enterprise repository."""
    svc = CarbonEmissionRecordService()
    try:
        item = svc.create_carbonemissionrecord(
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

@router.put("/carbonemissionrecords/{item_id}", response_model=Dict[str, Any])
def update_carbonemissionrecord(item_id: int, payload: CarbonEmissionRecordUpdateSchema):
    """Update existing CarbonEmissionRecord record fields."""
    svc = CarbonEmissionRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_carbonemissionrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CarbonEmissionRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/carbonemissionrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carbonemissionrecord(item_id: int, hard: bool = Query(False)):
    """Delete CarbonEmissionRecord record (soft-delete by default)."""
    svc = CarbonEmissionRecordService()
    ok = svc.delete_carbonemissionrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CarbonEmissionRecord with ID {item_id} not found")
    return None

@router.get("/carbonemissionrecords/analytics/metrics", response_model=Dict[str, Any])
def get_carbonemissionrecord_metrics():
    """Calculate summary statistical KPIs for CarbonEmissionRecord collection."""
    svc = CarbonEmissionRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== RenewableCredit Endpoints ====================
@router.get("/renewablecredits", response_model=List[Dict[str, Any]])
def list_renewablecredits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RenewableCredit records with pagination and filtering."""
    svc = RenewableCreditService()
    items = svc.list_renewablecredits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/renewablecredits/{item_id}", response_model=Dict[str, Any])
def get_renewablecredit_by_id(item_id: int):
    """Retrieve detailed record for RenewableCredit by ID."""
    svc = RenewableCreditService()
    item = svc.get_renewablecredit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RenewableCredit with ID {item_id} not found")
    return item.to_dict()

@router.post("/renewablecredits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_renewablecredit(payload: RenewableCreditCreateSchema):
    """Create new RenewableCredit instance in enterprise repository."""
    svc = RenewableCreditService()
    try:
        item = svc.create_renewablecredit(
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

@router.put("/renewablecredits/{item_id}", response_model=Dict[str, Any])
def update_renewablecredit(item_id: int, payload: RenewableCreditUpdateSchema):
    """Update existing RenewableCredit record fields."""
    svc = RenewableCreditService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_renewablecredit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RenewableCredit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/renewablecredits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_renewablecredit(item_id: int, hard: bool = Query(False)):
    """Delete RenewableCredit record (soft-delete by default)."""
    svc = RenewableCreditService()
    ok = svc.delete_renewablecredit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RenewableCredit with ID {item_id} not found")
    return None

@router.get("/renewablecredits/analytics/metrics", response_model=Dict[str, Any])
def get_renewablecredit_metrics():
    """Calculate summary statistical KPIs for RenewableCredit collection."""
    svc = RenewableCreditService()
    return svc.calculate_aggregate_metrics()

# ==================== WaterConsumptionLog Endpoints ====================
@router.get("/waterconsumptionlogs", response_model=List[Dict[str, Any]])
def list_waterconsumptionlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WaterConsumptionLog records with pagination and filtering."""
    svc = WaterConsumptionLogService()
    items = svc.list_waterconsumptionlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/waterconsumptionlogs/{item_id}", response_model=Dict[str, Any])
def get_waterconsumptionlog_by_id(item_id: int):
    """Retrieve detailed record for WaterConsumptionLog by ID."""
    svc = WaterConsumptionLogService()
    item = svc.get_waterconsumptionlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WaterConsumptionLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/waterconsumptionlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_waterconsumptionlog(payload: WaterConsumptionLogCreateSchema):
    """Create new WaterConsumptionLog instance in enterprise repository."""
    svc = WaterConsumptionLogService()
    try:
        item = svc.create_waterconsumptionlog(
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

@router.put("/waterconsumptionlogs/{item_id}", response_model=Dict[str, Any])
def update_waterconsumptionlog(item_id: int, payload: WaterConsumptionLogUpdateSchema):
    """Update existing WaterConsumptionLog record fields."""
    svc = WaterConsumptionLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_waterconsumptionlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WaterConsumptionLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/waterconsumptionlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_waterconsumptionlog(item_id: int, hard: bool = Query(False)):
    """Delete WaterConsumptionLog record (soft-delete by default)."""
    svc = WaterConsumptionLogService()
    ok = svc.delete_waterconsumptionlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WaterConsumptionLog with ID {item_id} not found")
    return None

@router.get("/waterconsumptionlogs/analytics/metrics", response_model=Dict[str, Any])
def get_waterconsumptionlog_metrics():
    """Calculate summary statistical KPIs for WaterConsumptionLog collection."""
    svc = WaterConsumptionLogService()
    return svc.calculate_aggregate_metrics()

# ==================== WasteDisposalManifest Endpoints ====================
@router.get("/wastedisposalmanifests", response_model=List[Dict[str, Any]])
def list_wastedisposalmanifests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WasteDisposalManifest records with pagination and filtering."""
    svc = WasteDisposalManifestService()
    items = svc.list_wastedisposalmanifests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/wastedisposalmanifests/{item_id}", response_model=Dict[str, Any])
def get_wastedisposalmanifest_by_id(item_id: int):
    """Retrieve detailed record for WasteDisposalManifest by ID."""
    svc = WasteDisposalManifestService()
    item = svc.get_wastedisposalmanifest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WasteDisposalManifest with ID {item_id} not found")
    return item.to_dict()

@router.post("/wastedisposalmanifests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_wastedisposalmanifest(payload: WasteDisposalManifestCreateSchema):
    """Create new WasteDisposalManifest instance in enterprise repository."""
    svc = WasteDisposalManifestService()
    try:
        item = svc.create_wastedisposalmanifest(
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

@router.put("/wastedisposalmanifests/{item_id}", response_model=Dict[str, Any])
def update_wastedisposalmanifest(item_id: int, payload: WasteDisposalManifestUpdateSchema):
    """Update existing WasteDisposalManifest record fields."""
    svc = WasteDisposalManifestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_wastedisposalmanifest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WasteDisposalManifest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/wastedisposalmanifests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wastedisposalmanifest(item_id: int, hard: bool = Query(False)):
    """Delete WasteDisposalManifest record (soft-delete by default)."""
    svc = WasteDisposalManifestService()
    ok = svc.delete_wastedisposalmanifest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WasteDisposalManifest with ID {item_id} not found")
    return None

@router.get("/wastedisposalmanifests/analytics/metrics", response_model=Dict[str, Any])
def get_wastedisposalmanifest_metrics():
    """Calculate summary statistical KPIs for WasteDisposalManifest collection."""
    svc = WasteDisposalManifestService()
    return svc.calculate_aggregate_metrics()

# ==================== HazardousMaterialTrack Endpoints ====================
@router.get("/hazardousmaterialtracks", response_model=List[Dict[str, Any]])
def list_hazardousmaterialtracks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HazardousMaterialTrack records with pagination and filtering."""
    svc = HazardousMaterialTrackService()
    items = svc.list_hazardousmaterialtracks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hazardousmaterialtracks/{item_id}", response_model=Dict[str, Any])
def get_hazardousmaterialtrack_by_id(item_id: int):
    """Retrieve detailed record for HazardousMaterialTrack by ID."""
    svc = HazardousMaterialTrackService()
    item = svc.get_hazardousmaterialtrack_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HazardousMaterialTrack with ID {item_id} not found")
    return item.to_dict()

@router.post("/hazardousmaterialtracks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hazardousmaterialtrack(payload: HazardousMaterialTrackCreateSchema):
    """Create new HazardousMaterialTrack instance in enterprise repository."""
    svc = HazardousMaterialTrackService()
    try:
        item = svc.create_hazardousmaterialtrack(
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

@router.put("/hazardousmaterialtracks/{item_id}", response_model=Dict[str, Any])
def update_hazardousmaterialtrack(item_id: int, payload: HazardousMaterialTrackUpdateSchema):
    """Update existing HazardousMaterialTrack record fields."""
    svc = HazardousMaterialTrackService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hazardousmaterialtrack(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HazardousMaterialTrack with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hazardousmaterialtracks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hazardousmaterialtrack(item_id: int, hard: bool = Query(False)):
    """Delete HazardousMaterialTrack record (soft-delete by default)."""
    svc = HazardousMaterialTrackService()
    ok = svc.delete_hazardousmaterialtrack(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HazardousMaterialTrack with ID {item_id} not found")
    return None

@router.get("/hazardousmaterialtracks/analytics/metrics", response_model=Dict[str, Any])
def get_hazardousmaterialtrack_metrics():
    """Calculate summary statistical KPIs for HazardousMaterialTrack collection."""
    svc = HazardousMaterialTrackService()
    return svc.calculate_aggregate_metrics()

# ==================== ESGComplianceMetric Endpoints ====================
@router.get("/esgcompliancemetrics", response_model=List[Dict[str, Any]])
def list_esgcompliancemetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ESGComplianceMetric records with pagination and filtering."""
    svc = ESGComplianceMetricService()
    items = svc.list_esgcompliancemetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/esgcompliancemetrics/{item_id}", response_model=Dict[str, Any])
def get_esgcompliancemetric_by_id(item_id: int):
    """Retrieve detailed record for ESGComplianceMetric by ID."""
    svc = ESGComplianceMetricService()
    item = svc.get_esgcompliancemetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ESGComplianceMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/esgcompliancemetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_esgcompliancemetric(payload: ESGComplianceMetricCreateSchema):
    """Create new ESGComplianceMetric instance in enterprise repository."""
    svc = ESGComplianceMetricService()
    try:
        item = svc.create_esgcompliancemetric(
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

@router.put("/esgcompliancemetrics/{item_id}", response_model=Dict[str, Any])
def update_esgcompliancemetric(item_id: int, payload: ESGComplianceMetricUpdateSchema):
    """Update existing ESGComplianceMetric record fields."""
    svc = ESGComplianceMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_esgcompliancemetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ESGComplianceMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/esgcompliancemetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_esgcompliancemetric(item_id: int, hard: bool = Query(False)):
    """Delete ESGComplianceMetric record (soft-delete by default)."""
    svc = ESGComplianceMetricService()
    ok = svc.delete_esgcompliancemetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ESGComplianceMetric with ID {item_id} not found")
    return None

@router.get("/esgcompliancemetrics/analytics/metrics", response_model=Dict[str, Any])
def get_esgcompliancemetric_metrics():
    """Calculate summary statistical KPIs for ESGComplianceMetric collection."""
    svc = ESGComplianceMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== SustainabilityInitiative Endpoints ====================
@router.get("/sustainabilityinitiatives", response_model=List[Dict[str, Any]])
def list_sustainabilityinitiatives(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SustainabilityInitiative records with pagination and filtering."""
    svc = SustainabilityInitiativeService()
    items = svc.list_sustainabilityinitiatives(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sustainabilityinitiatives/{item_id}", response_model=Dict[str, Any])
def get_sustainabilityinitiative_by_id(item_id: int):
    """Retrieve detailed record for SustainabilityInitiative by ID."""
    svc = SustainabilityInitiativeService()
    item = svc.get_sustainabilityinitiative_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SustainabilityInitiative with ID {item_id} not found")
    return item.to_dict()

@router.post("/sustainabilityinitiatives", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sustainabilityinitiative(payload: SustainabilityInitiativeCreateSchema):
    """Create new SustainabilityInitiative instance in enterprise repository."""
    svc = SustainabilityInitiativeService()
    try:
        item = svc.create_sustainabilityinitiative(
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

@router.put("/sustainabilityinitiatives/{item_id}", response_model=Dict[str, Any])
def update_sustainabilityinitiative(item_id: int, payload: SustainabilityInitiativeUpdateSchema):
    """Update existing SustainabilityInitiative record fields."""
    svc = SustainabilityInitiativeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sustainabilityinitiative(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SustainabilityInitiative with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sustainabilityinitiatives/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sustainabilityinitiative(item_id: int, hard: bool = Query(False)):
    """Delete SustainabilityInitiative record (soft-delete by default)."""
    svc = SustainabilityInitiativeService()
    ok = svc.delete_sustainabilityinitiative(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SustainabilityInitiative with ID {item_id} not found")
    return None

@router.get("/sustainabilityinitiatives/analytics/metrics", response_model=Dict[str, Any])
def get_sustainabilityinitiative_metrics():
    """Calculate summary statistical KPIs for SustainabilityInitiative collection."""
    svc = SustainabilityInitiativeService()
    return svc.calculate_aggregate_metrics()

# ==================== GreenhouseGasScope1 Endpoints ====================
@router.get("/greenhousegasscope1s", response_model=List[Dict[str, Any]])
def list_greenhousegasscope1s(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GreenhouseGasScope1 records with pagination and filtering."""
    svc = GreenhouseGasScope1Service()
    items = svc.list_greenhousegasscope1s(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/greenhousegasscope1s/{item_id}", response_model=Dict[str, Any])
def get_greenhousegasscope1_by_id(item_id: int):
    """Retrieve detailed record for GreenhouseGasScope1 by ID."""
    svc = GreenhouseGasScope1Service()
    item = svc.get_greenhousegasscope1_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope1 with ID {item_id} not found")
    return item.to_dict()

@router.post("/greenhousegasscope1s", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_greenhousegasscope1(payload: GreenhouseGasScope1CreateSchema):
    """Create new GreenhouseGasScope1 instance in enterprise repository."""
    svc = GreenhouseGasScope1Service()
    try:
        item = svc.create_greenhousegasscope1(
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

@router.put("/greenhousegasscope1s/{item_id}", response_model=Dict[str, Any])
def update_greenhousegasscope1(item_id: int, payload: GreenhouseGasScope1UpdateSchema):
    """Update existing GreenhouseGasScope1 record fields."""
    svc = GreenhouseGasScope1Service()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_greenhousegasscope1(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope1 with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/greenhousegasscope1s/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_greenhousegasscope1(item_id: int, hard: bool = Query(False)):
    """Delete GreenhouseGasScope1 record (soft-delete by default)."""
    svc = GreenhouseGasScope1Service()
    ok = svc.delete_greenhousegasscope1(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope1 with ID {item_id} not found")
    return None

@router.get("/greenhousegasscope1s/analytics/metrics", response_model=Dict[str, Any])
def get_greenhousegasscope1_metrics():
    """Calculate summary statistical KPIs for GreenhouseGasScope1 collection."""
    svc = GreenhouseGasScope1Service()
    return svc.calculate_aggregate_metrics()

# ==================== GreenhouseGasScope2 Endpoints ====================
@router.get("/greenhousegasscope2s", response_model=List[Dict[str, Any]])
def list_greenhousegasscope2s(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GreenhouseGasScope2 records with pagination and filtering."""
    svc = GreenhouseGasScope2Service()
    items = svc.list_greenhousegasscope2s(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/greenhousegasscope2s/{item_id}", response_model=Dict[str, Any])
def get_greenhousegasscope2_by_id(item_id: int):
    """Retrieve detailed record for GreenhouseGasScope2 by ID."""
    svc = GreenhouseGasScope2Service()
    item = svc.get_greenhousegasscope2_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope2 with ID {item_id} not found")
    return item.to_dict()

@router.post("/greenhousegasscope2s", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_greenhousegasscope2(payload: GreenhouseGasScope2CreateSchema):
    """Create new GreenhouseGasScope2 instance in enterprise repository."""
    svc = GreenhouseGasScope2Service()
    try:
        item = svc.create_greenhousegasscope2(
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

@router.put("/greenhousegasscope2s/{item_id}", response_model=Dict[str, Any])
def update_greenhousegasscope2(item_id: int, payload: GreenhouseGasScope2UpdateSchema):
    """Update existing GreenhouseGasScope2 record fields."""
    svc = GreenhouseGasScope2Service()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_greenhousegasscope2(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope2 with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/greenhousegasscope2s/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_greenhousegasscope2(item_id: int, hard: bool = Query(False)):
    """Delete GreenhouseGasScope2 record (soft-delete by default)."""
    svc = GreenhouseGasScope2Service()
    ok = svc.delete_greenhousegasscope2(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope2 with ID {item_id} not found")
    return None

@router.get("/greenhousegasscope2s/analytics/metrics", response_model=Dict[str, Any])
def get_greenhousegasscope2_metrics():
    """Calculate summary statistical KPIs for GreenhouseGasScope2 collection."""
    svc = GreenhouseGasScope2Service()
    return svc.calculate_aggregate_metrics()

# ==================== GreenhouseGasScope3 Endpoints ====================
@router.get("/greenhousegasscope3s", response_model=List[Dict[str, Any]])
def list_greenhousegasscope3s(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GreenhouseGasScope3 records with pagination and filtering."""
    svc = GreenhouseGasScope3Service()
    items = svc.list_greenhousegasscope3s(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/greenhousegasscope3s/{item_id}", response_model=Dict[str, Any])
def get_greenhousegasscope3_by_id(item_id: int):
    """Retrieve detailed record for GreenhouseGasScope3 by ID."""
    svc = GreenhouseGasScope3Service()
    item = svc.get_greenhousegasscope3_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope3 with ID {item_id} not found")
    return item.to_dict()

@router.post("/greenhousegasscope3s", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_greenhousegasscope3(payload: GreenhouseGasScope3CreateSchema):
    """Create new GreenhouseGasScope3 instance in enterprise repository."""
    svc = GreenhouseGasScope3Service()
    try:
        item = svc.create_greenhousegasscope3(
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

@router.put("/greenhousegasscope3s/{item_id}", response_model=Dict[str, Any])
def update_greenhousegasscope3(item_id: int, payload: GreenhouseGasScope3UpdateSchema):
    """Update existing GreenhouseGasScope3 record fields."""
    svc = GreenhouseGasScope3Service()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_greenhousegasscope3(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope3 with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/greenhousegasscope3s/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_greenhousegasscope3(item_id: int, hard: bool = Query(False)):
    """Delete GreenhouseGasScope3 record (soft-delete by default)."""
    svc = GreenhouseGasScope3Service()
    ok = svc.delete_greenhousegasscope3(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GreenhouseGasScope3 with ID {item_id} not found")
    return None

@router.get("/greenhousegasscope3s/analytics/metrics", response_model=Dict[str, Any])
def get_greenhousegasscope3_metrics():
    """Calculate summary statistical KPIs for GreenhouseGasScope3 collection."""
    svc = GreenhouseGasScope3Service()
    return svc.calculate_aggregate_metrics()

# ==================== EnergyAuditReport Endpoints ====================
@router.get("/energyauditreports", response_model=List[Dict[str, Any]])
def list_energyauditreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EnergyAuditReport records with pagination and filtering."""
    svc = EnergyAuditReportService()
    items = svc.list_energyauditreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/energyauditreports/{item_id}", response_model=Dict[str, Any])
def get_energyauditreport_by_id(item_id: int):
    """Retrieve detailed record for EnergyAuditReport by ID."""
    svc = EnergyAuditReportService()
    item = svc.get_energyauditreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EnergyAuditReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/energyauditreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_energyauditreport(payload: EnergyAuditReportCreateSchema):
    """Create new EnergyAuditReport instance in enterprise repository."""
    svc = EnergyAuditReportService()
    try:
        item = svc.create_energyauditreport(
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

@router.put("/energyauditreports/{item_id}", response_model=Dict[str, Any])
def update_energyauditreport(item_id: int, payload: EnergyAuditReportUpdateSchema):
    """Update existing EnergyAuditReport record fields."""
    svc = EnergyAuditReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_energyauditreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EnergyAuditReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/energyauditreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_energyauditreport(item_id: int, hard: bool = Query(False)):
    """Delete EnergyAuditReport record (soft-delete by default)."""
    svc = EnergyAuditReportService()
    ok = svc.delete_energyauditreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EnergyAuditReport with ID {item_id} not found")
    return None

@router.get("/energyauditreports/analytics/metrics", response_model=Dict[str, Any])
def get_energyauditreport_metrics():
    """Calculate summary statistical KPIs for EnergyAuditReport collection."""
    svc = EnergyAuditReportService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorESGScorecard Endpoints ====================
@router.get("/vendoresgscorecards", response_model=List[Dict[str, Any]])
def list_vendoresgscorecards(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorESGScorecard records with pagination and filtering."""
    svc = VendorESGScorecardService()
    items = svc.list_vendoresgscorecards(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendoresgscorecards/{item_id}", response_model=Dict[str, Any])
def get_vendoresgscorecard_by_id(item_id: int):
    """Retrieve detailed record for VendorESGScorecard by ID."""
    svc = VendorESGScorecardService()
    item = svc.get_vendoresgscorecard_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorESGScorecard with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendoresgscorecards", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendoresgscorecard(payload: VendorESGScorecardCreateSchema):
    """Create new VendorESGScorecard instance in enterprise repository."""
    svc = VendorESGScorecardService()
    try:
        item = svc.create_vendoresgscorecard(
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

@router.put("/vendoresgscorecards/{item_id}", response_model=Dict[str, Any])
def update_vendoresgscorecard(item_id: int, payload: VendorESGScorecardUpdateSchema):
    """Update existing VendorESGScorecard record fields."""
    svc = VendorESGScorecardService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendoresgscorecard(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorESGScorecard with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendoresgscorecards/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendoresgscorecard(item_id: int, hard: bool = Query(False)):
    """Delete VendorESGScorecard record (soft-delete by default)."""
    svc = VendorESGScorecardService()
    ok = svc.delete_vendoresgscorecard(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorESGScorecard with ID {item_id} not found")
    return None

@router.get("/vendoresgscorecards/analytics/metrics", response_model=Dict[str, Any])
def get_vendoresgscorecard_metrics():
    """Calculate summary statistical KPIs for VendorESGScorecard collection."""
    svc = VendorESGScorecardService()
    return svc.calculate_aggregate_metrics()

# ==================== RegulatoryCarbonFiling Endpoints ====================
@router.get("/regulatorycarbonfilings", response_model=List[Dict[str, Any]])
def list_regulatorycarbonfilings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RegulatoryCarbonFiling records with pagination and filtering."""
    svc = RegulatoryCarbonFilingService()
    items = svc.list_regulatorycarbonfilings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/regulatorycarbonfilings/{item_id}", response_model=Dict[str, Any])
def get_regulatorycarbonfiling_by_id(item_id: int):
    """Retrieve detailed record for RegulatoryCarbonFiling by ID."""
    svc = RegulatoryCarbonFilingService()
    item = svc.get_regulatorycarbonfiling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RegulatoryCarbonFiling with ID {item_id} not found")
    return item.to_dict()

@router.post("/regulatorycarbonfilings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_regulatorycarbonfiling(payload: RegulatoryCarbonFilingCreateSchema):
    """Create new RegulatoryCarbonFiling instance in enterprise repository."""
    svc = RegulatoryCarbonFilingService()
    try:
        item = svc.create_regulatorycarbonfiling(
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

@router.put("/regulatorycarbonfilings/{item_id}", response_model=Dict[str, Any])
def update_regulatorycarbonfiling(item_id: int, payload: RegulatoryCarbonFilingUpdateSchema):
    """Update existing RegulatoryCarbonFiling record fields."""
    svc = RegulatoryCarbonFilingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_regulatorycarbonfiling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RegulatoryCarbonFiling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/regulatorycarbonfilings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_regulatorycarbonfiling(item_id: int, hard: bool = Query(False)):
    """Delete RegulatoryCarbonFiling record (soft-delete by default)."""
    svc = RegulatoryCarbonFilingService()
    ok = svc.delete_regulatorycarbonfiling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RegulatoryCarbonFiling with ID {item_id} not found")
    return None

@router.get("/regulatorycarbonfilings/analytics/metrics", response_model=Dict[str, Any])
def get_regulatorycarbonfiling_metrics():
    """Calculate summary statistical KPIs for RegulatoryCarbonFiling collection."""
    svc = RegulatoryCarbonFilingService()
    return svc.calculate_aggregate_metrics()

# ==================== OffsetCertificate Endpoints ====================
@router.get("/offsetcertificates", response_model=List[Dict[str, Any]])
def list_offsetcertificates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OffsetCertificate records with pagination and filtering."""
    svc = OffsetCertificateService()
    items = svc.list_offsetcertificates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/offsetcertificates/{item_id}", response_model=Dict[str, Any])
def get_offsetcertificate_by_id(item_id: int):
    """Retrieve detailed record for OffsetCertificate by ID."""
    svc = OffsetCertificateService()
    item = svc.get_offsetcertificate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OffsetCertificate with ID {item_id} not found")
    return item.to_dict()

@router.post("/offsetcertificates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_offsetcertificate(payload: OffsetCertificateCreateSchema):
    """Create new OffsetCertificate instance in enterprise repository."""
    svc = OffsetCertificateService()
    try:
        item = svc.create_offsetcertificate(
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

@router.put("/offsetcertificates/{item_id}", response_model=Dict[str, Any])
def update_offsetcertificate(item_id: int, payload: OffsetCertificateUpdateSchema):
    """Update existing OffsetCertificate record fields."""
    svc = OffsetCertificateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_offsetcertificate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OffsetCertificate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/offsetcertificates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_offsetcertificate(item_id: int, hard: bool = Query(False)):
    """Delete OffsetCertificate record (soft-delete by default)."""
    svc = OffsetCertificateService()
    ok = svc.delete_offsetcertificate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OffsetCertificate with ID {item_id} not found")
    return None

@router.get("/offsetcertificates/analytics/metrics", response_model=Dict[str, Any])
def get_offsetcertificate_metrics():
    """Calculate summary statistical KPIs for OffsetCertificate collection."""
    svc = OffsetCertificateService()
    return svc.calculate_aggregate_metrics()

# ==================== CommunityImpactProject Endpoints ====================
@router.get("/communityimpactprojects", response_model=List[Dict[str, Any]])
def list_communityimpactprojects(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CommunityImpactProject records with pagination and filtering."""
    svc = CommunityImpactProjectService()
    items = svc.list_communityimpactprojects(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/communityimpactprojects/{item_id}", response_model=Dict[str, Any])
def get_communityimpactproject_by_id(item_id: int):
    """Retrieve detailed record for CommunityImpactProject by ID."""
    svc = CommunityImpactProjectService()
    item = svc.get_communityimpactproject_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CommunityImpactProject with ID {item_id} not found")
    return item.to_dict()

@router.post("/communityimpactprojects", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_communityimpactproject(payload: CommunityImpactProjectCreateSchema):
    """Create new CommunityImpactProject instance in enterprise repository."""
    svc = CommunityImpactProjectService()
    try:
        item = svc.create_communityimpactproject(
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

@router.put("/communityimpactprojects/{item_id}", response_model=Dict[str, Any])
def update_communityimpactproject(item_id: int, payload: CommunityImpactProjectUpdateSchema):
    """Update existing CommunityImpactProject record fields."""
    svc = CommunityImpactProjectService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_communityimpactproject(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CommunityImpactProject with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/communityimpactprojects/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_communityimpactproject(item_id: int, hard: bool = Query(False)):
    """Delete CommunityImpactProject record (soft-delete by default)."""
    svc = CommunityImpactProjectService()
    ok = svc.delete_communityimpactproject(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CommunityImpactProject with ID {item_id} not found")
    return None

@router.get("/communityimpactprojects/analytics/metrics", response_model=Dict[str, Any])
def get_communityimpactproject_metrics():
    """Calculate summary statistical KPIs for CommunityImpactProject collection."""
    svc = CommunityImpactProjectService()
    return svc.calculate_aggregate_metrics()

