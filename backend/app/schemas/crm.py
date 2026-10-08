from typing import Optional, List, Dict, Any, Union
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.schemas.customer import CustomerOut


class LeadBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    title: Optional[str] = None
    lead_source: Optional[str] = "WEBSITE"
    lead_status: Optional[str] = "NEW"
    lead_score: Optional[int] = 50
    estimated_value: Optional[Union[float, int]] = 0.0
    notes: Optional[str] = None
    assigned_to_id: Optional[int] = None


class LeadCreate(LeadBase):
    pass


class LeadUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    title: Optional[str] = None
    lead_source: Optional[str] = None
    lead_status: Optional[str] = None
    lead_score: Optional[int] = None
    estimated_value: Optional[Union[float, int]] = None
    notes: Optional[str] = None
    assigned_to_id: Optional[int] = None


class LeadOut(LeadBase):
    id: int
    converted_customer_id: Optional[int] = None
    converted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class LeadConvertRequest(BaseModel):
    customer_type: Optional[str] = "ENTERPRISE"
    industry: Optional[str] = None
    annual_revenue: Optional[Union[float, int]] = None
    credit_limit: Optional[Union[float, int]] = None


class InteractionCreate(BaseModel):
    customer_id: Optional[int] = None
    lead_id: Optional[int] = None
    interaction_type: str = "CALL"  # CALL, EMAIL, MEETING, NOTE, TASK, DEAL_UPDATE
    title: str
    notes: Optional[str] = None
    outcome: Optional[str] = "COMPLETED"
    interaction_date: Optional[datetime] = None
    next_follow_up: Optional[datetime] = None


class InteractionOut(BaseModel):
    id: int
    customer_id: Optional[int] = None
    lead_id: Optional[int] = None
    user_id: Optional[int] = None
    interaction_type: str
    title: str
    notes: Optional[str] = None
    outcome: Optional[str] = None
    interaction_date: Optional[datetime] = None
    next_follow_up: Optional[datetime] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class CRMOverviewStats(BaseModel):
    customers: Dict[str, Any]
    leads: Dict[str, Any]
    pipeline_value: float = 0.0
    win_rate: float = 0.0
