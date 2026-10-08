from typing import List, Optional
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database.session import get_db
from app.core.dependencies import get_current_user, require_role
from app.models.user import User
from app.models.procurement import Supplier, PurchaseOrder, PurchaseOrderItem
from app.models.product import Product
from app.models.warehouse import Warehouse
from app.models.inventory import WarehouseStock
from app.models.stock_movement import StockMovement
from app.schemas.procurement import (
    SupplierCreate,
    SupplierUpdate,
    SupplierOut,
    PurchaseOrderCreate,
    PurchaseOrderUpdateStatus,
    PurchaseOrderReceiveGoods,
    PurchaseOrderOut,
)

router = APIRouter(prefix="/procurement", tags=["Procurement & Supply Chain"])


# ============================================================================
# SUPPLIERS
# ============================================================================

@router.get("/suppliers", response_model=List[SupplierOut])
def list_suppliers(
    search: Optional[str] = Query(None),
    is_active: Optional[bool] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve suppliers directory with multi-field search."""
    query = db.query(Supplier)
    if search:
        s = f"%{search}%"
        query = query.filter(
            or_(
                Supplier.name.ilike(s),
                Supplier.supplier_code.ilike(s),
                Supplier.contact_name.ilike(s),
                Supplier.email.ilike(s),
                Supplier.city.ilike(s),
            )
        )
    if is_active is not None:
        query = query.filter(Supplier.is_active == is_active)

    return query.order_by(Supplier.id.desc()).offset(skip).limit(limit).all()


@router.post("/suppliers", response_model=SupplierOut, status_code=status.HTTP_201_CREATED)
def create_supplier(
    payload: SupplierCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Register a new vendor/supplier."""
    data = payload.model_dump(exclude_unset=True)
    supplier = Supplier(**data)
    if not supplier.supplier_code:
        count = db.query(Supplier).count()
        supplier.supplier_code = f"SUP-{1001 + count}"

    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier


@router.get("/suppliers/{supplier_id}", response_model=SupplierOut)
def get_supplier(
    supplier_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


@router.put("/suppliers/{supplier_id}", response_model=SupplierOut)
def update_supplier(
    supplier_id: int,
    payload: SupplierUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    for field, val in payload.model_dump(exclude_unset=True).items():
        setattr(supplier, field, val)

    supplier.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(supplier)
    return supplier


# ============================================================================
# PURCHASE ORDERS
# ============================================================================

@router.get("/purchase-orders", response_model=List[PurchaseOrderOut])
def list_purchase_orders(
    status: Optional[str] = Query(None),
    supplier_id: Optional[int] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List purchase orders with line items and status filters."""
    query = db.query(PurchaseOrder)
    if status:
        query = query.filter(PurchaseOrder.status == status)
    if supplier_id:
        query = query.filter(PurchaseOrder.supplier_id == supplier_id)

    orders = query.order_by(PurchaseOrder.id.desc()).offset(skip).limit(limit).all()
    # Attach supplier names
    for o in orders:
        if o.supplier:
            o.supplier_name = o.supplier.name
    return orders


@router.post("/purchase-orders", response_model=PurchaseOrderOut, status_code=status.HTTP_201_CREATED)
def create_purchase_order(
    payload: PurchaseOrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new commercial Purchase Order with line item calculations."""
    supplier = db.query(Supplier).filter(Supplier.id == payload.supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    now = datetime.now(timezone.utc)
    count_today = db.query(PurchaseOrder).count()
    po_number = f"PO-{now.year}-{1001 + count_today}"

    subtotal = 0.0
    order_items = []
    for item in payload.items:
        line_tot = float(item.quantity) * float(item.unit_cost)
        subtotal += line_tot
        order_items.append(
            PurchaseOrderItem(
                product_id=item.product_id,
                product_name=item.product_name,
                quantity=item.quantity,
                received_quantity=0.0,
                unit_cost=item.unit_cost,
                total_amount=line_tot,
            )
        )

    tax_amount = round(subtotal * 0.18, 2)
    shipping = float(payload.shipping_cost or 0.0)
    total_amount = round(subtotal + tax_amount + shipping, 2)

    po = PurchaseOrder(
        po_number=po_number,
        supplier_id=supplier.id,
        order_date=payload.order_date or now,
        expected_date=payload.expected_date,
        status="Draft",
        subtotal=subtotal,
        tax_amount=tax_amount,
        shipping_cost=shipping,
        total_amount=total_amount,
        payment_status="Unpaid",
        notes=payload.notes,
        created_by_id=current_user.id,
        items=order_items,
    )
    db.add(po)
    db.commit()
    db.refresh(po)
    po.supplier_name = supplier.name
    return po


@router.get("/purchase-orders/{po_id}", response_model=PurchaseOrderOut)
def get_purchase_order(
    po_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    po = db.query(PurchaseOrder).filter(PurchaseOrder.id == po_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    if po.supplier:
        po.supplier_name = po.supplier.name
    return po


@router.patch("/purchase-orders/{po_id}/status", response_model=PurchaseOrderOut)
def update_po_status(
    po_id: int,
    payload: PurchaseOrderUpdateStatus,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "MANAGER"])),
):
    po = db.query(PurchaseOrder).filter(PurchaseOrder.id == po_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="Purchase order not found")

    po.status = payload.status
    po.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(po)
    if po.supplier:
        po.supplier_name = po.supplier.name
    return po


@router.post("/purchase-orders/{po_id}/receive", response_model=PurchaseOrderOut)
def receive_goods(
    po_id: int,
    payload: PurchaseOrderReceiveGoods,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "MANAGER"])),
):
    """
    Goods Receipt: Intake delivered items, update received quantities, and
    automatically increment stock in the target warehouse.
    """
    po = db.query(PurchaseOrder).filter(PurchaseOrder.id == po_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="Purchase order not found")

    # Find warehouse (use specified or first active warehouse)
    warehouse = None
    if payload.warehouse_id:
        warehouse = db.query(Warehouse).filter(Warehouse.id == payload.warehouse_id).first()
    if not warehouse:
        warehouse = db.query(Warehouse).filter(Warehouse.is_active == True).first()

    received_map = {item.get("item_id"): float(item.get("quantity", 0)) for item in payload.items_received}

    all_received = True
    for line in po.items:
        add_qty = received_map.get(line.id, float(line.quantity) - float(line.received_quantity))
        if add_qty > 0:
            line.received_quantity = float(line.received_quantity) + add_qty

            # If product is tracked, increase warehouse stock
            if line.product_id and warehouse:
                stock = (
                    db.query(WarehouseStock)
                    .filter(
                        WarehouseStock.product_id == line.product_id,
                        WarehouseStock.warehouse_id == warehouse.id,
                    )
                    .first()
                )
                before_qty = stock.quantity_on_hand if stock else 0
                after_qty = before_qty + int(add_qty)

                if not stock:
                    stock = WarehouseStock(
                        product_id=line.product_id,
                        warehouse_id=warehouse.id,
                        quantity_on_hand=int(add_qty),
                        reserved_quantity=0,
                        available_quantity=int(add_qty),
                        reorder_level=10,
                    )
                    db.add(stock)
                else:
                    stock.quantity_on_hand += int(add_qty)
                    stock.available_quantity += int(add_qty)
                    stock.last_updated = datetime.now(timezone.utc)

                # Record stock movement
                movement = StockMovement(
                    product_id=line.product_id,
                    warehouse_id=warehouse.id,
                    movement_type="IN",
                    quantity=int(add_qty),
                    quantity_before=before_qty,
                    quantity_after=after_qty,
                    reference_type="PURCHASE_ORDER",
                    reference_id=po.po_number,
                    notes=f"Goods received from {po.supplier.name if po.supplier else 'vendor'}",
                    created_by=current_user.id,
                )
                db.add(movement)

        if float(line.received_quantity) < float(line.quantity):
            all_received = False

    if all_received:
        po.status = "Received"
    else:
        po.status = "Ordered"

    po.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(po)
    if po.supplier:
        po.supplier_name = po.supplier.name
    return po
