-- SmartERP Enterprise Titan Migration 014: Project Lifecycle & Milestone Billing DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS project_management_projectcharters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_projectcharters_code ON project_management_projectcharters(code);
CREATE INDEX IF NOT EXISTS idx_project_management_projectcharters_org_status ON project_management_projectcharters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_projectcharters_priority ON project_management_projectcharters(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_projectcharters_created_at ON project_management_projectcharters(created_at);

-- Operational seed data fixtures for project_management_projectcharters
INSERT OR IGNORE INTO project_management_projectcharters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProjectCharter 1", 24500.00, 150.0, "ACTIVE", "uuid-projectcharter-01"),
    (2, "PRO-0002", "Secondary Corporate ProjectCharter 2", 18200.50, 80.0, "ACTIVE", "uuid-projectcharter-02"),
    (3, "PRO-0003", "Consolidated Branch ProjectCharter 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-projectcharter-03"),
    (4, "PRO-0004", "Enterprise Audited ProjectCharter 4", 32800.00, 210.0, "ACTIVE", "uuid-projectcharter-04"),
    (5, "PRO-0005", "Executive Strategic ProjectCharter 5", 65000.00, 400.0, "ACTIVE", "uuid-projectcharter-05");

CREATE TABLE IF NOT EXISTS project_management_wbsphases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_wbsphases_code ON project_management_wbsphases(code);
CREATE INDEX IF NOT EXISTS idx_project_management_wbsphases_org_status ON project_management_wbsphases(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_wbsphases_priority ON project_management_wbsphases(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_wbsphases_created_at ON project_management_wbsphases(created_at);

-- Operational seed data fixtures for project_management_wbsphases
INSERT OR IGNORE INTO project_management_wbsphases (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WBS-0001", "Primary Operational WBSPhase 1", 24500.00, 150.0, "ACTIVE", "uuid-wbsphase-01"),
    (2, "WBS-0002", "Secondary Corporate WBSPhase 2", 18200.50, 80.0, "ACTIVE", "uuid-wbsphase-02"),
    (3, "WBS-0003", "Consolidated Branch WBSPhase 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-wbsphase-03"),
    (4, "WBS-0004", "Enterprise Audited WBSPhase 4", 32800.00, 210.0, "ACTIVE", "uuid-wbsphase-04"),
    (5, "WBS-0005", "Executive Strategic WBSPhase 5", 65000.00, 400.0, "ACTIVE", "uuid-wbsphase-05");

CREATE TABLE IF NOT EXISTS project_management_milestonedeliverables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_milestonedeliverables_code ON project_management_milestonedeliverables(code);
CREATE INDEX IF NOT EXISTS idx_project_management_milestonedeliverables_org_status ON project_management_milestonedeliverables(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_milestonedeliverables_priority ON project_management_milestonedeliverables(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_milestonedeliverables_created_at ON project_management_milestonedeliverables(created_at);

-- Operational seed data fixtures for project_management_milestonedeliverables
INSERT OR IGNORE INTO project_management_milestonedeliverables (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MIL-0001", "Primary Operational MilestoneDeliverable 1", 24500.00, 150.0, "ACTIVE", "uuid-milestonedeliverable-01"),
    (2, "MIL-0002", "Secondary Corporate MilestoneDeliverable 2", 18200.50, 80.0, "ACTIVE", "uuid-milestonedeliverable-02"),
    (3, "MIL-0003", "Consolidated Branch MilestoneDeliverable 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-milestonedeliverable-03"),
    (4, "MIL-0004", "Enterprise Audited MilestoneDeliverable 4", 32800.00, 210.0, "ACTIVE", "uuid-milestonedeliverable-04"),
    (5, "MIL-0005", "Executive Strategic MilestoneDeliverable 5", 65000.00, 400.0, "ACTIVE", "uuid-milestonedeliverable-05");

CREATE TABLE IF NOT EXISTS project_management_projecttasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_projecttasks_code ON project_management_projecttasks(code);
CREATE INDEX IF NOT EXISTS idx_project_management_projecttasks_org_status ON project_management_projecttasks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_projecttasks_priority ON project_management_projecttasks(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_projecttasks_created_at ON project_management_projecttasks(created_at);

-- Operational seed data fixtures for project_management_projecttasks
INSERT OR IGNORE INTO project_management_projecttasks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProjectTask 1", 24500.00, 150.0, "ACTIVE", "uuid-projecttask-01"),
    (2, "PRO-0002", "Secondary Corporate ProjectTask 2", 18200.50, 80.0, "ACTIVE", "uuid-projecttask-02"),
    (3, "PRO-0003", "Consolidated Branch ProjectTask 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-projecttask-03"),
    (4, "PRO-0004", "Enterprise Audited ProjectTask 4", 32800.00, 210.0, "ACTIVE", "uuid-projecttask-04"),
    (5, "PRO-0005", "Executive Strategic ProjectTask 5", 65000.00, 400.0, "ACTIVE", "uuid-projecttask-05");

CREATE TABLE IF NOT EXISTS project_management_resourceallocations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_resourceallocations_code ON project_management_resourceallocations(code);
CREATE INDEX IF NOT EXISTS idx_project_management_resourceallocations_org_status ON project_management_resourceallocations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_resourceallocations_priority ON project_management_resourceallocations(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_resourceallocations_created_at ON project_management_resourceallocations(created_at);

-- Operational seed data fixtures for project_management_resourceallocations
INSERT OR IGNORE INTO project_management_resourceallocations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RES-0001", "Primary Operational ResourceAllocation 1", 24500.00, 150.0, "ACTIVE", "uuid-resourceallocation-01"),
    (2, "RES-0002", "Secondary Corporate ResourceAllocation 2", 18200.50, 80.0, "ACTIVE", "uuid-resourceallocation-02"),
    (3, "RES-0003", "Consolidated Branch ResourceAllocation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-resourceallocation-03"),
    (4, "RES-0004", "Enterprise Audited ResourceAllocation 4", 32800.00, 210.0, "ACTIVE", "uuid-resourceallocation-04"),
    (5, "RES-0005", "Executive Strategic ResourceAllocation 5", 65000.00, 400.0, "ACTIVE", "uuid-resourceallocation-05");

CREATE TABLE IF NOT EXISTS project_management_timesheetlogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_timesheetlogs_code ON project_management_timesheetlogs(code);
CREATE INDEX IF NOT EXISTS idx_project_management_timesheetlogs_org_status ON project_management_timesheetlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_timesheetlogs_priority ON project_management_timesheetlogs(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_timesheetlogs_created_at ON project_management_timesheetlogs(created_at);

-- Operational seed data fixtures for project_management_timesheetlogs
INSERT OR IGNORE INTO project_management_timesheetlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIM-0001", "Primary Operational TimesheetLog 1", 24500.00, 150.0, "ACTIVE", "uuid-timesheetlog-01"),
    (2, "TIM-0002", "Secondary Corporate TimesheetLog 2", 18200.50, 80.0, "ACTIVE", "uuid-timesheetlog-02"),
    (3, "TIM-0003", "Consolidated Branch TimesheetLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-timesheetlog-03"),
    (4, "TIM-0004", "Enterprise Audited TimesheetLog 4", 32800.00, 210.0, "ACTIVE", "uuid-timesheetlog-04"),
    (5, "TIM-0005", "Executive Strategic TimesheetLog 5", 65000.00, 400.0, "ACTIVE", "uuid-timesheetlog-05");

CREATE TABLE IF NOT EXISTS project_management_expensereimbursements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_expensereimbursements_code ON project_management_expensereimbursements(code);
CREATE INDEX IF NOT EXISTS idx_project_management_expensereimbursements_org_status ON project_management_expensereimbursements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_expensereimbursements_priority ON project_management_expensereimbursements(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_expensereimbursements_created_at ON project_management_expensereimbursements(created_at);

-- Operational seed data fixtures for project_management_expensereimbursements
INSERT OR IGNORE INTO project_management_expensereimbursements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExpenseReimbursement 1", 24500.00, 150.0, "ACTIVE", "uuid-expensereimbursement-01"),
    (2, "EXP-0002", "Secondary Corporate ExpenseReimbursement 2", 18200.50, 80.0, "ACTIVE", "uuid-expensereimbursement-02"),
    (3, "EXP-0003", "Consolidated Branch ExpenseReimbursement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-expensereimbursement-03"),
    (4, "EXP-0004", "Enterprise Audited ExpenseReimbursement 4", 32800.00, 210.0, "ACTIVE", "uuid-expensereimbursement-04"),
    (5, "EXP-0005", "Executive Strategic ExpenseReimbursement 5", 65000.00, 400.0, "ACTIVE", "uuid-expensereimbursement-05");

CREATE TABLE IF NOT EXISTS project_management_projectbudgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_projectbudgets_code ON project_management_projectbudgets(code);
CREATE INDEX IF NOT EXISTS idx_project_management_projectbudgets_org_status ON project_management_projectbudgets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_projectbudgets_priority ON project_management_projectbudgets(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_projectbudgets_created_at ON project_management_projectbudgets(created_at);

-- Operational seed data fixtures for project_management_projectbudgets
INSERT OR IGNORE INTO project_management_projectbudgets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProjectBudget 1", 24500.00, 150.0, "ACTIVE", "uuid-projectbudget-01"),
    (2, "PRO-0002", "Secondary Corporate ProjectBudget 2", 18200.50, 80.0, "ACTIVE", "uuid-projectbudget-02"),
    (3, "PRO-0003", "Consolidated Branch ProjectBudget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-projectbudget-03"),
    (4, "PRO-0004", "Enterprise Audited ProjectBudget 4", 32800.00, 210.0, "ACTIVE", "uuid-projectbudget-04"),
    (5, "PRO-0005", "Executive Strategic ProjectBudget 5", 65000.00, 400.0, "ACTIVE", "uuid-projectbudget-05");

CREATE TABLE IF NOT EXISTS project_management_earnedvaluesnapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_earnedvaluesnapshots_code ON project_management_earnedvaluesnapshots(code);
CREATE INDEX IF NOT EXISTS idx_project_management_earnedvaluesnapshots_org_status ON project_management_earnedvaluesnapshots(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_earnedvaluesnapshots_priority ON project_management_earnedvaluesnapshots(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_earnedvaluesnapshots_created_at ON project_management_earnedvaluesnapshots(created_at);

-- Operational seed data fixtures for project_management_earnedvaluesnapshots
INSERT OR IGNORE INTO project_management_earnedvaluesnapshots (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EAR-0001", "Primary Operational EarnedValueSnapshot 1", 24500.00, 150.0, "ACTIVE", "uuid-earnedvaluesnapshot-01"),
    (2, "EAR-0002", "Secondary Corporate EarnedValueSnapshot 2", 18200.50, 80.0, "ACTIVE", "uuid-earnedvaluesnapshot-02"),
    (3, "EAR-0003", "Consolidated Branch EarnedValueSnapshot 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-earnedvaluesnapshot-03"),
    (4, "EAR-0004", "Enterprise Audited EarnedValueSnapshot 4", 32800.00, 210.0, "ACTIVE", "uuid-earnedvaluesnapshot-04"),
    (5, "EAR-0005", "Executive Strategic EarnedValueSnapshot 5", 65000.00, 400.0, "ACTIVE", "uuid-earnedvaluesnapshot-05");

CREATE TABLE IF NOT EXISTS project_management_changeorderrequests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_changeorderrequests_code ON project_management_changeorderrequests(code);
CREATE INDEX IF NOT EXISTS idx_project_management_changeorderrequests_org_status ON project_management_changeorderrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_changeorderrequests_priority ON project_management_changeorderrequests(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_changeorderrequests_created_at ON project_management_changeorderrequests(created_at);

-- Operational seed data fixtures for project_management_changeorderrequests
INSERT OR IGNORE INTO project_management_changeorderrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHA-0001", "Primary Operational ChangeOrderRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-changeorderrequest-01"),
    (2, "CHA-0002", "Secondary Corporate ChangeOrderRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-changeorderrequest-02"),
    (3, "CHA-0003", "Consolidated Branch ChangeOrderRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-changeorderrequest-03"),
    (4, "CHA-0004", "Enterprise Audited ChangeOrderRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-changeorderrequest-04"),
    (5, "CHA-0005", "Executive Strategic ChangeOrderRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-changeorderrequest-05");

CREATE TABLE IF NOT EXISTS project_management_projectrisklogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_projectrisklogs_code ON project_management_projectrisklogs(code);
CREATE INDEX IF NOT EXISTS idx_project_management_projectrisklogs_org_status ON project_management_projectrisklogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_projectrisklogs_priority ON project_management_projectrisklogs(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_projectrisklogs_created_at ON project_management_projectrisklogs(created_at);

-- Operational seed data fixtures for project_management_projectrisklogs
INSERT OR IGNORE INTO project_management_projectrisklogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProjectRiskLog 1", 24500.00, 150.0, "ACTIVE", "uuid-projectrisklog-01"),
    (2, "PRO-0002", "Secondary Corporate ProjectRiskLog 2", 18200.50, 80.0, "ACTIVE", "uuid-projectrisklog-02"),
    (3, "PRO-0003", "Consolidated Branch ProjectRiskLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-projectrisklog-03"),
    (4, "PRO-0004", "Enterprise Audited ProjectRiskLog 4", 32800.00, 210.0, "ACTIVE", "uuid-projectrisklog-04"),
    (5, "PRO-0005", "Executive Strategic ProjectRiskLog 5", 65000.00, 400.0, "ACTIVE", "uuid-projectrisklog-05");

CREATE TABLE IF NOT EXISTS project_management_stakeholderregisters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_stakeholderregisters_code ON project_management_stakeholderregisters(code);
CREATE INDEX IF NOT EXISTS idx_project_management_stakeholderregisters_org_status ON project_management_stakeholderregisters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_stakeholderregisters_priority ON project_management_stakeholderregisters(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_stakeholderregisters_created_at ON project_management_stakeholderregisters(created_at);

-- Operational seed data fixtures for project_management_stakeholderregisters
INSERT OR IGNORE INTO project_management_stakeholderregisters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StakeholderRegister 1", 24500.00, 150.0, "ACTIVE", "uuid-stakeholderregister-01"),
    (2, "STA-0002", "Secondary Corporate StakeholderRegister 2", 18200.50, 80.0, "ACTIVE", "uuid-stakeholderregister-02"),
    (3, "STA-0003", "Consolidated Branch StakeholderRegister 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-stakeholderregister-03"),
    (4, "STA-0004", "Enterprise Audited StakeholderRegister 4", 32800.00, 210.0, "ACTIVE", "uuid-stakeholderregister-04"),
    (5, "STA-0005", "Executive Strategic StakeholderRegister 5", 65000.00, 400.0, "ACTIVE", "uuid-stakeholderregister-05");

CREATE TABLE IF NOT EXISTS project_management_milestonebillinginvoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_milestonebillinginvoices_code ON project_management_milestonebillinginvoices(code);
CREATE INDEX IF NOT EXISTS idx_project_management_milestonebillinginvoices_org_status ON project_management_milestonebillinginvoices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_milestonebillinginvoices_priority ON project_management_milestonebillinginvoices(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_milestonebillinginvoices_created_at ON project_management_milestonebillinginvoices(created_at);

-- Operational seed data fixtures for project_management_milestonebillinginvoices
INSERT OR IGNORE INTO project_management_milestonebillinginvoices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MIL-0001", "Primary Operational MilestoneBillingInvoice 1", 24500.00, 150.0, "ACTIVE", "uuid-milestonebillinginvoice-01"),
    (2, "MIL-0002", "Secondary Corporate MilestoneBillingInvoice 2", 18200.50, 80.0, "ACTIVE", "uuid-milestonebillinginvoice-02"),
    (3, "MIL-0003", "Consolidated Branch MilestoneBillingInvoice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-milestonebillinginvoice-03"),
    (4, "MIL-0004", "Enterprise Audited MilestoneBillingInvoice 4", 32800.00, 210.0, "ACTIVE", "uuid-milestonebillinginvoice-04"),
    (5, "MIL-0005", "Executive Strategic MilestoneBillingInvoice 5", 65000.00, 400.0, "ACTIVE", "uuid-milestonebillinginvoice-05");

CREATE TABLE IF NOT EXISTS project_management_vendorsubcontracts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_vendorsubcontracts_code ON project_management_vendorsubcontracts(code);
CREATE INDEX IF NOT EXISTS idx_project_management_vendorsubcontracts_org_status ON project_management_vendorsubcontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_vendorsubcontracts_priority ON project_management_vendorsubcontracts(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_vendorsubcontracts_created_at ON project_management_vendorsubcontracts(created_at);

-- Operational seed data fixtures for project_management_vendorsubcontracts
INSERT OR IGNORE INTO project_management_vendorsubcontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorSubcontract 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorsubcontract-01"),
    (2, "VEN-0002", "Secondary Corporate VendorSubcontract 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorsubcontract-02"),
    (3, "VEN-0003", "Consolidated Branch VendorSubcontract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorsubcontract-03"),
    (4, "VEN-0004", "Enterprise Audited VendorSubcontract 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorsubcontract-04"),
    (5, "VEN-0005", "Executive Strategic VendorSubcontract 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorsubcontract-05");

CREATE TABLE IF NOT EXISTS project_management_statusreports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_statusreports_code ON project_management_statusreports(code);
CREATE INDEX IF NOT EXISTS idx_project_management_statusreports_org_status ON project_management_statusreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_statusreports_priority ON project_management_statusreports(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_statusreports_created_at ON project_management_statusreports(created_at);

-- Operational seed data fixtures for project_management_statusreports
INSERT OR IGNORE INTO project_management_statusreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StatusReport 1", 24500.00, 150.0, "ACTIVE", "uuid-statusreport-01"),
    (2, "STA-0002", "Secondary Corporate StatusReport 2", 18200.50, 80.0, "ACTIVE", "uuid-statusreport-02"),
    (3, "STA-0003", "Consolidated Branch StatusReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-statusreport-03"),
    (4, "STA-0004", "Enterprise Audited StatusReport 4", 32800.00, 210.0, "ACTIVE", "uuid-statusreport-04"),
    (5, "STA-0005", "Executive Strategic StatusReport 5", 65000.00, 400.0, "ACTIVE", "uuid-statusreport-05");

CREATE TABLE IF NOT EXISTS project_management_projectclosurereviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(64) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) DEFAULT "ACTIVE",
    priority VARCHAR(32) DEFAULT "MEDIUM",
    risk_rating VARCHAR(32) DEFAULT "MODERATE",
    organization_id INTEGER NOT NULL DEFAULT 1,
    department_id INTEGER DEFAULT 1,
    created_by_user_id INTEGER,
    assigned_to_user_id INTEGER,
    amount DECIMAL(18, 4) DEFAULT 0.0000,
    quantity DECIMAL(18, 4) DEFAULT 0.0000,
    unit_cost DECIMAL(18, 4) DEFAULT 0.0000,
    unit_price DECIMAL(18, 4) DEFAULT 0.0000,
    tax_rate DECIMAL(6, 4) DEFAULT 0.1800,
    discount_rate DECIMAL(6, 4) DEFAULT 0.0000,
    currency VARCHAR(8) DEFAULT "INR",
    external_reference VARCHAR(128),
    uuid_token VARCHAR(64) NOT NULL,
    version_number INTEGER DEFAULT 1,
    is_locked BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    is_deleted BOOLEAN DEFAULT 0,
    metadata_json TEXT DEFAULT "{}",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_project_management_projectclosurereviews_code ON project_management_projectclosurereviews(code);
CREATE INDEX IF NOT EXISTS idx_project_management_projectclosurereviews_org_status ON project_management_projectclosurereviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_project_management_projectclosurereviews_priority ON project_management_projectclosurereviews(priority);
CREATE INDEX IF NOT EXISTS idx_project_management_projectclosurereviews_created_at ON project_management_projectclosurereviews(created_at);

-- Operational seed data fixtures for project_management_projectclosurereviews
INSERT OR IGNORE INTO project_management_projectclosurereviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProjectClosureReview 1", 24500.00, 150.0, "ACTIVE", "uuid-projectclosurereview-01"),
    (2, "PRO-0002", "Secondary Corporate ProjectClosureReview 2", 18200.50, 80.0, "ACTIVE", "uuid-projectclosurereview-02"),
    (3, "PRO-0003", "Consolidated Branch ProjectClosureReview 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-projectclosurereview-03"),
    (4, "PRO-0004", "Enterprise Audited ProjectClosureReview 4", 32800.00, 210.0, "ACTIVE", "uuid-projectclosurereview-04"),
    (5, "PRO-0005", "Executive Strategic ProjectClosureReview 5", 65000.00, 400.0, "ACTIVE", "uuid-projectclosurereview-05");

