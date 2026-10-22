"""
Enterprise Risk Management & KRI Matrix - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    RiskCategoryDefinitionService,
    RiskRegisterItemService,
    RiskAssessmentScoreService,
    KeyRiskIndicatorService,
    KRIThresholdAlertService,
    RiskMitigationStrategyService,
    ActionOwnerAssignmentService,
    ScenarioStressTestService,
    LossEventIncidentService,
    BusinessContinuityPlanService,
    DisasterRecoveryScenarioService,
    ResidualRiskEvaluationService,
    RiskAppetiteStatementService,
    InsuranceCoverageLinkService,
    RiskCommitteeReportService,
    AuditRecommendationService,
)
from .schemas import (
    RiskCategoryDefinitionCreateSchema, RiskCategoryDefinitionUpdateSchema, RiskCategoryDefinitionResponseSchema,
    RiskRegisterItemCreateSchema, RiskRegisterItemUpdateSchema, RiskRegisterItemResponseSchema,
    RiskAssessmentScoreCreateSchema, RiskAssessmentScoreUpdateSchema, RiskAssessmentScoreResponseSchema,
    KeyRiskIndicatorCreateSchema, KeyRiskIndicatorUpdateSchema, KeyRiskIndicatorResponseSchema,
    KRIThresholdAlertCreateSchema, KRIThresholdAlertUpdateSchema, KRIThresholdAlertResponseSchema,
    RiskMitigationStrategyCreateSchema, RiskMitigationStrategyUpdateSchema, RiskMitigationStrategyResponseSchema,
    ActionOwnerAssignmentCreateSchema, ActionOwnerAssignmentUpdateSchema, ActionOwnerAssignmentResponseSchema,
    ScenarioStressTestCreateSchema, ScenarioStressTestUpdateSchema, ScenarioStressTestResponseSchema,
    LossEventIncidentCreateSchema, LossEventIncidentUpdateSchema, LossEventIncidentResponseSchema,
    BusinessContinuityPlanCreateSchema, BusinessContinuityPlanUpdateSchema, BusinessContinuityPlanResponseSchema,
    DisasterRecoveryScenarioCreateSchema, DisasterRecoveryScenarioUpdateSchema, DisasterRecoveryScenarioResponseSchema,
    ResidualRiskEvaluationCreateSchema, ResidualRiskEvaluationUpdateSchema, ResidualRiskEvaluationResponseSchema,
    RiskAppetiteStatementCreateSchema, RiskAppetiteStatementUpdateSchema, RiskAppetiteStatementResponseSchema,
    InsuranceCoverageLinkCreateSchema, InsuranceCoverageLinkUpdateSchema, InsuranceCoverageLinkResponseSchema,
    RiskCommitteeReportCreateSchema, RiskCommitteeReportUpdateSchema, RiskCommitteeReportResponseSchema,
    AuditRecommendationCreateSchema, AuditRecommendationUpdateSchema, AuditRecommendationResponseSchema,
)

router = APIRouter(prefix="/risk_management", tags=["Enterprise Risk Management & KRI Matrix"])

# ==================== RiskCategoryDefinition Endpoints ====================
@router.get("/riskcategorydefinitions", response_model=List[Dict[str, Any]])
def list_riskcategorydefinitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RiskCategoryDefinition records with pagination and filtering."""
    svc = RiskCategoryDefinitionService()
    items = svc.list_riskcategorydefinitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/riskcategorydefinitions/{item_id}", response_model=Dict[str, Any])
def get_riskcategorydefinition_by_id(item_id: int):
    """Retrieve detailed record for RiskCategoryDefinition by ID."""
    svc = RiskCategoryDefinitionService()
    item = svc.get_riskcategorydefinition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RiskCategoryDefinition with ID {item_id} not found")
    return item.to_dict()

@router.post("/riskcategorydefinitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_riskcategorydefinition(payload: RiskCategoryDefinitionCreateSchema):
    """Create new RiskCategoryDefinition instance in enterprise repository."""
    svc = RiskCategoryDefinitionService()
    try:
        item = svc.create_riskcategorydefinition(
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

@router.put("/riskcategorydefinitions/{item_id}", response_model=Dict[str, Any])
def update_riskcategorydefinition(item_id: int, payload: RiskCategoryDefinitionUpdateSchema):
    """Update existing RiskCategoryDefinition record fields."""
    svc = RiskCategoryDefinitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_riskcategorydefinition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RiskCategoryDefinition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/riskcategorydefinitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_riskcategorydefinition(item_id: int, hard: bool = Query(False)):
    """Delete RiskCategoryDefinition record (soft-delete by default)."""
    svc = RiskCategoryDefinitionService()
    ok = svc.delete_riskcategorydefinition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RiskCategoryDefinition with ID {item_id} not found")
    return None

@router.get("/riskcategorydefinitions/analytics/metrics", response_model=Dict[str, Any])
def get_riskcategorydefinition_metrics():
    """Calculate summary statistical KPIs for RiskCategoryDefinition collection."""
    svc = RiskCategoryDefinitionService()
    return svc.calculate_aggregate_metrics()

# ==================== RiskRegisterItem Endpoints ====================
@router.get("/riskregisteritems", response_model=List[Dict[str, Any]])
def list_riskregisteritems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RiskRegisterItem records with pagination and filtering."""
    svc = RiskRegisterItemService()
    items = svc.list_riskregisteritems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/riskregisteritems/{item_id}", response_model=Dict[str, Any])
def get_riskregisteritem_by_id(item_id: int):
    """Retrieve detailed record for RiskRegisterItem by ID."""
    svc = RiskRegisterItemService()
    item = svc.get_riskregisteritem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RiskRegisterItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/riskregisteritems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_riskregisteritem(payload: RiskRegisterItemCreateSchema):
    """Create new RiskRegisterItem instance in enterprise repository."""
    svc = RiskRegisterItemService()
    try:
        item = svc.create_riskregisteritem(
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

@router.put("/riskregisteritems/{item_id}", response_model=Dict[str, Any])
def update_riskregisteritem(item_id: int, payload: RiskRegisterItemUpdateSchema):
    """Update existing RiskRegisterItem record fields."""
    svc = RiskRegisterItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_riskregisteritem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RiskRegisterItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/riskregisteritems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_riskregisteritem(item_id: int, hard: bool = Query(False)):
    """Delete RiskRegisterItem record (soft-delete by default)."""
    svc = RiskRegisterItemService()
    ok = svc.delete_riskregisteritem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RiskRegisterItem with ID {item_id} not found")
    return None

@router.get("/riskregisteritems/analytics/metrics", response_model=Dict[str, Any])
def get_riskregisteritem_metrics():
    """Calculate summary statistical KPIs for RiskRegisterItem collection."""
    svc = RiskRegisterItemService()
    return svc.calculate_aggregate_metrics()

# ==================== RiskAssessmentScore Endpoints ====================
@router.get("/riskassessmentscores", response_model=List[Dict[str, Any]])
def list_riskassessmentscores(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RiskAssessmentScore records with pagination and filtering."""
    svc = RiskAssessmentScoreService()
    items = svc.list_riskassessmentscores(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/riskassessmentscores/{item_id}", response_model=Dict[str, Any])
def get_riskassessmentscore_by_id(item_id: int):
    """Retrieve detailed record for RiskAssessmentScore by ID."""
    svc = RiskAssessmentScoreService()
    item = svc.get_riskassessmentscore_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RiskAssessmentScore with ID {item_id} not found")
    return item.to_dict()

@router.post("/riskassessmentscores", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_riskassessmentscore(payload: RiskAssessmentScoreCreateSchema):
    """Create new RiskAssessmentScore instance in enterprise repository."""
    svc = RiskAssessmentScoreService()
    try:
        item = svc.create_riskassessmentscore(
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

@router.put("/riskassessmentscores/{item_id}", response_model=Dict[str, Any])
def update_riskassessmentscore(item_id: int, payload: RiskAssessmentScoreUpdateSchema):
    """Update existing RiskAssessmentScore record fields."""
    svc = RiskAssessmentScoreService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_riskassessmentscore(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RiskAssessmentScore with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/riskassessmentscores/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_riskassessmentscore(item_id: int, hard: bool = Query(False)):
    """Delete RiskAssessmentScore record (soft-delete by default)."""
    svc = RiskAssessmentScoreService()
    ok = svc.delete_riskassessmentscore(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RiskAssessmentScore with ID {item_id} not found")
    return None

@router.get("/riskassessmentscores/analytics/metrics", response_model=Dict[str, Any])
def get_riskassessmentscore_metrics():
    """Calculate summary statistical KPIs for RiskAssessmentScore collection."""
    svc = RiskAssessmentScoreService()
    return svc.calculate_aggregate_metrics()

# ==================== KeyRiskIndicator Endpoints ====================
@router.get("/keyriskindicators", response_model=List[Dict[str, Any]])
def list_keyriskindicators(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List KeyRiskIndicator records with pagination and filtering."""
    svc = KeyRiskIndicatorService()
    items = svc.list_keyriskindicators(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/keyriskindicators/{item_id}", response_model=Dict[str, Any])
def get_keyriskindicator_by_id(item_id: int):
    """Retrieve detailed record for KeyRiskIndicator by ID."""
    svc = KeyRiskIndicatorService()
    item = svc.get_keyriskindicator_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"KeyRiskIndicator with ID {item_id} not found")
    return item.to_dict()

@router.post("/keyriskindicators", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_keyriskindicator(payload: KeyRiskIndicatorCreateSchema):
    """Create new KeyRiskIndicator instance in enterprise repository."""
    svc = KeyRiskIndicatorService()
    try:
        item = svc.create_keyriskindicator(
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

@router.put("/keyriskindicators/{item_id}", response_model=Dict[str, Any])
def update_keyriskindicator(item_id: int, payload: KeyRiskIndicatorUpdateSchema):
    """Update existing KeyRiskIndicator record fields."""
    svc = KeyRiskIndicatorService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_keyriskindicator(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"KeyRiskIndicator with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/keyriskindicators/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_keyriskindicator(item_id: int, hard: bool = Query(False)):
    """Delete KeyRiskIndicator record (soft-delete by default)."""
    svc = KeyRiskIndicatorService()
    ok = svc.delete_keyriskindicator(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"KeyRiskIndicator with ID {item_id} not found")
    return None

@router.get("/keyriskindicators/analytics/metrics", response_model=Dict[str, Any])
def get_keyriskindicator_metrics():
    """Calculate summary statistical KPIs for KeyRiskIndicator collection."""
    svc = KeyRiskIndicatorService()
    return svc.calculate_aggregate_metrics()

# ==================== KRIThresholdAlert Endpoints ====================
@router.get("/krithresholdalerts", response_model=List[Dict[str, Any]])
def list_krithresholdalerts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List KRIThresholdAlert records with pagination and filtering."""
    svc = KRIThresholdAlertService()
    items = svc.list_krithresholdalerts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/krithresholdalerts/{item_id}", response_model=Dict[str, Any])
def get_krithresholdalert_by_id(item_id: int):
    """Retrieve detailed record for KRIThresholdAlert by ID."""
    svc = KRIThresholdAlertService()
    item = svc.get_krithresholdalert_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"KRIThresholdAlert with ID {item_id} not found")
    return item.to_dict()

@router.post("/krithresholdalerts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_krithresholdalert(payload: KRIThresholdAlertCreateSchema):
    """Create new KRIThresholdAlert instance in enterprise repository."""
    svc = KRIThresholdAlertService()
    try:
        item = svc.create_krithresholdalert(
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

@router.put("/krithresholdalerts/{item_id}", response_model=Dict[str, Any])
def update_krithresholdalert(item_id: int, payload: KRIThresholdAlertUpdateSchema):
    """Update existing KRIThresholdAlert record fields."""
    svc = KRIThresholdAlertService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_krithresholdalert(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"KRIThresholdAlert with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/krithresholdalerts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_krithresholdalert(item_id: int, hard: bool = Query(False)):
    """Delete KRIThresholdAlert record (soft-delete by default)."""
    svc = KRIThresholdAlertService()
    ok = svc.delete_krithresholdalert(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"KRIThresholdAlert with ID {item_id} not found")
    return None

@router.get("/krithresholdalerts/analytics/metrics", response_model=Dict[str, Any])
def get_krithresholdalert_metrics():
    """Calculate summary statistical KPIs for KRIThresholdAlert collection."""
    svc = KRIThresholdAlertService()
    return svc.calculate_aggregate_metrics()

# ==================== RiskMitigationStrategy Endpoints ====================
@router.get("/riskmitigationstrategys", response_model=List[Dict[str, Any]])
def list_riskmitigationstrategys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RiskMitigationStrategy records with pagination and filtering."""
    svc = RiskMitigationStrategyService()
    items = svc.list_riskmitigationstrategys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/riskmitigationstrategys/{item_id}", response_model=Dict[str, Any])
def get_riskmitigationstrategy_by_id(item_id: int):
    """Retrieve detailed record for RiskMitigationStrategy by ID."""
    svc = RiskMitigationStrategyService()
    item = svc.get_riskmitigationstrategy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RiskMitigationStrategy with ID {item_id} not found")
    return item.to_dict()

@router.post("/riskmitigationstrategys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_riskmitigationstrategy(payload: RiskMitigationStrategyCreateSchema):
    """Create new RiskMitigationStrategy instance in enterprise repository."""
    svc = RiskMitigationStrategyService()
    try:
        item = svc.create_riskmitigationstrategy(
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

@router.put("/riskmitigationstrategys/{item_id}", response_model=Dict[str, Any])
def update_riskmitigationstrategy(item_id: int, payload: RiskMitigationStrategyUpdateSchema):
    """Update existing RiskMitigationStrategy record fields."""
    svc = RiskMitigationStrategyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_riskmitigationstrategy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RiskMitigationStrategy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/riskmitigationstrategys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_riskmitigationstrategy(item_id: int, hard: bool = Query(False)):
    """Delete RiskMitigationStrategy record (soft-delete by default)."""
    svc = RiskMitigationStrategyService()
    ok = svc.delete_riskmitigationstrategy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RiskMitigationStrategy with ID {item_id} not found")
    return None

@router.get("/riskmitigationstrategys/analytics/metrics", response_model=Dict[str, Any])
def get_riskmitigationstrategy_metrics():
    """Calculate summary statistical KPIs for RiskMitigationStrategy collection."""
    svc = RiskMitigationStrategyService()
    return svc.calculate_aggregate_metrics()

# ==================== ActionOwnerAssignment Endpoints ====================
@router.get("/actionownerassignments", response_model=List[Dict[str, Any]])
def list_actionownerassignments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ActionOwnerAssignment records with pagination and filtering."""
    svc = ActionOwnerAssignmentService()
    items = svc.list_actionownerassignments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/actionownerassignments/{item_id}", response_model=Dict[str, Any])
def get_actionownerassignment_by_id(item_id: int):
    """Retrieve detailed record for ActionOwnerAssignment by ID."""
    svc = ActionOwnerAssignmentService()
    item = svc.get_actionownerassignment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ActionOwnerAssignment with ID {item_id} not found")
    return item.to_dict()

@router.post("/actionownerassignments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_actionownerassignment(payload: ActionOwnerAssignmentCreateSchema):
    """Create new ActionOwnerAssignment instance in enterprise repository."""
    svc = ActionOwnerAssignmentService()
    try:
        item = svc.create_actionownerassignment(
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

@router.put("/actionownerassignments/{item_id}", response_model=Dict[str, Any])
def update_actionownerassignment(item_id: int, payload: ActionOwnerAssignmentUpdateSchema):
    """Update existing ActionOwnerAssignment record fields."""
    svc = ActionOwnerAssignmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_actionownerassignment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ActionOwnerAssignment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/actionownerassignments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_actionownerassignment(item_id: int, hard: bool = Query(False)):
    """Delete ActionOwnerAssignment record (soft-delete by default)."""
    svc = ActionOwnerAssignmentService()
    ok = svc.delete_actionownerassignment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ActionOwnerAssignment with ID {item_id} not found")
    return None

@router.get("/actionownerassignments/analytics/metrics", response_model=Dict[str, Any])
def get_actionownerassignment_metrics():
    """Calculate summary statistical KPIs for ActionOwnerAssignment collection."""
    svc = ActionOwnerAssignmentService()
    return svc.calculate_aggregate_metrics()

# ==================== ScenarioStressTest Endpoints ====================
@router.get("/scenariostresstests", response_model=List[Dict[str, Any]])
def list_scenariostresstests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ScenarioStressTest records with pagination and filtering."""
    svc = ScenarioStressTestService()
    items = svc.list_scenariostresstests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/scenariostresstests/{item_id}", response_model=Dict[str, Any])
def get_scenariostresstest_by_id(item_id: int):
    """Retrieve detailed record for ScenarioStressTest by ID."""
    svc = ScenarioStressTestService()
    item = svc.get_scenariostresstest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ScenarioStressTest with ID {item_id} not found")
    return item.to_dict()

@router.post("/scenariostresstests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_scenariostresstest(payload: ScenarioStressTestCreateSchema):
    """Create new ScenarioStressTest instance in enterprise repository."""
    svc = ScenarioStressTestService()
    try:
        item = svc.create_scenariostresstest(
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

@router.put("/scenariostresstests/{item_id}", response_model=Dict[str, Any])
def update_scenariostresstest(item_id: int, payload: ScenarioStressTestUpdateSchema):
    """Update existing ScenarioStressTest record fields."""
    svc = ScenarioStressTestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_scenariostresstest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ScenarioStressTest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/scenariostresstests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scenariostresstest(item_id: int, hard: bool = Query(False)):
    """Delete ScenarioStressTest record (soft-delete by default)."""
    svc = ScenarioStressTestService()
    ok = svc.delete_scenariostresstest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ScenarioStressTest with ID {item_id} not found")
    return None

@router.get("/scenariostresstests/analytics/metrics", response_model=Dict[str, Any])
def get_scenariostresstest_metrics():
    """Calculate summary statistical KPIs for ScenarioStressTest collection."""
    svc = ScenarioStressTestService()
    return svc.calculate_aggregate_metrics()

# ==================== LossEventIncident Endpoints ====================
@router.get("/losseventincidents", response_model=List[Dict[str, Any]])
def list_losseventincidents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LossEventIncident records with pagination and filtering."""
    svc = LossEventIncidentService()
    items = svc.list_losseventincidents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/losseventincidents/{item_id}", response_model=Dict[str, Any])
def get_losseventincident_by_id(item_id: int):
    """Retrieve detailed record for LossEventIncident by ID."""
    svc = LossEventIncidentService()
    item = svc.get_losseventincident_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LossEventIncident with ID {item_id} not found")
    return item.to_dict()

@router.post("/losseventincidents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_losseventincident(payload: LossEventIncidentCreateSchema):
    """Create new LossEventIncident instance in enterprise repository."""
    svc = LossEventIncidentService()
    try:
        item = svc.create_losseventincident(
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

@router.put("/losseventincidents/{item_id}", response_model=Dict[str, Any])
def update_losseventincident(item_id: int, payload: LossEventIncidentUpdateSchema):
    """Update existing LossEventIncident record fields."""
    svc = LossEventIncidentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_losseventincident(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LossEventIncident with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/losseventincidents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_losseventincident(item_id: int, hard: bool = Query(False)):
    """Delete LossEventIncident record (soft-delete by default)."""
    svc = LossEventIncidentService()
    ok = svc.delete_losseventincident(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LossEventIncident with ID {item_id} not found")
    return None

@router.get("/losseventincidents/analytics/metrics", response_model=Dict[str, Any])
def get_losseventincident_metrics():
    """Calculate summary statistical KPIs for LossEventIncident collection."""
    svc = LossEventIncidentService()
    return svc.calculate_aggregate_metrics()

# ==================== BusinessContinuityPlan Endpoints ====================
@router.get("/businesscontinuityplans", response_model=List[Dict[str, Any]])
def list_businesscontinuityplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BusinessContinuityPlan records with pagination and filtering."""
    svc = BusinessContinuityPlanService()
    items = svc.list_businesscontinuityplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/businesscontinuityplans/{item_id}", response_model=Dict[str, Any])
def get_businesscontinuityplan_by_id(item_id: int):
    """Retrieve detailed record for BusinessContinuityPlan by ID."""
    svc = BusinessContinuityPlanService()
    item = svc.get_businesscontinuityplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BusinessContinuityPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/businesscontinuityplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_businesscontinuityplan(payload: BusinessContinuityPlanCreateSchema):
    """Create new BusinessContinuityPlan instance in enterprise repository."""
    svc = BusinessContinuityPlanService()
    try:
        item = svc.create_businesscontinuityplan(
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

@router.put("/businesscontinuityplans/{item_id}", response_model=Dict[str, Any])
def update_businesscontinuityplan(item_id: int, payload: BusinessContinuityPlanUpdateSchema):
    """Update existing BusinessContinuityPlan record fields."""
    svc = BusinessContinuityPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_businesscontinuityplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BusinessContinuityPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/businesscontinuityplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_businesscontinuityplan(item_id: int, hard: bool = Query(False)):
    """Delete BusinessContinuityPlan record (soft-delete by default)."""
    svc = BusinessContinuityPlanService()
    ok = svc.delete_businesscontinuityplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BusinessContinuityPlan with ID {item_id} not found")
    return None

@router.get("/businesscontinuityplans/analytics/metrics", response_model=Dict[str, Any])
def get_businesscontinuityplan_metrics():
    """Calculate summary statistical KPIs for BusinessContinuityPlan collection."""
    svc = BusinessContinuityPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== DisasterRecoveryScenario Endpoints ====================
@router.get("/disasterrecoveryscenarios", response_model=List[Dict[str, Any]])
def list_disasterrecoveryscenarios(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DisasterRecoveryScenario records with pagination and filtering."""
    svc = DisasterRecoveryScenarioService()
    items = svc.list_disasterrecoveryscenarios(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/disasterrecoveryscenarios/{item_id}", response_model=Dict[str, Any])
def get_disasterrecoveryscenario_by_id(item_id: int):
    """Retrieve detailed record for DisasterRecoveryScenario by ID."""
    svc = DisasterRecoveryScenarioService()
    item = svc.get_disasterrecoveryscenario_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DisasterRecoveryScenario with ID {item_id} not found")
    return item.to_dict()

@router.post("/disasterrecoveryscenarios", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_disasterrecoveryscenario(payload: DisasterRecoveryScenarioCreateSchema):
    """Create new DisasterRecoveryScenario instance in enterprise repository."""
    svc = DisasterRecoveryScenarioService()
    try:
        item = svc.create_disasterrecoveryscenario(
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

@router.put("/disasterrecoveryscenarios/{item_id}", response_model=Dict[str, Any])
def update_disasterrecoveryscenario(item_id: int, payload: DisasterRecoveryScenarioUpdateSchema):
    """Update existing DisasterRecoveryScenario record fields."""
    svc = DisasterRecoveryScenarioService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_disasterrecoveryscenario(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DisasterRecoveryScenario with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/disasterrecoveryscenarios/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_disasterrecoveryscenario(item_id: int, hard: bool = Query(False)):
    """Delete DisasterRecoveryScenario record (soft-delete by default)."""
    svc = DisasterRecoveryScenarioService()
    ok = svc.delete_disasterrecoveryscenario(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DisasterRecoveryScenario with ID {item_id} not found")
    return None

@router.get("/disasterrecoveryscenarios/analytics/metrics", response_model=Dict[str, Any])
def get_disasterrecoveryscenario_metrics():
    """Calculate summary statistical KPIs for DisasterRecoveryScenario collection."""
    svc = DisasterRecoveryScenarioService()
    return svc.calculate_aggregate_metrics()

# ==================== ResidualRiskEvaluation Endpoints ====================
@router.get("/residualriskevaluations", response_model=List[Dict[str, Any]])
def list_residualriskevaluations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ResidualRiskEvaluation records with pagination and filtering."""
    svc = ResidualRiskEvaluationService()
    items = svc.list_residualriskevaluations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/residualriskevaluations/{item_id}", response_model=Dict[str, Any])
def get_residualriskevaluation_by_id(item_id: int):
    """Retrieve detailed record for ResidualRiskEvaluation by ID."""
    svc = ResidualRiskEvaluationService()
    item = svc.get_residualriskevaluation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ResidualRiskEvaluation with ID {item_id} not found")
    return item.to_dict()

@router.post("/residualriskevaluations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_residualriskevaluation(payload: ResidualRiskEvaluationCreateSchema):
    """Create new ResidualRiskEvaluation instance in enterprise repository."""
    svc = ResidualRiskEvaluationService()
    try:
        item = svc.create_residualriskevaluation(
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

@router.put("/residualriskevaluations/{item_id}", response_model=Dict[str, Any])
def update_residualriskevaluation(item_id: int, payload: ResidualRiskEvaluationUpdateSchema):
    """Update existing ResidualRiskEvaluation record fields."""
    svc = ResidualRiskEvaluationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_residualriskevaluation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ResidualRiskEvaluation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/residualriskevaluations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_residualriskevaluation(item_id: int, hard: bool = Query(False)):
    """Delete ResidualRiskEvaluation record (soft-delete by default)."""
    svc = ResidualRiskEvaluationService()
    ok = svc.delete_residualriskevaluation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ResidualRiskEvaluation with ID {item_id} not found")
    return None

@router.get("/residualriskevaluations/analytics/metrics", response_model=Dict[str, Any])
def get_residualriskevaluation_metrics():
    """Calculate summary statistical KPIs for ResidualRiskEvaluation collection."""
    svc = ResidualRiskEvaluationService()
    return svc.calculate_aggregate_metrics()

# ==================== RiskAppetiteStatement Endpoints ====================
@router.get("/riskappetitestatements", response_model=List[Dict[str, Any]])
def list_riskappetitestatements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RiskAppetiteStatement records with pagination and filtering."""
    svc = RiskAppetiteStatementService()
    items = svc.list_riskappetitestatements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/riskappetitestatements/{item_id}", response_model=Dict[str, Any])
def get_riskappetitestatement_by_id(item_id: int):
    """Retrieve detailed record for RiskAppetiteStatement by ID."""
    svc = RiskAppetiteStatementService()
    item = svc.get_riskappetitestatement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RiskAppetiteStatement with ID {item_id} not found")
    return item.to_dict()

@router.post("/riskappetitestatements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_riskappetitestatement(payload: RiskAppetiteStatementCreateSchema):
    """Create new RiskAppetiteStatement instance in enterprise repository."""
    svc = RiskAppetiteStatementService()
    try:
        item = svc.create_riskappetitestatement(
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

@router.put("/riskappetitestatements/{item_id}", response_model=Dict[str, Any])
def update_riskappetitestatement(item_id: int, payload: RiskAppetiteStatementUpdateSchema):
    """Update existing RiskAppetiteStatement record fields."""
    svc = RiskAppetiteStatementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_riskappetitestatement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RiskAppetiteStatement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/riskappetitestatements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_riskappetitestatement(item_id: int, hard: bool = Query(False)):
    """Delete RiskAppetiteStatement record (soft-delete by default)."""
    svc = RiskAppetiteStatementService()
    ok = svc.delete_riskappetitestatement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RiskAppetiteStatement with ID {item_id} not found")
    return None

@router.get("/riskappetitestatements/analytics/metrics", response_model=Dict[str, Any])
def get_riskappetitestatement_metrics():
    """Calculate summary statistical KPIs for RiskAppetiteStatement collection."""
    svc = RiskAppetiteStatementService()
    return svc.calculate_aggregate_metrics()

# ==================== InsuranceCoverageLink Endpoints ====================
@router.get("/insurancecoveragelinks", response_model=List[Dict[str, Any]])
def list_insurancecoveragelinks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InsuranceCoverageLink records with pagination and filtering."""
    svc = InsuranceCoverageLinkService()
    items = svc.list_insurancecoveragelinks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/insurancecoveragelinks/{item_id}", response_model=Dict[str, Any])
def get_insurancecoveragelink_by_id(item_id: int):
    """Retrieve detailed record for InsuranceCoverageLink by ID."""
    svc = InsuranceCoverageLinkService()
    item = svc.get_insurancecoveragelink_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InsuranceCoverageLink with ID {item_id} not found")
    return item.to_dict()

@router.post("/insurancecoveragelinks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_insurancecoveragelink(payload: InsuranceCoverageLinkCreateSchema):
    """Create new InsuranceCoverageLink instance in enterprise repository."""
    svc = InsuranceCoverageLinkService()
    try:
        item = svc.create_insurancecoveragelink(
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

@router.put("/insurancecoveragelinks/{item_id}", response_model=Dict[str, Any])
def update_insurancecoveragelink(item_id: int, payload: InsuranceCoverageLinkUpdateSchema):
    """Update existing InsuranceCoverageLink record fields."""
    svc = InsuranceCoverageLinkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_insurancecoveragelink(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InsuranceCoverageLink with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/insurancecoveragelinks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurancecoveragelink(item_id: int, hard: bool = Query(False)):
    """Delete InsuranceCoverageLink record (soft-delete by default)."""
    svc = InsuranceCoverageLinkService()
    ok = svc.delete_insurancecoveragelink(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InsuranceCoverageLink with ID {item_id} not found")
    return None

@router.get("/insurancecoveragelinks/analytics/metrics", response_model=Dict[str, Any])
def get_insurancecoveragelink_metrics():
    """Calculate summary statistical KPIs for InsuranceCoverageLink collection."""
    svc = InsuranceCoverageLinkService()
    return svc.calculate_aggregate_metrics()

# ==================== RiskCommitteeReport Endpoints ====================
@router.get("/riskcommitteereports", response_model=List[Dict[str, Any]])
def list_riskcommitteereports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RiskCommitteeReport records with pagination and filtering."""
    svc = RiskCommitteeReportService()
    items = svc.list_riskcommitteereports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/riskcommitteereports/{item_id}", response_model=Dict[str, Any])
def get_riskcommitteereport_by_id(item_id: int):
    """Retrieve detailed record for RiskCommitteeReport by ID."""
    svc = RiskCommitteeReportService()
    item = svc.get_riskcommitteereport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RiskCommitteeReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/riskcommitteereports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_riskcommitteereport(payload: RiskCommitteeReportCreateSchema):
    """Create new RiskCommitteeReport instance in enterprise repository."""
    svc = RiskCommitteeReportService()
    try:
        item = svc.create_riskcommitteereport(
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

@router.put("/riskcommitteereports/{item_id}", response_model=Dict[str, Any])
def update_riskcommitteereport(item_id: int, payload: RiskCommitteeReportUpdateSchema):
    """Update existing RiskCommitteeReport record fields."""
    svc = RiskCommitteeReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_riskcommitteereport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RiskCommitteeReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/riskcommitteereports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_riskcommitteereport(item_id: int, hard: bool = Query(False)):
    """Delete RiskCommitteeReport record (soft-delete by default)."""
    svc = RiskCommitteeReportService()
    ok = svc.delete_riskcommitteereport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RiskCommitteeReport with ID {item_id} not found")
    return None

@router.get("/riskcommitteereports/analytics/metrics", response_model=Dict[str, Any])
def get_riskcommitteereport_metrics():
    """Calculate summary statistical KPIs for RiskCommitteeReport collection."""
    svc = RiskCommitteeReportService()
    return svc.calculate_aggregate_metrics()

# ==================== AuditRecommendation Endpoints ====================
@router.get("/auditrecommendations", response_model=List[Dict[str, Any]])
def list_auditrecommendations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AuditRecommendation records with pagination and filtering."""
    svc = AuditRecommendationService()
    items = svc.list_auditrecommendations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/auditrecommendations/{item_id}", response_model=Dict[str, Any])
def get_auditrecommendation_by_id(item_id: int):
    """Retrieve detailed record for AuditRecommendation by ID."""
    svc = AuditRecommendationService()
    item = svc.get_auditrecommendation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AuditRecommendation with ID {item_id} not found")
    return item.to_dict()

@router.post("/auditrecommendations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_auditrecommendation(payload: AuditRecommendationCreateSchema):
    """Create new AuditRecommendation instance in enterprise repository."""
    svc = AuditRecommendationService()
    try:
        item = svc.create_auditrecommendation(
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

@router.put("/auditrecommendations/{item_id}", response_model=Dict[str, Any])
def update_auditrecommendation(item_id: int, payload: AuditRecommendationUpdateSchema):
    """Update existing AuditRecommendation record fields."""
    svc = AuditRecommendationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_auditrecommendation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AuditRecommendation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/auditrecommendations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_auditrecommendation(item_id: int, hard: bool = Query(False)):
    """Delete AuditRecommendation record (soft-delete by default)."""
    svc = AuditRecommendationService()
    ok = svc.delete_auditrecommendation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AuditRecommendation with ID {item_id} not found")
    return None

@router.get("/auditrecommendations/analytics/metrics", response_model=Dict[str, Any])
def get_auditrecommendation_metrics():
    """Calculate summary statistical KPIs for AuditRecommendation collection."""
    svc = AuditRecommendationService()
    return svc.calculate_aggregate_metrics()

