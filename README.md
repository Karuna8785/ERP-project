# SmartERP — Unified Enterprise Resource Planning Platform

SmartERP is a modern, cohesive, full-stack Enterprise Resource Planning (ERP) platform designed for commercial sales execution, customer relationship management (CRM), multi-warehouse inventory control, human resource administration, procurement & vendor logistics, and financial cash-flow governance.

---

## 1. Executive System Overview & Modules

SmartERP unifies seven enterprise modules into one integrated software suite with shared data contracts, automated workflow triggers, and fine-grained Role-Based Access Control (RBAC):

1. **Executive Cockpit & Analytics (`/`)**: Real-time cross-enterprise business intelligence, gross invoiced volume, operating spend, stock health, workforce metrics, and visual monthly financial trends.
2. **Sales & Distribution (`/sales`)**: Full commercial lifecycle — quotations, sales orders, automated invoicing, customer payment receipts, printable tax vouchers, and pipeline analytics.
3. **CRM & Pipeline (`/crm`)**: Prospect qualification funnel (`New` → `Contacted` → `Qualified` → `Proposal` → `Won`), one-click lead-to-account conversion, multi-channel touchpoint logging (calls, emails, meetings, notes), and customer activity timelines.
4. **Inventory & Warehousing (`/inventory`)**: Master product catalog, categories, multi-warehouse stock tracking, stock transfers, inbound/outbound adjustments, and automated low-stock warnings with reorder triggers.
5. **Procurement & Vendors (`/procurement`)**: Approved supplier directory, purchase order generation, goods receipt notes (GRN), and automated warehouse inventory incrementing upon delivery receipt.
6. **Finance & Accounting (`/finance`)**: Real-time cash position, accounts receivable (AR), accounts payable (AP) tracking, operating expense ledger, and cash-flow summaries.
7. **Human Resources & Workforce (`/hr`)**: Employee directory, organizational departments, daily check-in/out attendance logging, and multi-tier leave request approval workflows.
8. **Security & Governance (`/security`)**: Immutable system audit logs tracking logins and mutations with IP/timestamp telemetry, plus visual enterprise RBAC permissions matrix.

---

## 2. Technology Stack

### Frontend
- **Framework**: React 19 + Vite 8
- **Routing**: React Router v7
- **Styling**: Tailwind CSS + Custom Enterprise Theme (Dark Slate 950 aesthetic)
- **Icons**: Lucide React
- **Data Visualizations**: Recharts + Custom Responsive SVG Analytics
- **Networking**: Axios with automatic JWT bearer interceptors and 401 token refresh handling

### Backend
- **Framework**: FastAPI (Asynchronous Python 3.10+)
- **ORM & Data Layer**: SQLAlchemy 2.0 with unified declarative models
- **Validation**: Pydantic v2 schemas
- **Database**: PostgreSQL support with seamless SQLite zero-config local engine fallback and automatic table column synchronization
- **Authentication**: JWT (JSON Web Tokens) with PBKDF2/bcrypt salted password hashing
- **Testing**: Pytest with HTTPX test client (90 comprehensive integration and unit tests passing)

---

## 3. Project Structure

```
Project1/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/          # FastAPI routers (auth, users, inventory, hr, sales, crm, procurement, finance, audit, reports)
│   │   ├── core/                # JWT security, config, permissions definitions
│   │   ├── database/            # Database session, base model registry, table column sync
│   │   ├── models/              # Unified SQLAlchemy ORM models (User, Customer, Lead, Product, Stock, Sale, Purchase, Expense, etc.)
│   │   ├── schemas/             # Pydantic request/response validation schemas
│   │   ├── services/            # Core business logic services
│   │   └── main.py              # Application entrypoint & lifespan table initializers
│   ├── tests/                   # Backend unit tests (65 tests)
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── api/                 # Inventory & auth API adapters
│   │   ├── components/          # Reusable UI components (AppLayout, Navbar, Sidebar, Modal, StatCard, etc.)
│   │   ├── context/             # AuthContext, NotificationContext
│   │   ├── pages/
│   │   │   ├── auth/            # Login, Register
│   │   │   ├── crm/             # CRMOverview, LeadsPage, CustomersPage
│   │   │   ├── dashboard/       # ExecutiveDashboard, SalesDashboard
│   │   │   ├── finance/         # FinancePage (Cash flow, expenses)
│   │   │   ├── hr/              # Employees, Departments, Attendance, Leaves
│   │   │   ├── inventory/       # Products, Warehouses, Categories, Stock, Movements
│   │   │   ├── procurement/     # Suppliers, Purchase Orders, Goods Receipt
│   │   │   ├── sales/           # Quotations, Sales Orders, Invoices, Payments
│   │   │   └── security/        # AuditLogsPage, RolesPermissionsPage
│   │   ├── services/            # Axios API services (crm, procurement, finance, report, audit, sales, hr, auth)
│   │   ├── App.jsx              # Main routing tree
│   │   └── index.css            # Dark enterprise design system
│   └── package.json             # Frontend dependencies
├── tests/                       # Root integration tests (25 tests covering CRM, Sales, RBAC, Finance, Audit)
├── start.bat                    # One-click Windows application launcher
└── README.md
```

---

## 4. Quick Start & Installation

### Option A: 1-Click Launch (Recommended for Windows)

Double-click `start.bat` from the root folder or execute in terminal:
```cmd
start.bat
```
This launcher checks prerequisites, prepares the Python virtual environment and frontend modules, and starts both servers concurrently.

---

### Option B: Manual Step-by-Step Setup

#### 1. Backend Server
```powershell
cd backend

# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
- API Base URL: `http://localhost:8000`
- Swagger UI Documentation: `http://localhost:8000/docs`
- ReDoc Interactive Documentation: `http://localhost:8000/redoc`

#### 2. Frontend Client
```powershell
cd frontend

# Install node packages
npm install

# Start Vite dev server
npm run dev
```
- Web Application: `http://localhost:5173`

---

## 5. Demo Credentials

The database automatically seeds standard user accounts upon startup:

| Role | Username | Password | Permissions Scope |
|---|---|---|---|
| **System Administrator** | `admin` | `Admin@123` | Unrestricted access across all 7 modules, user management, audit logs |
| **Sales Manager** | `salesmgr` | `Manager@123` | Full sales lifecycle, quotations, invoicing, customer accounts |
| **HR Manager** | `hrmanager` | `Hr@123` | Personnel directory, departmental records, leave management |
| **Enterprise Staff** | `staff` | `Staff@123` | Standard operational view and attendance logging |

---

## 6. Automated Testing Verification

The project includes 90 comprehensive automated tests passing with 100% success rate:

```powershell
# Run backend tests (65 tests)
.\.venv\Scripts\pytest.exe -v backend/tests/

# Run integration tests (25 tests)
.\.venv\Scripts\pytest.exe -v tests/

# Build production frontend bundle
cd frontend
npm run build
```

---

## 7. Cross-Module Workflows

- **Lead-to-Cash**: An inbound lead created in `/crm/leads` is qualified and converted into an active customer account. The sales rep issues a quotation in `/sales/quotations`, confirms it into a sales order, generates a commercial invoice, and logs receipt of payment.
- **Inbound Procurement-to-Stock**: When inventory runs low, a purchase order is raised to an approved vendor in `/procurement`. Upon physical delivery, clicking **Receive Stock** automatically increments on-hand warehouse inventory and creates an immutable Goods Receipt audit record.
- **Financial Balance**: Invoiced customer sales feed into Accounts Receivable, while vendor purchases and logged corporate spend (`/finance`) feed into Accounts Payable and expense tracking, presenting an accurate executive net cash position.
