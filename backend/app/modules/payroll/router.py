"""
Human Capital & Statutory Payroll - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    SalaryStructureService,
    PaySlipService,
    TaxDeductionService,
    EPFRecordService,
    ESICRecordService,
    GratuityCalculationService,
    BonusAllocationService,
    LeaveEncashmentService,
    ExpenseClaimService,
    LoanAdvanceService,
    ShiftAllowanceService,
    OvertimeRecordService,
    AppraisalReviewService,
    SkillCompetencyService,
    BenefitPlanService,
    FullFinalSettlementService,
)
from .schemas import (
    SalaryStructureCreateSchema, SalaryStructureUpdateSchema, SalaryStructureResponseSchema,
    PaySlipCreateSchema, PaySlipUpdateSchema, PaySlipResponseSchema,
    TaxDeductionCreateSchema, TaxDeductionUpdateSchema, TaxDeductionResponseSchema,
    EPFRecordCreateSchema, EPFRecordUpdateSchema, EPFRecordResponseSchema,
    ESICRecordCreateSchema, ESICRecordUpdateSchema, ESICRecordResponseSchema,
    GratuityCalculationCreateSchema, GratuityCalculationUpdateSchema, GratuityCalculationResponseSchema,
    BonusAllocationCreateSchema, BonusAllocationUpdateSchema, BonusAllocationResponseSchema,
    LeaveEncashmentCreateSchema, LeaveEncashmentUpdateSchema, LeaveEncashmentResponseSchema,
    ExpenseClaimCreateSchema, ExpenseClaimUpdateSchema, ExpenseClaimResponseSchema,
    LoanAdvanceCreateSchema, LoanAdvanceUpdateSchema, LoanAdvanceResponseSchema,
    ShiftAllowanceCreateSchema, ShiftAllowanceUpdateSchema, ShiftAllowanceResponseSchema,
    OvertimeRecordCreateSchema, OvertimeRecordUpdateSchema, OvertimeRecordResponseSchema,
    AppraisalReviewCreateSchema, AppraisalReviewUpdateSchema, AppraisalReviewResponseSchema,
    SkillCompetencyCreateSchema, SkillCompetencyUpdateSchema, SkillCompetencyResponseSchema,
    BenefitPlanCreateSchema, BenefitPlanUpdateSchema, BenefitPlanResponseSchema,
    FullFinalSettlementCreateSchema, FullFinalSettlementUpdateSchema, FullFinalSettlementResponseSchema,
)

router = APIRouter(prefix="/payroll", tags=["Human Capital & Statutory Payroll"])

# ==================== SalaryStructure Endpoints ====================
@router.get("/salarystructures", response_model=List[Dict[str, Any]])
def list_salarystructures(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SalaryStructure records with pagination and filtering."""
    svc = SalaryStructureService()
    items = svc.list_salarystructures(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/salarystructures/{item_id}", response_model=Dict[str, Any])
def get_salarystructure_by_id(item_id: int):
    """Retrieve detailed record for SalaryStructure by ID."""
    svc = SalaryStructureService()
    item = svc.get_salarystructure_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SalaryStructure with ID {item_id} not found")
    return item.to_dict()

@router.post("/salarystructures", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_salarystructure(payload: SalaryStructureCreateSchema):
    """Create new SalaryStructure instance in enterprise repository."""
    svc = SalaryStructureService()
    try:
        item = svc.create_salarystructure(
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

@router.put("/salarystructures/{item_id}", response_model=Dict[str, Any])
def update_salarystructure(item_id: int, payload: SalaryStructureUpdateSchema):
    """Update existing SalaryStructure record fields."""
    svc = SalaryStructureService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_salarystructure(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SalaryStructure with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/salarystructures/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_salarystructure(item_id: int, hard: bool = Query(False)):
    """Delete SalaryStructure record (soft-delete by default)."""
    svc = SalaryStructureService()
    ok = svc.delete_salarystructure(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SalaryStructure with ID {item_id} not found")
    return None

@router.get("/salarystructures/analytics/metrics", response_model=Dict[str, Any])
def get_salarystructure_metrics():
    """Calculate summary statistical KPIs for SalaryStructure collection."""
    svc = SalaryStructureService()
    return svc.calculate_aggregate_metrics()

# ==================== PaySlip Endpoints ====================
@router.get("/payslips", response_model=List[Dict[str, Any]])
def list_payslips(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PaySlip records with pagination and filtering."""
    svc = PaySlipService()
    items = svc.list_payslips(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/payslips/{item_id}", response_model=Dict[str, Any])
def get_payslip_by_id(item_id: int):
    """Retrieve detailed record for PaySlip by ID."""
    svc = PaySlipService()
    item = svc.get_payslip_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PaySlip with ID {item_id} not found")
    return item.to_dict()

@router.post("/payslips", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_payslip(payload: PaySlipCreateSchema):
    """Create new PaySlip instance in enterprise repository."""
    svc = PaySlipService()
    try:
        item = svc.create_payslip(
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

@router.put("/payslips/{item_id}", response_model=Dict[str, Any])
def update_payslip(item_id: int, payload: PaySlipUpdateSchema):
    """Update existing PaySlip record fields."""
    svc = PaySlipService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_payslip(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PaySlip with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/payslips/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payslip(item_id: int, hard: bool = Query(False)):
    """Delete PaySlip record (soft-delete by default)."""
    svc = PaySlipService()
    ok = svc.delete_payslip(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PaySlip with ID {item_id} not found")
    return None

@router.get("/payslips/analytics/metrics", response_model=Dict[str, Any])
def get_payslip_metrics():
    """Calculate summary statistical KPIs for PaySlip collection."""
    svc = PaySlipService()
    return svc.calculate_aggregate_metrics()

# ==================== TaxDeduction Endpoints ====================
@router.get("/taxdeductions", response_model=List[Dict[str, Any]])
def list_taxdeductions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TaxDeduction records with pagination and filtering."""
    svc = TaxDeductionService()
    items = svc.list_taxdeductions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/taxdeductions/{item_id}", response_model=Dict[str, Any])
def get_taxdeduction_by_id(item_id: int):
    """Retrieve detailed record for TaxDeduction by ID."""
    svc = TaxDeductionService()
    item = svc.get_taxdeduction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TaxDeduction with ID {item_id} not found")
    return item.to_dict()

@router.post("/taxdeductions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_taxdeduction(payload: TaxDeductionCreateSchema):
    """Create new TaxDeduction instance in enterprise repository."""
    svc = TaxDeductionService()
    try:
        item = svc.create_taxdeduction(
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

@router.put("/taxdeductions/{item_id}", response_model=Dict[str, Any])
def update_taxdeduction(item_id: int, payload: TaxDeductionUpdateSchema):
    """Update existing TaxDeduction record fields."""
    svc = TaxDeductionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_taxdeduction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TaxDeduction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/taxdeductions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_taxdeduction(item_id: int, hard: bool = Query(False)):
    """Delete TaxDeduction record (soft-delete by default)."""
    svc = TaxDeductionService()
    ok = svc.delete_taxdeduction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TaxDeduction with ID {item_id} not found")
    return None

@router.get("/taxdeductions/analytics/metrics", response_model=Dict[str, Any])
def get_taxdeduction_metrics():
    """Calculate summary statistical KPIs for TaxDeduction collection."""
    svc = TaxDeductionService()
    return svc.calculate_aggregate_metrics()

# ==================== EPFRecord Endpoints ====================
@router.get("/epfrecords", response_model=List[Dict[str, Any]])
def list_epfrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List EPFRecord records with pagination and filtering."""
    svc = EPFRecordService()
    items = svc.list_epfrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/epfrecords/{item_id}", response_model=Dict[str, Any])
def get_epfrecord_by_id(item_id: int):
    """Retrieve detailed record for EPFRecord by ID."""
    svc = EPFRecordService()
    item = svc.get_epfrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"EPFRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/epfrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_epfrecord(payload: EPFRecordCreateSchema):
    """Create new EPFRecord instance in enterprise repository."""
    svc = EPFRecordService()
    try:
        item = svc.create_epfrecord(
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

@router.put("/epfrecords/{item_id}", response_model=Dict[str, Any])
def update_epfrecord(item_id: int, payload: EPFRecordUpdateSchema):
    """Update existing EPFRecord record fields."""
    svc = EPFRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_epfrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"EPFRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/epfrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_epfrecord(item_id: int, hard: bool = Query(False)):
    """Delete EPFRecord record (soft-delete by default)."""
    svc = EPFRecordService()
    ok = svc.delete_epfrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"EPFRecord with ID {item_id} not found")
    return None

@router.get("/epfrecords/analytics/metrics", response_model=Dict[str, Any])
def get_epfrecord_metrics():
    """Calculate summary statistical KPIs for EPFRecord collection."""
    svc = EPFRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== ESICRecord Endpoints ====================
@router.get("/esicrecords", response_model=List[Dict[str, Any]])
def list_esicrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ESICRecord records with pagination and filtering."""
    svc = ESICRecordService()
    items = svc.list_esicrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/esicrecords/{item_id}", response_model=Dict[str, Any])
def get_esicrecord_by_id(item_id: int):
    """Retrieve detailed record for ESICRecord by ID."""
    svc = ESICRecordService()
    item = svc.get_esicrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ESICRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/esicrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_esicrecord(payload: ESICRecordCreateSchema):
    """Create new ESICRecord instance in enterprise repository."""
    svc = ESICRecordService()
    try:
        item = svc.create_esicrecord(
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

@router.put("/esicrecords/{item_id}", response_model=Dict[str, Any])
def update_esicrecord(item_id: int, payload: ESICRecordUpdateSchema):
    """Update existing ESICRecord record fields."""
    svc = ESICRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_esicrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ESICRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/esicrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_esicrecord(item_id: int, hard: bool = Query(False)):
    """Delete ESICRecord record (soft-delete by default)."""
    svc = ESICRecordService()
    ok = svc.delete_esicrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ESICRecord with ID {item_id} not found")
    return None

@router.get("/esicrecords/analytics/metrics", response_model=Dict[str, Any])
def get_esicrecord_metrics():
    """Calculate summary statistical KPIs for ESICRecord collection."""
    svc = ESICRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== GratuityCalculation Endpoints ====================
@router.get("/gratuitycalculations", response_model=List[Dict[str, Any]])
def list_gratuitycalculations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List GratuityCalculation records with pagination and filtering."""
    svc = GratuityCalculationService()
    items = svc.list_gratuitycalculations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/gratuitycalculations/{item_id}", response_model=Dict[str, Any])
def get_gratuitycalculation_by_id(item_id: int):
    """Retrieve detailed record for GratuityCalculation by ID."""
    svc = GratuityCalculationService()
    item = svc.get_gratuitycalculation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"GratuityCalculation with ID {item_id} not found")
    return item.to_dict()

@router.post("/gratuitycalculations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_gratuitycalculation(payload: GratuityCalculationCreateSchema):
    """Create new GratuityCalculation instance in enterprise repository."""
    svc = GratuityCalculationService()
    try:
        item = svc.create_gratuitycalculation(
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

@router.put("/gratuitycalculations/{item_id}", response_model=Dict[str, Any])
def update_gratuitycalculation(item_id: int, payload: GratuityCalculationUpdateSchema):
    """Update existing GratuityCalculation record fields."""
    svc = GratuityCalculationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_gratuitycalculation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"GratuityCalculation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/gratuitycalculations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gratuitycalculation(item_id: int, hard: bool = Query(False)):
    """Delete GratuityCalculation record (soft-delete by default)."""
    svc = GratuityCalculationService()
    ok = svc.delete_gratuitycalculation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"GratuityCalculation with ID {item_id} not found")
    return None

@router.get("/gratuitycalculations/analytics/metrics", response_model=Dict[str, Any])
def get_gratuitycalculation_metrics():
    """Calculate summary statistical KPIs for GratuityCalculation collection."""
    svc = GratuityCalculationService()
    return svc.calculate_aggregate_metrics()

# ==================== BonusAllocation Endpoints ====================
@router.get("/bonusallocations", response_model=List[Dict[str, Any]])
def list_bonusallocations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BonusAllocation records with pagination and filtering."""
    svc = BonusAllocationService()
    items = svc.list_bonusallocations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bonusallocations/{item_id}", response_model=Dict[str, Any])
def get_bonusallocation_by_id(item_id: int):
    """Retrieve detailed record for BonusAllocation by ID."""
    svc = BonusAllocationService()
    item = svc.get_bonusallocation_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BonusAllocation with ID {item_id} not found")
    return item.to_dict()

@router.post("/bonusallocations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bonusallocation(payload: BonusAllocationCreateSchema):
    """Create new BonusAllocation instance in enterprise repository."""
    svc = BonusAllocationService()
    try:
        item = svc.create_bonusallocation(
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

@router.put("/bonusallocations/{item_id}", response_model=Dict[str, Any])
def update_bonusallocation(item_id: int, payload: BonusAllocationUpdateSchema):
    """Update existing BonusAllocation record fields."""
    svc = BonusAllocationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bonusallocation(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BonusAllocation with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bonusallocations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bonusallocation(item_id: int, hard: bool = Query(False)):
    """Delete BonusAllocation record (soft-delete by default)."""
    svc = BonusAllocationService()
    ok = svc.delete_bonusallocation(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BonusAllocation with ID {item_id} not found")
    return None

@router.get("/bonusallocations/analytics/metrics", response_model=Dict[str, Any])
def get_bonusallocation_metrics():
    """Calculate summary statistical KPIs for BonusAllocation collection."""
    svc = BonusAllocationService()
    return svc.calculate_aggregate_metrics()

# ==================== LeaveEncashment Endpoints ====================
@router.get("/leaveencashments", response_model=List[Dict[str, Any]])
def list_leaveencashments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeaveEncashment records with pagination and filtering."""
    svc = LeaveEncashmentService()
    items = svc.list_leaveencashments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leaveencashments/{item_id}", response_model=Dict[str, Any])
def get_leaveencashment_by_id(item_id: int):
    """Retrieve detailed record for LeaveEncashment by ID."""
    svc = LeaveEncashmentService()
    item = svc.get_leaveencashment_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeaveEncashment with ID {item_id} not found")
    return item.to_dict()

@router.post("/leaveencashments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leaveencashment(payload: LeaveEncashmentCreateSchema):
    """Create new LeaveEncashment instance in enterprise repository."""
    svc = LeaveEncashmentService()
    try:
        item = svc.create_leaveencashment(
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

@router.put("/leaveencashments/{item_id}", response_model=Dict[str, Any])
def update_leaveencashment(item_id: int, payload: LeaveEncashmentUpdateSchema):
    """Update existing LeaveEncashment record fields."""
    svc = LeaveEncashmentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leaveencashment(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeaveEncashment with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leaveencashments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leaveencashment(item_id: int, hard: bool = Query(False)):
    """Delete LeaveEncashment record (soft-delete by default)."""
    svc = LeaveEncashmentService()
    ok = svc.delete_leaveencashment(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeaveEncashment with ID {item_id} not found")
    return None

@router.get("/leaveencashments/analytics/metrics", response_model=Dict[str, Any])
def get_leaveencashment_metrics():
    """Calculate summary statistical KPIs for LeaveEncashment collection."""
    svc = LeaveEncashmentService()
    return svc.calculate_aggregate_metrics()

# ==================== ExpenseClaim Endpoints ====================
@router.get("/expenseclaims", response_model=List[Dict[str, Any]])
def list_expenseclaims(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExpenseClaim records with pagination and filtering."""
    svc = ExpenseClaimService()
    items = svc.list_expenseclaims(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/expenseclaims/{item_id}", response_model=Dict[str, Any])
def get_expenseclaim_by_id(item_id: int):
    """Retrieve detailed record for ExpenseClaim by ID."""
    svc = ExpenseClaimService()
    item = svc.get_expenseclaim_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExpenseClaim with ID {item_id} not found")
    return item.to_dict()

@router.post("/expenseclaims", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_expenseclaim(payload: ExpenseClaimCreateSchema):
    """Create new ExpenseClaim instance in enterprise repository."""
    svc = ExpenseClaimService()
    try:
        item = svc.create_expenseclaim(
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

@router.put("/expenseclaims/{item_id}", response_model=Dict[str, Any])
def update_expenseclaim(item_id: int, payload: ExpenseClaimUpdateSchema):
    """Update existing ExpenseClaim record fields."""
    svc = ExpenseClaimService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_expenseclaim(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExpenseClaim with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/expenseclaims/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expenseclaim(item_id: int, hard: bool = Query(False)):
    """Delete ExpenseClaim record (soft-delete by default)."""
    svc = ExpenseClaimService()
    ok = svc.delete_expenseclaim(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExpenseClaim with ID {item_id} not found")
    return None

@router.get("/expenseclaims/analytics/metrics", response_model=Dict[str, Any])
def get_expenseclaim_metrics():
    """Calculate summary statistical KPIs for ExpenseClaim collection."""
    svc = ExpenseClaimService()
    return svc.calculate_aggregate_metrics()

# ==================== LoanAdvance Endpoints ====================
@router.get("/loanadvances", response_model=List[Dict[str, Any]])
def list_loanadvances(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LoanAdvance records with pagination and filtering."""
    svc = LoanAdvanceService()
    items = svc.list_loanadvances(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/loanadvances/{item_id}", response_model=Dict[str, Any])
def get_loanadvance_by_id(item_id: int):
    """Retrieve detailed record for LoanAdvance by ID."""
    svc = LoanAdvanceService()
    item = svc.get_loanadvance_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LoanAdvance with ID {item_id} not found")
    return item.to_dict()

@router.post("/loanadvances", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_loanadvance(payload: LoanAdvanceCreateSchema):
    """Create new LoanAdvance instance in enterprise repository."""
    svc = LoanAdvanceService()
    try:
        item = svc.create_loanadvance(
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

@router.put("/loanadvances/{item_id}", response_model=Dict[str, Any])
def update_loanadvance(item_id: int, payload: LoanAdvanceUpdateSchema):
    """Update existing LoanAdvance record fields."""
    svc = LoanAdvanceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_loanadvance(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LoanAdvance with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/loanadvances/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loanadvance(item_id: int, hard: bool = Query(False)):
    """Delete LoanAdvance record (soft-delete by default)."""
    svc = LoanAdvanceService()
    ok = svc.delete_loanadvance(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LoanAdvance with ID {item_id} not found")
    return None

@router.get("/loanadvances/analytics/metrics", response_model=Dict[str, Any])
def get_loanadvance_metrics():
    """Calculate summary statistical KPIs for LoanAdvance collection."""
    svc = LoanAdvanceService()
    return svc.calculate_aggregate_metrics()

# ==================== ShiftAllowance Endpoints ====================
@router.get("/shiftallowances", response_model=List[Dict[str, Any]])
def list_shiftallowances(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ShiftAllowance records with pagination and filtering."""
    svc = ShiftAllowanceService()
    items = svc.list_shiftallowances(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/shiftallowances/{item_id}", response_model=Dict[str, Any])
def get_shiftallowance_by_id(item_id: int):
    """Retrieve detailed record for ShiftAllowance by ID."""
    svc = ShiftAllowanceService()
    item = svc.get_shiftallowance_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ShiftAllowance with ID {item_id} not found")
    return item.to_dict()

@router.post("/shiftallowances", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_shiftallowance(payload: ShiftAllowanceCreateSchema):
    """Create new ShiftAllowance instance in enterprise repository."""
    svc = ShiftAllowanceService()
    try:
        item = svc.create_shiftallowance(
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

@router.put("/shiftallowances/{item_id}", response_model=Dict[str, Any])
def update_shiftallowance(item_id: int, payload: ShiftAllowanceUpdateSchema):
    """Update existing ShiftAllowance record fields."""
    svc = ShiftAllowanceService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_shiftallowance(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ShiftAllowance with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/shiftallowances/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shiftallowance(item_id: int, hard: bool = Query(False)):
    """Delete ShiftAllowance record (soft-delete by default)."""
    svc = ShiftAllowanceService()
    ok = svc.delete_shiftallowance(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ShiftAllowance with ID {item_id} not found")
    return None

@router.get("/shiftallowances/analytics/metrics", response_model=Dict[str, Any])
def get_shiftallowance_metrics():
    """Calculate summary statistical KPIs for ShiftAllowance collection."""
    svc = ShiftAllowanceService()
    return svc.calculate_aggregate_metrics()

# ==================== OvertimeRecord Endpoints ====================
@router.get("/overtimerecords", response_model=List[Dict[str, Any]])
def list_overtimerecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OvertimeRecord records with pagination and filtering."""
    svc = OvertimeRecordService()
    items = svc.list_overtimerecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/overtimerecords/{item_id}", response_model=Dict[str, Any])
def get_overtimerecord_by_id(item_id: int):
    """Retrieve detailed record for OvertimeRecord by ID."""
    svc = OvertimeRecordService()
    item = svc.get_overtimerecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OvertimeRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/overtimerecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_overtimerecord(payload: OvertimeRecordCreateSchema):
    """Create new OvertimeRecord instance in enterprise repository."""
    svc = OvertimeRecordService()
    try:
        item = svc.create_overtimerecord(
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

@router.put("/overtimerecords/{item_id}", response_model=Dict[str, Any])
def update_overtimerecord(item_id: int, payload: OvertimeRecordUpdateSchema):
    """Update existing OvertimeRecord record fields."""
    svc = OvertimeRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_overtimerecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OvertimeRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/overtimerecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_overtimerecord(item_id: int, hard: bool = Query(False)):
    """Delete OvertimeRecord record (soft-delete by default)."""
    svc = OvertimeRecordService()
    ok = svc.delete_overtimerecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OvertimeRecord with ID {item_id} not found")
    return None

@router.get("/overtimerecords/analytics/metrics", response_model=Dict[str, Any])
def get_overtimerecord_metrics():
    """Calculate summary statistical KPIs for OvertimeRecord collection."""
    svc = OvertimeRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== AppraisalReview Endpoints ====================
@router.get("/appraisalreviews", response_model=List[Dict[str, Any]])
def list_appraisalreviews(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AppraisalReview records with pagination and filtering."""
    svc = AppraisalReviewService()
    items = svc.list_appraisalreviews(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/appraisalreviews/{item_id}", response_model=Dict[str, Any])
def get_appraisalreview_by_id(item_id: int):
    """Retrieve detailed record for AppraisalReview by ID."""
    svc = AppraisalReviewService()
    item = svc.get_appraisalreview_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AppraisalReview with ID {item_id} not found")
    return item.to_dict()

@router.post("/appraisalreviews", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_appraisalreview(payload: AppraisalReviewCreateSchema):
    """Create new AppraisalReview instance in enterprise repository."""
    svc = AppraisalReviewService()
    try:
        item = svc.create_appraisalreview(
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

@router.put("/appraisalreviews/{item_id}", response_model=Dict[str, Any])
def update_appraisalreview(item_id: int, payload: AppraisalReviewUpdateSchema):
    """Update existing AppraisalReview record fields."""
    svc = AppraisalReviewService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_appraisalreview(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AppraisalReview with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/appraisalreviews/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appraisalreview(item_id: int, hard: bool = Query(False)):
    """Delete AppraisalReview record (soft-delete by default)."""
    svc = AppraisalReviewService()
    ok = svc.delete_appraisalreview(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AppraisalReview with ID {item_id} not found")
    return None

@router.get("/appraisalreviews/analytics/metrics", response_model=Dict[str, Any])
def get_appraisalreview_metrics():
    """Calculate summary statistical KPIs for AppraisalReview collection."""
    svc = AppraisalReviewService()
    return svc.calculate_aggregate_metrics()

# ==================== SkillCompetency Endpoints ====================
@router.get("/skillcompetencys", response_model=List[Dict[str, Any]])
def list_skillcompetencys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SkillCompetency records with pagination and filtering."""
    svc = SkillCompetencyService()
    items = svc.list_skillcompetencys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/skillcompetencys/{item_id}", response_model=Dict[str, Any])
def get_skillcompetency_by_id(item_id: int):
    """Retrieve detailed record for SkillCompetency by ID."""
    svc = SkillCompetencyService()
    item = svc.get_skillcompetency_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SkillCompetency with ID {item_id} not found")
    return item.to_dict()

@router.post("/skillcompetencys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_skillcompetency(payload: SkillCompetencyCreateSchema):
    """Create new SkillCompetency instance in enterprise repository."""
    svc = SkillCompetencyService()
    try:
        item = svc.create_skillcompetency(
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

@router.put("/skillcompetencys/{item_id}", response_model=Dict[str, Any])
def update_skillcompetency(item_id: int, payload: SkillCompetencyUpdateSchema):
    """Update existing SkillCompetency record fields."""
    svc = SkillCompetencyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_skillcompetency(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SkillCompetency with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/skillcompetencys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_skillcompetency(item_id: int, hard: bool = Query(False)):
    """Delete SkillCompetency record (soft-delete by default)."""
    svc = SkillCompetencyService()
    ok = svc.delete_skillcompetency(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SkillCompetency with ID {item_id} not found")
    return None

@router.get("/skillcompetencys/analytics/metrics", response_model=Dict[str, Any])
def get_skillcompetency_metrics():
    """Calculate summary statistical KPIs for SkillCompetency collection."""
    svc = SkillCompetencyService()
    return svc.calculate_aggregate_metrics()

# ==================== BenefitPlan Endpoints ====================
@router.get("/benefitplans", response_model=List[Dict[str, Any]])
def list_benefitplans(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BenefitPlan records with pagination and filtering."""
    svc = BenefitPlanService()
    items = svc.list_benefitplans(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/benefitplans/{item_id}", response_model=Dict[str, Any])
def get_benefitplan_by_id(item_id: int):
    """Retrieve detailed record for BenefitPlan by ID."""
    svc = BenefitPlanService()
    item = svc.get_benefitplan_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BenefitPlan with ID {item_id} not found")
    return item.to_dict()

@router.post("/benefitplans", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_benefitplan(payload: BenefitPlanCreateSchema):
    """Create new BenefitPlan instance in enterprise repository."""
    svc = BenefitPlanService()
    try:
        item = svc.create_benefitplan(
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

@router.put("/benefitplans/{item_id}", response_model=Dict[str, Any])
def update_benefitplan(item_id: int, payload: BenefitPlanUpdateSchema):
    """Update existing BenefitPlan record fields."""
    svc = BenefitPlanService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_benefitplan(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BenefitPlan with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/benefitplans/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_benefitplan(item_id: int, hard: bool = Query(False)):
    """Delete BenefitPlan record (soft-delete by default)."""
    svc = BenefitPlanService()
    ok = svc.delete_benefitplan(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BenefitPlan with ID {item_id} not found")
    return None

@router.get("/benefitplans/analytics/metrics", response_model=Dict[str, Any])
def get_benefitplan_metrics():
    """Calculate summary statistical KPIs for BenefitPlan collection."""
    svc = BenefitPlanService()
    return svc.calculate_aggregate_metrics()

# ==================== FullFinalSettlement Endpoints ====================
@router.get("/fullfinalsettlements", response_model=List[Dict[str, Any]])
def list_fullfinalsettlements(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FullFinalSettlement records with pagination and filtering."""
    svc = FullFinalSettlementService()
    items = svc.list_fullfinalsettlements(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/fullfinalsettlements/{item_id}", response_model=Dict[str, Any])
def get_fullfinalsettlement_by_id(item_id: int):
    """Retrieve detailed record for FullFinalSettlement by ID."""
    svc = FullFinalSettlementService()
    item = svc.get_fullfinalsettlement_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FullFinalSettlement with ID {item_id} not found")
    return item.to_dict()

@router.post("/fullfinalsettlements", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_fullfinalsettlement(payload: FullFinalSettlementCreateSchema):
    """Create new FullFinalSettlement instance in enterprise repository."""
    svc = FullFinalSettlementService()
    try:
        item = svc.create_fullfinalsettlement(
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

@router.put("/fullfinalsettlements/{item_id}", response_model=Dict[str, Any])
def update_fullfinalsettlement(item_id: int, payload: FullFinalSettlementUpdateSchema):
    """Update existing FullFinalSettlement record fields."""
    svc = FullFinalSettlementService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_fullfinalsettlement(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FullFinalSettlement with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/fullfinalsettlements/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fullfinalsettlement(item_id: int, hard: bool = Query(False)):
    """Delete FullFinalSettlement record (soft-delete by default)."""
    svc = FullFinalSettlementService()
    ok = svc.delete_fullfinalsettlement(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FullFinalSettlement with ID {item_id} not found")
    return None

@router.get("/fullfinalsettlements/analytics/metrics", response_model=Dict[str, Any])
def get_fullfinalsettlement_metrics():
    """Calculate summary statistical KPIs for FullFinalSettlement collection."""
    svc = FullFinalSettlementService()
    return svc.calculate_aggregate_metrics()

