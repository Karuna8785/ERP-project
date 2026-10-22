"""
Global Trade Compliance & Customs Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    CustomsDeclarationFormService,
    HarmonizedTariffScheduleService,
    CountryOfOriginCertService,
    ExportControlClassificationService,
    SanctionPartyScreeningService,
    ImportDutyAssessmentService,
    FreeTradeAgreementClaimService,
    BondedWarehouseLogService,
    AntiDumpingMeasureService,
    CarnetGuaranteeService,
    CustomsBrokerEngagementService,
    LetterOfCreditCustomsService,
    TariffPreferenceRuleService,
    TradeDisputeFilingService,
    InspectionReleaseOrderService,
    DutyDrawbackClaimService,
)
from .schemas import (
    CustomsDeclarationFormCreateSchema, CustomsDeclarationFormUpdateSchema, CustomsDeclarationFormResponseSchema,
    HarmonizedTariffScheduleCreateSchema, HarmonizedTariffScheduleUpdateSchema, HarmonizedTariffScheduleResponseSchema,
    CountryOfOriginCertCreateSchema, CountryOfOriginCertUpdateSchema, CountryOfOriginCertResponseSchema,
    ExportControlClassificationCreateSchema, ExportControlClassificationUpdateSchema, ExportControlClassificationResponseSchema,
    SanctionPartyScreeningCreateSchema, SanctionPartyScreeningUpdateSchema, SanctionPartyScreeningResponseSchema,
    ImportDutyAssessmentCreateSchema, ImportDutyAssessmentUpdateSchema, ImportDutyAssessmentResponseSchema,
    FreeTradeAgreementClaimCreateSchema, FreeTradeAgreementClaimUpdateSchema, FreeTradeAgreementClaimResponseSchema,
    BondedWarehouseLogCreateSchema, BondedWarehouseLogUpdateSchema, BondedWarehouseLogResponseSchema,
    AntiDumpingMeasureCreateSchema, AntiDumpingMeasureUpdateSchema, AntiDumpingMeasureResponseSchema,
    CarnetGuaranteeCreateSchema, CarnetGuaranteeUpdateSchema, CarnetGuaranteeResponseSchema,
    CustomsBrokerEngagementCreateSchema, CustomsBrokerEngagementUpdateSchema, CustomsBrokerEngagementResponseSchema,
    LetterOfCreditCustomsCreateSchema, LetterOfCreditCustomsUpdateSchema, LetterOfCreditCustomsResponseSchema,
    TariffPreferenceRuleCreateSchema, TariffPreferenceRuleUpdateSchema, TariffPreferenceRuleResponseSchema,
    TradeDisputeFilingCreateSchema, TradeDisputeFilingUpdateSchema, TradeDisputeFilingResponseSchema,
    InspectionReleaseOrderCreateSchema, InspectionReleaseOrderUpdateSchema, InspectionReleaseOrderResponseSchema,
    DutyDrawbackClaimCreateSchema, DutyDrawbackClaimUpdateSchema, DutyDrawbackClaimResponseSchema,
)

router = APIRouter(prefix="/customs_trade", tags=["Global Trade Compliance & Customs Management"])

# ==================== CustomsDeclarationForm Endpoints ====================
@router.get("/customsdeclarationforms", response_model=List[Dict[str, Any]])
def list_customsdeclarationforms(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomsDeclarationForm records with pagination and filtering."""
    svc = CustomsDeclarationFormService()
    items = svc.list_customsdeclarationforms(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customsdeclarationforms/{item_id}", response_model=Dict[str, Any])
def get_customsdeclarationform_by_id(item_id: int):
    """Retrieve detailed record for CustomsDeclarationForm by ID."""
    svc = CustomsDeclarationFormService()
    item = svc.get_customsdeclarationform_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomsDeclarationForm with ID {item_id} not found")
    return item.to_dict()

@router.post("/customsdeclarationforms", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customsdeclarationform(payload: CustomsDeclarationFormCreateSchema):
    """Create new CustomsDeclarationForm instance in enterprise repository."""
    svc = CustomsDeclarationFormService()
    try:
        item = svc.create_customsdeclarationform(
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

@router.put("/customsdeclarationforms/{item_id}", response_model=Dict[str, Any])
def update_customsdeclarationform(item_id: int, payload: CustomsDeclarationFormUpdateSchema):
    """Update existing CustomsDeclarationForm record fields."""
    svc = CustomsDeclarationFormService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customsdeclarationform(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomsDeclarationForm with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customsdeclarationforms/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customsdeclarationform(item_id: int, hard: bool = Query(False)):
    """Delete CustomsDeclarationForm record (soft-delete by default)."""
    svc = CustomsDeclarationFormService()
    ok = svc.delete_customsdeclarationform(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomsDeclarationForm with ID {item_id} not found")
    return None

@router.get("/customsdeclarationforms/analytics/metrics", response_model=Dict[str, Any])
def get_customsdeclarationform_metrics():
    """Calculate summary statistical KPIs for CustomsDeclarationForm collection."""
    svc = CustomsDeclarationFormService()
    return svc.calculate_aggregate_metrics()

# ==================== HarmonizedTariffSchedule Endpoints ====================
@router.get("/harmonizedtariffschedules", response_model=List[Dict[str, Any]])
def list_harmonizedtariffschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HarmonizedTariffSchedule records with pagination and filtering."""
    svc = HarmonizedTariffScheduleService()
    items = svc.list_harmonizedtariffschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/harmonizedtariffschedules/{item_id}", response_model=Dict[str, Any])
def get_harmonizedtariffschedule_by_id(item_id: int):
    """Retrieve detailed record for HarmonizedTariffSchedule by ID."""
    svc = HarmonizedTariffScheduleService()
    item = svc.get_harmonizedtariffschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HarmonizedTariffSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/harmonizedtariffschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_harmonizedtariffschedule(payload: HarmonizedTariffScheduleCreateSchema):
    """Create new HarmonizedTariffSchedule instance in enterprise repository."""
    svc = HarmonizedTariffScheduleService()
    try:
        item = svc.create_harmonizedtariffschedule(
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

@router.put("/harmonizedtariffschedules/{item_id}", response_model=Dict[str, Any])
def update_harmonizedtariffschedule(item_id: int, payload: HarmonizedTariffScheduleUpdateSchema):
    """Update existing HarmonizedTariffSchedule record fields."""
    svc = HarmonizedTariffScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_harmonizedtariffschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HarmonizedTariffSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/harmonizedtariffschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_harmonizedtariffschedule(item_id: int, hard: bool = Query(False)):
    """Delete HarmonizedTariffSchedule record (soft-delete by default)."""
    svc = HarmonizedTariffScheduleService()
    ok = svc.delete_harmonizedtariffschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HarmonizedTariffSchedule with ID {item_id} not found")
    return None

@router.get("/harmonizedtariffschedules/analytics/metrics", response_model=Dict[str, Any])
def get_harmonizedtariffschedule_metrics():
    """Calculate summary statistical KPIs for HarmonizedTariffSchedule collection."""
    svc = HarmonizedTariffScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== CountryOfOriginCert Endpoints ====================
@router.get("/countryoforigincerts", response_model=List[Dict[str, Any]])
def list_countryoforigincerts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CountryOfOriginCert records with pagination and filtering."""
    svc = CountryOfOriginCertService()
    items = svc.list_countryoforigincerts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/countryoforigincerts/{item_id}", response_model=Dict[str, Any])
def get_countryoforigincert_by_id(item_id: int):
    """Retrieve detailed record for CountryOfOriginCert by ID."""
    svc = CountryOfOriginCertService()
    item = svc.get_countryoforigincert_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CountryOfOriginCert with ID {item_id} not found")
    return item.to_dict()

@router.post("/countryoforigincerts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_countryoforigincert(payload: CountryOfOriginCertCreateSchema):
    """Create new CountryOfOriginCert instance in enterprise repository."""
    svc = CountryOfOriginCertService()
    try:
        item = svc.create_countryoforigincert(
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

@router.put("/countryoforigincerts/{item_id}", response_model=Dict[str, Any])
def update_countryoforigincert(item_id: int, payload: CountryOfOriginCertUpdateSchema):
    """Update existing CountryOfOriginCert record fields."""
    svc = CountryOfOriginCertService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_countryoforigincert(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CountryOfOriginCert with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/countryoforigincerts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_countryoforigincert(item_id: int, hard: bool = Query(False)):
    """Delete CountryOfOriginCert record (soft-delete by default)."""
    svc = CountryOfOriginCertService()
    ok = svc.delete_countryoforigincert(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CountryOfOriginCert with ID {item_id} not found")
    return None

@router.get("/countryoforigincerts/analytics/metrics", response_model=Dict[str, Any])
def get_countryoforigincert_metrics():
    """Calculate summary statistical KPIs for CountryOfOriginCert collection."""
    svc = CountryOfOriginCertService()
    return svc.calculate_aggregate_metrics()

# ==================== ExportControlClassification Endpoints ====================
@router.get("/exportcontrolclassifications", response_model=List[Dict[str, Any]])
def list_exportcontrolclassifications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExportControlClassification records with pagination and filtering."""
    svc = ExportControlClassificationService()
    items = svc.list_exportcontrolclassifications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/exportcontrolclassifications/{item_id}", response_model=Dict[str, Any])
def get_exportcontrolclassification_by_id(item_id: int):
    """Retrieve detailed record for ExportControlClassification by ID."""
    svc = ExportControlClassificationService()
    item = svc.get_exportcontrolclassification_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExportControlClassification with ID {item_id} not found")
    return item.to_dict()

@router.post("/exportcontrolclassifications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_exportcontrolclassification(payload: ExportControlClassificationCreateSchema):
    """Create new ExportControlClassification instance in enterprise repository."""
    svc = ExportControlClassificationService()
    try:
        item = svc.create_exportcontrolclassification(
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

@router.put("/exportcontrolclassifications/{item_id}", response_model=Dict[str, Any])
def update_exportcontrolclassification(item_id: int, payload: ExportControlClassificationUpdateSchema):
    """Update existing ExportControlClassification record fields."""
    svc = ExportControlClassificationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_exportcontrolclassification(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExportControlClassification with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/exportcontrolclassifications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exportcontrolclassification(item_id: int, hard: bool = Query(False)):
    """Delete ExportControlClassification record (soft-delete by default)."""
    svc = ExportControlClassificationService()
    ok = svc.delete_exportcontrolclassification(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExportControlClassification with ID {item_id} not found")
    return None

@router.get("/exportcontrolclassifications/analytics/metrics", response_model=Dict[str, Any])
def get_exportcontrolclassification_metrics():
    """Calculate summary statistical KPIs for ExportControlClassification collection."""
    svc = ExportControlClassificationService()
    return svc.calculate_aggregate_metrics()

# ==================== SanctionPartyScreening Endpoints ====================
@router.get("/sanctionpartyscreenings", response_model=List[Dict[str, Any]])
def list_sanctionpartyscreenings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SanctionPartyScreening records with pagination and filtering."""
    svc = SanctionPartyScreeningService()
    items = svc.list_sanctionpartyscreenings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sanctionpartyscreenings/{item_id}", response_model=Dict[str, Any])
def get_sanctionpartyscreening_by_id(item_id: int):
    """Retrieve detailed record for SanctionPartyScreening by ID."""
    svc = SanctionPartyScreeningService()
    item = svc.get_sanctionpartyscreening_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SanctionPartyScreening with ID {item_id} not found")
    return item.to_dict()

@router.post("/sanctionpartyscreenings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sanctionpartyscreening(payload: SanctionPartyScreeningCreateSchema):
    """Create new SanctionPartyScreening instance in enterprise repository."""
    svc = SanctionPartyScreeningService()
    try:
        item = svc.create_sanctionpartyscreening(
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

@router.put("/sanctionpartyscreenings/{item_id}", response_model=Dict[str, Any])
def update_sanctionpartyscreening(item_id: int, payload: SanctionPartyScreeningUpdateSchema):
    """Update existing SanctionPartyScreening record fields."""
    svc = SanctionPartyScreeningService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sanctionpartyscreening(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SanctionPartyScreening with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sanctionpartyscreenings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sanctionpartyscreening(item_id: int, hard: bool = Query(False)):
    """Delete SanctionPartyScreening record (soft-delete by default)."""
    svc = SanctionPartyScreeningService()
    ok = svc.delete_sanctionpartyscreening(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SanctionPartyScreening with ID {item_id} not found")
    return None

@router.get("/sanctionpartyscreenings/analytics/metrics", response_model=Dict[str, Any])
def get_sanctionpartyscreening_metrics():
    """Calculate summary statistical KPIs for SanctionPartyScreening collection."""
    svc = SanctionPartyScreeningService()
    return svc.calculate_aggregate_metrics()

# ==================== ImportDutyAssessment Endpoints ====================
@router.get("/importdutyassessments", response_model=List[Dict[str, Any]])
def list_importdutyassessments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ImportDutyAssessment records with pagination and filtering."""
    svc = ImportDutyAssessmentService()
    items = svc.list_importdutyassessments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/importdutyassessments/{item_id}", response_model=Dict[str, Any])
def get_importdutyassessment_by_id(item_id: int):
    """Retrieve detailed record for ImportDutyAssessment by ID."""
    svc = ImportDutyAssessmentService()
    item = svc.get_importdutyassessment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ImportDutyAssessment with ID {item_id} not found")
    return item.to_dict()

@router.post("/importdutyassessments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_importdutyassessment(payload: ImportDutyAssessmentCreateSchema):
    """Create new ImportDutyAssessment instance in enterprise repository."""
    svc = ImportDutyAssessmentService()
    try:
        item = svc.create_importdutyassessment(
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

@router.put("/importdutyassessments/{item_id}", response_model=Dict[str, Any])
def update_importdutyassessment(item_id: int, payload: ImportDutyAssessmentUpdateSchema):
    """Update existing ImportDutyAssessment record fields."""
    svc = ImportDutyAssessmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_importdutyassessment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ImportDutyAssessment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/importdutyassessments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_importdutyassessment(item_id: int, hard: bool = Query(False)):
    """Delete ImportDutyAssessment record (soft-delete by default)."""
    svc = ImportDutyAssessmentService()
    ok = svc.delete_importdutyassessment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ImportDutyAssessment with ID {item_id} not found")
    return None

@router.get("/importdutyassessments/analytics/metrics", response_model=Dict[str, Any])
def get_importdutyassessment_metrics():
    """Calculate summary statistical KPIs for ImportDutyAssessment collection."""
    svc = ImportDutyAssessmentService()
    return svc.calculate_aggregate_metrics()

# ==================== FreeTradeAgreementClaim Endpoints ====================
@router.get("/freetradeagreementclaims", response_model=List[Dict[str, Any]])
def list_freetradeagreementclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FreeTradeAgreementClaim records with pagination and filtering."""
    svc = FreeTradeAgreementClaimService()
    items = svc.list_freetradeagreementclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/freetradeagreementclaims/{item_id}", response_model=Dict[str, Any])
def get_freetradeagreementclaim_by_id(item_id: int):
    """Retrieve detailed record for FreeTradeAgreementClaim by ID."""
    svc = FreeTradeAgreementClaimService()
    item = svc.get_freetradeagreementclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FreeTradeAgreementClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/freetradeagreementclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_freetradeagreementclaim(payload: FreeTradeAgreementClaimCreateSchema):
    """Create new FreeTradeAgreementClaim instance in enterprise repository."""
    svc = FreeTradeAgreementClaimService()
    try:
        item = svc.create_freetradeagreementclaim(
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

@router.put("/freetradeagreementclaims/{item_id}", response_model=Dict[str, Any])
def update_freetradeagreementclaim(item_id: int, payload: FreeTradeAgreementClaimUpdateSchema):
    """Update existing FreeTradeAgreementClaim record fields."""
    svc = FreeTradeAgreementClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_freetradeagreementclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FreeTradeAgreementClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/freetradeagreementclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_freetradeagreementclaim(item_id: int, hard: bool = Query(False)):
    """Delete FreeTradeAgreementClaim record (soft-delete by default)."""
    svc = FreeTradeAgreementClaimService()
    ok = svc.delete_freetradeagreementclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FreeTradeAgreementClaim with ID {item_id} not found")
    return None

@router.get("/freetradeagreementclaims/analytics/metrics", response_model=Dict[str, Any])
def get_freetradeagreementclaim_metrics():
    """Calculate summary statistical KPIs for FreeTradeAgreementClaim collection."""
    svc = FreeTradeAgreementClaimService()
    return svc.calculate_aggregate_metrics()

# ==================== BondedWarehouseLog Endpoints ====================
@router.get("/bondedwarehouselogs", response_model=List[Dict[str, Any]])
def list_bondedwarehouselogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BondedWarehouseLog records with pagination and filtering."""
    svc = BondedWarehouseLogService()
    items = svc.list_bondedwarehouselogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bondedwarehouselogs/{item_id}", response_model=Dict[str, Any])
def get_bondedwarehouselog_by_id(item_id: int):
    """Retrieve detailed record for BondedWarehouseLog by ID."""
    svc = BondedWarehouseLogService()
    item = svc.get_bondedwarehouselog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BondedWarehouseLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/bondedwarehouselogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bondedwarehouselog(payload: BondedWarehouseLogCreateSchema):
    """Create new BondedWarehouseLog instance in enterprise repository."""
    svc = BondedWarehouseLogService()
    try:
        item = svc.create_bondedwarehouselog(
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

@router.put("/bondedwarehouselogs/{item_id}", response_model=Dict[str, Any])
def update_bondedwarehouselog(item_id: int, payload: BondedWarehouseLogUpdateSchema):
    """Update existing BondedWarehouseLog record fields."""
    svc = BondedWarehouseLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bondedwarehouselog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BondedWarehouseLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bondedwarehouselogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bondedwarehouselog(item_id: int, hard: bool = Query(False)):
    """Delete BondedWarehouseLog record (soft-delete by default)."""
    svc = BondedWarehouseLogService()
    ok = svc.delete_bondedwarehouselog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BondedWarehouseLog with ID {item_id} not found")
    return None

@router.get("/bondedwarehouselogs/analytics/metrics", response_model=Dict[str, Any])
def get_bondedwarehouselog_metrics():
    """Calculate summary statistical KPIs for BondedWarehouseLog collection."""
    svc = BondedWarehouseLogService()
    return svc.calculate_aggregate_metrics()

# ==================== AntiDumpingMeasure Endpoints ====================
@router.get("/antidumpingmeasures", response_model=List[Dict[str, Any]])
def list_antidumpingmeasures(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AntiDumpingMeasure records with pagination and filtering."""
    svc = AntiDumpingMeasureService()
    items = svc.list_antidumpingmeasures(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/antidumpingmeasures/{item_id}", response_model=Dict[str, Any])
def get_antidumpingmeasure_by_id(item_id: int):
    """Retrieve detailed record for AntiDumpingMeasure by ID."""
    svc = AntiDumpingMeasureService()
    item = svc.get_antidumpingmeasure_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AntiDumpingMeasure with ID {item_id} not found")
    return item.to_dict()

@router.post("/antidumpingmeasures", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_antidumpingmeasure(payload: AntiDumpingMeasureCreateSchema):
    """Create new AntiDumpingMeasure instance in enterprise repository."""
    svc = AntiDumpingMeasureService()
    try:
        item = svc.create_antidumpingmeasure(
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

@router.put("/antidumpingmeasures/{item_id}", response_model=Dict[str, Any])
def update_antidumpingmeasure(item_id: int, payload: AntiDumpingMeasureUpdateSchema):
    """Update existing AntiDumpingMeasure record fields."""
    svc = AntiDumpingMeasureService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_antidumpingmeasure(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AntiDumpingMeasure with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/antidumpingmeasures/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_antidumpingmeasure(item_id: int, hard: bool = Query(False)):
    """Delete AntiDumpingMeasure record (soft-delete by default)."""
    svc = AntiDumpingMeasureService()
    ok = svc.delete_antidumpingmeasure(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AntiDumpingMeasure with ID {item_id} not found")
    return None

@router.get("/antidumpingmeasures/analytics/metrics", response_model=Dict[str, Any])
def get_antidumpingmeasure_metrics():
    """Calculate summary statistical KPIs for AntiDumpingMeasure collection."""
    svc = AntiDumpingMeasureService()
    return svc.calculate_aggregate_metrics()

# ==================== CarnetGuarantee Endpoints ====================
@router.get("/carnetguarantees", response_model=List[Dict[str, Any]])
def list_carnetguarantees(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CarnetGuarantee records with pagination and filtering."""
    svc = CarnetGuaranteeService()
    items = svc.list_carnetguarantees(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/carnetguarantees/{item_id}", response_model=Dict[str, Any])
def get_carnetguarantee_by_id(item_id: int):
    """Retrieve detailed record for CarnetGuarantee by ID."""
    svc = CarnetGuaranteeService()
    item = svc.get_carnetguarantee_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CarnetGuarantee with ID {item_id} not found")
    return item.to_dict()

@router.post("/carnetguarantees", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_carnetguarantee(payload: CarnetGuaranteeCreateSchema):
    """Create new CarnetGuarantee instance in enterprise repository."""
    svc = CarnetGuaranteeService()
    try:
        item = svc.create_carnetguarantee(
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

@router.put("/carnetguarantees/{item_id}", response_model=Dict[str, Any])
def update_carnetguarantee(item_id: int, payload: CarnetGuaranteeUpdateSchema):
    """Update existing CarnetGuarantee record fields."""
    svc = CarnetGuaranteeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_carnetguarantee(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CarnetGuarantee with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/carnetguarantees/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carnetguarantee(item_id: int, hard: bool = Query(False)):
    """Delete CarnetGuarantee record (soft-delete by default)."""
    svc = CarnetGuaranteeService()
    ok = svc.delete_carnetguarantee(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CarnetGuarantee with ID {item_id} not found")
    return None

@router.get("/carnetguarantees/analytics/metrics", response_model=Dict[str, Any])
def get_carnetguarantee_metrics():
    """Calculate summary statistical KPIs for CarnetGuarantee collection."""
    svc = CarnetGuaranteeService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomsBrokerEngagement Endpoints ====================
@router.get("/customsbrokerengagements", response_model=List[Dict[str, Any]])
def list_customsbrokerengagements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomsBrokerEngagement records with pagination and filtering."""
    svc = CustomsBrokerEngagementService()
    items = svc.list_customsbrokerengagements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customsbrokerengagements/{item_id}", response_model=Dict[str, Any])
def get_customsbrokerengagement_by_id(item_id: int):
    """Retrieve detailed record for CustomsBrokerEngagement by ID."""
    svc = CustomsBrokerEngagementService()
    item = svc.get_customsbrokerengagement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomsBrokerEngagement with ID {item_id} not found")
    return item.to_dict()

@router.post("/customsbrokerengagements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customsbrokerengagement(payload: CustomsBrokerEngagementCreateSchema):
    """Create new CustomsBrokerEngagement instance in enterprise repository."""
    svc = CustomsBrokerEngagementService()
    try:
        item = svc.create_customsbrokerengagement(
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

@router.put("/customsbrokerengagements/{item_id}", response_model=Dict[str, Any])
def update_customsbrokerengagement(item_id: int, payload: CustomsBrokerEngagementUpdateSchema):
    """Update existing CustomsBrokerEngagement record fields."""
    svc = CustomsBrokerEngagementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customsbrokerengagement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomsBrokerEngagement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customsbrokerengagements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customsbrokerengagement(item_id: int, hard: bool = Query(False)):
    """Delete CustomsBrokerEngagement record (soft-delete by default)."""
    svc = CustomsBrokerEngagementService()
    ok = svc.delete_customsbrokerengagement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomsBrokerEngagement with ID {item_id} not found")
    return None

@router.get("/customsbrokerengagements/analytics/metrics", response_model=Dict[str, Any])
def get_customsbrokerengagement_metrics():
    """Calculate summary statistical KPIs for CustomsBrokerEngagement collection."""
    svc = CustomsBrokerEngagementService()
    return svc.calculate_aggregate_metrics()

# ==================== LetterOfCreditCustoms Endpoints ====================
@router.get("/letterofcreditcustomss", response_model=List[Dict[str, Any]])
def list_letterofcreditcustomss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LetterOfCreditCustoms records with pagination and filtering."""
    svc = LetterOfCreditCustomsService()
    items = svc.list_letterofcreditcustomss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/letterofcreditcustomss/{item_id}", response_model=Dict[str, Any])
def get_letterofcreditcustoms_by_id(item_id: int):
    """Retrieve detailed record for LetterOfCreditCustoms by ID."""
    svc = LetterOfCreditCustomsService()
    item = svc.get_letterofcreditcustoms_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LetterOfCreditCustoms with ID {item_id} not found")
    return item.to_dict()

@router.post("/letterofcreditcustomss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_letterofcreditcustoms(payload: LetterOfCreditCustomsCreateSchema):
    """Create new LetterOfCreditCustoms instance in enterprise repository."""
    svc = LetterOfCreditCustomsService()
    try:
        item = svc.create_letterofcreditcustoms(
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

@router.put("/letterofcreditcustomss/{item_id}", response_model=Dict[str, Any])
def update_letterofcreditcustoms(item_id: int, payload: LetterOfCreditCustomsUpdateSchema):
    """Update existing LetterOfCreditCustoms record fields."""
    svc = LetterOfCreditCustomsService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_letterofcreditcustoms(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LetterOfCreditCustoms with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/letterofcreditcustomss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_letterofcreditcustoms(item_id: int, hard: bool = Query(False)):
    """Delete LetterOfCreditCustoms record (soft-delete by default)."""
    svc = LetterOfCreditCustomsService()
    ok = svc.delete_letterofcreditcustoms(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LetterOfCreditCustoms with ID {item_id} not found")
    return None

@router.get("/letterofcreditcustomss/analytics/metrics", response_model=Dict[str, Any])
def get_letterofcreditcustoms_metrics():
    """Calculate summary statistical KPIs for LetterOfCreditCustoms collection."""
    svc = LetterOfCreditCustomsService()
    return svc.calculate_aggregate_metrics()

# ==================== TariffPreferenceRule Endpoints ====================
@router.get("/tariffpreferencerules", response_model=List[Dict[str, Any]])
def list_tariffpreferencerules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TariffPreferenceRule records with pagination and filtering."""
    svc = TariffPreferenceRuleService()
    items = svc.list_tariffpreferencerules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tariffpreferencerules/{item_id}", response_model=Dict[str, Any])
def get_tariffpreferencerule_by_id(item_id: int):
    """Retrieve detailed record for TariffPreferenceRule by ID."""
    svc = TariffPreferenceRuleService()
    item = svc.get_tariffpreferencerule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TariffPreferenceRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/tariffpreferencerules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tariffpreferencerule(payload: TariffPreferenceRuleCreateSchema):
    """Create new TariffPreferenceRule instance in enterprise repository."""
    svc = TariffPreferenceRuleService()
    try:
        item = svc.create_tariffpreferencerule(
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

@router.put("/tariffpreferencerules/{item_id}", response_model=Dict[str, Any])
def update_tariffpreferencerule(item_id: int, payload: TariffPreferenceRuleUpdateSchema):
    """Update existing TariffPreferenceRule record fields."""
    svc = TariffPreferenceRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tariffpreferencerule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TariffPreferenceRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tariffpreferencerules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tariffpreferencerule(item_id: int, hard: bool = Query(False)):
    """Delete TariffPreferenceRule record (soft-delete by default)."""
    svc = TariffPreferenceRuleService()
    ok = svc.delete_tariffpreferencerule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TariffPreferenceRule with ID {item_id} not found")
    return None

@router.get("/tariffpreferencerules/analytics/metrics", response_model=Dict[str, Any])
def get_tariffpreferencerule_metrics():
    """Calculate summary statistical KPIs for TariffPreferenceRule collection."""
    svc = TariffPreferenceRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== TradeDisputeFiling Endpoints ====================
@router.get("/tradedisputefilings", response_model=List[Dict[str, Any]])
def list_tradedisputefilings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TradeDisputeFiling records with pagination and filtering."""
    svc = TradeDisputeFilingService()
    items = svc.list_tradedisputefilings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/tradedisputefilings/{item_id}", response_model=Dict[str, Any])
def get_tradedisputefiling_by_id(item_id: int):
    """Retrieve detailed record for TradeDisputeFiling by ID."""
    svc = TradeDisputeFilingService()
    item = svc.get_tradedisputefiling_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TradeDisputeFiling with ID {item_id} not found")
    return item.to_dict()

@router.post("/tradedisputefilings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_tradedisputefiling(payload: TradeDisputeFilingCreateSchema):
    """Create new TradeDisputeFiling instance in enterprise repository."""
    svc = TradeDisputeFilingService()
    try:
        item = svc.create_tradedisputefiling(
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

@router.put("/tradedisputefilings/{item_id}", response_model=Dict[str, Any])
def update_tradedisputefiling(item_id: int, payload: TradeDisputeFilingUpdateSchema):
    """Update existing TradeDisputeFiling record fields."""
    svc = TradeDisputeFilingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_tradedisputefiling(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TradeDisputeFiling with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/tradedisputefilings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tradedisputefiling(item_id: int, hard: bool = Query(False)):
    """Delete TradeDisputeFiling record (soft-delete by default)."""
    svc = TradeDisputeFilingService()
    ok = svc.delete_tradedisputefiling(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TradeDisputeFiling with ID {item_id} not found")
    return None

@router.get("/tradedisputefilings/analytics/metrics", response_model=Dict[str, Any])
def get_tradedisputefiling_metrics():
    """Calculate summary statistical KPIs for TradeDisputeFiling collection."""
    svc = TradeDisputeFilingService()
    return svc.calculate_aggregate_metrics()

# ==================== InspectionReleaseOrder Endpoints ====================
@router.get("/inspectionreleaseorders", response_model=List[Dict[str, Any]])
def list_inspectionreleaseorders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InspectionReleaseOrder records with pagination and filtering."""
    svc = InspectionReleaseOrderService()
    items = svc.list_inspectionreleaseorders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/inspectionreleaseorders/{item_id}", response_model=Dict[str, Any])
def get_inspectionreleaseorder_by_id(item_id: int):
    """Retrieve detailed record for InspectionReleaseOrder by ID."""
    svc = InspectionReleaseOrderService()
    item = svc.get_inspectionreleaseorder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InspectionReleaseOrder with ID {item_id} not found")
    return item.to_dict()

@router.post("/inspectionreleaseorders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_inspectionreleaseorder(payload: InspectionReleaseOrderCreateSchema):
    """Create new InspectionReleaseOrder instance in enterprise repository."""
    svc = InspectionReleaseOrderService()
    try:
        item = svc.create_inspectionreleaseorder(
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

@router.put("/inspectionreleaseorders/{item_id}", response_model=Dict[str, Any])
def update_inspectionreleaseorder(item_id: int, payload: InspectionReleaseOrderUpdateSchema):
    """Update existing InspectionReleaseOrder record fields."""
    svc = InspectionReleaseOrderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_inspectionreleaseorder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InspectionReleaseOrder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/inspectionreleaseorders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inspectionreleaseorder(item_id: int, hard: bool = Query(False)):
    """Delete InspectionReleaseOrder record (soft-delete by default)."""
    svc = InspectionReleaseOrderService()
    ok = svc.delete_inspectionreleaseorder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InspectionReleaseOrder with ID {item_id} not found")
    return None

@router.get("/inspectionreleaseorders/analytics/metrics", response_model=Dict[str, Any])
def get_inspectionreleaseorder_metrics():
    """Calculate summary statistical KPIs for InspectionReleaseOrder collection."""
    svc = InspectionReleaseOrderService()
    return svc.calculate_aggregate_metrics()

# ==================== DutyDrawbackClaim Endpoints ====================
@router.get("/dutydrawbackclaims", response_model=List[Dict[str, Any]])
def list_dutydrawbackclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DutyDrawbackClaim records with pagination and filtering."""
    svc = DutyDrawbackClaimService()
    items = svc.list_dutydrawbackclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dutydrawbackclaims/{item_id}", response_model=Dict[str, Any])
def get_dutydrawbackclaim_by_id(item_id: int):
    """Retrieve detailed record for DutyDrawbackClaim by ID."""
    svc = DutyDrawbackClaimService()
    item = svc.get_dutydrawbackclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DutyDrawbackClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/dutydrawbackclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dutydrawbackclaim(payload: DutyDrawbackClaimCreateSchema):
    """Create new DutyDrawbackClaim instance in enterprise repository."""
    svc = DutyDrawbackClaimService()
    try:
        item = svc.create_dutydrawbackclaim(
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

@router.put("/dutydrawbackclaims/{item_id}", response_model=Dict[str, Any])
def update_dutydrawbackclaim(item_id: int, payload: DutyDrawbackClaimUpdateSchema):
    """Update existing DutyDrawbackClaim record fields."""
    svc = DutyDrawbackClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dutydrawbackclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DutyDrawbackClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dutydrawbackclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dutydrawbackclaim(item_id: int, hard: bool = Query(False)):
    """Delete DutyDrawbackClaim record (soft-delete by default)."""
    svc = DutyDrawbackClaimService()
    ok = svc.delete_dutydrawbackclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DutyDrawbackClaim with ID {item_id} not found")
    return None

@router.get("/dutydrawbackclaims/analytics/metrics", response_model=Dict[str, Any])
def get_dutydrawbackclaim_metrics():
    """Calculate summary statistical KPIs for DutyDrawbackClaim collection."""
    svc = DutyDrawbackClaimService()
    return svc.calculate_aggregate_metrics()

