import logging
from contextlib import asynccontextmanager
from datetime import datetime, timezone, date
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.session import engine, Base, SessionLocal
import app.database.base  # ensure all models are registered

# Route imports
from app.api.routes import (
    auth,
    users,
    audit,
    sales,
    master,
    crm,
    procurement,
    finance,
    reports,
    departments,
    employees,
    attendance,
    leaves,
)
from app.routers import categories, products, warehouses, inventory
from app.routers.auth import seed_default_roles_and_admin

# Models for sample seeding
from app.models.user import User, Role, Permission
from app.models.customer import Customer
from app.models.crm import Lead, CustomerInteraction
from app.models.product import Product
from app.models.category import Category
from app.models.warehouse import Warehouse
from app.models.inventory import WarehouseStock
from app.models.department import Department
from app.models.employee import Employee
from app.models.procurement import Supplier, PurchaseOrder, PurchaseOrderItem, Expense
from app.core.security import get_password_hash

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SmartERP")


def seed_initial_data(db=None):
    """Seed comprehensive initial demo data across all modules if database is fresh."""
    close_db = False
    if db is None:
        db = SessionLocal()
        close_db = True
    try:
        # 1. Roles & Permissions
        admin_role = db.query(Role).filter(Role.name == "ADMIN").first()
        if not admin_role:
            admin_role = Role(name="ADMIN", description="System Administrator")
            mgr_role = Role(name="MANAGER", description="Sales & Operations Manager")
            emp_role = Role(name="EMPLOYEE", description="Staff / Sales Executive")
            db.add_all([admin_role, mgr_role, emp_role])
            db.commit()
            db.refresh(admin_role)

        # 2. Users
        admin_user = db.query(User).filter(User.username == "admin").first()
        if not admin_user:
            admin_user = User(
                full_name="Administrator",
                username="admin",
                email="admin@smarterp.local",
                hashed_password=get_password_hash("Admin@123"),
                is_active=True,
                is_superuser=True,
            )
            admin_user.roles.append(admin_role)
            db.add(admin_user)
            db.commit()

        manager_user = db.query(User).filter(User.username == "salesmgr").first()
        if not manager_user:
            mgr_role = db.query(Role).filter(Role.name == "MANAGER").first()
            manager_user = User(
                full_name="Sarah Jenkins (Operations Manager)",
                username="salesmgr",
                email="sarah@smarterp.local",
                hashed_password=get_password_hash("Manager@123"),
                is_active=True,
                is_superuser=False,
            )
            if mgr_role:
                manager_user.roles.append(mgr_role)
            db.add(manager_user)
            db.commit()

        emp_user = db.query(User).filter(User.username == "employee").first()
        if not emp_user:
            emp_role = db.query(Role).filter(Role.name == "EMPLOYEE").first()
            emp_user = User(
                full_name="Alex Rivera (Sales & Operations Staff)",
                username="employee",
                email="employee@smarterp.local",
                hashed_password=get_password_hash("EmployeePassword123!"),
                is_active=True,
                is_superuser=False,
            )
            if emp_role:
                emp_user.roles.append(emp_role)
            db.add(emp_user)
            db.commit()

        # 3. Warehouses
        central_wh = db.query(Warehouse).first()
        if not central_wh:
            central_wh = Warehouse(
                warehouse_code="WH-MUM-01",
                warehouse_name="Central Distribution Facility",
                address="Plot 42, Logistics Park, Navi Mumbai",
                city="Mumbai",
                state="Maharashtra",
                postal_code="400701",
                contact_person="Ramesh Patel",
                phone="+91 98200 11223",
                email="warehouse.mum@smarterp.local",
                is_active=True,
            )
            db.add(central_wh)
            db.commit()
            db.refresh(central_wh)

        # 4. Inventory Categories & Products
        gen_cat = db.query(Category).first()
        if not gen_cat:
            gen_cat = Category(
                category_code="CAT-GEN",
                category_name="General Hardware & Software",
                description="Enterprise IT infrastructure and software subscriptions",
            )
            db.add(gen_cat)
            db.commit()
            db.refresh(gen_cat)

        if db.query(Product).count() == 0:
            products_list = [
                Product(
                    product_code="PRD-ERP-CORE",
                    sku="PROD-ERP-CORE",
                    product_name="SmartERP Cloud Subscription (1 Year)",
                    description="Full ERP platform access for up to 25 users with priority support",
                    category_id=gen_cat.id,
                    unit="License",
                    selling_price=120000.0,
                    cost_price=30000.0,
                    tax_percentage=18.0,
                    reorder_level=10,
                ),
                Product(
                    product_code="PRD-SRV-RACK",
                    sku="PROD-SRV-RACK",
                    product_name="Enterprise Rack Server X4",
                    description="Dual Xeon Gold, 128GB ECC RAM, 4TB NVMe SSD",
                    category_id=gen_cat.id,
                    unit="Units",
                    selling_price=245000.0,
                    cost_price=180000.0,
                    tax_percentage=18.0,
                    reorder_level=5,
                ),
                Product(
                    product_code="PRD-CNS-IMPL",
                    sku="PROD-CNS-IMPL",
                    product_name="ERP Implementation Consulting Services",
                    description="Professional deployment, migration, workflow customization and staff onboarding",
                    category_id=gen_cat.id,
                    unit="Hours",
                    selling_price=4500.0,
                    cost_price=2000.0,
                    tax_percentage=18.0,
                    reorder_level=20,
                ),
                Product(
                    product_code="PRD-IOT-SCAN",
                    sku="PROD-IOT-SCAN",
                    product_name="Industrial Barcode & RFID Scanner",
                    description="Rugged handheld 2D imager with Bluetooth 5.2 and IP65 protection",
                    category_id=gen_cat.id,
                    unit="Pcs",
                    selling_price=18500.0,
                    cost_price=11000.0,
                    tax_percentage=18.0,
                    reorder_level=15,
                ),
            ]
            db.add_all(products_list)
            db.commit()

            # Seed stock in central warehouse
            for p in products_list:
                stock = WarehouseStock(
                    product_id=p.id,
                    warehouse_id=central_wh.id,
                    quantity_on_hand=50,
                    reserved_quantity=5,
                    available_quantity=45,
                    reorder_level=p.reorder_level,
                )
                db.add(stock)
            db.commit()

        # 5. CRM Customers
        if db.query(Customer).count() == 0:
            customers = [
                Customer(
                    customer_code="CUST-1000",
                    name="Acme Corporation",
                    company_name="Acme Global Industries",
                    email="partnerships@acme.example.com",
                    phone="+1 (555) 234-5678",
                    industry="Manufacturing",
                    customer_type="ENTERPRISE",
                    status="ACTIVE",
                    address="100 Acme Way, Suite 400",
                    city="Chicago",
                    country="USA",
                    tax_id="36AABCA9999F1Z0",
                    annual_revenue=20000000.0,
                    credit_limit=3000000.0,
                ),
                Customer(
                    customer_code="CUST-1001",
                    name="Apex Global Technologies",
                    company_name="Apex Global Ltd.",
                    email="procurement@apextech.io",
                    phone="+91 98765 43210",
                    industry="Technology",
                    customer_type="ENTERPRISE",
                    status="ACTIVE",
                    address="Cyber City Tower 4, Phase 2",
                    city="Hyderabad",
                    country="India",
                    tax_id="36AABCA1234F1Z5",
                    annual_revenue=15000000.0,
                    credit_limit=2500000.0,
                ),
                Customer(
                    customer_code="CUST-1002",
                    name="Zenith Retail Ventures",
                    company_name="Zenith Retail India",
                    email="finance@zenithretail.com",
                    phone="+91 91234 56789",
                    industry="Retail",
                    customer_type="ENTERPRISE",
                    status="ACTIVE",
                    address="MG Road Commercial Complex",
                    city="Bengaluru",
                    country="India",
                    tax_id="29AABCB5678D1Z2",
                    annual_revenue=8500000.0,
                    credit_limit=1200000.0,
                ),
                Customer(
                    customer_code="CUST-1003",
                    name="Horizon Logistics Corp",
                    company_name="Horizon Freight Systems",
                    email="billing@horizonlogistics.com",
                    phone="+91 94455 66778",
                    industry="Logistics",
                    customer_type="ENTERPRISE",
                    status="ACTIVE",
                    address="Harbour Port Boulevard",
                    city="Mumbai",
                    country="India",
                    tax_id="27AABCC9988E1Z9",
                    annual_revenue=12000000.0,
                    credit_limit=1800000.0,
                ),
            ]
            db.add_all(customers)
            db.commit()

        # 6. CRM Leads & Interactions
        if db.query(Lead).count() == 0:
            sample_leads = [
                Lead(
                    first_name="Marcus",
                    last_name="Vance",
                    email="m.vance@solarenergy.example.com",
                    phone="+1 (555) 444-3333",
                    company="Solar Energy Group",
                    title="VP of Operations",
                    lead_source="WEBSITE",
                    lead_status="QUALIFIED",
                    lead_score=90,
                    estimated_value=250000.0,
                    notes="Interested in full ERP rollout across 4 manufacturing sites.",
                ),
                Lead(
                    first_name="Priya",
                    last_name="Sharma",
                    email="priya.s@novatech.io",
                    phone="+91 98111 22334",
                    company="NovaTech Solutions",
                    title="CTO",
                    lead_source="REFERRAL",
                    lead_status="PROPOSAL_SENT",
                    lead_score=85,
                    estimated_value=180000.0,
                    notes="Proposal sent for 50-user ERP cloud tier and data migration.",
                ),
                Lead(
                    first_name="David",
                    last_name="Chen",
                    email="david@pacifictrade.hk",
                    phone="+852 9876 5432",
                    company="Pacific Trade International",
                    title="Managing Director",
                    lead_source="TRADE_SHOW",
                    lead_status="NEGOTIATION",
                    lead_score=92,
                    estimated_value=420000.0,
                    notes="Contract review underway with procurement counsel.",
                ),
            ]
            db.add_all(sample_leads)
            db.commit()

            c1 = db.query(Customer).first()
            if c1:
                interaction = CustomerInteraction(
                    customer_id=c1.id,
                    user_id=admin_user.id if admin_user else None,
                    interaction_type="MEETING",
                    title="Quarterly Review & Renewal Discussion",
                    notes="Met with VP Procurement to review SLAs and planned expansion.",
                    outcome="COMPLETED",
                    interaction_date=datetime.now(timezone.utc),
                )
                db.add(interaction)
                db.commit()

        # 7. Procurement Suppliers & POs
        if db.query(Supplier).count() == 0:
            supplier = Supplier(
                supplier_code="SUP-1001",
                name="ServerTech Components Ltd",
                contact_name="Vikram Sethi",
                email="orders@servertech.in",
                phone="+91 98450 77889",
                address="Electronics City Industrial Zone",
                city="Bengaluru",
                country="India",
                tax_id="29AABCS1122A1Z4",
                payment_terms="Net 30",
                is_active=True,
            )
            db.add(supplier)
            db.commit()
            db.refresh(supplier)

            # Sample PO
            po = PurchaseOrder(
                po_number="PO-2026-1001",
                supplier_id=supplier.id,
                order_date=datetime.now(timezone.utc),
                status="Received",
                subtotal=360000.0,
                tax_amount=64800.0,
                shipping_cost=5000.0,
                total_amount=429800.0,
                payment_status="Paid",
                notes="Initial stock order for Enterprise Rack Servers.",
                created_by_id=admin_user.id if admin_user else None,
            )
            db.add(po)
            db.commit()

        # 8. Operating Expenses
        if db.query(Expense).count() == 0:
            expenses = [
                Expense(
                    title="AWS Cloud Hosting & Database Cluster",
                    category="Software & IT",
                    amount=45000.0,
                    payment_method="Credit Card",
                    reference_no="AWS-INV-2026-09",
                    status="Paid",
                    notes="Monthly production cloud infrastructure billing.",
                    created_by_id=admin_user.id if admin_user else None,
                ),
                Expense(
                    title="Office Internet Leased Line Fiber",
                    category="Utilities",
                    amount=8500.0,
                    payment_method="Bank Transfer",
                    reference_no="AIRTEL-OCT-01",
                    status="Paid",
                    notes="High-speed dedicated leased line for headquarters.",
                    created_by_id=admin_user.id if admin_user else None,
                ),
                Expense(
                    title="Warehouse Facility Rent (October)",
                    category="Rent & Facilities",
                    amount=120000.0,
                    payment_method="Bank Transfer",
                    reference_no="RENT-OCT-2026",
                    status="Approved",
                    notes="Monthly warehouse facility lease payment.",
                    created_by_id=admin_user.id if admin_user else None,
                ),
            ]
            db.add_all(expenses)
            db.commit()

    except Exception as e:
        logger.error(f"Error in seed_initial_data: {e}")
        db.rollback()
    finally:
        if close_db:
            db.close()


def sync_sqlite_columns(target_engine):
    """Ensure existing SQLite tables receive newly added model columns."""
    if not str(target_engine.url).startswith("sqlite"):
        return
    try:
        from sqlalchemy import inspect, text
        inspector = inspect(target_engine)
        for table_name, table in Base.metadata.tables.items():
            if inspector.has_table(table_name):
                existing_cols = {c["name"] for c in inspector.get_columns(table_name)}
                for col in table.columns:
                    if col.name not in existing_cols:
                        col_type = col.type.compile(target_engine.dialect)
                        with target_engine.begin() as conn:
                            conn.execute(text(f"ALTER TABLE {table_name} ADD COLUMN {col.name} {col_type}"))
    except Exception as e:
        logger.warning(f"Column sync notice: {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Synchronize schema and initialize tables
    sync_sqlite_columns(engine)
    Base.metadata.create_all(bind=engine)
    # Run seed scripts
    try:
        with SessionLocal() as db:
            seed_default_roles_and_admin(db)
            seed_initial_data(db)
    except Exception as e:
        logger.warning(f"Initial seed warning: {e}")
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="SmartERP — Modular Enterprise Resource Planning Platform with Auth, HR, Inventory, Sales, CRM, Procurement, and Finance.",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/api/openapi.json",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API v1 Prefix
api_v1_prefix = settings.API_V1_STR

# 1. Authentication & Security
app.include_router(auth.router, prefix=api_v1_prefix)
app.include_router(users.router, prefix=api_v1_prefix)
app.include_router(audit.router, prefix=api_v1_prefix)

# 2. Sales Management
app.include_router(sales.router, prefix=api_v1_prefix)
app.include_router(master.router, prefix=api_v1_prefix)

# 3. CRM (Customer Relationship Management)
app.include_router(crm.router, prefix=api_v1_prefix)

# 4. HR Management
app.include_router(departments.router, prefix=api_v1_prefix)
app.include_router(employees.router, prefix=api_v1_prefix)
app.include_router(attendance.router, prefix=api_v1_prefix)
app.include_router(leaves.router, prefix=api_v1_prefix)

# 5. Inventory & Warehousing
app.include_router(categories.router, prefix=api_v1_prefix)
app.include_router(products.router, prefix=api_v1_prefix)
app.include_router(warehouses.router, prefix=api_v1_prefix)
app.include_router(inventory.router, prefix=api_v1_prefix)

# 6. Procurement & Finance
app.include_router(procurement.router, prefix=api_v1_prefix)
app.include_router(finance.router, prefix=api_v1_prefix)

# 7. Executive Analytics & Reports
app.include_router(reports.router, prefix=api_v1_prefix)

# 8. Enterprise Titan Suite Dynamic Modules
try:
    import importlib
    import os
    _modules_dir = os.path.join(os.path.dirname(__file__), "modules")
    if os.path.exists(_modules_dir):
        for _m_name in sorted(os.listdir(_modules_dir)):
            _mod_pkg = os.path.join(_modules_dir, _m_name)
            if os.path.isdir(_mod_pkg) and os.path.exists(os.path.join(_mod_pkg, "__init__.py")):
                try:
                    _mod = importlib.import_module(f"app.modules.{_m_name}")
                    if hasattr(_mod, "router"):
                        app.include_router(_mod.router, prefix=api_v1_prefix)
                except Exception as _ex:
                    logger.debug(f"Module {_m_name} router not loaded: {_ex}")
except Exception as _ex:
    logger.debug(f"Enterprise modules registration error: {_ex}")


@app.get("/", tags=["Health"])
def root():
    return {
        "system": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "module": "Enterprise Resource Planning Platform",
        "status": "Online",
        "docs": "/docs",
        "redoc": "/redoc",
        "modules": {
            "auth": f"{api_v1_prefix}/auth",
            "users": f"{api_v1_prefix}/users",
            "audit": f"{api_v1_prefix}/audit",
            "sales": f"{api_v1_prefix}/sales",
            "crm": f"{api_v1_prefix}/crm",
            "inventory": f"{api_v1_prefix}/inventory",
            "hr": f"{api_v1_prefix}/employees",
            "procurement": f"{api_v1_prefix}/procurement",
            "finance": f"{api_v1_prefix}/finance",
            "reports": f"{api_v1_prefix}/reports",
        },
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "service": settings.PROJECT_NAME}


@app.get("/download/zip", tags=["Export"])
@app.get("/SmartERP_Enterprise_v1.1.0.zip", tags=["Export"])
def download_project_zip():
    from fastapi.responses import FileResponse
    import os
    zip_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "SmartERP_Enterprise_v1.1.0.zip"))
    return FileResponse(zip_path, media_type="application/zip", filename="SmartERP_Enterprise_v1.1.0.zip")

