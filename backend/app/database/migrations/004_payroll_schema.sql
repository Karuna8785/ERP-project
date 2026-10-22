-- SmartERP Enterprise Titan Migration 004: Human Capital & Statutory Payroll DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS payroll_salarystructures (
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

CREATE INDEX IF NOT EXISTS idx_payroll_salarystructures_code ON payroll_salarystructures(code);
CREATE INDEX IF NOT EXISTS idx_payroll_salarystructures_org_status ON payroll_salarystructures(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_salarystructures_priority ON payroll_salarystructures(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_salarystructures_created_at ON payroll_salarystructures(created_at);

-- Operational seed data fixtures for payroll_salarystructures
INSERT OR IGNORE INTO payroll_salarystructures (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAL-0001", "Primary Operational SalaryStructure 1", 24500.00, 150.0, "ACTIVE", "uuid-salarystructure-01"),
    (2, "SAL-0002", "Secondary Corporate SalaryStructure 2", 18200.50, 80.0, "ACTIVE", "uuid-salarystructure-02"),
    (3, "SAL-0003", "Consolidated Branch SalaryStructure 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-salarystructure-03"),
    (4, "SAL-0004", "Enterprise Audited SalaryStructure 4", 32800.00, 210.0, "ACTIVE", "uuid-salarystructure-04"),
    (5, "SAL-0005", "Executive Strategic SalaryStructure 5", 65000.00, 400.0, "ACTIVE", "uuid-salarystructure-05");

CREATE TABLE IF NOT EXISTS payroll_payslips (
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

CREATE INDEX IF NOT EXISTS idx_payroll_payslips_code ON payroll_payslips(code);
CREATE INDEX IF NOT EXISTS idx_payroll_payslips_org_status ON payroll_payslips(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_payslips_priority ON payroll_payslips(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_payslips_created_at ON payroll_payslips(created_at);

-- Operational seed data fixtures for payroll_payslips
INSERT OR IGNORE INTO payroll_payslips (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAY-0001", "Primary Operational PaySlip 1", 24500.00, 150.0, "ACTIVE", "uuid-payslip-01"),
    (2, "PAY-0002", "Secondary Corporate PaySlip 2", 18200.50, 80.0, "ACTIVE", "uuid-payslip-02"),
    (3, "PAY-0003", "Consolidated Branch PaySlip 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-payslip-03"),
    (4, "PAY-0004", "Enterprise Audited PaySlip 4", 32800.00, 210.0, "ACTIVE", "uuid-payslip-04"),
    (5, "PAY-0005", "Executive Strategic PaySlip 5", 65000.00, 400.0, "ACTIVE", "uuid-payslip-05");

CREATE TABLE IF NOT EXISTS payroll_taxdeductions (
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

CREATE INDEX IF NOT EXISTS idx_payroll_taxdeductions_code ON payroll_taxdeductions(code);
CREATE INDEX IF NOT EXISTS idx_payroll_taxdeductions_org_status ON payroll_taxdeductions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_taxdeductions_priority ON payroll_taxdeductions(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_taxdeductions_created_at ON payroll_taxdeductions(created_at);

-- Operational seed data fixtures for payroll_taxdeductions
INSERT OR IGNORE INTO payroll_taxdeductions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxDeduction 1", 24500.00, 150.0, "ACTIVE", "uuid-taxdeduction-01"),
    (2, "TAX-0002", "Secondary Corporate TaxDeduction 2", 18200.50, 80.0, "ACTIVE", "uuid-taxdeduction-02"),
    (3, "TAX-0003", "Consolidated Branch TaxDeduction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxdeduction-03"),
    (4, "TAX-0004", "Enterprise Audited TaxDeduction 4", 32800.00, 210.0, "ACTIVE", "uuid-taxdeduction-04"),
    (5, "TAX-0005", "Executive Strategic TaxDeduction 5", 65000.00, 400.0, "ACTIVE", "uuid-taxdeduction-05");

CREATE TABLE IF NOT EXISTS payroll_epfrecords (
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

CREATE INDEX IF NOT EXISTS idx_payroll_epfrecords_code ON payroll_epfrecords(code);
CREATE INDEX IF NOT EXISTS idx_payroll_epfrecords_org_status ON payroll_epfrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_epfrecords_priority ON payroll_epfrecords(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_epfrecords_created_at ON payroll_epfrecords(created_at);

-- Operational seed data fixtures for payroll_epfrecords
INSERT OR IGNORE INTO payroll_epfrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EPF-0001", "Primary Operational EPFRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-epfrecord-01"),
    (2, "EPF-0002", "Secondary Corporate EPFRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-epfrecord-02"),
    (3, "EPF-0003", "Consolidated Branch EPFRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-epfrecord-03"),
    (4, "EPF-0004", "Enterprise Audited EPFRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-epfrecord-04"),
    (5, "EPF-0005", "Executive Strategic EPFRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-epfrecord-05");

CREATE TABLE IF NOT EXISTS payroll_esicrecords (
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

CREATE INDEX IF NOT EXISTS idx_payroll_esicrecords_code ON payroll_esicrecords(code);
CREATE INDEX IF NOT EXISTS idx_payroll_esicrecords_org_status ON payroll_esicrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_esicrecords_priority ON payroll_esicrecords(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_esicrecords_created_at ON payroll_esicrecords(created_at);

-- Operational seed data fixtures for payroll_esicrecords
INSERT OR IGNORE INTO payroll_esicrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ESI-0001", "Primary Operational ESICRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-esicrecord-01"),
    (2, "ESI-0002", "Secondary Corporate ESICRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-esicrecord-02"),
    (3, "ESI-0003", "Consolidated Branch ESICRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-esicrecord-03"),
    (4, "ESI-0004", "Enterprise Audited ESICRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-esicrecord-04"),
    (5, "ESI-0005", "Executive Strategic ESICRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-esicrecord-05");

CREATE TABLE IF NOT EXISTS payroll_gratuitycalculations (
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

CREATE INDEX IF NOT EXISTS idx_payroll_gratuitycalculations_code ON payroll_gratuitycalculations(code);
CREATE INDEX IF NOT EXISTS idx_payroll_gratuitycalculations_org_status ON payroll_gratuitycalculations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_gratuitycalculations_priority ON payroll_gratuitycalculations(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_gratuitycalculations_created_at ON payroll_gratuitycalculations(created_at);

-- Operational seed data fixtures for payroll_gratuitycalculations
INSERT OR IGNORE INTO payroll_gratuitycalculations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GRA-0001", "Primary Operational GratuityCalculation 1", 24500.00, 150.0, "ACTIVE", "uuid-gratuitycalculation-01"),
    (2, "GRA-0002", "Secondary Corporate GratuityCalculation 2", 18200.50, 80.0, "ACTIVE", "uuid-gratuitycalculation-02"),
    (3, "GRA-0003", "Consolidated Branch GratuityCalculation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-gratuitycalculation-03"),
    (4, "GRA-0004", "Enterprise Audited GratuityCalculation 4", 32800.00, 210.0, "ACTIVE", "uuid-gratuitycalculation-04"),
    (5, "GRA-0005", "Executive Strategic GratuityCalculation 5", 65000.00, 400.0, "ACTIVE", "uuid-gratuitycalculation-05");

CREATE TABLE IF NOT EXISTS payroll_bonusallocations (
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

CREATE INDEX IF NOT EXISTS idx_payroll_bonusallocations_code ON payroll_bonusallocations(code);
CREATE INDEX IF NOT EXISTS idx_payroll_bonusallocations_org_status ON payroll_bonusallocations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_bonusallocations_priority ON payroll_bonusallocations(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_bonusallocations_created_at ON payroll_bonusallocations(created_at);

-- Operational seed data fixtures for payroll_bonusallocations
INSERT OR IGNORE INTO payroll_bonusallocations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BON-0001", "Primary Operational BonusAllocation 1", 24500.00, 150.0, "ACTIVE", "uuid-bonusallocation-01"),
    (2, "BON-0002", "Secondary Corporate BonusAllocation 2", 18200.50, 80.0, "ACTIVE", "uuid-bonusallocation-02"),
    (3, "BON-0003", "Consolidated Branch BonusAllocation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bonusallocation-03"),
    (4, "BON-0004", "Enterprise Audited BonusAllocation 4", 32800.00, 210.0, "ACTIVE", "uuid-bonusallocation-04"),
    (5, "BON-0005", "Executive Strategic BonusAllocation 5", 65000.00, 400.0, "ACTIVE", "uuid-bonusallocation-05");

CREATE TABLE IF NOT EXISTS payroll_leaveencashments (
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

CREATE INDEX IF NOT EXISTS idx_payroll_leaveencashments_code ON payroll_leaveencashments(code);
CREATE INDEX IF NOT EXISTS idx_payroll_leaveencashments_org_status ON payroll_leaveencashments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_leaveencashments_priority ON payroll_leaveencashments(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_leaveencashments_created_at ON payroll_leaveencashments(created_at);

-- Operational seed data fixtures for payroll_leaveencashments
INSERT OR IGNORE INTO payroll_leaveencashments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeaveEncashment 1", 24500.00, 150.0, "ACTIVE", "uuid-leaveencashment-01"),
    (2, "LEA-0002", "Secondary Corporate LeaveEncashment 2", 18200.50, 80.0, "ACTIVE", "uuid-leaveencashment-02"),
    (3, "LEA-0003", "Consolidated Branch LeaveEncashment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leaveencashment-03"),
    (4, "LEA-0004", "Enterprise Audited LeaveEncashment 4", 32800.00, 210.0, "ACTIVE", "uuid-leaveencashment-04"),
    (5, "LEA-0005", "Executive Strategic LeaveEncashment 5", 65000.00, 400.0, "ACTIVE", "uuid-leaveencashment-05");

CREATE TABLE IF NOT EXISTS payroll_expenseclaims (
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

CREATE INDEX IF NOT EXISTS idx_payroll_expenseclaims_code ON payroll_expenseclaims(code);
CREATE INDEX IF NOT EXISTS idx_payroll_expenseclaims_org_status ON payroll_expenseclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_expenseclaims_priority ON payroll_expenseclaims(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_expenseclaims_created_at ON payroll_expenseclaims(created_at);

-- Operational seed data fixtures for payroll_expenseclaims
INSERT OR IGNORE INTO payroll_expenseclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExpenseClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-expenseclaim-01"),
    (2, "EXP-0002", "Secondary Corporate ExpenseClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-expenseclaim-02"),
    (3, "EXP-0003", "Consolidated Branch ExpenseClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-expenseclaim-03"),
    (4, "EXP-0004", "Enterprise Audited ExpenseClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-expenseclaim-04"),
    (5, "EXP-0005", "Executive Strategic ExpenseClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-expenseclaim-05");

CREATE TABLE IF NOT EXISTS payroll_loanadvances (
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

CREATE INDEX IF NOT EXISTS idx_payroll_loanadvances_code ON payroll_loanadvances(code);
CREATE INDEX IF NOT EXISTS idx_payroll_loanadvances_org_status ON payroll_loanadvances(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_loanadvances_priority ON payroll_loanadvances(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_loanadvances_created_at ON payroll_loanadvances(created_at);

-- Operational seed data fixtures for payroll_loanadvances
INSERT OR IGNORE INTO payroll_loanadvances (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LOA-0001", "Primary Operational LoanAdvance 1", 24500.00, 150.0, "ACTIVE", "uuid-loanadvance-01"),
    (2, "LOA-0002", "Secondary Corporate LoanAdvance 2", 18200.50, 80.0, "ACTIVE", "uuid-loanadvance-02"),
    (3, "LOA-0003", "Consolidated Branch LoanAdvance 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-loanadvance-03"),
    (4, "LOA-0004", "Enterprise Audited LoanAdvance 4", 32800.00, 210.0, "ACTIVE", "uuid-loanadvance-04"),
    (5, "LOA-0005", "Executive Strategic LoanAdvance 5", 65000.00, 400.0, "ACTIVE", "uuid-loanadvance-05");

CREATE TABLE IF NOT EXISTS payroll_shiftallowances (
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

CREATE INDEX IF NOT EXISTS idx_payroll_shiftallowances_code ON payroll_shiftallowances(code);
CREATE INDEX IF NOT EXISTS idx_payroll_shiftallowances_org_status ON payroll_shiftallowances(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_shiftallowances_priority ON payroll_shiftallowances(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_shiftallowances_created_at ON payroll_shiftallowances(created_at);

-- Operational seed data fixtures for payroll_shiftallowances
INSERT OR IGNORE INTO payroll_shiftallowances (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational ShiftAllowance 1", 24500.00, 150.0, "ACTIVE", "uuid-shiftallowance-01"),
    (2, "SHI-0002", "Secondary Corporate ShiftAllowance 2", 18200.50, 80.0, "ACTIVE", "uuid-shiftallowance-02"),
    (3, "SHI-0003", "Consolidated Branch ShiftAllowance 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shiftallowance-03"),
    (4, "SHI-0004", "Enterprise Audited ShiftAllowance 4", 32800.00, 210.0, "ACTIVE", "uuid-shiftallowance-04"),
    (5, "SHI-0005", "Executive Strategic ShiftAllowance 5", 65000.00, 400.0, "ACTIVE", "uuid-shiftallowance-05");

CREATE TABLE IF NOT EXISTS payroll_overtimerecords (
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

CREATE INDEX IF NOT EXISTS idx_payroll_overtimerecords_code ON payroll_overtimerecords(code);
CREATE INDEX IF NOT EXISTS idx_payroll_overtimerecords_org_status ON payroll_overtimerecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_overtimerecords_priority ON payroll_overtimerecords(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_overtimerecords_created_at ON payroll_overtimerecords(created_at);

-- Operational seed data fixtures for payroll_overtimerecords
INSERT OR IGNORE INTO payroll_overtimerecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OVE-0001", "Primary Operational OvertimeRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-overtimerecord-01"),
    (2, "OVE-0002", "Secondary Corporate OvertimeRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-overtimerecord-02"),
    (3, "OVE-0003", "Consolidated Branch OvertimeRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-overtimerecord-03"),
    (4, "OVE-0004", "Enterprise Audited OvertimeRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-overtimerecord-04"),
    (5, "OVE-0005", "Executive Strategic OvertimeRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-overtimerecord-05");

CREATE TABLE IF NOT EXISTS payroll_appraisalreviews (
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

CREATE INDEX IF NOT EXISTS idx_payroll_appraisalreviews_code ON payroll_appraisalreviews(code);
CREATE INDEX IF NOT EXISTS idx_payroll_appraisalreviews_org_status ON payroll_appraisalreviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_appraisalreviews_priority ON payroll_appraisalreviews(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_appraisalreviews_created_at ON payroll_appraisalreviews(created_at);

-- Operational seed data fixtures for payroll_appraisalreviews
INSERT OR IGNORE INTO payroll_appraisalreviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "APP-0001", "Primary Operational AppraisalReview 1", 24500.00, 150.0, "ACTIVE", "uuid-appraisalreview-01"),
    (2, "APP-0002", "Secondary Corporate AppraisalReview 2", 18200.50, 80.0, "ACTIVE", "uuid-appraisalreview-02"),
    (3, "APP-0003", "Consolidated Branch AppraisalReview 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-appraisalreview-03"),
    (4, "APP-0004", "Enterprise Audited AppraisalReview 4", 32800.00, 210.0, "ACTIVE", "uuid-appraisalreview-04"),
    (5, "APP-0005", "Executive Strategic AppraisalReview 5", 65000.00, 400.0, "ACTIVE", "uuid-appraisalreview-05");

CREATE TABLE IF NOT EXISTS payroll_skillcompetencys (
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

CREATE INDEX IF NOT EXISTS idx_payroll_skillcompetencys_code ON payroll_skillcompetencys(code);
CREATE INDEX IF NOT EXISTS idx_payroll_skillcompetencys_org_status ON payroll_skillcompetencys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_skillcompetencys_priority ON payroll_skillcompetencys(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_skillcompetencys_created_at ON payroll_skillcompetencys(created_at);

-- Operational seed data fixtures for payroll_skillcompetencys
INSERT OR IGNORE INTO payroll_skillcompetencys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SKI-0001", "Primary Operational SkillCompetency 1", 24500.00, 150.0, "ACTIVE", "uuid-skillcompetency-01"),
    (2, "SKI-0002", "Secondary Corporate SkillCompetency 2", 18200.50, 80.0, "ACTIVE", "uuid-skillcompetency-02"),
    (3, "SKI-0003", "Consolidated Branch SkillCompetency 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-skillcompetency-03"),
    (4, "SKI-0004", "Enterprise Audited SkillCompetency 4", 32800.00, 210.0, "ACTIVE", "uuid-skillcompetency-04"),
    (5, "SKI-0005", "Executive Strategic SkillCompetency 5", 65000.00, 400.0, "ACTIVE", "uuid-skillcompetency-05");

CREATE TABLE IF NOT EXISTS payroll_benefitplans (
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

CREATE INDEX IF NOT EXISTS idx_payroll_benefitplans_code ON payroll_benefitplans(code);
CREATE INDEX IF NOT EXISTS idx_payroll_benefitplans_org_status ON payroll_benefitplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_benefitplans_priority ON payroll_benefitplans(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_benefitplans_created_at ON payroll_benefitplans(created_at);

-- Operational seed data fixtures for payroll_benefitplans
INSERT OR IGNORE INTO payroll_benefitplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BEN-0001", "Primary Operational BenefitPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-benefitplan-01"),
    (2, "BEN-0002", "Secondary Corporate BenefitPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-benefitplan-02"),
    (3, "BEN-0003", "Consolidated Branch BenefitPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-benefitplan-03"),
    (4, "BEN-0004", "Enterprise Audited BenefitPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-benefitplan-04"),
    (5, "BEN-0005", "Executive Strategic BenefitPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-benefitplan-05");

CREATE TABLE IF NOT EXISTS payroll_fullfinalsettlements (
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

CREATE INDEX IF NOT EXISTS idx_payroll_fullfinalsettlements_code ON payroll_fullfinalsettlements(code);
CREATE INDEX IF NOT EXISTS idx_payroll_fullfinalsettlements_org_status ON payroll_fullfinalsettlements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_payroll_fullfinalsettlements_priority ON payroll_fullfinalsettlements(priority);
CREATE INDEX IF NOT EXISTS idx_payroll_fullfinalsettlements_created_at ON payroll_fullfinalsettlements(created_at);

-- Operational seed data fixtures for payroll_fullfinalsettlements
INSERT OR IGNORE INTO payroll_fullfinalsettlements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FUL-0001", "Primary Operational FullFinalSettlement 1", 24500.00, 150.0, "ACTIVE", "uuid-fullfinalsettlement-01"),
    (2, "FUL-0002", "Secondary Corporate FullFinalSettlement 2", 18200.50, 80.0, "ACTIVE", "uuid-fullfinalsettlement-02"),
    (3, "FUL-0003", "Consolidated Branch FullFinalSettlement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fullfinalsettlement-03"),
    (4, "FUL-0004", "Enterprise Audited FullFinalSettlement 4", 32800.00, 210.0, "ACTIVE", "uuid-fullfinalsettlement-04"),
    (5, "FUL-0005", "Executive Strategic FullFinalSettlement 5", 65000.00, 400.0, "ACTIVE", "uuid-fullfinalsettlement-05");

