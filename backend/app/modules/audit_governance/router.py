"""
Enterprise Audit Governance & SoD - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    SegregationOfDutiesRuleService,
    SoDViolationDetectionService,
    UserRoleMatrixService,
    PermissionEntitlementService,
    PeriodicAccessReviewCampaignService,
    PrivilegedAccessRequestService,
    EmergencyFirefighterAccessService,
    ImmutableSystemAuditLogService,
    DataChangeCaptureEventService,
    SecurityPolicyDefinitionService,
    SessionAuthenticationLogService,
    DatabaseQueryAuditLogService,
    ExportActivityLogService,
    AdminActionLogService,
    CertificationSignoffService,
    ComplianceExceptionWaiverService,
)
from .schemas import (
    SegregationOfDutiesRuleCreateSchema, SegregationOfDutiesRuleUpdateSchema, SegregationOfDutiesRuleResponseSchema,
    SoDViolationDetectionCreateSchema, SoDViolationDetectionUpdateSchema, SoDViolationDetectionResponseSchema,
    UserRoleMatrixCreateSchema, UserRoleMatrixUpdateSchema, UserRoleMatrixResponseSchema,
    PermissionEntitlementCreateSchema, PermissionEntitlementUpdateSchema, PermissionEntitlementResponseSchema,
    PeriodicAccessReviewCampaignCreateSchema, PeriodicAccessReviewCampaignUpdateSchema, PeriodicAccessReviewCampaignResponseSchema,
    PrivilegedAccessRequestCreateSchema, PrivilegedAccessRequestUpdateSchema, PrivilegedAccessRequestResponseSchema,
    EmergencyFirefighterAccessCreateSchema, EmergencyFirefighterAccessUpdateSchema, EmergencyFirefighterAccessResponseSchema,
    ImmutableSystemAuditLogCreateSchema, ImmutableSystemAuditLogUpdateSchema, ImmutableSystemAuditLogResponseSchema,
    DataChangeCaptureEventCreateSchema, DataChangeCaptureEventUpdateSchema, DataChangeCaptureEventResponseSchema,
    SecurityPolicyDefinitionCreateSchema, SecurityPolicyDefinitionUpdateSchema, SecurityPolicyDefinitionResponseSchema,
    SessionAuthenticationLogCreateSchema, SessionAuthenticationLogUpdateSchema, SessionAuthenticationLogResponseSchema,
    DatabaseQueryAuditLogCreateSchema, DatabaseQueryAuditLogUpdateSchema, DatabaseQueryAuditLogResponseSchema,
    ExportActivityLogCreateSchema, ExportActivityLogUpdateSchema, ExportActivityLogResponseSchema,
    AdminActionLogCreateSchema, AdminActionLogUpdateSchema, AdminActionLogResponseSchema,
    CertificationSignoffCreateSchema, CertificationSignoffUpdateSchema, CertificationSignoffResponseSchema,
    ComplianceExceptionWaiverCreateSchema, ComplianceExceptionWaiverUpdateSchema, ComplianceExceptionWaiverResponseSchema,
)

router = APIRouter(prefix="/audit_governance", tags=["Enterprise Audit Governance & SoD"])

# ==================== SegregationOfDutiesRule Endpoints ====================
@router.get("/segregationofdutiesrules", response_model=List[Dict[str, Any]])
def list_segregationofdutiesrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SegregationOfDutiesRule records with pagination and filtering."""
    svc = SegregationOfDutiesRuleService()
    items = svc.list_segregationofdutiesrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/segregationofdutiesrules/{item_id}", response_model=Dict[str, Any])
def get_segregationofdutiesrule_by_id(item_id: int):
    """Retrieve detailed record for SegregationOfDutiesRule by ID."""
    svc = SegregationOfDutiesRuleService()
    item = svc.get_segregationofdutiesrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SegregationOfDutiesRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/segregationofdutiesrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_segregationofdutiesrule(payload: SegregationOfDutiesRuleCreateSchema):
    """Create new SegregationOfDutiesRule instance in enterprise repository."""
    svc = SegregationOfDutiesRuleService()
    try:
        item = svc.create_segregationofdutiesrule(
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

@router.put("/segregationofdutiesrules/{item_id}", response_model=Dict[str, Any])
def update_segregationofdutiesrule(item_id: int, payload: SegregationOfDutiesRuleUpdateSchema):
    """Update existing SegregationOfDutiesRule record fields."""
    svc = SegregationOfDutiesRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_segregationofdutiesrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SegregationOfDutiesRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/segregationofdutiesrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_segregationofdutiesrule(item_id: int, hard: bool = Query(False)):
    """Delete SegregationOfDutiesRule record (soft-delete by default)."""
    svc = SegregationOfDutiesRuleService()
    ok = svc.delete_segregationofdutiesrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SegregationOfDutiesRule with ID {item_id} not found")
    return None

@router.get("/segregationofdutiesrules/analytics/metrics", response_model=Dict[str, Any])
def get_segregationofdutiesrule_metrics():
    """Calculate summary statistical KPIs for SegregationOfDutiesRule collection."""
    svc = SegregationOfDutiesRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== SoDViolationDetection Endpoints ====================
@router.get("/sodviolationdetections", response_model=List[Dict[str, Any]])
def list_sodviolationdetections(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SoDViolationDetection records with pagination and filtering."""
    svc = SoDViolationDetectionService()
    items = svc.list_sodviolationdetections(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sodviolationdetections/{item_id}", response_model=Dict[str, Any])
def get_sodviolationdetection_by_id(item_id: int):
    """Retrieve detailed record for SoDViolationDetection by ID."""
    svc = SoDViolationDetectionService()
    item = svc.get_sodviolationdetection_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SoDViolationDetection with ID {item_id} not found")
    return item.to_dict()

@router.post("/sodviolationdetections", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sodviolationdetection(payload: SoDViolationDetectionCreateSchema):
    """Create new SoDViolationDetection instance in enterprise repository."""
    svc = SoDViolationDetectionService()
    try:
        item = svc.create_sodviolationdetection(
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

@router.put("/sodviolationdetections/{item_id}", response_model=Dict[str, Any])
def update_sodviolationdetection(item_id: int, payload: SoDViolationDetectionUpdateSchema):
    """Update existing SoDViolationDetection record fields."""
    svc = SoDViolationDetectionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sodviolationdetection(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SoDViolationDetection with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sodviolationdetections/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sodviolationdetection(item_id: int, hard: bool = Query(False)):
    """Delete SoDViolationDetection record (soft-delete by default)."""
    svc = SoDViolationDetectionService()
    ok = svc.delete_sodviolationdetection(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SoDViolationDetection with ID {item_id} not found")
    return None

@router.get("/sodviolationdetections/analytics/metrics", response_model=Dict[str, Any])
def get_sodviolationdetection_metrics():
    """Calculate summary statistical KPIs for SoDViolationDetection collection."""
    svc = SoDViolationDetectionService()
    return svc.calculate_aggregate_metrics()

# ==================== UserRoleMatrix Endpoints ====================
@router.get("/userrolematrixs", response_model=List[Dict[str, Any]])
def list_userrolematrixs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UserRoleMatrix records with pagination and filtering."""
    svc = UserRoleMatrixService()
    items = svc.list_userrolematrixs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/userrolematrixs/{item_id}", response_model=Dict[str, Any])
def get_userrolematrix_by_id(item_id: int):
    """Retrieve detailed record for UserRoleMatrix by ID."""
    svc = UserRoleMatrixService()
    item = svc.get_userrolematrix_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UserRoleMatrix with ID {item_id} not found")
    return item.to_dict()

@router.post("/userrolematrixs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_userrolematrix(payload: UserRoleMatrixCreateSchema):
    """Create new UserRoleMatrix instance in enterprise repository."""
    svc = UserRoleMatrixService()
    try:
        item = svc.create_userrolematrix(
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

@router.put("/userrolematrixs/{item_id}", response_model=Dict[str, Any])
def update_userrolematrix(item_id: int, payload: UserRoleMatrixUpdateSchema):
    """Update existing UserRoleMatrix record fields."""
    svc = UserRoleMatrixService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_userrolematrix(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UserRoleMatrix with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/userrolematrixs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_userrolematrix(item_id: int, hard: bool = Query(False)):
    """Delete UserRoleMatrix record (soft-delete by default)."""
    svc = UserRoleMatrixService()
    ok = svc.delete_userrolematrix(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UserRoleMatrix with ID {item_id} not found")
    return None

@router.get("/userrolematrixs/analytics/metrics", response_model=Dict[str, Any])
def get_userrolematrix_metrics():
    """Calculate summary statistical KPIs for UserRoleMatrix collection."""
    svc = UserRoleMatrixService()
    return svc.calculate_aggregate_metrics()

# ==================== PermissionEntitlement Endpoints ====================
@router.get("/permissionentitlements", response_model=List[Dict[str, Any]])
def list_permissionentitlements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PermissionEntitlement records with pagination and filtering."""
    svc = PermissionEntitlementService()
    items = svc.list_permissionentitlements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/permissionentitlements/{item_id}", response_model=Dict[str, Any])
def get_permissionentitlement_by_id(item_id: int):
    """Retrieve detailed record for PermissionEntitlement by ID."""
    svc = PermissionEntitlementService()
    item = svc.get_permissionentitlement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PermissionEntitlement with ID {item_id} not found")
    return item.to_dict()

@router.post("/permissionentitlements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_permissionentitlement(payload: PermissionEntitlementCreateSchema):
    """Create new PermissionEntitlement instance in enterprise repository."""
    svc = PermissionEntitlementService()
    try:
        item = svc.create_permissionentitlement(
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

@router.put("/permissionentitlements/{item_id}", response_model=Dict[str, Any])
def update_permissionentitlement(item_id: int, payload: PermissionEntitlementUpdateSchema):
    """Update existing PermissionEntitlement record fields."""
    svc = PermissionEntitlementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_permissionentitlement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PermissionEntitlement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/permissionentitlements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_permissionentitlement(item_id: int, hard: bool = Query(False)):
    """Delete PermissionEntitlement record (soft-delete by default)."""
    svc = PermissionEntitlementService()
    ok = svc.delete_permissionentitlement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PermissionEntitlement with ID {item_id} not found")
    return None

@router.get("/permissionentitlements/analytics/metrics", response_model=Dict[str, Any])
def get_permissionentitlement_metrics():
    """Calculate summary statistical KPIs for PermissionEntitlement collection."""
    svc = PermissionEntitlementService()
    return svc.calculate_aggregate_metrics()

# ==================== PeriodicAccessReviewCampaign Endpoints ====================
@router.get("/periodicaccessreviewcampaigns", response_model=List[Dict[str, Any]])
def list_periodicaccessreviewcampaigns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PeriodicAccessReviewCampaign records with pagination and filtering."""
    svc = PeriodicAccessReviewCampaignService()
    items = svc.list_periodicaccessreviewcampaigns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/periodicaccessreviewcampaigns/{item_id}", response_model=Dict[str, Any])
def get_periodicaccessreviewcampaign_by_id(item_id: int):
    """Retrieve detailed record for PeriodicAccessReviewCampaign by ID."""
    svc = PeriodicAccessReviewCampaignService()
    item = svc.get_periodicaccessreviewcampaign_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PeriodicAccessReviewCampaign with ID {item_id} not found")
    return item.to_dict()

@router.post("/periodicaccessreviewcampaigns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_periodicaccessreviewcampaign(payload: PeriodicAccessReviewCampaignCreateSchema):
    """Create new PeriodicAccessReviewCampaign instance in enterprise repository."""
    svc = PeriodicAccessReviewCampaignService()
    try:
        item = svc.create_periodicaccessreviewcampaign(
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

@router.put("/periodicaccessreviewcampaigns/{item_id}", response_model=Dict[str, Any])
def update_periodicaccessreviewcampaign(item_id: int, payload: PeriodicAccessReviewCampaignUpdateSchema):
    """Update existing PeriodicAccessReviewCampaign record fields."""
    svc = PeriodicAccessReviewCampaignService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_periodicaccessreviewcampaign(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PeriodicAccessReviewCampaign with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/periodicaccessreviewcampaigns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_periodicaccessreviewcampaign(item_id: int, hard: bool = Query(False)):
    """Delete PeriodicAccessReviewCampaign record (soft-delete by default)."""
    svc = PeriodicAccessReviewCampaignService()
    ok = svc.delete_periodicaccessreviewcampaign(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PeriodicAccessReviewCampaign with ID {item_id} not found")
    return None

@router.get("/periodicaccessreviewcampaigns/analytics/metrics", response_model=Dict[str, Any])
def get_periodicaccessreviewcampaign_metrics():
    """Calculate summary statistical KPIs for PeriodicAccessReviewCampaign collection."""
    svc = PeriodicAccessReviewCampaignService()
    return svc.calculate_aggregate_metrics()

# ==================== PrivilegedAccessRequest Endpoints ====================
@router.get("/privilegedaccessrequests", response_model=List[Dict[str, Any]])
def list_privilegedaccessrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PrivilegedAccessRequest records with pagination and filtering."""
    svc = PrivilegedAccessRequestService()
    items = svc.list_privilegedaccessrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/privilegedaccessrequests/{item_id}", response_model=Dict[str, Any])
def get_privilegedaccessrequest_by_id(item_id: int):
    """Retrieve detailed record for PrivilegedAccessRequest by ID."""
    svc = PrivilegedAccessRequestService()
    item = svc.get_privilegedaccessrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PrivilegedAccessRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/privilegedaccessrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_privilegedaccessrequest(payload: PrivilegedAccessRequestCreateSchema):
    """Create new PrivilegedAccessRequest instance in enterprise repository."""
    svc = PrivilegedAccessRequestService()
    try:
        item = svc.create_privilegedaccessrequest(
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

@router.put("/privilegedaccessrequests/{item_id}", response_model=Dict[str, Any])
def update_privilegedaccessrequest(item_id: int, payload: PrivilegedAccessRequestUpdateSchema):
    """Update existing PrivilegedAccessRequest record fields."""
    svc = PrivilegedAccessRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_privilegedaccessrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PrivilegedAccessRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/privilegedaccessrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_privilegedaccessrequest(item_id: int, hard: bool = Query(False)):
    """Delete PrivilegedAccessRequest record (soft-delete by default)."""
    svc = PrivilegedAccessRequestService()
    ok = svc.delete_privilegedaccessrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PrivilegedAccessRequest with ID {item_id} not found")
    return None

@router.get("/privilegedaccessrequests/analytics/metrics", response_model=Dict[str, Any])
def get_privilegedaccessrequest_metrics():
    """Calculate summary statistical KPIs for PrivilegedAccessRequest collection."""
    svc = PrivilegedAccessRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== EmergencyFirefighterAccess Endpoints ====================
@router.get("/emergencyfirefighteraccesss", response_model=List[Dict[str, Any]])
def list_emergencyfirefighteraccesss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmergencyFirefighterAccess records with pagination and filtering."""
    svc = EmergencyFirefighterAccessService()
    items = svc.list_emergencyfirefighteraccesss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/emergencyfirefighteraccesss/{item_id}", response_model=Dict[str, Any])
def get_emergencyfirefighteraccess_by_id(item_id: int):
    """Retrieve detailed record for EmergencyFirefighterAccess by ID."""
    svc = EmergencyFirefighterAccessService()
    item = svc.get_emergencyfirefighteraccess_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmergencyFirefighterAccess with ID {item_id} not found")
    return item.to_dict()

@router.post("/emergencyfirefighteraccesss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_emergencyfirefighteraccess(payload: EmergencyFirefighterAccessCreateSchema):
    """Create new EmergencyFirefighterAccess instance in enterprise repository."""
    svc = EmergencyFirefighterAccessService()
    try:
        item = svc.create_emergencyfirefighteraccess(
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

@router.put("/emergencyfirefighteraccesss/{item_id}", response_model=Dict[str, Any])
def update_emergencyfirefighteraccess(item_id: int, payload: EmergencyFirefighterAccessUpdateSchema):
    """Update existing EmergencyFirefighterAccess record fields."""
    svc = EmergencyFirefighterAccessService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_emergencyfirefighteraccess(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmergencyFirefighterAccess with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/emergencyfirefighteraccesss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_emergencyfirefighteraccess(item_id: int, hard: bool = Query(False)):
    """Delete EmergencyFirefighterAccess record (soft-delete by default)."""
    svc = EmergencyFirefighterAccessService()
    ok = svc.delete_emergencyfirefighteraccess(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmergencyFirefighterAccess with ID {item_id} not found")
    return None

@router.get("/emergencyfirefighteraccesss/analytics/metrics", response_model=Dict[str, Any])
def get_emergencyfirefighteraccess_metrics():
    """Calculate summary statistical KPIs for EmergencyFirefighterAccess collection."""
    svc = EmergencyFirefighterAccessService()
    return svc.calculate_aggregate_metrics()

# ==================== ImmutableSystemAuditLog Endpoints ====================
@router.get("/immutablesystemauditlogs", response_model=List[Dict[str, Any]])
def list_immutablesystemauditlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ImmutableSystemAuditLog records with pagination and filtering."""
    svc = ImmutableSystemAuditLogService()
    items = svc.list_immutablesystemauditlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/immutablesystemauditlogs/{item_id}", response_model=Dict[str, Any])
def get_immutablesystemauditlog_by_id(item_id: int):
    """Retrieve detailed record for ImmutableSystemAuditLog by ID."""
    svc = ImmutableSystemAuditLogService()
    item = svc.get_immutablesystemauditlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ImmutableSystemAuditLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/immutablesystemauditlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_immutablesystemauditlog(payload: ImmutableSystemAuditLogCreateSchema):
    """Create new ImmutableSystemAuditLog instance in enterprise repository."""
    svc = ImmutableSystemAuditLogService()
    try:
        item = svc.create_immutablesystemauditlog(
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

@router.put("/immutablesystemauditlogs/{item_id}", response_model=Dict[str, Any])
def update_immutablesystemauditlog(item_id: int, payload: ImmutableSystemAuditLogUpdateSchema):
    """Update existing ImmutableSystemAuditLog record fields."""
    svc = ImmutableSystemAuditLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_immutablesystemauditlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ImmutableSystemAuditLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/immutablesystemauditlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_immutablesystemauditlog(item_id: int, hard: bool = Query(False)):
    """Delete ImmutableSystemAuditLog record (soft-delete by default)."""
    svc = ImmutableSystemAuditLogService()
    ok = svc.delete_immutablesystemauditlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ImmutableSystemAuditLog with ID {item_id} not found")
    return None

@router.get("/immutablesystemauditlogs/analytics/metrics", response_model=Dict[str, Any])
def get_immutablesystemauditlog_metrics():
    """Calculate summary statistical KPIs for ImmutableSystemAuditLog collection."""
    svc = ImmutableSystemAuditLogService()
    return svc.calculate_aggregate_metrics()

# ==================== DataChangeCaptureEvent Endpoints ====================
@router.get("/datachangecaptureevents", response_model=List[Dict[str, Any]])
def list_datachangecaptureevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataChangeCaptureEvent records with pagination and filtering."""
    svc = DataChangeCaptureEventService()
    items = svc.list_datachangecaptureevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/datachangecaptureevents/{item_id}", response_model=Dict[str, Any])
def get_datachangecaptureevent_by_id(item_id: int):
    """Retrieve detailed record for DataChangeCaptureEvent by ID."""
    svc = DataChangeCaptureEventService()
    item = svc.get_datachangecaptureevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataChangeCaptureEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/datachangecaptureevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_datachangecaptureevent(payload: DataChangeCaptureEventCreateSchema):
    """Create new DataChangeCaptureEvent instance in enterprise repository."""
    svc = DataChangeCaptureEventService()
    try:
        item = svc.create_datachangecaptureevent(
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

@router.put("/datachangecaptureevents/{item_id}", response_model=Dict[str, Any])
def update_datachangecaptureevent(item_id: int, payload: DataChangeCaptureEventUpdateSchema):
    """Update existing DataChangeCaptureEvent record fields."""
    svc = DataChangeCaptureEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_datachangecaptureevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataChangeCaptureEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/datachangecaptureevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_datachangecaptureevent(item_id: int, hard: bool = Query(False)):
    """Delete DataChangeCaptureEvent record (soft-delete by default)."""
    svc = DataChangeCaptureEventService()
    ok = svc.delete_datachangecaptureevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataChangeCaptureEvent with ID {item_id} not found")
    return None

@router.get("/datachangecaptureevents/analytics/metrics", response_model=Dict[str, Any])
def get_datachangecaptureevent_metrics():
    """Calculate summary statistical KPIs for DataChangeCaptureEvent collection."""
    svc = DataChangeCaptureEventService()
    return svc.calculate_aggregate_metrics()

# ==================== SecurityPolicyDefinition Endpoints ====================
@router.get("/securitypolicydefinitions", response_model=List[Dict[str, Any]])
def list_securitypolicydefinitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SecurityPolicyDefinition records with pagination and filtering."""
    svc = SecurityPolicyDefinitionService()
    items = svc.list_securitypolicydefinitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/securitypolicydefinitions/{item_id}", response_model=Dict[str, Any])
def get_securitypolicydefinition_by_id(item_id: int):
    """Retrieve detailed record for SecurityPolicyDefinition by ID."""
    svc = SecurityPolicyDefinitionService()
    item = svc.get_securitypolicydefinition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SecurityPolicyDefinition with ID {item_id} not found")
    return item.to_dict()

@router.post("/securitypolicydefinitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_securitypolicydefinition(payload: SecurityPolicyDefinitionCreateSchema):
    """Create new SecurityPolicyDefinition instance in enterprise repository."""
    svc = SecurityPolicyDefinitionService()
    try:
        item = svc.create_securitypolicydefinition(
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

@router.put("/securitypolicydefinitions/{item_id}", response_model=Dict[str, Any])
def update_securitypolicydefinition(item_id: int, payload: SecurityPolicyDefinitionUpdateSchema):
    """Update existing SecurityPolicyDefinition record fields."""
    svc = SecurityPolicyDefinitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_securitypolicydefinition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SecurityPolicyDefinition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/securitypolicydefinitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_securitypolicydefinition(item_id: int, hard: bool = Query(False)):
    """Delete SecurityPolicyDefinition record (soft-delete by default)."""
    svc = SecurityPolicyDefinitionService()
    ok = svc.delete_securitypolicydefinition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SecurityPolicyDefinition with ID {item_id} not found")
    return None

@router.get("/securitypolicydefinitions/analytics/metrics", response_model=Dict[str, Any])
def get_securitypolicydefinition_metrics():
    """Calculate summary statistical KPIs for SecurityPolicyDefinition collection."""
    svc = SecurityPolicyDefinitionService()
    return svc.calculate_aggregate_metrics()

# ==================== SessionAuthenticationLog Endpoints ====================
@router.get("/sessionauthenticationlogs", response_model=List[Dict[str, Any]])
def list_sessionauthenticationlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SessionAuthenticationLog records with pagination and filtering."""
    svc = SessionAuthenticationLogService()
    items = svc.list_sessionauthenticationlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sessionauthenticationlogs/{item_id}", response_model=Dict[str, Any])
def get_sessionauthenticationlog_by_id(item_id: int):
    """Retrieve detailed record for SessionAuthenticationLog by ID."""
    svc = SessionAuthenticationLogService()
    item = svc.get_sessionauthenticationlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SessionAuthenticationLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/sessionauthenticationlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sessionauthenticationlog(payload: SessionAuthenticationLogCreateSchema):
    """Create new SessionAuthenticationLog instance in enterprise repository."""
    svc = SessionAuthenticationLogService()
    try:
        item = svc.create_sessionauthenticationlog(
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

@router.put("/sessionauthenticationlogs/{item_id}", response_model=Dict[str, Any])
def update_sessionauthenticationlog(item_id: int, payload: SessionAuthenticationLogUpdateSchema):
    """Update existing SessionAuthenticationLog record fields."""
    svc = SessionAuthenticationLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sessionauthenticationlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SessionAuthenticationLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sessionauthenticationlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sessionauthenticationlog(item_id: int, hard: bool = Query(False)):
    """Delete SessionAuthenticationLog record (soft-delete by default)."""
    svc = SessionAuthenticationLogService()
    ok = svc.delete_sessionauthenticationlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SessionAuthenticationLog with ID {item_id} not found")
    return None

@router.get("/sessionauthenticationlogs/analytics/metrics", response_model=Dict[str, Any])
def get_sessionauthenticationlog_metrics():
    """Calculate summary statistical KPIs for SessionAuthenticationLog collection."""
    svc = SessionAuthenticationLogService()
    return svc.calculate_aggregate_metrics()

# ==================== DatabaseQueryAuditLog Endpoints ====================
@router.get("/databasequeryauditlogs", response_model=List[Dict[str, Any]])
def list_databasequeryauditlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DatabaseQueryAuditLog records with pagination and filtering."""
    svc = DatabaseQueryAuditLogService()
    items = svc.list_databasequeryauditlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/databasequeryauditlogs/{item_id}", response_model=Dict[str, Any])
def get_databasequeryauditlog_by_id(item_id: int):
    """Retrieve detailed record for DatabaseQueryAuditLog by ID."""
    svc = DatabaseQueryAuditLogService()
    item = svc.get_databasequeryauditlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DatabaseQueryAuditLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/databasequeryauditlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_databasequeryauditlog(payload: DatabaseQueryAuditLogCreateSchema):
    """Create new DatabaseQueryAuditLog instance in enterprise repository."""
    svc = DatabaseQueryAuditLogService()
    try:
        item = svc.create_databasequeryauditlog(
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

@router.put("/databasequeryauditlogs/{item_id}", response_model=Dict[str, Any])
def update_databasequeryauditlog(item_id: int, payload: DatabaseQueryAuditLogUpdateSchema):
    """Update existing DatabaseQueryAuditLog record fields."""
    svc = DatabaseQueryAuditLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_databasequeryauditlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DatabaseQueryAuditLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/databasequeryauditlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_databasequeryauditlog(item_id: int, hard: bool = Query(False)):
    """Delete DatabaseQueryAuditLog record (soft-delete by default)."""
    svc = DatabaseQueryAuditLogService()
    ok = svc.delete_databasequeryauditlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DatabaseQueryAuditLog with ID {item_id} not found")
    return None

@router.get("/databasequeryauditlogs/analytics/metrics", response_model=Dict[str, Any])
def get_databasequeryauditlog_metrics():
    """Calculate summary statistical KPIs for DatabaseQueryAuditLog collection."""
    svc = DatabaseQueryAuditLogService()
    return svc.calculate_aggregate_metrics()

# ==================== ExportActivityLog Endpoints ====================
@router.get("/exportactivitylogs", response_model=List[Dict[str, Any]])
def list_exportactivitylogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExportActivityLog records with pagination and filtering."""
    svc = ExportActivityLogService()
    items = svc.list_exportactivitylogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/exportactivitylogs/{item_id}", response_model=Dict[str, Any])
def get_exportactivitylog_by_id(item_id: int):
    """Retrieve detailed record for ExportActivityLog by ID."""
    svc = ExportActivityLogService()
    item = svc.get_exportactivitylog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExportActivityLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/exportactivitylogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_exportactivitylog(payload: ExportActivityLogCreateSchema):
    """Create new ExportActivityLog instance in enterprise repository."""
    svc = ExportActivityLogService()
    try:
        item = svc.create_exportactivitylog(
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

@router.put("/exportactivitylogs/{item_id}", response_model=Dict[str, Any])
def update_exportactivitylog(item_id: int, payload: ExportActivityLogUpdateSchema):
    """Update existing ExportActivityLog record fields."""
    svc = ExportActivityLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_exportactivitylog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExportActivityLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/exportactivitylogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exportactivitylog(item_id: int, hard: bool = Query(False)):
    """Delete ExportActivityLog record (soft-delete by default)."""
    svc = ExportActivityLogService()
    ok = svc.delete_exportactivitylog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExportActivityLog with ID {item_id} not found")
    return None

@router.get("/exportactivitylogs/analytics/metrics", response_model=Dict[str, Any])
def get_exportactivitylog_metrics():
    """Calculate summary statistical KPIs for ExportActivityLog collection."""
    svc = ExportActivityLogService()
    return svc.calculate_aggregate_metrics()

# ==================== AdminActionLog Endpoints ====================
@router.get("/adminactionlogs", response_model=List[Dict[str, Any]])
def list_adminactionlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AdminActionLog records with pagination and filtering."""
    svc = AdminActionLogService()
    items = svc.list_adminactionlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/adminactionlogs/{item_id}", response_model=Dict[str, Any])
def get_adminactionlog_by_id(item_id: int):
    """Retrieve detailed record for AdminActionLog by ID."""
    svc = AdminActionLogService()
    item = svc.get_adminactionlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AdminActionLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/adminactionlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_adminactionlog(payload: AdminActionLogCreateSchema):
    """Create new AdminActionLog instance in enterprise repository."""
    svc = AdminActionLogService()
    try:
        item = svc.create_adminactionlog(
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

@router.put("/adminactionlogs/{item_id}", response_model=Dict[str, Any])
def update_adminactionlog(item_id: int, payload: AdminActionLogUpdateSchema):
    """Update existing AdminActionLog record fields."""
    svc = AdminActionLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_adminactionlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AdminActionLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/adminactionlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_adminactionlog(item_id: int, hard: bool = Query(False)):
    """Delete AdminActionLog record (soft-delete by default)."""
    svc = AdminActionLogService()
    ok = svc.delete_adminactionlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AdminActionLog with ID {item_id} not found")
    return None

@router.get("/adminactionlogs/analytics/metrics", response_model=Dict[str, Any])
def get_adminactionlog_metrics():
    """Calculate summary statistical KPIs for AdminActionLog collection."""
    svc = AdminActionLogService()
    return svc.calculate_aggregate_metrics()

# ==================== CertificationSignoff Endpoints ====================
@router.get("/certificationsignoffs", response_model=List[Dict[str, Any]])
def list_certificationsignoffs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CertificationSignoff records with pagination and filtering."""
    svc = CertificationSignoffService()
    items = svc.list_certificationsignoffs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/certificationsignoffs/{item_id}", response_model=Dict[str, Any])
def get_certificationsignoff_by_id(item_id: int):
    """Retrieve detailed record for CertificationSignoff by ID."""
    svc = CertificationSignoffService()
    item = svc.get_certificationsignoff_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CertificationSignoff with ID {item_id} not found")
    return item.to_dict()

@router.post("/certificationsignoffs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_certificationsignoff(payload: CertificationSignoffCreateSchema):
    """Create new CertificationSignoff instance in enterprise repository."""
    svc = CertificationSignoffService()
    try:
        item = svc.create_certificationsignoff(
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

@router.put("/certificationsignoffs/{item_id}", response_model=Dict[str, Any])
def update_certificationsignoff(item_id: int, payload: CertificationSignoffUpdateSchema):
    """Update existing CertificationSignoff record fields."""
    svc = CertificationSignoffService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_certificationsignoff(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CertificationSignoff with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/certificationsignoffs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_certificationsignoff(item_id: int, hard: bool = Query(False)):
    """Delete CertificationSignoff record (soft-delete by default)."""
    svc = CertificationSignoffService()
    ok = svc.delete_certificationsignoff(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CertificationSignoff with ID {item_id} not found")
    return None

@router.get("/certificationsignoffs/analytics/metrics", response_model=Dict[str, Any])
def get_certificationsignoff_metrics():
    """Calculate summary statistical KPIs for CertificationSignoff collection."""
    svc = CertificationSignoffService()
    return svc.calculate_aggregate_metrics()

# ==================== ComplianceExceptionWaiver Endpoints ====================
@router.get("/complianceexceptionwaivers", response_model=List[Dict[str, Any]])
def list_complianceexceptionwaivers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ComplianceExceptionWaiver records with pagination and filtering."""
    svc = ComplianceExceptionWaiverService()
    items = svc.list_complianceexceptionwaivers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/complianceexceptionwaivers/{item_id}", response_model=Dict[str, Any])
def get_complianceexceptionwaiver_by_id(item_id: int):
    """Retrieve detailed record for ComplianceExceptionWaiver by ID."""
    svc = ComplianceExceptionWaiverService()
    item = svc.get_complianceexceptionwaiver_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ComplianceExceptionWaiver with ID {item_id} not found")
    return item.to_dict()

@router.post("/complianceexceptionwaivers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_complianceexceptionwaiver(payload: ComplianceExceptionWaiverCreateSchema):
    """Create new ComplianceExceptionWaiver instance in enterprise repository."""
    svc = ComplianceExceptionWaiverService()
    try:
        item = svc.create_complianceexceptionwaiver(
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

@router.put("/complianceexceptionwaivers/{item_id}", response_model=Dict[str, Any])
def update_complianceexceptionwaiver(item_id: int, payload: ComplianceExceptionWaiverUpdateSchema):
    """Update existing ComplianceExceptionWaiver record fields."""
    svc = ComplianceExceptionWaiverService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_complianceexceptionwaiver(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ComplianceExceptionWaiver with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/complianceexceptionwaivers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_complianceexceptionwaiver(item_id: int, hard: bool = Query(False)):
    """Delete ComplianceExceptionWaiver record (soft-delete by default)."""
    svc = ComplianceExceptionWaiverService()
    ok = svc.delete_complianceexceptionwaiver(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ComplianceExceptionWaiver with ID {item_id} not found")
    return None

@router.get("/complianceexceptionwaivers/analytics/metrics", response_model=Dict[str, Any])
def get_complianceexceptionwaiver_metrics():
    """Calculate summary statistical KPIs for ComplianceExceptionWaiver collection."""
    svc = ComplianceExceptionWaiverService()
    return svc.calculate_aggregate_metrics()

