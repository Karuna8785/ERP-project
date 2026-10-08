from typing import Optional, List, Union
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SupplierBase(BaseModel):
    name: str
    contact_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = "India"
    tax_id: Optional[str] = None
    payment_terms: Optional[str] = "Net 30"
    is_active: Optional[bool] = True


class SupplierCreate(SupplierBase):
    supplier_code: Optional[str] = None


class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    contact_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    tax_id: Optional[str] = None
    payment_terms: Optional[str] = None
    is_active: Optional[bool] = None


class SupplierOut(SupplierBase):
    id: int
    supplier_code: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class PurchaseOrderItemBase(BaseModel):
    product_id: Optional[int] = None
    product_name: str
    quantity: float = 1.0
    unit_cost: float = 0.0


class PurchaseOrderItemCreate(PurchaseOrderItemBase):
    pass


class PurchaseOrderItemOut(PurchaseOrderItemBase):
    id: int
    purchase_order_id: int
    received_quantity: float = 0.0
    total_amount: float = 0.0

    model_config = ConfigDict(from_attributes=True)


class PurchaseOrderCreate(BaseModel):
    supplier_id: int
    order_date: Optional[datetime] = None
    expected_date: Optional[datetime] = None
    shipping_cost: Optional[float] = 0.0
    notes: Optional[str] = None
    items: List[PurchaseOrderItemCreate] = []


class PurchaseOrderUpdateStatus(BaseModel):
    status: str  # Draft, Approved, Ordered, Received, Cancelled


class PurchaseOrderReceiveGoods(BaseModel):
    warehouse_id: Optional[int] = None
    items_received: List[dict] = []  # [{item_id: int, quantity: float}]


class PurchaseOrderOut(BaseModel):
    id: int
    po_number: str
    supplier_id: int
    supplier_name: Optional[str] = None
    order_date: Optional[datetime] = None
    expected_date: Optional[datetime] = None
    status: str
    subtotal: float
    tax_amount: float
    shipping_cost: float
    total_amount: float
    payment_status: str
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    items: List[PurchaseOrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)


class ExpenseCreate(BaseModel):
    title: str
    category: str
    amount: float
    date: Optional[datetime] = None
    payment_method: Optional[str] = "Bank Transfer"
    reference_no: Optional[str] = None
    notes: Optional[str] = None


class ExpenseOut(BaseModel):
    id: int
    title: str
    category: str
    amount: float
    date: Optional[datetime] = None
    payment_method: str
    reference_no: Optional[str] = None
    status: str
    notes: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
