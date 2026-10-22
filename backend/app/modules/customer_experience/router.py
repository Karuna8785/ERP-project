"""
Customer Experience (CX) & Sentiment Analytics - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    CustomerJourneyMapStageService,
    CSATSurveySubmissionService,
    NPSScorecardMetricService,
    SentimentNLPAnalysisService,
    CustomerEffortScoreCESService,
    VoiceOfCustomerFeedbackService,
    OmnichannelTouchpointEventService,
    CustomerChurnPredictionService,
    SupportResolutionTimeKPIService,
    PersonalizationProfileService,
    ExperienceGapIncidentService,
    AdvocateReferralRecordService,
    RetentionCampaignTriggerService,
    FeedbackCategorizationRuleService,
    CustomerDelightActionService,
    ExecutiveCXScorecardService,
)
from .schemas import (
    CustomerJourneyMapStageCreateSchema, CustomerJourneyMapStageUpdateSchema, CustomerJourneyMapStageResponseSchema,
    CSATSurveySubmissionCreateSchema, CSATSurveySubmissionUpdateSchema, CSATSurveySubmissionResponseSchema,
    NPSScorecardMetricCreateSchema, NPSScorecardMetricUpdateSchema, NPSScorecardMetricResponseSchema,
    SentimentNLPAnalysisCreateSchema, SentimentNLPAnalysisUpdateSchema, SentimentNLPAnalysisResponseSchema,
    CustomerEffortScoreCESCreateSchema, CustomerEffortScoreCESUpdateSchema, CustomerEffortScoreCESResponseSchema,
    VoiceOfCustomerFeedbackCreateSchema, VoiceOfCustomerFeedbackUpdateSchema, VoiceOfCustomerFeedbackResponseSchema,
    OmnichannelTouchpointEventCreateSchema, OmnichannelTouchpointEventUpdateSchema, OmnichannelTouchpointEventResponseSchema,
    CustomerChurnPredictionCreateSchema, CustomerChurnPredictionUpdateSchema, CustomerChurnPredictionResponseSchema,
    SupportResolutionTimeKPICreateSchema, SupportResolutionTimeKPIUpdateSchema, SupportResolutionTimeKPIResponseSchema,
    PersonalizationProfileCreateSchema, PersonalizationProfileUpdateSchema, PersonalizationProfileResponseSchema,
    ExperienceGapIncidentCreateSchema, ExperienceGapIncidentUpdateSchema, ExperienceGapIncidentResponseSchema,
    AdvocateReferralRecordCreateSchema, AdvocateReferralRecordUpdateSchema, AdvocateReferralRecordResponseSchema,
    RetentionCampaignTriggerCreateSchema, RetentionCampaignTriggerUpdateSchema, RetentionCampaignTriggerResponseSchema,
    FeedbackCategorizationRuleCreateSchema, FeedbackCategorizationRuleUpdateSchema, FeedbackCategorizationRuleResponseSchema,
    CustomerDelightActionCreateSchema, CustomerDelightActionUpdateSchema, CustomerDelightActionResponseSchema,
    ExecutiveCXScorecardCreateSchema, ExecutiveCXScorecardUpdateSchema, ExecutiveCXScorecardResponseSchema,
)

router = APIRouter(prefix="/customer_experience", tags=["Customer Experience (CX) & Sentiment Analytics"])

# ==================== CustomerJourneyMapStage Endpoints ====================
@router.get("/customerjourneymapstages", response_model=List[Dict[str, Any]])
def list_customerjourneymapstages(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerJourneyMapStage records with pagination and filtering."""
    svc = CustomerJourneyMapStageService()
    items = svc.list_customerjourneymapstages(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerjourneymapstages/{item_id}", response_model=Dict[str, Any])
def get_customerjourneymapstage_by_id(item_id: int):
    """Retrieve detailed record for CustomerJourneyMapStage by ID."""
    svc = CustomerJourneyMapStageService()
    item = svc.get_customerjourneymapstage_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerJourneyMapStage with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerjourneymapstages", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerjourneymapstage(payload: CustomerJourneyMapStageCreateSchema):
    """Create new CustomerJourneyMapStage instance in enterprise repository."""
    svc = CustomerJourneyMapStageService()
    try:
        item = svc.create_customerjourneymapstage(
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

@router.put("/customerjourneymapstages/{item_id}", response_model=Dict[str, Any])
def update_customerjourneymapstage(item_id: int, payload: CustomerJourneyMapStageUpdateSchema):
    """Update existing CustomerJourneyMapStage record fields."""
    svc = CustomerJourneyMapStageService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerjourneymapstage(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerJourneyMapStage with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerjourneymapstages/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerjourneymapstage(item_id: int, hard: bool = Query(False)):
    """Delete CustomerJourneyMapStage record (soft-delete by default)."""
    svc = CustomerJourneyMapStageService()
    ok = svc.delete_customerjourneymapstage(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerJourneyMapStage with ID {item_id} not found")
    return None

@router.get("/customerjourneymapstages/analytics/metrics", response_model=Dict[str, Any])
def get_customerjourneymapstage_metrics():
    """Calculate summary statistical KPIs for CustomerJourneyMapStage collection."""
    svc = CustomerJourneyMapStageService()
    return svc.calculate_aggregate_metrics()

# ==================== CSATSurveySubmission Endpoints ====================
@router.get("/csatsurveysubmissions", response_model=List[Dict[str, Any]])
def list_csatsurveysubmissions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CSATSurveySubmission records with pagination and filtering."""
    svc = CSATSurveySubmissionService()
    items = svc.list_csatsurveysubmissions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/csatsurveysubmissions/{item_id}", response_model=Dict[str, Any])
def get_csatsurveysubmission_by_id(item_id: int):
    """Retrieve detailed record for CSATSurveySubmission by ID."""
    svc = CSATSurveySubmissionService()
    item = svc.get_csatsurveysubmission_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CSATSurveySubmission with ID {item_id} not found")
    return item.to_dict()

@router.post("/csatsurveysubmissions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_csatsurveysubmission(payload: CSATSurveySubmissionCreateSchema):
    """Create new CSATSurveySubmission instance in enterprise repository."""
    svc = CSATSurveySubmissionService()
    try:
        item = svc.create_csatsurveysubmission(
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

@router.put("/csatsurveysubmissions/{item_id}", response_model=Dict[str, Any])
def update_csatsurveysubmission(item_id: int, payload: CSATSurveySubmissionUpdateSchema):
    """Update existing CSATSurveySubmission record fields."""
    svc = CSATSurveySubmissionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_csatsurveysubmission(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CSATSurveySubmission with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/csatsurveysubmissions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_csatsurveysubmission(item_id: int, hard: bool = Query(False)):
    """Delete CSATSurveySubmission record (soft-delete by default)."""
    svc = CSATSurveySubmissionService()
    ok = svc.delete_csatsurveysubmission(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CSATSurveySubmission with ID {item_id} not found")
    return None

@router.get("/csatsurveysubmissions/analytics/metrics", response_model=Dict[str, Any])
def get_csatsurveysubmission_metrics():
    """Calculate summary statistical KPIs for CSATSurveySubmission collection."""
    svc = CSATSurveySubmissionService()
    return svc.calculate_aggregate_metrics()

# ==================== NPSScorecardMetric Endpoints ====================
@router.get("/npsscorecardmetrics", response_model=List[Dict[str, Any]])
def list_npsscorecardmetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List NPSScorecardMetric records with pagination and filtering."""
    svc = NPSScorecardMetricService()
    items = svc.list_npsscorecardmetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/npsscorecardmetrics/{item_id}", response_model=Dict[str, Any])
def get_npsscorecardmetric_by_id(item_id: int):
    """Retrieve detailed record for NPSScorecardMetric by ID."""
    svc = NPSScorecardMetricService()
    item = svc.get_npsscorecardmetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"NPSScorecardMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/npsscorecardmetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_npsscorecardmetric(payload: NPSScorecardMetricCreateSchema):
    """Create new NPSScorecardMetric instance in enterprise repository."""
    svc = NPSScorecardMetricService()
    try:
        item = svc.create_npsscorecardmetric(
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

@router.put("/npsscorecardmetrics/{item_id}", response_model=Dict[str, Any])
def update_npsscorecardmetric(item_id: int, payload: NPSScorecardMetricUpdateSchema):
    """Update existing NPSScorecardMetric record fields."""
    svc = NPSScorecardMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_npsscorecardmetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"NPSScorecardMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/npsscorecardmetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_npsscorecardmetric(item_id: int, hard: bool = Query(False)):
    """Delete NPSScorecardMetric record (soft-delete by default)."""
    svc = NPSScorecardMetricService()
    ok = svc.delete_npsscorecardmetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"NPSScorecardMetric with ID {item_id} not found")
    return None

@router.get("/npsscorecardmetrics/analytics/metrics", response_model=Dict[str, Any])
def get_npsscorecardmetric_metrics():
    """Calculate summary statistical KPIs for NPSScorecardMetric collection."""
    svc = NPSScorecardMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== SentimentNLPAnalysis Endpoints ====================
@router.get("/sentimentnlpanalysiss", response_model=List[Dict[str, Any]])
def list_sentimentnlpanalysiss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SentimentNLPAnalysis records with pagination and filtering."""
    svc = SentimentNLPAnalysisService()
    items = svc.list_sentimentnlpanalysiss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sentimentnlpanalysiss/{item_id}", response_model=Dict[str, Any])
def get_sentimentnlpanalysis_by_id(item_id: int):
    """Retrieve detailed record for SentimentNLPAnalysis by ID."""
    svc = SentimentNLPAnalysisService()
    item = svc.get_sentimentnlpanalysis_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SentimentNLPAnalysis with ID {item_id} not found")
    return item.to_dict()

@router.post("/sentimentnlpanalysiss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sentimentnlpanalysis(payload: SentimentNLPAnalysisCreateSchema):
    """Create new SentimentNLPAnalysis instance in enterprise repository."""
    svc = SentimentNLPAnalysisService()
    try:
        item = svc.create_sentimentnlpanalysis(
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

@router.put("/sentimentnlpanalysiss/{item_id}", response_model=Dict[str, Any])
def update_sentimentnlpanalysis(item_id: int, payload: SentimentNLPAnalysisUpdateSchema):
    """Update existing SentimentNLPAnalysis record fields."""
    svc = SentimentNLPAnalysisService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sentimentnlpanalysis(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SentimentNLPAnalysis with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sentimentnlpanalysiss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sentimentnlpanalysis(item_id: int, hard: bool = Query(False)):
    """Delete SentimentNLPAnalysis record (soft-delete by default)."""
    svc = SentimentNLPAnalysisService()
    ok = svc.delete_sentimentnlpanalysis(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SentimentNLPAnalysis with ID {item_id} not found")
    return None

@router.get("/sentimentnlpanalysiss/analytics/metrics", response_model=Dict[str, Any])
def get_sentimentnlpanalysis_metrics():
    """Calculate summary statistical KPIs for SentimentNLPAnalysis collection."""
    svc = SentimentNLPAnalysisService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerEffortScoreCES Endpoints ====================
@router.get("/customereffortscorecess", response_model=List[Dict[str, Any]])
def list_customereffortscorecess(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerEffortScoreCES records with pagination and filtering."""
    svc = CustomerEffortScoreCESService()
    items = svc.list_customereffortscorecess(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customereffortscorecess/{item_id}", response_model=Dict[str, Any])
def get_customereffortscoreces_by_id(item_id: int):
    """Retrieve detailed record for CustomerEffortScoreCES by ID."""
    svc = CustomerEffortScoreCESService()
    item = svc.get_customereffortscoreces_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerEffortScoreCES with ID {item_id} not found")
    return item.to_dict()

@router.post("/customereffortscorecess", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customereffortscoreces(payload: CustomerEffortScoreCESCreateSchema):
    """Create new CustomerEffortScoreCES instance in enterprise repository."""
    svc = CustomerEffortScoreCESService()
    try:
        item = svc.create_customereffortscoreces(
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

@router.put("/customereffortscorecess/{item_id}", response_model=Dict[str, Any])
def update_customereffortscoreces(item_id: int, payload: CustomerEffortScoreCESUpdateSchema):
    """Update existing CustomerEffortScoreCES record fields."""
    svc = CustomerEffortScoreCESService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customereffortscoreces(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerEffortScoreCES with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customereffortscorecess/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customereffortscoreces(item_id: int, hard: bool = Query(False)):
    """Delete CustomerEffortScoreCES record (soft-delete by default)."""
    svc = CustomerEffortScoreCESService()
    ok = svc.delete_customereffortscoreces(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerEffortScoreCES with ID {item_id} not found")
    return None

@router.get("/customereffortscorecess/analytics/metrics", response_model=Dict[str, Any])
def get_customereffortscoreces_metrics():
    """Calculate summary statistical KPIs for CustomerEffortScoreCES collection."""
    svc = CustomerEffortScoreCESService()
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

# ==================== OmnichannelTouchpointEvent Endpoints ====================
@router.get("/omnichanneltouchpointevents", response_model=List[Dict[str, Any]])
def list_omnichanneltouchpointevents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OmnichannelTouchpointEvent records with pagination and filtering."""
    svc = OmnichannelTouchpointEventService()
    items = svc.list_omnichanneltouchpointevents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/omnichanneltouchpointevents/{item_id}", response_model=Dict[str, Any])
def get_omnichanneltouchpointevent_by_id(item_id: int):
    """Retrieve detailed record for OmnichannelTouchpointEvent by ID."""
    svc = OmnichannelTouchpointEventService()
    item = svc.get_omnichanneltouchpointevent_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OmnichannelTouchpointEvent with ID {item_id} not found")
    return item.to_dict()

@router.post("/omnichanneltouchpointevents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_omnichanneltouchpointevent(payload: OmnichannelTouchpointEventCreateSchema):
    """Create new OmnichannelTouchpointEvent instance in enterprise repository."""
    svc = OmnichannelTouchpointEventService()
    try:
        item = svc.create_omnichanneltouchpointevent(
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

@router.put("/omnichanneltouchpointevents/{item_id}", response_model=Dict[str, Any])
def update_omnichanneltouchpointevent(item_id: int, payload: OmnichannelTouchpointEventUpdateSchema):
    """Update existing OmnichannelTouchpointEvent record fields."""
    svc = OmnichannelTouchpointEventService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_omnichanneltouchpointevent(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OmnichannelTouchpointEvent with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/omnichanneltouchpointevents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_omnichanneltouchpointevent(item_id: int, hard: bool = Query(False)):
    """Delete OmnichannelTouchpointEvent record (soft-delete by default)."""
    svc = OmnichannelTouchpointEventService()
    ok = svc.delete_omnichanneltouchpointevent(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OmnichannelTouchpointEvent with ID {item_id} not found")
    return None

@router.get("/omnichanneltouchpointevents/analytics/metrics", response_model=Dict[str, Any])
def get_omnichanneltouchpointevent_metrics():
    """Calculate summary statistical KPIs for OmnichannelTouchpointEvent collection."""
    svc = OmnichannelTouchpointEventService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerChurnPrediction Endpoints ====================
@router.get("/customerchurnpredictions", response_model=List[Dict[str, Any]])
def list_customerchurnpredictions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerChurnPrediction records with pagination and filtering."""
    svc = CustomerChurnPredictionService()
    items = svc.list_customerchurnpredictions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerchurnpredictions/{item_id}", response_model=Dict[str, Any])
def get_customerchurnprediction_by_id(item_id: int):
    """Retrieve detailed record for CustomerChurnPrediction by ID."""
    svc = CustomerChurnPredictionService()
    item = svc.get_customerchurnprediction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerChurnPrediction with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerchurnpredictions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerchurnprediction(payload: CustomerChurnPredictionCreateSchema):
    """Create new CustomerChurnPrediction instance in enterprise repository."""
    svc = CustomerChurnPredictionService()
    try:
        item = svc.create_customerchurnprediction(
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

@router.put("/customerchurnpredictions/{item_id}", response_model=Dict[str, Any])
def update_customerchurnprediction(item_id: int, payload: CustomerChurnPredictionUpdateSchema):
    """Update existing CustomerChurnPrediction record fields."""
    svc = CustomerChurnPredictionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerchurnprediction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerChurnPrediction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerchurnpredictions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerchurnprediction(item_id: int, hard: bool = Query(False)):
    """Delete CustomerChurnPrediction record (soft-delete by default)."""
    svc = CustomerChurnPredictionService()
    ok = svc.delete_customerchurnprediction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerChurnPrediction with ID {item_id} not found")
    return None

@router.get("/customerchurnpredictions/analytics/metrics", response_model=Dict[str, Any])
def get_customerchurnprediction_metrics():
    """Calculate summary statistical KPIs for CustomerChurnPrediction collection."""
    svc = CustomerChurnPredictionService()
    return svc.calculate_aggregate_metrics()

# ==================== SupportResolutionTimeKPI Endpoints ====================
@router.get("/supportresolutiontimekpis", response_model=List[Dict[str, Any]])
def list_supportresolutiontimekpis(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SupportResolutionTimeKPI records with pagination and filtering."""
    svc = SupportResolutionTimeKPIService()
    items = svc.list_supportresolutiontimekpis(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/supportresolutiontimekpis/{item_id}", response_model=Dict[str, Any])
def get_supportresolutiontimekpi_by_id(item_id: int):
    """Retrieve detailed record for SupportResolutionTimeKPI by ID."""
    svc = SupportResolutionTimeKPIService()
    item = svc.get_supportresolutiontimekpi_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SupportResolutionTimeKPI with ID {item_id} not found")
    return item.to_dict()

@router.post("/supportresolutiontimekpis", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_supportresolutiontimekpi(payload: SupportResolutionTimeKPICreateSchema):
    """Create new SupportResolutionTimeKPI instance in enterprise repository."""
    svc = SupportResolutionTimeKPIService()
    try:
        item = svc.create_supportresolutiontimekpi(
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

@router.put("/supportresolutiontimekpis/{item_id}", response_model=Dict[str, Any])
def update_supportresolutiontimekpi(item_id: int, payload: SupportResolutionTimeKPIUpdateSchema):
    """Update existing SupportResolutionTimeKPI record fields."""
    svc = SupportResolutionTimeKPIService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_supportresolutiontimekpi(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SupportResolutionTimeKPI with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/supportresolutiontimekpis/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supportresolutiontimekpi(item_id: int, hard: bool = Query(False)):
    """Delete SupportResolutionTimeKPI record (soft-delete by default)."""
    svc = SupportResolutionTimeKPIService()
    ok = svc.delete_supportresolutiontimekpi(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SupportResolutionTimeKPI with ID {item_id} not found")
    return None

@router.get("/supportresolutiontimekpis/analytics/metrics", response_model=Dict[str, Any])
def get_supportresolutiontimekpi_metrics():
    """Calculate summary statistical KPIs for SupportResolutionTimeKPI collection."""
    svc = SupportResolutionTimeKPIService()
    return svc.calculate_aggregate_metrics()

# ==================== PersonalizationProfile Endpoints ====================
@router.get("/personalizationprofiles", response_model=List[Dict[str, Any]])
def list_personalizationprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PersonalizationProfile records with pagination and filtering."""
    svc = PersonalizationProfileService()
    items = svc.list_personalizationprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/personalizationprofiles/{item_id}", response_model=Dict[str, Any])
def get_personalizationprofile_by_id(item_id: int):
    """Retrieve detailed record for PersonalizationProfile by ID."""
    svc = PersonalizationProfileService()
    item = svc.get_personalizationprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PersonalizationProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/personalizationprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_personalizationprofile(payload: PersonalizationProfileCreateSchema):
    """Create new PersonalizationProfile instance in enterprise repository."""
    svc = PersonalizationProfileService()
    try:
        item = svc.create_personalizationprofile(
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

@router.put("/personalizationprofiles/{item_id}", response_model=Dict[str, Any])
def update_personalizationprofile(item_id: int, payload: PersonalizationProfileUpdateSchema):
    """Update existing PersonalizationProfile record fields."""
    svc = PersonalizationProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_personalizationprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PersonalizationProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/personalizationprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_personalizationprofile(item_id: int, hard: bool = Query(False)):
    """Delete PersonalizationProfile record (soft-delete by default)."""
    svc = PersonalizationProfileService()
    ok = svc.delete_personalizationprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PersonalizationProfile with ID {item_id} not found")
    return None

@router.get("/personalizationprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_personalizationprofile_metrics():
    """Calculate summary statistical KPIs for PersonalizationProfile collection."""
    svc = PersonalizationProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== ExperienceGapIncident Endpoints ====================
@router.get("/experiencegapincidents", response_model=List[Dict[str, Any]])
def list_experiencegapincidents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExperienceGapIncident records with pagination and filtering."""
    svc = ExperienceGapIncidentService()
    items = svc.list_experiencegapincidents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/experiencegapincidents/{item_id}", response_model=Dict[str, Any])
def get_experiencegapincident_by_id(item_id: int):
    """Retrieve detailed record for ExperienceGapIncident by ID."""
    svc = ExperienceGapIncidentService()
    item = svc.get_experiencegapincident_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExperienceGapIncident with ID {item_id} not found")
    return item.to_dict()

@router.post("/experiencegapincidents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_experiencegapincident(payload: ExperienceGapIncidentCreateSchema):
    """Create new ExperienceGapIncident instance in enterprise repository."""
    svc = ExperienceGapIncidentService()
    try:
        item = svc.create_experiencegapincident(
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

@router.put("/experiencegapincidents/{item_id}", response_model=Dict[str, Any])
def update_experiencegapincident(item_id: int, payload: ExperienceGapIncidentUpdateSchema):
    """Update existing ExperienceGapIncident record fields."""
    svc = ExperienceGapIncidentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_experiencegapincident(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExperienceGapIncident with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/experiencegapincidents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_experiencegapincident(item_id: int, hard: bool = Query(False)):
    """Delete ExperienceGapIncident record (soft-delete by default)."""
    svc = ExperienceGapIncidentService()
    ok = svc.delete_experiencegapincident(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExperienceGapIncident with ID {item_id} not found")
    return None

@router.get("/experiencegapincidents/analytics/metrics", response_model=Dict[str, Any])
def get_experiencegapincident_metrics():
    """Calculate summary statistical KPIs for ExperienceGapIncident collection."""
    svc = ExperienceGapIncidentService()
    return svc.calculate_aggregate_metrics()

# ==================== AdvocateReferralRecord Endpoints ====================
@router.get("/advocatereferralrecords", response_model=List[Dict[str, Any]])
def list_advocatereferralrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AdvocateReferralRecord records with pagination and filtering."""
    svc = AdvocateReferralRecordService()
    items = svc.list_advocatereferralrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/advocatereferralrecords/{item_id}", response_model=Dict[str, Any])
def get_advocatereferralrecord_by_id(item_id: int):
    """Retrieve detailed record for AdvocateReferralRecord by ID."""
    svc = AdvocateReferralRecordService()
    item = svc.get_advocatereferralrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AdvocateReferralRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/advocatereferralrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_advocatereferralrecord(payload: AdvocateReferralRecordCreateSchema):
    """Create new AdvocateReferralRecord instance in enterprise repository."""
    svc = AdvocateReferralRecordService()
    try:
        item = svc.create_advocatereferralrecord(
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

@router.put("/advocatereferralrecords/{item_id}", response_model=Dict[str, Any])
def update_advocatereferralrecord(item_id: int, payload: AdvocateReferralRecordUpdateSchema):
    """Update existing AdvocateReferralRecord record fields."""
    svc = AdvocateReferralRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_advocatereferralrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AdvocateReferralRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/advocatereferralrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_advocatereferralrecord(item_id: int, hard: bool = Query(False)):
    """Delete AdvocateReferralRecord record (soft-delete by default)."""
    svc = AdvocateReferralRecordService()
    ok = svc.delete_advocatereferralrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AdvocateReferralRecord with ID {item_id} not found")
    return None

@router.get("/advocatereferralrecords/analytics/metrics", response_model=Dict[str, Any])
def get_advocatereferralrecord_metrics():
    """Calculate summary statistical KPIs for AdvocateReferralRecord collection."""
    svc = AdvocateReferralRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== RetentionCampaignTrigger Endpoints ====================
@router.get("/retentioncampaigntriggers", response_model=List[Dict[str, Any]])
def list_retentioncampaigntriggers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RetentionCampaignTrigger records with pagination and filtering."""
    svc = RetentionCampaignTriggerService()
    items = svc.list_retentioncampaigntriggers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/retentioncampaigntriggers/{item_id}", response_model=Dict[str, Any])
def get_retentioncampaigntrigger_by_id(item_id: int):
    """Retrieve detailed record for RetentionCampaignTrigger by ID."""
    svc = RetentionCampaignTriggerService()
    item = svc.get_retentioncampaigntrigger_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RetentionCampaignTrigger with ID {item_id} not found")
    return item.to_dict()

@router.post("/retentioncampaigntriggers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_retentioncampaigntrigger(payload: RetentionCampaignTriggerCreateSchema):
    """Create new RetentionCampaignTrigger instance in enterprise repository."""
    svc = RetentionCampaignTriggerService()
    try:
        item = svc.create_retentioncampaigntrigger(
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

@router.put("/retentioncampaigntriggers/{item_id}", response_model=Dict[str, Any])
def update_retentioncampaigntrigger(item_id: int, payload: RetentionCampaignTriggerUpdateSchema):
    """Update existing RetentionCampaignTrigger record fields."""
    svc = RetentionCampaignTriggerService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_retentioncampaigntrigger(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RetentionCampaignTrigger with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/retentioncampaigntriggers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_retentioncampaigntrigger(item_id: int, hard: bool = Query(False)):
    """Delete RetentionCampaignTrigger record (soft-delete by default)."""
    svc = RetentionCampaignTriggerService()
    ok = svc.delete_retentioncampaigntrigger(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RetentionCampaignTrigger with ID {item_id} not found")
    return None

@router.get("/retentioncampaigntriggers/analytics/metrics", response_model=Dict[str, Any])
def get_retentioncampaigntrigger_metrics():
    """Calculate summary statistical KPIs for RetentionCampaignTrigger collection."""
    svc = RetentionCampaignTriggerService()
    return svc.calculate_aggregate_metrics()

# ==================== FeedbackCategorizationRule Endpoints ====================
@router.get("/feedbackcategorizationrules", response_model=List[Dict[str, Any]])
def list_feedbackcategorizationrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FeedbackCategorizationRule records with pagination and filtering."""
    svc = FeedbackCategorizationRuleService()
    items = svc.list_feedbackcategorizationrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/feedbackcategorizationrules/{item_id}", response_model=Dict[str, Any])
def get_feedbackcategorizationrule_by_id(item_id: int):
    """Retrieve detailed record for FeedbackCategorizationRule by ID."""
    svc = FeedbackCategorizationRuleService()
    item = svc.get_feedbackcategorizationrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FeedbackCategorizationRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/feedbackcategorizationrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_feedbackcategorizationrule(payload: FeedbackCategorizationRuleCreateSchema):
    """Create new FeedbackCategorizationRule instance in enterprise repository."""
    svc = FeedbackCategorizationRuleService()
    try:
        item = svc.create_feedbackcategorizationrule(
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

@router.put("/feedbackcategorizationrules/{item_id}", response_model=Dict[str, Any])
def update_feedbackcategorizationrule(item_id: int, payload: FeedbackCategorizationRuleUpdateSchema):
    """Update existing FeedbackCategorizationRule record fields."""
    svc = FeedbackCategorizationRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_feedbackcategorizationrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FeedbackCategorizationRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/feedbackcategorizationrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feedbackcategorizationrule(item_id: int, hard: bool = Query(False)):
    """Delete FeedbackCategorizationRule record (soft-delete by default)."""
    svc = FeedbackCategorizationRuleService()
    ok = svc.delete_feedbackcategorizationrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FeedbackCategorizationRule with ID {item_id} not found")
    return None

@router.get("/feedbackcategorizationrules/analytics/metrics", response_model=Dict[str, Any])
def get_feedbackcategorizationrule_metrics():
    """Calculate summary statistical KPIs for FeedbackCategorizationRule collection."""
    svc = FeedbackCategorizationRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== CustomerDelightAction Endpoints ====================
@router.get("/customerdelightactions", response_model=List[Dict[str, Any]])
def list_customerdelightactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CustomerDelightAction records with pagination and filtering."""
    svc = CustomerDelightActionService()
    items = svc.list_customerdelightactions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/customerdelightactions/{item_id}", response_model=Dict[str, Any])
def get_customerdelightaction_by_id(item_id: int):
    """Retrieve detailed record for CustomerDelightAction by ID."""
    svc = CustomerDelightActionService()
    item = svc.get_customerdelightaction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CustomerDelightAction with ID {item_id} not found")
    return item.to_dict()

@router.post("/customerdelightactions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_customerdelightaction(payload: CustomerDelightActionCreateSchema):
    """Create new CustomerDelightAction instance in enterprise repository."""
    svc = CustomerDelightActionService()
    try:
        item = svc.create_customerdelightaction(
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

@router.put("/customerdelightactions/{item_id}", response_model=Dict[str, Any])
def update_customerdelightaction(item_id: int, payload: CustomerDelightActionUpdateSchema):
    """Update existing CustomerDelightAction record fields."""
    svc = CustomerDelightActionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_customerdelightaction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CustomerDelightAction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/customerdelightactions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customerdelightaction(item_id: int, hard: bool = Query(False)):
    """Delete CustomerDelightAction record (soft-delete by default)."""
    svc = CustomerDelightActionService()
    ok = svc.delete_customerdelightaction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CustomerDelightAction with ID {item_id} not found")
    return None

@router.get("/customerdelightactions/analytics/metrics", response_model=Dict[str, Any])
def get_customerdelightaction_metrics():
    """Calculate summary statistical KPIs for CustomerDelightAction collection."""
    svc = CustomerDelightActionService()
    return svc.calculate_aggregate_metrics()

# ==================== ExecutiveCXScorecard Endpoints ====================
@router.get("/executivecxscorecards", response_model=List[Dict[str, Any]])
def list_executivecxscorecards(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExecutiveCXScorecard records with pagination and filtering."""
    svc = ExecutiveCXScorecardService()
    items = svc.list_executivecxscorecards(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/executivecxscorecards/{item_id}", response_model=Dict[str, Any])
def get_executivecxscorecard_by_id(item_id: int):
    """Retrieve detailed record for ExecutiveCXScorecard by ID."""
    svc = ExecutiveCXScorecardService()
    item = svc.get_executivecxscorecard_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExecutiveCXScorecard with ID {item_id} not found")
    return item.to_dict()

@router.post("/executivecxscorecards", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_executivecxscorecard(payload: ExecutiveCXScorecardCreateSchema):
    """Create new ExecutiveCXScorecard instance in enterprise repository."""
    svc = ExecutiveCXScorecardService()
    try:
        item = svc.create_executivecxscorecard(
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

@router.put("/executivecxscorecards/{item_id}", response_model=Dict[str, Any])
def update_executivecxscorecard(item_id: int, payload: ExecutiveCXScorecardUpdateSchema):
    """Update existing ExecutiveCXScorecard record fields."""
    svc = ExecutiveCXScorecardService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_executivecxscorecard(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExecutiveCXScorecard with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/executivecxscorecards/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_executivecxscorecard(item_id: int, hard: bool = Query(False)):
    """Delete ExecutiveCXScorecard record (soft-delete by default)."""
    svc = ExecutiveCXScorecardService()
    ok = svc.delete_executivecxscorecard(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExecutiveCXScorecard with ID {item_id} not found")
    return None

@router.get("/executivecxscorecards/analytics/metrics", response_model=Dict[str, Any])
def get_executivecxscorecard_metrics():
    """Calculate summary statistical KPIs for ExecutiveCXScorecard collection."""
    svc = ExecutiveCXScorecardService()
    return svc.calculate_aggregate_metrics()

