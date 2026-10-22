"""
Customer Success & Retention Engineering - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    CustomerHealthScoreService,
    OnboardingMilestonePlanService,
    QuarterlyBusinessReviewService,
    NPSFeedbackSurveyService,
    ChurnEarlyWarningSignalService,
    AccountExpansionDealService,
    ProductAdoptionMetricService,
    CustomerJourneyTouchpointService,
    SupportEscalationFlagService,
    SuccessPlanObjectiveService,
    ClientReferenceAdvocateService,
    RenewalForecastPipelineService,
    ProductUsageAnalyticsService,
    CustomerEngagementScoreService,
    VoiceOfCustomerFeedbackService,
    SuccessExecutiveAssignmentService,
)
from .schemas import (
    CustomerHealthScoreCreateSchema, CustomerHealthScoreUpdateSchema, CustomerHealthScoreResponseSchema,
    OnboardingMilestonePlanCreateSchema, OnboardingMilestonePlanUpdateSchema, OnboardingMilestonePlanResponseSchema,
    QuarterlyBusinessReviewCreateSchema, QuarterlyBusinessReviewUpdateSchema, QuarterlyBusinessReviewResponseSchema,
    NPSFeedbackSurveyCreateSchema, NPSFeedbackSurveyUpdateSchema, NPSFeedbackSurveyResponseSchema,
    ChurnEarlyWarningSignalCreateSchema, ChurnEarlyWarningSignalUpdateSchema, ChurnEarlyWarningSignalResponseSchema,
    AccountExpansionDealCreateSchema, AccountExpansionDealUpdateSchema, AccountExpansionDealResponseSchema,
    ProductAdoptionMetricCreateSchema, ProductAdoptionMetricUpdateSchema, ProductAdoptionMetricResponseSchema,
    CustomerJourneyTouchpointCreateSchema, CustomerJourneyTouchpointUpdateSchema, CustomerJourneyTouchpointResponseSchema,
    SupportEscalationFlagCreateSchema, SupportEscalationFlagUpdateSchema, SupportEscalationFlagResponseSchema,
    SuccessPlanObjectiveCreateSchema, SuccessPlanObjectiveUpdateSchema, SuccessPlanObjectiveResponseSchema,
    ClientReferenceAdvocateCreateSchema, ClientReferenceAdvocateUpdateSchema, ClientReferenceAdvocateResponseSchema,
    RenewalForecastPipelineCreateSchema, RenewalForecastPipelineUpdateSchema, RenewalForecastPipelineResponseSchema,
    ProductUsageAnalyticsCreateSchema, ProductUsageAnalyticsUpdateSchema, ProductUsageAnalyticsResponseSchema,
    CustomerEngagementScoreCreateSchema, CustomerEngagementScoreUpdateSchema, CustomerEngagementScoreResponseSchema,
    VoiceOfCustomerFeedbackCreateSchema, VoiceOfCustomerFeedbackUpdateSchema, VoiceOfCustomerFeedbackResponseSchema,
    SuccessExecutiveAssignmentCreateSchema, SuccessExecutiveAssignmentUpdateSchema, SuccessExecutiveAssignmentResponseSchema,
)

router = APIRouter(prefix="/customer_success", tags=["Customer Success & Retention Engineering"])

# ==================== CustomerHealthScore Endpoints ====================
@router.get("/customerhealthscores", response_model=List[Dict[str, Any]])
def list_customerhealthscores(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerHealthScore records with pagination and filtering."""
    svc = CustomerHealthScoreService()
    items = svc.list_customerhealthscores(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerhealthscores/{item_id}", response_model=Dict[str, Any])
def get_customerhealthscore_by_id(item_id: int):
    """Retrieve detailed record for CustomerHealthScore by ID."""
    svc = CustomerHealthScoreService()
    item = svc.get_customerhealthscore_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerHealthScore with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerhealthscores", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerhealthscore(payload: CustomerHealthScoreCreateSchema):
    """Create new CustomerHealthScore instance in enterprise repository."""
    svc = CustomerHealthScoreService()
    try:
        item = svc.create_customerhealthscore(
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

@router.put("/customerhealthscores/{item_id}", response_model=Dict[str, Any])
def update_customerhealthscore(item_id: int, payload: CustomerHealthScoreUpdateSchema):
    """Update existing CustomerHealthScore record fields."""
    svc = CustomerHealthScoreService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerhealthscore(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerHealthScore with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerhealthscores/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerhealthscore(item_id: int, hard: bool = Query(False)):
    """Delete CustomerHealthScore record (soft-delete by default)."""
    svc = CustomerHealthScoreService()
    ok = svc.delete_customerhealthscore(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerHealthScore with ID {item_id} not found")
    return None

@router.get("/customerhealthscores/analytics/metrics", response_model=Dict[str, Any])
def get_customerhealthscore_metrics():
    """Calculate summary statistical KPIs for CustomerHealthScore collection."""
    svc = CustomerHealthScoreService()
    return svc.calculate_aggregate_metrics()

# ==================== OnboardingMilestonePlan Endpoints ====================
@router.get("/onboardingmilestoneplans", response_model=List[Dict[str, Any]])
def list_onboardingmilestoneplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OnboardingMilestonePlan records with pagination and filtering."""
    svc = OnboardingMilestonePlanService()
    items = svc.list_onboardingmilestoneplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/onboardingmilestoneplans/{item_id}", response_model=Dict[str, Any])
def get_onboardingmilestoneplan_by_id(item_id: int):
    """Retrieve detailed record for OnboardingMilestonePlan by ID."""
    svc = OnboardingMilestonePlanService()
    item = svc.get_onboardingmilestoneplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OnboardingMilestonePlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/onboardingmilestoneplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_onboardingmilestoneplan(payload: OnboardingMilestonePlanCreateSchema):
    """Create new OnboardingMilestonePlan instance in enterprise repository."""
    svc = OnboardingMilestonePlanService()
    try:
        item = svc.create_onboardingmilestoneplan(
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

@router.put("/onboardingmilestoneplans/{item_id}", response_model=Dict[str, Any])
def update_onboardingmilestoneplan(item_id: int, payload: OnboardingMilestonePlanUpdateSchema):
    """Update existing OnboardingMilestonePlan record fields."""
    svc = OnboardingMilestonePlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_onboardingmilestoneplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OnboardingMilestonePlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/onboardingmilestoneplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_onboardingmilestoneplan(item_id: int, hard: bool = Query(False)):
    """Delete OnboardingMilestonePlan record (soft-delete by default)."""
    svc = OnboardingMilestonePlanService()
    ok = svc.delete_onboardingmilestoneplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OnboardingMilestonePlan with ID {item_id} not found")
    return None

@router.get("/onboardingmilestoneplans/analytics/metrics", response_model=Dict[str, Any])
def get_onboardingmilestoneplan_metrics():
    """Calculate summary statistical KPIs for OnboardingMilestonePlan collection."""
    svc = OnboardingMilestonePlanService()
    return svc.calculate_aggregate_metrics()

# ==================== QuarterlyBusinessReview Endpoints ====================
@router.get("/quarterlybusinessreviews", response_model=List[Dict[str, Any]])
def list_quarterlybusinessreviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List QuarterlyBusinessReview records with pagination and filtering."""
    svc = QuarterlyBusinessReviewService()
    items = svc.list_quarterlybusinessreviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/quarterlybusinessreviews/{item_id}", response_model=Dict[str, Any])
def get_quarterlybusinessreview_by_id(item_id: int):
    """Retrieve detailed record for QuarterlyBusinessReview by ID."""
    svc = QuarterlyBusinessReviewService()
    item = svc.get_quarterlybusinessreview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"QuarterlyBusinessReview with ID {item_id} not found")
    return item.to_dict()

@router.post("/quarterlybusinessreviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_quarterlybusinessreview(payload: QuarterlyBusinessReviewCreateSchema):
    """Create new QuarterlyBusinessReview instance in enterprise repository."""
    svc = QuarterlyBusinessReviewService()
    try:
        item = svc.create_quarterlybusinessreview(
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

@router.put("/quarterlybusinessreviews/{item_id}", response_model=Dict[str, Any])
def update_quarterlybusinessreview(item_id: int, payload: QuarterlyBusinessReviewUpdateSchema):
    """Update existing QuarterlyBusinessReview record fields."""
    svc = QuarterlyBusinessReviewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_quarterlybusinessreview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"QuarterlyBusinessReview with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/quarterlybusinessreviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quarterlybusinessreview(item_id: int, hard: bool = Query(False)):
    """Delete QuarterlyBusinessReview record (soft-delete by default)."""
    svc = QuarterlyBusinessReviewService()
    ok = svc.delete_quarterlybusinessreview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"QuarterlyBusinessReview with ID {item_id} not found")
    return None

@router.get("/quarterlybusinessreviews/analytics/metrics", response_model=Dict[str, Any])
def get_quarterlybusinessreview_metrics():
    """Calculate summary statistical KPIs for QuarterlyBusinessReview collection."""
    svc = QuarterlyBusinessReviewService()
    return svc.calculate_aggregate_metrics()

# ==================== NPSFeedbackSurvey Endpoints ====================
@router.get("/npsfeedbacksurveys", response_model=List[Dict[str, Any]])
def list_npsfeedbacksurveys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List NPSFeedbackSurvey records with pagination and filtering."""
    svc = NPSFeedbackSurveyService()
    items = svc.list_npsfeedbacksurveys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/npsfeedbacksurveys/{item_id}", response_model=Dict[str, Any])
def get_npsfeedbacksurvey_by_id(item_id: int):
    """Retrieve detailed record for NPSFeedbackSurvey by ID."""
    svc = NPSFeedbackSurveyService()
    item = svc.get_npsfeedbacksurvey_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"NPSFeedbackSurvey with ID {item_id} not found")
    return item.to_dict()

@router.post("/npsfeedbacksurveys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_npsfeedbacksurvey(payload: NPSFeedbackSurveyCreateSchema):
    """Create new NPSFeedbackSurvey instance in enterprise repository."""
    svc = NPSFeedbackSurveyService()
    try:
        item = svc.create_npsfeedbacksurvey(
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

@router.put("/npsfeedbacksurveys/{item_id}", response_model=Dict[str, Any])
def update_npsfeedbacksurvey(item_id: int, payload: NPSFeedbackSurveyUpdateSchema):
    """Update existing NPSFeedbackSurvey record fields."""
    svc = NPSFeedbackSurveyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_npsfeedbacksurvey(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"NPSFeedbackSurvey with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/npsfeedbacksurveys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_npsfeedbacksurvey(item_id: int, hard: bool = Query(False)):
    """Delete NPSFeedbackSurvey record (soft-delete by default)."""
    svc = NPSFeedbackSurveyService()
    ok = svc.delete_npsfeedbacksurvey(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"NPSFeedbackSurvey with ID {item_id} not found")
    return None

@router.get("/npsfeedbacksurveys/analytics/metrics", response_model=Dict[str, Any])
def get_npsfeedbacksurvey_metrics():
    """Calculate summary statistical KPIs for NPSFeedbackSurvey collection."""
    svc = NPSFeedbackSurveyService()
    return svc.calculate_aggregate_metrics()

# ==================== ChurnEarlyWarningSignal Endpoints ====================
@router.get("/churnearlywarningsignals", response_model=List[Dict[str, Any]])
def list_churnearlywarningsignals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChurnEarlyWarningSignal records with pagination and filtering."""
    svc = ChurnEarlyWarningSignalService()
    items = svc.list_churnearlywarningsignals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/churnearlywarningsignals/{item_id}", response_model=Dict[str, Any])
def get_churnearlywarningsignal_by_id(item_id: int):
    """Retrieve detailed record for ChurnEarlyWarningSignal by ID."""
    svc = ChurnEarlyWarningSignalService()
    item = svc.get_churnearlywarningsignal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChurnEarlyWarningSignal with ID {item_id} not found")
    return item.to_dict()

@router.post("/churnearlywarningsignals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_churnearlywarningsignal(payload: ChurnEarlyWarningSignalCreateSchema):
    """Create new ChurnEarlyWarningSignal instance in enterprise repository."""
    svc = ChurnEarlyWarningSignalService()
    try:
        item = svc.create_churnearlywarningsignal(
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

@router.put("/churnearlywarningsignals/{item_id}", response_model=Dict[str, Any])
def update_churnearlywarningsignal(item_id: int, payload: ChurnEarlyWarningSignalUpdateSchema):
    """Update existing ChurnEarlyWarningSignal record fields."""
    svc = ChurnEarlyWarningSignalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_churnearlywarningsignal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChurnEarlyWarningSignal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/churnearlywarningsignals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_churnearlywarningsignal(item_id: int, hard: bool = Query(False)):
    """Delete ChurnEarlyWarningSignal record (soft-delete by default)."""
    svc = ChurnEarlyWarningSignalService()
    ok = svc.delete_churnearlywarningsignal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChurnEarlyWarningSignal with ID {item_id} not found")
    return None

@router.get("/churnearlywarningsignals/analytics/metrics", response_model=Dict[str, Any])
def get_churnearlywarningsignal_metrics():
    """Calculate summary statistical KPIs for ChurnEarlyWarningSignal collection."""
    svc = ChurnEarlyWarningSignalService()
    return svc.calculate_aggregate_metrics()

# ==================== AccountExpansionDeal Endpoints ====================
@router.get("/accountexpansiondeals", response_model=List[Dict[str, Any]])
def list_accountexpansiondeals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AccountExpansionDeal records with pagination and filtering."""
    svc = AccountExpansionDealService()
    items = svc.list_accountexpansiondeals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/accountexpansiondeals/{item_id}", response_model=Dict[str, Any])
def get_accountexpansiondeal_by_id(item_id: int):
    """Retrieve detailed record for AccountExpansionDeal by ID."""
    svc = AccountExpansionDealService()
    item = svc.get_accountexpansiondeal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AccountExpansionDeal with ID {item_id} not found")
    return item.to_dict()

@router.post("/accountexpansiondeals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_accountexpansiondeal(payload: AccountExpansionDealCreateSchema):
    """Create new AccountExpansionDeal instance in enterprise repository."""
    svc = AccountExpansionDealService()
    try:
        item = svc.create_accountexpansiondeal(
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

@router.put("/accountexpansiondeals/{item_id}", response_model=Dict[str, Any])
def update_accountexpansiondeal(item_id: int, payload: AccountExpansionDealUpdateSchema):
    """Update existing AccountExpansionDeal record fields."""
    svc = AccountExpansionDealService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_accountexpansiondeal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AccountExpansionDeal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/accountexpansiondeals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accountexpansiondeal(item_id: int, hard: bool = Query(False)):
    """Delete AccountExpansionDeal record (soft-delete by default)."""
    svc = AccountExpansionDealService()
    ok = svc.delete_accountexpansiondeal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AccountExpansionDeal with ID {item_id} not found")
    return None

@router.get("/accountexpansiondeals/analytics/metrics", response_model=Dict[str, Any])
def get_accountexpansiondeal_metrics():
    """Calculate summary statistical KPIs for AccountExpansionDeal collection."""
    svc = AccountExpansionDealService()
    return svc.calculate_aggregate_metrics()

# ==================== ProductAdoptionMetric Endpoints ====================
@router.get("/productadoptionmetrics", response_model=List[Dict[str, Any]])
def list_productadoptionmetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProductAdoptionMetric records with pagination and filtering."""
    svc = ProductAdoptionMetricService()
    items = svc.list_productadoptionmetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/productadoptionmetrics/{item_id}", response_model=Dict[str, Any])
def get_productadoptionmetric_by_id(item_id: int):
    """Retrieve detailed record for ProductAdoptionMetric by ID."""
    svc = ProductAdoptionMetricService()
    item = svc.get_productadoptionmetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProductAdoptionMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/productadoptionmetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_productadoptionmetric(payload: ProductAdoptionMetricCreateSchema):
    """Create new ProductAdoptionMetric instance in enterprise repository."""
    svc = ProductAdoptionMetricService()
    try:
        item = svc.create_productadoptionmetric(
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

@router.put("/productadoptionmetrics/{item_id}", response_model=Dict[str, Any])
def update_productadoptionmetric(item_id: int, payload: ProductAdoptionMetricUpdateSchema):
    """Update existing ProductAdoptionMetric record fields."""
    svc = ProductAdoptionMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_productadoptionmetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProductAdoptionMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/productadoptionmetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_productadoptionmetric(item_id: int, hard: bool = Query(False)):
    """Delete ProductAdoptionMetric record (soft-delete by default)."""
    svc = ProductAdoptionMetricService()
    ok = svc.delete_productadoptionmetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProductAdoptionMetric with ID {item_id} not found")
    return None

@router.get("/productadoptionmetrics/analytics/metrics", response_model=Dict[str, Any])
def get_productadoptionmetric_metrics():
    """Calculate summary statistical KPIs for ProductAdoptionMetric collection."""
    svc = ProductAdoptionMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerJourneyTouchpoint Endpoints ====================
@router.get("/customerjourneytouchpoints", response_model=List[Dict[str, Any]])
def list_customerjourneytouchpoints(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerJourneyTouchpoint records with pagination and filtering."""
    svc = CustomerJourneyTouchpointService()
    items = svc.list_customerjourneytouchpoints(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerjourneytouchpoints/{item_id}", response_model=Dict[str, Any])
def get_customerjourneytouchpoint_by_id(item_id: int):
    """Retrieve detailed record for CustomerJourneyTouchpoint by ID."""
    svc = CustomerJourneyTouchpointService()
    item = svc.get_customerjourneytouchpoint_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerJourneyTouchpoint with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerjourneytouchpoints", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerjourneytouchpoint(payload: CustomerJourneyTouchpointCreateSchema):
    """Create new CustomerJourneyTouchpoint instance in enterprise repository."""
    svc = CustomerJourneyTouchpointService()
    try:
        item = svc.create_customerjourneytouchpoint(
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

@router.put("/customerjourneytouchpoints/{item_id}", response_model=Dict[str, Any])
def update_customerjourneytouchpoint(item_id: int, payload: CustomerJourneyTouchpointUpdateSchema):
    """Update existing CustomerJourneyTouchpoint record fields."""
    svc = CustomerJourneyTouchpointService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerjourneytouchpoint(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerJourneyTouchpoint with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerjourneytouchpoints/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerjourneytouchpoint(item_id: int, hard: bool = Query(False)):
    """Delete CustomerJourneyTouchpoint record (soft-delete by default)."""
    svc = CustomerJourneyTouchpointService()
    ok = svc.delete_customerjourneytouchpoint(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerJourneyTouchpoint with ID {item_id} not found")
    return None

@router.get("/customerjourneytouchpoints/analytics/metrics", response_model=Dict[str, Any])
def get_customerjourneytouchpoint_metrics():
    """Calculate summary statistical KPIs for CustomerJourneyTouchpoint collection."""
    svc = CustomerJourneyTouchpointService()
    return svc.calculate_aggregate_metrics()

# ==================== SupportEscalationFlag Endpoints ====================
@router.get("/supportescalationflags", response_model=List[Dict[str, Any]])
def list_supportescalationflags(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupportEscalationFlag records with pagination and filtering."""
    svc = SupportEscalationFlagService()
    items = svc.list_supportescalationflags(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supportescalationflags/{item_id}", response_model=Dict[str, Any])
def get_supportescalationflag_by_id(item_id: int):
    """Retrieve detailed record for SupportEscalationFlag by ID."""
    svc = SupportEscalationFlagService()
    item = svc.get_supportescalationflag_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupportEscalationFlag with ID {item_id} not found")
    return item.to_dict()

@router.post("/supportescalationflags", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supportescalationflag(payload: SupportEscalationFlagCreateSchema):
    """Create new SupportEscalationFlag instance in enterprise repository."""
    svc = SupportEscalationFlagService()
    try:
        item = svc.create_supportescalationflag(
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

@router.put("/supportescalationflags/{item_id}", response_model=Dict[str, Any])
def update_supportescalationflag(item_id: int, payload: SupportEscalationFlagUpdateSchema):
    """Update existing SupportEscalationFlag record fields."""
    svc = SupportEscalationFlagService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supportescalationflag(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupportEscalationFlag with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supportescalationflags/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supportescalationflag(item_id: int, hard: bool = Query(False)):
    """Delete SupportEscalationFlag record (soft-delete by default)."""
    svc = SupportEscalationFlagService()
    ok = svc.delete_supportescalationflag(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupportEscalationFlag with ID {item_id} not found")
    return None

@router.get("/supportescalationflags/analytics/metrics", response_model=Dict[str, Any])
def get_supportescalationflag_metrics():
    """Calculate summary statistical KPIs for SupportEscalationFlag collection."""
    svc = SupportEscalationFlagService()
    return svc.calculate_aggregate_metrics()

# ==================== SuccessPlanObjective Endpoints ====================
@router.get("/successplanobjectives", response_model=List[Dict[str, Any]])
def list_successplanobjectives(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SuccessPlanObjective records with pagination and filtering."""
    svc = SuccessPlanObjectiveService()
    items = svc.list_successplanobjectives(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/successplanobjectives/{item_id}", response_model=Dict[str, Any])
def get_successplanobjective_by_id(item_id: int):
    """Retrieve detailed record for SuccessPlanObjective by ID."""
    svc = SuccessPlanObjectiveService()
    item = svc.get_successplanobjective_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SuccessPlanObjective with ID {item_id} not found")
    return item.to_dict()

@router.post("/successplanobjectives", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_successplanobjective(payload: SuccessPlanObjectiveCreateSchema):
    """Create new SuccessPlanObjective instance in enterprise repository."""
    svc = SuccessPlanObjectiveService()
    try:
        item = svc.create_successplanobjective(
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

@router.put("/successplanobjectives/{item_id}", response_model=Dict[str, Any])
def update_successplanobjective(item_id: int, payload: SuccessPlanObjectiveUpdateSchema):
    """Update existing SuccessPlanObjective record fields."""
    svc = SuccessPlanObjectiveService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_successplanobjective(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SuccessPlanObjective with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/successplanobjectives/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_successplanobjective(item_id: int, hard: bool = Query(False)):
    """Delete SuccessPlanObjective record (soft-delete by default)."""
    svc = SuccessPlanObjectiveService()
    ok = svc.delete_successplanobjective(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SuccessPlanObjective with ID {item_id} not found")
    return None

@router.get("/successplanobjectives/analytics/metrics", response_model=Dict[str, Any])
def get_successplanobjective_metrics():
    """Calculate summary statistical KPIs for SuccessPlanObjective collection."""
    svc = SuccessPlanObjectiveService()
    return svc.calculate_aggregate_metrics()

# ==================== ClientReferenceAdvocate Endpoints ====================
@router.get("/clientreferenceadvocates", response_model=List[Dict[str, Any]])
def list_clientreferenceadvocates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ClientReferenceAdvocate records with pagination and filtering."""
    svc = ClientReferenceAdvocateService()
    items = svc.list_clientreferenceadvocates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/clientreferenceadvocates/{item_id}", response_model=Dict[str, Any])
def get_clientreferenceadvocate_by_id(item_id: int):
    """Retrieve detailed record for ClientReferenceAdvocate by ID."""
    svc = ClientReferenceAdvocateService()
    item = svc.get_clientreferenceadvocate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ClientReferenceAdvocate with ID {item_id} not found")
    return item.to_dict()

@router.post("/clientreferenceadvocates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_clientreferenceadvocate(payload: ClientReferenceAdvocateCreateSchema):
    """Create new ClientReferenceAdvocate instance in enterprise repository."""
    svc = ClientReferenceAdvocateService()
    try:
        item = svc.create_clientreferenceadvocate(
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

@router.put("/clientreferenceadvocates/{item_id}", response_model=Dict[str, Any])
def update_clientreferenceadvocate(item_id: int, payload: ClientReferenceAdvocateUpdateSchema):
    """Update existing ClientReferenceAdvocate record fields."""
    svc = ClientReferenceAdvocateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_clientreferenceadvocate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ClientReferenceAdvocate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/clientreferenceadvocates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_clientreferenceadvocate(item_id: int, hard: bool = Query(False)):
    """Delete ClientReferenceAdvocate record (soft-delete by default)."""
    svc = ClientReferenceAdvocateService()
    ok = svc.delete_clientreferenceadvocate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ClientReferenceAdvocate with ID {item_id} not found")
    return None

@router.get("/clientreferenceadvocates/analytics/metrics", response_model=Dict[str, Any])
def get_clientreferenceadvocate_metrics():
    """Calculate summary statistical KPIs for ClientReferenceAdvocate collection."""
    svc = ClientReferenceAdvocateService()
    return svc.calculate_aggregate_metrics()

# ==================== RenewalForecastPipeline Endpoints ====================
@router.get("/renewalforecastpipelines", response_model=List[Dict[str, Any]])
def list_renewalforecastpipelines(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RenewalForecastPipeline records with pagination and filtering."""
    svc = RenewalForecastPipelineService()
    items = svc.list_renewalforecastpipelines(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/renewalforecastpipelines/{item_id}", response_model=Dict[str, Any])
def get_renewalforecastpipeline_by_id(item_id: int):
    """Retrieve detailed record for RenewalForecastPipeline by ID."""
    svc = RenewalForecastPipelineService()
    item = svc.get_renewalforecastpipeline_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RenewalForecastPipeline with ID {item_id} not found")
    return item.to_dict()

@router.post("/renewalforecastpipelines", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_renewalforecastpipeline(payload: RenewalForecastPipelineCreateSchema):
    """Create new RenewalForecastPipeline instance in enterprise repository."""
    svc = RenewalForecastPipelineService()
    try:
        item = svc.create_renewalforecastpipeline(
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

@router.put("/renewalforecastpipelines/{item_id}", response_model=Dict[str, Any])
def update_renewalforecastpipeline(item_id: int, payload: RenewalForecastPipelineUpdateSchema):
    """Update existing RenewalForecastPipeline record fields."""
    svc = RenewalForecastPipelineService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_renewalforecastpipeline(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RenewalForecastPipeline with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/renewalforecastpipelines/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_renewalforecastpipeline(item_id: int, hard: bool = Query(False)):
    """Delete RenewalForecastPipeline record (soft-delete by default)."""
    svc = RenewalForecastPipelineService()
    ok = svc.delete_renewalforecastpipeline(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RenewalForecastPipeline with ID {item_id} not found")
    return None

@router.get("/renewalforecastpipelines/analytics/metrics", response_model=Dict[str, Any])
def get_renewalforecastpipeline_metrics():
    """Calculate summary statistical KPIs for RenewalForecastPipeline collection."""
    svc = RenewalForecastPipelineService()
    return svc.calculate_aggregate_metrics()

# ==================== ProductUsageAnalytics Endpoints ====================
@router.get("/productusageanalyticss", response_model=List[Dict[str, Any]])
def list_productusageanalyticss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProductUsageAnalytics records with pagination and filtering."""
    svc = ProductUsageAnalyticsService()
    items = svc.list_productusageanalyticss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/productusageanalyticss/{item_id}", response_model=Dict[str, Any])
def get_productusageanalytics_by_id(item_id: int):
    """Retrieve detailed record for ProductUsageAnalytics by ID."""
    svc = ProductUsageAnalyticsService()
    item = svc.get_productusageanalytics_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProductUsageAnalytics with ID {item_id} not found")
    return item.to_dict()

@router.post("/productusageanalyticss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_productusageanalytics(payload: ProductUsageAnalyticsCreateSchema):
    """Create new ProductUsageAnalytics instance in enterprise repository."""
    svc = ProductUsageAnalyticsService()
    try:
        item = svc.create_productusageanalytics(
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

@router.put("/productusageanalyticss/{item_id}", response_model=Dict[str, Any])
def update_productusageanalytics(item_id: int, payload: ProductUsageAnalyticsUpdateSchema):
    """Update existing ProductUsageAnalytics record fields."""
    svc = ProductUsageAnalyticsService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_productusageanalytics(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProductUsageAnalytics with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/productusageanalyticss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_productusageanalytics(item_id: int, hard: bool = Query(False)):
    """Delete ProductUsageAnalytics record (soft-delete by default)."""
    svc = ProductUsageAnalyticsService()
    ok = svc.delete_productusageanalytics(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProductUsageAnalytics with ID {item_id} not found")
    return None

@router.get("/productusageanalyticss/analytics/metrics", response_model=Dict[str, Any])
def get_productusageanalytics_metrics():
    """Calculate summary statistical KPIs for ProductUsageAnalytics collection."""
    svc = ProductUsageAnalyticsService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerEngagementScore Endpoints ====================
@router.get("/customerengagementscores", response_model=List[Dict[str, Any]])
def list_customerengagementscores(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerEngagementScore records with pagination and filtering."""
    svc = CustomerEngagementScoreService()
    items = svc.list_customerengagementscores(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerengagementscores/{item_id}", response_model=Dict[str, Any])
def get_customerengagementscore_by_id(item_id: int):
    """Retrieve detailed record for CustomerEngagementScore by ID."""
    svc = CustomerEngagementScoreService()
    item = svc.get_customerengagementscore_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerEngagementScore with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerengagementscores", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerengagementscore(payload: CustomerEngagementScoreCreateSchema):
    """Create new CustomerEngagementScore instance in enterprise repository."""
    svc = CustomerEngagementScoreService()
    try:
        item = svc.create_customerengagementscore(
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

@router.put("/customerengagementscores/{item_id}", response_model=Dict[str, Any])
def update_customerengagementscore(item_id: int, payload: CustomerEngagementScoreUpdateSchema):
    """Update existing CustomerEngagementScore record fields."""
    svc = CustomerEngagementScoreService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerengagementscore(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerEngagementScore with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerengagementscores/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerengagementscore(item_id: int, hard: bool = Query(False)):
    """Delete CustomerEngagementScore record (soft-delete by default)."""
    svc = CustomerEngagementScoreService()
    ok = svc.delete_customerengagementscore(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerEngagementScore with ID {item_id} not found")
    return None

@router.get("/customerengagementscores/analytics/metrics", response_model=Dict[str, Any])
def get_customerengagementscore_metrics():
    """Calculate summary statistical KPIs for CustomerEngagementScore collection."""
    svc = CustomerEngagementScoreService()
    return svc.calculate_aggregate_metrics()

# ==================== VoiceOfCustomerFeedback Endpoints ====================
@router.get("/voiceofcustomerfeedbacks", response_model=List[Dict[str, Any]])
def list_voiceofcustomerfeedbacks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VoiceOfCustomerFeedback records with pagination and filtering."""
    svc = VoiceOfCustomerFeedbackService()
    items = svc.list_voiceofcustomerfeedbacks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/voiceofcustomerfeedbacks/{item_id}", response_model=Dict[str, Any])
def get_voiceofcustomerfeedback_by_id(item_id: int):
    """Retrieve detailed record for VoiceOfCustomerFeedback by ID."""
    svc = VoiceOfCustomerFeedbackService()
    item = svc.get_voiceofcustomerfeedback_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VoiceOfCustomerFeedback with ID {item_id} not found")
    return item.to_dict()

@router.post("/voiceofcustomerfeedbacks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_voiceofcustomerfeedback(payload: VoiceOfCustomerFeedbackCreateSchema):
    """Create new VoiceOfCustomerFeedback instance in enterprise repository."""
    svc = VoiceOfCustomerFeedbackService()
    try:
        item = svc.create_voiceofcustomerfeedback(
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

@router.put("/voiceofcustomerfeedbacks/{item_id}", response_model=Dict[str, Any])
def update_voiceofcustomerfeedback(item_id: int, payload: VoiceOfCustomerFeedbackUpdateSchema):
    """Update existing VoiceOfCustomerFeedback record fields."""
    svc = VoiceOfCustomerFeedbackService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_voiceofcustomerfeedback(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VoiceOfCustomerFeedback with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/voiceofcustomerfeedbacks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_voiceofcustomerfeedback(item_id: int, hard: bool = Query(False)):
    """Delete VoiceOfCustomerFeedback record (soft-delete by default)."""
    svc = VoiceOfCustomerFeedbackService()
    ok = svc.delete_voiceofcustomerfeedback(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VoiceOfCustomerFeedback with ID {item_id} not found")
    return None

@router.get("/voiceofcustomerfeedbacks/analytics/metrics", response_model=Dict[str, Any])
def get_voiceofcustomerfeedback_metrics():
    """Calculate summary statistical KPIs for VoiceOfCustomerFeedback collection."""
    svc = VoiceOfCustomerFeedbackService()
    return svc.calculate_aggregate_metrics()

# ==================== SuccessExecutiveAssignment Endpoints ====================
@router.get("/successexecutiveassignments", response_model=List[Dict[str, Any]])
def list_successexecutiveassignments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SuccessExecutiveAssignment records with pagination and filtering."""
    svc = SuccessExecutiveAssignmentService()
    items = svc.list_successexecutiveassignments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/successexecutiveassignments/{item_id}", response_model=Dict[str, Any])
def get_successexecutiveassignment_by_id(item_id: int):
    """Retrieve detailed record for SuccessExecutiveAssignment by ID."""
    svc = SuccessExecutiveAssignmentService()
    item = svc.get_successexecutiveassignment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SuccessExecutiveAssignment with ID {item_id} not found")
    return item.to_dict()

@router.post("/successexecutiveassignments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_successexecutiveassignment(payload: SuccessExecutiveAssignmentCreateSchema):
    """Create new SuccessExecutiveAssignment instance in enterprise repository."""
    svc = SuccessExecutiveAssignmentService()
    try:
        item = svc.create_successexecutiveassignment(
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

@router.put("/successexecutiveassignments/{item_id}", response_model=Dict[str, Any])
def update_successexecutiveassignment(item_id: int, payload: SuccessExecutiveAssignmentUpdateSchema):
    """Update existing SuccessExecutiveAssignment record fields."""
    svc = SuccessExecutiveAssignmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_successexecutiveassignment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SuccessExecutiveAssignment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/successexecutiveassignments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_successexecutiveassignment(item_id: int, hard: bool = Query(False)):
    """Delete SuccessExecutiveAssignment record (soft-delete by default)."""
    svc = SuccessExecutiveAssignmentService()
    ok = svc.delete_successexecutiveassignment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SuccessExecutiveAssignment with ID {item_id} not found")
    return None

@router.get("/successexecutiveassignments/analytics/metrics", response_model=Dict[str, Any])
def get_successexecutiveassignment_metrics():
    """Calculate summary statistical KPIs for SuccessExecutiveAssignment collection."""
    svc = SuccessExecutiveAssignmentService()
    return svc.calculate_aggregate_metrics()

