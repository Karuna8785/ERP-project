"""
Identity & Access Management (IAM / SSO) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    UserIdentityProfileService,
    DirectoryServiceGroupService,
    SSOIdentityProviderService,
    SAMLMetadataConfigService,
    SCIMProvisioningRuleService,
    MFATokenDeviceService,
    PasswordPolicyRuleService,
    SessionTokenRegistryService,
    RoleAssignmentScopeService,
    EmergencyAccountBreakGlassService,
    OAuthClientApplicationService,
    UserConsentRecordService,
    AccessReviewAttestationService,
    AuthenticationAuditLogService,
    SecurityKeyWebAuthnService,
    TenantDomainMappingService,
)
from .schemas import (
    UserIdentityProfileCreateSchema, UserIdentityProfileUpdateSchema, UserIdentityProfileResponseSchema,
    DirectoryServiceGroupCreateSchema, DirectoryServiceGroupUpdateSchema, DirectoryServiceGroupResponseSchema,
    SSOIdentityProviderCreateSchema, SSOIdentityProviderUpdateSchema, SSOIdentityProviderResponseSchema,
    SAMLMetadataConfigCreateSchema, SAMLMetadataConfigUpdateSchema, SAMLMetadataConfigResponseSchema,
    SCIMProvisioningRuleCreateSchema, SCIMProvisioningRuleUpdateSchema, SCIMProvisioningRuleResponseSchema,
    MFATokenDeviceCreateSchema, MFATokenDeviceUpdateSchema, MFATokenDeviceResponseSchema,
    PasswordPolicyRuleCreateSchema, PasswordPolicyRuleUpdateSchema, PasswordPolicyRuleResponseSchema,
    SessionTokenRegistryCreateSchema, SessionTokenRegistryUpdateSchema, SessionTokenRegistryResponseSchema,
    RoleAssignmentScopeCreateSchema, RoleAssignmentScopeUpdateSchema, RoleAssignmentScopeResponseSchema,
    EmergencyAccountBreakGlassCreateSchema, EmergencyAccountBreakGlassUpdateSchema, EmergencyAccountBreakGlassResponseSchema,
    OAuthClientApplicationCreateSchema, OAuthClientApplicationUpdateSchema, OAuthClientApplicationResponseSchema,
    UserConsentRecordCreateSchema, UserConsentRecordUpdateSchema, UserConsentRecordResponseSchema,
    AccessReviewAttestationCreateSchema, AccessReviewAttestationUpdateSchema, AccessReviewAttestationResponseSchema,
    AuthenticationAuditLogCreateSchema, AuthenticationAuditLogUpdateSchema, AuthenticationAuditLogResponseSchema,
    SecurityKeyWebAuthnCreateSchema, SecurityKeyWebAuthnUpdateSchema, SecurityKeyWebAuthnResponseSchema,
    TenantDomainMappingCreateSchema, TenantDomainMappingUpdateSchema, TenantDomainMappingResponseSchema,
)

router = APIRouter(prefix="/identity_access", tags=["Identity & Access Management (IAM / SSO)"])

# ==================== UserIdentityProfile Endpoints ====================
@router.get("/useridentityprofiles", response_model=List[Dict[str, Any]])
def list_useridentityprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UserIdentityProfile records with pagination and filtering."""
    svc = UserIdentityProfileService()
    items = svc.list_useridentityprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/useridentityprofiles/{item_id}", response_model=Dict[str, Any])
def get_useridentityprofile_by_id(item_id: int):
    """Retrieve detailed record for UserIdentityProfile by ID."""
    svc = UserIdentityProfileService()
    item = svc.get_useridentityprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UserIdentityProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/useridentityprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_useridentityprofile(payload: UserIdentityProfileCreateSchema):
    """Create new UserIdentityProfile instance in enterprise repository."""
    svc = UserIdentityProfileService()
    try:
        item = svc.create_useridentityprofile(
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

@router.put("/useridentityprofiles/{item_id}", response_model=Dict[str, Any])
def update_useridentityprofile(item_id: int, payload: UserIdentityProfileUpdateSchema):
    """Update existing UserIdentityProfile record fields."""
    svc = UserIdentityProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_useridentityprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UserIdentityProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/useridentityprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_useridentityprofile(item_id: int, hard: bool = Query(False)):
    """Delete UserIdentityProfile record (soft-delete by default)."""
    svc = UserIdentityProfileService()
    ok = svc.delete_useridentityprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UserIdentityProfile with ID {item_id} not found")
    return None

@router.get("/useridentityprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_useridentityprofile_metrics():
    """Calculate summary statistical KPIs for UserIdentityProfile collection."""
    svc = UserIdentityProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== DirectoryServiceGroup Endpoints ====================
@router.get("/directoryservicegroups", response_model=List[Dict[str, Any]])
def list_directoryservicegroups(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DirectoryServiceGroup records with pagination and filtering."""
    svc = DirectoryServiceGroupService()
    items = svc.list_directoryservicegroups(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/directoryservicegroups/{item_id}", response_model=Dict[str, Any])
def get_directoryservicegroup_by_id(item_id: int):
    """Retrieve detailed record for DirectoryServiceGroup by ID."""
    svc = DirectoryServiceGroupService()
    item = svc.get_directoryservicegroup_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DirectoryServiceGroup with ID {item_id} not found")
    return item.to_dict()

@router.post("/directoryservicegroups", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_directoryservicegroup(payload: DirectoryServiceGroupCreateSchema):
    """Create new DirectoryServiceGroup instance in enterprise repository."""
    svc = DirectoryServiceGroupService()
    try:
        item = svc.create_directoryservicegroup(
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

@router.put("/directoryservicegroups/{item_id}", response_model=Dict[str, Any])
def update_directoryservicegroup(item_id: int, payload: DirectoryServiceGroupUpdateSchema):
    """Update existing DirectoryServiceGroup record fields."""
    svc = DirectoryServiceGroupService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_directoryservicegroup(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DirectoryServiceGroup with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/directoryservicegroups/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_directoryservicegroup(item_id: int, hard: bool = Query(False)):
    """Delete DirectoryServiceGroup record (soft-delete by default)."""
    svc = DirectoryServiceGroupService()
    ok = svc.delete_directoryservicegroup(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DirectoryServiceGroup with ID {item_id} not found")
    return None

@router.get("/directoryservicegroups/analytics/metrics", response_model=Dict[str, Any])
def get_directoryservicegroup_metrics():
    """Calculate summary statistical KPIs for DirectoryServiceGroup collection."""
    svc = DirectoryServiceGroupService()
    return svc.calculate_aggregate_metrics()

# ==================== SSOIdentityProvider Endpoints ====================
@router.get("/ssoidentityproviders", response_model=List[Dict[str, Any]])
def list_ssoidentityproviders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SSOIdentityProvider records with pagination and filtering."""
    svc = SSOIdentityProviderService()
    items = svc.list_ssoidentityproviders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ssoidentityproviders/{item_id}", response_model=Dict[str, Any])
def get_ssoidentityprovider_by_id(item_id: int):
    """Retrieve detailed record for SSOIdentityProvider by ID."""
    svc = SSOIdentityProviderService()
    item = svc.get_ssoidentityprovider_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SSOIdentityProvider with ID {item_id} not found")
    return item.to_dict()

@router.post("/ssoidentityproviders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ssoidentityprovider(payload: SSOIdentityProviderCreateSchema):
    """Create new SSOIdentityProvider instance in enterprise repository."""
    svc = SSOIdentityProviderService()
    try:
        item = svc.create_ssoidentityprovider(
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

@router.put("/ssoidentityproviders/{item_id}", response_model=Dict[str, Any])
def update_ssoidentityprovider(item_id: int, payload: SSOIdentityProviderUpdateSchema):
    """Update existing SSOIdentityProvider record fields."""
    svc = SSOIdentityProviderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ssoidentityprovider(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SSOIdentityProvider with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ssoidentityproviders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ssoidentityprovider(item_id: int, hard: bool = Query(False)):
    """Delete SSOIdentityProvider record (soft-delete by default)."""
    svc = SSOIdentityProviderService()
    ok = svc.delete_ssoidentityprovider(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SSOIdentityProvider with ID {item_id} not found")
    return None

@router.get("/ssoidentityproviders/analytics/metrics", response_model=Dict[str, Any])
def get_ssoidentityprovider_metrics():
    """Calculate summary statistical KPIs for SSOIdentityProvider collection."""
    svc = SSOIdentityProviderService()
    return svc.calculate_aggregate_metrics()

# ==================== SAMLMetadataConfig Endpoints ====================
@router.get("/samlmetadataconfigs", response_model=List[Dict[str, Any]])
def list_samlmetadataconfigs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SAMLMetadataConfig records with pagination and filtering."""
    svc = SAMLMetadataConfigService()
    items = svc.list_samlmetadataconfigs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/samlmetadataconfigs/{item_id}", response_model=Dict[str, Any])
def get_samlmetadataconfig_by_id(item_id: int):
    """Retrieve detailed record for SAMLMetadataConfig by ID."""
    svc = SAMLMetadataConfigService()
    item = svc.get_samlmetadataconfig_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SAMLMetadataConfig with ID {item_id} not found")
    return item.to_dict()

@router.post("/samlmetadataconfigs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_samlmetadataconfig(payload: SAMLMetadataConfigCreateSchema):
    """Create new SAMLMetadataConfig instance in enterprise repository."""
    svc = SAMLMetadataConfigService()
    try:
        item = svc.create_samlmetadataconfig(
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

@router.put("/samlmetadataconfigs/{item_id}", response_model=Dict[str, Any])
def update_samlmetadataconfig(item_id: int, payload: SAMLMetadataConfigUpdateSchema):
    """Update existing SAMLMetadataConfig record fields."""
    svc = SAMLMetadataConfigService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_samlmetadataconfig(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SAMLMetadataConfig with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/samlmetadataconfigs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_samlmetadataconfig(item_id: int, hard: bool = Query(False)):
    """Delete SAMLMetadataConfig record (soft-delete by default)."""
    svc = SAMLMetadataConfigService()
    ok = svc.delete_samlmetadataconfig(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SAMLMetadataConfig with ID {item_id} not found")
    return None

@router.get("/samlmetadataconfigs/analytics/metrics", response_model=Dict[str, Any])
def get_samlmetadataconfig_metrics():
    """Calculate summary statistical KPIs for SAMLMetadataConfig collection."""
    svc = SAMLMetadataConfigService()
    return svc.calculate_aggregate_metrics()

# ==================== SCIMProvisioningRule Endpoints ====================
@router.get("/scimprovisioningrules", response_model=List[Dict[str, Any]])
def list_scimprovisioningrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SCIMProvisioningRule records with pagination and filtering."""
    svc = SCIMProvisioningRuleService()
    items = svc.list_scimprovisioningrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/scimprovisioningrules/{item_id}", response_model=Dict[str, Any])
def get_scimprovisioningrule_by_id(item_id: int):
    """Retrieve detailed record for SCIMProvisioningRule by ID."""
    svc = SCIMProvisioningRuleService()
    item = svc.get_scimprovisioningrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SCIMProvisioningRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/scimprovisioningrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_scimprovisioningrule(payload: SCIMProvisioningRuleCreateSchema):
    """Create new SCIMProvisioningRule instance in enterprise repository."""
    svc = SCIMProvisioningRuleService()
    try:
        item = svc.create_scimprovisioningrule(
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

@router.put("/scimprovisioningrules/{item_id}", response_model=Dict[str, Any])
def update_scimprovisioningrule(item_id: int, payload: SCIMProvisioningRuleUpdateSchema):
    """Update existing SCIMProvisioningRule record fields."""
    svc = SCIMProvisioningRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_scimprovisioningrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SCIMProvisioningRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/scimprovisioningrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scimprovisioningrule(item_id: int, hard: bool = Query(False)):
    """Delete SCIMProvisioningRule record (soft-delete by default)."""
    svc = SCIMProvisioningRuleService()
    ok = svc.delete_scimprovisioningrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SCIMProvisioningRule with ID {item_id} not found")
    return None

@router.get("/scimprovisioningrules/analytics/metrics", response_model=Dict[str, Any])
def get_scimprovisioningrule_metrics():
    """Calculate summary statistical KPIs for SCIMProvisioningRule collection."""
    svc = SCIMProvisioningRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== MFATokenDevice Endpoints ====================
@router.get("/mfatokendevices", response_model=List[Dict[str, Any]])
def list_mfatokendevices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MFATokenDevice records with pagination and filtering."""
    svc = MFATokenDeviceService()
    items = svc.list_mfatokendevices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/mfatokendevices/{item_id}", response_model=Dict[str, Any])
def get_mfatokendevice_by_id(item_id: int):
    """Retrieve detailed record for MFATokenDevice by ID."""
    svc = MFATokenDeviceService()
    item = svc.get_mfatokendevice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MFATokenDevice with ID {item_id} not found")
    return item.to_dict()

@router.post("/mfatokendevices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_mfatokendevice(payload: MFATokenDeviceCreateSchema):
    """Create new MFATokenDevice instance in enterprise repository."""
    svc = MFATokenDeviceService()
    try:
        item = svc.create_mfatokendevice(
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

@router.put("/mfatokendevices/{item_id}", response_model=Dict[str, Any])
def update_mfatokendevice(item_id: int, payload: MFATokenDeviceUpdateSchema):
    """Update existing MFATokenDevice record fields."""
    svc = MFATokenDeviceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_mfatokendevice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MFATokenDevice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/mfatokendevices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mfatokendevice(item_id: int, hard: bool = Query(False)):
    """Delete MFATokenDevice record (soft-delete by default)."""
    svc = MFATokenDeviceService()
    ok = svc.delete_mfatokendevice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MFATokenDevice with ID {item_id} not found")
    return None

@router.get("/mfatokendevices/analytics/metrics", response_model=Dict[str, Any])
def get_mfatokendevice_metrics():
    """Calculate summary statistical KPIs for MFATokenDevice collection."""
    svc = MFATokenDeviceService()
    return svc.calculate_aggregate_metrics()

# ==================== PasswordPolicyRule Endpoints ====================
@router.get("/passwordpolicyrules", response_model=List[Dict[str, Any]])
def list_passwordpolicyrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PasswordPolicyRule records with pagination and filtering."""
    svc = PasswordPolicyRuleService()
    items = svc.list_passwordpolicyrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/passwordpolicyrules/{item_id}", response_model=Dict[str, Any])
def get_passwordpolicyrule_by_id(item_id: int):
    """Retrieve detailed record for PasswordPolicyRule by ID."""
    svc = PasswordPolicyRuleService()
    item = svc.get_passwordpolicyrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PasswordPolicyRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/passwordpolicyrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_passwordpolicyrule(payload: PasswordPolicyRuleCreateSchema):
    """Create new PasswordPolicyRule instance in enterprise repository."""
    svc = PasswordPolicyRuleService()
    try:
        item = svc.create_passwordpolicyrule(
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

@router.put("/passwordpolicyrules/{item_id}", response_model=Dict[str, Any])
def update_passwordpolicyrule(item_id: int, payload: PasswordPolicyRuleUpdateSchema):
    """Update existing PasswordPolicyRule record fields."""
    svc = PasswordPolicyRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_passwordpolicyrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PasswordPolicyRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/passwordpolicyrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_passwordpolicyrule(item_id: int, hard: bool = Query(False)):
    """Delete PasswordPolicyRule record (soft-delete by default)."""
    svc = PasswordPolicyRuleService()
    ok = svc.delete_passwordpolicyrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PasswordPolicyRule with ID {item_id} not found")
    return None

@router.get("/passwordpolicyrules/analytics/metrics", response_model=Dict[str, Any])
def get_passwordpolicyrule_metrics():
    """Calculate summary statistical KPIs for PasswordPolicyRule collection."""
    svc = PasswordPolicyRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== SessionTokenRegistry Endpoints ====================
@router.get("/sessiontokenregistrys", response_model=List[Dict[str, Any]])
def list_sessiontokenregistrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SessionTokenRegistry records with pagination and filtering."""
    svc = SessionTokenRegistryService()
    items = svc.list_sessiontokenregistrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sessiontokenregistrys/{item_id}", response_model=Dict[str, Any])
def get_sessiontokenregistry_by_id(item_id: int):
    """Retrieve detailed record for SessionTokenRegistry by ID."""
    svc = SessionTokenRegistryService()
    item = svc.get_sessiontokenregistry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SessionTokenRegistry with ID {item_id} not found")
    return item.to_dict()

@router.post("/sessiontokenregistrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sessiontokenregistry(payload: SessionTokenRegistryCreateSchema):
    """Create new SessionTokenRegistry instance in enterprise repository."""
    svc = SessionTokenRegistryService()
    try:
        item = svc.create_sessiontokenregistry(
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

@router.put("/sessiontokenregistrys/{item_id}", response_model=Dict[str, Any])
def update_sessiontokenregistry(item_id: int, payload: SessionTokenRegistryUpdateSchema):
    """Update existing SessionTokenRegistry record fields."""
    svc = SessionTokenRegistryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sessiontokenregistry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SessionTokenRegistry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sessiontokenregistrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sessiontokenregistry(item_id: int, hard: bool = Query(False)):
    """Delete SessionTokenRegistry record (soft-delete by default)."""
    svc = SessionTokenRegistryService()
    ok = svc.delete_sessiontokenregistry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SessionTokenRegistry with ID {item_id} not found")
    return None

@router.get("/sessiontokenregistrys/analytics/metrics", response_model=Dict[str, Any])
def get_sessiontokenregistry_metrics():
    """Calculate summary statistical KPIs for SessionTokenRegistry collection."""
    svc = SessionTokenRegistryService()
    return svc.calculate_aggregate_metrics()

# ==================== RoleAssignmentScope Endpoints ====================
@router.get("/roleassignmentscopes", response_model=List[Dict[str, Any]])
def list_roleassignmentscopes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RoleAssignmentScope records with pagination and filtering."""
    svc = RoleAssignmentScopeService()
    items = svc.list_roleassignmentscopes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/roleassignmentscopes/{item_id}", response_model=Dict[str, Any])
def get_roleassignmentscope_by_id(item_id: int):
    """Retrieve detailed record for RoleAssignmentScope by ID."""
    svc = RoleAssignmentScopeService()
    item = svc.get_roleassignmentscope_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RoleAssignmentScope with ID {item_id} not found")
    return item.to_dict()

@router.post("/roleassignmentscopes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_roleassignmentscope(payload: RoleAssignmentScopeCreateSchema):
    """Create new RoleAssignmentScope instance in enterprise repository."""
    svc = RoleAssignmentScopeService()
    try:
        item = svc.create_roleassignmentscope(
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

@router.put("/roleassignmentscopes/{item_id}", response_model=Dict[str, Any])
def update_roleassignmentscope(item_id: int, payload: RoleAssignmentScopeUpdateSchema):
    """Update existing RoleAssignmentScope record fields."""
    svc = RoleAssignmentScopeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_roleassignmentscope(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RoleAssignmentScope with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/roleassignmentscopes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_roleassignmentscope(item_id: int, hard: bool = Query(False)):
    """Delete RoleAssignmentScope record (soft-delete by default)."""
    svc = RoleAssignmentScopeService()
    ok = svc.delete_roleassignmentscope(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RoleAssignmentScope with ID {item_id} not found")
    return None

@router.get("/roleassignmentscopes/analytics/metrics", response_model=Dict[str, Any])
def get_roleassignmentscope_metrics():
    """Calculate summary statistical KPIs for RoleAssignmentScope collection."""
    svc = RoleAssignmentScopeService()
    return svc.calculate_aggregate_metrics()

# ==================== EmergencyAccountBreakGlass Endpoints ====================
@router.get("/emergencyaccountbreakglasss", response_model=List[Dict[str, Any]])
def list_emergencyaccountbreakglasss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmergencyAccountBreakGlass records with pagination and filtering."""
    svc = EmergencyAccountBreakGlassService()
    items = svc.list_emergencyaccountbreakglasss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/emergencyaccountbreakglasss/{item_id}", response_model=Dict[str, Any])
def get_emergencyaccountbreakglass_by_id(item_id: int):
    """Retrieve detailed record for EmergencyAccountBreakGlass by ID."""
    svc = EmergencyAccountBreakGlassService()
    item = svc.get_emergencyaccountbreakglass_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmergencyAccountBreakGlass with ID {item_id} not found")
    return item.to_dict()

@router.post("/emergencyaccountbreakglasss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_emergencyaccountbreakglass(payload: EmergencyAccountBreakGlassCreateSchema):
    """Create new EmergencyAccountBreakGlass instance in enterprise repository."""
    svc = EmergencyAccountBreakGlassService()
    try:
        item = svc.create_emergencyaccountbreakglass(
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

@router.put("/emergencyaccountbreakglasss/{item_id}", response_model=Dict[str, Any])
def update_emergencyaccountbreakglass(item_id: int, payload: EmergencyAccountBreakGlassUpdateSchema):
    """Update existing EmergencyAccountBreakGlass record fields."""
    svc = EmergencyAccountBreakGlassService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_emergencyaccountbreakglass(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmergencyAccountBreakGlass with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/emergencyaccountbreakglasss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_emergencyaccountbreakglass(item_id: int, hard: bool = Query(False)):
    """Delete EmergencyAccountBreakGlass record (soft-delete by default)."""
    svc = EmergencyAccountBreakGlassService()
    ok = svc.delete_emergencyaccountbreakglass(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmergencyAccountBreakGlass with ID {item_id} not found")
    return None

@router.get("/emergencyaccountbreakglasss/analytics/metrics", response_model=Dict[str, Any])
def get_emergencyaccountbreakglass_metrics():
    """Calculate summary statistical KPIs for EmergencyAccountBreakGlass collection."""
    svc = EmergencyAccountBreakGlassService()
    return svc.calculate_aggregate_metrics()

# ==================== OAuthClientApplication Endpoints ====================
@router.get("/oauthclientapplications", response_model=List[Dict[str, Any]])
def list_oauthclientapplications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OAuthClientApplication records with pagination and filtering."""
    svc = OAuthClientApplicationService()
    items = svc.list_oauthclientapplications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/oauthclientapplications/{item_id}", response_model=Dict[str, Any])
def get_oauthclientapplication_by_id(item_id: int):
    """Retrieve detailed record for OAuthClientApplication by ID."""
    svc = OAuthClientApplicationService()
    item = svc.get_oauthclientapplication_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OAuthClientApplication with ID {item_id} not found")
    return item.to_dict()

@router.post("/oauthclientapplications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_oauthclientapplication(payload: OAuthClientApplicationCreateSchema):
    """Create new OAuthClientApplication instance in enterprise repository."""
    svc = OAuthClientApplicationService()
    try:
        item = svc.create_oauthclientapplication(
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

@router.put("/oauthclientapplications/{item_id}", response_model=Dict[str, Any])
def update_oauthclientapplication(item_id: int, payload: OAuthClientApplicationUpdateSchema):
    """Update existing OAuthClientApplication record fields."""
    svc = OAuthClientApplicationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_oauthclientapplication(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OAuthClientApplication with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/oauthclientapplications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_oauthclientapplication(item_id: int, hard: bool = Query(False)):
    """Delete OAuthClientApplication record (soft-delete by default)."""
    svc = OAuthClientApplicationService()
    ok = svc.delete_oauthclientapplication(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OAuthClientApplication with ID {item_id} not found")
    return None

@router.get("/oauthclientapplications/analytics/metrics", response_model=Dict[str, Any])
def get_oauthclientapplication_metrics():
    """Calculate summary statistical KPIs for OAuthClientApplication collection."""
    svc = OAuthClientApplicationService()
    return svc.calculate_aggregate_metrics()

# ==================== UserConsentRecord Endpoints ====================
@router.get("/userconsentrecords", response_model=List[Dict[str, Any]])
def list_userconsentrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UserConsentRecord records with pagination and filtering."""
    svc = UserConsentRecordService()
    items = svc.list_userconsentrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/userconsentrecords/{item_id}", response_model=Dict[str, Any])
def get_userconsentrecord_by_id(item_id: int):
    """Retrieve detailed record for UserConsentRecord by ID."""
    svc = UserConsentRecordService()
    item = svc.get_userconsentrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UserConsentRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/userconsentrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_userconsentrecord(payload: UserConsentRecordCreateSchema):
    """Create new UserConsentRecord instance in enterprise repository."""
    svc = UserConsentRecordService()
    try:
        item = svc.create_userconsentrecord(
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

@router.put("/userconsentrecords/{item_id}", response_model=Dict[str, Any])
def update_userconsentrecord(item_id: int, payload: UserConsentRecordUpdateSchema):
    """Update existing UserConsentRecord record fields."""
    svc = UserConsentRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_userconsentrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UserConsentRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/userconsentrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_userconsentrecord(item_id: int, hard: bool = Query(False)):
    """Delete UserConsentRecord record (soft-delete by default)."""
    svc = UserConsentRecordService()
    ok = svc.delete_userconsentrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UserConsentRecord with ID {item_id} not found")
    return None

@router.get("/userconsentrecords/analytics/metrics", response_model=Dict[str, Any])
def get_userconsentrecord_metrics():
    """Calculate summary statistical KPIs for UserConsentRecord collection."""
    svc = UserConsentRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== AccessReviewAttestation Endpoints ====================
@router.get("/accessreviewattestations", response_model=List[Dict[str, Any]])
def list_accessreviewattestations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AccessReviewAttestation records with pagination and filtering."""
    svc = AccessReviewAttestationService()
    items = svc.list_accessreviewattestations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/accessreviewattestations/{item_id}", response_model=Dict[str, Any])
def get_accessreviewattestation_by_id(item_id: int):
    """Retrieve detailed record for AccessReviewAttestation by ID."""
    svc = AccessReviewAttestationService()
    item = svc.get_accessreviewattestation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AccessReviewAttestation with ID {item_id} not found")
    return item.to_dict()

@router.post("/accessreviewattestations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_accessreviewattestation(payload: AccessReviewAttestationCreateSchema):
    """Create new AccessReviewAttestation instance in enterprise repository."""
    svc = AccessReviewAttestationService()
    try:
        item = svc.create_accessreviewattestation(
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

@router.put("/accessreviewattestations/{item_id}", response_model=Dict[str, Any])
def update_accessreviewattestation(item_id: int, payload: AccessReviewAttestationUpdateSchema):
    """Update existing AccessReviewAttestation record fields."""
    svc = AccessReviewAttestationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_accessreviewattestation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AccessReviewAttestation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/accessreviewattestations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accessreviewattestation(item_id: int, hard: bool = Query(False)):
    """Delete AccessReviewAttestation record (soft-delete by default)."""
    svc = AccessReviewAttestationService()
    ok = svc.delete_accessreviewattestation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AccessReviewAttestation with ID {item_id} not found")
    return None

@router.get("/accessreviewattestations/analytics/metrics", response_model=Dict[str, Any])
def get_accessreviewattestation_metrics():
    """Calculate summary statistical KPIs for AccessReviewAttestation collection."""
    svc = AccessReviewAttestationService()
    return svc.calculate_aggregate_metrics()

# ==================== AuthenticationAuditLog Endpoints ====================
@router.get("/authenticationauditlogs", response_model=List[Dict[str, Any]])
def list_authenticationauditlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AuthenticationAuditLog records with pagination and filtering."""
    svc = AuthenticationAuditLogService()
    items = svc.list_authenticationauditlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/authenticationauditlogs/{item_id}", response_model=Dict[str, Any])
def get_authenticationauditlog_by_id(item_id: int):
    """Retrieve detailed record for AuthenticationAuditLog by ID."""
    svc = AuthenticationAuditLogService()
    item = svc.get_authenticationauditlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AuthenticationAuditLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/authenticationauditlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_authenticationauditlog(payload: AuthenticationAuditLogCreateSchema):
    """Create new AuthenticationAuditLog instance in enterprise repository."""
    svc = AuthenticationAuditLogService()
    try:
        item = svc.create_authenticationauditlog(
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

@router.put("/authenticationauditlogs/{item_id}", response_model=Dict[str, Any])
def update_authenticationauditlog(item_id: int, payload: AuthenticationAuditLogUpdateSchema):
    """Update existing AuthenticationAuditLog record fields."""
    svc = AuthenticationAuditLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_authenticationauditlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AuthenticationAuditLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/authenticationauditlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_authenticationauditlog(item_id: int, hard: bool = Query(False)):
    """Delete AuthenticationAuditLog record (soft-delete by default)."""
    svc = AuthenticationAuditLogService()
    ok = svc.delete_authenticationauditlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AuthenticationAuditLog with ID {item_id} not found")
    return None

@router.get("/authenticationauditlogs/analytics/metrics", response_model=Dict[str, Any])
def get_authenticationauditlog_metrics():
    """Calculate summary statistical KPIs for AuthenticationAuditLog collection."""
    svc = AuthenticationAuditLogService()
    return svc.calculate_aggregate_metrics()

# ==================== SecurityKeyWebAuthn Endpoints ====================
@router.get("/securitykeywebauthns", response_model=List[Dict[str, Any]])
def list_securitykeywebauthns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SecurityKeyWebAuthn records with pagination and filtering."""
    svc = SecurityKeyWebAuthnService()
    items = svc.list_securitykeywebauthns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/securitykeywebauthns/{item_id}", response_model=Dict[str, Any])
def get_securitykeywebauthn_by_id(item_id: int):
    """Retrieve detailed record for SecurityKeyWebAuthn by ID."""
    svc = SecurityKeyWebAuthnService()
    item = svc.get_securitykeywebauthn_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SecurityKeyWebAuthn with ID {item_id} not found")
    return item.to_dict()

@router.post("/securitykeywebauthns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_securitykeywebauthn(payload: SecurityKeyWebAuthnCreateSchema):
    """Create new SecurityKeyWebAuthn instance in enterprise repository."""
    svc = SecurityKeyWebAuthnService()
    try:
        item = svc.create_securitykeywebauthn(
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

@router.put("/securitykeywebauthns/{item_id}", response_model=Dict[str, Any])
def update_securitykeywebauthn(item_id: int, payload: SecurityKeyWebAuthnUpdateSchema):
    """Update existing SecurityKeyWebAuthn record fields."""
    svc = SecurityKeyWebAuthnService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_securitykeywebauthn(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SecurityKeyWebAuthn with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/securitykeywebauthns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_securitykeywebauthn(item_id: int, hard: bool = Query(False)):
    """Delete SecurityKeyWebAuthn record (soft-delete by default)."""
    svc = SecurityKeyWebAuthnService()
    ok = svc.delete_securitykeywebauthn(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SecurityKeyWebAuthn with ID {item_id} not found")
    return None

@router.get("/securitykeywebauthns/analytics/metrics", response_model=Dict[str, Any])
def get_securitykeywebauthn_metrics():
    """Calculate summary statistical KPIs for SecurityKeyWebAuthn collection."""
    svc = SecurityKeyWebAuthnService()
    return svc.calculate_aggregate_metrics()

# ==================== TenantDomainMapping Endpoints ====================
@router.get("/tenantdomainmappings", response_model=List[Dict[str, Any]])
def list_tenantdomainmappings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TenantDomainMapping records with pagination and filtering."""
    svc = TenantDomainMappingService()
    items = svc.list_tenantdomainmappings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tenantdomainmappings/{item_id}", response_model=Dict[str, Any])
def get_tenantdomainmapping_by_id(item_id: int):
    """Retrieve detailed record for TenantDomainMapping by ID."""
    svc = TenantDomainMappingService()
    item = svc.get_tenantdomainmapping_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TenantDomainMapping with ID {item_id} not found")
    return item.to_dict()

@router.post("/tenantdomainmappings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tenantdomainmapping(payload: TenantDomainMappingCreateSchema):
    """Create new TenantDomainMapping instance in enterprise repository."""
    svc = TenantDomainMappingService()
    try:
        item = svc.create_tenantdomainmapping(
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

@router.put("/tenantdomainmappings/{item_id}", response_model=Dict[str, Any])
def update_tenantdomainmapping(item_id: int, payload: TenantDomainMappingUpdateSchema):
    """Update existing TenantDomainMapping record fields."""
    svc = TenantDomainMappingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tenantdomainmapping(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TenantDomainMapping with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tenantdomainmappings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tenantdomainmapping(item_id: int, hard: bool = Query(False)):
    """Delete TenantDomainMapping record (soft-delete by default)."""
    svc = TenantDomainMappingService()
    ok = svc.delete_tenantdomainmapping(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TenantDomainMapping with ID {item_id} not found")
    return None

@router.get("/tenantdomainmappings/analytics/metrics", response_model=Dict[str, Any])
def get_tenantdomainmapping_metrics():
    """Calculate summary statistical KPIs for TenantDomainMapping collection."""
    svc = TenantDomainMappingService()
    return svc.calculate_aggregate_metrics()

