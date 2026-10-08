import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.session import SessionLocal
from app.models.product import Product

client = TestClient(app)


def get_admin_token():
    resp = client.post(
        "/api/v1/auth/login",
        json={"username_or_email": "admin", "password": "Admin@123"}
    )
    assert resp.status_code == 200
    return resp.json()["access_token"]


def test_supplier_crud():
    token = get_admin_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "name": "Global Tech Logistics Ltd",
        "contact_name": "Rajiv Mehra",
        "email": "supply@gtlogistics.example.com",
        "phone": "+91 98760 12345",
        "city": "Bengaluru",
        "country": "India",
        "payment_terms": "Net 30",
        "is_active": True,
    }
    # Create
    create_resp = client.post("/api/v1/procurement/suppliers", json=payload, headers=headers)
    assert create_resp.status_code == 201
    supplier = create_resp.json()
    assert supplier["name"] == "Global Tech Logistics Ltd"
    assert supplier["supplier_code"].startswith("SUP-")

    # List & Search
    list_resp = client.get("/api/v1/procurement/suppliers?search=Logistics", headers=headers)
    assert list_resp.status_code == 200
    items = list_resp.json()
    assert len(items) >= 1


def test_purchase_order_lifecycle():
    token = get_admin_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Find a product and supplier
    db = SessionLocal()
    product = db.query(Product).first()
    db.close()

    sup_resp = client.get("/api/v1/procurement/suppliers", headers=headers)
    suppliers = sup_resp.json()
    assert len(suppliers) > 0
    supplier_id = suppliers[0]["id"]

    po_payload = {
        "supplier_id": supplier_id,
        "shipping_cost": 2500.0,
        "notes": "Bulk enterprise inventory restock",
        "items": [
            {
                "product_id": product.id if product else None,
                "product_name": product.product_name if product else "Generic IT Server Unit",
                "quantity": 10.0,
                "unit_cost": 5000.0,
            }
        ]
    }
    po_resp = client.post("/api/v1/procurement/purchase-orders", json=po_payload, headers=headers)
    assert po_resp.status_code == 201
    po = po_resp.json()
    assert po["po_number"].startswith("PO-")
    assert po["status"] == "Draft"
    assert po["total_amount"] > 0
    po_id = po["id"]

    # Status update
    status_resp = client.patch(
        f"/api/v1/procurement/purchase-orders/{po_id}/status",
        json={"status": "Approved"},
        headers=headers
    )
    assert status_resp.status_code == 200
    assert status_resp.json()["status"] == "Approved"

    # Goods receipt
    rcv_resp = client.post(
        f"/api/v1/procurement/purchase-orders/{po_id}/receive",
        json={"items_received": [{"item_id": po["items"][0]["id"], "quantity": 10.0}]},
        headers=headers
    )
    assert rcv_resp.status_code == 200
    assert rcv_resp.json()["status"] == "Received"


def test_expenses_and_finance_overview():
    token = get_admin_token()
    headers = {"Authorization": f"Bearer {token}"}

    exp_payload = {
        "title": "Cloud Server Scaling - Q4",
        "category": "Software & IT",
        "amount": 32000.0,
        "payment_method": "Credit Card",
        "reference_no": "INV-AWS-8899",
        "notes": "Scaling web instances for load surge",
    }
    exp_resp = client.post("/api/v1/finance/expenses", json=exp_payload, headers=headers)
    assert exp_resp.status_code == 201
    expense = exp_resp.json()
    assert expense["category"] == "Software & IT"

    # Overview
    overview_resp = client.get("/api/v1/finance/overview", headers=headers)
    assert overview_resp.status_code == 200
    data = overview_resp.json()
    assert "kpis" in data
    assert "payables" in data
    assert data["kpis"]["total_expenses"] > 0


def test_executive_reports():
    token = get_admin_token()
    headers = {"Authorization": f"Bearer {token}"}

    report_resp = client.get("/api/v1/reports/executive", headers=headers)
    assert report_resp.status_code == 200
    data = report_resp.json()
    assert "summary" in data
    assert "inventory" in data
    assert "hr" in data
    assert "crm" in data
    assert "trends" in data
