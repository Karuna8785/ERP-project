-- SmartERP Enterprise Titan Migration 039: Executive Compensation & Equity (ESOP) Engine DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS compensation_equity_equityplanschemes (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityplanschemes_code ON compensation_equity_equityplanschemes(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityplanschemes_org_status ON compensation_equity_equityplanschemes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityplanschemes_priority ON compensation_equity_equityplanschemes(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityplanschemes_created_at ON compensation_equity_equityplanschemes(created_at);

-- Operational seed data fixtures for compensation_equity_equityplanschemes
INSERT OR IGNORE INTO compensation_equity_equityplanschemes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EQU-0001", "Primary Operational EquityPlanScheme 1", 24500.00, 150.0, "ACTIVE", "uuid-equityplanscheme-01"),
    (2, "EQU-0002", "Secondary Corporate EquityPlanScheme 2", 18200.50, 80.0, "ACTIVE", "uuid-equityplanscheme-02"),
    (3, "EQU-0003", "Consolidated Branch EquityPlanScheme 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-equityplanscheme-03"),
    (4, "EQU-0004", "Enterprise Audited EquityPlanScheme 4", 32800.00, 210.0, "ACTIVE", "uuid-equityplanscheme-04"),
    (5, "EQU-0005", "Executive Strategic EquityPlanScheme 5", 65000.00, 400.0, "ACTIVE", "uuid-equityplanscheme-05");

CREATE TABLE IF NOT EXISTS compensation_equity_optiongrantagreements (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_optiongrantagreements_code ON compensation_equity_optiongrantagreements(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_optiongrantagreements_org_status ON compensation_equity_optiongrantagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_optiongrantagreements_priority ON compensation_equity_optiongrantagreements(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_optiongrantagreements_created_at ON compensation_equity_optiongrantagreements(created_at);

-- Operational seed data fixtures for compensation_equity_optiongrantagreements
INSERT OR IGNORE INTO compensation_equity_optiongrantagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OPT-0001", "Primary Operational OptionGrantAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-optiongrantagreement-01"),
    (2, "OPT-0002", "Secondary Corporate OptionGrantAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-optiongrantagreement-02"),
    (3, "OPT-0003", "Consolidated Branch OptionGrantAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-optiongrantagreement-03"),
    (4, "OPT-0004", "Enterprise Audited OptionGrantAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-optiongrantagreement-04"),
    (5, "OPT-0005", "Executive Strategic OptionGrantAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-optiongrantagreement-05");

CREATE TABLE IF NOT EXISTS compensation_equity_vestingschedulerules (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_vestingschedulerules_code ON compensation_equity_vestingschedulerules(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_vestingschedulerules_org_status ON compensation_equity_vestingschedulerules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_vestingschedulerules_priority ON compensation_equity_vestingschedulerules(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_vestingschedulerules_created_at ON compensation_equity_vestingschedulerules(created_at);

-- Operational seed data fixtures for compensation_equity_vestingschedulerules
INSERT OR IGNORE INTO compensation_equity_vestingschedulerules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VES-0001", "Primary Operational VestingScheduleRule 1", 24500.00, 150.0, "ACTIVE", "uuid-vestingschedulerule-01"),
    (2, "VES-0002", "Secondary Corporate VestingScheduleRule 2", 18200.50, 80.0, "ACTIVE", "uuid-vestingschedulerule-02"),
    (3, "VES-0003", "Consolidated Branch VestingScheduleRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vestingschedulerule-03"),
    (4, "VES-0004", "Enterprise Audited VestingScheduleRule 4", 32800.00, 210.0, "ACTIVE", "uuid-vestingschedulerule-04"),
    (5, "VES-0005", "Executive Strategic VestingScheduleRule 5", 65000.00, 400.0, "ACTIVE", "uuid-vestingschedulerule-05");

CREATE TABLE IF NOT EXISTS compensation_equity_exercisenoticeorders (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_exercisenoticeorders_code ON compensation_equity_exercisenoticeorders(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_exercisenoticeorders_org_status ON compensation_equity_exercisenoticeorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_exercisenoticeorders_priority ON compensation_equity_exercisenoticeorders(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_exercisenoticeorders_created_at ON compensation_equity_exercisenoticeorders(created_at);

-- Operational seed data fixtures for compensation_equity_exercisenoticeorders
INSERT OR IGNORE INTO compensation_equity_exercisenoticeorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExerciseNoticeOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-exercisenoticeorder-01"),
    (2, "EXE-0002", "Secondary Corporate ExerciseNoticeOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-exercisenoticeorder-02"),
    (3, "EXE-0003", "Consolidated Branch ExerciseNoticeOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-exercisenoticeorder-03"),
    (4, "EXE-0004", "Enterprise Audited ExerciseNoticeOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-exercisenoticeorder-04"),
    (5, "EXE-0005", "Executive Strategic ExerciseNoticeOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-exercisenoticeorder-05");

CREATE TABLE IF NOT EXISTS compensation_equity_captableshareholders (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_captableshareholders_code ON compensation_equity_captableshareholders(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_captableshareholders_org_status ON compensation_equity_captableshareholders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_captableshareholders_priority ON compensation_equity_captableshareholders(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_captableshareholders_created_at ON compensation_equity_captableshareholders(created_at);

-- Operational seed data fixtures for compensation_equity_captableshareholders
INSERT OR IGNORE INTO compensation_equity_captableshareholders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAP-0001", "Primary Operational CapTableShareholder 1", 24500.00, 150.0, "ACTIVE", "uuid-captableshareholder-01"),
    (2, "CAP-0002", "Secondary Corporate CapTableShareholder 2", 18200.50, 80.0, "ACTIVE", "uuid-captableshareholder-02"),
    (3, "CAP-0003", "Consolidated Branch CapTableShareholder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-captableshareholder-03"),
    (4, "CAP-0004", "Enterprise Audited CapTableShareholder 4", 32800.00, 210.0, "ACTIVE", "uuid-captableshareholder-04"),
    (5, "CAP-0005", "Executive Strategic CapTableShareholder 5", 65000.00, 400.0, "ACTIVE", "uuid-captableshareholder-05");

CREATE TABLE IF NOT EXISTS compensation_equity_sharerepurchasebuybacks (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_sharerepurchasebuybacks_code ON compensation_equity_sharerepurchasebuybacks(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_sharerepurchasebuybacks_org_status ON compensation_equity_sharerepurchasebuybacks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_sharerepurchasebuybacks_priority ON compensation_equity_sharerepurchasebuybacks(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_sharerepurchasebuybacks_created_at ON compensation_equity_sharerepurchasebuybacks(created_at);

-- Operational seed data fixtures for compensation_equity_sharerepurchasebuybacks
INSERT OR IGNORE INTO compensation_equity_sharerepurchasebuybacks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHA-0001", "Primary Operational ShareRepurchaseBuyback 1", 24500.00, 150.0, "ACTIVE", "uuid-sharerepurchasebuyback-01"),
    (2, "SHA-0002", "Secondary Corporate ShareRepurchaseBuyback 2", 18200.50, 80.0, "ACTIVE", "uuid-sharerepurchasebuyback-02"),
    (3, "SHA-0003", "Consolidated Branch ShareRepurchaseBuyback 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sharerepurchasebuyback-03"),
    (4, "SHA-0004", "Enterprise Audited ShareRepurchaseBuyback 4", 32800.00, 210.0, "ACTIVE", "uuid-sharerepurchasebuyback-04"),
    (5, "SHA-0005", "Executive Strategic ShareRepurchaseBuyback 5", 65000.00, 400.0, "ACTIVE", "uuid-sharerepurchasebuyback-05");

CREATE TABLE IF NOT EXISTS compensation_equity_annualbonuspools (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_annualbonuspools_code ON compensation_equity_annualbonuspools(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_annualbonuspools_org_status ON compensation_equity_annualbonuspools(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_annualbonuspools_priority ON compensation_equity_annualbonuspools(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_annualbonuspools_created_at ON compensation_equity_annualbonuspools(created_at);

-- Operational seed data fixtures for compensation_equity_annualbonuspools
INSERT OR IGNORE INTO compensation_equity_annualbonuspools (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ANN-0001", "Primary Operational AnnualBonusPool 1", 24500.00, 150.0, "ACTIVE", "uuid-annualbonuspool-01"),
    (2, "ANN-0002", "Secondary Corporate AnnualBonusPool 2", 18200.50, 80.0, "ACTIVE", "uuid-annualbonuspool-02"),
    (3, "ANN-0003", "Consolidated Branch AnnualBonusPool 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-annualbonuspool-03"),
    (4, "ANN-0004", "Enterprise Audited AnnualBonusPool 4", 32800.00, 210.0, "ACTIVE", "uuid-annualbonuspool-04"),
    (5, "ANN-0005", "Executive Strategic AnnualBonusPool 5", 65000.00, 400.0, "ACTIVE", "uuid-annualbonuspool-05");

CREATE TABLE IF NOT EXISTS compensation_equity_longtermincentiveplans (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_longtermincentiveplans_code ON compensation_equity_longtermincentiveplans(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_longtermincentiveplans_org_status ON compensation_equity_longtermincentiveplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_longtermincentiveplans_priority ON compensation_equity_longtermincentiveplans(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_longtermincentiveplans_created_at ON compensation_equity_longtermincentiveplans(created_at);

-- Operational seed data fixtures for compensation_equity_longtermincentiveplans
INSERT OR IGNORE INTO compensation_equity_longtermincentiveplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LON-0001", "Primary Operational LongTermIncentivePlan 1", 24500.00, 150.0, "ACTIVE", "uuid-longtermincentiveplan-01"),
    (2, "LON-0002", "Secondary Corporate LongTermIncentivePlan 2", 18200.50, 80.0, "ACTIVE", "uuid-longtermincentiveplan-02"),
    (3, "LON-0003", "Consolidated Branch LongTermIncentivePlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-longtermincentiveplan-03"),
    (4, "LON-0004", "Enterprise Audited LongTermIncentivePlan 4", 32800.00, 210.0, "ACTIVE", "uuid-longtermincentiveplan-04"),
    (5, "LON-0005", "Executive Strategic LongTermIncentivePlan 5", 65000.00, 400.0, "ACTIVE", "uuid-longtermincentiveplan-05");

CREATE TABLE IF NOT EXISTS compensation_equity_salarybenchmarksurveys (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_salarybenchmarksurveys_code ON compensation_equity_salarybenchmarksurveys(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_salarybenchmarksurveys_org_status ON compensation_equity_salarybenchmarksurveys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_salarybenchmarksurveys_priority ON compensation_equity_salarybenchmarksurveys(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_salarybenchmarksurveys_created_at ON compensation_equity_salarybenchmarksurveys(created_at);

-- Operational seed data fixtures for compensation_equity_salarybenchmarksurveys
INSERT OR IGNORE INTO compensation_equity_salarybenchmarksurveys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAL-0001", "Primary Operational SalaryBenchmarkSurvey 1", 24500.00, 150.0, "ACTIVE", "uuid-salarybenchmarksurvey-01"),
    (2, "SAL-0002", "Secondary Corporate SalaryBenchmarkSurvey 2", 18200.50, 80.0, "ACTIVE", "uuid-salarybenchmarksurvey-02"),
    (3, "SAL-0003", "Consolidated Branch SalaryBenchmarkSurvey 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-salarybenchmarksurvey-03"),
    (4, "SAL-0004", "Enterprise Audited SalaryBenchmarkSurvey 4", 32800.00, 210.0, "ACTIVE", "uuid-salarybenchmarksurvey-04"),
    (5, "SAL-0005", "Executive Strategic SalaryBenchmarkSurvey 5", 65000.00, 400.0, "ACTIVE", "uuid-salarybenchmarksurvey-05");

CREATE TABLE IF NOT EXISTS compensation_equity_fairmarketvaluation409as (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_fairmarketvaluation409as_code ON compensation_equity_fairmarketvaluation409as(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_fairmarketvaluation409as_org_status ON compensation_equity_fairmarketvaluation409as(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_fairmarketvaluation409as_priority ON compensation_equity_fairmarketvaluation409as(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_fairmarketvaluation409as_created_at ON compensation_equity_fairmarketvaluation409as(created_at);

-- Operational seed data fixtures for compensation_equity_fairmarketvaluation409as
INSERT OR IGNORE INTO compensation_equity_fairmarketvaluation409as (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FAI-0001", "Primary Operational FairMarketValuation409A 1", 24500.00, 150.0, "ACTIVE", "uuid-fairmarketvaluation409a-01"),
    (2, "FAI-0002", "Secondary Corporate FairMarketValuation409A 2", 18200.50, 80.0, "ACTIVE", "uuid-fairmarketvaluation409a-02"),
    (3, "FAI-0003", "Consolidated Branch FairMarketValuation409A 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fairmarketvaluation409a-03"),
    (4, "FAI-0004", "Enterprise Audited FairMarketValuation409A 4", 32800.00, 210.0, "ACTIVE", "uuid-fairmarketvaluation409a-04"),
    (5, "FAI-0005", "Executive Strategic FairMarketValuation409A 5", 65000.00, 400.0, "ACTIVE", "uuid-fairmarketvaluation409a-05");

CREATE TABLE IF NOT EXISTS compensation_equity_dividendsdistributions (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_dividendsdistributions_code ON compensation_equity_dividendsdistributions(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_dividendsdistributions_org_status ON compensation_equity_dividendsdistributions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_dividendsdistributions_priority ON compensation_equity_dividendsdistributions(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_dividendsdistributions_created_at ON compensation_equity_dividendsdistributions(created_at);

-- Operational seed data fixtures for compensation_equity_dividendsdistributions
INSERT OR IGNORE INTO compensation_equity_dividendsdistributions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIV-0001", "Primary Operational DividendsDistribution 1", 24500.00, 150.0, "ACTIVE", "uuid-dividendsdistribution-01"),
    (2, "DIV-0002", "Secondary Corporate DividendsDistribution 2", 18200.50, 80.0, "ACTIVE", "uuid-dividendsdistribution-02"),
    (3, "DIV-0003", "Consolidated Branch DividendsDistribution 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dividendsdistribution-03"),
    (4, "DIV-0004", "Enterprise Audited DividendsDistribution 4", 32800.00, 210.0, "ACTIVE", "uuid-dividendsdistribution-04"),
    (5, "DIV-0005", "Executive Strategic DividendsDistribution 5", 65000.00, 400.0, "ACTIVE", "uuid-dividendsdistribution-05");

CREATE TABLE IF NOT EXISTS compensation_equity_stockoptioncancellations (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_stockoptioncancellations_code ON compensation_equity_stockoptioncancellations(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_stockoptioncancellations_org_status ON compensation_equity_stockoptioncancellations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_stockoptioncancellations_priority ON compensation_equity_stockoptioncancellations(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_stockoptioncancellations_created_at ON compensation_equity_stockoptioncancellations(created_at);

-- Operational seed data fixtures for compensation_equity_stockoptioncancellations
INSERT OR IGNORE INTO compensation_equity_stockoptioncancellations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STO-0001", "Primary Operational StockOptionCancellation 1", 24500.00, 150.0, "ACTIVE", "uuid-stockoptioncancellation-01"),
    (2, "STO-0002", "Secondary Corporate StockOptionCancellation 2", 18200.50, 80.0, "ACTIVE", "uuid-stockoptioncancellation-02"),
    (3, "STO-0003", "Consolidated Branch StockOptionCancellation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-stockoptioncancellation-03"),
    (4, "STO-0004", "Enterprise Audited StockOptionCancellation 4", 32800.00, 210.0, "ACTIVE", "uuid-stockoptioncancellation-04"),
    (5, "STO-0005", "Executive Strategic StockOptionCancellation 5", 65000.00, 400.0, "ACTIVE", "uuid-stockoptioncancellation-05");

CREATE TABLE IF NOT EXISTS compensation_equity_form16statutoryfilings (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_form16statutoryfilings_code ON compensation_equity_form16statutoryfilings(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_form16statutoryfilings_org_status ON compensation_equity_form16statutoryfilings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_form16statutoryfilings_priority ON compensation_equity_form16statutoryfilings(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_form16statutoryfilings_created_at ON compensation_equity_form16statutoryfilings(created_at);

-- Operational seed data fixtures for compensation_equity_form16statutoryfilings
INSERT OR IGNORE INTO compensation_equity_form16statutoryfilings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FOR-0001", "Primary Operational Form16StatutoryFiling 1", 24500.00, 150.0, "ACTIVE", "uuid-form16statutoryfiling-01"),
    (2, "FOR-0002", "Secondary Corporate Form16StatutoryFiling 2", 18200.50, 80.0, "ACTIVE", "uuid-form16statutoryfiling-02"),
    (3, "FOR-0003", "Consolidated Branch Form16StatutoryFiling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-form16statutoryfiling-03"),
    (4, "FOR-0004", "Enterprise Audited Form16StatutoryFiling 4", 32800.00, 210.0, "ACTIVE", "uuid-form16statutoryfiling-04"),
    (5, "FOR-0005", "Executive Strategic Form16StatutoryFiling 5", 65000.00, 400.0, "ACTIVE", "uuid-form16statutoryfiling-05");

CREATE TABLE IF NOT EXISTS compensation_equity_executiveperformancescores (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_executiveperformancescores_code ON compensation_equity_executiveperformancescores(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_executiveperformancescores_org_status ON compensation_equity_executiveperformancescores(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_executiveperformancescores_priority ON compensation_equity_executiveperformancescores(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_executiveperformancescores_created_at ON compensation_equity_executiveperformancescores(created_at);

-- Operational seed data fixtures for compensation_equity_executiveperformancescores
INSERT OR IGNORE INTO compensation_equity_executiveperformancescores (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutivePerformanceScore 1", 24500.00, 150.0, "ACTIVE", "uuid-executiveperformancescore-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutivePerformanceScore 2", 18200.50, 80.0, "ACTIVE", "uuid-executiveperformancescore-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutivePerformanceScore 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executiveperformancescore-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutivePerformanceScore 4", 32800.00, 210.0, "ACTIVE", "uuid-executiveperformancescore-04"),
    (5, "EXE-0005", "Executive Strategic ExecutivePerformanceScore 5", 65000.00, 400.0, "ACTIVE", "uuid-executiveperformancescore-05");

CREATE TABLE IF NOT EXISTS compensation_equity_equityclawbackrules (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityclawbackrules_code ON compensation_equity_equityclawbackrules(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityclawbackrules_org_status ON compensation_equity_equityclawbackrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityclawbackrules_priority ON compensation_equity_equityclawbackrules(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_equityclawbackrules_created_at ON compensation_equity_equityclawbackrules(created_at);

-- Operational seed data fixtures for compensation_equity_equityclawbackrules
INSERT OR IGNORE INTO compensation_equity_equityclawbackrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EQU-0001", "Primary Operational EquityClawbackRule 1", 24500.00, 150.0, "ACTIVE", "uuid-equityclawbackrule-01"),
    (2, "EQU-0002", "Secondary Corporate EquityClawbackRule 2", 18200.50, 80.0, "ACTIVE", "uuid-equityclawbackrule-02"),
    (3, "EQU-0003", "Consolidated Branch EquityClawbackRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-equityclawbackrule-03"),
    (4, "EQU-0004", "Enterprise Audited EquityClawbackRule 4", 32800.00, 210.0, "ACTIVE", "uuid-equityclawbackrule-04"),
    (5, "EQU-0005", "Executive Strategic EquityClawbackRule 5", 65000.00, 400.0, "ACTIVE", "uuid-equityclawbackrule-05");

CREATE TABLE IF NOT EXISTS compensation_equity_secondarysalewindows (
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

CREATE INDEX IF NOT EXISTS idx_compensation_equity_secondarysalewindows_code ON compensation_equity_secondarysalewindows(code);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_secondarysalewindows_org_status ON compensation_equity_secondarysalewindows(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_secondarysalewindows_priority ON compensation_equity_secondarysalewindows(priority);
CREATE INDEX IF NOT EXISTS idx_compensation_equity_secondarysalewindows_created_at ON compensation_equity_secondarysalewindows(created_at);

-- Operational seed data fixtures for compensation_equity_secondarysalewindows
INSERT OR IGNORE INTO compensation_equity_secondarysalewindows (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEC-0001", "Primary Operational SecondarySaleWindow 1", 24500.00, 150.0, "ACTIVE", "uuid-secondarysalewindow-01"),
    (2, "SEC-0002", "Secondary Corporate SecondarySaleWindow 2", 18200.50, 80.0, "ACTIVE", "uuid-secondarysalewindow-02"),
    (3, "SEC-0003", "Consolidated Branch SecondarySaleWindow 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-secondarysalewindow-03"),
    (4, "SEC-0004", "Enterprise Audited SecondarySaleWindow 4", 32800.00, 210.0, "ACTIVE", "uuid-secondarysalewindow-04"),
    (5, "SEC-0005", "Executive Strategic SecondarySaleWindow 5", 65000.00, 400.0, "ACTIVE", "uuid-secondarysalewindow-05");

