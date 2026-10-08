from typing import Optional, Union
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    name: str
    company_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    industry: Optional[str] = None
    customer_type: Optional[str] = "ENTERPRISE"
    status: Optional[str] = "ACTIVE"
    address: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = "India"
    tax_id: Optional[str] = None
    annual_revenue: Optional[Union[float, int]] = 0.0
    credit_limit: Optional[Union[float, int]] = 0.0
    notes: Optional[str] = None
    assigned_to_id: Optional[int] = None


class CustomerCreate(CustomerBase):
    customer_code: Optional[str] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    company_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    industry: Optional[str] = None
    customer_type: Optional[str] = None
    status: Optional[str] = None
    address: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    tax_id: Optional[str] = None
    annual_revenue: Optional[Union[float, int]] = None
    credit_limit: Optional[Union[float, int]] = None
    notes: Optional[str] = None
    assigned_to_id: Optional[int] = None


class CustomerOut(CustomerBase):
    id: int
    customer_code: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
