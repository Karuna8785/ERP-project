"""
Governance, Risk & Compliance (GRC) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    AuditFindingService,
    RiskRegisterService,
    ControlActivityService,
    CompliancePolicyService,
    AccessReviewService,
    DataRetentionScheduleService,
    GDPRRequestService,
    SOXControlService,
    ISORequirementService,
    VendorAssessmentService,
    PolicyAcknowledgementService,
    WhistleblowerReportService,
    SecurityIncidentService,
    CorrectiveActionService,
    EvidenceAttachmentService,
    RegulatoryFilingService,
)
from .schemas import (
    AuditFindingCreateSchema, AuditFindingUpdateSchema, AuditFindingResponseSchema,
    RiskRegisterCreateSchema, RiskRegisterUpdateSchema, RiskRegisterResponseSchema,
    ControlActivityCreateSchema, ControlActivityUpdateSchema, ControlActivityResponseSchema,
    CompliancePolicyCreateSchema, CompliancePolicyUpdateSchema, CompliancePolicyResponseSchema,
    AccessReviewCreateSchema, AccessReviewUpdateSchema, AccessReviewResponseSchema,
    DataRetentionScheduleCreateSchema, DataRetentionScheduleUpdateSchema, DataRetentionScheduleResponseSchema,
    GDPRRequestCreateSchema, GDPRRequestUpdateSchema, GDPRRequestResponseSchema,
    SOXControlCreateSchema, SOXControlUpdateSchema, SOXControlResponseSchema,
    ISORequirementCreateSchema, ISORequirementUpdateSchema, ISORequirementResponseSchema,
    VendorAssessmentCreateSchema, VendorAssessmentUpdateSchema, VendorAssessmentResponseSchema,
    PolicyAcknowledgementCreateSchema, PolicyAcknowledgementUpdateSchema, PolicyAcknowledgementResponseSchema,
    WhistleblowerReportCreateSchema, WhistleblowerReportUpdateSchema, WhistleblowerReportResponseSchema,
    SecurityIncidentCreateSchema, SecurityIncidentUpdateSchema, SecurityIncidentResponseSchema,
    CorrectiveActionCreateSchema, CorrectiveActionUpdateSchema, CorrectiveActionResponseSchema,
    EvidenceAttachmentCreateSchema, EvidenceAttachmentUpdateSchema, EvidenceAttachmentResponseSchema,
    RegulatoryFilingCreateSchema, RegulatoryFilingUpdateSchema, RegulatoryFilingResponseSchema,
)

router = APIRouter(prefix="/compliance", tags=["Governance, Risk & Compliance (GRC)"])

# ==================== AuditFinding Endpoints ====================
@router.get("/auditfindings", response_model=List[Dict[str, Any]])
def list_auditfindings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AuditFinding records with pagination and filtering."""
    svc = AuditFindingService()
    items = svc.list_auditfindings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/auditfindings/{item_id}", response_model=Dict[str, Any])
def get_auditfinding_by_id(item_id: int):
    """Retrieve detailed record for AuditFinding by ID."""
    svc = AuditFindingService()
    item = svc.get_auditfinding_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AuditFinding with ID {item_id} not found")
    return item.to_dict()

@router.post("/auditfindings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_auditfinding(payload: AuditFindingCreateSchema):
    """Create new AuditFinding instance in enterprise repository."""
    svc = AuditFindingService()
    try:
        item = svc.create_auditfinding(
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

@router.put("/auditfindings/{item_id}", response_model=Dict[str, Any])
def update_auditfinding(item_id: int, payload: AuditFindingUpdateSchema):
    """Update existing AuditFinding record fields."""
    svc = AuditFindingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_auditfinding(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AuditFinding with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/auditfindings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_auditfinding(item_id: int, hard: bool = Query(False)):
    """Delete AuditFinding record (soft-delete by default)."""
    svc = AuditFindingService()
    ok = svc.delete_auditfinding(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AuditFinding with ID {item_id} not found")
    return None

@router.get("/auditfindings/analytics/metrics", response_model=Dict[str, Any])
def get_auditfinding_metrics():
    """Calculate summary statistical KPIs for AuditFinding collection."""
    svc = AuditFindingService()
    return svc.calculate_aggregate_metrics()

# ==================== RiskRegister Endpoints ====================
@router.get("/riskregisters", response_model=List[Dict[str, Any]])
def list_riskregisters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RiskRegister records with pagination and filtering."""
    svc = RiskRegisterService()
    items = svc.list_riskregisters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/riskregisters/{item_id}", response_model=Dict[str, Any])
def get_riskregister_by_id(item_id: int):
    """Retrieve detailed record for RiskRegister by ID."""
    svc = RiskRegisterService()
    item = svc.get_riskregister_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RiskRegister with ID {item_id} not found")
    return item.to_dict()

@router.post("/riskregisters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_riskregister(payload: RiskRegisterCreateSchema):
    """Create new RiskRegister instance in enterprise repository."""
    svc = RiskRegisterService()
    try:
        item = svc.create_riskregister(
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

@router.put("/riskregisters/{item_id}", response_model=Dict[str, Any])
def update_riskregister(item_id: int, payload: RiskRegisterUpdateSchema):
    """Update existing RiskRegister record fields."""
    svc = RiskRegisterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_riskregister(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RiskRegister with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/riskregisters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_riskregister(item_id: int, hard: bool = Query(False)):
    """Delete RiskRegister record (soft-delete by default)."""
    svc = RiskRegisterService()
    ok = svc.delete_riskregister(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RiskRegister with ID {item_id} not found")
    return None

@router.get("/riskregisters/analytics/metrics", response_model=Dict[str, Any])
def get_riskregister_metrics():
    """Calculate summary statistical KPIs for RiskRegister collection."""
    svc = RiskRegisterService()
    return svc.calculate_aggregate_metrics()

# ==================== ControlActivity Endpoints ====================
@router.get("/controlactivitys", response_model=List[Dict[str, Any]])
def list_controlactivitys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ControlActivity records with pagination and filtering."""
    svc = ControlActivityService()
    items = svc.list_controlactivitys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/controlactivitys/{item_id}", response_model=Dict[str, Any])
def get_controlactivity_by_id(item_id: int):
    """Retrieve detailed record for ControlActivity by ID."""
    svc = ControlActivityService()
    item = svc.get_controlactivity_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ControlActivity with ID {item_id} not found")
    return item.to_dict()

@router.post("/controlactivitys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_controlactivity(payload: ControlActivityCreateSchema):
    """Create new ControlActivity instance in enterprise repository."""
    svc = ControlActivityService()
    try:
        item = svc.create_controlactivity(
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

@router.put("/controlactivitys/{item_id}", response_model=Dict[str, Any])
def update_controlactivity(item_id: int, payload: ControlActivityUpdateSchema):
    """Update existing ControlActivity record fields."""
    svc = ControlActivityService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_controlactivity(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ControlActivity with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/controlactivitys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_controlactivity(item_id: int, hard: bool = Query(False)):
    """Delete ControlActivity record (soft-delete by default)."""
    svc = ControlActivityService()
    ok = svc.delete_controlactivity(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ControlActivity with ID {item_id} not found")
    return None

@router.get("/controlactivitys/analytics/metrics", response_model=Dict[str, Any])
def get_controlactivity_metrics():
    """Calculate summary statistical KPIs for ControlActivity collection."""
    svc = ControlActivityService()
    return svc.calculate_aggregate_metrics()

# ==================== CompliancePolicy Endpoints ====================
@router.get("/compliancepolicys", response_model=List[Dict[str, Any]])
def list_compliancepolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CompliancePolicy records with pagination and filtering."""
    svc = CompliancePolicyService()
    items = svc.list_compliancepolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/compliancepolicys/{item_id}", response_model=Dict[str, Any])
def get_compliancepolicy_by_id(item_id: int):
    """Retrieve detailed record for CompliancePolicy by ID."""
    svc = CompliancePolicyService()
    item = svc.get_compliancepolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CompliancePolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/compliancepolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_compliancepolicy(payload: CompliancePolicyCreateSchema):
    """Create new CompliancePolicy instance in enterprise repository."""
    svc = CompliancePolicyService()
    try:
        item = svc.create_compliancepolicy(
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

@router.put("/compliancepolicys/{item_id}", response_model=Dict[str, Any])
def update_compliancepolicy(item_id: int, payload: CompliancePolicyUpdateSchema):
    """Update existing CompliancePolicy record fields."""
    svc = CompliancePolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_compliancepolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CompliancePolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/compliancepolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_compliancepolicy(item_id: int, hard: bool = Query(False)):
    """Delete CompliancePolicy record (soft-delete by default)."""
    svc = CompliancePolicyService()
    ok = svc.delete_compliancepolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CompliancePolicy with ID {item_id} not found")
    return None

@router.get("/compliancepolicys/analytics/metrics", response_model=Dict[str, Any])
def get_compliancepolicy_metrics():
    """Calculate summary statistical KPIs for CompliancePolicy collection."""
    svc = CompliancePolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== AccessReview Endpoints ====================
@router.get("/accessreviews", response_model=List[Dict[str, Any]])
def list_accessreviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AccessReview records with pagination and filtering."""
    svc = AccessReviewService()
    items = svc.list_accessreviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/accessreviews/{item_id}", response_model=Dict[str, Any])
def get_accessreview_by_id(item_id: int):
    """Retrieve detailed record for AccessReview by ID."""
    svc = AccessReviewService()
    item = svc.get_accessreview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AccessReview with ID {item_id} not found")
    return item.to_dict()

@router.post("/accessreviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_accessreview(payload: AccessReviewCreateSchema):
    """Create new AccessReview instance in enterprise repository."""
    svc = AccessReviewService()
    try:
        item = svc.create_accessreview(
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

@router.put("/accessreviews/{item_id}", response_model=Dict[str, Any])
def update_accessreview(item_id: int, payload: AccessReviewUpdateSchema):
    """Update existing AccessReview record fields."""
    svc = AccessReviewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_accessreview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AccessReview with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/accessreviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accessreview(item_id: int, hard: bool = Query(False)):
    """Delete AccessReview record (soft-delete by default)."""
    svc = AccessReviewService()
    ok = svc.delete_accessreview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AccessReview with ID {item_id} not found")
    return None

@router.get("/accessreviews/analytics/metrics", response_model=Dict[str, Any])
def get_accessreview_metrics():
    """Calculate summary statistical KPIs for AccessReview collection."""
    svc = AccessReviewService()
    return svc.calculate_aggregate_metrics()

# ==================== DataRetentionSchedule Endpoints ====================
@router.get("/dataretentionschedules", response_model=List[Dict[str, Any]])
def list_dataretentionschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataRetentionSchedule records with pagination and filtering."""
    svc = DataRetentionScheduleService()
    items = svc.list_dataretentionschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dataretentionschedules/{item_id}", response_model=Dict[str, Any])
def get_dataretentionschedule_by_id(item_id: int):
    """Retrieve detailed record for DataRetentionSchedule by ID."""
    svc = DataRetentionScheduleService()
    item = svc.get_dataretentionschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataRetentionSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/dataretentionschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dataretentionschedule(payload: DataRetentionScheduleCreateSchema):
    """Create new DataRetentionSchedule instance in enterprise repository."""
    svc = DataRetentionScheduleService()
    try:
        item = svc.create_dataretentionschedule(
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

@router.put("/dataretentionschedules/{item_id}", response_model=Dict[str, Any])
def update_dataretentionschedule(item_id: int, payload: DataRetentionScheduleUpdateSchema):
    """Update existing DataRetentionSchedule record fields."""
    svc = DataRetentionScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dataretentionschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataRetentionSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dataretentionschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dataretentionschedule(item_id: int, hard: bool = Query(False)):
    """Delete DataRetentionSchedule record (soft-delete by default)."""
    svc = DataRetentionScheduleService()
    ok = svc.delete_dataretentionschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataRetentionSchedule with ID {item_id} not found")
    return None

@router.get("/dataretentionschedules/analytics/metrics", response_model=Dict[str, Any])
def get_dataretentionschedule_metrics():
    """Calculate summary statistical KPIs for DataRetentionSchedule collection."""
    svc = DataRetentionScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== GDPRRequest Endpoints ====================
@router.get("/gdprrequests", response_model=List[Dict[str, Any]])
def list_gdprrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GDPRRequest records with pagination and filtering."""
    svc = GDPRRequestService()
    items = svc.list_gdprrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/gdprrequests/{item_id}", response_model=Dict[str, Any])
def get_gdprrequest_by_id(item_id: int):
    """Retrieve detailed record for GDPRRequest by ID."""
    svc = GDPRRequestService()
    item = svc.get_gdprrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GDPRRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/gdprrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_gdprrequest(payload: GDPRRequestCreateSchema):
    """Create new GDPRRequest instance in enterprise repository."""
    svc = GDPRRequestService()
    try:
        item = svc.create_gdprrequest(
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

@router.put("/gdprrequests/{item_id}", response_model=Dict[str, Any])
def update_gdprrequest(item_id: int, payload: GDPRRequestUpdateSchema):
    """Update existing GDPRRequest record fields."""
    svc = GDPRRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_gdprrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GDPRRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/gdprrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gdprrequest(item_id: int, hard: bool = Query(False)):
    """Delete GDPRRequest record (soft-delete by default)."""
    svc = GDPRRequestService()
    ok = svc.delete_gdprrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GDPRRequest with ID {item_id} not found")
    return None

@router.get("/gdprrequests/analytics/metrics", response_model=Dict[str, Any])
def get_gdprrequest_metrics():
    """Calculate summary statistical KPIs for GDPRRequest collection."""
    svc = GDPRRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== SOXControl Endpoints ====================
@router.get("/soxcontrols", response_model=List[Dict[str, Any]])
def list_soxcontrols(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SOXControl records with pagination and filtering."""
    svc = SOXControlService()
    items = svc.list_soxcontrols(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/soxcontrols/{item_id}", response_model=Dict[str, Any])
def get_soxcontrol_by_id(item_id: int):
    """Retrieve detailed record for SOXControl by ID."""
    svc = SOXControlService()
    item = svc.get_soxcontrol_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SOXControl with ID {item_id} not found")
    return item.to_dict()

@router.post("/soxcontrols", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_soxcontrol(payload: SOXControlCreateSchema):
    """Create new SOXControl instance in enterprise repository."""
    svc = SOXControlService()
    try:
        item = svc.create_soxcontrol(
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

@router.put("/soxcontrols/{item_id}", response_model=Dict[str, Any])
def update_soxcontrol(item_id: int, payload: SOXControlUpdateSchema):
    """Update existing SOXControl record fields."""
    svc = SOXControlService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_soxcontrol(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SOXControl with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/soxcontrols/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_soxcontrol(item_id: int, hard: bool = Query(False)):
    """Delete SOXControl record (soft-delete by default)."""
    svc = SOXControlService()
    ok = svc.delete_soxcontrol(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SOXControl with ID {item_id} not found")
    return None

@router.get("/soxcontrols/analytics/metrics", response_model=Dict[str, Any])
def get_soxcontrol_metrics():
    """Calculate summary statistical KPIs for SOXControl collection."""
    svc = SOXControlService()
    return svc.calculate_aggregate_metrics()

# ==================== ISORequirement Endpoints ====================
@router.get("/isorequirements", response_model=List[Dict[str, Any]])
def list_isorequirements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ISORequirement records with pagination and filtering."""
    svc = ISORequirementService()
    items = svc.list_isorequirements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/isorequirements/{item_id}", response_model=Dict[str, Any])
def get_isorequirement_by_id(item_id: int):
    """Retrieve detailed record for ISORequirement by ID."""
    svc = ISORequirementService()
    item = svc.get_isorequirement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ISORequirement with ID {item_id} not found")
    return item.to_dict()

@router.post("/isorequirements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_isorequirement(payload: ISORequirementCreateSchema):
    """Create new ISORequirement instance in enterprise repository."""
    svc = ISORequirementService()
    try:
        item = svc.create_isorequirement(
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

@router.put("/isorequirements/{item_id}", response_model=Dict[str, Any])
def update_isorequirement(item_id: int, payload: ISORequirementUpdateSchema):
    """Update existing ISORequirement record fields."""
    svc = ISORequirementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_isorequirement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ISORequirement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/isorequirements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_isorequirement(item_id: int, hard: bool = Query(False)):
    """Delete ISORequirement record (soft-delete by default)."""
    svc = ISORequirementService()
    ok = svc.delete_isorequirement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ISORequirement with ID {item_id} not found")
    return None

@router.get("/isorequirements/analytics/metrics", response_model=Dict[str, Any])
def get_isorequirement_metrics():
    """Calculate summary statistical KPIs for ISORequirement collection."""
    svc = ISORequirementService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorAssessment Endpoints ====================
@router.get("/vendorassessments", response_model=List[Dict[str, Any]])
def list_vendorassessments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorAssessment records with pagination and filtering."""
    svc = VendorAssessmentService()
    items = svc.list_vendorassessments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorassessments/{item_id}", response_model=Dict[str, Any])
def get_vendorassessment_by_id(item_id: int):
    """Retrieve detailed record for VendorAssessment by ID."""
    svc = VendorAssessmentService()
    item = svc.get_vendorassessment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorAssessment with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorassessments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorassessment(payload: VendorAssessmentCreateSchema):
    """Create new VendorAssessment instance in enterprise repository."""
    svc = VendorAssessmentService()
    try:
        item = svc.create_vendorassessment(
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

@router.put("/vendorassessments/{item_id}", response_model=Dict[str, Any])
def update_vendorassessment(item_id: int, payload: VendorAssessmentUpdateSchema):
    """Update existing VendorAssessment record fields."""
    svc = VendorAssessmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorassessment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorAssessment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorassessments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorassessment(item_id: int, hard: bool = Query(False)):
    """Delete VendorAssessment record (soft-delete by default)."""
    svc = VendorAssessmentService()
    ok = svc.delete_vendorassessment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorAssessment with ID {item_id} not found")
    return None

@router.get("/vendorassessments/analytics/metrics", response_model=Dict[str, Any])
def get_vendorassessment_metrics():
    """Calculate summary statistical KPIs for VendorAssessment collection."""
    svc = VendorAssessmentService()
    return svc.calculate_aggregate_metrics()

# ==================== PolicyAcknowledgement Endpoints ====================
@router.get("/policyacknowledgements", response_model=List[Dict[str, Any]])
def list_policyacknowledgements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PolicyAcknowledgement records with pagination and filtering."""
    svc = PolicyAcknowledgementService()
    items = svc.list_policyacknowledgements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/policyacknowledgements/{item_id}", response_model=Dict[str, Any])
def get_policyacknowledgement_by_id(item_id: int):
    """Retrieve detailed record for PolicyAcknowledgement by ID."""
    svc = PolicyAcknowledgementService()
    item = svc.get_policyacknowledgement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PolicyAcknowledgement with ID {item_id} not found")
    return item.to_dict()

@router.post("/policyacknowledgements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_policyacknowledgement(payload: PolicyAcknowledgementCreateSchema):
    """Create new PolicyAcknowledgement instance in enterprise repository."""
    svc = PolicyAcknowledgementService()
    try:
        item = svc.create_policyacknowledgement(
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

@router.put("/policyacknowledgements/{item_id}", response_model=Dict[str, Any])
def update_policyacknowledgement(item_id: int, payload: PolicyAcknowledgementUpdateSchema):
    """Update existing PolicyAcknowledgement record fields."""
    svc = PolicyAcknowledgementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_policyacknowledgement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PolicyAcknowledgement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/policyacknowledgements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_policyacknowledgement(item_id: int, hard: bool = Query(False)):
    """Delete PolicyAcknowledgement record (soft-delete by default)."""
    svc = PolicyAcknowledgementService()
    ok = svc.delete_policyacknowledgement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PolicyAcknowledgement with ID {item_id} not found")
    return None

@router.get("/policyacknowledgements/analytics/metrics", response_model=Dict[str, Any])
def get_policyacknowledgement_metrics():
    """Calculate summary statistical KPIs for PolicyAcknowledgement collection."""
    svc = PolicyAcknowledgementService()
    return svc.calculate_aggregate_metrics()

# ==================== WhistleblowerReport Endpoints ====================
@router.get("/whistleblowerreports", response_model=List[Dict[str, Any]])
def list_whistleblowerreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WhistleblowerReport records with pagination and filtering."""
    svc = WhistleblowerReportService()
    items = svc.list_whistleblowerreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/whistleblowerreports/{item_id}", response_model=Dict[str, Any])
def get_whistleblowerreport_by_id(item_id: int):
    """Retrieve detailed record for WhistleblowerReport by ID."""
    svc = WhistleblowerReportService()
    item = svc.get_whistleblowerreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WhistleblowerReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/whistleblowerreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_whistleblowerreport(payload: WhistleblowerReportCreateSchema):
    """Create new WhistleblowerReport instance in enterprise repository."""
    svc = WhistleblowerReportService()
    try:
        item = svc.create_whistleblowerreport(
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

@router.put("/whistleblowerreports/{item_id}", response_model=Dict[str, Any])
def update_whistleblowerreport(item_id: int, payload: WhistleblowerReportUpdateSchema):
    """Update existing WhistleblowerReport record fields."""
    svc = WhistleblowerReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_whistleblowerreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WhistleblowerReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/whistleblowerreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_whistleblowerreport(item_id: int, hard: bool = Query(False)):
    """Delete WhistleblowerReport record (soft-delete by default)."""
    svc = WhistleblowerReportService()
    ok = svc.delete_whistleblowerreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WhistleblowerReport with ID {item_id} not found")
    return None

@router.get("/whistleblowerreports/analytics/metrics", response_model=Dict[str, Any])
def get_whistleblowerreport_metrics():
    """Calculate summary statistical KPIs for WhistleblowerReport collection."""
    svc = WhistleblowerReportService()
    return svc.calculate_aggregate_metrics()

# ==================== SecurityIncident Endpoints ====================
@router.get("/securityincidents", response_model=List[Dict[str, Any]])
def list_securityincidents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SecurityIncident records with pagination and filtering."""
    svc = SecurityIncidentService()
    items = svc.list_securityincidents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/securityincidents/{item_id}", response_model=Dict[str, Any])
def get_securityincident_by_id(item_id: int):
    """Retrieve detailed record for SecurityIncident by ID."""
    svc = SecurityIncidentService()
    item = svc.get_securityincident_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SecurityIncident with ID {item_id} not found")
    return item.to_dict()

@router.post("/securityincidents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_securityincident(payload: SecurityIncidentCreateSchema):
    """Create new SecurityIncident instance in enterprise repository."""
    svc = SecurityIncidentService()
    try:
        item = svc.create_securityincident(
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

@router.put("/securityincidents/{item_id}", response_model=Dict[str, Any])
def update_securityincident(item_id: int, payload: SecurityIncidentUpdateSchema):
    """Update existing SecurityIncident record fields."""
    svc = SecurityIncidentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_securityincident(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SecurityIncident with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/securityincidents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_securityincident(item_id: int, hard: bool = Query(False)):
    """Delete SecurityIncident record (soft-delete by default)."""
    svc = SecurityIncidentService()
    ok = svc.delete_securityincident(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SecurityIncident with ID {item_id} not found")
    return None

@router.get("/securityincidents/analytics/metrics", response_model=Dict[str, Any])
def get_securityincident_metrics():
    """Calculate summary statistical KPIs for SecurityIncident collection."""
    svc = SecurityIncidentService()
    return svc.calculate_aggregate_metrics()

# ==================== CorrectiveAction Endpoints ====================
@router.get("/correctiveactions", response_model=List[Dict[str, Any]])
def list_correctiveactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CorrectiveAction records with pagination and filtering."""
    svc = CorrectiveActionService()
    items = svc.list_correctiveactions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/correctiveactions/{item_id}", response_model=Dict[str, Any])
def get_correctiveaction_by_id(item_id: int):
    """Retrieve detailed record for CorrectiveAction by ID."""
    svc = CorrectiveActionService()
    item = svc.get_correctiveaction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CorrectiveAction with ID {item_id} not found")
    return item.to_dict()

@router.post("/correctiveactions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_correctiveaction(payload: CorrectiveActionCreateSchema):
    """Create new CorrectiveAction instance in enterprise repository."""
    svc = CorrectiveActionService()
    try:
        item = svc.create_correctiveaction(
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

@router.put("/correctiveactions/{item_id}", response_model=Dict[str, Any])
def update_correctiveaction(item_id: int, payload: CorrectiveActionUpdateSchema):
    """Update existing CorrectiveAction record fields."""
    svc = CorrectiveActionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_correctiveaction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CorrectiveAction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/correctiveactions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_correctiveaction(item_id: int, hard: bool = Query(False)):
    """Delete CorrectiveAction record (soft-delete by default)."""
    svc = CorrectiveActionService()
    ok = svc.delete_correctiveaction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CorrectiveAction with ID {item_id} not found")
    return None

@router.get("/correctiveactions/analytics/metrics", response_model=Dict[str, Any])
def get_correctiveaction_metrics():
    """Calculate summary statistical KPIs for CorrectiveAction collection."""
    svc = CorrectiveActionService()
    return svc.calculate_aggregate_metrics()

# ==================== EvidenceAttachment Endpoints ====================
@router.get("/evidenceattachments", response_model=List[Dict[str, Any]])
def list_evidenceattachments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EvidenceAttachment records with pagination and filtering."""
    svc = EvidenceAttachmentService()
    items = svc.list_evidenceattachments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/evidenceattachments/{item_id}", response_model=Dict[str, Any])
def get_evidenceattachment_by_id(item_id: int):
    """Retrieve detailed record for EvidenceAttachment by ID."""
    svc = EvidenceAttachmentService()
    item = svc.get_evidenceattachment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EvidenceAttachment with ID {item_id} not found")
    return item.to_dict()

@router.post("/evidenceattachments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_evidenceattachment(payload: EvidenceAttachmentCreateSchema):
    """Create new EvidenceAttachment instance in enterprise repository."""
    svc = EvidenceAttachmentService()
    try:
        item = svc.create_evidenceattachment(
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

@router.put("/evidenceattachments/{item_id}", response_model=Dict[str, Any])
def update_evidenceattachment(item_id: int, payload: EvidenceAttachmentUpdateSchema):
    """Update existing EvidenceAttachment record fields."""
    svc = EvidenceAttachmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_evidenceattachment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EvidenceAttachment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/evidenceattachments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_evidenceattachment(item_id: int, hard: bool = Query(False)):
    """Delete EvidenceAttachment record (soft-delete by default)."""
    svc = EvidenceAttachmentService()
    ok = svc.delete_evidenceattachment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EvidenceAttachment with ID {item_id} not found")
    return None

@router.get("/evidenceattachments/analytics/metrics", response_model=Dict[str, Any])
def get_evidenceattachment_metrics():
    """Calculate summary statistical KPIs for EvidenceAttachment collection."""
    svc = EvidenceAttachmentService()
    return svc.calculate_aggregate_metrics()

# ==================== RegulatoryFiling Endpoints ====================
@router.get("/regulatoryfilings", response_model=List[Dict[str, Any]])
def list_regulatoryfilings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RegulatoryFiling records with pagination and filtering."""
    svc = RegulatoryFilingService()
    items = svc.list_regulatoryfilings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/regulatoryfilings/{item_id}", response_model=Dict[str, Any])
def get_regulatoryfiling_by_id(item_id: int):
    """Retrieve detailed record for RegulatoryFiling by ID."""
    svc = RegulatoryFilingService()
    item = svc.get_regulatoryfiling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RegulatoryFiling with ID {item_id} not found")
    return item.to_dict()

@router.post("/regulatoryfilings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_regulatoryfiling(payload: RegulatoryFilingCreateSchema):
    """Create new RegulatoryFiling instance in enterprise repository."""
    svc = RegulatoryFilingService()
    try:
        item = svc.create_regulatoryfiling(
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

@router.put("/regulatoryfilings/{item_id}", response_model=Dict[str, Any])
def update_regulatoryfiling(item_id: int, payload: RegulatoryFilingUpdateSchema):
    """Update existing RegulatoryFiling record fields."""
    svc = RegulatoryFilingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_regulatoryfiling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RegulatoryFiling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/regulatoryfilings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_regulatoryfiling(item_id: int, hard: bool = Query(False)):
    """Delete RegulatoryFiling record (soft-delete by default)."""
    svc = RegulatoryFilingService()
    ok = svc.delete_regulatoryfiling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RegulatoryFiling with ID {item_id} not found")
    return None

@router.get("/regulatoryfilings/analytics/metrics", response_model=Dict[str, Any])
def get_regulatoryfiling_metrics():
    """Calculate summary statistical KPIs for RegulatoryFiling collection."""
    svc = RegulatoryFilingService()
    return svc.calculate_aggregate_metrics()

