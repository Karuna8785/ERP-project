"""
Quality Management & CAPA Engine - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    InspectionPlanTemplateService,
    IncomingInspectionRecordService,
    InProcessAuditService,
    FinalReleaseInspectionService,
    NonConformanceReportService,
    CorrectiveActionPlanService,
    PreventiveActionItemService,
    RootCauseAnalysisService,
    CalibrationScheduleService,
    GaugeToolService,
    SamplingStandardRuleService,
    SupplierQualityAuditService,
    CustomerComplaintQAService,
    CertificateOfAnalysisService,
    StabilityStudyService,
    RegulatoryAuditInspectionService,
)
from .schemas import (
    InspectionPlanTemplateCreateSchema, InspectionPlanTemplateUpdateSchema, InspectionPlanTemplateResponseSchema,
    IncomingInspectionRecordCreateSchema, IncomingInspectionRecordUpdateSchema, IncomingInspectionRecordResponseSchema,
    InProcessAuditCreateSchema, InProcessAuditUpdateSchema, InProcessAuditResponseSchema,
    FinalReleaseInspectionCreateSchema, FinalReleaseInspectionUpdateSchema, FinalReleaseInspectionResponseSchema,
    NonConformanceReportCreateSchema, NonConformanceReportUpdateSchema, NonConformanceReportResponseSchema,
    CorrectiveActionPlanCreateSchema, CorrectiveActionPlanUpdateSchema, CorrectiveActionPlanResponseSchema,
    PreventiveActionItemCreateSchema, PreventiveActionItemUpdateSchema, PreventiveActionItemResponseSchema,
    RootCauseAnalysisCreateSchema, RootCauseAnalysisUpdateSchema, RootCauseAnalysisResponseSchema,
    CalibrationScheduleCreateSchema, CalibrationScheduleUpdateSchema, CalibrationScheduleResponseSchema,
    GaugeToolCreateSchema, GaugeToolUpdateSchema, GaugeToolResponseSchema,
    SamplingStandardRuleCreateSchema, SamplingStandardRuleUpdateSchema, SamplingStandardRuleResponseSchema,
    SupplierQualityAuditCreateSchema, SupplierQualityAuditUpdateSchema, SupplierQualityAuditResponseSchema,
    CustomerComplaintQACreateSchema, CustomerComplaintQAUpdateSchema, CustomerComplaintQAResponseSchema,
    CertificateOfAnalysisCreateSchema, CertificateOfAnalysisUpdateSchema, CertificateOfAnalysisResponseSchema,
    StabilityStudyCreateSchema, StabilityStudyUpdateSchema, StabilityStudyResponseSchema,
    RegulatoryAuditInspectionCreateSchema, RegulatoryAuditInspectionUpdateSchema, RegulatoryAuditInspectionResponseSchema,
)

router = APIRouter(prefix="/quality_assurance", tags=["Quality Management & CAPA Engine"])

# ==================== InspectionPlanTemplate Endpoints ====================
@router.get("/inspectionplantemplates", response_model=List[Dict[str, Any]])
def list_inspectionplantemplates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InspectionPlanTemplate records with pagination and filtering."""
    svc = InspectionPlanTemplateService()
    items = svc.list_inspectionplantemplates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inspectionplantemplates/{item_id}", response_model=Dict[str, Any])
def get_inspectionplantemplate_by_id(item_id: int):
    """Retrieve detailed record for InspectionPlanTemplate by ID."""
    svc = InspectionPlanTemplateService()
    item = svc.get_inspectionplantemplate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InspectionPlanTemplate with ID {item_id} not found")
    return item.to_dict()

@router.post("/inspectionplantemplates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inspectionplantemplate(payload: InspectionPlanTemplateCreateSchema):
    """Create new InspectionPlanTemplate instance in enterprise repository."""
    svc = InspectionPlanTemplateService()
    try:
        item = svc.create_inspectionplantemplate(
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

@router.put("/inspectionplantemplates/{item_id}", response_model=Dict[str, Any])
def update_inspectionplantemplate(item_id: int, payload: InspectionPlanTemplateUpdateSchema):
    """Update existing InspectionPlanTemplate record fields."""
    svc = InspectionPlanTemplateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inspectionplantemplate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InspectionPlanTemplate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inspectionplantemplates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inspectionplantemplate(item_id: int, hard: bool = Query(False)):
    """Delete InspectionPlanTemplate record (soft-delete by default)."""
    svc = InspectionPlanTemplateService()
    ok = svc.delete_inspectionplantemplate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InspectionPlanTemplate with ID {item_id} not found")
    return None

@router.get("/inspectionplantemplates/analytics/metrics", response_model=Dict[str, Any])
def get_inspectionplantemplate_metrics():
    """Calculate summary statistical KPIs for InspectionPlanTemplate collection."""
    svc = InspectionPlanTemplateService()
    return svc.calculate_aggregate_metrics()

# ==================== IncomingInspectionRecord Endpoints ====================
@router.get("/incominginspectionrecords", response_model=List[Dict[str, Any]])
def list_incominginspectionrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IncomingInspectionRecord records with pagination and filtering."""
    svc = IncomingInspectionRecordService()
    items = svc.list_incominginspectionrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/incominginspectionrecords/{item_id}", response_model=Dict[str, Any])
def get_incominginspectionrecord_by_id(item_id: int):
    """Retrieve detailed record for IncomingInspectionRecord by ID."""
    svc = IncomingInspectionRecordService()
    item = svc.get_incominginspectionrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IncomingInspectionRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/incominginspectionrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_incominginspectionrecord(payload: IncomingInspectionRecordCreateSchema):
    """Create new IncomingInspectionRecord instance in enterprise repository."""
    svc = IncomingInspectionRecordService()
    try:
        item = svc.create_incominginspectionrecord(
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

@router.put("/incominginspectionrecords/{item_id}", response_model=Dict[str, Any])
def update_incominginspectionrecord(item_id: int, payload: IncomingInspectionRecordUpdateSchema):
    """Update existing IncomingInspectionRecord record fields."""
    svc = IncomingInspectionRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_incominginspectionrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IncomingInspectionRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/incominginspectionrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incominginspectionrecord(item_id: int, hard: bool = Query(False)):
    """Delete IncomingInspectionRecord record (soft-delete by default)."""
    svc = IncomingInspectionRecordService()
    ok = svc.delete_incominginspectionrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IncomingInspectionRecord with ID {item_id} not found")
    return None

@router.get("/incominginspectionrecords/analytics/metrics", response_model=Dict[str, Any])
def get_incominginspectionrecord_metrics():
    """Calculate summary statistical KPIs for IncomingInspectionRecord collection."""
    svc = IncomingInspectionRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== InProcessAudit Endpoints ====================
@router.get("/inprocessaudits", response_model=List[Dict[str, Any]])
def list_inprocessaudits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InProcessAudit records with pagination and filtering."""
    svc = InProcessAuditService()
    items = svc.list_inprocessaudits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inprocessaudits/{item_id}", response_model=Dict[str, Any])
def get_inprocessaudit_by_id(item_id: int):
    """Retrieve detailed record for InProcessAudit by ID."""
    svc = InProcessAuditService()
    item = svc.get_inprocessaudit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InProcessAudit with ID {item_id} not found")
    return item.to_dict()

@router.post("/inprocessaudits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inprocessaudit(payload: InProcessAuditCreateSchema):
    """Create new InProcessAudit instance in enterprise repository."""
    svc = InProcessAuditService()
    try:
        item = svc.create_inprocessaudit(
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

@router.put("/inprocessaudits/{item_id}", response_model=Dict[str, Any])
def update_inprocessaudit(item_id: int, payload: InProcessAuditUpdateSchema):
    """Update existing InProcessAudit record fields."""
    svc = InProcessAuditService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inprocessaudit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InProcessAudit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inprocessaudits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inprocessaudit(item_id: int, hard: bool = Query(False)):
    """Delete InProcessAudit record (soft-delete by default)."""
    svc = InProcessAuditService()
    ok = svc.delete_inprocessaudit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InProcessAudit with ID {item_id} not found")
    return None

@router.get("/inprocessaudits/analytics/metrics", response_model=Dict[str, Any])
def get_inprocessaudit_metrics():
    """Calculate summary statistical KPIs for InProcessAudit collection."""
    svc = InProcessAuditService()
    return svc.calculate_aggregate_metrics()

# ==================== FinalReleaseInspection Endpoints ====================
@router.get("/finalreleaseinspections", response_model=List[Dict[str, Any]])
def list_finalreleaseinspections(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FinalReleaseInspection records with pagination and filtering."""
    svc = FinalReleaseInspectionService()
    items = svc.list_finalreleaseinspections(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/finalreleaseinspections/{item_id}", response_model=Dict[str, Any])
def get_finalreleaseinspection_by_id(item_id: int):
    """Retrieve detailed record for FinalReleaseInspection by ID."""
    svc = FinalReleaseInspectionService()
    item = svc.get_finalreleaseinspection_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FinalReleaseInspection with ID {item_id} not found")
    return item.to_dict()

@router.post("/finalreleaseinspections", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_finalreleaseinspection(payload: FinalReleaseInspectionCreateSchema):
    """Create new FinalReleaseInspection instance in enterprise repository."""
    svc = FinalReleaseInspectionService()
    try:
        item = svc.create_finalreleaseinspection(
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

@router.put("/finalreleaseinspections/{item_id}", response_model=Dict[str, Any])
def update_finalreleaseinspection(item_id: int, payload: FinalReleaseInspectionUpdateSchema):
    """Update existing FinalReleaseInspection record fields."""
    svc = FinalReleaseInspectionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_finalreleaseinspection(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FinalReleaseInspection with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/finalreleaseinspections/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_finalreleaseinspection(item_id: int, hard: bool = Query(False)):
    """Delete FinalReleaseInspection record (soft-delete by default)."""
    svc = FinalReleaseInspectionService()
    ok = svc.delete_finalreleaseinspection(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FinalReleaseInspection with ID {item_id} not found")
    return None

@router.get("/finalreleaseinspections/analytics/metrics", response_model=Dict[str, Any])
def get_finalreleaseinspection_metrics():
    """Calculate summary statistical KPIs for FinalReleaseInspection collection."""
    svc = FinalReleaseInspectionService()
    return svc.calculate_aggregate_metrics()

# ==================== NonConformanceReport Endpoints ====================
@router.get("/nonconformancereports", response_model=List[Dict[str, Any]])
def list_nonconformancereports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List NonConformanceReport records with pagination and filtering."""
    svc = NonConformanceReportService()
    items = svc.list_nonconformancereports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/nonconformancereports/{item_id}", response_model=Dict[str, Any])
def get_nonconformancereport_by_id(item_id: int):
    """Retrieve detailed record for NonConformanceReport by ID."""
    svc = NonConformanceReportService()
    item = svc.get_nonconformancereport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"NonConformanceReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/nonconformancereports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_nonconformancereport(payload: NonConformanceReportCreateSchema):
    """Create new NonConformanceReport instance in enterprise repository."""
    svc = NonConformanceReportService()
    try:
        item = svc.create_nonconformancereport(
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

@router.put("/nonconformancereports/{item_id}", response_model=Dict[str, Any])
def update_nonconformancereport(item_id: int, payload: NonConformanceReportUpdateSchema):
    """Update existing NonConformanceReport record fields."""
    svc = NonConformanceReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_nonconformancereport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"NonConformanceReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/nonconformancereports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nonconformancereport(item_id: int, hard: bool = Query(False)):
    """Delete NonConformanceReport record (soft-delete by default)."""
    svc = NonConformanceReportService()
    ok = svc.delete_nonconformancereport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"NonConformanceReport with ID {item_id} not found")
    return None

@router.get("/nonconformancereports/analytics/metrics", response_model=Dict[str, Any])
def get_nonconformancereport_metrics():
    """Calculate summary statistical KPIs for NonConformanceReport collection."""
    svc = NonConformanceReportService()
    return svc.calculate_aggregate_metrics()

# ==================== CorrectiveActionPlan Endpoints ====================
@router.get("/correctiveactionplans", response_model=List[Dict[str, Any]])
def list_correctiveactionplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CorrectiveActionPlan records with pagination and filtering."""
    svc = CorrectiveActionPlanService()
    items = svc.list_correctiveactionplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/correctiveactionplans/{item_id}", response_model=Dict[str, Any])
def get_correctiveactionplan_by_id(item_id: int):
    """Retrieve detailed record for CorrectiveActionPlan by ID."""
    svc = CorrectiveActionPlanService()
    item = svc.get_correctiveactionplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CorrectiveActionPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/correctiveactionplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_correctiveactionplan(payload: CorrectiveActionPlanCreateSchema):
    """Create new CorrectiveActionPlan instance in enterprise repository."""
    svc = CorrectiveActionPlanService()
    try:
        item = svc.create_correctiveactionplan(
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

@router.put("/correctiveactionplans/{item_id}", response_model=Dict[str, Any])
def update_correctiveactionplan(item_id: int, payload: CorrectiveActionPlanUpdateSchema):
    """Update existing CorrectiveActionPlan record fields."""
    svc = CorrectiveActionPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_correctiveactionplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CorrectiveActionPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/correctiveactionplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_correctiveactionplan(item_id: int, hard: bool = Query(False)):
    """Delete CorrectiveActionPlan record (soft-delete by default)."""
    svc = CorrectiveActionPlanService()
    ok = svc.delete_correctiveactionplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CorrectiveActionPlan with ID {item_id} not found")
    return None

@router.get("/correctiveactionplans/analytics/metrics", response_model=Dict[str, Any])
def get_correctiveactionplan_metrics():
    """Calculate summary statistical KPIs for CorrectiveActionPlan collection."""
    svc = CorrectiveActionPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== PreventiveActionItem Endpoints ====================
@router.get("/preventiveactionitems", response_model=List[Dict[str, Any]])
def list_preventiveactionitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PreventiveActionItem records with pagination and filtering."""
    svc = PreventiveActionItemService()
    items = svc.list_preventiveactionitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/preventiveactionitems/{item_id}", response_model=Dict[str, Any])
def get_preventiveactionitem_by_id(item_id: int):
    """Retrieve detailed record for PreventiveActionItem by ID."""
    svc = PreventiveActionItemService()
    item = svc.get_preventiveactionitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PreventiveActionItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/preventiveactionitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_preventiveactionitem(payload: PreventiveActionItemCreateSchema):
    """Create new PreventiveActionItem instance in enterprise repository."""
    svc = PreventiveActionItemService()
    try:
        item = svc.create_preventiveactionitem(
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

@router.put("/preventiveactionitems/{item_id}", response_model=Dict[str, Any])
def update_preventiveactionitem(item_id: int, payload: PreventiveActionItemUpdateSchema):
    """Update existing PreventiveActionItem record fields."""
    svc = PreventiveActionItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_preventiveactionitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PreventiveActionItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/preventiveactionitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_preventiveactionitem(item_id: int, hard: bool = Query(False)):
    """Delete PreventiveActionItem record (soft-delete by default)."""
    svc = PreventiveActionItemService()
    ok = svc.delete_preventiveactionitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PreventiveActionItem with ID {item_id} not found")
    return None

@router.get("/preventiveactionitems/analytics/metrics", response_model=Dict[str, Any])
def get_preventiveactionitem_metrics():
    """Calculate summary statistical KPIs for PreventiveActionItem collection."""
    svc = PreventiveActionItemService()
    return svc.calculate_aggregate_metrics()

# ==================== RootCauseAnalysis Endpoints ====================
@router.get("/rootcauseanalysiss", response_model=List[Dict[str, Any]])
def list_rootcauseanalysiss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RootCauseAnalysis records with pagination and filtering."""
    svc = RootCauseAnalysisService()
    items = svc.list_rootcauseanalysiss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/rootcauseanalysiss/{item_id}", response_model=Dict[str, Any])
def get_rootcauseanalysis_by_id(item_id: int):
    """Retrieve detailed record for RootCauseAnalysis by ID."""
    svc = RootCauseAnalysisService()
    item = svc.get_rootcauseanalysis_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RootCauseAnalysis with ID {item_id} not found")
    return item.to_dict()

@router.post("/rootcauseanalysiss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_rootcauseanalysis(payload: RootCauseAnalysisCreateSchema):
    """Create new RootCauseAnalysis instance in enterprise repository."""
    svc = RootCauseAnalysisService()
    try:
        item = svc.create_rootcauseanalysis(
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

@router.put("/rootcauseanalysiss/{item_id}", response_model=Dict[str, Any])
def update_rootcauseanalysis(item_id: int, payload: RootCauseAnalysisUpdateSchema):
    """Update existing RootCauseAnalysis record fields."""
    svc = RootCauseAnalysisService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_rootcauseanalysis(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RootCauseAnalysis with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/rootcauseanalysiss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rootcauseanalysis(item_id: int, hard: bool = Query(False)):
    """Delete RootCauseAnalysis record (soft-delete by default)."""
    svc = RootCauseAnalysisService()
    ok = svc.delete_rootcauseanalysis(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RootCauseAnalysis with ID {item_id} not found")
    return None

@router.get("/rootcauseanalysiss/analytics/metrics", response_model=Dict[str, Any])
def get_rootcauseanalysis_metrics():
    """Calculate summary statistical KPIs for RootCauseAnalysis collection."""
    svc = RootCauseAnalysisService()
    return svc.calculate_aggregate_metrics()

# ==================== CalibrationSchedule Endpoints ====================
@router.get("/calibrationschedules", response_model=List[Dict[str, Any]])
def list_calibrationschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CalibrationSchedule records with pagination and filtering."""
    svc = CalibrationScheduleService()
    items = svc.list_calibrationschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/calibrationschedules/{item_id}", response_model=Dict[str, Any])
def get_calibrationschedule_by_id(item_id: int):
    """Retrieve detailed record for CalibrationSchedule by ID."""
    svc = CalibrationScheduleService()
    item = svc.get_calibrationschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CalibrationSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/calibrationschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_calibrationschedule(payload: CalibrationScheduleCreateSchema):
    """Create new CalibrationSchedule instance in enterprise repository."""
    svc = CalibrationScheduleService()
    try:
        item = svc.create_calibrationschedule(
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

@router.put("/calibrationschedules/{item_id}", response_model=Dict[str, Any])
def update_calibrationschedule(item_id: int, payload: CalibrationScheduleUpdateSchema):
    """Update existing CalibrationSchedule record fields."""
    svc = CalibrationScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_calibrationschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CalibrationSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/calibrationschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_calibrationschedule(item_id: int, hard: bool = Query(False)):
    """Delete CalibrationSchedule record (soft-delete by default)."""
    svc = CalibrationScheduleService()
    ok = svc.delete_calibrationschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CalibrationSchedule with ID {item_id} not found")
    return None

@router.get("/calibrationschedules/analytics/metrics", response_model=Dict[str, Any])
def get_calibrationschedule_metrics():
    """Calculate summary statistical KPIs for CalibrationSchedule collection."""
    svc = CalibrationScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== GaugeTool Endpoints ====================
@router.get("/gaugetools", response_model=List[Dict[str, Any]])
def list_gaugetools(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GaugeTool records with pagination and filtering."""
    svc = GaugeToolService()
    items = svc.list_gaugetools(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/gaugetools/{item_id}", response_model=Dict[str, Any])
def get_gaugetool_by_id(item_id: int):
    """Retrieve detailed record for GaugeTool by ID."""
    svc = GaugeToolService()
    item = svc.get_gaugetool_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GaugeTool with ID {item_id} not found")
    return item.to_dict()

@router.post("/gaugetools", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_gaugetool(payload: GaugeToolCreateSchema):
    """Create new GaugeTool instance in enterprise repository."""
    svc = GaugeToolService()
    try:
        item = svc.create_gaugetool(
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

@router.put("/gaugetools/{item_id}", response_model=Dict[str, Any])
def update_gaugetool(item_id: int, payload: GaugeToolUpdateSchema):
    """Update existing GaugeTool record fields."""
    svc = GaugeToolService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_gaugetool(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GaugeTool with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/gaugetools/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gaugetool(item_id: int, hard: bool = Query(False)):
    """Delete GaugeTool record (soft-delete by default)."""
    svc = GaugeToolService()
    ok = svc.delete_gaugetool(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GaugeTool with ID {item_id} not found")
    return None

@router.get("/gaugetools/analytics/metrics", response_model=Dict[str, Any])
def get_gaugetool_metrics():
    """Calculate summary statistical KPIs for GaugeTool collection."""
    svc = GaugeToolService()
    return svc.calculate_aggregate_metrics()

# ==================== SamplingStandardRule Endpoints ====================
@router.get("/samplingstandardrules", response_model=List[Dict[str, Any]])
def list_samplingstandardrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SamplingStandardRule records with pagination and filtering."""
    svc = SamplingStandardRuleService()
    items = svc.list_samplingstandardrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/samplingstandardrules/{item_id}", response_model=Dict[str, Any])
def get_samplingstandardrule_by_id(item_id: int):
    """Retrieve detailed record for SamplingStandardRule by ID."""
    svc = SamplingStandardRuleService()
    item = svc.get_samplingstandardrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SamplingStandardRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/samplingstandardrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_samplingstandardrule(payload: SamplingStandardRuleCreateSchema):
    """Create new SamplingStandardRule instance in enterprise repository."""
    svc = SamplingStandardRuleService()
    try:
        item = svc.create_samplingstandardrule(
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

@router.put("/samplingstandardrules/{item_id}", response_model=Dict[str, Any])
def update_samplingstandardrule(item_id: int, payload: SamplingStandardRuleUpdateSchema):
    """Update existing SamplingStandardRule record fields."""
    svc = SamplingStandardRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_samplingstandardrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SamplingStandardRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/samplingstandardrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_samplingstandardrule(item_id: int, hard: bool = Query(False)):
    """Delete SamplingStandardRule record (soft-delete by default)."""
    svc = SamplingStandardRuleService()
    ok = svc.delete_samplingstandardrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SamplingStandardRule with ID {item_id} not found")
    return None

@router.get("/samplingstandardrules/analytics/metrics", response_model=Dict[str, Any])
def get_samplingstandardrule_metrics():
    """Calculate summary statistical KPIs for SamplingStandardRule collection."""
    svc = SamplingStandardRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== SupplierQualityAudit Endpoints ====================
@router.get("/supplierqualityaudits", response_model=List[Dict[str, Any]])
def list_supplierqualityaudits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupplierQualityAudit records with pagination and filtering."""
    svc = SupplierQualityAuditService()
    items = svc.list_supplierqualityaudits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supplierqualityaudits/{item_id}", response_model=Dict[str, Any])
def get_supplierqualityaudit_by_id(item_id: int):
    """Retrieve detailed record for SupplierQualityAudit by ID."""
    svc = SupplierQualityAuditService()
    item = svc.get_supplierqualityaudit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupplierQualityAudit with ID {item_id} not found")
    return item.to_dict()

@router.post("/supplierqualityaudits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supplierqualityaudit(payload: SupplierQualityAuditCreateSchema):
    """Create new SupplierQualityAudit instance in enterprise repository."""
    svc = SupplierQualityAuditService()
    try:
        item = svc.create_supplierqualityaudit(
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

@router.put("/supplierqualityaudits/{item_id}", response_model=Dict[str, Any])
def update_supplierqualityaudit(item_id: int, payload: SupplierQualityAuditUpdateSchema):
    """Update existing SupplierQualityAudit record fields."""
    svc = SupplierQualityAuditService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supplierqualityaudit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupplierQualityAudit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supplierqualityaudits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplierqualityaudit(item_id: int, hard: bool = Query(False)):
    """Delete SupplierQualityAudit record (soft-delete by default)."""
    svc = SupplierQualityAuditService()
    ok = svc.delete_supplierqualityaudit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupplierQualityAudit with ID {item_id} not found")
    return None

@router.get("/supplierqualityaudits/analytics/metrics", response_model=Dict[str, Any])
def get_supplierqualityaudit_metrics():
    """Calculate summary statistical KPIs for SupplierQualityAudit collection."""
    svc = SupplierQualityAuditService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerComplaintQA Endpoints ====================
@router.get("/customercomplaintqas", response_model=List[Dict[str, Any]])
def list_customercomplaintqas(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerComplaintQA records with pagination and filtering."""
    svc = CustomerComplaintQAService()
    items = svc.list_customercomplaintqas(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customercomplaintqas/{item_id}", response_model=Dict[str, Any])
def get_customercomplaintqa_by_id(item_id: int):
    """Retrieve detailed record for CustomerComplaintQA by ID."""
    svc = CustomerComplaintQAService()
    item = svc.get_customercomplaintqa_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerComplaintQA with ID {item_id} not found")
    return item.to_dict()

@router.post("/customercomplaintqas", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customercomplaintqa(payload: CustomerComplaintQACreateSchema):
    """Create new CustomerComplaintQA instance in enterprise repository."""
    svc = CustomerComplaintQAService()
    try:
        item = svc.create_customercomplaintqa(
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

@router.put("/customercomplaintqas/{item_id}", response_model=Dict[str, Any])
def update_customercomplaintqa(item_id: int, payload: CustomerComplaintQAUpdateSchema):
    """Update existing CustomerComplaintQA record fields."""
    svc = CustomerComplaintQAService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customercomplaintqa(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerComplaintQA with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customercomplaintqas/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customercomplaintqa(item_id: int, hard: bool = Query(False)):
    """Delete CustomerComplaintQA record (soft-delete by default)."""
    svc = CustomerComplaintQAService()
    ok = svc.delete_customercomplaintqa(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerComplaintQA with ID {item_id} not found")
    return None

@router.get("/customercomplaintqas/analytics/metrics", response_model=Dict[str, Any])
def get_customercomplaintqa_metrics():
    """Calculate summary statistical KPIs for CustomerComplaintQA collection."""
    svc = CustomerComplaintQAService()
    return svc.calculate_aggregate_metrics()

# ==================== CertificateOfAnalysis Endpoints ====================
@router.get("/certificateofanalysiss", response_model=List[Dict[str, Any]])
def list_certificateofanalysiss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CertificateOfAnalysis records with pagination and filtering."""
    svc = CertificateOfAnalysisService()
    items = svc.list_certificateofanalysiss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/certificateofanalysiss/{item_id}", response_model=Dict[str, Any])
def get_certificateofanalysis_by_id(item_id: int):
    """Retrieve detailed record for CertificateOfAnalysis by ID."""
    svc = CertificateOfAnalysisService()
    item = svc.get_certificateofanalysis_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CertificateOfAnalysis with ID {item_id} not found")
    return item.to_dict()

@router.post("/certificateofanalysiss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_certificateofanalysis(payload: CertificateOfAnalysisCreateSchema):
    """Create new CertificateOfAnalysis instance in enterprise repository."""
    svc = CertificateOfAnalysisService()
    try:
        item = svc.create_certificateofanalysis(
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

@router.put("/certificateofanalysiss/{item_id}", response_model=Dict[str, Any])
def update_certificateofanalysis(item_id: int, payload: CertificateOfAnalysisUpdateSchema):
    """Update existing CertificateOfAnalysis record fields."""
    svc = CertificateOfAnalysisService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_certificateofanalysis(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CertificateOfAnalysis with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/certificateofanalysiss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_certificateofanalysis(item_id: int, hard: bool = Query(False)):
    """Delete CertificateOfAnalysis record (soft-delete by default)."""
    svc = CertificateOfAnalysisService()
    ok = svc.delete_certificateofanalysis(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CertificateOfAnalysis with ID {item_id} not found")
    return None

@router.get("/certificateofanalysiss/analytics/metrics", response_model=Dict[str, Any])
def get_certificateofanalysis_metrics():
    """Calculate summary statistical KPIs for CertificateOfAnalysis collection."""
    svc = CertificateOfAnalysisService()
    return svc.calculate_aggregate_metrics()

# ==================== StabilityStudy Endpoints ====================
@router.get("/stabilitystudys", response_model=List[Dict[str, Any]])
def list_stabilitystudys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StabilityStudy records with pagination and filtering."""
    svc = StabilityStudyService()
    items = svc.list_stabilitystudys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/stabilitystudys/{item_id}", response_model=Dict[str, Any])
def get_stabilitystudy_by_id(item_id: int):
    """Retrieve detailed record for StabilityStudy by ID."""
    svc = StabilityStudyService()
    item = svc.get_stabilitystudy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StabilityStudy with ID {item_id} not found")
    return item.to_dict()

@router.post("/stabilitystudys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_stabilitystudy(payload: StabilityStudyCreateSchema):
    """Create new StabilityStudy instance in enterprise repository."""
    svc = StabilityStudyService()
    try:
        item = svc.create_stabilitystudy(
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

@router.put("/stabilitystudys/{item_id}", response_model=Dict[str, Any])
def update_stabilitystudy(item_id: int, payload: StabilityStudyUpdateSchema):
    """Update existing StabilityStudy record fields."""
    svc = StabilityStudyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_stabilitystudy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StabilityStudy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/stabilitystudys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stabilitystudy(item_id: int, hard: bool = Query(False)):
    """Delete StabilityStudy record (soft-delete by default)."""
    svc = StabilityStudyService()
    ok = svc.delete_stabilitystudy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StabilityStudy with ID {item_id} not found")
    return None

@router.get("/stabilitystudys/analytics/metrics", response_model=Dict[str, Any])
def get_stabilitystudy_metrics():
    """Calculate summary statistical KPIs for StabilityStudy collection."""
    svc = StabilityStudyService()
    return svc.calculate_aggregate_metrics()

# ==================== RegulatoryAuditInspection Endpoints ====================
@router.get("/regulatoryauditinspections", response_model=List[Dict[str, Any]])
def list_regulatoryauditinspections(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RegulatoryAuditInspection records with pagination and filtering."""
    svc = RegulatoryAuditInspectionService()
    items = svc.list_regulatoryauditinspections(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/regulatoryauditinspections/{item_id}", response_model=Dict[str, Any])
def get_regulatoryauditinspection_by_id(item_id: int):
    """Retrieve detailed record for RegulatoryAuditInspection by ID."""
    svc = RegulatoryAuditInspectionService()
    item = svc.get_regulatoryauditinspection_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RegulatoryAuditInspection with ID {item_id} not found")
    return item.to_dict()

@router.post("/regulatoryauditinspections", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_regulatoryauditinspection(payload: RegulatoryAuditInspectionCreateSchema):
    """Create new RegulatoryAuditInspection instance in enterprise repository."""
    svc = RegulatoryAuditInspectionService()
    try:
        item = svc.create_regulatoryauditinspection(
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

@router.put("/regulatoryauditinspections/{item_id}", response_model=Dict[str, Any])
def update_regulatoryauditinspection(item_id: int, payload: RegulatoryAuditInspectionUpdateSchema):
    """Update existing RegulatoryAuditInspection record fields."""
    svc = RegulatoryAuditInspectionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_regulatoryauditinspection(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RegulatoryAuditInspection with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/regulatoryauditinspections/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_regulatoryauditinspection(item_id: int, hard: bool = Query(False)):
    """Delete RegulatoryAuditInspection record (soft-delete by default)."""
    svc = RegulatoryAuditInspectionService()
    ok = svc.delete_regulatoryauditinspection(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RegulatoryAuditInspection with ID {item_id} not found")
    return None

@router.get("/regulatoryauditinspections/analytics/metrics", response_model=Dict[str, Any])
def get_regulatoryauditinspection_metrics():
    """Calculate summary statistical KPIs for RegulatoryAuditInspection collection."""
    svc = RegulatoryAuditInspectionService()
    return svc.calculate_aggregate_metrics()

