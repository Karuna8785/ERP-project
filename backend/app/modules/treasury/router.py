"""
Corporate Treasury & Cash Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    BankAccountService,
    CashFlowForecastService,
    ExchangeContractService,
    LetterOfCreditService,
    BankGuaranteeService,
    InvestmentSecurityService,
    LoanFacilityService,
    InterestAccrualService,
    LiquidityPoolService,
    TreasuryDealService,
    HedgingContractService,
    SweepRuleService,
    CounterpartyLimitService,
    DividendRecordService,
    LeaseContractService,
    FinancialRatioService,
)
from .schemas import (
    BankAccountCreateSchema, BankAccountUpdateSchema, BankAccountResponseSchema,
    CashFlowForecastCreateSchema, CashFlowForecastUpdateSchema, CashFlowForecastResponseSchema,
    ExchangeContractCreateSchema, ExchangeContractUpdateSchema, ExchangeContractResponseSchema,
    LetterOfCreditCreateSchema, LetterOfCreditUpdateSchema, LetterOfCreditResponseSchema,
    BankGuaranteeCreateSchema, BankGuaranteeUpdateSchema, BankGuaranteeResponseSchema,
    InvestmentSecurityCreateSchema, InvestmentSecurityUpdateSchema, InvestmentSecurityResponseSchema,
    LoanFacilityCreateSchema, LoanFacilityUpdateSchema, LoanFacilityResponseSchema,
    InterestAccrualCreateSchema, InterestAccrualUpdateSchema, InterestAccrualResponseSchema,
    LiquidityPoolCreateSchema, LiquidityPoolUpdateSchema, LiquidityPoolResponseSchema,
    TreasuryDealCreateSchema, TreasuryDealUpdateSchema, TreasuryDealResponseSchema,
    HedgingContractCreateSchema, HedgingContractUpdateSchema, HedgingContractResponseSchema,
    SweepRuleCreateSchema, SweepRuleUpdateSchema, SweepRuleResponseSchema,
    CounterpartyLimitCreateSchema, CounterpartyLimitUpdateSchema, CounterpartyLimitResponseSchema,
    DividendRecordCreateSchema, DividendRecordUpdateSchema, DividendRecordResponseSchema,
    LeaseContractCreateSchema, LeaseContractUpdateSchema, LeaseContractResponseSchema,
    FinancialRatioCreateSchema, FinancialRatioUpdateSchema, FinancialRatioResponseSchema,
)

router = APIRouter(prefix="/treasury", tags=["Corporate Treasury & Cash Management"])

# ==================== BankAccount Endpoints ====================
@router.get("/bankaccounts", response_model=List[Dict[str, Any]])
def list_bankaccounts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BankAccount records with pagination and filtering."""
    svc = BankAccountService()
    items = svc.list_bankaccounts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bankaccounts/{item_id}", response_model=Dict[str, Any])
def get_bankaccount_by_id(item_id: int):
    """Retrieve detailed record for BankAccount by ID."""
    svc = BankAccountService()
    item = svc.get_bankaccount_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BankAccount with ID {item_id} not found")
    return item.to_dict()

@router.post("/bankaccounts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bankaccount(payload: BankAccountCreateSchema):
    """Create new BankAccount instance in enterprise repository."""
    svc = BankAccountService()
    try:
        item = svc.create_bankaccount(
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

@router.put("/bankaccounts/{item_id}", response_model=Dict[str, Any])
def update_bankaccount(item_id: int, payload: BankAccountUpdateSchema):
    """Update existing BankAccount record fields."""
    svc = BankAccountService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bankaccount(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BankAccount with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bankaccounts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bankaccount(item_id: int, hard: bool = Query(False)):
    """Delete BankAccount record (soft-delete by default)."""
    svc = BankAccountService()
    ok = svc.delete_bankaccount(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BankAccount with ID {item_id} not found")
    return None

@router.get("/bankaccounts/analytics/metrics", response_model=Dict[str, Any])
def get_bankaccount_metrics():
    """Calculate summary statistical KPIs for BankAccount collection."""
    svc = BankAccountService()
    return svc.calculate_aggregate_metrics()

# ==================== CashFlowForecast Endpoints ====================
@router.get("/cashflowforecasts", response_model=List[Dict[str, Any]])
def list_cashflowforecasts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CashFlowForecast records with pagination and filtering."""
    svc = CashFlowForecastService()
    items = svc.list_cashflowforecasts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/cashflowforecasts/{item_id}", response_model=Dict[str, Any])
def get_cashflowforecast_by_id(item_id: int):
    """Retrieve detailed record for CashFlowForecast by ID."""
    svc = CashFlowForecastService()
    item = svc.get_cashflowforecast_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CashFlowForecast with ID {item_id} not found")
    return item.to_dict()

@router.post("/cashflowforecasts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_cashflowforecast(payload: CashFlowForecastCreateSchema):
    """Create new CashFlowForecast instance in enterprise repository."""
    svc = CashFlowForecastService()
    try:
        item = svc.create_cashflowforecast(
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

@router.put("/cashflowforecasts/{item_id}", response_model=Dict[str, Any])
def update_cashflowforecast(item_id: int, payload: CashFlowForecastUpdateSchema):
    """Update existing CashFlowForecast record fields."""
    svc = CashFlowForecastService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_cashflowforecast(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CashFlowForecast with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/cashflowforecasts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cashflowforecast(item_id: int, hard: bool = Query(False)):
    """Delete CashFlowForecast record (soft-delete by default)."""
    svc = CashFlowForecastService()
    ok = svc.delete_cashflowforecast(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CashFlowForecast with ID {item_id} not found")
    return None

@router.get("/cashflowforecasts/analytics/metrics", response_model=Dict[str, Any])
def get_cashflowforecast_metrics():
    """Calculate summary statistical KPIs for CashFlowForecast collection."""
    svc = CashFlowForecastService()
    return svc.calculate_aggregate_metrics()

# ==================== ExchangeContract Endpoints ====================
@router.get("/exchangecontracts", response_model=List[Dict[str, Any]])
def list_exchangecontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExchangeContract records with pagination and filtering."""
    svc = ExchangeContractService()
    items = svc.list_exchangecontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/exchangecontracts/{item_id}", response_model=Dict[str, Any])
def get_exchangecontract_by_id(item_id: int):
    """Retrieve detailed record for ExchangeContract by ID."""
    svc = ExchangeContractService()
    item = svc.get_exchangecontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExchangeContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/exchangecontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_exchangecontract(payload: ExchangeContractCreateSchema):
    """Create new ExchangeContract instance in enterprise repository."""
    svc = ExchangeContractService()
    try:
        item = svc.create_exchangecontract(
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

@router.put("/exchangecontracts/{item_id}", response_model=Dict[str, Any])
def update_exchangecontract(item_id: int, payload: ExchangeContractUpdateSchema):
    """Update existing ExchangeContract record fields."""
    svc = ExchangeContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_exchangecontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExchangeContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/exchangecontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exchangecontract(item_id: int, hard: bool = Query(False)):
    """Delete ExchangeContract record (soft-delete by default)."""
    svc = ExchangeContractService()
    ok = svc.delete_exchangecontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExchangeContract with ID {item_id} not found")
    return None

@router.get("/exchangecontracts/analytics/metrics", response_model=Dict[str, Any])
def get_exchangecontract_metrics():
    """Calculate summary statistical KPIs for ExchangeContract collection."""
    svc = ExchangeContractService()
    return svc.calculate_aggregate_metrics()

# ==================== LetterOfCredit Endpoints ====================
@router.get("/letterofcredits", response_model=List[Dict[str, Any]])
def list_letterofcredits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LetterOfCredit records with pagination and filtering."""
    svc = LetterOfCreditService()
    items = svc.list_letterofcredits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/letterofcredits/{item_id}", response_model=Dict[str, Any])
def get_letterofcredit_by_id(item_id: int):
    """Retrieve detailed record for LetterOfCredit by ID."""
    svc = LetterOfCreditService()
    item = svc.get_letterofcredit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LetterOfCredit with ID {item_id} not found")
    return item.to_dict()

@router.post("/letterofcredits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_letterofcredit(payload: LetterOfCreditCreateSchema):
    """Create new LetterOfCredit instance in enterprise repository."""
    svc = LetterOfCreditService()
    try:
        item = svc.create_letterofcredit(
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

@router.put("/letterofcredits/{item_id}", response_model=Dict[str, Any])
def update_letterofcredit(item_id: int, payload: LetterOfCreditUpdateSchema):
    """Update existing LetterOfCredit record fields."""
    svc = LetterOfCreditService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_letterofcredit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LetterOfCredit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/letterofcredits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_letterofcredit(item_id: int, hard: bool = Query(False)):
    """Delete LetterOfCredit record (soft-delete by default)."""
    svc = LetterOfCreditService()
    ok = svc.delete_letterofcredit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LetterOfCredit with ID {item_id} not found")
    return None

@router.get("/letterofcredits/analytics/metrics", response_model=Dict[str, Any])
def get_letterofcredit_metrics():
    """Calculate summary statistical KPIs for LetterOfCredit collection."""
    svc = LetterOfCreditService()
    return svc.calculate_aggregate_metrics()

# ==================== BankGuarantee Endpoints ====================
@router.get("/bankguarantees", response_model=List[Dict[str, Any]])
def list_bankguarantees(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BankGuarantee records with pagination and filtering."""
    svc = BankGuaranteeService()
    items = svc.list_bankguarantees(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/bankguarantees/{item_id}", response_model=Dict[str, Any])
def get_bankguarantee_by_id(item_id: int):
    """Retrieve detailed record for BankGuarantee by ID."""
    svc = BankGuaranteeService()
    item = svc.get_bankguarantee_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BankGuarantee with ID {item_id} not found")
    return item.to_dict()

@router.post("/bankguarantees", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_bankguarantee(payload: BankGuaranteeCreateSchema):
    """Create new BankGuarantee instance in enterprise repository."""
    svc = BankGuaranteeService()
    try:
        item = svc.create_bankguarantee(
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

@router.put("/bankguarantees/{item_id}", response_model=Dict[str, Any])
def update_bankguarantee(item_id: int, payload: BankGuaranteeUpdateSchema):
    """Update existing BankGuarantee record fields."""
    svc = BankGuaranteeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_bankguarantee(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BankGuarantee with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/bankguarantees/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bankguarantee(item_id: int, hard: bool = Query(False)):
    """Delete BankGuarantee record (soft-delete by default)."""
    svc = BankGuaranteeService()
    ok = svc.delete_bankguarantee(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BankGuarantee with ID {item_id} not found")
    return None

@router.get("/bankguarantees/analytics/metrics", response_model=Dict[str, Any])
def get_bankguarantee_metrics():
    """Calculate summary statistical KPIs for BankGuarantee collection."""
    svc = BankGuaranteeService()
    return svc.calculate_aggregate_metrics()

# ==================== InvestmentSecurity Endpoints ====================
@router.get("/investmentsecuritys", response_model=List[Dict[str, Any]])
def list_investmentsecuritys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InvestmentSecurity records with pagination and filtering."""
    svc = InvestmentSecurityService()
    items = svc.list_investmentsecuritys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/investmentsecuritys/{item_id}", response_model=Dict[str, Any])
def get_investmentsecurity_by_id(item_id: int):
    """Retrieve detailed record for InvestmentSecurity by ID."""
    svc = InvestmentSecurityService()
    item = svc.get_investmentsecurity_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InvestmentSecurity with ID {item_id} not found")
    return item.to_dict()

@router.post("/investmentsecuritys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_investmentsecurity(payload: InvestmentSecurityCreateSchema):
    """Create new InvestmentSecurity instance in enterprise repository."""
    svc = InvestmentSecurityService()
    try:
        item = svc.create_investmentsecurity(
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

@router.put("/investmentsecuritys/{item_id}", response_model=Dict[str, Any])
def update_investmentsecurity(item_id: int, payload: InvestmentSecurityUpdateSchema):
    """Update existing InvestmentSecurity record fields."""
    svc = InvestmentSecurityService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_investmentsecurity(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InvestmentSecurity with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/investmentsecuritys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_investmentsecurity(item_id: int, hard: bool = Query(False)):
    """Delete InvestmentSecurity record (soft-delete by default)."""
    svc = InvestmentSecurityService()
    ok = svc.delete_investmentsecurity(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InvestmentSecurity with ID {item_id} not found")
    return None

@router.get("/investmentsecuritys/analytics/metrics", response_model=Dict[str, Any])
def get_investmentsecurity_metrics():
    """Calculate summary statistical KPIs for InvestmentSecurity collection."""
    svc = InvestmentSecurityService()
    return svc.calculate_aggregate_metrics()

# ==================== LoanFacility Endpoints ====================
@router.get("/loanfacilitys", response_model=List[Dict[str, Any]])
def list_loanfacilitys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LoanFacility records with pagination and filtering."""
    svc = LoanFacilityService()
    items = svc.list_loanfacilitys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/loanfacilitys/{item_id}", response_model=Dict[str, Any])
def get_loanfacility_by_id(item_id: int):
    """Retrieve detailed record for LoanFacility by ID."""
    svc = LoanFacilityService()
    item = svc.get_loanfacility_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LoanFacility with ID {item_id} not found")
    return item.to_dict()

@router.post("/loanfacilitys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_loanfacility(payload: LoanFacilityCreateSchema):
    """Create new LoanFacility instance in enterprise repository."""
    svc = LoanFacilityService()
    try:
        item = svc.create_loanfacility(
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

@router.put("/loanfacilitys/{item_id}", response_model=Dict[str, Any])
def update_loanfacility(item_id: int, payload: LoanFacilityUpdateSchema):
    """Update existing LoanFacility record fields."""
    svc = LoanFacilityService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_loanfacility(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LoanFacility with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/loanfacilitys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loanfacility(item_id: int, hard: bool = Query(False)):
    """Delete LoanFacility record (soft-delete by default)."""
    svc = LoanFacilityService()
    ok = svc.delete_loanfacility(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LoanFacility with ID {item_id} not found")
    return None

@router.get("/loanfacilitys/analytics/metrics", response_model=Dict[str, Any])
def get_loanfacility_metrics():
    """Calculate summary statistical KPIs for LoanFacility collection."""
    svc = LoanFacilityService()
    return svc.calculate_aggregate_metrics()

# ==================== InterestAccrual Endpoints ====================
@router.get("/interestaccruals", response_model=List[Dict[str, Any]])
def list_interestaccruals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InterestAccrual records with pagination and filtering."""
    svc = InterestAccrualService()
    items = svc.list_interestaccruals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/interestaccruals/{item_id}", response_model=Dict[str, Any])
def get_interestaccrual_by_id(item_id: int):
    """Retrieve detailed record for InterestAccrual by ID."""
    svc = InterestAccrualService()
    item = svc.get_interestaccrual_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InterestAccrual with ID {item_id} not found")
    return item.to_dict()

@router.post("/interestaccruals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_interestaccrual(payload: InterestAccrualCreateSchema):
    """Create new InterestAccrual instance in enterprise repository."""
    svc = InterestAccrualService()
    try:
        item = svc.create_interestaccrual(
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

@router.put("/interestaccruals/{item_id}", response_model=Dict[str, Any])
def update_interestaccrual(item_id: int, payload: InterestAccrualUpdateSchema):
    """Update existing InterestAccrual record fields."""
    svc = InterestAccrualService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_interestaccrual(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InterestAccrual with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/interestaccruals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_interestaccrual(item_id: int, hard: bool = Query(False)):
    """Delete InterestAccrual record (soft-delete by default)."""
    svc = InterestAccrualService()
    ok = svc.delete_interestaccrual(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InterestAccrual with ID {item_id} not found")
    return None

@router.get("/interestaccruals/analytics/metrics", response_model=Dict[str, Any])
def get_interestaccrual_metrics():
    """Calculate summary statistical KPIs for InterestAccrual collection."""
    svc = InterestAccrualService()
    return svc.calculate_aggregate_metrics()

# ==================== LiquidityPool Endpoints ====================
@router.get("/liquiditypools", response_model=List[Dict[str, Any]])
def list_liquiditypools(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LiquidityPool records with pagination and filtering."""
    svc = LiquidityPoolService()
    items = svc.list_liquiditypools(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/liquiditypools/{item_id}", response_model=Dict[str, Any])
def get_liquiditypool_by_id(item_id: int):
    """Retrieve detailed record for LiquidityPool by ID."""
    svc = LiquidityPoolService()
    item = svc.get_liquiditypool_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LiquidityPool with ID {item_id} not found")
    return item.to_dict()

@router.post("/liquiditypools", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_liquiditypool(payload: LiquidityPoolCreateSchema):
    """Create new LiquidityPool instance in enterprise repository."""
    svc = LiquidityPoolService()
    try:
        item = svc.create_liquiditypool(
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

@router.put("/liquiditypools/{item_id}", response_model=Dict[str, Any])
def update_liquiditypool(item_id: int, payload: LiquidityPoolUpdateSchema):
    """Update existing LiquidityPool record fields."""
    svc = LiquidityPoolService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_liquiditypool(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LiquidityPool with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/liquiditypools/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_liquiditypool(item_id: int, hard: bool = Query(False)):
    """Delete LiquidityPool record (soft-delete by default)."""
    svc = LiquidityPoolService()
    ok = svc.delete_liquiditypool(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LiquidityPool with ID {item_id} not found")
    return None

@router.get("/liquiditypools/analytics/metrics", response_model=Dict[str, Any])
def get_liquiditypool_metrics():
    """Calculate summary statistical KPIs for LiquidityPool collection."""
    svc = LiquidityPoolService()
    return svc.calculate_aggregate_metrics()

# ==================== TreasuryDeal Endpoints ====================
@router.get("/treasurydeals", response_model=List[Dict[str, Any]])
def list_treasurydeals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TreasuryDeal records with pagination and filtering."""
    svc = TreasuryDealService()
    items = svc.list_treasurydeals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/treasurydeals/{item_id}", response_model=Dict[str, Any])
def get_treasurydeal_by_id(item_id: int):
    """Retrieve detailed record for TreasuryDeal by ID."""
    svc = TreasuryDealService()
    item = svc.get_treasurydeal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TreasuryDeal with ID {item_id} not found")
    return item.to_dict()

@router.post("/treasurydeals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_treasurydeal(payload: TreasuryDealCreateSchema):
    """Create new TreasuryDeal instance in enterprise repository."""
    svc = TreasuryDealService()
    try:
        item = svc.create_treasurydeal(
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

@router.put("/treasurydeals/{item_id}", response_model=Dict[str, Any])
def update_treasurydeal(item_id: int, payload: TreasuryDealUpdateSchema):
    """Update existing TreasuryDeal record fields."""
    svc = TreasuryDealService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_treasurydeal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TreasuryDeal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/treasurydeals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_treasurydeal(item_id: int, hard: bool = Query(False)):
    """Delete TreasuryDeal record (soft-delete by default)."""
    svc = TreasuryDealService()
    ok = svc.delete_treasurydeal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TreasuryDeal with ID {item_id} not found")
    return None

@router.get("/treasurydeals/analytics/metrics", response_model=Dict[str, Any])
def get_treasurydeal_metrics():
    """Calculate summary statistical KPIs for TreasuryDeal collection."""
    svc = TreasuryDealService()
    return svc.calculate_aggregate_metrics()

# ==================== HedgingContract Endpoints ====================
@router.get("/hedgingcontracts", response_model=List[Dict[str, Any]])
def list_hedgingcontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List HedgingContract records with pagination and filtering."""
    svc = HedgingContractService()
    items = svc.list_hedgingcontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/hedgingcontracts/{item_id}", response_model=Dict[str, Any])
def get_hedgingcontract_by_id(item_id: int):
    """Retrieve detailed record for HedgingContract by ID."""
    svc = HedgingContractService()
    item = svc.get_hedgingcontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"HedgingContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/hedgingcontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_hedgingcontract(payload: HedgingContractCreateSchema):
    """Create new HedgingContract instance in enterprise repository."""
    svc = HedgingContractService()
    try:
        item = svc.create_hedgingcontract(
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

@router.put("/hedgingcontracts/{item_id}", response_model=Dict[str, Any])
def update_hedgingcontract(item_id: int, payload: HedgingContractUpdateSchema):
    """Update existing HedgingContract record fields."""
    svc = HedgingContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_hedgingcontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"HedgingContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/hedgingcontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hedgingcontract(item_id: int, hard: bool = Query(False)):
    """Delete HedgingContract record (soft-delete by default)."""
    svc = HedgingContractService()
    ok = svc.delete_hedgingcontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"HedgingContract with ID {item_id} not found")
    return None

@router.get("/hedgingcontracts/analytics/metrics", response_model=Dict[str, Any])
def get_hedgingcontract_metrics():
    """Calculate summary statistical KPIs for HedgingContract collection."""
    svc = HedgingContractService()
    return svc.calculate_aggregate_metrics()

# ==================== SweepRule Endpoints ====================
@router.get("/sweeprules", response_model=List[Dict[str, Any]])
def list_sweeprules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SweepRule records with pagination and filtering."""
    svc = SweepRuleService()
    items = svc.list_sweeprules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/sweeprules/{item_id}", response_model=Dict[str, Any])
def get_sweeprule_by_id(item_id: int):
    """Retrieve detailed record for SweepRule by ID."""
    svc = SweepRuleService()
    item = svc.get_sweeprule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SweepRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/sweeprules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_sweeprule(payload: SweepRuleCreateSchema):
    """Create new SweepRule instance in enterprise repository."""
    svc = SweepRuleService()
    try:
        item = svc.create_sweeprule(
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

@router.put("/sweeprules/{item_id}", response_model=Dict[str, Any])
def update_sweeprule(item_id: int, payload: SweepRuleUpdateSchema):
    """Update existing SweepRule record fields."""
    svc = SweepRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_sweeprule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SweepRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/sweeprules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sweeprule(item_id: int, hard: bool = Query(False)):
    """Delete SweepRule record (soft-delete by default)."""
    svc = SweepRuleService()
    ok = svc.delete_sweeprule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SweepRule with ID {item_id} not found")
    return None

@router.get("/sweeprules/analytics/metrics", response_model=Dict[str, Any])
def get_sweeprule_metrics():
    """Calculate summary statistical KPIs for SweepRule collection."""
    svc = SweepRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== CounterpartyLimit Endpoints ====================
@router.get("/counterpartylimits", response_model=List[Dict[str, Any]])
def list_counterpartylimits(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CounterpartyLimit records with pagination and filtering."""
    svc = CounterpartyLimitService()
    items = svc.list_counterpartylimits(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/counterpartylimits/{item_id}", response_model=Dict[str, Any])
def get_counterpartylimit_by_id(item_id: int):
    """Retrieve detailed record for CounterpartyLimit by ID."""
    svc = CounterpartyLimitService()
    item = svc.get_counterpartylimit_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CounterpartyLimit with ID {item_id} not found")
    return item.to_dict()

@router.post("/counterpartylimits", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_counterpartylimit(payload: CounterpartyLimitCreateSchema):
    """Create new CounterpartyLimit instance in enterprise repository."""
    svc = CounterpartyLimitService()
    try:
        item = svc.create_counterpartylimit(
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

@router.put("/counterpartylimits/{item_id}", response_model=Dict[str, Any])
def update_counterpartylimit(item_id: int, payload: CounterpartyLimitUpdateSchema):
    """Update existing CounterpartyLimit record fields."""
    svc = CounterpartyLimitService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_counterpartylimit(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CounterpartyLimit with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/counterpartylimits/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_counterpartylimit(item_id: int, hard: bool = Query(False)):
    """Delete CounterpartyLimit record (soft-delete by default)."""
    svc = CounterpartyLimitService()
    ok = svc.delete_counterpartylimit(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CounterpartyLimit with ID {item_id} not found")
    return None

@router.get("/counterpartylimits/analytics/metrics", response_model=Dict[str, Any])
def get_counterpartylimit_metrics():
    """Calculate summary statistical KPIs for CounterpartyLimit collection."""
    svc = CounterpartyLimitService()
    return svc.calculate_aggregate_metrics()

# ==================== DividendRecord Endpoints ====================
@router.get("/dividendrecords", response_model=List[Dict[str, Any]])
def list_dividendrecords(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DividendRecord records with pagination and filtering."""
    svc = DividendRecordService()
    items = svc.list_dividendrecords(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dividendrecords/{item_id}", response_model=Dict[str, Any])
def get_dividendrecord_by_id(item_id: int):
    """Retrieve detailed record for DividendRecord by ID."""
    svc = DividendRecordService()
    item = svc.get_dividendrecord_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DividendRecord with ID {item_id} not found")
    return item.to_dict()

@router.post("/dividendrecords", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dividendrecord(payload: DividendRecordCreateSchema):
    """Create new DividendRecord instance in enterprise repository."""
    svc = DividendRecordService()
    try:
        item = svc.create_dividendrecord(
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

@router.put("/dividendrecords/{item_id}", response_model=Dict[str, Any])
def update_dividendrecord(item_id: int, payload: DividendRecordUpdateSchema):
    """Update existing DividendRecord record fields."""
    svc = DividendRecordService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dividendrecord(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DividendRecord with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dividendrecords/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dividendrecord(item_id: int, hard: bool = Query(False)):
    """Delete DividendRecord record (soft-delete by default)."""
    svc = DividendRecordService()
    ok = svc.delete_dividendrecord(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DividendRecord with ID {item_id} not found")
    return None

@router.get("/dividendrecords/analytics/metrics", response_model=Dict[str, Any])
def get_dividendrecord_metrics():
    """Calculate summary statistical KPIs for DividendRecord collection."""
    svc = DividendRecordService()
    return svc.calculate_aggregate_metrics()

# ==================== LeaseContract Endpoints ====================
@router.get("/leasecontracts", response_model=List[Dict[str, Any]])
def list_leasecontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeaseContract records with pagination and filtering."""
    svc = LeaseContractService()
    items = svc.list_leasecontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leasecontracts/{item_id}", response_model=Dict[str, Any])
def get_leasecontract_by_id(item_id: int):
    """Retrieve detailed record for LeaseContract by ID."""
    svc = LeaseContractService()
    item = svc.get_leasecontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeaseContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/leasecontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leasecontract(payload: LeaseContractCreateSchema):
    """Create new LeaseContract instance in enterprise repository."""
    svc = LeaseContractService()
    try:
        item = svc.create_leasecontract(
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

@router.put("/leasecontracts/{item_id}", response_model=Dict[str, Any])
def update_leasecontract(item_id: int, payload: LeaseContractUpdateSchema):
    """Update existing LeaseContract record fields."""
    svc = LeaseContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leasecontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeaseContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leasecontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leasecontract(item_id: int, hard: bool = Query(False)):
    """Delete LeaseContract record (soft-delete by default)."""
    svc = LeaseContractService()
    ok = svc.delete_leasecontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeaseContract with ID {item_id} not found")
    return None

@router.get("/leasecontracts/analytics/metrics", response_model=Dict[str, Any])
def get_leasecontract_metrics():
    """Calculate summary statistical KPIs for LeaseContract collection."""
    svc = LeaseContractService()
    return svc.calculate_aggregate_metrics()

# ==================== FinancialRatio Endpoints ====================
@router.get("/financialratios", response_model=List[Dict[str, Any]])
def list_financialratios(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List FinancialRatio records with pagination and filtering."""
    svc = FinancialRatioService()
    items = svc.list_financialratios(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/financialratios/{item_id}", response_model=Dict[str, Any])
def get_financialratio_by_id(item_id: int):
    """Retrieve detailed record for FinancialRatio by ID."""
    svc = FinancialRatioService()
    item = svc.get_financialratio_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"FinancialRatio with ID {item_id} not found")
    return item.to_dict()

@router.post("/financialratios", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_financialratio(payload: FinancialRatioCreateSchema):
    """Create new FinancialRatio instance in enterprise repository."""
    svc = FinancialRatioService()
    try:
        item = svc.create_financialratio(
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

@router.put("/financialratios/{item_id}", response_model=Dict[str, Any])
def update_financialratio(item_id: int, payload: FinancialRatioUpdateSchema):
    """Update existing FinancialRatio record fields."""
    svc = FinancialRatioService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_financialratio(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"FinancialRatio with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/financialratios/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_financialratio(item_id: int, hard: bool = Query(False)):
    """Delete FinancialRatio record (soft-delete by default)."""
    svc = FinancialRatioService()
    ok = svc.delete_financialratio(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"FinancialRatio with ID {item_id} not found")
    return None

@router.get("/financialratios/analytics/metrics", response_model=Dict[str, Any])
def get_financialratio_metrics():
    """Calculate summary statistical KPIs for FinancialRatio collection."""
    svc = FinancialRatioService()
    return svc.calculate_aggregate_metrics()

