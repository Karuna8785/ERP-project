"""
Employee Total Rewards & Benefits Administration - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    BenefitPlanDefinitionService,
    EmployeeEnrollmentRecordService,
    HealthInsurancePolicyService,
    RetirementPensionFundService,
    WellnessReimbursementService,
    LifeInsuranceCoverageService,
    FlexibleSpendingAccountService,
    DependentBeneficiaryService,
    BenefitClaimSubmissionService,
    DeductionPayrollMapService,
    OpenEnrollmentWindowService,
    CarrierBillingReconcileService,
    COBRAContinuationLogService,
    EmployeeAssistanceProgService,
    VoluntaryBenefitOptionService,
    BenefitCostAnalyticsService,
)
from .schemas import (
    BenefitPlanDefinitionCreateSchema, BenefitPlanDefinitionUpdateSchema, BenefitPlanDefinitionResponseSchema,
    EmployeeEnrollmentRecordCreateSchema, EmployeeEnrollmentRecordUpdateSchema, EmployeeEnrollmentRecordResponseSchema,
    HealthInsurancePolicyCreateSchema, HealthInsurancePolicyUpdateSchema, HealthInsurancePolicyResponseSchema,
    RetirementPensionFundCreateSchema, RetirementPensionFundUpdateSchema, RetirementPensionFundResponseSchema,
    WellnessReimbursementCreateSchema, WellnessReimbursementUpdateSchema, WellnessReimbursementResponseSchema,
    LifeInsuranceCoverageCreateSchema, LifeInsuranceCoverageUpdateSchema, LifeInsuranceCoverageResponseSchema,
    FlexibleSpendingAccountCreateSchema, FlexibleSpendingAccountUpdateSchema, FlexibleSpendingAccountResponseSchema,
    DependentBeneficiaryCreateSchema, DependentBeneficiaryUpdateSchema, DependentBeneficiaryResponseSchema,
    BenefitClaimSubmissionCreateSchema, BenefitClaimSubmissionUpdateSchema, BenefitClaimSubmissionResponseSchema,
    DeductionPayrollMapCreateSchema, DeductionPayrollMapUpdateSchema, DeductionPayrollMapResponseSchema,
    OpenEnrollmentWindowCreateSchema, OpenEnrollmentWindowUpdateSchema, OpenEnrollmentWindowResponseSchema,
    CarrierBillingReconcileCreateSchema, CarrierBillingReconcileUpdateSchema, CarrierBillingReconcileResponseSchema,
    COBRAContinuationLogCreateSchema, COBRAContinuationLogUpdateSchema, COBRAContinuationLogResponseSchema,
    EmployeeAssistanceProgCreateSchema, EmployeeAssistanceProgUpdateSchema, EmployeeAssistanceProgResponseSchema,
    VoluntaryBenefitOptionCreateSchema, VoluntaryBenefitOptionUpdateSchema, VoluntaryBenefitOptionResponseSchema,
    BenefitCostAnalyticsCreateSchema, BenefitCostAnalyticsUpdateSchema, BenefitCostAnalyticsResponseSchema,
)

router = APIRouter(prefix="/employee_benefits", tags=["Employee Total Rewards & Benefits Administration"])

# ==================== BenefitPlanDefinition Endpoints ====================
@router.get("/benefitplandefinitions", response_model=List[Dict[str, Any]])
def list_benefitplandefinitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BenefitPlanDefinition records with pagination and filtering."""
    svc = BenefitPlanDefinitionService()
    items = svc.list_benefitplandefinitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/benefitplandefinitions/{item_id}", response_model=Dict[str, Any])
def get_benefitplandefinition_by_id(item_id: int):
    """Retrieve detailed record for BenefitPlanDefinition by ID."""
    svc = BenefitPlanDefinitionService()
    item = svc.get_benefitplandefinition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BenefitPlanDefinition with ID {item_id} not found")
    return item.to_dict()

@router.post("/benefitplandefinitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_benefitplandefinition(payload: BenefitPlanDefinitionCreateSchema):
    """Create new BenefitPlanDefinition instance in enterprise repository."""
    svc = BenefitPlanDefinitionService()
    try:
        item = svc.create_benefitplandefinition(
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

@router.put("/benefitplandefinitions/{item_id}", response_model=Dict[str, Any])
def update_benefitplandefinition(item_id: int, payload: BenefitPlanDefinitionUpdateSchema):
    """Update existing BenefitPlanDefinition record fields."""
    svc = BenefitPlanDefinitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_benefitplandefinition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BenefitPlanDefinition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/benefitplandefinitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_benefitplandefinition(item_id: int, hard: bool = Query(False)):
    """Delete BenefitPlanDefinition record (soft-delete by default)."""
    svc = BenefitPlanDefinitionService()
    ok = svc.delete_benefitplandefinition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BenefitPlanDefinition with ID {item_id} not found")
    return None

@router.get("/benefitplandefinitions/analytics/metrics", response_model=Dict[str, Any])
def get_benefitplandefinition_metrics():
    """Calculate summary statistical KPIs for BenefitPlanDefinition collection."""
    svc = BenefitPlanDefinitionService()
    return svc.calculate_aggregate_metrics()

# ==================== EmployeeEnrollmentRecord Endpoints ====================
@router.get("/employeeenrollmentrecords", response_model=List[Dict[str, Any]])
def list_employeeenrollmentrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmployeeEnrollmentRecord records with pagination and filtering."""
    svc = EmployeeEnrollmentRecordService()
    items = svc.list_employeeenrollmentrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/employeeenrollmentrecords/{item_id}", response_model=Dict[str, Any])
def get_employeeenrollmentrecord_by_id(item_id: int):
    """Retrieve detailed record for EmployeeEnrollmentRecord by ID."""
    svc = EmployeeEnrollmentRecordService()
    item = svc.get_employeeenrollmentrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmployeeEnrollmentRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/employeeenrollmentrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_employeeenrollmentrecord(payload: EmployeeEnrollmentRecordCreateSchema):
    """Create new EmployeeEnrollmentRecord instance in enterprise repository."""
    svc = EmployeeEnrollmentRecordService()
    try:
        item = svc.create_employeeenrollmentrecord(
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

@router.put("/employeeenrollmentrecords/{item_id}", response_model=Dict[str, Any])
def update_employeeenrollmentrecord(item_id: int, payload: EmployeeEnrollmentRecordUpdateSchema):
    """Update existing EmployeeEnrollmentRecord record fields."""
    svc = EmployeeEnrollmentRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_employeeenrollmentrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmployeeEnrollmentRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/employeeenrollmentrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employeeenrollmentrecord(item_id: int, hard: bool = Query(False)):
    """Delete EmployeeEnrollmentRecord record (soft-delete by default)."""
    svc = EmployeeEnrollmentRecordService()
    ok = svc.delete_employeeenrollmentrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmployeeEnrollmentRecord with ID {item_id} not found")
    return None

@router.get("/employeeenrollmentrecords/analytics/metrics", response_model=Dict[str, Any])
def get_employeeenrollmentrecord_metrics():
    """Calculate summary statistical KPIs for EmployeeEnrollmentRecord collection."""
    svc = EmployeeEnrollmentRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== HealthInsurancePolicy Endpoints ====================
@router.get("/healthinsurancepolicys", response_model=List[Dict[str, Any]])
def list_healthinsurancepolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HealthInsurancePolicy records with pagination and filtering."""
    svc = HealthInsurancePolicyService()
    items = svc.list_healthinsurancepolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/healthinsurancepolicys/{item_id}", response_model=Dict[str, Any])
def get_healthinsurancepolicy_by_id(item_id: int):
    """Retrieve detailed record for HealthInsurancePolicy by ID."""
    svc = HealthInsurancePolicyService()
    item = svc.get_healthinsurancepolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HealthInsurancePolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/healthinsurancepolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_healthinsurancepolicy(payload: HealthInsurancePolicyCreateSchema):
    """Create new HealthInsurancePolicy instance in enterprise repository."""
    svc = HealthInsurancePolicyService()
    try:
        item = svc.create_healthinsurancepolicy(
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

@router.put("/healthinsurancepolicys/{item_id}", response_model=Dict[str, Any])
def update_healthinsurancepolicy(item_id: int, payload: HealthInsurancePolicyUpdateSchema):
    """Update existing HealthInsurancePolicy record fields."""
    svc = HealthInsurancePolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_healthinsurancepolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HealthInsurancePolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/healthinsurancepolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_healthinsurancepolicy(item_id: int, hard: bool = Query(False)):
    """Delete HealthInsurancePolicy record (soft-delete by default)."""
    svc = HealthInsurancePolicyService()
    ok = svc.delete_healthinsurancepolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HealthInsurancePolicy with ID {item_id} not found")
    return None

@router.get("/healthinsurancepolicys/analytics/metrics", response_model=Dict[str, Any])
def get_healthinsurancepolicy_metrics():
    """Calculate summary statistical KPIs for HealthInsurancePolicy collection."""
    svc = HealthInsurancePolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== RetirementPensionFund Endpoints ====================
@router.get("/retirementpensionfunds", response_model=List[Dict[str, Any]])
def list_retirementpensionfunds(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RetirementPensionFund records with pagination and filtering."""
    svc = RetirementPensionFundService()
    items = svc.list_retirementpensionfunds(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/retirementpensionfunds/{item_id}", response_model=Dict[str, Any])
def get_retirementpensionfund_by_id(item_id: int):
    """Retrieve detailed record for RetirementPensionFund by ID."""
    svc = RetirementPensionFundService()
    item = svc.get_retirementpensionfund_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RetirementPensionFund with ID {item_id} not found")
    return item.to_dict()

@router.post("/retirementpensionfunds", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_retirementpensionfund(payload: RetirementPensionFundCreateSchema):
    """Create new RetirementPensionFund instance in enterprise repository."""
    svc = RetirementPensionFundService()
    try:
        item = svc.create_retirementpensionfund(
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

@router.put("/retirementpensionfunds/{item_id}", response_model=Dict[str, Any])
def update_retirementpensionfund(item_id: int, payload: RetirementPensionFundUpdateSchema):
    """Update existing RetirementPensionFund record fields."""
    svc = RetirementPensionFundService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_retirementpensionfund(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RetirementPensionFund with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/retirementpensionfunds/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_retirementpensionfund(item_id: int, hard: bool = Query(False)):
    """Delete RetirementPensionFund record (soft-delete by default)."""
    svc = RetirementPensionFundService()
    ok = svc.delete_retirementpensionfund(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RetirementPensionFund with ID {item_id} not found")
    return None

@router.get("/retirementpensionfunds/analytics/metrics", response_model=Dict[str, Any])
def get_retirementpensionfund_metrics():
    """Calculate summary statistical KPIs for RetirementPensionFund collection."""
    svc = RetirementPensionFundService()
    return svc.calculate_aggregate_metrics()

# ==================== WellnessReimbursement Endpoints ====================
@router.get("/wellnessreimbursements", response_model=List[Dict[str, Any]])
def list_wellnessreimbursements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WellnessReimbursement records with pagination and filtering."""
    svc = WellnessReimbursementService()
    items = svc.list_wellnessreimbursements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/wellnessreimbursements/{item_id}", response_model=Dict[str, Any])
def get_wellnessreimbursement_by_id(item_id: int):
    """Retrieve detailed record for WellnessReimbursement by ID."""
    svc = WellnessReimbursementService()
    item = svc.get_wellnessreimbursement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WellnessReimbursement with ID {item_id} not found")
    return item.to_dict()

@router.post("/wellnessreimbursements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_wellnessreimbursement(payload: WellnessReimbursementCreateSchema):
    """Create new WellnessReimbursement instance in enterprise repository."""
    svc = WellnessReimbursementService()
    try:
        item = svc.create_wellnessreimbursement(
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

@router.put("/wellnessreimbursements/{item_id}", response_model=Dict[str, Any])
def update_wellnessreimbursement(item_id: int, payload: WellnessReimbursementUpdateSchema):
    """Update existing WellnessReimbursement record fields."""
    svc = WellnessReimbursementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_wellnessreimbursement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WellnessReimbursement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/wellnessreimbursements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wellnessreimbursement(item_id: int, hard: bool = Query(False)):
    """Delete WellnessReimbursement record (soft-delete by default)."""
    svc = WellnessReimbursementService()
    ok = svc.delete_wellnessreimbursement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WellnessReimbursement with ID {item_id} not found")
    return None

@router.get("/wellnessreimbursements/analytics/metrics", response_model=Dict[str, Any])
def get_wellnessreimbursement_metrics():
    """Calculate summary statistical KPIs for WellnessReimbursement collection."""
    svc = WellnessReimbursementService()
    return svc.calculate_aggregate_metrics()

# ==================== LifeInsuranceCoverage Endpoints ====================
@router.get("/lifeinsurancecoverages", response_model=List[Dict[str, Any]])
def list_lifeinsurancecoverages(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LifeInsuranceCoverage records with pagination and filtering."""
    svc = LifeInsuranceCoverageService()
    items = svc.list_lifeinsurancecoverages(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/lifeinsurancecoverages/{item_id}", response_model=Dict[str, Any])
def get_lifeinsurancecoverage_by_id(item_id: int):
    """Retrieve detailed record for LifeInsuranceCoverage by ID."""
    svc = LifeInsuranceCoverageService()
    item = svc.get_lifeinsurancecoverage_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LifeInsuranceCoverage with ID {item_id} not found")
    return item.to_dict()

@router.post("/lifeinsurancecoverages", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_lifeinsurancecoverage(payload: LifeInsuranceCoverageCreateSchema):
    """Create new LifeInsuranceCoverage instance in enterprise repository."""
    svc = LifeInsuranceCoverageService()
    try:
        item = svc.create_lifeinsurancecoverage(
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

@router.put("/lifeinsurancecoverages/{item_id}", response_model=Dict[str, Any])
def update_lifeinsurancecoverage(item_id: int, payload: LifeInsuranceCoverageUpdateSchema):
    """Update existing LifeInsuranceCoverage record fields."""
    svc = LifeInsuranceCoverageService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_lifeinsurancecoverage(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LifeInsuranceCoverage with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/lifeinsurancecoverages/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lifeinsurancecoverage(item_id: int, hard: bool = Query(False)):
    """Delete LifeInsuranceCoverage record (soft-delete by default)."""
    svc = LifeInsuranceCoverageService()
    ok = svc.delete_lifeinsurancecoverage(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LifeInsuranceCoverage with ID {item_id} not found")
    return None

@router.get("/lifeinsurancecoverages/analytics/metrics", response_model=Dict[str, Any])
def get_lifeinsurancecoverage_metrics():
    """Calculate summary statistical KPIs for LifeInsuranceCoverage collection."""
    svc = LifeInsuranceCoverageService()
    return svc.calculate_aggregate_metrics()

# ==================== FlexibleSpendingAccount Endpoints ====================
@router.get("/flexiblespendingaccounts", response_model=List[Dict[str, Any]])
def list_flexiblespendingaccounts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FlexibleSpendingAccount records with pagination and filtering."""
    svc = FlexibleSpendingAccountService()
    items = svc.list_flexiblespendingaccounts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/flexiblespendingaccounts/{item_id}", response_model=Dict[str, Any])
def get_flexiblespendingaccount_by_id(item_id: int):
    """Retrieve detailed record for FlexibleSpendingAccount by ID."""
    svc = FlexibleSpendingAccountService()
    item = svc.get_flexiblespendingaccount_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FlexibleSpendingAccount with ID {item_id} not found")
    return item.to_dict()

@router.post("/flexiblespendingaccounts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_flexiblespendingaccount(payload: FlexibleSpendingAccountCreateSchema):
    """Create new FlexibleSpendingAccount instance in enterprise repository."""
    svc = FlexibleSpendingAccountService()
    try:
        item = svc.create_flexiblespendingaccount(
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

@router.put("/flexiblespendingaccounts/{item_id}", response_model=Dict[str, Any])
def update_flexiblespendingaccount(item_id: int, payload: FlexibleSpendingAccountUpdateSchema):
    """Update existing FlexibleSpendingAccount record fields."""
    svc = FlexibleSpendingAccountService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_flexiblespendingaccount(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FlexibleSpendingAccount with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/flexiblespendingaccounts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_flexiblespendingaccount(item_id: int, hard: bool = Query(False)):
    """Delete FlexibleSpendingAccount record (soft-delete by default)."""
    svc = FlexibleSpendingAccountService()
    ok = svc.delete_flexiblespendingaccount(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FlexibleSpendingAccount with ID {item_id} not found")
    return None

@router.get("/flexiblespendingaccounts/analytics/metrics", response_model=Dict[str, Any])
def get_flexiblespendingaccount_metrics():
    """Calculate summary statistical KPIs for FlexibleSpendingAccount collection."""
    svc = FlexibleSpendingAccountService()
    return svc.calculate_aggregate_metrics()

# ==================== DependentBeneficiary Endpoints ====================
@router.get("/dependentbeneficiarys", response_model=List[Dict[str, Any]])
def list_dependentbeneficiarys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DependentBeneficiary records with pagination and filtering."""
    svc = DependentBeneficiaryService()
    items = svc.list_dependentbeneficiarys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dependentbeneficiarys/{item_id}", response_model=Dict[str, Any])
def get_dependentbeneficiary_by_id(item_id: int):
    """Retrieve detailed record for DependentBeneficiary by ID."""
    svc = DependentBeneficiaryService()
    item = svc.get_dependentbeneficiary_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DependentBeneficiary with ID {item_id} not found")
    return item.to_dict()

@router.post("/dependentbeneficiarys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dependentbeneficiary(payload: DependentBeneficiaryCreateSchema):
    """Create new DependentBeneficiary instance in enterprise repository."""
    svc = DependentBeneficiaryService()
    try:
        item = svc.create_dependentbeneficiary(
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

@router.put("/dependentbeneficiarys/{item_id}", response_model=Dict[str, Any])
def update_dependentbeneficiary(item_id: int, payload: DependentBeneficiaryUpdateSchema):
    """Update existing DependentBeneficiary record fields."""
    svc = DependentBeneficiaryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dependentbeneficiary(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DependentBeneficiary with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dependentbeneficiarys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dependentbeneficiary(item_id: int, hard: bool = Query(False)):
    """Delete DependentBeneficiary record (soft-delete by default)."""
    svc = DependentBeneficiaryService()
    ok = svc.delete_dependentbeneficiary(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DependentBeneficiary with ID {item_id} not found")
    return None

@router.get("/dependentbeneficiarys/analytics/metrics", response_model=Dict[str, Any])
def get_dependentbeneficiary_metrics():
    """Calculate summary statistical KPIs for DependentBeneficiary collection."""
    svc = DependentBeneficiaryService()
    return svc.calculate_aggregate_metrics()

# ==================== BenefitClaimSubmission Endpoints ====================
@router.get("/benefitclaimsubmissions", response_model=List[Dict[str, Any]])
def list_benefitclaimsubmissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BenefitClaimSubmission records with pagination and filtering."""
    svc = BenefitClaimSubmissionService()
    items = svc.list_benefitclaimsubmissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/benefitclaimsubmissions/{item_id}", response_model=Dict[str, Any])
def get_benefitclaimsubmission_by_id(item_id: int):
    """Retrieve detailed record for BenefitClaimSubmission by ID."""
    svc = BenefitClaimSubmissionService()
    item = svc.get_benefitclaimsubmission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BenefitClaimSubmission with ID {item_id} not found")
    return item.to_dict()

@router.post("/benefitclaimsubmissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_benefitclaimsubmission(payload: BenefitClaimSubmissionCreateSchema):
    """Create new BenefitClaimSubmission instance in enterprise repository."""
    svc = BenefitClaimSubmissionService()
    try:
        item = svc.create_benefitclaimsubmission(
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

@router.put("/benefitclaimsubmissions/{item_id}", response_model=Dict[str, Any])
def update_benefitclaimsubmission(item_id: int, payload: BenefitClaimSubmissionUpdateSchema):
    """Update existing BenefitClaimSubmission record fields."""
    svc = BenefitClaimSubmissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_benefitclaimsubmission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BenefitClaimSubmission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/benefitclaimsubmissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_benefitclaimsubmission(item_id: int, hard: bool = Query(False)):
    """Delete BenefitClaimSubmission record (soft-delete by default)."""
    svc = BenefitClaimSubmissionService()
    ok = svc.delete_benefitclaimsubmission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BenefitClaimSubmission with ID {item_id} not found")
    return None

@router.get("/benefitclaimsubmissions/analytics/metrics", response_model=Dict[str, Any])
def get_benefitclaimsubmission_metrics():
    """Calculate summary statistical KPIs for BenefitClaimSubmission collection."""
    svc = BenefitClaimSubmissionService()
    return svc.calculate_aggregate_metrics()

# ==================== DeductionPayrollMap Endpoints ====================
@router.get("/deductionpayrollmaps", response_model=List[Dict[str, Any]])
def list_deductionpayrollmaps(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeductionPayrollMap records with pagination and filtering."""
    svc = DeductionPayrollMapService()
    items = svc.list_deductionpayrollmaps(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/deductionpayrollmaps/{item_id}", response_model=Dict[str, Any])
def get_deductionpayrollmap_by_id(item_id: int):
    """Retrieve detailed record for DeductionPayrollMap by ID."""
    svc = DeductionPayrollMapService()
    item = svc.get_deductionpayrollmap_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeductionPayrollMap with ID {item_id} not found")
    return item.to_dict()

@router.post("/deductionpayrollmaps", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_deductionpayrollmap(payload: DeductionPayrollMapCreateSchema):
    """Create new DeductionPayrollMap instance in enterprise repository."""
    svc = DeductionPayrollMapService()
    try:
        item = svc.create_deductionpayrollmap(
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

@router.put("/deductionpayrollmaps/{item_id}", response_model=Dict[str, Any])
def update_deductionpayrollmap(item_id: int, payload: DeductionPayrollMapUpdateSchema):
    """Update existing DeductionPayrollMap record fields."""
    svc = DeductionPayrollMapService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_deductionpayrollmap(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeductionPayrollMap with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/deductionpayrollmaps/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deductionpayrollmap(item_id: int, hard: bool = Query(False)):
    """Delete DeductionPayrollMap record (soft-delete by default)."""
    svc = DeductionPayrollMapService()
    ok = svc.delete_deductionpayrollmap(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeductionPayrollMap with ID {item_id} not found")
    return None

@router.get("/deductionpayrollmaps/analytics/metrics", response_model=Dict[str, Any])
def get_deductionpayrollmap_metrics():
    """Calculate summary statistical KPIs for DeductionPayrollMap collection."""
    svc = DeductionPayrollMapService()
    return svc.calculate_aggregate_metrics()

# ==================== OpenEnrollmentWindow Endpoints ====================
@router.get("/openenrollmentwindows", response_model=List[Dict[str, Any]])
def list_openenrollmentwindows(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OpenEnrollmentWindow records with pagination and filtering."""
    svc = OpenEnrollmentWindowService()
    items = svc.list_openenrollmentwindows(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/openenrollmentwindows/{item_id}", response_model=Dict[str, Any])
def get_openenrollmentwindow_by_id(item_id: int):
    """Retrieve detailed record for OpenEnrollmentWindow by ID."""
    svc = OpenEnrollmentWindowService()
    item = svc.get_openenrollmentwindow_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OpenEnrollmentWindow with ID {item_id} not found")
    return item.to_dict()

@router.post("/openenrollmentwindows", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_openenrollmentwindow(payload: OpenEnrollmentWindowCreateSchema):
    """Create new OpenEnrollmentWindow instance in enterprise repository."""
    svc = OpenEnrollmentWindowService()
    try:
        item = svc.create_openenrollmentwindow(
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

@router.put("/openenrollmentwindows/{item_id}", response_model=Dict[str, Any])
def update_openenrollmentwindow(item_id: int, payload: OpenEnrollmentWindowUpdateSchema):
    """Update existing OpenEnrollmentWindow record fields."""
    svc = OpenEnrollmentWindowService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_openenrollmentwindow(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OpenEnrollmentWindow with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/openenrollmentwindows/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_openenrollmentwindow(item_id: int, hard: bool = Query(False)):
    """Delete OpenEnrollmentWindow record (soft-delete by default)."""
    svc = OpenEnrollmentWindowService()
    ok = svc.delete_openenrollmentwindow(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OpenEnrollmentWindow with ID {item_id} not found")
    return None

@router.get("/openenrollmentwindows/analytics/metrics", response_model=Dict[str, Any])
def get_openenrollmentwindow_metrics():
    """Calculate summary statistical KPIs for OpenEnrollmentWindow collection."""
    svc = OpenEnrollmentWindowService()
    return svc.calculate_aggregate_metrics()

# ==================== CarrierBillingReconcile Endpoints ====================
@router.get("/carrierbillingreconciles", response_model=List[Dict[str, Any]])
def list_carrierbillingreconciles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CarrierBillingReconcile records with pagination and filtering."""
    svc = CarrierBillingReconcileService()
    items = svc.list_carrierbillingreconciles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/carrierbillingreconciles/{item_id}", response_model=Dict[str, Any])
def get_carrierbillingreconcile_by_id(item_id: int):
    """Retrieve detailed record for CarrierBillingReconcile by ID."""
    svc = CarrierBillingReconcileService()
    item = svc.get_carrierbillingreconcile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CarrierBillingReconcile with ID {item_id} not found")
    return item.to_dict()

@router.post("/carrierbillingreconciles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_carrierbillingreconcile(payload: CarrierBillingReconcileCreateSchema):
    """Create new CarrierBillingReconcile instance in enterprise repository."""
    svc = CarrierBillingReconcileService()
    try:
        item = svc.create_carrierbillingreconcile(
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

@router.put("/carrierbillingreconciles/{item_id}", response_model=Dict[str, Any])
def update_carrierbillingreconcile(item_id: int, payload: CarrierBillingReconcileUpdateSchema):
    """Update existing CarrierBillingReconcile record fields."""
    svc = CarrierBillingReconcileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_carrierbillingreconcile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CarrierBillingReconcile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/carrierbillingreconciles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrierbillingreconcile(item_id: int, hard: bool = Query(False)):
    """Delete CarrierBillingReconcile record (soft-delete by default)."""
    svc = CarrierBillingReconcileService()
    ok = svc.delete_carrierbillingreconcile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CarrierBillingReconcile with ID {item_id} not found")
    return None

@router.get("/carrierbillingreconciles/analytics/metrics", response_model=Dict[str, Any])
def get_carrierbillingreconcile_metrics():
    """Calculate summary statistical KPIs for CarrierBillingReconcile collection."""
    svc = CarrierBillingReconcileService()
    return svc.calculate_aggregate_metrics()

# ==================== COBRAContinuationLog Endpoints ====================
@router.get("/cobracontinuationlogs", response_model=List[Dict[str, Any]])
def list_cobracontinuationlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List COBRAContinuationLog records with pagination and filtering."""
    svc = COBRAContinuationLogService()
    items = svc.list_cobracontinuationlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cobracontinuationlogs/{item_id}", response_model=Dict[str, Any])
def get_cobracontinuationlog_by_id(item_id: int):
    """Retrieve detailed record for COBRAContinuationLog by ID."""
    svc = COBRAContinuationLogService()
    item = svc.get_cobracontinuationlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"COBRAContinuationLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/cobracontinuationlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cobracontinuationlog(payload: COBRAContinuationLogCreateSchema):
    """Create new COBRAContinuationLog instance in enterprise repository."""
    svc = COBRAContinuationLogService()
    try:
        item = svc.create_cobracontinuationlog(
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

@router.put("/cobracontinuationlogs/{item_id}", response_model=Dict[str, Any])
def update_cobracontinuationlog(item_id: int, payload: COBRAContinuationLogUpdateSchema):
    """Update existing COBRAContinuationLog record fields."""
    svc = COBRAContinuationLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cobracontinuationlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"COBRAContinuationLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cobracontinuationlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cobracontinuationlog(item_id: int, hard: bool = Query(False)):
    """Delete COBRAContinuationLog record (soft-delete by default)."""
    svc = COBRAContinuationLogService()
    ok = svc.delete_cobracontinuationlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"COBRAContinuationLog with ID {item_id} not found")
    return None

@router.get("/cobracontinuationlogs/analytics/metrics", response_model=Dict[str, Any])
def get_cobracontinuationlog_metrics():
    """Calculate summary statistical KPIs for COBRAContinuationLog collection."""
    svc = COBRAContinuationLogService()
    return svc.calculate_aggregate_metrics()

# ==================== EmployeeAssistanceProg Endpoints ====================
@router.get("/employeeassistanceprogs", response_model=List[Dict[str, Any]])
def list_employeeassistanceprogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmployeeAssistanceProg records with pagination and filtering."""
    svc = EmployeeAssistanceProgService()
    items = svc.list_employeeassistanceprogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/employeeassistanceprogs/{item_id}", response_model=Dict[str, Any])
def get_employeeassistanceprog_by_id(item_id: int):
    """Retrieve detailed record for EmployeeAssistanceProg by ID."""
    svc = EmployeeAssistanceProgService()
    item = svc.get_employeeassistanceprog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmployeeAssistanceProg with ID {item_id} not found")
    return item.to_dict()

@router.post("/employeeassistanceprogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_employeeassistanceprog(payload: EmployeeAssistanceProgCreateSchema):
    """Create new EmployeeAssistanceProg instance in enterprise repository."""
    svc = EmployeeAssistanceProgService()
    try:
        item = svc.create_employeeassistanceprog(
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

@router.put("/employeeassistanceprogs/{item_id}", response_model=Dict[str, Any])
def update_employeeassistanceprog(item_id: int, payload: EmployeeAssistanceProgUpdateSchema):
    """Update existing EmployeeAssistanceProg record fields."""
    svc = EmployeeAssistanceProgService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_employeeassistanceprog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmployeeAssistanceProg with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/employeeassistanceprogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employeeassistanceprog(item_id: int, hard: bool = Query(False)):
    """Delete EmployeeAssistanceProg record (soft-delete by default)."""
    svc = EmployeeAssistanceProgService()
    ok = svc.delete_employeeassistanceprog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmployeeAssistanceProg with ID {item_id} not found")
    return None

@router.get("/employeeassistanceprogs/analytics/metrics", response_model=Dict[str, Any])
def get_employeeassistanceprog_metrics():
    """Calculate summary statistical KPIs for EmployeeAssistanceProg collection."""
    svc = EmployeeAssistanceProgService()
    return svc.calculate_aggregate_metrics()

# ==================== VoluntaryBenefitOption Endpoints ====================
@router.get("/voluntarybenefitoptions", response_model=List[Dict[str, Any]])
def list_voluntarybenefitoptions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VoluntaryBenefitOption records with pagination and filtering."""
    svc = VoluntaryBenefitOptionService()
    items = svc.list_voluntarybenefitoptions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/voluntarybenefitoptions/{item_id}", response_model=Dict[str, Any])
def get_voluntarybenefitoption_by_id(item_id: int):
    """Retrieve detailed record for VoluntaryBenefitOption by ID."""
    svc = VoluntaryBenefitOptionService()
    item = svc.get_voluntarybenefitoption_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VoluntaryBenefitOption with ID {item_id} not found")
    return item.to_dict()

@router.post("/voluntarybenefitoptions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_voluntarybenefitoption(payload: VoluntaryBenefitOptionCreateSchema):
    """Create new VoluntaryBenefitOption instance in enterprise repository."""
    svc = VoluntaryBenefitOptionService()
    try:
        item = svc.create_voluntarybenefitoption(
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

@router.put("/voluntarybenefitoptions/{item_id}", response_model=Dict[str, Any])
def update_voluntarybenefitoption(item_id: int, payload: VoluntaryBenefitOptionUpdateSchema):
    """Update existing VoluntaryBenefitOption record fields."""
    svc = VoluntaryBenefitOptionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_voluntarybenefitoption(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VoluntaryBenefitOption with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/voluntarybenefitoptions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_voluntarybenefitoption(item_id: int, hard: bool = Query(False)):
    """Delete VoluntaryBenefitOption record (soft-delete by default)."""
    svc = VoluntaryBenefitOptionService()
    ok = svc.delete_voluntarybenefitoption(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VoluntaryBenefitOption with ID {item_id} not found")
    return None

@router.get("/voluntarybenefitoptions/analytics/metrics", response_model=Dict[str, Any])
def get_voluntarybenefitoption_metrics():
    """Calculate summary statistical KPIs for VoluntaryBenefitOption collection."""
    svc = VoluntaryBenefitOptionService()
    return svc.calculate_aggregate_metrics()

# ==================== BenefitCostAnalytics Endpoints ====================
@router.get("/benefitcostanalyticss", response_model=List[Dict[str, Any]])
def list_benefitcostanalyticss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BenefitCostAnalytics records with pagination and filtering."""
    svc = BenefitCostAnalyticsService()
    items = svc.list_benefitcostanalyticss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/benefitcostanalyticss/{item_id}", response_model=Dict[str, Any])
def get_benefitcostanalytics_by_id(item_id: int):
    """Retrieve detailed record for BenefitCostAnalytics by ID."""
    svc = BenefitCostAnalyticsService()
    item = svc.get_benefitcostanalytics_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BenefitCostAnalytics with ID {item_id} not found")
    return item.to_dict()

@router.post("/benefitcostanalyticss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_benefitcostanalytics(payload: BenefitCostAnalyticsCreateSchema):
    """Create new BenefitCostAnalytics instance in enterprise repository."""
    svc = BenefitCostAnalyticsService()
    try:
        item = svc.create_benefitcostanalytics(
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

@router.put("/benefitcostanalyticss/{item_id}", response_model=Dict[str, Any])
def update_benefitcostanalytics(item_id: int, payload: BenefitCostAnalyticsUpdateSchema):
    """Update existing BenefitCostAnalytics record fields."""
    svc = BenefitCostAnalyticsService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_benefitcostanalytics(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BenefitCostAnalytics with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/benefitcostanalyticss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_benefitcostanalytics(item_id: int, hard: bool = Query(False)):
    """Delete BenefitCostAnalytics record (soft-delete by default)."""
    svc = BenefitCostAnalyticsService()
    ok = svc.delete_benefitcostanalytics(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BenefitCostAnalytics with ID {item_id} not found")
    return None

@router.get("/benefitcostanalyticss/analytics/metrics", response_model=Dict[str, Any])
def get_benefitcostanalytics_metrics():
    """Calculate summary statistical KPIs for BenefitCostAnalytics collection."""
    svc = BenefitCostAnalyticsService()
    return svc.calculate_aggregate_metrics()

