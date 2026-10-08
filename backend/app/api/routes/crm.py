from typing import List, Optional
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from app.database.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.customer import Customer
from app.models.crm import Lead, CustomerInteraction
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerOut
from app.schemas.crm import (
    LeadCreate,
    LeadUpdate,
    LeadOut,
    LeadConvertRequest,
    InteractionCreate,
    InteractionOut,
    CRMOverviewStats,
)

router = APIRouter(prefix="/crm", tags=["Customer Relationship Management"])


# ============================================================================
# OVERVIEW & ANALYTICS
# ============================================================================

@router.get("/overview", response_model=CRMOverviewStats)
def get_crm_overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve high-level CRM performance KPIs, pipeline volume, and stage distributions."""
    total_customers = db.query(Customer).count()
    active_customers = db.query(Customer).filter(Customer.status == "ACTIVE").count()
    enterprise_customers = db.query(Customer).filter(Customer.customer_type == "ENTERPRISE").count()

    total_leads = db.query(Lead).count()
    open_leads = db.query(Lead).filter(~Lead.lead_status.in_(["WON", "LOST"])).count()
    won_leads = db.query(Lead).filter(Lead.lead_status == "WON").count()
    lost_leads = db.query(Lead).filter(Lead.lead_status == "LOST").count()

    pipeline_sum = db.query(func.sum(Lead.estimated_value)).filter(~Lead.lead_status.in_(["LOST"])).scalar() or 0.0
    win_rate = (won_leads / (won_leads + lost_leads) * 100.0) if (won_leads + lost_leads) > 0 else 25.0

    return {
        "customers": {
            "total_customers": total_customers,
            "active_customers": active_customers,
            "enterprise_customers": enterprise_customers,
        },
        "leads": {
            "total_leads": total_leads,
            "open_leads": open_leads,
            "won_leads": won_leads,
            "lost_leads": lost_leads,
        },
        "pipeline_value": float(pipeline_sum),
        "win_rate": round(win_rate, 1),
    }


# ============================================================================
# CUSTOMERS
# ============================================================================

@router.get("/customers", response_model=List[CustomerOut])
def list_customers(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    customer_type: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Search and filter enterprise customer accounts."""
    query = db.query(Customer)
    if search:
        s = f"%{search}%"
        query = query.filter(
            or_(
                Customer.name.ilike(s),
                Customer.company_name.ilike(s),
                Customer.email.ilike(s),
                Customer.customer_code.ilike(s),
                Customer.city.ilike(s),
            )
        )
    if status:
        query = query.filter(Customer.status == status)
    if customer_type:
        query = query.filter(Customer.customer_type == customer_type)

    return query.order_by(Customer.id.desc()).offset(skip).limit(limit).all()


@router.post("/customers", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new customer account with auto-generated tracking code."""
    data = payload.model_dump(exclude_unset=True)
    customer = Customer(**data)
    db.add(customer)
    db.flush()

    if not customer.customer_code:
        customer.customer_code = f"CUST-{1000 + customer.id}"
    db.commit()
    db.refresh(customer)
    return customer


@router.get("/customers/{customer_id}", response_model=CustomerOut)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve full account record by customer ID."""
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.put("/customers/{customer_id}", response_model=CustomerOut)
def update_customer(
    customer_id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update existing customer details."""
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    for field, val in payload.model_dump(exclude_unset=True).items():
        setattr(customer, field, val)

    customer.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(customer)
    return customer


# ============================================================================
# LEADS & CONVERSION
# ============================================================================

@router.get("/leads", response_model=List[LeadOut])
def list_leads(
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List business leads across pipeline stages."""
    query = db.query(Lead)
    if search:
        s = f"%{search}%"
        query = query.filter(
            or_(
                Lead.first_name.ilike(s),
                Lead.last_name.ilike(s),
                Lead.email.ilike(s),
                Lead.company.ilike(s),
            )
        )
    if status:
        query = query.filter(Lead.lead_status == status)

    return query.order_by(Lead.id.desc()).offset(skip).limit(limit).all()


@router.post("/leads", response_model=LeadOut, status_code=status.HTTP_201_CREATED)
def create_lead(
    payload: LeadCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a prospective sales lead."""
    data = payload.model_dump()
    lead = Lead(**data)
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead


@router.get("/leads/{lead_id}", response_model=LeadOut)
def get_lead(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve lead profile."""
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@router.put("/leads/{lead_id}", response_model=LeadOut)
def update_lead(
    lead_id: int,
    payload: LeadUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update lead pipeline details and qualification scores."""
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    for field, val in payload.model_dump(exclude_unset=True).items():
        setattr(lead, field, val)

    lead.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(lead)
    return lead


@router.post("/leads/{lead_id}/convert", response_model=CustomerOut)
def convert_lead_to_customer(
    lead_id: int,
    payload: Optional[LeadConvertRequest] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """1-Click promote a qualified lead into an active customer account."""
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    customer_type = payload.customer_type if payload and payload.customer_type else "ENTERPRISE"
    industry = payload.industry if payload and payload.industry else (lead.company or "Commercial")
    annual_rev = payload.annual_revenue if payload and payload.annual_revenue is not None else float(lead.estimated_value)
    credit_lim = payload.credit_limit if payload and payload.credit_limit is not None else 50000.0

    customer = Customer(
        name=f"{lead.first_name} {lead.last_name}".strip(),
        company_name=lead.company or f"{lead.first_name}'s Enterprise",
        email=lead.email,
        phone=lead.phone,
        industry=industry,
        customer_type=customer_type,
        status="ACTIVE",
        annual_revenue=annual_rev,
        credit_limit=credit_lim,
        assigned_to_id=lead.assigned_to_id or current_user.id,
    )
    db.add(customer)
    db.flush()

    customer.customer_code = f"CUST-{1000 + customer.id}"

    # Update Lead record
    lead.converted_customer_id = customer.id
    lead.converted_at = datetime.now(timezone.utc)
    lead.lead_status = "WON"

    # Transfer lead interactions to customer
    db.query(CustomerInteraction).filter(CustomerInteraction.lead_id == lead.id).update(
        {CustomerInteraction.customer_id: customer.id}
    )

    db.commit()
    db.refresh(customer)
    return customer


# ============================================================================
# INTERACTIONS & TIMELINE
# ============================================================================

@router.post("/interactions", response_model=InteractionOut, status_code=status.HTTP_201_CREATED)
def log_interaction(
    payload: InteractionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Log an interaction touchpoint (Call, Email, Meeting, Note, Task)."""
    data = payload.model_dump()
    interaction = CustomerInteraction(**data)
    interaction.user_id = current_user.id
    if not interaction.interaction_date:
        interaction.interaction_date = datetime.now(timezone.utc)

    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction


@router.get("/customers/{customer_id}/timeline", response_model=List[InteractionOut])
def get_customer_timeline(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve chronological communication history for a specific customer."""
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return (
        db.query(CustomerInteraction)
        .filter(CustomerInteraction.customer_id == customer_id)
        .order_by(CustomerInteraction.interaction_date.desc(), CustomerInteraction.id.desc())
        .all()
    )
