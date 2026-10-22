"""
Field Service & Dispatch Automation - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ServiceWorkOrderService,
    TechnicianProfileService,
    SkillCertificationService,
    DispatchAssignmentService,
    RouteWayfindingService,
    PartsRequirementService,
    VanInventoryStockService,
    ServiceReportSignatureService,
    CustomerFeedbackRatingService,
    EmergencyCalloutService,
    MaintenanceChecklistService,
    WarrantyEntitlementService,
    ServiceLevelBreachAlertService,
    TimeOnSiteLogService,
    EquipmentAssetHistoryService,
    FieldExpenseClaimService,
)
from .schemas import (
    ServiceWorkOrderCreateSchema, ServiceWorkOrderUpdateSchema, ServiceWorkOrderResponseSchema,
    TechnicianProfileCreateSchema, TechnicianProfileUpdateSchema, TechnicianProfileResponseSchema,
    SkillCertificationCreateSchema, SkillCertificationUpdateSchema, SkillCertificationResponseSchema,
    DispatchAssignmentCreateSchema, DispatchAssignmentUpdateSchema, DispatchAssignmentResponseSchema,
    RouteWayfindingCreateSchema, RouteWayfindingUpdateSchema, RouteWayfindingResponseSchema,
    PartsRequirementCreateSchema, PartsRequirementUpdateSchema, PartsRequirementResponseSchema,
    VanInventoryStockCreateSchema, VanInventoryStockUpdateSchema, VanInventoryStockResponseSchema,
    ServiceReportSignatureCreateSchema, ServiceReportSignatureUpdateSchema, ServiceReportSignatureResponseSchema,
    CustomerFeedbackRatingCreateSchema, CustomerFeedbackRatingUpdateSchema, CustomerFeedbackRatingResponseSchema,
    EmergencyCalloutCreateSchema, EmergencyCalloutUpdateSchema, EmergencyCalloutResponseSchema,
    MaintenanceChecklistCreateSchema, MaintenanceChecklistUpdateSchema, MaintenanceChecklistResponseSchema,
    WarrantyEntitlementCreateSchema, WarrantyEntitlementUpdateSchema, WarrantyEntitlementResponseSchema,
    ServiceLevelBreachAlertCreateSchema, ServiceLevelBreachAlertUpdateSchema, ServiceLevelBreachAlertResponseSchema,
    TimeOnSiteLogCreateSchema, TimeOnSiteLogUpdateSchema, TimeOnSiteLogResponseSchema,
    EquipmentAssetHistoryCreateSchema, EquipmentAssetHistoryUpdateSchema, EquipmentAssetHistoryResponseSchema,
    FieldExpenseClaimCreateSchema, FieldExpenseClaimUpdateSchema, FieldExpenseClaimResponseSchema,
)

router = APIRouter(prefix="/field_service", tags=["Field Service & Dispatch Automation"])

# ==================== ServiceWorkOrder Endpoints ====================
@router.get("/serviceworkorders", response_model=List[Dict[str, Any]])
def list_serviceworkorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceWorkOrder records with pagination and filtering."""
    svc = ServiceWorkOrderService()
    items = svc.list_serviceworkorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/serviceworkorders/{item_id}", response_model=Dict[str, Any])
def get_serviceworkorder_by_id(item_id: int):
    """Retrieve detailed record for ServiceWorkOrder by ID."""
    svc = ServiceWorkOrderService()
    item = svc.get_serviceworkorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceWorkOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/serviceworkorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_serviceworkorder(payload: ServiceWorkOrderCreateSchema):
    """Create new ServiceWorkOrder instance in enterprise repository."""
    svc = ServiceWorkOrderService()
    try:
        item = svc.create_serviceworkorder(
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

@router.put("/serviceworkorders/{item_id}", response_model=Dict[str, Any])
def update_serviceworkorder(item_id: int, payload: ServiceWorkOrderUpdateSchema):
    """Update existing ServiceWorkOrder record fields."""
    svc = ServiceWorkOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_serviceworkorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceWorkOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/serviceworkorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_serviceworkorder(item_id: int, hard: bool = Query(False)):
    """Delete ServiceWorkOrder record (soft-delete by default)."""
    svc = ServiceWorkOrderService()
    ok = svc.delete_serviceworkorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceWorkOrder with ID {item_id} not found")
    return None

@router.get("/serviceworkorders/analytics/metrics", response_model=Dict[str, Any])
def get_serviceworkorder_metrics():
    """Calculate summary statistical KPIs for ServiceWorkOrder collection."""
    svc = ServiceWorkOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== TechnicianProfile Endpoints ====================
@router.get("/technicianprofiles", response_model=List[Dict[str, Any]])
def list_technicianprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TechnicianProfile records with pagination and filtering."""
    svc = TechnicianProfileService()
    items = svc.list_technicianprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/technicianprofiles/{item_id}", response_model=Dict[str, Any])
def get_technicianprofile_by_id(item_id: int):
    """Retrieve detailed record for TechnicianProfile by ID."""
    svc = TechnicianProfileService()
    item = svc.get_technicianprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TechnicianProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/technicianprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_technicianprofile(payload: TechnicianProfileCreateSchema):
    """Create new TechnicianProfile instance in enterprise repository."""
    svc = TechnicianProfileService()
    try:
        item = svc.create_technicianprofile(
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

@router.put("/technicianprofiles/{item_id}", response_model=Dict[str, Any])
def update_technicianprofile(item_id: int, payload: TechnicianProfileUpdateSchema):
    """Update existing TechnicianProfile record fields."""
    svc = TechnicianProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_technicianprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TechnicianProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/technicianprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_technicianprofile(item_id: int, hard: bool = Query(False)):
    """Delete TechnicianProfile record (soft-delete by default)."""
    svc = TechnicianProfileService()
    ok = svc.delete_technicianprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TechnicianProfile with ID {item_id} not found")
    return None

@router.get("/technicianprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_technicianprofile_metrics():
    """Calculate summary statistical KPIs for TechnicianProfile collection."""
    svc = TechnicianProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== SkillCertification Endpoints ====================
@router.get("/skillcertifications", response_model=List[Dict[str, Any]])
def list_skillcertifications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SkillCertification records with pagination and filtering."""
    svc = SkillCertificationService()
    items = svc.list_skillcertifications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/skillcertifications/{item_id}", response_model=Dict[str, Any])
def get_skillcertification_by_id(item_id: int):
    """Retrieve detailed record for SkillCertification by ID."""
    svc = SkillCertificationService()
    item = svc.get_skillcertification_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SkillCertification with ID {item_id} not found")
    return item.to_dict()

@router.post("/skillcertifications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_skillcertification(payload: SkillCertificationCreateSchema):
    """Create new SkillCertification instance in enterprise repository."""
    svc = SkillCertificationService()
    try:
        item = svc.create_skillcertification(
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

@router.put("/skillcertifications/{item_id}", response_model=Dict[str, Any])
def update_skillcertification(item_id: int, payload: SkillCertificationUpdateSchema):
    """Update existing SkillCertification record fields."""
    svc = SkillCertificationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_skillcertification(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SkillCertification with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/skillcertifications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_skillcertification(item_id: int, hard: bool = Query(False)):
    """Delete SkillCertification record (soft-delete by default)."""
    svc = SkillCertificationService()
    ok = svc.delete_skillcertification(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SkillCertification with ID {item_id} not found")
    return None

@router.get("/skillcertifications/analytics/metrics", response_model=Dict[str, Any])
def get_skillcertification_metrics():
    """Calculate summary statistical KPIs for SkillCertification collection."""
    svc = SkillCertificationService()
    return svc.calculate_aggregate_metrics()

# ==================== DispatchAssignment Endpoints ====================
@router.get("/dispatchassignments", response_model=List[Dict[str, Any]])
def list_dispatchassignments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DispatchAssignment records with pagination and filtering."""
    svc = DispatchAssignmentService()
    items = svc.list_dispatchassignments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dispatchassignments/{item_id}", response_model=Dict[str, Any])
def get_dispatchassignment_by_id(item_id: int):
    """Retrieve detailed record for DispatchAssignment by ID."""
    svc = DispatchAssignmentService()
    item = svc.get_dispatchassignment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DispatchAssignment with ID {item_id} not found")
    return item.to_dict()

@router.post("/dispatchassignments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dispatchassignment(payload: DispatchAssignmentCreateSchema):
    """Create new DispatchAssignment instance in enterprise repository."""
    svc = DispatchAssignmentService()
    try:
        item = svc.create_dispatchassignment(
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

@router.put("/dispatchassignments/{item_id}", response_model=Dict[str, Any])
def update_dispatchassignment(item_id: int, payload: DispatchAssignmentUpdateSchema):
    """Update existing DispatchAssignment record fields."""
    svc = DispatchAssignmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dispatchassignment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DispatchAssignment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dispatchassignments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dispatchassignment(item_id: int, hard: bool = Query(False)):
    """Delete DispatchAssignment record (soft-delete by default)."""
    svc = DispatchAssignmentService()
    ok = svc.delete_dispatchassignment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DispatchAssignment with ID {item_id} not found")
    return None

@router.get("/dispatchassignments/analytics/metrics", response_model=Dict[str, Any])
def get_dispatchassignment_metrics():
    """Calculate summary statistical KPIs for DispatchAssignment collection."""
    svc = DispatchAssignmentService()
    return svc.calculate_aggregate_metrics()

# ==================== RouteWayfinding Endpoints ====================
@router.get("/routewayfindings", response_model=List[Dict[str, Any]])
def list_routewayfindings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RouteWayfinding records with pagination and filtering."""
    svc = RouteWayfindingService()
    items = svc.list_routewayfindings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/routewayfindings/{item_id}", response_model=Dict[str, Any])
def get_routewayfinding_by_id(item_id: int):
    """Retrieve detailed record for RouteWayfinding by ID."""
    svc = RouteWayfindingService()
    item = svc.get_routewayfinding_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RouteWayfinding with ID {item_id} not found")
    return item.to_dict()

@router.post("/routewayfindings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_routewayfinding(payload: RouteWayfindingCreateSchema):
    """Create new RouteWayfinding instance in enterprise repository."""
    svc = RouteWayfindingService()
    try:
        item = svc.create_routewayfinding(
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

@router.put("/routewayfindings/{item_id}", response_model=Dict[str, Any])
def update_routewayfinding(item_id: int, payload: RouteWayfindingUpdateSchema):
    """Update existing RouteWayfinding record fields."""
    svc = RouteWayfindingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_routewayfinding(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RouteWayfinding with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/routewayfindings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_routewayfinding(item_id: int, hard: bool = Query(False)):
    """Delete RouteWayfinding record (soft-delete by default)."""
    svc = RouteWayfindingService()
    ok = svc.delete_routewayfinding(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RouteWayfinding with ID {item_id} not found")
    return None

@router.get("/routewayfindings/analytics/metrics", response_model=Dict[str, Any])
def get_routewayfinding_metrics():
    """Calculate summary statistical KPIs for RouteWayfinding collection."""
    svc = RouteWayfindingService()
    return svc.calculate_aggregate_metrics()

# ==================== PartsRequirement Endpoints ====================
@router.get("/partsrequirements", response_model=List[Dict[str, Any]])
def list_partsrequirements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartsRequirement records with pagination and filtering."""
    svc = PartsRequirementService()
    items = svc.list_partsrequirements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partsrequirements/{item_id}", response_model=Dict[str, Any])
def get_partsrequirement_by_id(item_id: int):
    """Retrieve detailed record for PartsRequirement by ID."""
    svc = PartsRequirementService()
    item = svc.get_partsrequirement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartsRequirement with ID {item_id} not found")
    return item.to_dict()

@router.post("/partsrequirements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partsrequirement(payload: PartsRequirementCreateSchema):
    """Create new PartsRequirement instance in enterprise repository."""
    svc = PartsRequirementService()
    try:
        item = svc.create_partsrequirement(
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

@router.put("/partsrequirements/{item_id}", response_model=Dict[str, Any])
def update_partsrequirement(item_id: int, payload: PartsRequirementUpdateSchema):
    """Update existing PartsRequirement record fields."""
    svc = PartsRequirementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partsrequirement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartsRequirement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partsrequirements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partsrequirement(item_id: int, hard: bool = Query(False)):
    """Delete PartsRequirement record (soft-delete by default)."""
    svc = PartsRequirementService()
    ok = svc.delete_partsrequirement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartsRequirement with ID {item_id} not found")
    return None

@router.get("/partsrequirements/analytics/metrics", response_model=Dict[str, Any])
def get_partsrequirement_metrics():
    """Calculate summary statistical KPIs for PartsRequirement collection."""
    svc = PartsRequirementService()
    return svc.calculate_aggregate_metrics()

# ==================== VanInventoryStock Endpoints ====================
@router.get("/vaninventorystocks", response_model=List[Dict[str, Any]])
def list_vaninventorystocks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VanInventoryStock records with pagination and filtering."""
    svc = VanInventoryStockService()
    items = svc.list_vaninventorystocks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vaninventorystocks/{item_id}", response_model=Dict[str, Any])
def get_vaninventorystock_by_id(item_id: int):
    """Retrieve detailed record for VanInventoryStock by ID."""
    svc = VanInventoryStockService()
    item = svc.get_vaninventorystock_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VanInventoryStock with ID {item_id} not found")
    return item.to_dict()

@router.post("/vaninventorystocks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vaninventorystock(payload: VanInventoryStockCreateSchema):
    """Create new VanInventoryStock instance in enterprise repository."""
    svc = VanInventoryStockService()
    try:
        item = svc.create_vaninventorystock(
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

@router.put("/vaninventorystocks/{item_id}", response_model=Dict[str, Any])
def update_vaninventorystock(item_id: int, payload: VanInventoryStockUpdateSchema):
    """Update existing VanInventoryStock record fields."""
    svc = VanInventoryStockService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vaninventorystock(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VanInventoryStock with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vaninventorystocks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vaninventorystock(item_id: int, hard: bool = Query(False)):
    """Delete VanInventoryStock record (soft-delete by default)."""
    svc = VanInventoryStockService()
    ok = svc.delete_vaninventorystock(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VanInventoryStock with ID {item_id} not found")
    return None

@router.get("/vaninventorystocks/analytics/metrics", response_model=Dict[str, Any])
def get_vaninventorystock_metrics():
    """Calculate summary statistical KPIs for VanInventoryStock collection."""
    svc = VanInventoryStockService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceReportSignature Endpoints ====================
@router.get("/servicereportsignatures", response_model=List[Dict[str, Any]])
def list_servicereportsignatures(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceReportSignature records with pagination and filtering."""
    svc = ServiceReportSignatureService()
    items = svc.list_servicereportsignatures(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicereportsignatures/{item_id}", response_model=Dict[str, Any])
def get_servicereportsignature_by_id(item_id: int):
    """Retrieve detailed record for ServiceReportSignature by ID."""
    svc = ServiceReportSignatureService()
    item = svc.get_servicereportsignature_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceReportSignature with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicereportsignatures", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicereportsignature(payload: ServiceReportSignatureCreateSchema):
    """Create new ServiceReportSignature instance in enterprise repository."""
    svc = ServiceReportSignatureService()
    try:
        item = svc.create_servicereportsignature(
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

@router.put("/servicereportsignatures/{item_id}", response_model=Dict[str, Any])
def update_servicereportsignature(item_id: int, payload: ServiceReportSignatureUpdateSchema):
    """Update existing ServiceReportSignature record fields."""
    svc = ServiceReportSignatureService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicereportsignature(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceReportSignature with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicereportsignatures/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicereportsignature(item_id: int, hard: bool = Query(False)):
    """Delete ServiceReportSignature record (soft-delete by default)."""
    svc = ServiceReportSignatureService()
    ok = svc.delete_servicereportsignature(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceReportSignature with ID {item_id} not found")
    return None

@router.get("/servicereportsignatures/analytics/metrics", response_model=Dict[str, Any])
def get_servicereportsignature_metrics():
    """Calculate summary statistical KPIs for ServiceReportSignature collection."""
    svc = ServiceReportSignatureService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerFeedbackRating Endpoints ====================
@router.get("/customerfeedbackratings", response_model=List[Dict[str, Any]])
def list_customerfeedbackratings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerFeedbackRating records with pagination and filtering."""
    svc = CustomerFeedbackRatingService()
    items = svc.list_customerfeedbackratings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerfeedbackratings/{item_id}", response_model=Dict[str, Any])
def get_customerfeedbackrating_by_id(item_id: int):
    """Retrieve detailed record for CustomerFeedbackRating by ID."""
    svc = CustomerFeedbackRatingService()
    item = svc.get_customerfeedbackrating_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerFeedbackRating with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerfeedbackratings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerfeedbackrating(payload: CustomerFeedbackRatingCreateSchema):
    """Create new CustomerFeedbackRating instance in enterprise repository."""
    svc = CustomerFeedbackRatingService()
    try:
        item = svc.create_customerfeedbackrating(
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

@router.put("/customerfeedbackratings/{item_id}", response_model=Dict[str, Any])
def update_customerfeedbackrating(item_id: int, payload: CustomerFeedbackRatingUpdateSchema):
    """Update existing CustomerFeedbackRating record fields."""
    svc = CustomerFeedbackRatingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerfeedbackrating(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerFeedbackRating with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerfeedbackratings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerfeedbackrating(item_id: int, hard: bool = Query(False)):
    """Delete CustomerFeedbackRating record (soft-delete by default)."""
    svc = CustomerFeedbackRatingService()
    ok = svc.delete_customerfeedbackrating(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerFeedbackRating with ID {item_id} not found")
    return None

@router.get("/customerfeedbackratings/analytics/metrics", response_model=Dict[str, Any])
def get_customerfeedbackrating_metrics():
    """Calculate summary statistical KPIs for CustomerFeedbackRating collection."""
    svc = CustomerFeedbackRatingService()
    return svc.calculate_aggregate_metrics()

# ==================== EmergencyCallout Endpoints ====================
@router.get("/emergencycallouts", response_model=List[Dict[str, Any]])
def list_emergencycallouts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmergencyCallout records with pagination and filtering."""
    svc = EmergencyCalloutService()
    items = svc.list_emergencycallouts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/emergencycallouts/{item_id}", response_model=Dict[str, Any])
def get_emergencycallout_by_id(item_id: int):
    """Retrieve detailed record for EmergencyCallout by ID."""
    svc = EmergencyCalloutService()
    item = svc.get_emergencycallout_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmergencyCallout with ID {item_id} not found")
    return item.to_dict()

@router.post("/emergencycallouts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_emergencycallout(payload: EmergencyCalloutCreateSchema):
    """Create new EmergencyCallout instance in enterprise repository."""
    svc = EmergencyCalloutService()
    try:
        item = svc.create_emergencycallout(
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

@router.put("/emergencycallouts/{item_id}", response_model=Dict[str, Any])
def update_emergencycallout(item_id: int, payload: EmergencyCalloutUpdateSchema):
    """Update existing EmergencyCallout record fields."""
    svc = EmergencyCalloutService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_emergencycallout(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmergencyCallout with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/emergencycallouts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_emergencycallout(item_id: int, hard: bool = Query(False)):
    """Delete EmergencyCallout record (soft-delete by default)."""
    svc = EmergencyCalloutService()
    ok = svc.delete_emergencycallout(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmergencyCallout with ID {item_id} not found")
    return None

@router.get("/emergencycallouts/analytics/metrics", response_model=Dict[str, Any])
def get_emergencycallout_metrics():
    """Calculate summary statistical KPIs for EmergencyCallout collection."""
    svc = EmergencyCalloutService()
    return svc.calculate_aggregate_metrics()

# ==================== MaintenanceChecklist Endpoints ====================
@router.get("/maintenancechecklists", response_model=List[Dict[str, Any]])
def list_maintenancechecklists(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MaintenanceChecklist records with pagination and filtering."""
    svc = MaintenanceChecklistService()
    items = svc.list_maintenancechecklists(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/maintenancechecklists/{item_id}", response_model=Dict[str, Any])
def get_maintenancechecklist_by_id(item_id: int):
    """Retrieve detailed record for MaintenanceChecklist by ID."""
    svc = MaintenanceChecklistService()
    item = svc.get_maintenancechecklist_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MaintenanceChecklist with ID {item_id} not found")
    return item.to_dict()

@router.post("/maintenancechecklists", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_maintenancechecklist(payload: MaintenanceChecklistCreateSchema):
    """Create new MaintenanceChecklist instance in enterprise repository."""
    svc = MaintenanceChecklistService()
    try:
        item = svc.create_maintenancechecklist(
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

@router.put("/maintenancechecklists/{item_id}", response_model=Dict[str, Any])
def update_maintenancechecklist(item_id: int, payload: MaintenanceChecklistUpdateSchema):
    """Update existing MaintenanceChecklist record fields."""
    svc = MaintenanceChecklistService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_maintenancechecklist(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MaintenanceChecklist with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/maintenancechecklists/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenancechecklist(item_id: int, hard: bool = Query(False)):
    """Delete MaintenanceChecklist record (soft-delete by default)."""
    svc = MaintenanceChecklistService()
    ok = svc.delete_maintenancechecklist(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MaintenanceChecklist with ID {item_id} not found")
    return None

@router.get("/maintenancechecklists/analytics/metrics", response_model=Dict[str, Any])
def get_maintenancechecklist_metrics():
    """Calculate summary statistical KPIs for MaintenanceChecklist collection."""
    svc = MaintenanceChecklistService()
    return svc.calculate_aggregate_metrics()

# ==================== WarrantyEntitlement Endpoints ====================
@router.get("/warrantyentitlements", response_model=List[Dict[str, Any]])
def list_warrantyentitlements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WarrantyEntitlement records with pagination and filtering."""
    svc = WarrantyEntitlementService()
    items = svc.list_warrantyentitlements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/warrantyentitlements/{item_id}", response_model=Dict[str, Any])
def get_warrantyentitlement_by_id(item_id: int):
    """Retrieve detailed record for WarrantyEntitlement by ID."""
    svc = WarrantyEntitlementService()
    item = svc.get_warrantyentitlement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WarrantyEntitlement with ID {item_id} not found")
    return item.to_dict()

@router.post("/warrantyentitlements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_warrantyentitlement(payload: WarrantyEntitlementCreateSchema):
    """Create new WarrantyEntitlement instance in enterprise repository."""
    svc = WarrantyEntitlementService()
    try:
        item = svc.create_warrantyentitlement(
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

@router.put("/warrantyentitlements/{item_id}", response_model=Dict[str, Any])
def update_warrantyentitlement(item_id: int, payload: WarrantyEntitlementUpdateSchema):
    """Update existing WarrantyEntitlement record fields."""
    svc = WarrantyEntitlementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_warrantyentitlement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WarrantyEntitlement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/warrantyentitlements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warrantyentitlement(item_id: int, hard: bool = Query(False)):
    """Delete WarrantyEntitlement record (soft-delete by default)."""
    svc = WarrantyEntitlementService()
    ok = svc.delete_warrantyentitlement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WarrantyEntitlement with ID {item_id} not found")
    return None

@router.get("/warrantyentitlements/analytics/metrics", response_model=Dict[str, Any])
def get_warrantyentitlement_metrics():
    """Calculate summary statistical KPIs for WarrantyEntitlement collection."""
    svc = WarrantyEntitlementService()
    return svc.calculate_aggregate_metrics()

# ==================== ServiceLevelBreachAlert Endpoints ====================
@router.get("/servicelevelbreachalerts", response_model=List[Dict[str, Any]])
def list_servicelevelbreachalerts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ServiceLevelBreachAlert records with pagination and filtering."""
    svc = ServiceLevelBreachAlertService()
    items = svc.list_servicelevelbreachalerts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/servicelevelbreachalerts/{item_id}", response_model=Dict[str, Any])
def get_servicelevelbreachalert_by_id(item_id: int):
    """Retrieve detailed record for ServiceLevelBreachAlert by ID."""
    svc = ServiceLevelBreachAlertService()
    item = svc.get_servicelevelbreachalert_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ServiceLevelBreachAlert with ID {item_id} not found")
    return item.to_dict()

@router.post("/servicelevelbreachalerts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_servicelevelbreachalert(payload: ServiceLevelBreachAlertCreateSchema):
    """Create new ServiceLevelBreachAlert instance in enterprise repository."""
    svc = ServiceLevelBreachAlertService()
    try:
        item = svc.create_servicelevelbreachalert(
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

@router.put("/servicelevelbreachalerts/{item_id}", response_model=Dict[str, Any])
def update_servicelevelbreachalert(item_id: int, payload: ServiceLevelBreachAlertUpdateSchema):
    """Update existing ServiceLevelBreachAlert record fields."""
    svc = ServiceLevelBreachAlertService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_servicelevelbreachalert(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ServiceLevelBreachAlert with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/servicelevelbreachalerts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servicelevelbreachalert(item_id: int, hard: bool = Query(False)):
    """Delete ServiceLevelBreachAlert record (soft-delete by default)."""
    svc = ServiceLevelBreachAlertService()
    ok = svc.delete_servicelevelbreachalert(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ServiceLevelBreachAlert with ID {item_id} not found")
    return None

@router.get("/servicelevelbreachalerts/analytics/metrics", response_model=Dict[str, Any])
def get_servicelevelbreachalert_metrics():
    """Calculate summary statistical KPIs for ServiceLevelBreachAlert collection."""
    svc = ServiceLevelBreachAlertService()
    return svc.calculate_aggregate_metrics()

# ==================== TimeOnSiteLog Endpoints ====================
@router.get("/timeonsitelogs", response_model=List[Dict[str, Any]])
def list_timeonsitelogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TimeOnSiteLog records with pagination and filtering."""
    svc = TimeOnSiteLogService()
    items = svc.list_timeonsitelogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/timeonsitelogs/{item_id}", response_model=Dict[str, Any])
def get_timeonsitelog_by_id(item_id: int):
    """Retrieve detailed record for TimeOnSiteLog by ID."""
    svc = TimeOnSiteLogService()
    item = svc.get_timeonsitelog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TimeOnSiteLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/timeonsitelogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_timeonsitelog(payload: TimeOnSiteLogCreateSchema):
    """Create new TimeOnSiteLog instance in enterprise repository."""
    svc = TimeOnSiteLogService()
    try:
        item = svc.create_timeonsitelog(
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

@router.put("/timeonsitelogs/{item_id}", response_model=Dict[str, Any])
def update_timeonsitelog(item_id: int, payload: TimeOnSiteLogUpdateSchema):
    """Update existing TimeOnSiteLog record fields."""
    svc = TimeOnSiteLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_timeonsitelog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TimeOnSiteLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/timeonsitelogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_timeonsitelog(item_id: int, hard: bool = Query(False)):
    """Delete TimeOnSiteLog record (soft-delete by default)."""
    svc = TimeOnSiteLogService()
    ok = svc.delete_timeonsitelog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TimeOnSiteLog with ID {item_id} not found")
    return None

@router.get("/timeonsitelogs/analytics/metrics", response_model=Dict[str, Any])
def get_timeonsitelog_metrics():
    """Calculate summary statistical KPIs for TimeOnSiteLog collection."""
    svc = TimeOnSiteLogService()
    return svc.calculate_aggregate_metrics()

# ==================== EquipmentAssetHistory Endpoints ====================
@router.get("/equipmentassethistorys", response_model=List[Dict[str, Any]])
def list_equipmentassethistorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EquipmentAssetHistory records with pagination and filtering."""
    svc = EquipmentAssetHistoryService()
    items = svc.list_equipmentassethistorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/equipmentassethistorys/{item_id}", response_model=Dict[str, Any])
def get_equipmentassethistory_by_id(item_id: int):
    """Retrieve detailed record for EquipmentAssetHistory by ID."""
    svc = EquipmentAssetHistoryService()
    item = svc.get_equipmentassethistory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EquipmentAssetHistory with ID {item_id} not found")
    return item.to_dict()

@router.post("/equipmentassethistorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_equipmentassethistory(payload: EquipmentAssetHistoryCreateSchema):
    """Create new EquipmentAssetHistory instance in enterprise repository."""
    svc = EquipmentAssetHistoryService()
    try:
        item = svc.create_equipmentassethistory(
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

@router.put("/equipmentassethistorys/{item_id}", response_model=Dict[str, Any])
def update_equipmentassethistory(item_id: int, payload: EquipmentAssetHistoryUpdateSchema):
    """Update existing EquipmentAssetHistory record fields."""
    svc = EquipmentAssetHistoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_equipmentassethistory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EquipmentAssetHistory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/equipmentassethistorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equipmentassethistory(item_id: int, hard: bool = Query(False)):
    """Delete EquipmentAssetHistory record (soft-delete by default)."""
    svc = EquipmentAssetHistoryService()
    ok = svc.delete_equipmentassethistory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EquipmentAssetHistory with ID {item_id} not found")
    return None

@router.get("/equipmentassethistorys/analytics/metrics", response_model=Dict[str, Any])
def get_equipmentassethistory_metrics():
    """Calculate summary statistical KPIs for EquipmentAssetHistory collection."""
    svc = EquipmentAssetHistoryService()
    return svc.calculate_aggregate_metrics()

# ==================== FieldExpenseClaim Endpoints ====================
@router.get("/fieldexpenseclaims", response_model=List[Dict[str, Any]])
def list_fieldexpenseclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FieldExpenseClaim records with pagination and filtering."""
    svc = FieldExpenseClaimService()
    items = svc.list_fieldexpenseclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fieldexpenseclaims/{item_id}", response_model=Dict[str, Any])
def get_fieldexpenseclaim_by_id(item_id: int):
    """Retrieve detailed record for FieldExpenseClaim by ID."""
    svc = FieldExpenseClaimService()
    item = svc.get_fieldexpenseclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FieldExpenseClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/fieldexpenseclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fieldexpenseclaim(payload: FieldExpenseClaimCreateSchema):
    """Create new FieldExpenseClaim instance in enterprise repository."""
    svc = FieldExpenseClaimService()
    try:
        item = svc.create_fieldexpenseclaim(
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

@router.put("/fieldexpenseclaims/{item_id}", response_model=Dict[str, Any])
def update_fieldexpenseclaim(item_id: int, payload: FieldExpenseClaimUpdateSchema):
    """Update existing FieldExpenseClaim record fields."""
    svc = FieldExpenseClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fieldexpenseclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FieldExpenseClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fieldexpenseclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fieldexpenseclaim(item_id: int, hard: bool = Query(False)):
    """Delete FieldExpenseClaim record (soft-delete by default)."""
    svc = FieldExpenseClaimService()
    ok = svc.delete_fieldexpenseclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FieldExpenseClaim with ID {item_id} not found")
    return None

@router.get("/fieldexpenseclaims/analytics/metrics", response_model=Dict[str, Any])
def get_fieldexpenseclaim_metrics():
    """Calculate summary statistical KPIs for FieldExpenseClaim collection."""
    svc = FieldExpenseClaimService()
    return svc.calculate_aggregate_metrics()

