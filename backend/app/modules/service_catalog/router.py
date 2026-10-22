"""
ITIL Service Catalog & Enterprise Requests - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ServiceCatalogItemService,
    ServiceCategoryGroupService,
    ServiceOrderRequestService,
    ApprovalHierarchyPathService,
    FulfillmentTaskStepService,
    SLACommitmentTargetService,
    HardwareProvisioningOrderService,
    SoftwareLicenseRequestService,
    CloudResourceQuotaService,
    EmployeeAccessRequestService,
    CostCenterChargebackService,
    ServiceDeskTicketLinkService,
    CatalogItemDependencyService,
    UserEntitlementRuleService,
    RequestSatisfactionScoreService,
    RecurringServiceOrderService,
)
from .schemas import (
    ServiceCatalogItemCreateSchema, ServiceCatalogItemUpdateSchema, ServiceCatalogItemResponseSchema,
    ServiceCategoryGroupCreateSchema, ServiceCategoryGroupUpdateSchema, ServiceCategoryGroupResponseSchema,
    ServiceOrderRequestCreateSchema, ServiceOrderRequestUpdateSchema, ServiceOrderRequestResponseSchema,
    ApprovalHierarchyPathCreateSchema, ApprovalHierarchyPathUpdateSchema, ApprovalHierarchyPathResponseSchema,
    FulfillmentTaskStepCreateSchema, FulfillmentTaskStepUpdateSchema, FulfillmentTaskStepResponseSchema,
    SLACommitmentTargetCreateSchema, SLACommitmentTargetUpdateSchema, SLACommitmentTargetResponseSchema,
    HardwareProvisioningOrderCreateSchema, HardwareProvisioningOrderUpdateSchema, HardwareProvisioningOrderResponseSchema,
    SoftwareLicenseRequestCreateSchema, SoftwareLicenseRequestUpdateSchema, SoftwareLicenseRequestResponseSchema,
    CloudResourceQuotaCreateSchema, CloudResourceQuotaUpdateSchema, CloudResourceQuotaResponseSchema,
    EmployeeAccessRequestCreateSchema, EmployeeAccessRequestUpdateSchema, EmployeeAccessRequestResponseSchema,
    CostCenterChargebackCreateSchema, CostCenterChargebackUpdateSchema, CostCenterChargebackResponseSchema,
    ServiceDeskTicketLinkCreateSchema, ServiceDeskTicketLinkUpdateSchema, ServiceDeskTicketLinkResponseSchema,
    CatalogItemDependencyCreateSchema, CatalogItemDependencyUpdateSchema, CatalogItemDependencyResponseSchema,
    UserEntitlementRuleCreateSchema, UserEntitlementRuleUpdateSchema, UserEntitlementRuleResponseSchema,
    RequestSatisfactionScoreCreateSchema, RequestSatisfactionScoreUpdateSchema, RequestSatisfactionScoreResponseSchema,
    RecurringServiceOrderCreateSchema, RecurringServiceOrderUpdateSchema, RecurringServiceOrderResponseSchema,
)

router = APIRouter(prefix="/service_catalog", tags=["ITIL Service Catalog & Enterprise Requests"])

# ==================== ServiceCatalogItem Endpoints ====================
@router.get("/servicecatalogitems", response_model=List[Dict[str, Any]])
def list_servicecatalogitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceCatalogItem records with pagination and filtering."""
    svc = ServiceCatalogItemService()
    items = svc.list_servicecatalogitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicecatalogitems/{item_id}", response_model=Dict[str, Any])
def get_servicecatalogitem_by_id(item_id: int):
    """Retrieve detailed record for ServiceCatalogItem by ID."""
    svc = ServiceCatalogItemService()
    item = svc.get_servicecatalogitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceCatalogItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicecatalogitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicecatalogitem(payload: ServiceCatalogItemCreateSchema):
    """Create new ServiceCatalogItem instance in enterprise repository."""
    svc = ServiceCatalogItemService()
    try:
        item = svc.create_servicecatalogitem(
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

@router.put("/servicecatalogitems/{item_id}", response_model=Dict[str, Any])
def update_servicecatalogitem(item_id: int, payload: ServiceCatalogItemUpdateSchema):
    """Update existing ServiceCatalogItem record fields."""
    svc = ServiceCatalogItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicecatalogitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceCatalogItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicecatalogitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicecatalogitem(item_id: int, hard: bool = Query(False)):
    """Delete ServiceCatalogItem record (soft-delete by default)."""
    svc = ServiceCatalogItemService()
    ok = svc.delete_servicecatalogitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceCatalogItem with ID {item_id} not found")
    return None

@router.get("/servicecatalogitems/analytics/metrics", response_model=Dict[str, Any])
def get_servicecatalogitem_metrics():
    """Calculate summary statistical KPIs for ServiceCatalogItem collection."""
    svc = ServiceCatalogItemService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceCategoryGroup Endpoints ====================
@router.get("/servicecategorygroups", response_model=List[Dict[str, Any]])
def list_servicecategorygroups(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceCategoryGroup records with pagination and filtering."""
    svc = ServiceCategoryGroupService()
    items = svc.list_servicecategorygroups(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicecategorygroups/{item_id}", response_model=Dict[str, Any])
def get_servicecategorygroup_by_id(item_id: int):
    """Retrieve detailed record for ServiceCategoryGroup by ID."""
    svc = ServiceCategoryGroupService()
    item = svc.get_servicecategorygroup_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceCategoryGroup with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicecategorygroups", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicecategorygroup(payload: ServiceCategoryGroupCreateSchema):
    """Create new ServiceCategoryGroup instance in enterprise repository."""
    svc = ServiceCategoryGroupService()
    try:
        item = svc.create_servicecategorygroup(
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

@router.put("/servicecategorygroups/{item_id}", response_model=Dict[str, Any])
def update_servicecategorygroup(item_id: int, payload: ServiceCategoryGroupUpdateSchema):
    """Update existing ServiceCategoryGroup record fields."""
    svc = ServiceCategoryGroupService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicecategorygroup(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceCategoryGroup with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicecategorygroups/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicecategorygroup(item_id: int, hard: bool = Query(False)):
    """Delete ServiceCategoryGroup record (soft-delete by default)."""
    svc = ServiceCategoryGroupService()
    ok = svc.delete_servicecategorygroup(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceCategoryGroup with ID {item_id} not found")
    return None

@router.get("/servicecategorygroups/analytics/metrics", response_model=Dict[str, Any])
def get_servicecategorygroup_metrics():
    """Calculate summary statistical KPIs for ServiceCategoryGroup collection."""
    svc = ServiceCategoryGroupService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceOrderRequest Endpoints ====================
@router.get("/serviceorderrequests", response_model=List[Dict[str, Any]])
def list_serviceorderrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceOrderRequest records with pagination and filtering."""
    svc = ServiceOrderRequestService()
    items = svc.list_serviceorderrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/serviceorderrequests/{item_id}", response_model=Dict[str, Any])
def get_serviceorderrequest_by_id(item_id: int):
    """Retrieve detailed record for ServiceOrderRequest by ID."""
    svc = ServiceOrderRequestService()
    item = svc.get_serviceorderrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceOrderRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/serviceorderrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_serviceorderrequest(payload: ServiceOrderRequestCreateSchema):
    """Create new ServiceOrderRequest instance in enterprise repository."""
    svc = ServiceOrderRequestService()
    try:
        item = svc.create_serviceorderrequest(
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

@router.put("/serviceorderrequests/{item_id}", response_model=Dict[str, Any])
def update_serviceorderrequest(item_id: int, payload: ServiceOrderRequestUpdateSchema):
    """Update existing ServiceOrderRequest record fields."""
    svc = ServiceOrderRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_serviceorderrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceOrderRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/serviceorderrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_serviceorderrequest(item_id: int, hard: bool = Query(False)):
    """Delete ServiceOrderRequest record (soft-delete by default)."""
    svc = ServiceOrderRequestService()
    ok = svc.delete_serviceorderrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceOrderRequest with ID {item_id} not found")
    return None

@router.get("/serviceorderrequests/analytics/metrics", response_model=Dict[str, Any])
def get_serviceorderrequest_metrics():
    """Calculate summary statistical KPIs for ServiceOrderRequest collection."""
    svc = ServiceOrderRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== ApprovalHierarchyPath Endpoints ====================
@router.get("/approvalhierarchypaths", response_model=List[Dict[str, Any]])
def list_approvalhierarchypaths(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ApprovalHierarchyPath records with pagination and filtering."""
    svc = ApprovalHierarchyPathService()
    items = svc.list_approvalhierarchypaths(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/approvalhierarchypaths/{item_id}", response_model=Dict[str, Any])
def get_approvalhierarchypath_by_id(item_id: int):
    """Retrieve detailed record for ApprovalHierarchyPath by ID."""
    svc = ApprovalHierarchyPathService()
    item = svc.get_approvalhierarchypath_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ApprovalHierarchyPath with ID {item_id} not found")
    return item.to_dict()

@router.post("/approvalhierarchypaths", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_approvalhierarchypath(payload: ApprovalHierarchyPathCreateSchema):
    """Create new ApprovalHierarchyPath instance in enterprise repository."""
    svc = ApprovalHierarchyPathService()
    try:
        item = svc.create_approvalhierarchypath(
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

@router.put("/approvalhierarchypaths/{item_id}", response_model=Dict[str, Any])
def update_approvalhierarchypath(item_id: int, payload: ApprovalHierarchyPathUpdateSchema):
    """Update existing ApprovalHierarchyPath record fields."""
    svc = ApprovalHierarchyPathService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_approvalhierarchypath(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ApprovalHierarchyPath with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/approvalhierarchypaths/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_approvalhierarchypath(item_id: int, hard: bool = Query(False)):
    """Delete ApprovalHierarchyPath record (soft-delete by default)."""
    svc = ApprovalHierarchyPathService()
    ok = svc.delete_approvalhierarchypath(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ApprovalHierarchyPath with ID {item_id} not found")
    return None

@router.get("/approvalhierarchypaths/analytics/metrics", response_model=Dict[str, Any])
def get_approvalhierarchypath_metrics():
    """Calculate summary statistical KPIs for ApprovalHierarchyPath collection."""
    svc = ApprovalHierarchyPathService()
    return svc.calculate_aggregate_metrics()

# ==================== FulfillmentTaskStep Endpoints ====================
@router.get("/fulfillmenttasksteps", response_model=List[Dict[str, Any]])
def list_fulfillmenttasksteps(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FulfillmentTaskStep records with pagination and filtering."""
    svc = FulfillmentTaskStepService()
    items = svc.list_fulfillmenttasksteps(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fulfillmenttasksteps/{item_id}", response_model=Dict[str, Any])
def get_fulfillmenttaskstep_by_id(item_id: int):
    """Retrieve detailed record for FulfillmentTaskStep by ID."""
    svc = FulfillmentTaskStepService()
    item = svc.get_fulfillmenttaskstep_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FulfillmentTaskStep with ID {item_id} not found")
    return item.to_dict()

@router.post("/fulfillmenttasksteps", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fulfillmenttaskstep(payload: FulfillmentTaskStepCreateSchema):
    """Create new FulfillmentTaskStep instance in enterprise repository."""
    svc = FulfillmentTaskStepService()
    try:
        item = svc.create_fulfillmenttaskstep(
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

@router.put("/fulfillmenttasksteps/{item_id}", response_model=Dict[str, Any])
def update_fulfillmenttaskstep(item_id: int, payload: FulfillmentTaskStepUpdateSchema):
    """Update existing FulfillmentTaskStep record fields."""
    svc = FulfillmentTaskStepService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fulfillmenttaskstep(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FulfillmentTaskStep with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fulfillmenttasksteps/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fulfillmenttaskstep(item_id: int, hard: bool = Query(False)):
    """Delete FulfillmentTaskStep record (soft-delete by default)."""
    svc = FulfillmentTaskStepService()
    ok = svc.delete_fulfillmenttaskstep(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FulfillmentTaskStep with ID {item_id} not found")
    return None

@router.get("/fulfillmenttasksteps/analytics/metrics", response_model=Dict[str, Any])
def get_fulfillmenttaskstep_metrics():
    """Calculate summary statistical KPIs for FulfillmentTaskStep collection."""
    svc = FulfillmentTaskStepService()
    return svc.calculate_aggregate_metrics()

# ==================== SLACommitmentTarget Endpoints ====================
@router.get("/slacommitmenttargets", response_model=List[Dict[str, Any]])
def list_slacommitmenttargets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SLACommitmentTarget records with pagination and filtering."""
    svc = SLACommitmentTargetService()
    items = svc.list_slacommitmenttargets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/slacommitmenttargets/{item_id}", response_model=Dict[str, Any])
def get_slacommitmenttarget_by_id(item_id: int):
    """Retrieve detailed record for SLACommitmentTarget by ID."""
    svc = SLACommitmentTargetService()
    item = svc.get_slacommitmenttarget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SLACommitmentTarget with ID {item_id} not found")
    return item.to_dict()

@router.post("/slacommitmenttargets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_slacommitmenttarget(payload: SLACommitmentTargetCreateSchema):
    """Create new SLACommitmentTarget instance in enterprise repository."""
    svc = SLACommitmentTargetService()
    try:
        item = svc.create_slacommitmenttarget(
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

@router.put("/slacommitmenttargets/{item_id}", response_model=Dict[str, Any])
def update_slacommitmenttarget(item_id: int, payload: SLACommitmentTargetUpdateSchema):
    """Update existing SLACommitmentTarget record fields."""
    svc = SLACommitmentTargetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_slacommitmenttarget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SLACommitmentTarget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/slacommitmenttargets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_slacommitmenttarget(item_id: int, hard: bool = Query(False)):
    """Delete SLACommitmentTarget record (soft-delete by default)."""
    svc = SLACommitmentTargetService()
    ok = svc.delete_slacommitmenttarget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SLACommitmentTarget with ID {item_id} not found")
    return None

@router.get("/slacommitmenttargets/analytics/metrics", response_model=Dict[str, Any])
def get_slacommitmenttarget_metrics():
    """Calculate summary statistical KPIs for SLACommitmentTarget collection."""
    svc = SLACommitmentTargetService()
    return svc.calculate_aggregate_metrics()

# ==================== HardwareProvisioningOrder Endpoints ====================
@router.get("/hardwareprovisioningorders", response_model=List[Dict[str, Any]])
def list_hardwareprovisioningorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HardwareProvisioningOrder records with pagination and filtering."""
    svc = HardwareProvisioningOrderService()
    items = svc.list_hardwareprovisioningorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hardwareprovisioningorders/{item_id}", response_model=Dict[str, Any])
def get_hardwareprovisioningorder_by_id(item_id: int):
    """Retrieve detailed record for HardwareProvisioningOrder by ID."""
    svc = HardwareProvisioningOrderService()
    item = svc.get_hardwareprovisioningorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HardwareProvisioningOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/hardwareprovisioningorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hardwareprovisioningorder(payload: HardwareProvisioningOrderCreateSchema):
    """Create new HardwareProvisioningOrder instance in enterprise repository."""
    svc = HardwareProvisioningOrderService()
    try:
        item = svc.create_hardwareprovisioningorder(
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

@router.put("/hardwareprovisioningorders/{item_id}", response_model=Dict[str, Any])
def update_hardwareprovisioningorder(item_id: int, payload: HardwareProvisioningOrderUpdateSchema):
    """Update existing HardwareProvisioningOrder record fields."""
    svc = HardwareProvisioningOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hardwareprovisioningorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HardwareProvisioningOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hardwareprovisioningorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hardwareprovisioningorder(item_id: int, hard: bool = Query(False)):
    """Delete HardwareProvisioningOrder record (soft-delete by default)."""
    svc = HardwareProvisioningOrderService()
    ok = svc.delete_hardwareprovisioningorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HardwareProvisioningOrder with ID {item_id} not found")
    return None

@router.get("/hardwareprovisioningorders/analytics/metrics", response_model=Dict[str, Any])
def get_hardwareprovisioningorder_metrics():
    """Calculate summary statistical KPIs for HardwareProvisioningOrder collection."""
    svc = HardwareProvisioningOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== SoftwareLicenseRequest Endpoints ====================
@router.get("/softwarelicenserequests", response_model=List[Dict[str, Any]])
def list_softwarelicenserequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SoftwareLicenseRequest records with pagination and filtering."""
    svc = SoftwareLicenseRequestService()
    items = svc.list_softwarelicenserequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/softwarelicenserequests/{item_id}", response_model=Dict[str, Any])
def get_softwarelicenserequest_by_id(item_id: int):
    """Retrieve detailed record for SoftwareLicenseRequest by ID."""
    svc = SoftwareLicenseRequestService()
    item = svc.get_softwarelicenserequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SoftwareLicenseRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/softwarelicenserequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_softwarelicenserequest(payload: SoftwareLicenseRequestCreateSchema):
    """Create new SoftwareLicenseRequest instance in enterprise repository."""
    svc = SoftwareLicenseRequestService()
    try:
        item = svc.create_softwarelicenserequest(
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

@router.put("/softwarelicenserequests/{item_id}", response_model=Dict[str, Any])
def update_softwarelicenserequest(item_id: int, payload: SoftwareLicenseRequestUpdateSchema):
    """Update existing SoftwareLicenseRequest record fields."""
    svc = SoftwareLicenseRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_softwarelicenserequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SoftwareLicenseRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/softwarelicenserequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_softwarelicenserequest(item_id: int, hard: bool = Query(False)):
    """Delete SoftwareLicenseRequest record (soft-delete by default)."""
    svc = SoftwareLicenseRequestService()
    ok = svc.delete_softwarelicenserequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SoftwareLicenseRequest with ID {item_id} not found")
    return None

@router.get("/softwarelicenserequests/analytics/metrics", response_model=Dict[str, Any])
def get_softwarelicenserequest_metrics():
    """Calculate summary statistical KPIs for SoftwareLicenseRequest collection."""
    svc = SoftwareLicenseRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== CloudResourceQuota Endpoints ====================
@router.get("/cloudresourcequotas", response_model=List[Dict[str, Any]])
def list_cloudresourcequotas(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CloudResourceQuota records with pagination and filtering."""
    svc = CloudResourceQuotaService()
    items = svc.list_cloudresourcequotas(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cloudresourcequotas/{item_id}", response_model=Dict[str, Any])
def get_cloudresourcequota_by_id(item_id: int):
    """Retrieve detailed record for CloudResourceQuota by ID."""
    svc = CloudResourceQuotaService()
    item = svc.get_cloudresourcequota_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CloudResourceQuota with ID {item_id} not found")
    return item.to_dict()

@router.post("/cloudresourcequotas", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cloudresourcequota(payload: CloudResourceQuotaCreateSchema):
    """Create new CloudResourceQuota instance in enterprise repository."""
    svc = CloudResourceQuotaService()
    try:
        item = svc.create_cloudresourcequota(
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

@router.put("/cloudresourcequotas/{item_id}", response_model=Dict[str, Any])
def update_cloudresourcequota(item_id: int, payload: CloudResourceQuotaUpdateSchema):
    """Update existing CloudResourceQuota record fields."""
    svc = CloudResourceQuotaService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cloudresourcequota(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CloudResourceQuota with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cloudresourcequotas/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cloudresourcequota(item_id: int, hard: bool = Query(False)):
    """Delete CloudResourceQuota record (soft-delete by default)."""
    svc = CloudResourceQuotaService()
    ok = svc.delete_cloudresourcequota(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CloudResourceQuota with ID {item_id} not found")
    return None

@router.get("/cloudresourcequotas/analytics/metrics", response_model=Dict[str, Any])
def get_cloudresourcequota_metrics():
    """Calculate summary statistical KPIs for CloudResourceQuota collection."""
    svc = CloudResourceQuotaService()
    return svc.calculate_aggregate_metrics()

# ==================== EmployeeAccessRequest Endpoints ====================
@router.get("/employeeaccessrequests", response_model=List[Dict[str, Any]])
def list_employeeaccessrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmployeeAccessRequest records with pagination and filtering."""
    svc = EmployeeAccessRequestService()
    items = svc.list_employeeaccessrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/employeeaccessrequests/{item_id}", response_model=Dict[str, Any])
def get_employeeaccessrequest_by_id(item_id: int):
    """Retrieve detailed record for EmployeeAccessRequest by ID."""
    svc = EmployeeAccessRequestService()
    item = svc.get_employeeaccessrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmployeeAccessRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/employeeaccessrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_employeeaccessrequest(payload: EmployeeAccessRequestCreateSchema):
    """Create new EmployeeAccessRequest instance in enterprise repository."""
    svc = EmployeeAccessRequestService()
    try:
        item = svc.create_employeeaccessrequest(
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

@router.put("/employeeaccessrequests/{item_id}", response_model=Dict[str, Any])
def update_employeeaccessrequest(item_id: int, payload: EmployeeAccessRequestUpdateSchema):
    """Update existing EmployeeAccessRequest record fields."""
    svc = EmployeeAccessRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_employeeaccessrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmployeeAccessRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/employeeaccessrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employeeaccessrequest(item_id: int, hard: bool = Query(False)):
    """Delete EmployeeAccessRequest record (soft-delete by default)."""
    svc = EmployeeAccessRequestService()
    ok = svc.delete_employeeaccessrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmployeeAccessRequest with ID {item_id} not found")
    return None

@router.get("/employeeaccessrequests/analytics/metrics", response_model=Dict[str, Any])
def get_employeeaccessrequest_metrics():
    """Calculate summary statistical KPIs for EmployeeAccessRequest collection."""
    svc = EmployeeAccessRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== CostCenterChargeback Endpoints ====================
@router.get("/costcenterchargebacks", response_model=List[Dict[str, Any]])
def list_costcenterchargebacks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CostCenterChargeback records with pagination and filtering."""
    svc = CostCenterChargebackService()
    items = svc.list_costcenterchargebacks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/costcenterchargebacks/{item_id}", response_model=Dict[str, Any])
def get_costcenterchargeback_by_id(item_id: int):
    """Retrieve detailed record for CostCenterChargeback by ID."""
    svc = CostCenterChargebackService()
    item = svc.get_costcenterchargeback_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CostCenterChargeback with ID {item_id} not found")
    return item.to_dict()

@router.post("/costcenterchargebacks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_costcenterchargeback(payload: CostCenterChargebackCreateSchema):
    """Create new CostCenterChargeback instance in enterprise repository."""
    svc = CostCenterChargebackService()
    try:
        item = svc.create_costcenterchargeback(
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

@router.put("/costcenterchargebacks/{item_id}", response_model=Dict[str, Any])
def update_costcenterchargeback(item_id: int, payload: CostCenterChargebackUpdateSchema):
    """Update existing CostCenterChargeback record fields."""
    svc = CostCenterChargebackService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_costcenterchargeback(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CostCenterChargeback with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/costcenterchargebacks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_costcenterchargeback(item_id: int, hard: bool = Query(False)):
    """Delete CostCenterChargeback record (soft-delete by default)."""
    svc = CostCenterChargebackService()
    ok = svc.delete_costcenterchargeback(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CostCenterChargeback with ID {item_id} not found")
    return None

@router.get("/costcenterchargebacks/analytics/metrics", response_model=Dict[str, Any])
def get_costcenterchargeback_metrics():
    """Calculate summary statistical KPIs for CostCenterChargeback collection."""
    svc = CostCenterChargebackService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceDeskTicketLink Endpoints ====================
@router.get("/servicedeskticketlinks", response_model=List[Dict[str, Any]])
def list_servicedeskticketlinks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceDeskTicketLink records with pagination and filtering."""
    svc = ServiceDeskTicketLinkService()
    items = svc.list_servicedeskticketlinks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicedeskticketlinks/{item_id}", response_model=Dict[str, Any])
def get_servicedeskticketlink_by_id(item_id: int):
    """Retrieve detailed record for ServiceDeskTicketLink by ID."""
    svc = ServiceDeskTicketLinkService()
    item = svc.get_servicedeskticketlink_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceDeskTicketLink with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicedeskticketlinks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicedeskticketlink(payload: ServiceDeskTicketLinkCreateSchema):
    """Create new ServiceDeskTicketLink instance in enterprise repository."""
    svc = ServiceDeskTicketLinkService()
    try:
        item = svc.create_servicedeskticketlink(
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

@router.put("/servicedeskticketlinks/{item_id}", response_model=Dict[str, Any])
def update_servicedeskticketlink(item_id: int, payload: ServiceDeskTicketLinkUpdateSchema):
    """Update existing ServiceDeskTicketLink record fields."""
    svc = ServiceDeskTicketLinkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicedeskticketlink(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceDeskTicketLink with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicedeskticketlinks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicedeskticketlink(item_id: int, hard: bool = Query(False)):
    """Delete ServiceDeskTicketLink record (soft-delete by default)."""
    svc = ServiceDeskTicketLinkService()
    ok = svc.delete_servicedeskticketlink(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceDeskTicketLink with ID {item_id} not found")
    return None

@router.get("/servicedeskticketlinks/analytics/metrics", response_model=Dict[str, Any])
def get_servicedeskticketlink_metrics():
    """Calculate summary statistical KPIs for ServiceDeskTicketLink collection."""
    svc = ServiceDeskTicketLinkService()
    return svc.calculate_aggregate_metrics()

# ==================== CatalogItemDependency Endpoints ====================
@router.get("/catalogitemdependencys", response_model=List[Dict[str, Any]])
def list_catalogitemdependencys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CatalogItemDependency records with pagination and filtering."""
    svc = CatalogItemDependencyService()
    items = svc.list_catalogitemdependencys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/catalogitemdependencys/{item_id}", response_model=Dict[str, Any])
def get_catalogitemdependency_by_id(item_id: int):
    """Retrieve detailed record for CatalogItemDependency by ID."""
    svc = CatalogItemDependencyService()
    item = svc.get_catalogitemdependency_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CatalogItemDependency with ID {item_id} not found")
    return item.to_dict()

@router.post("/catalogitemdependencys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_catalogitemdependency(payload: CatalogItemDependencyCreateSchema):
    """Create new CatalogItemDependency instance in enterprise repository."""
    svc = CatalogItemDependencyService()
    try:
        item = svc.create_catalogitemdependency(
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

@router.put("/catalogitemdependencys/{item_id}", response_model=Dict[str, Any])
def update_catalogitemdependency(item_id: int, payload: CatalogItemDependencyUpdateSchema):
    """Update existing CatalogItemDependency record fields."""
    svc = CatalogItemDependencyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_catalogitemdependency(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CatalogItemDependency with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/catalogitemdependencys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_catalogitemdependency(item_id: int, hard: bool = Query(False)):
    """Delete CatalogItemDependency record (soft-delete by default)."""
    svc = CatalogItemDependencyService()
    ok = svc.delete_catalogitemdependency(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CatalogItemDependency with ID {item_id} not found")
    return None

@router.get("/catalogitemdependencys/analytics/metrics", response_model=Dict[str, Any])
def get_catalogitemdependency_metrics():
    """Calculate summary statistical KPIs for CatalogItemDependency collection."""
    svc = CatalogItemDependencyService()
    return svc.calculate_aggregate_metrics()

# ==================== UserEntitlementRule Endpoints ====================
@router.get("/userentitlementrules", response_model=List[Dict[str, Any]])
def list_userentitlementrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List UserEntitlementRule records with pagination and filtering."""
    svc = UserEntitlementRuleService()
    items = svc.list_userentitlementrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/userentitlementrules/{item_id}", response_model=Dict[str, Any])
def get_userentitlementrule_by_id(item_id: int):
    """Retrieve detailed record for UserEntitlementRule by ID."""
    svc = UserEntitlementRuleService()
    item = svc.get_userentitlementrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"UserEntitlementRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/userentitlementrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_userentitlementrule(payload: UserEntitlementRuleCreateSchema):
    """Create new UserEntitlementRule instance in enterprise repository."""
    svc = UserEntitlementRuleService()
    try:
        item = svc.create_userentitlementrule(
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

@router.put("/userentitlementrules/{item_id}", response_model=Dict[str, Any])
def update_userentitlementrule(item_id: int, payload: UserEntitlementRuleUpdateSchema):
    """Update existing UserEntitlementRule record fields."""
    svc = UserEntitlementRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_userentitlementrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"UserEntitlementRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/userentitlementrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_userentitlementrule(item_id: int, hard: bool = Query(False)):
    """Delete UserEntitlementRule record (soft-delete by default)."""
    svc = UserEntitlementRuleService()
    ok = svc.delete_userentitlementrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"UserEntitlementRule with ID {item_id} not found")
    return None

@router.get("/userentitlementrules/analytics/metrics", response_model=Dict[str, Any])
def get_userentitlementrule_metrics():
    """Calculate summary statistical KPIs for UserEntitlementRule collection."""
    svc = UserEntitlementRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== RequestSatisfactionScore Endpoints ====================
@router.get("/requestsatisfactionscores", response_model=List[Dict[str, Any]])
def list_requestsatisfactionscores(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RequestSatisfactionScore records with pagination and filtering."""
    svc = RequestSatisfactionScoreService()
    items = svc.list_requestsatisfactionscores(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/requestsatisfactionscores/{item_id}", response_model=Dict[str, Any])
def get_requestsatisfactionscore_by_id(item_id: int):
    """Retrieve detailed record for RequestSatisfactionScore by ID."""
    svc = RequestSatisfactionScoreService()
    item = svc.get_requestsatisfactionscore_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RequestSatisfactionScore with ID {item_id} not found")
    return item.to_dict()

@router.post("/requestsatisfactionscores", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_requestsatisfactionscore(payload: RequestSatisfactionScoreCreateSchema):
    """Create new RequestSatisfactionScore instance in enterprise repository."""
    svc = RequestSatisfactionScoreService()
    try:
        item = svc.create_requestsatisfactionscore(
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

@router.put("/requestsatisfactionscores/{item_id}", response_model=Dict[str, Any])
def update_requestsatisfactionscore(item_id: int, payload: RequestSatisfactionScoreUpdateSchema):
    """Update existing RequestSatisfactionScore record fields."""
    svc = RequestSatisfactionScoreService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_requestsatisfactionscore(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RequestSatisfactionScore with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/requestsatisfactionscores/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_requestsatisfactionscore(item_id: int, hard: bool = Query(False)):
    """Delete RequestSatisfactionScore record (soft-delete by default)."""
    svc = RequestSatisfactionScoreService()
    ok = svc.delete_requestsatisfactionscore(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RequestSatisfactionScore with ID {item_id} not found")
    return None

@router.get("/requestsatisfactionscores/analytics/metrics", response_model=Dict[str, Any])
def get_requestsatisfactionscore_metrics():
    """Calculate summary statistical KPIs for RequestSatisfactionScore collection."""
    svc = RequestSatisfactionScoreService()
    return svc.calculate_aggregate_metrics()

# ==================== RecurringServiceOrder Endpoints ====================
@router.get("/recurringserviceorders", response_model=List[Dict[str, Any]])
def list_recurringserviceorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RecurringServiceOrder records with pagination and filtering."""
    svc = RecurringServiceOrderService()
    items = svc.list_recurringserviceorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/recurringserviceorders/{item_id}", response_model=Dict[str, Any])
def get_recurringserviceorder_by_id(item_id: int):
    """Retrieve detailed record for RecurringServiceOrder by ID."""
    svc = RecurringServiceOrderService()
    item = svc.get_recurringserviceorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RecurringServiceOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/recurringserviceorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_recurringserviceorder(payload: RecurringServiceOrderCreateSchema):
    """Create new RecurringServiceOrder instance in enterprise repository."""
    svc = RecurringServiceOrderService()
    try:
        item = svc.create_recurringserviceorder(
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

@router.put("/recurringserviceorders/{item_id}", response_model=Dict[str, Any])
def update_recurringserviceorder(item_id: int, payload: RecurringServiceOrderUpdateSchema):
    """Update existing RecurringServiceOrder record fields."""
    svc = RecurringServiceOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_recurringserviceorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RecurringServiceOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/recurringserviceorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recurringserviceorder(item_id: int, hard: bool = Query(False)):
    """Delete RecurringServiceOrder record (soft-delete by default)."""
    svc = RecurringServiceOrderService()
    ok = svc.delete_recurringserviceorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RecurringServiceOrder with ID {item_id} not found")
    return None

@router.get("/recurringserviceorders/analytics/metrics", response_model=Dict[str, Any])
def get_recurringserviceorder_metrics():
    """Calculate summary statistical KPIs for RecurringServiceOrder collection."""
    svc = RecurringServiceOrderService()
    return svc.calculate_aggregate_metrics()

