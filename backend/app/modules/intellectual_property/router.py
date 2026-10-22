"""
Intellectual Property & Patent Portfolio - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    PatentApplicationService,
    TrademarkRegistrationService,
    CopyrightFilingService,
    TradeSecretInventoryService,
    InventionDisclosureService,
    PatentOfficeActionService,
    IPRoyaltyAgreementService,
    LicenseGrantRightService,
    PriorArtSearchService,
    InfringementMonitoringService,
    ExternalPatentCounselService,
    AnnuityFeeScheduleService,
    JointDevelopmentPactService,
    PatentFamilyMappingService,
    CommercialValuationService,
    TechnologyTransferService,
)
from .schemas import (
    PatentApplicationCreateSchema, PatentApplicationUpdateSchema, PatentApplicationResponseSchema,
    TrademarkRegistrationCreateSchema, TrademarkRegistrationUpdateSchema, TrademarkRegistrationResponseSchema,
    CopyrightFilingCreateSchema, CopyrightFilingUpdateSchema, CopyrightFilingResponseSchema,
    TradeSecretInventoryCreateSchema, TradeSecretInventoryUpdateSchema, TradeSecretInventoryResponseSchema,
    InventionDisclosureCreateSchema, InventionDisclosureUpdateSchema, InventionDisclosureResponseSchema,
    PatentOfficeActionCreateSchema, PatentOfficeActionUpdateSchema, PatentOfficeActionResponseSchema,
    IPRoyaltyAgreementCreateSchema, IPRoyaltyAgreementUpdateSchema, IPRoyaltyAgreementResponseSchema,
    LicenseGrantRightCreateSchema, LicenseGrantRightUpdateSchema, LicenseGrantRightResponseSchema,
    PriorArtSearchCreateSchema, PriorArtSearchUpdateSchema, PriorArtSearchResponseSchema,
    InfringementMonitoringCreateSchema, InfringementMonitoringUpdateSchema, InfringementMonitoringResponseSchema,
    ExternalPatentCounselCreateSchema, ExternalPatentCounselUpdateSchema, ExternalPatentCounselResponseSchema,
    AnnuityFeeScheduleCreateSchema, AnnuityFeeScheduleUpdateSchema, AnnuityFeeScheduleResponseSchema,
    JointDevelopmentPactCreateSchema, JointDevelopmentPactUpdateSchema, JointDevelopmentPactResponseSchema,
    PatentFamilyMappingCreateSchema, PatentFamilyMappingUpdateSchema, PatentFamilyMappingResponseSchema,
    CommercialValuationCreateSchema, CommercialValuationUpdateSchema, CommercialValuationResponseSchema,
    TechnologyTransferCreateSchema, TechnologyTransferUpdateSchema, TechnologyTransferResponseSchema,
)

router = APIRouter(prefix="/intellectual_property", tags=["Intellectual Property & Patent Portfolio"])

# ==================== PatentApplication Endpoints ====================
@router.get("/patentapplications", response_model=List[Dict[str, Any]])
def list_patentapplications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PatentApplication records with pagination and filtering."""
    svc = PatentApplicationService()
    items = svc.list_patentapplications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/patentapplications/{item_id}", response_model=Dict[str, Any])
def get_patentapplication_by_id(item_id: int):
    """Retrieve detailed record for PatentApplication by ID."""
    svc = PatentApplicationService()
    item = svc.get_patentapplication_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PatentApplication with ID {item_id} not found")
    return item.to_dict()

@router.post("/patentapplications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_patentapplication(payload: PatentApplicationCreateSchema):
    """Create new PatentApplication instance in enterprise repository."""
    svc = PatentApplicationService()
    try:
        item = svc.create_patentapplication(
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

@router.put("/patentapplications/{item_id}", response_model=Dict[str, Any])
def update_patentapplication(item_id: int, payload: PatentApplicationUpdateSchema):
    """Update existing PatentApplication record fields."""
    svc = PatentApplicationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_patentapplication(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PatentApplication with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/patentapplications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patentapplication(item_id: int, hard: bool = Query(False)):
    """Delete PatentApplication record (soft-delete by default)."""
    svc = PatentApplicationService()
    ok = svc.delete_patentapplication(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PatentApplication with ID {item_id} not found")
    return None

@router.get("/patentapplications/analytics/metrics", response_model=Dict[str, Any])
def get_patentapplication_metrics():
    """Calculate summary statistical KPIs for PatentApplication collection."""
    svc = PatentApplicationService()
    return svc.calculate_aggregate_metrics()

# ==================== TrademarkRegistration Endpoints ====================
@router.get("/trademarkregistrations", response_model=List[Dict[str, Any]])
def list_trademarkregistrations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TrademarkRegistration records with pagination and filtering."""
    svc = TrademarkRegistrationService()
    items = svc.list_trademarkregistrations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/trademarkregistrations/{item_id}", response_model=Dict[str, Any])
def get_trademarkregistration_by_id(item_id: int):
    """Retrieve detailed record for TrademarkRegistration by ID."""
    svc = TrademarkRegistrationService()
    item = svc.get_trademarkregistration_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TrademarkRegistration with ID {item_id} not found")
    return item.to_dict()

@router.post("/trademarkregistrations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_trademarkregistration(payload: TrademarkRegistrationCreateSchema):
    """Create new TrademarkRegistration instance in enterprise repository."""
    svc = TrademarkRegistrationService()
    try:
        item = svc.create_trademarkregistration(
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

@router.put("/trademarkregistrations/{item_id}", response_model=Dict[str, Any])
def update_trademarkregistration(item_id: int, payload: TrademarkRegistrationUpdateSchema):
    """Update existing TrademarkRegistration record fields."""
    svc = TrademarkRegistrationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_trademarkregistration(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TrademarkRegistration with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/trademarkregistrations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trademarkregistration(item_id: int, hard: bool = Query(False)):
    """Delete TrademarkRegistration record (soft-delete by default)."""
    svc = TrademarkRegistrationService()
    ok = svc.delete_trademarkregistration(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TrademarkRegistration with ID {item_id} not found")
    return None

@router.get("/trademarkregistrations/analytics/metrics", response_model=Dict[str, Any])
def get_trademarkregistration_metrics():
    """Calculate summary statistical KPIs for TrademarkRegistration collection."""
    svc = TrademarkRegistrationService()
    return svc.calculate_aggregate_metrics()

# ==================== CopyrightFiling Endpoints ====================
@router.get("/copyrightfilings", response_model=List[Dict[str, Any]])
def list_copyrightfilings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CopyrightFiling records with pagination and filtering."""
    svc = CopyrightFilingService()
    items = svc.list_copyrightfilings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/copyrightfilings/{item_id}", response_model=Dict[str, Any])
def get_copyrightfiling_by_id(item_id: int):
    """Retrieve detailed record for CopyrightFiling by ID."""
    svc = CopyrightFilingService()
    item = svc.get_copyrightfiling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CopyrightFiling with ID {item_id} not found")
    return item.to_dict()

@router.post("/copyrightfilings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_copyrightfiling(payload: CopyrightFilingCreateSchema):
    """Create new CopyrightFiling instance in enterprise repository."""
    svc = CopyrightFilingService()
    try:
        item = svc.create_copyrightfiling(
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

@router.put("/copyrightfilings/{item_id}", response_model=Dict[str, Any])
def update_copyrightfiling(item_id: int, payload: CopyrightFilingUpdateSchema):
    """Update existing CopyrightFiling record fields."""
    svc = CopyrightFilingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_copyrightfiling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CopyrightFiling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/copyrightfilings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_copyrightfiling(item_id: int, hard: bool = Query(False)):
    """Delete CopyrightFiling record (soft-delete by default)."""
    svc = CopyrightFilingService()
    ok = svc.delete_copyrightfiling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CopyrightFiling with ID {item_id} not found")
    return None

@router.get("/copyrightfilings/analytics/metrics", response_model=Dict[str, Any])
def get_copyrightfiling_metrics():
    """Calculate summary statistical KPIs for CopyrightFiling collection."""
    svc = CopyrightFilingService()
    return svc.calculate_aggregate_metrics()

# ==================== TradeSecretInventory Endpoints ====================
@router.get("/tradesecretinventorys", response_model=List[Dict[str, Any]])
def list_tradesecretinventorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TradeSecretInventory records with pagination and filtering."""
    svc = TradeSecretInventoryService()
    items = svc.list_tradesecretinventorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tradesecretinventorys/{item_id}", response_model=Dict[str, Any])
def get_tradesecretinventory_by_id(item_id: int):
    """Retrieve detailed record for TradeSecretInventory by ID."""
    svc = TradeSecretInventoryService()
    item = svc.get_tradesecretinventory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TradeSecretInventory with ID {item_id} not found")
    return item.to_dict()

@router.post("/tradesecretinventorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tradesecretinventory(payload: TradeSecretInventoryCreateSchema):
    """Create new TradeSecretInventory instance in enterprise repository."""
    svc = TradeSecretInventoryService()
    try:
        item = svc.create_tradesecretinventory(
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

@router.put("/tradesecretinventorys/{item_id}", response_model=Dict[str, Any])
def update_tradesecretinventory(item_id: int, payload: TradeSecretInventoryUpdateSchema):
    """Update existing TradeSecretInventory record fields."""
    svc = TradeSecretInventoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tradesecretinventory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TradeSecretInventory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tradesecretinventorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tradesecretinventory(item_id: int, hard: bool = Query(False)):
    """Delete TradeSecretInventory record (soft-delete by default)."""
    svc = TradeSecretInventoryService()
    ok = svc.delete_tradesecretinventory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TradeSecretInventory with ID {item_id} not found")
    return None

@router.get("/tradesecretinventorys/analytics/metrics", response_model=Dict[str, Any])
def get_tradesecretinventory_metrics():
    """Calculate summary statistical KPIs for TradeSecretInventory collection."""
    svc = TradeSecretInventoryService()
    return svc.calculate_aggregate_metrics()

# ==================== InventionDisclosure Endpoints ====================
@router.get("/inventiondisclosures", response_model=List[Dict[str, Any]])
def list_inventiondisclosures(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InventionDisclosure records with pagination and filtering."""
    svc = InventionDisclosureService()
    items = svc.list_inventiondisclosures(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inventiondisclosures/{item_id}", response_model=Dict[str, Any])
def get_inventiondisclosure_by_id(item_id: int):
    """Retrieve detailed record for InventionDisclosure by ID."""
    svc = InventionDisclosureService()
    item = svc.get_inventiondisclosure_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InventionDisclosure with ID {item_id} not found")
    return item.to_dict()

@router.post("/inventiondisclosures", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inventiondisclosure(payload: InventionDisclosureCreateSchema):
    """Create new InventionDisclosure instance in enterprise repository."""
    svc = InventionDisclosureService()
    try:
        item = svc.create_inventiondisclosure(
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

@router.put("/inventiondisclosures/{item_id}", response_model=Dict[str, Any])
def update_inventiondisclosure(item_id: int, payload: InventionDisclosureUpdateSchema):
    """Update existing InventionDisclosure record fields."""
    svc = InventionDisclosureService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inventiondisclosure(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InventionDisclosure with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inventiondisclosures/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inventiondisclosure(item_id: int, hard: bool = Query(False)):
    """Delete InventionDisclosure record (soft-delete by default)."""
    svc = InventionDisclosureService()
    ok = svc.delete_inventiondisclosure(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InventionDisclosure with ID {item_id} not found")
    return None

@router.get("/inventiondisclosures/analytics/metrics", response_model=Dict[str, Any])
def get_inventiondisclosure_metrics():
    """Calculate summary statistical KPIs for InventionDisclosure collection."""
    svc = InventionDisclosureService()
    return svc.calculate_aggregate_metrics()

# ==================== PatentOfficeAction Endpoints ====================
@router.get("/patentofficeactions", response_model=List[Dict[str, Any]])
def list_patentofficeactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PatentOfficeAction records with pagination and filtering."""
    svc = PatentOfficeActionService()
    items = svc.list_patentofficeactions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/patentofficeactions/{item_id}", response_model=Dict[str, Any])
def get_patentofficeaction_by_id(item_id: int):
    """Retrieve detailed record for PatentOfficeAction by ID."""
    svc = PatentOfficeActionService()
    item = svc.get_patentofficeaction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PatentOfficeAction with ID {item_id} not found")
    return item.to_dict()

@router.post("/patentofficeactions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_patentofficeaction(payload: PatentOfficeActionCreateSchema):
    """Create new PatentOfficeAction instance in enterprise repository."""
    svc = PatentOfficeActionService()
    try:
        item = svc.create_patentofficeaction(
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

@router.put("/patentofficeactions/{item_id}", response_model=Dict[str, Any])
def update_patentofficeaction(item_id: int, payload: PatentOfficeActionUpdateSchema):
    """Update existing PatentOfficeAction record fields."""
    svc = PatentOfficeActionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_patentofficeaction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PatentOfficeAction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/patentofficeactions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patentofficeaction(item_id: int, hard: bool = Query(False)):
    """Delete PatentOfficeAction record (soft-delete by default)."""
    svc = PatentOfficeActionService()
    ok = svc.delete_patentofficeaction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PatentOfficeAction with ID {item_id} not found")
    return None

@router.get("/patentofficeactions/analytics/metrics", response_model=Dict[str, Any])
def get_patentofficeaction_metrics():
    """Calculate summary statistical KPIs for PatentOfficeAction collection."""
    svc = PatentOfficeActionService()
    return svc.calculate_aggregate_metrics()

# ==================== IPRoyaltyAgreement Endpoints ====================
@router.get("/iproyaltyagreements", response_model=List[Dict[str, Any]])
def list_iproyaltyagreements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IPRoyaltyAgreement records with pagination and filtering."""
    svc = IPRoyaltyAgreementService()
    items = svc.list_iproyaltyagreements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/iproyaltyagreements/{item_id}", response_model=Dict[str, Any])
def get_iproyaltyagreement_by_id(item_id: int):
    """Retrieve detailed record for IPRoyaltyAgreement by ID."""
    svc = IPRoyaltyAgreementService()
    item = svc.get_iproyaltyagreement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IPRoyaltyAgreement with ID {item_id} not found")
    return item.to_dict()

@router.post("/iproyaltyagreements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_iproyaltyagreement(payload: IPRoyaltyAgreementCreateSchema):
    """Create new IPRoyaltyAgreement instance in enterprise repository."""
    svc = IPRoyaltyAgreementService()
    try:
        item = svc.create_iproyaltyagreement(
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

@router.put("/iproyaltyagreements/{item_id}", response_model=Dict[str, Any])
def update_iproyaltyagreement(item_id: int, payload: IPRoyaltyAgreementUpdateSchema):
    """Update existing IPRoyaltyAgreement record fields."""
    svc = IPRoyaltyAgreementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_iproyaltyagreement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IPRoyaltyAgreement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/iproyaltyagreements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_iproyaltyagreement(item_id: int, hard: bool = Query(False)):
    """Delete IPRoyaltyAgreement record (soft-delete by default)."""
    svc = IPRoyaltyAgreementService()
    ok = svc.delete_iproyaltyagreement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IPRoyaltyAgreement with ID {item_id} not found")
    return None

@router.get("/iproyaltyagreements/analytics/metrics", response_model=Dict[str, Any])
def get_iproyaltyagreement_metrics():
    """Calculate summary statistical KPIs for IPRoyaltyAgreement collection."""
    svc = IPRoyaltyAgreementService()
    return svc.calculate_aggregate_metrics()

# ==================== LicenseGrantRight Endpoints ====================
@router.get("/licensegrantrights", response_model=List[Dict[str, Any]])
def list_licensegrantrights(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LicenseGrantRight records with pagination and filtering."""
    svc = LicenseGrantRightService()
    items = svc.list_licensegrantrights(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/licensegrantrights/{item_id}", response_model=Dict[str, Any])
def get_licensegrantright_by_id(item_id: int):
    """Retrieve detailed record for LicenseGrantRight by ID."""
    svc = LicenseGrantRightService()
    item = svc.get_licensegrantright_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LicenseGrantRight with ID {item_id} not found")
    return item.to_dict()

@router.post("/licensegrantrights", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_licensegrantright(payload: LicenseGrantRightCreateSchema):
    """Create new LicenseGrantRight instance in enterprise repository."""
    svc = LicenseGrantRightService()
    try:
        item = svc.create_licensegrantright(
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

@router.put("/licensegrantrights/{item_id}", response_model=Dict[str, Any])
def update_licensegrantright(item_id: int, payload: LicenseGrantRightUpdateSchema):
    """Update existing LicenseGrantRight record fields."""
    svc = LicenseGrantRightService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_licensegrantright(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LicenseGrantRight with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/licensegrantrights/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_licensegrantright(item_id: int, hard: bool = Query(False)):
    """Delete LicenseGrantRight record (soft-delete by default)."""
    svc = LicenseGrantRightService()
    ok = svc.delete_licensegrantright(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LicenseGrantRight with ID {item_id} not found")
    return None

@router.get("/licensegrantrights/analytics/metrics", response_model=Dict[str, Any])
def get_licensegrantright_metrics():
    """Calculate summary statistical KPIs for LicenseGrantRight collection."""
    svc = LicenseGrantRightService()
    return svc.calculate_aggregate_metrics()

# ==================== PriorArtSearch Endpoints ====================
@router.get("/priorartsearchs", response_model=List[Dict[str, Any]])
def list_priorartsearchs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PriorArtSearch records with pagination and filtering."""
    svc = PriorArtSearchService()
    items = svc.list_priorartsearchs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/priorartsearchs/{item_id}", response_model=Dict[str, Any])
def get_priorartsearch_by_id(item_id: int):
    """Retrieve detailed record for PriorArtSearch by ID."""
    svc = PriorArtSearchService()
    item = svc.get_priorartsearch_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PriorArtSearch with ID {item_id} not found")
    return item.to_dict()

@router.post("/priorartsearchs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_priorartsearch(payload: PriorArtSearchCreateSchema):
    """Create new PriorArtSearch instance in enterprise repository."""
    svc = PriorArtSearchService()
    try:
        item = svc.create_priorartsearch(
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

@router.put("/priorartsearchs/{item_id}", response_model=Dict[str, Any])
def update_priorartsearch(item_id: int, payload: PriorArtSearchUpdateSchema):
    """Update existing PriorArtSearch record fields."""
    svc = PriorArtSearchService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_priorartsearch(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PriorArtSearch with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/priorartsearchs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_priorartsearch(item_id: int, hard: bool = Query(False)):
    """Delete PriorArtSearch record (soft-delete by default)."""
    svc = PriorArtSearchService()
    ok = svc.delete_priorartsearch(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PriorArtSearch with ID {item_id} not found")
    return None

@router.get("/priorartsearchs/analytics/metrics", response_model=Dict[str, Any])
def get_priorartsearch_metrics():
    """Calculate summary statistical KPIs for PriorArtSearch collection."""
    svc = PriorArtSearchService()
    return svc.calculate_aggregate_metrics()

# ==================== InfringementMonitoring Endpoints ====================
@router.get("/infringementmonitorings", response_model=List[Dict[str, Any]])
def list_infringementmonitorings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InfringementMonitoring records with pagination and filtering."""
    svc = InfringementMonitoringService()
    items = svc.list_infringementmonitorings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/infringementmonitorings/{item_id}", response_model=Dict[str, Any])
def get_infringementmonitoring_by_id(item_id: int):
    """Retrieve detailed record for InfringementMonitoring by ID."""
    svc = InfringementMonitoringService()
    item = svc.get_infringementmonitoring_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InfringementMonitoring with ID {item_id} not found")
    return item.to_dict()

@router.post("/infringementmonitorings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_infringementmonitoring(payload: InfringementMonitoringCreateSchema):
    """Create new InfringementMonitoring instance in enterprise repository."""
    svc = InfringementMonitoringService()
    try:
        item = svc.create_infringementmonitoring(
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

@router.put("/infringementmonitorings/{item_id}", response_model=Dict[str, Any])
def update_infringementmonitoring(item_id: int, payload: InfringementMonitoringUpdateSchema):
    """Update existing InfringementMonitoring record fields."""
    svc = InfringementMonitoringService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_infringementmonitoring(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InfringementMonitoring with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/infringementmonitorings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_infringementmonitoring(item_id: int, hard: bool = Query(False)):
    """Delete InfringementMonitoring record (soft-delete by default)."""
    svc = InfringementMonitoringService()
    ok = svc.delete_infringementmonitoring(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InfringementMonitoring with ID {item_id} not found")
    return None

@router.get("/infringementmonitorings/analytics/metrics", response_model=Dict[str, Any])
def get_infringementmonitoring_metrics():
    """Calculate summary statistical KPIs for InfringementMonitoring collection."""
    svc = InfringementMonitoringService()
    return svc.calculate_aggregate_metrics()

# ==================== ExternalPatentCounsel Endpoints ====================
@router.get("/externalpatentcounsels", response_model=List[Dict[str, Any]])
def list_externalpatentcounsels(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExternalPatentCounsel records with pagination and filtering."""
    svc = ExternalPatentCounselService()
    items = svc.list_externalpatentcounsels(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/externalpatentcounsels/{item_id}", response_model=Dict[str, Any])
def get_externalpatentcounsel_by_id(item_id: int):
    """Retrieve detailed record for ExternalPatentCounsel by ID."""
    svc = ExternalPatentCounselService()
    item = svc.get_externalpatentcounsel_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExternalPatentCounsel with ID {item_id} not found")
    return item.to_dict()

@router.post("/externalpatentcounsels", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_externalpatentcounsel(payload: ExternalPatentCounselCreateSchema):
    """Create new ExternalPatentCounsel instance in enterprise repository."""
    svc = ExternalPatentCounselService()
    try:
        item = svc.create_externalpatentcounsel(
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

@router.put("/externalpatentcounsels/{item_id}", response_model=Dict[str, Any])
def update_externalpatentcounsel(item_id: int, payload: ExternalPatentCounselUpdateSchema):
    """Update existing ExternalPatentCounsel record fields."""
    svc = ExternalPatentCounselService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_externalpatentcounsel(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExternalPatentCounsel with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/externalpatentcounsels/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_externalpatentcounsel(item_id: int, hard: bool = Query(False)):
    """Delete ExternalPatentCounsel record (soft-delete by default)."""
    svc = ExternalPatentCounselService()
    ok = svc.delete_externalpatentcounsel(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExternalPatentCounsel with ID {item_id} not found")
    return None

@router.get("/externalpatentcounsels/analytics/metrics", response_model=Dict[str, Any])
def get_externalpatentcounsel_metrics():
    """Calculate summary statistical KPIs for ExternalPatentCounsel collection."""
    svc = ExternalPatentCounselService()
    return svc.calculate_aggregate_metrics()

# ==================== AnnuityFeeSchedule Endpoints ====================
@router.get("/annuityfeeschedules", response_model=List[Dict[str, Any]])
def list_annuityfeeschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AnnuityFeeSchedule records with pagination and filtering."""
    svc = AnnuityFeeScheduleService()
    items = svc.list_annuityfeeschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/annuityfeeschedules/{item_id}", response_model=Dict[str, Any])
def get_annuityfeeschedule_by_id(item_id: int):
    """Retrieve detailed record for AnnuityFeeSchedule by ID."""
    svc = AnnuityFeeScheduleService()
    item = svc.get_annuityfeeschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AnnuityFeeSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/annuityfeeschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_annuityfeeschedule(payload: AnnuityFeeScheduleCreateSchema):
    """Create new AnnuityFeeSchedule instance in enterprise repository."""
    svc = AnnuityFeeScheduleService()
    try:
        item = svc.create_annuityfeeschedule(
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

@router.put("/annuityfeeschedules/{item_id}", response_model=Dict[str, Any])
def update_annuityfeeschedule(item_id: int, payload: AnnuityFeeScheduleUpdateSchema):
    """Update existing AnnuityFeeSchedule record fields."""
    svc = AnnuityFeeScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_annuityfeeschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AnnuityFeeSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/annuityfeeschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_annuityfeeschedule(item_id: int, hard: bool = Query(False)):
    """Delete AnnuityFeeSchedule record (soft-delete by default)."""
    svc = AnnuityFeeScheduleService()
    ok = svc.delete_annuityfeeschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AnnuityFeeSchedule with ID {item_id} not found")
    return None

@router.get("/annuityfeeschedules/analytics/metrics", response_model=Dict[str, Any])
def get_annuityfeeschedule_metrics():
    """Calculate summary statistical KPIs for AnnuityFeeSchedule collection."""
    svc = AnnuityFeeScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== JointDevelopmentPact Endpoints ====================
@router.get("/jointdevelopmentpacts", response_model=List[Dict[str, Any]])
def list_jointdevelopmentpacts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List JointDevelopmentPact records with pagination and filtering."""
    svc = JointDevelopmentPactService()
    items = svc.list_jointdevelopmentpacts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/jointdevelopmentpacts/{item_id}", response_model=Dict[str, Any])
def get_jointdevelopmentpact_by_id(item_id: int):
    """Retrieve detailed record for JointDevelopmentPact by ID."""
    svc = JointDevelopmentPactService()
    item = svc.get_jointdevelopmentpact_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"JointDevelopmentPact with ID {item_id} not found")
    return item.to_dict()

@router.post("/jointdevelopmentpacts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_jointdevelopmentpact(payload: JointDevelopmentPactCreateSchema):
    """Create new JointDevelopmentPact instance in enterprise repository."""
    svc = JointDevelopmentPactService()
    try:
        item = svc.create_jointdevelopmentpact(
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

@router.put("/jointdevelopmentpacts/{item_id}", response_model=Dict[str, Any])
def update_jointdevelopmentpact(item_id: int, payload: JointDevelopmentPactUpdateSchema):
    """Update existing JointDevelopmentPact record fields."""
    svc = JointDevelopmentPactService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_jointdevelopmentpact(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"JointDevelopmentPact with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/jointdevelopmentpacts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_jointdevelopmentpact(item_id: int, hard: bool = Query(False)):
    """Delete JointDevelopmentPact record (soft-delete by default)."""
    svc = JointDevelopmentPactService()
    ok = svc.delete_jointdevelopmentpact(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"JointDevelopmentPact with ID {item_id} not found")
    return None

@router.get("/jointdevelopmentpacts/analytics/metrics", response_model=Dict[str, Any])
def get_jointdevelopmentpact_metrics():
    """Calculate summary statistical KPIs for JointDevelopmentPact collection."""
    svc = JointDevelopmentPactService()
    return svc.calculate_aggregate_metrics()

# ==================== PatentFamilyMapping Endpoints ====================
@router.get("/patentfamilymappings", response_model=List[Dict[str, Any]])
def list_patentfamilymappings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PatentFamilyMapping records with pagination and filtering."""
    svc = PatentFamilyMappingService()
    items = svc.list_patentfamilymappings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/patentfamilymappings/{item_id}", response_model=Dict[str, Any])
def get_patentfamilymapping_by_id(item_id: int):
    """Retrieve detailed record for PatentFamilyMapping by ID."""
    svc = PatentFamilyMappingService()
    item = svc.get_patentfamilymapping_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PatentFamilyMapping with ID {item_id} not found")
    return item.to_dict()

@router.post("/patentfamilymappings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_patentfamilymapping(payload: PatentFamilyMappingCreateSchema):
    """Create new PatentFamilyMapping instance in enterprise repository."""
    svc = PatentFamilyMappingService()
    try:
        item = svc.create_patentfamilymapping(
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

@router.put("/patentfamilymappings/{item_id}", response_model=Dict[str, Any])
def update_patentfamilymapping(item_id: int, payload: PatentFamilyMappingUpdateSchema):
    """Update existing PatentFamilyMapping record fields."""
    svc = PatentFamilyMappingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_patentfamilymapping(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PatentFamilyMapping with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/patentfamilymappings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patentfamilymapping(item_id: int, hard: bool = Query(False)):
    """Delete PatentFamilyMapping record (soft-delete by default)."""
    svc = PatentFamilyMappingService()
    ok = svc.delete_patentfamilymapping(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PatentFamilyMapping with ID {item_id} not found")
    return None

@router.get("/patentfamilymappings/analytics/metrics", response_model=Dict[str, Any])
def get_patentfamilymapping_metrics():
    """Calculate summary statistical KPIs for PatentFamilyMapping collection."""
    svc = PatentFamilyMappingService()
    return svc.calculate_aggregate_metrics()

# ==================== CommercialValuation Endpoints ====================
@router.get("/commercialvaluations", response_model=List[Dict[str, Any]])
def list_commercialvaluations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CommercialValuation records with pagination and filtering."""
    svc = CommercialValuationService()
    items = svc.list_commercialvaluations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/commercialvaluations/{item_id}", response_model=Dict[str, Any])
def get_commercialvaluation_by_id(item_id: int):
    """Retrieve detailed record for CommercialValuation by ID."""
    svc = CommercialValuationService()
    item = svc.get_commercialvaluation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CommercialValuation with ID {item_id} not found")
    return item.to_dict()

@router.post("/commercialvaluations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_commercialvaluation(payload: CommercialValuationCreateSchema):
    """Create new CommercialValuation instance in enterprise repository."""
    svc = CommercialValuationService()
    try:
        item = svc.create_commercialvaluation(
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

@router.put("/commercialvaluations/{item_id}", response_model=Dict[str, Any])
def update_commercialvaluation(item_id: int, payload: CommercialValuationUpdateSchema):
    """Update existing CommercialValuation record fields."""
    svc = CommercialValuationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_commercialvaluation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CommercialValuation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/commercialvaluations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_commercialvaluation(item_id: int, hard: bool = Query(False)):
    """Delete CommercialValuation record (soft-delete by default)."""
    svc = CommercialValuationService()
    ok = svc.delete_commercialvaluation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CommercialValuation with ID {item_id} not found")
    return None

@router.get("/commercialvaluations/analytics/metrics", response_model=Dict[str, Any])
def get_commercialvaluation_metrics():
    """Calculate summary statistical KPIs for CommercialValuation collection."""
    svc = CommercialValuationService()
    return svc.calculate_aggregate_metrics()

# ==================== TechnologyTransfer Endpoints ====================
@router.get("/technologytransfers", response_model=List[Dict[str, Any]])
def list_technologytransfers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TechnologyTransfer records with pagination and filtering."""
    svc = TechnologyTransferService()
    items = svc.list_technologytransfers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/technologytransfers/{item_id}", response_model=Dict[str, Any])
def get_technologytransfer_by_id(item_id: int):
    """Retrieve detailed record for TechnologyTransfer by ID."""
    svc = TechnologyTransferService()
    item = svc.get_technologytransfer_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TechnologyTransfer with ID {item_id} not found")
    return item.to_dict()

@router.post("/technologytransfers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_technologytransfer(payload: TechnologyTransferCreateSchema):
    """Create new TechnologyTransfer instance in enterprise repository."""
    svc = TechnologyTransferService()
    try:
        item = svc.create_technologytransfer(
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

@router.put("/technologytransfers/{item_id}", response_model=Dict[str, Any])
def update_technologytransfer(item_id: int, payload: TechnologyTransferUpdateSchema):
    """Update existing TechnologyTransfer record fields."""
    svc = TechnologyTransferService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_technologytransfer(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TechnologyTransfer with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/technologytransfers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_technologytransfer(item_id: int, hard: bool = Query(False)):
    """Delete TechnologyTransfer record (soft-delete by default)."""
    svc = TechnologyTransferService()
    ok = svc.delete_technologytransfer(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TechnologyTransfer with ID {item_id} not found")
    return None

@router.get("/technologytransfers/analytics/metrics", response_model=Dict[str, Any])
def get_technologytransfer_metrics():
    """Calculate summary statistical KPIs for TechnologyTransfer collection."""
    svc = TechnologyTransferService()
    return svc.calculate_aggregate_metrics()

