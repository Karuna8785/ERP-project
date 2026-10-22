"""
Project Lifecycle & Milestone Billing - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ProjectCharterService,
    WBSPhaseService,
    MilestoneDeliverableService,
    ProjectTaskService,
    ResourceAllocationService,
    TimesheetLogService,
    ExpenseReimbursementService,
    ProjectBudgetService,
    EarnedValueSnapshotService,
    ChangeOrderRequestService,
    ProjectRiskLogService,
    StakeholderRegisterService,
    MilestoneBillingInvoiceService,
    VendorSubcontractService,
    StatusReportService,
    ProjectClosureReviewService,
)
from .schemas import (
    ProjectCharterCreateSchema, ProjectCharterUpdateSchema, ProjectCharterResponseSchema,
    WBSPhaseCreateSchema, WBSPhaseUpdateSchema, WBSPhaseResponseSchema,
    MilestoneDeliverableCreateSchema, MilestoneDeliverableUpdateSchema, MilestoneDeliverableResponseSchema,
    ProjectTaskCreateSchema, ProjectTaskUpdateSchema, ProjectTaskResponseSchema,
    ResourceAllocationCreateSchema, ResourceAllocationUpdateSchema, ResourceAllocationResponseSchema,
    TimesheetLogCreateSchema, TimesheetLogUpdateSchema, TimesheetLogResponseSchema,
    ExpenseReimbursementCreateSchema, ExpenseReimbursementUpdateSchema, ExpenseReimbursementResponseSchema,
    ProjectBudgetCreateSchema, ProjectBudgetUpdateSchema, ProjectBudgetResponseSchema,
    EarnedValueSnapshotCreateSchema, EarnedValueSnapshotUpdateSchema, EarnedValueSnapshotResponseSchema,
    ChangeOrderRequestCreateSchema, ChangeOrderRequestUpdateSchema, ChangeOrderRequestResponseSchema,
    ProjectRiskLogCreateSchema, ProjectRiskLogUpdateSchema, ProjectRiskLogResponseSchema,
    StakeholderRegisterCreateSchema, StakeholderRegisterUpdateSchema, StakeholderRegisterResponseSchema,
    MilestoneBillingInvoiceCreateSchema, MilestoneBillingInvoiceUpdateSchema, MilestoneBillingInvoiceResponseSchema,
    VendorSubcontractCreateSchema, VendorSubcontractUpdateSchema, VendorSubcontractResponseSchema,
    StatusReportCreateSchema, StatusReportUpdateSchema, StatusReportResponseSchema,
    ProjectClosureReviewCreateSchema, ProjectClosureReviewUpdateSchema, ProjectClosureReviewResponseSchema,
)

router = APIRouter(prefix="/project_management", tags=["Project Lifecycle & Milestone Billing"])

# ==================== ProjectCharter Endpoints ====================
@router.get("/projectcharters", response_model=List[Dict[str, Any]])
def list_projectcharters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProjectCharter records with pagination and filtering."""
    svc = ProjectCharterService()
    items = svc.list_projectcharters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/projectcharters/{item_id}", response_model=Dict[str, Any])
def get_projectcharter_by_id(item_id: int):
    """Retrieve detailed record for ProjectCharter by ID."""
    svc = ProjectCharterService()
    item = svc.get_projectcharter_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProjectCharter with ID {item_id} not found")
    return item.to_dict()

@router.post("/projectcharters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_projectcharter(payload: ProjectCharterCreateSchema):
    """Create new ProjectCharter instance in enterprise repository."""
    svc = ProjectCharterService()
    try:
        item = svc.create_projectcharter(
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

@router.put("/projectcharters/{item_id}", response_model=Dict[str, Any])
def update_projectcharter(item_id: int, payload: ProjectCharterUpdateSchema):
    """Update existing ProjectCharter record fields."""
    svc = ProjectCharterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_projectcharter(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProjectCharter with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/projectcharters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projectcharter(item_id: int, hard: bool = Query(False)):
    """Delete ProjectCharter record (soft-delete by default)."""
    svc = ProjectCharterService()
    ok = svc.delete_projectcharter(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProjectCharter with ID {item_id} not found")
    return None

@router.get("/projectcharters/analytics/metrics", response_model=Dict[str, Any])
def get_projectcharter_metrics():
    """Calculate summary statistical KPIs for ProjectCharter collection."""
    svc = ProjectCharterService()
    return svc.calculate_aggregate_metrics()

# ==================== WBSPhase Endpoints ====================
@router.get("/wbsphases", response_model=List[Dict[str, Any]])
def list_wbsphases(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WBSPhase records with pagination and filtering."""
    svc = WBSPhaseService()
    items = svc.list_wbsphases(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/wbsphases/{item_id}", response_model=Dict[str, Any])
def get_wbsphase_by_id(item_id: int):
    """Retrieve detailed record for WBSPhase by ID."""
    svc = WBSPhaseService()
    item = svc.get_wbsphase_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WBSPhase with ID {item_id} not found")
    return item.to_dict()

@router.post("/wbsphases", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_wbsphase(payload: WBSPhaseCreateSchema):
    """Create new WBSPhase instance in enterprise repository."""
    svc = WBSPhaseService()
    try:
        item = svc.create_wbsphase(
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

@router.put("/wbsphases/{item_id}", response_model=Dict[str, Any])
def update_wbsphase(item_id: int, payload: WBSPhaseUpdateSchema):
    """Update existing WBSPhase record fields."""
    svc = WBSPhaseService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_wbsphase(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WBSPhase with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/wbsphases/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wbsphase(item_id: int, hard: bool = Query(False)):
    """Delete WBSPhase record (soft-delete by default)."""
    svc = WBSPhaseService()
    ok = svc.delete_wbsphase(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WBSPhase with ID {item_id} not found")
    return None

@router.get("/wbsphases/analytics/metrics", response_model=Dict[str, Any])
def get_wbsphase_metrics():
    """Calculate summary statistical KPIs for WBSPhase collection."""
    svc = WBSPhaseService()
    return svc.calculate_aggregate_metrics()

# ==================== MilestoneDeliverable Endpoints ====================
@router.get("/milestonedeliverables", response_model=List[Dict[str, Any]])
def list_milestonedeliverables(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MilestoneDeliverable records with pagination and filtering."""
    svc = MilestoneDeliverableService()
    items = svc.list_milestonedeliverables(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/milestonedeliverables/{item_id}", response_model=Dict[str, Any])
def get_milestonedeliverable_by_id(item_id: int):
    """Retrieve detailed record for MilestoneDeliverable by ID."""
    svc = MilestoneDeliverableService()
    item = svc.get_milestonedeliverable_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MilestoneDeliverable with ID {item_id} not found")
    return item.to_dict()

@router.post("/milestonedeliverables", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_milestonedeliverable(payload: MilestoneDeliverableCreateSchema):
    """Create new MilestoneDeliverable instance in enterprise repository."""
    svc = MilestoneDeliverableService()
    try:
        item = svc.create_milestonedeliverable(
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

@router.put("/milestonedeliverables/{item_id}", response_model=Dict[str, Any])
def update_milestonedeliverable(item_id: int, payload: MilestoneDeliverableUpdateSchema):
    """Update existing MilestoneDeliverable record fields."""
    svc = MilestoneDeliverableService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_milestonedeliverable(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MilestoneDeliverable with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/milestonedeliverables/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_milestonedeliverable(item_id: int, hard: bool = Query(False)):
    """Delete MilestoneDeliverable record (soft-delete by default)."""
    svc = MilestoneDeliverableService()
    ok = svc.delete_milestonedeliverable(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MilestoneDeliverable with ID {item_id} not found")
    return None

@router.get("/milestonedeliverables/analytics/metrics", response_model=Dict[str, Any])
def get_milestonedeliverable_metrics():
    """Calculate summary statistical KPIs for MilestoneDeliverable collection."""
    svc = MilestoneDeliverableService()
    return svc.calculate_aggregate_metrics()

# ==================== ProjectTask Endpoints ====================
@router.get("/projecttasks", response_model=List[Dict[str, Any]])
def list_projecttasks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProjectTask records with pagination and filtering."""
    svc = ProjectTaskService()
    items = svc.list_projecttasks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/projecttasks/{item_id}", response_model=Dict[str, Any])
def get_projecttask_by_id(item_id: int):
    """Retrieve detailed record for ProjectTask by ID."""
    svc = ProjectTaskService()
    item = svc.get_projecttask_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProjectTask with ID {item_id} not found")
    return item.to_dict()

@router.post("/projecttasks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_projecttask(payload: ProjectTaskCreateSchema):
    """Create new ProjectTask instance in enterprise repository."""
    svc = ProjectTaskService()
    try:
        item = svc.create_projecttask(
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

@router.put("/projecttasks/{item_id}", response_model=Dict[str, Any])
def update_projecttask(item_id: int, payload: ProjectTaskUpdateSchema):
    """Update existing ProjectTask record fields."""
    svc = ProjectTaskService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_projecttask(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProjectTask with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/projecttasks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projecttask(item_id: int, hard: bool = Query(False)):
    """Delete ProjectTask record (soft-delete by default)."""
    svc = ProjectTaskService()
    ok = svc.delete_projecttask(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProjectTask with ID {item_id} not found")
    return None

@router.get("/projecttasks/analytics/metrics", response_model=Dict[str, Any])
def get_projecttask_metrics():
    """Calculate summary statistical KPIs for ProjectTask collection."""
    svc = ProjectTaskService()
    return svc.calculate_aggregate_metrics()

# ==================== ResourceAllocation Endpoints ====================
@router.get("/resourceallocations", response_model=List[Dict[str, Any]])
def list_resourceallocations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ResourceAllocation records with pagination and filtering."""
    svc = ResourceAllocationService()
    items = svc.list_resourceallocations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/resourceallocations/{item_id}", response_model=Dict[str, Any])
def get_resourceallocation_by_id(item_id: int):
    """Retrieve detailed record for ResourceAllocation by ID."""
    svc = ResourceAllocationService()
    item = svc.get_resourceallocation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ResourceAllocation with ID {item_id} not found")
    return item.to_dict()

@router.post("/resourceallocations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_resourceallocation(payload: ResourceAllocationCreateSchema):
    """Create new ResourceAllocation instance in enterprise repository."""
    svc = ResourceAllocationService()
    try:
        item = svc.create_resourceallocation(
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

@router.put("/resourceallocations/{item_id}", response_model=Dict[str, Any])
def update_resourceallocation(item_id: int, payload: ResourceAllocationUpdateSchema):
    """Update existing ResourceAllocation record fields."""
    svc = ResourceAllocationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_resourceallocation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ResourceAllocation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/resourceallocations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resourceallocation(item_id: int, hard: bool = Query(False)):
    """Delete ResourceAllocation record (soft-delete by default)."""
    svc = ResourceAllocationService()
    ok = svc.delete_resourceallocation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ResourceAllocation with ID {item_id} not found")
    return None

@router.get("/resourceallocations/analytics/metrics", response_model=Dict[str, Any])
def get_resourceallocation_metrics():
    """Calculate summary statistical KPIs for ResourceAllocation collection."""
    svc = ResourceAllocationService()
    return svc.calculate_aggregate_metrics()

# ==================== TimesheetLog Endpoints ====================
@router.get("/timesheetlogs", response_model=List[Dict[str, Any]])
def list_timesheetlogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TimesheetLog records with pagination and filtering."""
    svc = TimesheetLogService()
    items = svc.list_timesheetlogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/timesheetlogs/{item_id}", response_model=Dict[str, Any])
def get_timesheetlog_by_id(item_id: int):
    """Retrieve detailed record for TimesheetLog by ID."""
    svc = TimesheetLogService()
    item = svc.get_timesheetlog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TimesheetLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/timesheetlogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_timesheetlog(payload: TimesheetLogCreateSchema):
    """Create new TimesheetLog instance in enterprise repository."""
    svc = TimesheetLogService()
    try:
        item = svc.create_timesheetlog(
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

@router.put("/timesheetlogs/{item_id}", response_model=Dict[str, Any])
def update_timesheetlog(item_id: int, payload: TimesheetLogUpdateSchema):
    """Update existing TimesheetLog record fields."""
    svc = TimesheetLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_timesheetlog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TimesheetLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/timesheetlogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_timesheetlog(item_id: int, hard: bool = Query(False)):
    """Delete TimesheetLog record (soft-delete by default)."""
    svc = TimesheetLogService()
    ok = svc.delete_timesheetlog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TimesheetLog with ID {item_id} not found")
    return None

@router.get("/timesheetlogs/analytics/metrics", response_model=Dict[str, Any])
def get_timesheetlog_metrics():
    """Calculate summary statistical KPIs for TimesheetLog collection."""
    svc = TimesheetLogService()
    return svc.calculate_aggregate_metrics()

# ==================== ExpenseReimbursement Endpoints ====================
@router.get("/expensereimbursements", response_model=List[Dict[str, Any]])
def list_expensereimbursements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExpenseReimbursement records with pagination and filtering."""
    svc = ExpenseReimbursementService()
    items = svc.list_expensereimbursements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/expensereimbursements/{item_id}", response_model=Dict[str, Any])
def get_expensereimbursement_by_id(item_id: int):
    """Retrieve detailed record for ExpenseReimbursement by ID."""
    svc = ExpenseReimbursementService()
    item = svc.get_expensereimbursement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExpenseReimbursement with ID {item_id} not found")
    return item.to_dict()

@router.post("/expensereimbursements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_expensereimbursement(payload: ExpenseReimbursementCreateSchema):
    """Create new ExpenseReimbursement instance in enterprise repository."""
    svc = ExpenseReimbursementService()
    try:
        item = svc.create_expensereimbursement(
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

@router.put("/expensereimbursements/{item_id}", response_model=Dict[str, Any])
def update_expensereimbursement(item_id: int, payload: ExpenseReimbursementUpdateSchema):
    """Update existing ExpenseReimbursement record fields."""
    svc = ExpenseReimbursementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_expensereimbursement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExpenseReimbursement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/expensereimbursements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expensereimbursement(item_id: int, hard: bool = Query(False)):
    """Delete ExpenseReimbursement record (soft-delete by default)."""
    svc = ExpenseReimbursementService()
    ok = svc.delete_expensereimbursement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExpenseReimbursement with ID {item_id} not found")
    return None

@router.get("/expensereimbursements/analytics/metrics", response_model=Dict[str, Any])
def get_expensereimbursement_metrics():
    """Calculate summary statistical KPIs for ExpenseReimbursement collection."""
    svc = ExpenseReimbursementService()
    return svc.calculate_aggregate_metrics()

# ==================== ProjectBudget Endpoints ====================
@router.get("/projectbudgets", response_model=List[Dict[str, Any]])
def list_projectbudgets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProjectBudget records with pagination and filtering."""
    svc = ProjectBudgetService()
    items = svc.list_projectbudgets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/projectbudgets/{item_id}", response_model=Dict[str, Any])
def get_projectbudget_by_id(item_id: int):
    """Retrieve detailed record for ProjectBudget by ID."""
    svc = ProjectBudgetService()
    item = svc.get_projectbudget_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProjectBudget with ID {item_id} not found")
    return item.to_dict()

@router.post("/projectbudgets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_projectbudget(payload: ProjectBudgetCreateSchema):
    """Create new ProjectBudget instance in enterprise repository."""
    svc = ProjectBudgetService()
    try:
        item = svc.create_projectbudget(
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

@router.put("/projectbudgets/{item_id}", response_model=Dict[str, Any])
def update_projectbudget(item_id: int, payload: ProjectBudgetUpdateSchema):
    """Update existing ProjectBudget record fields."""
    svc = ProjectBudgetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_projectbudget(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProjectBudget with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/projectbudgets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projectbudget(item_id: int, hard: bool = Query(False)):
    """Delete ProjectBudget record (soft-delete by default)."""
    svc = ProjectBudgetService()
    ok = svc.delete_projectbudget(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProjectBudget with ID {item_id} not found")
    return None

@router.get("/projectbudgets/analytics/metrics", response_model=Dict[str, Any])
def get_projectbudget_metrics():
    """Calculate summary statistical KPIs for ProjectBudget collection."""
    svc = ProjectBudgetService()
    return svc.calculate_aggregate_metrics()

# ==================== EarnedValueSnapshot Endpoints ====================
@router.get("/earnedvaluesnapshots", response_model=List[Dict[str, Any]])
def list_earnedvaluesnapshots(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EarnedValueSnapshot records with pagination and filtering."""
    svc = EarnedValueSnapshotService()
    items = svc.list_earnedvaluesnapshots(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/earnedvaluesnapshots/{item_id}", response_model=Dict[str, Any])
def get_earnedvaluesnapshot_by_id(item_id: int):
    """Retrieve detailed record for EarnedValueSnapshot by ID."""
    svc = EarnedValueSnapshotService()
    item = svc.get_earnedvaluesnapshot_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EarnedValueSnapshot with ID {item_id} not found")
    return item.to_dict()

@router.post("/earnedvaluesnapshots", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_earnedvaluesnapshot(payload: EarnedValueSnapshotCreateSchema):
    """Create new EarnedValueSnapshot instance in enterprise repository."""
    svc = EarnedValueSnapshotService()
    try:
        item = svc.create_earnedvaluesnapshot(
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

@router.put("/earnedvaluesnapshots/{item_id}", response_model=Dict[str, Any])
def update_earnedvaluesnapshot(item_id: int, payload: EarnedValueSnapshotUpdateSchema):
    """Update existing EarnedValueSnapshot record fields."""
    svc = EarnedValueSnapshotService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_earnedvaluesnapshot(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EarnedValueSnapshot with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/earnedvaluesnapshots/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_earnedvaluesnapshot(item_id: int, hard: bool = Query(False)):
    """Delete EarnedValueSnapshot record (soft-delete by default)."""
    svc = EarnedValueSnapshotService()
    ok = svc.delete_earnedvaluesnapshot(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EarnedValueSnapshot with ID {item_id} not found")
    return None

@router.get("/earnedvaluesnapshots/analytics/metrics", response_model=Dict[str, Any])
def get_earnedvaluesnapshot_metrics():
    """Calculate summary statistical KPIs for EarnedValueSnapshot collection."""
    svc = EarnedValueSnapshotService()
    return svc.calculate_aggregate_metrics()

# ==================== ChangeOrderRequest Endpoints ====================
@router.get("/changeorderrequests", response_model=List[Dict[str, Any]])
def list_changeorderrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChangeOrderRequest records with pagination and filtering."""
    svc = ChangeOrderRequestService()
    items = svc.list_changeorderrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/changeorderrequests/{item_id}", response_model=Dict[str, Any])
def get_changeorderrequest_by_id(item_id: int):
    """Retrieve detailed record for ChangeOrderRequest by ID."""
    svc = ChangeOrderRequestService()
    item = svc.get_changeorderrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChangeOrderRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/changeorderrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_changeorderrequest(payload: ChangeOrderRequestCreateSchema):
    """Create new ChangeOrderRequest instance in enterprise repository."""
    svc = ChangeOrderRequestService()
    try:
        item = svc.create_changeorderrequest(
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

@router.put("/changeorderrequests/{item_id}", response_model=Dict[str, Any])
def update_changeorderrequest(item_id: int, payload: ChangeOrderRequestUpdateSchema):
    """Update existing ChangeOrderRequest record fields."""
    svc = ChangeOrderRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_changeorderrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChangeOrderRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/changeorderrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_changeorderrequest(item_id: int, hard: bool = Query(False)):
    """Delete ChangeOrderRequest record (soft-delete by default)."""
    svc = ChangeOrderRequestService()
    ok = svc.delete_changeorderrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChangeOrderRequest with ID {item_id} not found")
    return None

@router.get("/changeorderrequests/analytics/metrics", response_model=Dict[str, Any])
def get_changeorderrequest_metrics():
    """Calculate summary statistical KPIs for ChangeOrderRequest collection."""
    svc = ChangeOrderRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== ProjectRiskLog Endpoints ====================
@router.get("/projectrisklogs", response_model=List[Dict[str, Any]])
def list_projectrisklogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProjectRiskLog records with pagination and filtering."""
    svc = ProjectRiskLogService()
    items = svc.list_projectrisklogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/projectrisklogs/{item_id}", response_model=Dict[str, Any])
def get_projectrisklog_by_id(item_id: int):
    """Retrieve detailed record for ProjectRiskLog by ID."""
    svc = ProjectRiskLogService()
    item = svc.get_projectrisklog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProjectRiskLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/projectrisklogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_projectrisklog(payload: ProjectRiskLogCreateSchema):
    """Create new ProjectRiskLog instance in enterprise repository."""
    svc = ProjectRiskLogService()
    try:
        item = svc.create_projectrisklog(
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

@router.put("/projectrisklogs/{item_id}", response_model=Dict[str, Any])
def update_projectrisklog(item_id: int, payload: ProjectRiskLogUpdateSchema):
    """Update existing ProjectRiskLog record fields."""
    svc = ProjectRiskLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_projectrisklog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProjectRiskLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/projectrisklogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projectrisklog(item_id: int, hard: bool = Query(False)):
    """Delete ProjectRiskLog record (soft-delete by default)."""
    svc = ProjectRiskLogService()
    ok = svc.delete_projectrisklog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProjectRiskLog with ID {item_id} not found")
    return None

@router.get("/projectrisklogs/analytics/metrics", response_model=Dict[str, Any])
def get_projectrisklog_metrics():
    """Calculate summary statistical KPIs for ProjectRiskLog collection."""
    svc = ProjectRiskLogService()
    return svc.calculate_aggregate_metrics()

# ==================== StakeholderRegister Endpoints ====================
@router.get("/stakeholderregisters", response_model=List[Dict[str, Any]])
def list_stakeholderregisters(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StakeholderRegister records with pagination and filtering."""
    svc = StakeholderRegisterService()
    items = svc.list_stakeholderregisters(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/stakeholderregisters/{item_id}", response_model=Dict[str, Any])
def get_stakeholderregister_by_id(item_id: int):
    """Retrieve detailed record for StakeholderRegister by ID."""
    svc = StakeholderRegisterService()
    item = svc.get_stakeholderregister_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StakeholderRegister with ID {item_id} not found")
    return item.to_dict()

@router.post("/stakeholderregisters", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_stakeholderregister(payload: StakeholderRegisterCreateSchema):
    """Create new StakeholderRegister instance in enterprise repository."""
    svc = StakeholderRegisterService()
    try:
        item = svc.create_stakeholderregister(
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

@router.put("/stakeholderregisters/{item_id}", response_model=Dict[str, Any])
def update_stakeholderregister(item_id: int, payload: StakeholderRegisterUpdateSchema):
    """Update existing StakeholderRegister record fields."""
    svc = StakeholderRegisterService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_stakeholderregister(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StakeholderRegister with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/stakeholderregisters/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stakeholderregister(item_id: int, hard: bool = Query(False)):
    """Delete StakeholderRegister record (soft-delete by default)."""
    svc = StakeholderRegisterService()
    ok = svc.delete_stakeholderregister(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StakeholderRegister with ID {item_id} not found")
    return None

@router.get("/stakeholderregisters/analytics/metrics", response_model=Dict[str, Any])
def get_stakeholderregister_metrics():
    """Calculate summary statistical KPIs for StakeholderRegister collection."""
    svc = StakeholderRegisterService()
    return svc.calculate_aggregate_metrics()

# ==================== MilestoneBillingInvoice Endpoints ====================
@router.get("/milestonebillinginvoices", response_model=List[Dict[str, Any]])
def list_milestonebillinginvoices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MilestoneBillingInvoice records with pagination and filtering."""
    svc = MilestoneBillingInvoiceService()
    items = svc.list_milestonebillinginvoices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/milestonebillinginvoices/{item_id}", response_model=Dict[str, Any])
def get_milestonebillinginvoice_by_id(item_id: int):
    """Retrieve detailed record for MilestoneBillingInvoice by ID."""
    svc = MilestoneBillingInvoiceService()
    item = svc.get_milestonebillinginvoice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MilestoneBillingInvoice with ID {item_id} not found")
    return item.to_dict()

@router.post("/milestonebillinginvoices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_milestonebillinginvoice(payload: MilestoneBillingInvoiceCreateSchema):
    """Create new MilestoneBillingInvoice instance in enterprise repository."""
    svc = MilestoneBillingInvoiceService()
    try:
        item = svc.create_milestonebillinginvoice(
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

@router.put("/milestonebillinginvoices/{item_id}", response_model=Dict[str, Any])
def update_milestonebillinginvoice(item_id: int, payload: MilestoneBillingInvoiceUpdateSchema):
    """Update existing MilestoneBillingInvoice record fields."""
    svc = MilestoneBillingInvoiceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_milestonebillinginvoice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MilestoneBillingInvoice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/milestonebillinginvoices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_milestonebillinginvoice(item_id: int, hard: bool = Query(False)):
    """Delete MilestoneBillingInvoice record (soft-delete by default)."""
    svc = MilestoneBillingInvoiceService()
    ok = svc.delete_milestonebillinginvoice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MilestoneBillingInvoice with ID {item_id} not found")
    return None

@router.get("/milestonebillinginvoices/analytics/metrics", response_model=Dict[str, Any])
def get_milestonebillinginvoice_metrics():
    """Calculate summary statistical KPIs for MilestoneBillingInvoice collection."""
    svc = MilestoneBillingInvoiceService()
    return svc.calculate_aggregate_metrics()

# ==================== VendorSubcontract Endpoints ====================
@router.get("/vendorsubcontracts", response_model=List[Dict[str, Any]])
def list_vendorsubcontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List VendorSubcontract records with pagination and filtering."""
    svc = VendorSubcontractService()
    items = svc.list_vendorsubcontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/vendorsubcontracts/{item_id}", response_model=Dict[str, Any])
def get_vendorsubcontract_by_id(item_id: int):
    """Retrieve detailed record for VendorSubcontract by ID."""
    svc = VendorSubcontractService()
    item = svc.get_vendorsubcontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"VendorSubcontract with ID {item_id} not found")
    return item.to_dict()

@router.post("/vendorsubcontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_vendorsubcontract(payload: VendorSubcontractCreateSchema):
    """Create new VendorSubcontract instance in enterprise repository."""
    svc = VendorSubcontractService()
    try:
        item = svc.create_vendorsubcontract(
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

@router.put("/vendorsubcontracts/{item_id}", response_model=Dict[str, Any])
def update_vendorsubcontract(item_id: int, payload: VendorSubcontractUpdateSchema):
    """Update existing VendorSubcontract record fields."""
    svc = VendorSubcontractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_vendorsubcontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"VendorSubcontract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/vendorsubcontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendorsubcontract(item_id: int, hard: bool = Query(False)):
    """Delete VendorSubcontract record (soft-delete by default)."""
    svc = VendorSubcontractService()
    ok = svc.delete_vendorsubcontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"VendorSubcontract with ID {item_id} not found")
    return None

@router.get("/vendorsubcontracts/analytics/metrics", response_model=Dict[str, Any])
def get_vendorsubcontract_metrics():
    """Calculate summary statistical KPIs for VendorSubcontract collection."""
    svc = VendorSubcontractService()
    return svc.calculate_aggregate_metrics()

# ==================== StatusReport Endpoints ====================
@router.get("/statusreports", response_model=List[Dict[str, Any]])
def list_statusreports(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StatusReport records with pagination and filtering."""
    svc = StatusReportService()
    items = svc.list_statusreports(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/statusreports/{item_id}", response_model=Dict[str, Any])
def get_statusreport_by_id(item_id: int):
    """Retrieve detailed record for StatusReport by ID."""
    svc = StatusReportService()
    item = svc.get_statusreport_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StatusReport with ID {item_id} not found")
    return item.to_dict()

@router.post("/statusreports", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_statusreport(payload: StatusReportCreateSchema):
    """Create new StatusReport instance in enterprise repository."""
    svc = StatusReportService()
    try:
        item = svc.create_statusreport(
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

@router.put("/statusreports/{item_id}", response_model=Dict[str, Any])
def update_statusreport(item_id: int, payload: StatusReportUpdateSchema):
    """Update existing StatusReport record fields."""
    svc = StatusReportService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_statusreport(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StatusReport with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/statusreports/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_statusreport(item_id: int, hard: bool = Query(False)):
    """Delete StatusReport record (soft-delete by default)."""
    svc = StatusReportService()
    ok = svc.delete_statusreport(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StatusReport with ID {item_id} not found")
    return None

@router.get("/statusreports/analytics/metrics", response_model=Dict[str, Any])
def get_statusreport_metrics():
    """Calculate summary statistical KPIs for StatusReport collection."""
    svc = StatusReportService()
    return svc.calculate_aggregate_metrics()

# ==================== ProjectClosureReview Endpoints ====================
@router.get("/projectclosurereviews", response_model=List[Dict[str, Any]])
def list_projectclosurereviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ProjectClosureReview records with pagination and filtering."""
    svc = ProjectClosureReviewService()
    items = svc.list_projectclosurereviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/projectclosurereviews/{item_id}", response_model=Dict[str, Any])
def get_projectclosurereview_by_id(item_id: int):
    """Retrieve detailed record for ProjectClosureReview by ID."""
    svc = ProjectClosureReviewService()
    item = svc.get_projectclosurereview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ProjectClosureReview with ID {item_id} not found")
    return item.to_dict()

@router.post("/projectclosurereviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_projectclosurereview(payload: ProjectClosureReviewCreateSchema):
    """Create new ProjectClosureReview instance in enterprise repository."""
    svc = ProjectClosureReviewService()
    try:
        item = svc.create_projectclosurereview(
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

@router.put("/projectclosurereviews/{item_id}", response_model=Dict[str, Any])
def update_projectclosurereview(item_id: int, payload: ProjectClosureReviewUpdateSchema):
    """Update existing ProjectClosureReview record fields."""
    svc = ProjectClosureReviewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_projectclosurereview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ProjectClosureReview with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/projectclosurereviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projectclosurereview(item_id: int, hard: bool = Query(False)):
    """Delete ProjectClosureReview record (soft-delete by default)."""
    svc = ProjectClosureReviewService()
    ok = svc.delete_projectclosurereview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ProjectClosureReview with ID {item_id} not found")
    return None

@router.get("/projectclosurereviews/analytics/metrics", response_model=Dict[str, Any])
def get_projectclosurereview_metrics():
    """Calculate summary statistical KPIs for ProjectClosureReview collection."""
    svc = ProjectClosureReviewService()
    return svc.calculate_aggregate_metrics()

