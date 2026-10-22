"""
Global Tax Determination & Reporting - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    TaxJurisdictionService,
    TaxRateScheduleService,
    TaxExemptionCertificateService,
    HSNSACCodeMasterService,
    CrossBorderTariffRuleService,
    ReverseChargeProvisionService,
    TDSWithholdingCategoryService,
    TaxInvoiceHeaderService,
    TaxInvoiceLineItemService,
    InputTaxCreditLedgerService,
    MonthlyTaxReturnGSTRService,
    AnnualTaxReconciliationService,
    TaxAuditTrailService,
    EWayBillRecordService,
    EInvoiceIRNRegistryService,
    TaxPenaltyNoticeService,
)
from .schemas import (
    TaxJurisdictionCreateSchema, TaxJurisdictionUpdateSchema, TaxJurisdictionResponseSchema,
    TaxRateScheduleCreateSchema, TaxRateScheduleUpdateSchema, TaxRateScheduleResponseSchema,
    TaxExemptionCertificateCreateSchema, TaxExemptionCertificateUpdateSchema, TaxExemptionCertificateResponseSchema,
    HSNSACCodeMasterCreateSchema, HSNSACCodeMasterUpdateSchema, HSNSACCodeMasterResponseSchema,
    CrossBorderTariffRuleCreateSchema, CrossBorderTariffRuleUpdateSchema, CrossBorderTariffRuleResponseSchema,
    ReverseChargeProvisionCreateSchema, ReverseChargeProvisionUpdateSchema, ReverseChargeProvisionResponseSchema,
    TDSWithholdingCategoryCreateSchema, TDSWithholdingCategoryUpdateSchema, TDSWithholdingCategoryResponseSchema,
    TaxInvoiceHeaderCreateSchema, TaxInvoiceHeaderUpdateSchema, TaxInvoiceHeaderResponseSchema,
    TaxInvoiceLineItemCreateSchema, TaxInvoiceLineItemUpdateSchema, TaxInvoiceLineItemResponseSchema,
    InputTaxCreditLedgerCreateSchema, InputTaxCreditLedgerUpdateSchema, InputTaxCreditLedgerResponseSchema,
    MonthlyTaxReturnGSTRCreateSchema, MonthlyTaxReturnGSTRUpdateSchema, MonthlyTaxReturnGSTRResponseSchema,
    AnnualTaxReconciliationCreateSchema, AnnualTaxReconciliationUpdateSchema, AnnualTaxReconciliationResponseSchema,
    TaxAuditTrailCreateSchema, TaxAuditTrailUpdateSchema, TaxAuditTrailResponseSchema,
    EWayBillRecordCreateSchema, EWayBillRecordUpdateSchema, EWayBillRecordResponseSchema,
    EInvoiceIRNRegistryCreateSchema, EInvoiceIRNRegistryUpdateSchema, EInvoiceIRNRegistryResponseSchema,
    TaxPenaltyNoticeCreateSchema, TaxPenaltyNoticeUpdateSchema, TaxPenaltyNoticeResponseSchema,
)

router = APIRouter(prefix="/tax_engine", tags=["Global Tax Determination & Reporting"])

# ==================== TaxJurisdiction Endpoints ====================
@router.get("/taxjurisdictions", response_model=List[Dict[str, Any]])
def list_taxjurisdictions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxJurisdiction records with pagination and filtering."""
    svc = TaxJurisdictionService()
    items = svc.list_taxjurisdictions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxjurisdictions/{item_id}", response_model=Dict[str, Any])
def get_taxjurisdiction_by_id(item_id: int):
    """Retrieve detailed record for TaxJurisdiction by ID."""
    svc = TaxJurisdictionService()
    item = svc.get_taxjurisdiction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxJurisdiction with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxjurisdictions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxjurisdiction(payload: TaxJurisdictionCreateSchema):
    """Create new TaxJurisdiction instance in enterprise repository."""
    svc = TaxJurisdictionService()
    try:
        item = svc.create_taxjurisdiction(
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

@router.put("/taxjurisdictions/{item_id}", response_model=Dict[str, Any])
def update_taxjurisdiction(item_id: int, payload: TaxJurisdictionUpdateSchema):
    """Update existing TaxJurisdiction record fields."""
    svc = TaxJurisdictionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxjurisdiction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxJurisdiction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxjurisdictions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxjurisdiction(item_id: int, hard: bool = Query(False)):
    """Delete TaxJurisdiction record (soft-delete by default)."""
    svc = TaxJurisdictionService()
    ok = svc.delete_taxjurisdiction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxJurisdiction with ID {item_id} not found")
    return None

@router.get("/taxjurisdictions/analytics/metrics", response_model=Dict[str, Any])
def get_taxjurisdiction_metrics():
    """Calculate summary statistical KPIs for TaxJurisdiction collection."""
    svc = TaxJurisdictionService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxRateSchedule Endpoints ====================
@router.get("/taxrateschedules", response_model=List[Dict[str, Any]])
def list_taxrateschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxRateSchedule records with pagination and filtering."""
    svc = TaxRateScheduleService()
    items = svc.list_taxrateschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxrateschedules/{item_id}", response_model=Dict[str, Any])
def get_taxrateschedule_by_id(item_id: int):
    """Retrieve detailed record for TaxRateSchedule by ID."""
    svc = TaxRateScheduleService()
    item = svc.get_taxrateschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxRateSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxrateschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxrateschedule(payload: TaxRateScheduleCreateSchema):
    """Create new TaxRateSchedule instance in enterprise repository."""
    svc = TaxRateScheduleService()
    try:
        item = svc.create_taxrateschedule(
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

@router.put("/taxrateschedules/{item_id}", response_model=Dict[str, Any])
def update_taxrateschedule(item_id: int, payload: TaxRateScheduleUpdateSchema):
    """Update existing TaxRateSchedule record fields."""
    svc = TaxRateScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxrateschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxRateSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxrateschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxrateschedule(item_id: int, hard: bool = Query(False)):
    """Delete TaxRateSchedule record (soft-delete by default)."""
    svc = TaxRateScheduleService()
    ok = svc.delete_taxrateschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxRateSchedule with ID {item_id} not found")
    return None

@router.get("/taxrateschedules/analytics/metrics", response_model=Dict[str, Any])
def get_taxrateschedule_metrics():
    """Calculate summary statistical KPIs for TaxRateSchedule collection."""
    svc = TaxRateScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxExemptionCertificate Endpoints ====================
@router.get("/taxexemptioncertificates", response_model=List[Dict[str, Any]])
def list_taxexemptioncertificates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxExemptionCertificate records with pagination and filtering."""
    svc = TaxExemptionCertificateService()
    items = svc.list_taxexemptioncertificates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxexemptioncertificates/{item_id}", response_model=Dict[str, Any])
def get_taxexemptioncertificate_by_id(item_id: int):
    """Retrieve detailed record for TaxExemptionCertificate by ID."""
    svc = TaxExemptionCertificateService()
    item = svc.get_taxexemptioncertificate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxExemptionCertificate with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxexemptioncertificates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxexemptioncertificate(payload: TaxExemptionCertificateCreateSchema):
    """Create new TaxExemptionCertificate instance in enterprise repository."""
    svc = TaxExemptionCertificateService()
    try:
        item = svc.create_taxexemptioncertificate(
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

@router.put("/taxexemptioncertificates/{item_id}", response_model=Dict[str, Any])
def update_taxexemptioncertificate(item_id: int, payload: TaxExemptionCertificateUpdateSchema):
    """Update existing TaxExemptionCertificate record fields."""
    svc = TaxExemptionCertificateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxexemptioncertificate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxExemptionCertificate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxexemptioncertificates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxexemptioncertificate(item_id: int, hard: bool = Query(False)):
    """Delete TaxExemptionCertificate record (soft-delete by default)."""
    svc = TaxExemptionCertificateService()
    ok = svc.delete_taxexemptioncertificate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxExemptionCertificate with ID {item_id} not found")
    return None

@router.get("/taxexemptioncertificates/analytics/metrics", response_model=Dict[str, Any])
def get_taxexemptioncertificate_metrics():
    """Calculate summary statistical KPIs for TaxExemptionCertificate collection."""
    svc = TaxExemptionCertificateService()
    return svc.calculate_aggregate_metrics()

# ==================== HSNSACCodeMaster Endpoints ====================
@router.get("/hsnsaccodemasters", response_model=List[Dict[str, Any]])
def list_hsnsaccodemasters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HSNSACCodeMaster records with pagination and filtering."""
    svc = HSNSACCodeMasterService()
    items = svc.list_hsnsaccodemasters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hsnsaccodemasters/{item_id}", response_model=Dict[str, Any])
def get_hsnsaccodemaster_by_id(item_id: int):
    """Retrieve detailed record for HSNSACCodeMaster by ID."""
    svc = HSNSACCodeMasterService()
    item = svc.get_hsnsaccodemaster_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HSNSACCodeMaster with ID {item_id} not found")
    return item.to_dict()

@router.post("/hsnsaccodemasters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hsnsaccodemaster(payload: HSNSACCodeMasterCreateSchema):
    """Create new HSNSACCodeMaster instance in enterprise repository."""
    svc = HSNSACCodeMasterService()
    try:
        item = svc.create_hsnsaccodemaster(
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

@router.put("/hsnsaccodemasters/{item_id}", response_model=Dict[str, Any])
def update_hsnsaccodemaster(item_id: int, payload: HSNSACCodeMasterUpdateSchema):
    """Update existing HSNSACCodeMaster record fields."""
    svc = HSNSACCodeMasterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hsnsaccodemaster(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HSNSACCodeMaster with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hsnsaccodemasters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hsnsaccodemaster(item_id: int, hard: bool = Query(False)):
    """Delete HSNSACCodeMaster record (soft-delete by default)."""
    svc = HSNSACCodeMasterService()
    ok = svc.delete_hsnsaccodemaster(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HSNSACCodeMaster with ID {item_id} not found")
    return None

@router.get("/hsnsaccodemasters/analytics/metrics", response_model=Dict[str, Any])
def get_hsnsaccodemaster_metrics():
    """Calculate summary statistical KPIs for HSNSACCodeMaster collection."""
    svc = HSNSACCodeMasterService()
    return svc.calculate_aggregate_metrics()

# ==================== CrossBorderTariffRule Endpoints ====================
@router.get("/crossbordertariffrules", response_model=List[Dict[str, Any]])
def list_crossbordertariffrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CrossBorderTariffRule records with pagination and filtering."""
    svc = CrossBorderTariffRuleService()
    items = svc.list_crossbordertariffrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/crossbordertariffrules/{item_id}", response_model=Dict[str, Any])
def get_crossbordertariffrule_by_id(item_id: int):
    """Retrieve detailed record for CrossBorderTariffRule by ID."""
    svc = CrossBorderTariffRuleService()
    item = svc.get_crossbordertariffrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CrossBorderTariffRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/crossbordertariffrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_crossbordertariffrule(payload: CrossBorderTariffRuleCreateSchema):
    """Create new CrossBorderTariffRule instance in enterprise repository."""
    svc = CrossBorderTariffRuleService()
    try:
        item = svc.create_crossbordertariffrule(
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

@router.put("/crossbordertariffrules/{item_id}", response_model=Dict[str, Any])
def update_crossbordertariffrule(item_id: int, payload: CrossBorderTariffRuleUpdateSchema):
    """Update existing CrossBorderTariffRule record fields."""
    svc = CrossBorderTariffRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_crossbordertariffrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CrossBorderTariffRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/crossbordertariffrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_crossbordertariffrule(item_id: int, hard: bool = Query(False)):
    """Delete CrossBorderTariffRule record (soft-delete by default)."""
    svc = CrossBorderTariffRuleService()
    ok = svc.delete_crossbordertariffrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CrossBorderTariffRule with ID {item_id} not found")
    return None

@router.get("/crossbordertariffrules/analytics/metrics", response_model=Dict[str, Any])
def get_crossbordertariffrule_metrics():
    """Calculate summary statistical KPIs for CrossBorderTariffRule collection."""
    svc = CrossBorderTariffRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== ReverseChargeProvision Endpoints ====================
@router.get("/reversechargeprovisions", response_model=List[Dict[str, Any]])
def list_reversechargeprovisions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ReverseChargeProvision records with pagination and filtering."""
    svc = ReverseChargeProvisionService()
    items = svc.list_reversechargeprovisions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/reversechargeprovisions/{item_id}", response_model=Dict[str, Any])
def get_reversechargeprovision_by_id(item_id: int):
    """Retrieve detailed record for ReverseChargeProvision by ID."""
    svc = ReverseChargeProvisionService()
    item = svc.get_reversechargeprovision_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ReverseChargeProvision with ID {item_id} not found")
    return item.to_dict()

@router.post("/reversechargeprovisions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_reversechargeprovision(payload: ReverseChargeProvisionCreateSchema):
    """Create new ReverseChargeProvision instance in enterprise repository."""
    svc = ReverseChargeProvisionService()
    try:
        item = svc.create_reversechargeprovision(
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

@router.put("/reversechargeprovisions/{item_id}", response_model=Dict[str, Any])
def update_reversechargeprovision(item_id: int, payload: ReverseChargeProvisionUpdateSchema):
    """Update existing ReverseChargeProvision record fields."""
    svc = ReverseChargeProvisionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_reversechargeprovision(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ReverseChargeProvision with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/reversechargeprovisions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reversechargeprovision(item_id: int, hard: bool = Query(False)):
    """Delete ReverseChargeProvision record (soft-delete by default)."""
    svc = ReverseChargeProvisionService()
    ok = svc.delete_reversechargeprovision(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ReverseChargeProvision with ID {item_id} not found")
    return None

@router.get("/reversechargeprovisions/analytics/metrics", response_model=Dict[str, Any])
def get_reversechargeprovision_metrics():
    """Calculate summary statistical KPIs for ReverseChargeProvision collection."""
    svc = ReverseChargeProvisionService()
    return svc.calculate_aggregate_metrics()

# ==================== TDSWithholdingCategory Endpoints ====================
@router.get("/tdswithholdingcategorys", response_model=List[Dict[str, Any]])
def list_tdswithholdingcategorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TDSWithholdingCategory records with pagination and filtering."""
    svc = TDSWithholdingCategoryService()
    items = svc.list_tdswithholdingcategorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tdswithholdingcategorys/{item_id}", response_model=Dict[str, Any])
def get_tdswithholdingcategory_by_id(item_id: int):
    """Retrieve detailed record for TDSWithholdingCategory by ID."""
    svc = TDSWithholdingCategoryService()
    item = svc.get_tdswithholdingcategory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TDSWithholdingCategory with ID {item_id} not found")
    return item.to_dict()

@router.post("/tdswithholdingcategorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tdswithholdingcategory(payload: TDSWithholdingCategoryCreateSchema):
    """Create new TDSWithholdingCategory instance in enterprise repository."""
    svc = TDSWithholdingCategoryService()
    try:
        item = svc.create_tdswithholdingcategory(
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

@router.put("/tdswithholdingcategorys/{item_id}", response_model=Dict[str, Any])
def update_tdswithholdingcategory(item_id: int, payload: TDSWithholdingCategoryUpdateSchema):
    """Update existing TDSWithholdingCategory record fields."""
    svc = TDSWithholdingCategoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tdswithholdingcategory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TDSWithholdingCategory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tdswithholdingcategorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tdswithholdingcategory(item_id: int, hard: bool = Query(False)):
    """Delete TDSWithholdingCategory record (soft-delete by default)."""
    svc = TDSWithholdingCategoryService()
    ok = svc.delete_tdswithholdingcategory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TDSWithholdingCategory with ID {item_id} not found")
    return None

@router.get("/tdswithholdingcategorys/analytics/metrics", response_model=Dict[str, Any])
def get_tdswithholdingcategory_metrics():
    """Calculate summary statistical KPIs for TDSWithholdingCategory collection."""
    svc = TDSWithholdingCategoryService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxInvoiceHeader Endpoints ====================
@router.get("/taxinvoiceheaders", response_model=List[Dict[str, Any]])
def list_taxinvoiceheaders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxInvoiceHeader records with pagination and filtering."""
    svc = TaxInvoiceHeaderService()
    items = svc.list_taxinvoiceheaders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxinvoiceheaders/{item_id}", response_model=Dict[str, Any])
def get_taxinvoiceheader_by_id(item_id: int):
    """Retrieve detailed record for TaxInvoiceHeader by ID."""
    svc = TaxInvoiceHeaderService()
    item = svc.get_taxinvoiceheader_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxInvoiceHeader with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxinvoiceheaders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxinvoiceheader(payload: TaxInvoiceHeaderCreateSchema):
    """Create new TaxInvoiceHeader instance in enterprise repository."""
    svc = TaxInvoiceHeaderService()
    try:
        item = svc.create_taxinvoiceheader(
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

@router.put("/taxinvoiceheaders/{item_id}", response_model=Dict[str, Any])
def update_taxinvoiceheader(item_id: int, payload: TaxInvoiceHeaderUpdateSchema):
    """Update existing TaxInvoiceHeader record fields."""
    svc = TaxInvoiceHeaderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxinvoiceheader(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxInvoiceHeader with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxinvoiceheaders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxinvoiceheader(item_id: int, hard: bool = Query(False)):
    """Delete TaxInvoiceHeader record (soft-delete by default)."""
    svc = TaxInvoiceHeaderService()
    ok = svc.delete_taxinvoiceheader(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxInvoiceHeader with ID {item_id} not found")
    return None

@router.get("/taxinvoiceheaders/analytics/metrics", response_model=Dict[str, Any])
def get_taxinvoiceheader_metrics():
    """Calculate summary statistical KPIs for TaxInvoiceHeader collection."""
    svc = TaxInvoiceHeaderService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxInvoiceLineItem Endpoints ====================
@router.get("/taxinvoicelineitems", response_model=List[Dict[str, Any]])
def list_taxinvoicelineitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxInvoiceLineItem records with pagination and filtering."""
    svc = TaxInvoiceLineItemService()
    items = svc.list_taxinvoicelineitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxinvoicelineitems/{item_id}", response_model=Dict[str, Any])
def get_taxinvoicelineitem_by_id(item_id: int):
    """Retrieve detailed record for TaxInvoiceLineItem by ID."""
    svc = TaxInvoiceLineItemService()
    item = svc.get_taxinvoicelineitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxInvoiceLineItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxinvoicelineitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxinvoicelineitem(payload: TaxInvoiceLineItemCreateSchema):
    """Create new TaxInvoiceLineItem instance in enterprise repository."""
    svc = TaxInvoiceLineItemService()
    try:
        item = svc.create_taxinvoicelineitem(
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

@router.put("/taxinvoicelineitems/{item_id}", response_model=Dict[str, Any])
def update_taxinvoicelineitem(item_id: int, payload: TaxInvoiceLineItemUpdateSchema):
    """Update existing TaxInvoiceLineItem record fields."""
    svc = TaxInvoiceLineItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxinvoicelineitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxInvoiceLineItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxinvoicelineitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxinvoicelineitem(item_id: int, hard: bool = Query(False)):
    """Delete TaxInvoiceLineItem record (soft-delete by default)."""
    svc = TaxInvoiceLineItemService()
    ok = svc.delete_taxinvoicelineitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxInvoiceLineItem with ID {item_id} not found")
    return None

@router.get("/taxinvoicelineitems/analytics/metrics", response_model=Dict[str, Any])
def get_taxinvoicelineitem_metrics():
    """Calculate summary statistical KPIs for TaxInvoiceLineItem collection."""
    svc = TaxInvoiceLineItemService()
    return svc.calculate_aggregate_metrics()

# ==================== InputTaxCreditLedger Endpoints ====================
@router.get("/inputtaxcreditledgers", response_model=List[Dict[str, Any]])
def list_inputtaxcreditledgers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InputTaxCreditLedger records with pagination and filtering."""
    svc = InputTaxCreditLedgerService()
    items = svc.list_inputtaxcreditledgers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inputtaxcreditledgers/{item_id}", response_model=Dict[str, Any])
def get_inputtaxcreditledger_by_id(item_id: int):
    """Retrieve detailed record for InputTaxCreditLedger by ID."""
    svc = InputTaxCreditLedgerService()
    item = svc.get_inputtaxcreditledger_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InputTaxCreditLedger with ID {item_id} not found")
    return item.to_dict()

@router.post("/inputtaxcreditledgers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inputtaxcreditledger(payload: InputTaxCreditLedgerCreateSchema):
    """Create new InputTaxCreditLedger instance in enterprise repository."""
    svc = InputTaxCreditLedgerService()
    try:
        item = svc.create_inputtaxcreditledger(
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

@router.put("/inputtaxcreditledgers/{item_id}", response_model=Dict[str, Any])
def update_inputtaxcreditledger(item_id: int, payload: InputTaxCreditLedgerUpdateSchema):
    """Update existing InputTaxCreditLedger record fields."""
    svc = InputTaxCreditLedgerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inputtaxcreditledger(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InputTaxCreditLedger with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inputtaxcreditledgers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inputtaxcreditledger(item_id: int, hard: bool = Query(False)):
    """Delete InputTaxCreditLedger record (soft-delete by default)."""
    svc = InputTaxCreditLedgerService()
    ok = svc.delete_inputtaxcreditledger(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InputTaxCreditLedger with ID {item_id} not found")
    return None

@router.get("/inputtaxcreditledgers/analytics/metrics", response_model=Dict[str, Any])
def get_inputtaxcreditledger_metrics():
    """Calculate summary statistical KPIs for InputTaxCreditLedger collection."""
    svc = InputTaxCreditLedgerService()
    return svc.calculate_aggregate_metrics()

# ==================== MonthlyTaxReturnGSTR Endpoints ====================
@router.get("/monthlytaxreturngstrs", response_model=List[Dict[str, Any]])
def list_monthlytaxreturngstrs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MonthlyTaxReturnGSTR records with pagination and filtering."""
    svc = MonthlyTaxReturnGSTRService()
    items = svc.list_monthlytaxreturngstrs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/monthlytaxreturngstrs/{item_id}", response_model=Dict[str, Any])
def get_monthlytaxreturngstr_by_id(item_id: int):
    """Retrieve detailed record for MonthlyTaxReturnGSTR by ID."""
    svc = MonthlyTaxReturnGSTRService()
    item = svc.get_monthlytaxreturngstr_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MonthlyTaxReturnGSTR with ID {item_id} not found")
    return item.to_dict()

@router.post("/monthlytaxreturngstrs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_monthlytaxreturngstr(payload: MonthlyTaxReturnGSTRCreateSchema):
    """Create new MonthlyTaxReturnGSTR instance in enterprise repository."""
    svc = MonthlyTaxReturnGSTRService()
    try:
        item = svc.create_monthlytaxreturngstr(
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

@router.put("/monthlytaxreturngstrs/{item_id}", response_model=Dict[str, Any])
def update_monthlytaxreturngstr(item_id: int, payload: MonthlyTaxReturnGSTRUpdateSchema):
    """Update existing MonthlyTaxReturnGSTR record fields."""
    svc = MonthlyTaxReturnGSTRService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_monthlytaxreturngstr(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MonthlyTaxReturnGSTR with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/monthlytaxreturngstrs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_monthlytaxreturngstr(item_id: int, hard: bool = Query(False)):
    """Delete MonthlyTaxReturnGSTR record (soft-delete by default)."""
    svc = MonthlyTaxReturnGSTRService()
    ok = svc.delete_monthlytaxreturngstr(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MonthlyTaxReturnGSTR with ID {item_id} not found")
    return None

@router.get("/monthlytaxreturngstrs/analytics/metrics", response_model=Dict[str, Any])
def get_monthlytaxreturngstr_metrics():
    """Calculate summary statistical KPIs for MonthlyTaxReturnGSTR collection."""
    svc = MonthlyTaxReturnGSTRService()
    return svc.calculate_aggregate_metrics()

# ==================== AnnualTaxReconciliation Endpoints ====================
@router.get("/annualtaxreconciliations", response_model=List[Dict[str, Any]])
def list_annualtaxreconciliations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AnnualTaxReconciliation records with pagination and filtering."""
    svc = AnnualTaxReconciliationService()
    items = svc.list_annualtaxreconciliations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/annualtaxreconciliations/{item_id}", response_model=Dict[str, Any])
def get_annualtaxreconciliation_by_id(item_id: int):
    """Retrieve detailed record for AnnualTaxReconciliation by ID."""
    svc = AnnualTaxReconciliationService()
    item = svc.get_annualtaxreconciliation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AnnualTaxReconciliation with ID {item_id} not found")
    return item.to_dict()

@router.post("/annualtaxreconciliations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_annualtaxreconciliation(payload: AnnualTaxReconciliationCreateSchema):
    """Create new AnnualTaxReconciliation instance in enterprise repository."""
    svc = AnnualTaxReconciliationService()
    try:
        item = svc.create_annualtaxreconciliation(
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

@router.put("/annualtaxreconciliations/{item_id}", response_model=Dict[str, Any])
def update_annualtaxreconciliation(item_id: int, payload: AnnualTaxReconciliationUpdateSchema):
    """Update existing AnnualTaxReconciliation record fields."""
    svc = AnnualTaxReconciliationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_annualtaxreconciliation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AnnualTaxReconciliation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/annualtaxreconciliations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_annualtaxreconciliation(item_id: int, hard: bool = Query(False)):
    """Delete AnnualTaxReconciliation record (soft-delete by default)."""
    svc = AnnualTaxReconciliationService()
    ok = svc.delete_annualtaxreconciliation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AnnualTaxReconciliation with ID {item_id} not found")
    return None

@router.get("/annualtaxreconciliations/analytics/metrics", response_model=Dict[str, Any])
def get_annualtaxreconciliation_metrics():
    """Calculate summary statistical KPIs for AnnualTaxReconciliation collection."""
    svc = AnnualTaxReconciliationService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxAuditTrail Endpoints ====================
@router.get("/taxaudittrails", response_model=List[Dict[str, Any]])
def list_taxaudittrails(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxAuditTrail records with pagination and filtering."""
    svc = TaxAuditTrailService()
    items = svc.list_taxaudittrails(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxaudittrails/{item_id}", response_model=Dict[str, Any])
def get_taxaudittrail_by_id(item_id: int):
    """Retrieve detailed record for TaxAuditTrail by ID."""
    svc = TaxAuditTrailService()
    item = svc.get_taxaudittrail_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxAuditTrail with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxaudittrails", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxaudittrail(payload: TaxAuditTrailCreateSchema):
    """Create new TaxAuditTrail instance in enterprise repository."""
    svc = TaxAuditTrailService()
    try:
        item = svc.create_taxaudittrail(
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

@router.put("/taxaudittrails/{item_id}", response_model=Dict[str, Any])
def update_taxaudittrail(item_id: int, payload: TaxAuditTrailUpdateSchema):
    """Update existing TaxAuditTrail record fields."""
    svc = TaxAuditTrailService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxaudittrail(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxAuditTrail with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxaudittrails/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxaudittrail(item_id: int, hard: bool = Query(False)):
    """Delete TaxAuditTrail record (soft-delete by default)."""
    svc = TaxAuditTrailService()
    ok = svc.delete_taxaudittrail(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxAuditTrail with ID {item_id} not found")
    return None

@router.get("/taxaudittrails/analytics/metrics", response_model=Dict[str, Any])
def get_taxaudittrail_metrics():
    """Calculate summary statistical KPIs for TaxAuditTrail collection."""
    svc = TaxAuditTrailService()
    return svc.calculate_aggregate_metrics()

# ==================== EWayBillRecord Endpoints ====================
@router.get("/ewaybillrecords", response_model=List[Dict[str, Any]])
def list_ewaybillrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EWayBillRecord records with pagination and filtering."""
    svc = EWayBillRecordService()
    items = svc.list_ewaybillrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ewaybillrecords/{item_id}", response_model=Dict[str, Any])
def get_ewaybillrecord_by_id(item_id: int):
    """Retrieve detailed record for EWayBillRecord by ID."""
    svc = EWayBillRecordService()
    item = svc.get_ewaybillrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EWayBillRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/ewaybillrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ewaybillrecord(payload: EWayBillRecordCreateSchema):
    """Create new EWayBillRecord instance in enterprise repository."""
    svc = EWayBillRecordService()
    try:
        item = svc.create_ewaybillrecord(
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

@router.put("/ewaybillrecords/{item_id}", response_model=Dict[str, Any])
def update_ewaybillrecord(item_id: int, payload: EWayBillRecordUpdateSchema):
    """Update existing EWayBillRecord record fields."""
    svc = EWayBillRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ewaybillrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EWayBillRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ewaybillrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ewaybillrecord(item_id: int, hard: bool = Query(False)):
    """Delete EWayBillRecord record (soft-delete by default)."""
    svc = EWayBillRecordService()
    ok = svc.delete_ewaybillrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EWayBillRecord with ID {item_id} not found")
    return None

@router.get("/ewaybillrecords/analytics/metrics", response_model=Dict[str, Any])
def get_ewaybillrecord_metrics():
    """Calculate summary statistical KPIs for EWayBillRecord collection."""
    svc = EWayBillRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== EInvoiceIRNRegistry Endpoints ====================
@router.get("/einvoiceirnregistrys", response_model=List[Dict[str, Any]])
def list_einvoiceirnregistrys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EInvoiceIRNRegistry records with pagination and filtering."""
    svc = EInvoiceIRNRegistryService()
    items = svc.list_einvoiceirnregistrys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/einvoiceirnregistrys/{item_id}", response_model=Dict[str, Any])
def get_einvoiceirnregistry_by_id(item_id: int):
    """Retrieve detailed record for EInvoiceIRNRegistry by ID."""
    svc = EInvoiceIRNRegistryService()
    item = svc.get_einvoiceirnregistry_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EInvoiceIRNRegistry with ID {item_id} not found")
    return item.to_dict()

@router.post("/einvoiceirnregistrys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_einvoiceirnregistry(payload: EInvoiceIRNRegistryCreateSchema):
    """Create new EInvoiceIRNRegistry instance in enterprise repository."""
    svc = EInvoiceIRNRegistryService()
    try:
        item = svc.create_einvoiceirnregistry(
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

@router.put("/einvoiceirnregistrys/{item_id}", response_model=Dict[str, Any])
def update_einvoiceirnregistry(item_id: int, payload: EInvoiceIRNRegistryUpdateSchema):
    """Update existing EInvoiceIRNRegistry record fields."""
    svc = EInvoiceIRNRegistryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_einvoiceirnregistry(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EInvoiceIRNRegistry with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/einvoiceirnregistrys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_einvoiceirnregistry(item_id: int, hard: bool = Query(False)):
    """Delete EInvoiceIRNRegistry record (soft-delete by default)."""
    svc = EInvoiceIRNRegistryService()
    ok = svc.delete_einvoiceirnregistry(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EInvoiceIRNRegistry with ID {item_id} not found")
    return None

@router.get("/einvoiceirnregistrys/analytics/metrics", response_model=Dict[str, Any])
def get_einvoiceirnregistry_metrics():
    """Calculate summary statistical KPIs for EInvoiceIRNRegistry collection."""
    svc = EInvoiceIRNRegistryService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxPenaltyNotice Endpoints ====================
@router.get("/taxpenaltynotices", response_model=List[Dict[str, Any]])
def list_taxpenaltynotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxPenaltyNotice records with pagination and filtering."""
    svc = TaxPenaltyNoticeService()
    items = svc.list_taxpenaltynotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxpenaltynotices/{item_id}", response_model=Dict[str, Any])
def get_taxpenaltynotice_by_id(item_id: int):
    """Retrieve detailed record for TaxPenaltyNotice by ID."""
    svc = TaxPenaltyNoticeService()
    item = svc.get_taxpenaltynotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxPenaltyNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxpenaltynotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxpenaltynotice(payload: TaxPenaltyNoticeCreateSchema):
    """Create new TaxPenaltyNotice instance in enterprise repository."""
    svc = TaxPenaltyNoticeService()
    try:
        item = svc.create_taxpenaltynotice(
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

@router.put("/taxpenaltynotices/{item_id}", response_model=Dict[str, Any])
def update_taxpenaltynotice(item_id: int, payload: TaxPenaltyNoticeUpdateSchema):
    """Update existing TaxPenaltyNotice record fields."""
    svc = TaxPenaltyNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxpenaltynotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxPenaltyNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxpenaltynotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxpenaltynotice(item_id: int, hard: bool = Query(False)):
    """Delete TaxPenaltyNotice record (soft-delete by default)."""
    svc = TaxPenaltyNoticeService()
    ok = svc.delete_taxpenaltynotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxPenaltyNotice with ID {item_id} not found")
    return None

@router.get("/taxpenaltynotices/analytics/metrics", response_model=Dict[str, Any])
def get_taxpenaltynotice_metrics():
    """Calculate summary statistical KPIs for TaxPenaltyNotice collection."""
    svc = TaxPenaltyNoticeService()
    return svc.calculate_aggregate_metrics()

