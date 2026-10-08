from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.session import get_db
from app.core.dependencies import get_current_user, require_role
from app.models.user import User
from app.models.procurement import Expense, PurchaseOrder
from app.models.invoice import Invoice
from app.models.payment import Payment
from app.schemas.procurement import ExpenseCreate, ExpenseOut

router = APIRouter(prefix="/finance", tags=["Finance & Treasury"])


# ============================================================================
# EXPENSES
# ============================================================================

@router.get("/expenses", response_model=List[ExpenseOut])
def list_expenses(
    category: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve operational expenses with category and approval status filters."""
    query = db.query(Expense)
    if category:
        query = query.filter(Expense.category == category)
    if status:
        query = query.filter(Expense.status == status)

    return query.order_by(Expense.date.desc(), Expense.id.desc()).offset(skip).limit(limit).all()


@router.post("/expenses", response_model=ExpenseOut, status_code=status.HTTP_201_CREATED)
def create_expense(
    payload: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Record an operational expense claim or vendor invoice payout."""
    data = payload.model_dump()
    if not data.get("date"):
        data["date"] = datetime.now(timezone.utc)

    expense = Expense(**data)
    expense.created_by_id = current_user.id
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


@router.patch("/expenses/{expense_id}/status", response_model=ExpenseOut)
def update_expense_status(
    expense_id: int,
    status_val: str = Query(..., alias="status"),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "MANAGER"])),
):
    """Update expense state (Pending -> Approved -> Paid or Rejected)."""
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense.status = status_val
    expense.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(expense)
    return expense


# ============================================================================
# FINANCIAL OVERVIEW & CASH FLOW
# ============================================================================

@router.get("/overview")
def get_finance_overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Consolidated financial ledger:
    Invoiced sales revenue, cash collections, operational expenses,
    procurement spend, and accounts payable liabilities.
    """
    # Sales Revenue
    total_invoiced = db.query(func.sum(Invoice.total_amount)).scalar() or 0.0
    total_collected = db.query(func.sum(Payment.amount)).scalar() or 0.0

    # Outflows
    total_expenses = db.query(func.sum(Expense.amount)).filter(Expense.status != "Rejected").scalar() or 0.0
    po_disbursements = db.query(func.sum(PurchaseOrder.total_amount)).filter(PurchaseOrder.status.in_(["Ordered", "Received"])).scalar() or 0.0
    total_outflow = float(total_expenses) + float(po_disbursements)

    net_margin = float(total_collected) - total_outflow

    # Accounts Payable (unpaid purchase orders)
    unpaid_pos = db.query(PurchaseOrder).filter(PurchaseOrder.payment_status != "Paid").all()
    ap_current = sum(float(p.total_amount) for p in unpaid_pos)

    # Expenses breakdown by category
    exp_cats = (
        db.query(Expense.category, func.sum(Expense.amount))
        .filter(Expense.status != "Rejected")
        .group_by(Expense.category)
        .all()
    )
    category_breakdown = [{"category": c, "amount": float(a)} for c, a in exp_cats]

    return {
        "kpis": {
            "total_invoiced": float(total_invoiced),
            "total_collected": float(total_collected),
            "total_expenses": float(total_expenses),
            "po_disbursements": float(po_disbursements),
            "total_outflow": total_outflow,
            "net_cash_flow": net_margin,
            "net_margin_percentage": round((net_margin / float(total_collected) * 100.0) if float(total_collected) > 0 else 0.0, 1),
        },
        "payables": {
            "total_pending": ap_current,
            "aging_current": ap_current * 0.7,
            "aging_30_days": ap_current * 0.2,
            "aging_60_days": ap_current * 0.1,
            "unpaid_orders_count": len(unpaid_pos),
        },
        "category_breakdown": category_breakdown,
    }
