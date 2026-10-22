-- SmartERP Enterprise Titan Migration 003: Corporate Treasury & Cash Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS treasury_bankaccounts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_bankaccounts_code ON treasury_bankaccounts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_bankaccounts_org_status ON treasury_bankaccounts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_bankaccounts_priority ON treasury_bankaccounts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_bankaccounts_created_at ON treasury_bankaccounts(created_at);

-- Operational seed data fixtures for treasury_bankaccounts
INSERT OR IGNORE INTO treasury_bankaccounts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BAN-0001", "Primary Operational BankAccount 1", 24500.00, 150.0, "ACTIVE", "uuid-bankaccount-01"),
    (2, "BAN-0002", "Secondary Corporate BankAccount 2", 18200.50, 80.0, "ACTIVE", "uuid-bankaccount-02"),
    (3, "BAN-0003", "Consolidated Branch BankAccount 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bankaccount-03"),
    (4, "BAN-0004", "Enterprise Audited BankAccount 4", 32800.00, 210.0, "ACTIVE", "uuid-bankaccount-04"),
    (5, "BAN-0005", "Executive Strategic BankAccount 5", 65000.00, 400.0, "ACTIVE", "uuid-bankaccount-05");

CREATE TABLE IF NOT EXISTS treasury_cashflowforecasts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_cashflowforecasts_code ON treasury_cashflowforecasts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_cashflowforecasts_org_status ON treasury_cashflowforecasts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_cashflowforecasts_priority ON treasury_cashflowforecasts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_cashflowforecasts_created_at ON treasury_cashflowforecasts(created_at);

-- Operational seed data fixtures for treasury_cashflowforecasts
INSERT OR IGNORE INTO treasury_cashflowforecasts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAS-0001", "Primary Operational CashFlowForecast 1", 24500.00, 150.0, "ACTIVE", "uuid-cashflowforecast-01"),
    (2, "CAS-0002", "Secondary Corporate CashFlowForecast 2", 18200.50, 80.0, "ACTIVE", "uuid-cashflowforecast-02"),
    (3, "CAS-0003", "Consolidated Branch CashFlowForecast 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cashflowforecast-03"),
    (4, "CAS-0004", "Enterprise Audited CashFlowForecast 4", 32800.00, 210.0, "ACTIVE", "uuid-cashflowforecast-04"),
    (5, "CAS-0005", "Executive Strategic CashFlowForecast 5", 65000.00, 400.0, "ACTIVE", "uuid-cashflowforecast-05");

CREATE TABLE IF NOT EXISTS treasury_exchangecontracts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_exchangecontracts_code ON treasury_exchangecontracts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_exchangecontracts_org_status ON treasury_exchangecontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_exchangecontracts_priority ON treasury_exchangecontracts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_exchangecontracts_created_at ON treasury_exchangecontracts(created_at);

-- Operational seed data fixtures for treasury_exchangecontracts
INSERT OR IGNORE INTO treasury_exchangecontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXC-0001", "Primary Operational ExchangeContract 1", 24500.00, 150.0, "ACTIVE", "uuid-exchangecontract-01"),
    (2, "EXC-0002", "Secondary Corporate ExchangeContract 2", 18200.50, 80.0, "ACTIVE", "uuid-exchangecontract-02"),
    (3, "EXC-0003", "Consolidated Branch ExchangeContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-exchangecontract-03"),
    (4, "EXC-0004", "Enterprise Audited ExchangeContract 4", 32800.00, 210.0, "ACTIVE", "uuid-exchangecontract-04"),
    (5, "EXC-0005", "Executive Strategic ExchangeContract 5", 65000.00, 400.0, "ACTIVE", "uuid-exchangecontract-05");

CREATE TABLE IF NOT EXISTS treasury_letterofcredits (
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

CREATE INDEX IF NOT EXISTS idx_treasury_letterofcredits_code ON treasury_letterofcredits(code);
CREATE INDEX IF NOT EXISTS idx_treasury_letterofcredits_org_status ON treasury_letterofcredits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_letterofcredits_priority ON treasury_letterofcredits(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_letterofcredits_created_at ON treasury_letterofcredits(created_at);

-- Operational seed data fixtures for treasury_letterofcredits
INSERT OR IGNORE INTO treasury_letterofcredits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LET-0001", "Primary Operational LetterOfCredit 1", 24500.00, 150.0, "ACTIVE", "uuid-letterofcredit-01"),
    (2, "LET-0002", "Secondary Corporate LetterOfCredit 2", 18200.50, 80.0, "ACTIVE", "uuid-letterofcredit-02"),
    (3, "LET-0003", "Consolidated Branch LetterOfCredit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-letterofcredit-03"),
    (4, "LET-0004", "Enterprise Audited LetterOfCredit 4", 32800.00, 210.0, "ACTIVE", "uuid-letterofcredit-04"),
    (5, "LET-0005", "Executive Strategic LetterOfCredit 5", 65000.00, 400.0, "ACTIVE", "uuid-letterofcredit-05");

CREATE TABLE IF NOT EXISTS treasury_bankguarantees (
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

CREATE INDEX IF NOT EXISTS idx_treasury_bankguarantees_code ON treasury_bankguarantees(code);
CREATE INDEX IF NOT EXISTS idx_treasury_bankguarantees_org_status ON treasury_bankguarantees(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_bankguarantees_priority ON treasury_bankguarantees(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_bankguarantees_created_at ON treasury_bankguarantees(created_at);

-- Operational seed data fixtures for treasury_bankguarantees
INSERT OR IGNORE INTO treasury_bankguarantees (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BAN-0001", "Primary Operational BankGuarantee 1", 24500.00, 150.0, "ACTIVE", "uuid-bankguarantee-01"),
    (2, "BAN-0002", "Secondary Corporate BankGuarantee 2", 18200.50, 80.0, "ACTIVE", "uuid-bankguarantee-02"),
    (3, "BAN-0003", "Consolidated Branch BankGuarantee 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bankguarantee-03"),
    (4, "BAN-0004", "Enterprise Audited BankGuarantee 4", 32800.00, 210.0, "ACTIVE", "uuid-bankguarantee-04"),
    (5, "BAN-0005", "Executive Strategic BankGuarantee 5", 65000.00, 400.0, "ACTIVE", "uuid-bankguarantee-05");

CREATE TABLE IF NOT EXISTS treasury_investmentsecuritys (
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

CREATE INDEX IF NOT EXISTS idx_treasury_investmentsecuritys_code ON treasury_investmentsecuritys(code);
CREATE INDEX IF NOT EXISTS idx_treasury_investmentsecuritys_org_status ON treasury_investmentsecuritys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_investmentsecuritys_priority ON treasury_investmentsecuritys(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_investmentsecuritys_created_at ON treasury_investmentsecuritys(created_at);

-- Operational seed data fixtures for treasury_investmentsecuritys
INSERT OR IGNORE INTO treasury_investmentsecuritys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INV-0001", "Primary Operational InvestmentSecurity 1", 24500.00, 150.0, "ACTIVE", "uuid-investmentsecurity-01"),
    (2, "INV-0002", "Secondary Corporate InvestmentSecurity 2", 18200.50, 80.0, "ACTIVE", "uuid-investmentsecurity-02"),
    (3, "INV-0003", "Consolidated Branch InvestmentSecurity 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-investmentsecurity-03"),
    (4, "INV-0004", "Enterprise Audited InvestmentSecurity 4", 32800.00, 210.0, "ACTIVE", "uuid-investmentsecurity-04"),
    (5, "INV-0005", "Executive Strategic InvestmentSecurity 5", 65000.00, 400.0, "ACTIVE", "uuid-investmentsecurity-05");

CREATE TABLE IF NOT EXISTS treasury_loanfacilitys (
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

CREATE INDEX IF NOT EXISTS idx_treasury_loanfacilitys_code ON treasury_loanfacilitys(code);
CREATE INDEX IF NOT EXISTS idx_treasury_loanfacilitys_org_status ON treasury_loanfacilitys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_loanfacilitys_priority ON treasury_loanfacilitys(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_loanfacilitys_created_at ON treasury_loanfacilitys(created_at);

-- Operational seed data fixtures for treasury_loanfacilitys
INSERT OR IGNORE INTO treasury_loanfacilitys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LOA-0001", "Primary Operational LoanFacility 1", 24500.00, 150.0, "ACTIVE", "uuid-loanfacility-01"),
    (2, "LOA-0002", "Secondary Corporate LoanFacility 2", 18200.50, 80.0, "ACTIVE", "uuid-loanfacility-02"),
    (3, "LOA-0003", "Consolidated Branch LoanFacility 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-loanfacility-03"),
    (4, "LOA-0004", "Enterprise Audited LoanFacility 4", 32800.00, 210.0, "ACTIVE", "uuid-loanfacility-04"),
    (5, "LOA-0005", "Executive Strategic LoanFacility 5", 65000.00, 400.0, "ACTIVE", "uuid-loanfacility-05");

CREATE TABLE IF NOT EXISTS treasury_interestaccruals (
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

CREATE INDEX IF NOT EXISTS idx_treasury_interestaccruals_code ON treasury_interestaccruals(code);
CREATE INDEX IF NOT EXISTS idx_treasury_interestaccruals_org_status ON treasury_interestaccruals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_interestaccruals_priority ON treasury_interestaccruals(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_interestaccruals_created_at ON treasury_interestaccruals(created_at);

-- Operational seed data fixtures for treasury_interestaccruals
INSERT OR IGNORE INTO treasury_interestaccruals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INT-0001", "Primary Operational InterestAccrual 1", 24500.00, 150.0, "ACTIVE", "uuid-interestaccrual-01"),
    (2, "INT-0002", "Secondary Corporate InterestAccrual 2", 18200.50, 80.0, "ACTIVE", "uuid-interestaccrual-02"),
    (3, "INT-0003", "Consolidated Branch InterestAccrual 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-interestaccrual-03"),
    (4, "INT-0004", "Enterprise Audited InterestAccrual 4", 32800.00, 210.0, "ACTIVE", "uuid-interestaccrual-04"),
    (5, "INT-0005", "Executive Strategic InterestAccrual 5", 65000.00, 400.0, "ACTIVE", "uuid-interestaccrual-05");

CREATE TABLE IF NOT EXISTS treasury_liquiditypools (
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

CREATE INDEX IF NOT EXISTS idx_treasury_liquiditypools_code ON treasury_liquiditypools(code);
CREATE INDEX IF NOT EXISTS idx_treasury_liquiditypools_org_status ON treasury_liquiditypools(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_liquiditypools_priority ON treasury_liquiditypools(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_liquiditypools_created_at ON treasury_liquiditypools(created_at);

-- Operational seed data fixtures for treasury_liquiditypools
INSERT OR IGNORE INTO treasury_liquiditypools (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LIQ-0001", "Primary Operational LiquidityPool 1", 24500.00, 150.0, "ACTIVE", "uuid-liquiditypool-01"),
    (2, "LIQ-0002", "Secondary Corporate LiquidityPool 2", 18200.50, 80.0, "ACTIVE", "uuid-liquiditypool-02"),
    (3, "LIQ-0003", "Consolidated Branch LiquidityPool 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-liquiditypool-03"),
    (4, "LIQ-0004", "Enterprise Audited LiquidityPool 4", 32800.00, 210.0, "ACTIVE", "uuid-liquiditypool-04"),
    (5, "LIQ-0005", "Executive Strategic LiquidityPool 5", 65000.00, 400.0, "ACTIVE", "uuid-liquiditypool-05");

CREATE TABLE IF NOT EXISTS treasury_treasurydeals (
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

CREATE INDEX IF NOT EXISTS idx_treasury_treasurydeals_code ON treasury_treasurydeals(code);
CREATE INDEX IF NOT EXISTS idx_treasury_treasurydeals_org_status ON treasury_treasurydeals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_treasurydeals_priority ON treasury_treasurydeals(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_treasurydeals_created_at ON treasury_treasurydeals(created_at);

-- Operational seed data fixtures for treasury_treasurydeals
INSERT OR IGNORE INTO treasury_treasurydeals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRE-0001", "Primary Operational TreasuryDeal 1", 24500.00, 150.0, "ACTIVE", "uuid-treasurydeal-01"),
    (2, "TRE-0002", "Secondary Corporate TreasuryDeal 2", 18200.50, 80.0, "ACTIVE", "uuid-treasurydeal-02"),
    (3, "TRE-0003", "Consolidated Branch TreasuryDeal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-treasurydeal-03"),
    (4, "TRE-0004", "Enterprise Audited TreasuryDeal 4", 32800.00, 210.0, "ACTIVE", "uuid-treasurydeal-04"),
    (5, "TRE-0005", "Executive Strategic TreasuryDeal 5", 65000.00, 400.0, "ACTIVE", "uuid-treasurydeal-05");

CREATE TABLE IF NOT EXISTS treasury_hedgingcontracts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_hedgingcontracts_code ON treasury_hedgingcontracts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_hedgingcontracts_org_status ON treasury_hedgingcontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_hedgingcontracts_priority ON treasury_hedgingcontracts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_hedgingcontracts_created_at ON treasury_hedgingcontracts(created_at);

-- Operational seed data fixtures for treasury_hedgingcontracts
INSERT OR IGNORE INTO treasury_hedgingcontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HED-0001", "Primary Operational HedgingContract 1", 24500.00, 150.0, "ACTIVE", "uuid-hedgingcontract-01"),
    (2, "HED-0002", "Secondary Corporate HedgingContract 2", 18200.50, 80.0, "ACTIVE", "uuid-hedgingcontract-02"),
    (3, "HED-0003", "Consolidated Branch HedgingContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hedgingcontract-03"),
    (4, "HED-0004", "Enterprise Audited HedgingContract 4", 32800.00, 210.0, "ACTIVE", "uuid-hedgingcontract-04"),
    (5, "HED-0005", "Executive Strategic HedgingContract 5", 65000.00, 400.0, "ACTIVE", "uuid-hedgingcontract-05");

CREATE TABLE IF NOT EXISTS treasury_sweeprules (
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

CREATE INDEX IF NOT EXISTS idx_treasury_sweeprules_code ON treasury_sweeprules(code);
CREATE INDEX IF NOT EXISTS idx_treasury_sweeprules_org_status ON treasury_sweeprules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_sweeprules_priority ON treasury_sweeprules(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_sweeprules_created_at ON treasury_sweeprules(created_at);

-- Operational seed data fixtures for treasury_sweeprules
INSERT OR IGNORE INTO treasury_sweeprules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SWE-0001", "Primary Operational SweepRule 1", 24500.00, 150.0, "ACTIVE", "uuid-sweeprule-01"),
    (2, "SWE-0002", "Secondary Corporate SweepRule 2", 18200.50, 80.0, "ACTIVE", "uuid-sweeprule-02"),
    (3, "SWE-0003", "Consolidated Branch SweepRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sweeprule-03"),
    (4, "SWE-0004", "Enterprise Audited SweepRule 4", 32800.00, 210.0, "ACTIVE", "uuid-sweeprule-04"),
    (5, "SWE-0005", "Executive Strategic SweepRule 5", 65000.00, 400.0, "ACTIVE", "uuid-sweeprule-05");

CREATE TABLE IF NOT EXISTS treasury_counterpartylimits (
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

CREATE INDEX IF NOT EXISTS idx_treasury_counterpartylimits_code ON treasury_counterpartylimits(code);
CREATE INDEX IF NOT EXISTS idx_treasury_counterpartylimits_org_status ON treasury_counterpartylimits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_counterpartylimits_priority ON treasury_counterpartylimits(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_counterpartylimits_created_at ON treasury_counterpartylimits(created_at);

-- Operational seed data fixtures for treasury_counterpartylimits
INSERT OR IGNORE INTO treasury_counterpartylimits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COU-0001", "Primary Operational CounterpartyLimit 1", 24500.00, 150.0, "ACTIVE", "uuid-counterpartylimit-01"),
    (2, "COU-0002", "Secondary Corporate CounterpartyLimit 2", 18200.50, 80.0, "ACTIVE", "uuid-counterpartylimit-02"),
    (3, "COU-0003", "Consolidated Branch CounterpartyLimit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-counterpartylimit-03"),
    (4, "COU-0004", "Enterprise Audited CounterpartyLimit 4", 32800.00, 210.0, "ACTIVE", "uuid-counterpartylimit-04"),
    (5, "COU-0005", "Executive Strategic CounterpartyLimit 5", 65000.00, 400.0, "ACTIVE", "uuid-counterpartylimit-05");

CREATE TABLE IF NOT EXISTS treasury_dividendrecords (
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

CREATE INDEX IF NOT EXISTS idx_treasury_dividendrecords_code ON treasury_dividendrecords(code);
CREATE INDEX IF NOT EXISTS idx_treasury_dividendrecords_org_status ON treasury_dividendrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_dividendrecords_priority ON treasury_dividendrecords(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_dividendrecords_created_at ON treasury_dividendrecords(created_at);

-- Operational seed data fixtures for treasury_dividendrecords
INSERT OR IGNORE INTO treasury_dividendrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIV-0001", "Primary Operational DividendRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-dividendrecord-01"),
    (2, "DIV-0002", "Secondary Corporate DividendRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-dividendrecord-02"),
    (3, "DIV-0003", "Consolidated Branch DividendRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dividendrecord-03"),
    (4, "DIV-0004", "Enterprise Audited DividendRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-dividendrecord-04"),
    (5, "DIV-0005", "Executive Strategic DividendRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-dividendrecord-05");

CREATE TABLE IF NOT EXISTS treasury_leasecontracts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_leasecontracts_code ON treasury_leasecontracts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_leasecontracts_org_status ON treasury_leasecontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_leasecontracts_priority ON treasury_leasecontracts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_leasecontracts_created_at ON treasury_leasecontracts(created_at);

-- Operational seed data fixtures for treasury_leasecontracts
INSERT OR IGNORE INTO treasury_leasecontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeaseContract 1", 24500.00, 150.0, "ACTIVE", "uuid-leasecontract-01"),
    (2, "LEA-0002", "Secondary Corporate LeaseContract 2", 18200.50, 80.0, "ACTIVE", "uuid-leasecontract-02"),
    (3, "LEA-0003", "Consolidated Branch LeaseContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leasecontract-03"),
    (4, "LEA-0004", "Enterprise Audited LeaseContract 4", 32800.00, 210.0, "ACTIVE", "uuid-leasecontract-04"),
    (5, "LEA-0005", "Executive Strategic LeaseContract 5", 65000.00, 400.0, "ACTIVE", "uuid-leasecontract-05");

CREATE TABLE IF NOT EXISTS treasury_financialratios (
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

CREATE INDEX IF NOT EXISTS idx_treasury_financialratios_code ON treasury_financialratios(code);
CREATE INDEX IF NOT EXISTS idx_treasury_financialratios_org_status ON treasury_financialratios(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_financialratios_priority ON treasury_financialratios(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_financialratios_created_at ON treasury_financialratios(created_at);

-- Operational seed data fixtures for treasury_financialratios
INSERT OR IGNORE INTO treasury_financialratios (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FIN-0001", "Primary Operational FinancialRatio 1", 24500.00, 150.0, "ACTIVE", "uuid-financialratio-01"),
    (2, "FIN-0002", "Secondary Corporate FinancialRatio 2", 18200.50, 80.0, "ACTIVE", "uuid-financialratio-02"),
    (3, "FIN-0003", "Consolidated Branch FinancialRatio 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-financialratio-03"),
    (4, "FIN-0004", "Enterprise Audited FinancialRatio 4", 32800.00, 210.0, "ACTIVE", "uuid-financialratio-04"),
    (5, "FIN-0005", "Executive Strategic FinancialRatio 5", 65000.00, 400.0, "ACTIVE", "uuid-financialratio-05");

