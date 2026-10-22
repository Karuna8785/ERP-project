-- SmartERP Enterprise Titan Migration 050: Multi-Entity Financial Consolidation & Reporting DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS financial_consolidation_consolidationentitygroups (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidationentitygroups_code ON financial_consolidation_consolidationentitygroups(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidationentitygroups_org_status ON financial_consolidation_consolidationentitygroups(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidationentitygroups_priority ON financial_consolidation_consolidationentitygroups(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidationentitygroups_created_at ON financial_consolidation_consolidationentitygroups(created_at);

-- Operational seed data fixtures for financial_consolidation_consolidationentitygroups
INSERT OR IGNORE INTO financial_consolidation_consolidationentitygroups (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ConsolidationEntityGroup 1", 24500.00, 150.0, "ACTIVE", "uuid-consolidationentitygroup-01"),
    (2, "CON-0002", "Secondary Corporate ConsolidationEntityGroup 2", 18200.50, 80.0, "ACTIVE", "uuid-consolidationentitygroup-02"),
    (3, "CON-0003", "Consolidated Branch ConsolidationEntityGroup 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-consolidationentitygroup-03"),
    (4, "CON-0004", "Enterprise Audited ConsolidationEntityGroup 4", 32800.00, 210.0, "ACTIVE", "uuid-consolidationentitygroup-04"),
    (5, "CON-0005", "Executive Strategic ConsolidationEntityGroup 5", 65000.00, 400.0, "ACTIVE", "uuid-consolidationentitygroup-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_intercompanyeliminationentrys (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_intercompanyeliminationentrys_code ON financial_consolidation_intercompanyeliminationentrys(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_intercompanyeliminationentrys_org_status ON financial_consolidation_intercompanyeliminationentrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_intercompanyeliminationentrys_priority ON financial_consolidation_intercompanyeliminationentrys(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_intercompanyeliminationentrys_created_at ON financial_consolidation_intercompanyeliminationentrys(created_at);

-- Operational seed data fixtures for financial_consolidation_intercompanyeliminationentrys
INSERT OR IGNORE INTO financial_consolidation_intercompanyeliminationentrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INT-0001", "Primary Operational IntercompanyEliminationEntry 1", 24500.00, 150.0, "ACTIVE", "uuid-intercompanyeliminationentry-01"),
    (2, "INT-0002", "Secondary Corporate IntercompanyEliminationEntry 2", 18200.50, 80.0, "ACTIVE", "uuid-intercompanyeliminationentry-02"),
    (3, "INT-0003", "Consolidated Branch IntercompanyEliminationEntry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-intercompanyeliminationentry-03"),
    (4, "INT-0004", "Enterprise Audited IntercompanyEliminationEntry 4", 32800.00, 210.0, "ACTIVE", "uuid-intercompanyeliminationentry-04"),
    (5, "INT-0005", "Executive Strategic IntercompanyEliminationEntry 5", 65000.00, 400.0, "ACTIVE", "uuid-intercompanyeliminationentry-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_consolidatedtrialbalances (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedtrialbalances_code ON financial_consolidation_consolidatedtrialbalances(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedtrialbalances_org_status ON financial_consolidation_consolidatedtrialbalances(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedtrialbalances_priority ON financial_consolidation_consolidatedtrialbalances(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedtrialbalances_created_at ON financial_consolidation_consolidatedtrialbalances(created_at);

-- Operational seed data fixtures for financial_consolidation_consolidatedtrialbalances
INSERT OR IGNORE INTO financial_consolidation_consolidatedtrialbalances (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ConsolidatedTrialBalance 1", 24500.00, 150.0, "ACTIVE", "uuid-consolidatedtrialbalance-01"),
    (2, "CON-0002", "Secondary Corporate ConsolidatedTrialBalance 2", 18200.50, 80.0, "ACTIVE", "uuid-consolidatedtrialbalance-02"),
    (3, "CON-0003", "Consolidated Branch ConsolidatedTrialBalance 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-consolidatedtrialbalance-03"),
    (4, "CON-0004", "Enterprise Audited ConsolidatedTrialBalance 4", 32800.00, 210.0, "ACTIVE", "uuid-consolidatedtrialbalance-04"),
    (5, "CON-0005", "Executive Strategic ConsolidatedTrialBalance 5", 65000.00, 400.0, "ACTIVE", "uuid-consolidatedtrialbalance-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_currencytranslationrates (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_currencytranslationrates_code ON financial_consolidation_currencytranslationrates(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_currencytranslationrates_org_status ON financial_consolidation_currencytranslationrates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_currencytranslationrates_priority ON financial_consolidation_currencytranslationrates(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_currencytranslationrates_created_at ON financial_consolidation_currencytranslationrates(created_at);

-- Operational seed data fixtures for financial_consolidation_currencytranslationrates
INSERT OR IGNORE INTO financial_consolidation_currencytranslationrates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUR-0001", "Primary Operational CurrencyTranslationRate 1", 24500.00, 150.0, "ACTIVE", "uuid-currencytranslationrate-01"),
    (2, "CUR-0002", "Secondary Corporate CurrencyTranslationRate 2", 18200.50, 80.0, "ACTIVE", "uuid-currencytranslationrate-02"),
    (3, "CUR-0003", "Consolidated Branch CurrencyTranslationRate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-currencytranslationrate-03"),
    (4, "CUR-0004", "Enterprise Audited CurrencyTranslationRate 4", 32800.00, 210.0, "ACTIVE", "uuid-currencytranslationrate-04"),
    (5, "CUR-0005", "Executive Strategic CurrencyTranslationRate 5", 65000.00, 400.0, "ACTIVE", "uuid-currencytranslationrate-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_minorityinterestshares (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_minorityinterestshares_code ON financial_consolidation_minorityinterestshares(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_minorityinterestshares_org_status ON financial_consolidation_minorityinterestshares(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_minorityinterestshares_priority ON financial_consolidation_minorityinterestshares(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_minorityinterestshares_created_at ON financial_consolidation_minorityinterestshares(created_at);

-- Operational seed data fixtures for financial_consolidation_minorityinterestshares
INSERT OR IGNORE INTO financial_consolidation_minorityinterestshares (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MIN-0001", "Primary Operational MinorityInterestShare 1", 24500.00, 150.0, "ACTIVE", "uuid-minorityinterestshare-01"),
    (2, "MIN-0002", "Secondary Corporate MinorityInterestShare 2", 18200.50, 80.0, "ACTIVE", "uuid-minorityinterestshare-02"),
    (3, "MIN-0003", "Consolidated Branch MinorityInterestShare 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-minorityinterestshare-03"),
    (4, "MIN-0004", "Enterprise Audited MinorityInterestShare 4", 32800.00, 210.0, "ACTIVE", "uuid-minorityinterestshare-04"),
    (5, "MIN-0005", "Executive Strategic MinorityInterestShare 5", 65000.00, 400.0, "ACTIVE", "uuid-minorityinterestshare-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_jointventureequityshares (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_jointventureequityshares_code ON financial_consolidation_jointventureequityshares(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_jointventureequityshares_org_status ON financial_consolidation_jointventureequityshares(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_jointventureequityshares_priority ON financial_consolidation_jointventureequityshares(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_jointventureequityshares_created_at ON financial_consolidation_jointventureequityshares(created_at);

-- Operational seed data fixtures for financial_consolidation_jointventureequityshares
INSERT OR IGNORE INTO financial_consolidation_jointventureequityshares (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "JOI-0001", "Primary Operational JointVentureEquityShare 1", 24500.00, 150.0, "ACTIVE", "uuid-jointventureequityshare-01"),
    (2, "JOI-0002", "Secondary Corporate JointVentureEquityShare 2", 18200.50, 80.0, "ACTIVE", "uuid-jointventureequityshare-02"),
    (3, "JOI-0003", "Consolidated Branch JointVentureEquityShare 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-jointventureequityshare-03"),
    (4, "JOI-0004", "Enterprise Audited JointVentureEquityShare 4", 32800.00, 210.0, "ACTIVE", "uuid-jointventureequityshare-04"),
    (5, "JOI-0005", "Executive Strategic JointVentureEquityShare 5", 65000.00, 400.0, "ACTIVE", "uuid-jointventureequityshare-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_financialadjustmentvouchers (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialadjustmentvouchers_code ON financial_consolidation_financialadjustmentvouchers(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialadjustmentvouchers_org_status ON financial_consolidation_financialadjustmentvouchers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialadjustmentvouchers_priority ON financial_consolidation_financialadjustmentvouchers(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialadjustmentvouchers_created_at ON financial_consolidation_financialadjustmentvouchers(created_at);

-- Operational seed data fixtures for financial_consolidation_financialadjustmentvouchers
INSERT OR IGNORE INTO financial_consolidation_financialadjustmentvouchers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FIN-0001", "Primary Operational FinancialAdjustmentVoucher 1", 24500.00, 150.0, "ACTIVE", "uuid-financialadjustmentvoucher-01"),
    (2, "FIN-0002", "Secondary Corporate FinancialAdjustmentVoucher 2", 18200.50, 80.0, "ACTIVE", "uuid-financialadjustmentvoucher-02"),
    (3, "FIN-0003", "Consolidated Branch FinancialAdjustmentVoucher 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-financialadjustmentvoucher-03"),
    (4, "FIN-0004", "Enterprise Audited FinancialAdjustmentVoucher 4", 32800.00, 210.0, "ACTIVE", "uuid-financialadjustmentvoucher-04"),
    (5, "FIN-0005", "Executive Strategic FinancialAdjustmentVoucher 5", 65000.00, 400.0, "ACTIVE", "uuid-financialadjustmentvoucher-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_goodwillimpairmentschedules (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_goodwillimpairmentschedules_code ON financial_consolidation_goodwillimpairmentschedules(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_goodwillimpairmentschedules_org_status ON financial_consolidation_goodwillimpairmentschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_goodwillimpairmentschedules_priority ON financial_consolidation_goodwillimpairmentschedules(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_goodwillimpairmentschedules_created_at ON financial_consolidation_goodwillimpairmentschedules(created_at);

-- Operational seed data fixtures for financial_consolidation_goodwillimpairmentschedules
INSERT OR IGNORE INTO financial_consolidation_goodwillimpairmentschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GOO-0001", "Primary Operational GoodwillImpairmentSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-goodwillimpairmentschedule-01"),
    (2, "GOO-0002", "Secondary Corporate GoodwillImpairmentSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-goodwillimpairmentschedule-02"),
    (3, "GOO-0003", "Consolidated Branch GoodwillImpairmentSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-goodwillimpairmentschedule-03"),
    (4, "GOO-0004", "Enterprise Audited GoodwillImpairmentSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-goodwillimpairmentschedule-04"),
    (5, "GOO-0005", "Executive Strategic GoodwillImpairmentSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-goodwillimpairmentschedule-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_segmentalreportingunits (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_segmentalreportingunits_code ON financial_consolidation_segmentalreportingunits(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_segmentalreportingunits_org_status ON financial_consolidation_segmentalreportingunits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_segmentalreportingunits_priority ON financial_consolidation_segmentalreportingunits(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_segmentalreportingunits_created_at ON financial_consolidation_segmentalreportingunits(created_at);

-- Operational seed data fixtures for financial_consolidation_segmentalreportingunits
INSERT OR IGNORE INTO financial_consolidation_segmentalreportingunits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEG-0001", "Primary Operational SegmentalReportingUnit 1", 24500.00, 150.0, "ACTIVE", "uuid-segmentalreportingunit-01"),
    (2, "SEG-0002", "Secondary Corporate SegmentalReportingUnit 2", 18200.50, 80.0, "ACTIVE", "uuid-segmentalreportingunit-02"),
    (3, "SEG-0003", "Consolidated Branch SegmentalReportingUnit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-segmentalreportingunit-03"),
    (4, "SEG-0004", "Enterprise Audited SegmentalReportingUnit 4", 32800.00, 210.0, "ACTIVE", "uuid-segmentalreportingunit-04"),
    (5, "SEG-0005", "Executive Strategic SegmentalReportingUnit 5", 65000.00, 400.0, "ACTIVE", "uuid-segmentalreportingunit-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_consolidatedcashflows (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedcashflows_code ON financial_consolidation_consolidatedcashflows(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedcashflows_org_status ON financial_consolidation_consolidatedcashflows(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedcashflows_priority ON financial_consolidation_consolidatedcashflows(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedcashflows_created_at ON financial_consolidation_consolidatedcashflows(created_at);

-- Operational seed data fixtures for financial_consolidation_consolidatedcashflows
INSERT OR IGNORE INTO financial_consolidation_consolidatedcashflows (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ConsolidatedCashFlow 1", 24500.00, 150.0, "ACTIVE", "uuid-consolidatedcashflow-01"),
    (2, "CON-0002", "Secondary Corporate ConsolidatedCashFlow 2", 18200.50, 80.0, "ACTIVE", "uuid-consolidatedcashflow-02"),
    (3, "CON-0003", "Consolidated Branch ConsolidatedCashFlow 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-consolidatedcashflow-03"),
    (4, "CON-0004", "Enterprise Audited ConsolidatedCashFlow 4", 32800.00, 210.0, "ACTIVE", "uuid-consolidatedcashflow-04"),
    (5, "CON-0005", "Executive Strategic ConsolidatedCashFlow 5", 65000.00, 400.0, "ACTIVE", "uuid-consolidatedcashflow-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_statutorybalancesheets (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_statutorybalancesheets_code ON financial_consolidation_statutorybalancesheets(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_statutorybalancesheets_org_status ON financial_consolidation_statutorybalancesheets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_statutorybalancesheets_priority ON financial_consolidation_statutorybalancesheets(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_statutorybalancesheets_created_at ON financial_consolidation_statutorybalancesheets(created_at);

-- Operational seed data fixtures for financial_consolidation_statutorybalancesheets
INSERT OR IGNORE INTO financial_consolidation_statutorybalancesheets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StatutoryBalanceSheet 1", 24500.00, 150.0, "ACTIVE", "uuid-statutorybalancesheet-01"),
    (2, "STA-0002", "Secondary Corporate StatutoryBalanceSheet 2", 18200.50, 80.0, "ACTIVE", "uuid-statutorybalancesheet-02"),
    (3, "STA-0003", "Consolidated Branch StatutoryBalanceSheet 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-statutorybalancesheet-03"),
    (4, "STA-0004", "Enterprise Audited StatutoryBalanceSheet 4", 32800.00, 210.0, "ACTIVE", "uuid-statutorybalancesheet-04"),
    (5, "STA-0005", "Executive Strategic StatutoryBalanceSheet 5", 65000.00, 400.0, "ACTIVE", "uuid-statutorybalancesheet-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_consolidatedincomestatements (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedincomestatements_code ON financial_consolidation_consolidatedincomestatements(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedincomestatements_org_status ON financial_consolidation_consolidatedincomestatements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedincomestatements_priority ON financial_consolidation_consolidatedincomestatements(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_consolidatedincomestatements_created_at ON financial_consolidation_consolidatedincomestatements(created_at);

-- Operational seed data fixtures for financial_consolidation_consolidatedincomestatements
INSERT OR IGNORE INTO financial_consolidation_consolidatedincomestatements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ConsolidatedIncomeStatement 1", 24500.00, 150.0, "ACTIVE", "uuid-consolidatedincomestatement-01"),
    (2, "CON-0002", "Secondary Corporate ConsolidatedIncomeStatement 2", 18200.50, 80.0, "ACTIVE", "uuid-consolidatedincomestatement-02"),
    (3, "CON-0003", "Consolidated Branch ConsolidatedIncomeStatement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-consolidatedincomestatement-03"),
    (4, "CON-0004", "Enterprise Audited ConsolidatedIncomeStatement 4", 32800.00, 210.0, "ACTIVE", "uuid-consolidatedincomestatement-04"),
    (5, "CON-0005", "Executive Strategic ConsolidatedIncomeStatement 5", 65000.00, 400.0, "ACTIVE", "uuid-consolidatedincomestatement-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_audittraileliminations (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_audittraileliminations_code ON financial_consolidation_audittraileliminations(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_audittraileliminations_org_status ON financial_consolidation_audittraileliminations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_audittraileliminations_priority ON financial_consolidation_audittraileliminations(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_audittraileliminations_created_at ON financial_consolidation_audittraileliminations(created_at);

-- Operational seed data fixtures for financial_consolidation_audittraileliminations
INSERT OR IGNORE INTO financial_consolidation_audittraileliminations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "AUD-0001", "Primary Operational AuditTrailElimination 1", 24500.00, 150.0, "ACTIVE", "uuid-audittrailelimination-01"),
    (2, "AUD-0002", "Secondary Corporate AuditTrailElimination 2", 18200.50, 80.0, "ACTIVE", "uuid-audittrailelimination-02"),
    (3, "AUD-0003", "Consolidated Branch AuditTrailElimination 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-audittrailelimination-03"),
    (4, "AUD-0004", "Enterprise Audited AuditTrailElimination 4", 32800.00, 210.0, "ACTIVE", "uuid-audittrailelimination-04"),
    (5, "AUD-0005", "Executive Strategic AuditTrailElimination 5", 65000.00, 400.0, "ACTIVE", "uuid-audittrailelimination-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_taxprovisioningconsolidateds (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_taxprovisioningconsolidateds_code ON financial_consolidation_taxprovisioningconsolidateds(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_taxprovisioningconsolidateds_org_status ON financial_consolidation_taxprovisioningconsolidateds(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_taxprovisioningconsolidateds_priority ON financial_consolidation_taxprovisioningconsolidateds(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_taxprovisioningconsolidateds_created_at ON financial_consolidation_taxprovisioningconsolidateds(created_at);

-- Operational seed data fixtures for financial_consolidation_taxprovisioningconsolidateds
INSERT OR IGNORE INTO financial_consolidation_taxprovisioningconsolidateds (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxProvisioningConsolidated 1", 24500.00, 150.0, "ACTIVE", "uuid-taxprovisioningconsolidated-01"),
    (2, "TAX-0002", "Secondary Corporate TaxProvisioningConsolidated 2", 18200.50, 80.0, "ACTIVE", "uuid-taxprovisioningconsolidated-02"),
    (3, "TAX-0003", "Consolidated Branch TaxProvisioningConsolidated 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxprovisioningconsolidated-03"),
    (4, "TAX-0004", "Enterprise Audited TaxProvisioningConsolidated 4", 32800.00, 210.0, "ACTIVE", "uuid-taxprovisioningconsolidated-04"),
    (5, "TAX-0005", "Executive Strategic TaxProvisioningConsolidated 5", 65000.00, 400.0, "ACTIVE", "uuid-taxprovisioningconsolidated-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_financialclosingchecklists (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialclosingchecklists_code ON financial_consolidation_financialclosingchecklists(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialclosingchecklists_org_status ON financial_consolidation_financialclosingchecklists(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialclosingchecklists_priority ON financial_consolidation_financialclosingchecklists(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_financialclosingchecklists_created_at ON financial_consolidation_financialclosingchecklists(created_at);

-- Operational seed data fixtures for financial_consolidation_financialclosingchecklists
INSERT OR IGNORE INTO financial_consolidation_financialclosingchecklists (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FIN-0001", "Primary Operational FinancialClosingChecklist 1", 24500.00, 150.0, "ACTIVE", "uuid-financialclosingchecklist-01"),
    (2, "FIN-0002", "Secondary Corporate FinancialClosingChecklist 2", 18200.50, 80.0, "ACTIVE", "uuid-financialclosingchecklist-02"),
    (3, "FIN-0003", "Consolidated Branch FinancialClosingChecklist 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-financialclosingchecklist-03"),
    (4, "FIN-0004", "Enterprise Audited FinancialClosingChecklist 4", 32800.00, 210.0, "ACTIVE", "uuid-financialclosingchecklist-04"),
    (5, "FIN-0005", "Executive Strategic FinancialClosingChecklist 5", 65000.00, 400.0, "ACTIVE", "uuid-financialclosingchecklist-05");

CREATE TABLE IF NOT EXISTS financial_consolidation_executiveboardfinancialreports (
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

CREATE INDEX IF NOT EXISTS idx_financial_consolidation_executiveboardfinancialreports_code ON financial_consolidation_executiveboardfinancialreports(code);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_executiveboardfinancialreports_org_status ON financial_consolidation_executiveboardfinancialreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_executiveboardfinancialreports_priority ON financial_consolidation_executiveboardfinancialreports(priority);
CREATE INDEX IF NOT EXISTS idx_financial_consolidation_executiveboardfinancialreports_created_at ON financial_consolidation_executiveboardfinancialreports(created_at);

-- Operational seed data fixtures for financial_consolidation_executiveboardfinancialreports
INSERT OR IGNORE INTO financial_consolidation_executiveboardfinancialreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutiveBoardFinancialReport 1", 24500.00, 150.0, "ACTIVE", "uuid-executiveboardfinancialreport-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutiveBoardFinancialReport 2", 18200.50, 80.0, "ACTIVE", "uuid-executiveboardfinancialreport-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutiveBoardFinancialReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executiveboardfinancialreport-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutiveBoardFinancialReport 4", 32800.00, 210.0, "ACTIVE", "uuid-executiveboardfinancialreport-04"),
    (5, "EXE-0005", "Executive Strategic ExecutiveBoardFinancialReport 5", 65000.00, 400.0, "ACTIVE", "uuid-executiveboardfinancialreport-05");

