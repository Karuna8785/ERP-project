"""
Human Capital & Talent Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    JobOpeningService,
    CandidateProfileService,
    InterviewScheduleService,
    OfferLetterService,
    OnboardingChecklistService,
    EmployeeTrainingCourseService,
    CertificationRecordService,
    SuccessionPlanService,
    PerformanceObjectiveService,
    PeerReviewFeedbackService,
    DisciplinaryActionService,
    HealthSafetyIncidentService,
    ExitInterviewService,
    OrgHierarchyNodeService,
    CompensationBandService,
    EmployeeSurveyService,
)
from .schemas import (
    JobOpeningCreateSchema, JobOpeningUpdateSchema, JobOpeningResponseSchema,
    CandidateProfileCreateSchema, CandidateProfileUpdateSchema, CandidateProfileResponseSchema,
    InterviewScheduleCreateSchema, InterviewScheduleUpdateSchema, InterviewScheduleResponseSchema,
    OfferLetterCreateSchema, OfferLetterUpdateSchema, OfferLetterResponseSchema,
    OnboardingChecklistCreateSchema, OnboardingChecklistUpdateSchema, OnboardingChecklistResponseSchema,
    EmployeeTrainingCourseCreateSchema, EmployeeTrainingCourseUpdateSchema, EmployeeTrainingCourseResponseSchema,
    CertificationRecordCreateSchema, CertificationRecordUpdateSchema, CertificationRecordResponseSchema,
    SuccessionPlanCreateSchema, SuccessionPlanUpdateSchema, SuccessionPlanResponseSchema,
    PerformanceObjectiveCreateSchema, PerformanceObjectiveUpdateSchema, PerformanceObjectiveResponseSchema,
    PeerReviewFeedbackCreateSchema, PeerReviewFeedbackUpdateSchema, PeerReviewFeedbackResponseSchema,
    DisciplinaryActionCreateSchema, DisciplinaryActionUpdateSchema, DisciplinaryActionResponseSchema,
    HealthSafetyIncidentCreateSchema, HealthSafetyIncidentUpdateSchema, HealthSafetyIncidentResponseSchema,
    ExitInterviewCreateSchema, ExitInterviewUpdateSchema, ExitInterviewResponseSchema,
    OrgHierarchyNodeCreateSchema, OrgHierarchyNodeUpdateSchema, OrgHierarchyNodeResponseSchema,
    CompensationBandCreateSchema, CompensationBandUpdateSchema, CompensationBandResponseSchema,
    EmployeeSurveyCreateSchema, EmployeeSurveyUpdateSchema, EmployeeSurveyResponseSchema,
)

router = APIRouter(prefix="/human_capital", tags=["Human Capital & Talent Management"])

# ==================== JobOpening Endpoints ====================
@router.get("/jobopenings", response_model=List[Dict[str, Any]])
def list_jobopenings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List JobOpening records with pagination and filtering."""
    svc = JobOpeningService()
    items = svc.list_jobopenings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/jobopenings/{item_id}", response_model=Dict[str, Any])
def get_jobopening_by_id(item_id: int):
    """Retrieve detailed record for JobOpening by ID."""
    svc = JobOpeningService()
    item = svc.get_jobopening_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"JobOpening with ID {item_id} not found")
    return item.to_dict()

@router.post("/jobopenings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_jobopening(payload: JobOpeningCreateSchema):
    """Create new JobOpening instance in enterprise repository."""
    svc = JobOpeningService()
    try:
        item = svc.create_jobopening(
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

@router.put("/jobopenings/{item_id}", response_model=Dict[str, Any])
def update_jobopening(item_id: int, payload: JobOpeningUpdateSchema):
    """Update existing JobOpening record fields."""
    svc = JobOpeningService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_jobopening(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"JobOpening with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/jobopenings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_jobopening(item_id: int, hard: bool = Query(False)):
    """Delete JobOpening record (soft-delete by default)."""
    svc = JobOpeningService()
    ok = svc.delete_jobopening(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"JobOpening with ID {item_id} not found")
    return None

@router.get("/jobopenings/analytics/metrics", response_model=Dict[str, Any])
def get_jobopening_metrics():
    """Calculate summary statistical KPIs for JobOpening collection."""
    svc = JobOpeningService()
    return svc.calculate_aggregate_metrics()

# ==================== CandidateProfile Endpoints ====================
@router.get("/candidateprofiles", response_model=List[Dict[str, Any]])
def list_candidateprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CandidateProfile records with pagination and filtering."""
    svc = CandidateProfileService()
    items = svc.list_candidateprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/candidateprofiles/{item_id}", response_model=Dict[str, Any])
def get_candidateprofile_by_id(item_id: int):
    """Retrieve detailed record for CandidateProfile by ID."""
    svc = CandidateProfileService()
    item = svc.get_candidateprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CandidateProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/candidateprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_candidateprofile(payload: CandidateProfileCreateSchema):
    """Create new CandidateProfile instance in enterprise repository."""
    svc = CandidateProfileService()
    try:
        item = svc.create_candidateprofile(
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

@router.put("/candidateprofiles/{item_id}", response_model=Dict[str, Any])
def update_candidateprofile(item_id: int, payload: CandidateProfileUpdateSchema):
    """Update existing CandidateProfile record fields."""
    svc = CandidateProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_candidateprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CandidateProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/candidateprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_candidateprofile(item_id: int, hard: bool = Query(False)):
    """Delete CandidateProfile record (soft-delete by default)."""
    svc = CandidateProfileService()
    ok = svc.delete_candidateprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CandidateProfile with ID {item_id} not found")
    return None

@router.get("/candidateprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_candidateprofile_metrics():
    """Calculate summary statistical KPIs for CandidateProfile collection."""
    svc = CandidateProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== InterviewSchedule Endpoints ====================
@router.get("/interviewschedules", response_model=List[Dict[str, Any]])
def list_interviewschedules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InterviewSchedule records with pagination and filtering."""
    svc = InterviewScheduleService()
    items = svc.list_interviewschedules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/interviewschedules/{item_id}", response_model=Dict[str, Any])
def get_interviewschedule_by_id(item_id: int):
    """Retrieve detailed record for InterviewSchedule by ID."""
    svc = InterviewScheduleService()
    item = svc.get_interviewschedule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InterviewSchedule with ID {item_id} not found")
    return item.to_dict()

@router.post("/interviewschedules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_interviewschedule(payload: InterviewScheduleCreateSchema):
    """Create new InterviewSchedule instance in enterprise repository."""
    svc = InterviewScheduleService()
    try:
        item = svc.create_interviewschedule(
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

@router.put("/interviewschedules/{item_id}", response_model=Dict[str, Any])
def update_interviewschedule(item_id: int, payload: InterviewScheduleUpdateSchema):
    """Update existing InterviewSchedule record fields."""
    svc = InterviewScheduleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_interviewschedule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InterviewSchedule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/interviewschedules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_interviewschedule(item_id: int, hard: bool = Query(False)):
    """Delete InterviewSchedule record (soft-delete by default)."""
    svc = InterviewScheduleService()
    ok = svc.delete_interviewschedule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InterviewSchedule with ID {item_id} not found")
    return None

@router.get("/interviewschedules/analytics/metrics", response_model=Dict[str, Any])
def get_interviewschedule_metrics():
    """Calculate summary statistical KPIs for InterviewSchedule collection."""
    svc = InterviewScheduleService()
    return svc.calculate_aggregate_metrics()

# ==================== OfferLetter Endpoints ====================
@router.get("/offerletters", response_model=List[Dict[str, Any]])
def list_offerletters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OfferLetter records with pagination and filtering."""
    svc = OfferLetterService()
    items = svc.list_offerletters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/offerletters/{item_id}", response_model=Dict[str, Any])
def get_offerletter_by_id(item_id: int):
    """Retrieve detailed record for OfferLetter by ID."""
    svc = OfferLetterService()
    item = svc.get_offerletter_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OfferLetter with ID {item_id} not found")
    return item.to_dict()

@router.post("/offerletters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_offerletter(payload: OfferLetterCreateSchema):
    """Create new OfferLetter instance in enterprise repository."""
    svc = OfferLetterService()
    try:
        item = svc.create_offerletter(
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

@router.put("/offerletters/{item_id}", response_model=Dict[str, Any])
def update_offerletter(item_id: int, payload: OfferLetterUpdateSchema):
    """Update existing OfferLetter record fields."""
    svc = OfferLetterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_offerletter(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OfferLetter with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/offerletters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_offerletter(item_id: int, hard: bool = Query(False)):
    """Delete OfferLetter record (soft-delete by default)."""
    svc = OfferLetterService()
    ok = svc.delete_offerletter(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OfferLetter with ID {item_id} not found")
    return None

@router.get("/offerletters/analytics/metrics", response_model=Dict[str, Any])
def get_offerletter_metrics():
    """Calculate summary statistical KPIs for OfferLetter collection."""
    svc = OfferLetterService()
    return svc.calculate_aggregate_metrics()

# ==================== OnboardingChecklist Endpoints ====================
@router.get("/onboardingchecklists", response_model=List[Dict[str, Any]])
def list_onboardingchecklists(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OnboardingChecklist records with pagination and filtering."""
    svc = OnboardingChecklistService()
    items = svc.list_onboardingchecklists(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/onboardingchecklists/{item_id}", response_model=Dict[str, Any])
def get_onboardingchecklist_by_id(item_id: int):
    """Retrieve detailed record for OnboardingChecklist by ID."""
    svc = OnboardingChecklistService()
    item = svc.get_onboardingchecklist_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OnboardingChecklist with ID {item_id} not found")
    return item.to_dict()

@router.post("/onboardingchecklists", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_onboardingchecklist(payload: OnboardingChecklistCreateSchema):
    """Create new OnboardingChecklist instance in enterprise repository."""
    svc = OnboardingChecklistService()
    try:
        item = svc.create_onboardingchecklist(
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

@router.put("/onboardingchecklists/{item_id}", response_model=Dict[str, Any])
def update_onboardingchecklist(item_id: int, payload: OnboardingChecklistUpdateSchema):
    """Update existing OnboardingChecklist record fields."""
    svc = OnboardingChecklistService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_onboardingchecklist(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OnboardingChecklist with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/onboardingchecklists/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_onboardingchecklist(item_id: int, hard: bool = Query(False)):
    """Delete OnboardingChecklist record (soft-delete by default)."""
    svc = OnboardingChecklistService()
    ok = svc.delete_onboardingchecklist(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OnboardingChecklist with ID {item_id} not found")
    return None

@router.get("/onboardingchecklists/analytics/metrics", response_model=Dict[str, Any])
def get_onboardingchecklist_metrics():
    """Calculate summary statistical KPIs for OnboardingChecklist collection."""
    svc = OnboardingChecklistService()
    return svc.calculate_aggregate_metrics()

# ==================== EmployeeTrainingCourse Endpoints ====================
@router.get("/employeetrainingcourses", response_model=List[Dict[str, Any]])
def list_employeetrainingcourses(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmployeeTrainingCourse records with pagination and filtering."""
    svc = EmployeeTrainingCourseService()
    items = svc.list_employeetrainingcourses(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/employeetrainingcourses/{item_id}", response_model=Dict[str, Any])
def get_employeetrainingcourse_by_id(item_id: int):
    """Retrieve detailed record for EmployeeTrainingCourse by ID."""
    svc = EmployeeTrainingCourseService()
    item = svc.get_employeetrainingcourse_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmployeeTrainingCourse with ID {item_id} not found")
    return item.to_dict()

@router.post("/employeetrainingcourses", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_employeetrainingcourse(payload: EmployeeTrainingCourseCreateSchema):
    """Create new EmployeeTrainingCourse instance in enterprise repository."""
    svc = EmployeeTrainingCourseService()
    try:
        item = svc.create_employeetrainingcourse(
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

@router.put("/employeetrainingcourses/{item_id}", response_model=Dict[str, Any])
def update_employeetrainingcourse(item_id: int, payload: EmployeeTrainingCourseUpdateSchema):
    """Update existing EmployeeTrainingCourse record fields."""
    svc = EmployeeTrainingCourseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_employeetrainingcourse(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmployeeTrainingCourse with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/employeetrainingcourses/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employeetrainingcourse(item_id: int, hard: bool = Query(False)):
    """Delete EmployeeTrainingCourse record (soft-delete by default)."""
    svc = EmployeeTrainingCourseService()
    ok = svc.delete_employeetrainingcourse(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmployeeTrainingCourse with ID {item_id} not found")
    return None

@router.get("/employeetrainingcourses/analytics/metrics", response_model=Dict[str, Any])
def get_employeetrainingcourse_metrics():
    """Calculate summary statistical KPIs for EmployeeTrainingCourse collection."""
    svc = EmployeeTrainingCourseService()
    return svc.calculate_aggregate_metrics()

# ==================== CertificationRecord Endpoints ====================
@router.get("/certificationrecords", response_model=List[Dict[str, Any]])
def list_certificationrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CertificationRecord records with pagination and filtering."""
    svc = CertificationRecordService()
    items = svc.list_certificationrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/certificationrecords/{item_id}", response_model=Dict[str, Any])
def get_certificationrecord_by_id(item_id: int):
    """Retrieve detailed record for CertificationRecord by ID."""
    svc = CertificationRecordService()
    item = svc.get_certificationrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CertificationRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/certificationrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_certificationrecord(payload: CertificationRecordCreateSchema):
    """Create new CertificationRecord instance in enterprise repository."""
    svc = CertificationRecordService()
    try:
        item = svc.create_certificationrecord(
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

@router.put("/certificationrecords/{item_id}", response_model=Dict[str, Any])
def update_certificationrecord(item_id: int, payload: CertificationRecordUpdateSchema):
    """Update existing CertificationRecord record fields."""
    svc = CertificationRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_certificationrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CertificationRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/certificationrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_certificationrecord(item_id: int, hard: bool = Query(False)):
    """Delete CertificationRecord record (soft-delete by default)."""
    svc = CertificationRecordService()
    ok = svc.delete_certificationrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CertificationRecord with ID {item_id} not found")
    return None

@router.get("/certificationrecords/analytics/metrics", response_model=Dict[str, Any])
def get_certificationrecord_metrics():
    """Calculate summary statistical KPIs for CertificationRecord collection."""
    svc = CertificationRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== SuccessionPlan Endpoints ====================
@router.get("/successionplans", response_model=List[Dict[str, Any]])
def list_successionplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SuccessionPlan records with pagination and filtering."""
    svc = SuccessionPlanService()
    items = svc.list_successionplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/successionplans/{item_id}", response_model=Dict[str, Any])
def get_successionplan_by_id(item_id: int):
    """Retrieve detailed record for SuccessionPlan by ID."""
    svc = SuccessionPlanService()
    item = svc.get_successionplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SuccessionPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/successionplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_successionplan(payload: SuccessionPlanCreateSchema):
    """Create new SuccessionPlan instance in enterprise repository."""
    svc = SuccessionPlanService()
    try:
        item = svc.create_successionplan(
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

@router.put("/successionplans/{item_id}", response_model=Dict[str, Any])
def update_successionplan(item_id: int, payload: SuccessionPlanUpdateSchema):
    """Update existing SuccessionPlan record fields."""
    svc = SuccessionPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_successionplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SuccessionPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/successionplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_successionplan(item_id: int, hard: bool = Query(False)):
    """Delete SuccessionPlan record (soft-delete by default)."""
    svc = SuccessionPlanService()
    ok = svc.delete_successionplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SuccessionPlan with ID {item_id} not found")
    return None

@router.get("/successionplans/analytics/metrics", response_model=Dict[str, Any])
def get_successionplan_metrics():
    """Calculate summary statistical KPIs for SuccessionPlan collection."""
    svc = SuccessionPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== PerformanceObjective Endpoints ====================
@router.get("/performanceobjectives", response_model=List[Dict[str, Any]])
def list_performanceobjectives(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PerformanceObjective records with pagination and filtering."""
    svc = PerformanceObjectiveService()
    items = svc.list_performanceobjectives(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/performanceobjectives/{item_id}", response_model=Dict[str, Any])
def get_performanceobjective_by_id(item_id: int):
    """Retrieve detailed record for PerformanceObjective by ID."""
    svc = PerformanceObjectiveService()
    item = svc.get_performanceobjective_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PerformanceObjective with ID {item_id} not found")
    return item.to_dict()

@router.post("/performanceobjectives", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_performanceobjective(payload: PerformanceObjectiveCreateSchema):
    """Create new PerformanceObjective instance in enterprise repository."""
    svc = PerformanceObjectiveService()
    try:
        item = svc.create_performanceobjective(
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

@router.put("/performanceobjectives/{item_id}", response_model=Dict[str, Any])
def update_performanceobjective(item_id: int, payload: PerformanceObjectiveUpdateSchema):
    """Update existing PerformanceObjective record fields."""
    svc = PerformanceObjectiveService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_performanceobjective(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PerformanceObjective with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/performanceobjectives/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_performanceobjective(item_id: int, hard: bool = Query(False)):
    """Delete PerformanceObjective record (soft-delete by default)."""
    svc = PerformanceObjectiveService()
    ok = svc.delete_performanceobjective(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PerformanceObjective with ID {item_id} not found")
    return None

@router.get("/performanceobjectives/analytics/metrics", response_model=Dict[str, Any])
def get_performanceobjective_metrics():
    """Calculate summary statistical KPIs for PerformanceObjective collection."""
    svc = PerformanceObjectiveService()
    return svc.calculate_aggregate_metrics()

# ==================== PeerReviewFeedback Endpoints ====================
@router.get("/peerreviewfeedbacks", response_model=List[Dict[str, Any]])
def list_peerreviewfeedbacks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PeerReviewFeedback records with pagination and filtering."""
    svc = PeerReviewFeedbackService()
    items = svc.list_peerreviewfeedbacks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/peerreviewfeedbacks/{item_id}", response_model=Dict[str, Any])
def get_peerreviewfeedback_by_id(item_id: int):
    """Retrieve detailed record for PeerReviewFeedback by ID."""
    svc = PeerReviewFeedbackService()
    item = svc.get_peerreviewfeedback_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PeerReviewFeedback with ID {item_id} not found")
    return item.to_dict()

@router.post("/peerreviewfeedbacks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_peerreviewfeedback(payload: PeerReviewFeedbackCreateSchema):
    """Create new PeerReviewFeedback instance in enterprise repository."""
    svc = PeerReviewFeedbackService()
    try:
        item = svc.create_peerreviewfeedback(
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

@router.put("/peerreviewfeedbacks/{item_id}", response_model=Dict[str, Any])
def update_peerreviewfeedback(item_id: int, payload: PeerReviewFeedbackUpdateSchema):
    """Update existing PeerReviewFeedback record fields."""
    svc = PeerReviewFeedbackService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_peerreviewfeedback(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PeerReviewFeedback with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/peerreviewfeedbacks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_peerreviewfeedback(item_id: int, hard: bool = Query(False)):
    """Delete PeerReviewFeedback record (soft-delete by default)."""
    svc = PeerReviewFeedbackService()
    ok = svc.delete_peerreviewfeedback(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PeerReviewFeedback with ID {item_id} not found")
    return None

@router.get("/peerreviewfeedbacks/analytics/metrics", response_model=Dict[str, Any])
def get_peerreviewfeedback_metrics():
    """Calculate summary statistical KPIs for PeerReviewFeedback collection."""
    svc = PeerReviewFeedbackService()
    return svc.calculate_aggregate_metrics()

# ==================== DisciplinaryAction Endpoints ====================
@router.get("/disciplinaryactions", response_model=List[Dict[str, Any]])
def list_disciplinaryactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DisciplinaryAction records with pagination and filtering."""
    svc = DisciplinaryActionService()
    items = svc.list_disciplinaryactions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/disciplinaryactions/{item_id}", response_model=Dict[str, Any])
def get_disciplinaryaction_by_id(item_id: int):
    """Retrieve detailed record for DisciplinaryAction by ID."""
    svc = DisciplinaryActionService()
    item = svc.get_disciplinaryaction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DisciplinaryAction with ID {item_id} not found")
    return item.to_dict()

@router.post("/disciplinaryactions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_disciplinaryaction(payload: DisciplinaryActionCreateSchema):
    """Create new DisciplinaryAction instance in enterprise repository."""
    svc = DisciplinaryActionService()
    try:
        item = svc.create_disciplinaryaction(
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

@router.put("/disciplinaryactions/{item_id}", response_model=Dict[str, Any])
def update_disciplinaryaction(item_id: int, payload: DisciplinaryActionUpdateSchema):
    """Update existing DisciplinaryAction record fields."""
    svc = DisciplinaryActionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_disciplinaryaction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DisciplinaryAction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/disciplinaryactions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_disciplinaryaction(item_id: int, hard: bool = Query(False)):
    """Delete DisciplinaryAction record (soft-delete by default)."""
    svc = DisciplinaryActionService()
    ok = svc.delete_disciplinaryaction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DisciplinaryAction with ID {item_id} not found")
    return None

@router.get("/disciplinaryactions/analytics/metrics", response_model=Dict[str, Any])
def get_disciplinaryaction_metrics():
    """Calculate summary statistical KPIs for DisciplinaryAction collection."""
    svc = DisciplinaryActionService()
    return svc.calculate_aggregate_metrics()

# ==================== HealthSafetyIncident Endpoints ====================
@router.get("/healthsafetyincidents", response_model=List[Dict[str, Any]])
def list_healthsafetyincidents(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HealthSafetyIncident records with pagination and filtering."""
    svc = HealthSafetyIncidentService()
    items = svc.list_healthsafetyincidents(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/healthsafetyincidents/{item_id}", response_model=Dict[str, Any])
def get_healthsafetyincident_by_id(item_id: int):
    """Retrieve detailed record for HealthSafetyIncident by ID."""
    svc = HealthSafetyIncidentService()
    item = svc.get_healthsafetyincident_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HealthSafetyIncident with ID {item_id} not found")
    return item.to_dict()

@router.post("/healthsafetyincidents", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_healthsafetyincident(payload: HealthSafetyIncidentCreateSchema):
    """Create new HealthSafetyIncident instance in enterprise repository."""
    svc = HealthSafetyIncidentService()
    try:
        item = svc.create_healthsafetyincident(
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

@router.put("/healthsafetyincidents/{item_id}", response_model=Dict[str, Any])
def update_healthsafetyincident(item_id: int, payload: HealthSafetyIncidentUpdateSchema):
    """Update existing HealthSafetyIncident record fields."""
    svc = HealthSafetyIncidentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_healthsafetyincident(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HealthSafetyIncident with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/healthsafetyincidents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_healthsafetyincident(item_id: int, hard: bool = Query(False)):
    """Delete HealthSafetyIncident record (soft-delete by default)."""
    svc = HealthSafetyIncidentService()
    ok = svc.delete_healthsafetyincident(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HealthSafetyIncident with ID {item_id} not found")
    return None

@router.get("/healthsafetyincidents/analytics/metrics", response_model=Dict[str, Any])
def get_healthsafetyincident_metrics():
    """Calculate summary statistical KPIs for HealthSafetyIncident collection."""
    svc = HealthSafetyIncidentService()
    return svc.calculate_aggregate_metrics()

# ==================== ExitInterview Endpoints ====================
@router.get("/exitinterviews", response_model=List[Dict[str, Any]])
def list_exitinterviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExitInterview records with pagination and filtering."""
    svc = ExitInterviewService()
    items = svc.list_exitinterviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/exitinterviews/{item_id}", response_model=Dict[str, Any])
def get_exitinterview_by_id(item_id: int):
    """Retrieve detailed record for ExitInterview by ID."""
    svc = ExitInterviewService()
    item = svc.get_exitinterview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExitInterview with ID {item_id} not found")
    return item.to_dict()

@router.post("/exitinterviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_exitinterview(payload: ExitInterviewCreateSchema):
    """Create new ExitInterview instance in enterprise repository."""
    svc = ExitInterviewService()
    try:
        item = svc.create_exitinterview(
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

@router.put("/exitinterviews/{item_id}", response_model=Dict[str, Any])
def update_exitinterview(item_id: int, payload: ExitInterviewUpdateSchema):
    """Update existing ExitInterview record fields."""
    svc = ExitInterviewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_exitinterview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExitInterview with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/exitinterviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exitinterview(item_id: int, hard: bool = Query(False)):
    """Delete ExitInterview record (soft-delete by default)."""
    svc = ExitInterviewService()
    ok = svc.delete_exitinterview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExitInterview with ID {item_id} not found")
    return None

@router.get("/exitinterviews/analytics/metrics", response_model=Dict[str, Any])
def get_exitinterview_metrics():
    """Calculate summary statistical KPIs for ExitInterview collection."""
    svc = ExitInterviewService()
    return svc.calculate_aggregate_metrics()

# ==================== OrgHierarchyNode Endpoints ====================
@router.get("/orghierarchynodes", response_model=List[Dict[str, Any]])
def list_orghierarchynodes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OrgHierarchyNode records with pagination and filtering."""
    svc = OrgHierarchyNodeService()
    items = svc.list_orghierarchynodes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/orghierarchynodes/{item_id}", response_model=Dict[str, Any])
def get_orghierarchynode_by_id(item_id: int):
    """Retrieve detailed record for OrgHierarchyNode by ID."""
    svc = OrgHierarchyNodeService()
    item = svc.get_orghierarchynode_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OrgHierarchyNode with ID {item_id} not found")
    return item.to_dict()

@router.post("/orghierarchynodes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_orghierarchynode(payload: OrgHierarchyNodeCreateSchema):
    """Create new OrgHierarchyNode instance in enterprise repository."""
    svc = OrgHierarchyNodeService()
    try:
        item = svc.create_orghierarchynode(
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

@router.put("/orghierarchynodes/{item_id}", response_model=Dict[str, Any])
def update_orghierarchynode(item_id: int, payload: OrgHierarchyNodeUpdateSchema):
    """Update existing OrgHierarchyNode record fields."""
    svc = OrgHierarchyNodeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_orghierarchynode(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OrgHierarchyNode with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/orghierarchynodes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_orghierarchynode(item_id: int, hard: bool = Query(False)):
    """Delete OrgHierarchyNode record (soft-delete by default)."""
    svc = OrgHierarchyNodeService()
    ok = svc.delete_orghierarchynode(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OrgHierarchyNode with ID {item_id} not found")
    return None

@router.get("/orghierarchynodes/analytics/metrics", response_model=Dict[str, Any])
def get_orghierarchynode_metrics():
    """Calculate summary statistical KPIs for OrgHierarchyNode collection."""
    svc = OrgHierarchyNodeService()
    return svc.calculate_aggregate_metrics()

# ==================== CompensationBand Endpoints ====================
@router.get("/compensationbands", response_model=List[Dict[str, Any]])
def list_compensationbands(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CompensationBand records with pagination and filtering."""
    svc = CompensationBandService()
    items = svc.list_compensationbands(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/compensationbands/{item_id}", response_model=Dict[str, Any])
def get_compensationband_by_id(item_id: int):
    """Retrieve detailed record for CompensationBand by ID."""
    svc = CompensationBandService()
    item = svc.get_compensationband_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CompensationBand with ID {item_id} not found")
    return item.to_dict()

@router.post("/compensationbands", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_compensationband(payload: CompensationBandCreateSchema):
    """Create new CompensationBand instance in enterprise repository."""
    svc = CompensationBandService()
    try:
        item = svc.create_compensationband(
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

@router.put("/compensationbands/{item_id}", response_model=Dict[str, Any])
def update_compensationband(item_id: int, payload: CompensationBandUpdateSchema):
    """Update existing CompensationBand record fields."""
    svc = CompensationBandService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_compensationband(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CompensationBand with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/compensationbands/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_compensationband(item_id: int, hard: bool = Query(False)):
    """Delete CompensationBand record (soft-delete by default)."""
    svc = CompensationBandService()
    ok = svc.delete_compensationband(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CompensationBand with ID {item_id} not found")
    return None

@router.get("/compensationbands/analytics/metrics", response_model=Dict[str, Any])
def get_compensationband_metrics():
    """Calculate summary statistical KPIs for CompensationBand collection."""
    svc = CompensationBandService()
    return svc.calculate_aggregate_metrics()

# ==================== EmployeeSurvey Endpoints ====================
@router.get("/employeesurveys", response_model=List[Dict[str, Any]])
def list_employeesurveys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EmployeeSurvey records with pagination and filtering."""
    svc = EmployeeSurveyService()
    items = svc.list_employeesurveys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/employeesurveys/{item_id}", response_model=Dict[str, Any])
def get_employeesurvey_by_id(item_id: int):
    """Retrieve detailed record for EmployeeSurvey by ID."""
    svc = EmployeeSurveyService()
    item = svc.get_employeesurvey_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EmployeeSurvey with ID {item_id} not found")
    return item.to_dict()

@router.post("/employeesurveys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_employeesurvey(payload: EmployeeSurveyCreateSchema):
    """Create new EmployeeSurvey instance in enterprise repository."""
    svc = EmployeeSurveyService()
    try:
        item = svc.create_employeesurvey(
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

@router.put("/employeesurveys/{item_id}", response_model=Dict[str, Any])
def update_employeesurvey(item_id: int, payload: EmployeeSurveyUpdateSchema):
    """Update existing EmployeeSurvey record fields."""
    svc = EmployeeSurveyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_employeesurvey(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EmployeeSurvey with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/employeesurveys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employeesurvey(item_id: int, hard: bool = Query(False)):
    """Delete EmployeeSurvey record (soft-delete by default)."""
    svc = EmployeeSurveyService()
    ok = svc.delete_employeesurvey(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EmployeeSurvey with ID {item_id} not found")
    return None

@router.get("/employeesurveys/analytics/metrics", response_model=Dict[str, Any])
def get_employeesurvey_metrics():
    """Calculate summary statistical KPIs for EmployeeSurvey collection."""
    svc = EmployeeSurveyService()
    return svc.calculate_aggregate_metrics()

