from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    phone = Column(String(50), nullable=True)
    company = Column(String(150), nullable=True)
    title = Column(String(100), nullable=True)
    lead_source = Column(String(50), default="WEBSITE", nullable=False)
    lead_status = Column(String(50), default="NEW", nullable=False)  # NEW, CONTACTED, QUALIFIED, PROPOSAL_SENT, NEGOTIATION, WON, LOST
    lead_score = Column(Integer, default=50, nullable=False)
    estimated_value = Column(Numeric(15, 2), default=0.00, nullable=False)
    notes = Column(Text, nullable=True)
    assigned_to_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    converted_customer_id = Column(Integer, ForeignKey("customers.id", ondelete="SET NULL"), nullable=True)
    converted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])
    converted_customer = relationship("Customer", foreign_keys=[converted_customer_id])
    interactions = relationship("CustomerInteraction", back_populates="lead", cascade="all, delete-orphan")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()


class CustomerInteraction(Base):
    __tablename__ = "customer_history"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id", ondelete="CASCADE"), nullable=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    interaction_type = Column(String(50), nullable=False)  # CALL, EMAIL, MEETING, NOTE, TASK, DEAL_UPDATE
    title = Column(String(200), nullable=False)
    notes = Column(Text, nullable=True)
    outcome = Column(String(100), nullable=True)  # COMPLETED, PENDING, FOLLOW_UP_REQUIRED, NO_ANSWER
    interaction_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    next_follow_up = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    customer = relationship("Customer", back_populates="interactions")
    lead = relationship("Lead", back_populates="interactions")
    user = relationship("User", foreign_keys=[user_id])
