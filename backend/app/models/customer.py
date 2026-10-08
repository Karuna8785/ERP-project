from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_code = Column(String(50), unique=True, index=True, nullable=True)
    name = Column(String(150), nullable=False, index=True)
    company_name = Column(String(150), nullable=True)
    email = Column(String(255), nullable=True, index=True)
    phone = Column(String(50), nullable=True)
    website = Column(String(255), nullable=True)
    industry = Column(String(100), nullable=True)
    customer_type = Column(String(50), default="ENTERPRISE", nullable=True)
    status = Column(String(50), default="ACTIVE", nullable=True)
    
    address = Column(Text, nullable=True)
    address_line1 = Column(String(255), nullable=True)
    address_line2 = Column(String(255), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    postal_code = Column(String(20), nullable=True)
    country = Column(String(100), default="India")
    tax_id = Column(String(50), nullable=True)  # GSTIN or VAT number
    
    annual_revenue = Column(Numeric(15, 2), default=0.00, nullable=True)
    credit_limit = Column(Numeric(15, 2), default=0.00, nullable=True)
    notes = Column(Text, nullable=True)
    assigned_to_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    quotations = relationship("Quotation", back_populates="customer")
    sales_orders = relationship("SalesOrder", back_populates="customer")
    invoices = relationship("Invoice", back_populates="customer")
    interactions = relationship("CustomerInteraction", back_populates="customer", cascade="all, delete-orphan")
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])
