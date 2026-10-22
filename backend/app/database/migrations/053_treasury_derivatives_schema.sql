-- SmartERP Enterprise Titan Migration 053: Financial Derivatives & Mark-to-Market Hedging DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS treasury_derivatives_interestrateswapcontracts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_interestrateswapcontracts_code ON treasury_derivatives_interestrateswapcontracts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_interestrateswapcontracts_org_status ON treasury_derivatives_interestrateswapcontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_interestrateswapcontracts_priority ON treasury_derivatives_interestrateswapcontracts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_interestrateswapcontracts_created_at ON treasury_derivatives_interestrateswapcontracts(created_at);

-- Operational seed data fixtures for treasury_derivatives_interestrateswapcontracts
INSERT OR IGNORE INTO treasury_derivatives_interestrateswapcontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INT-0001", "Primary Operational InterestRateSwapContract 1", 24500.00, 150.0, "ACTIVE", "uuid-interestrateswapcontract-01"),
    (2, "INT-0002", "Secondary Corporate InterestRateSwapContract 2", 18200.50, 80.0, "ACTIVE", "uuid-interestrateswapcontract-02"),
    (3, "INT-0003", "Consolidated Branch InterestRateSwapContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-interestrateswapcontract-03"),
    (4, "INT-0004", "Enterprise Audited InterestRateSwapContract 4", 32800.00, 210.0, "ACTIVE", "uuid-interestrateswapcontract-04"),
    (5, "INT-0005", "Executive Strategic InterestRateSwapContract 5", 65000.00, 400.0, "ACTIVE", "uuid-interestrateswapcontract-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_fxforwardcontracts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_fxforwardcontracts_code ON treasury_derivatives_fxforwardcontracts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_fxforwardcontracts_org_status ON treasury_derivatives_fxforwardcontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_fxforwardcontracts_priority ON treasury_derivatives_fxforwardcontracts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_fxforwardcontracts_created_at ON treasury_derivatives_fxforwardcontracts(created_at);

-- Operational seed data fixtures for treasury_derivatives_fxforwardcontracts
INSERT OR IGNORE INTO treasury_derivatives_fxforwardcontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FXF-0001", "Primary Operational FXForwardContract 1", 24500.00, 150.0, "ACTIVE", "uuid-fxforwardcontract-01"),
    (2, "FXF-0002", "Secondary Corporate FXForwardContract 2", 18200.50, 80.0, "ACTIVE", "uuid-fxforwardcontract-02"),
    (3, "FXF-0003", "Consolidated Branch FXForwardContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fxforwardcontract-03"),
    (4, "FXF-0004", "Enterprise Audited FXForwardContract 4", 32800.00, 210.0, "ACTIVE", "uuid-fxforwardcontract-04"),
    (5, "FXF-0005", "Executive Strategic FXForwardContract 5", 65000.00, 400.0, "ACTIVE", "uuid-fxforwardcontract-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_commodityfuturehedges (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_commodityfuturehedges_code ON treasury_derivatives_commodityfuturehedges(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_commodityfuturehedges_org_status ON treasury_derivatives_commodityfuturehedges(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_commodityfuturehedges_priority ON treasury_derivatives_commodityfuturehedges(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_commodityfuturehedges_created_at ON treasury_derivatives_commodityfuturehedges(created_at);

-- Operational seed data fixtures for treasury_derivatives_commodityfuturehedges
INSERT OR IGNORE INTO treasury_derivatives_commodityfuturehedges (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CommodityFutureHedge 1", 24500.00, 150.0, "ACTIVE", "uuid-commodityfuturehedge-01"),
    (2, "COM-0002", "Secondary Corporate CommodityFutureHedge 2", 18200.50, 80.0, "ACTIVE", "uuid-commodityfuturehedge-02"),
    (3, "COM-0003", "Consolidated Branch CommodityFutureHedge 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-commodityfuturehedge-03"),
    (4, "COM-0004", "Enterprise Audited CommodityFutureHedge 4", 32800.00, 210.0, "ACTIVE", "uuid-commodityfuturehedge-04"),
    (5, "COM-0005", "Executive Strategic CommodityFutureHedge 5", 65000.00, 400.0, "ACTIVE", "uuid-commodityfuturehedge-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_currencyoptionstrategys (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_currencyoptionstrategys_code ON treasury_derivatives_currencyoptionstrategys(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_currencyoptionstrategys_org_status ON treasury_derivatives_currencyoptionstrategys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_currencyoptionstrategys_priority ON treasury_derivatives_currencyoptionstrategys(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_currencyoptionstrategys_created_at ON treasury_derivatives_currencyoptionstrategys(created_at);

-- Operational seed data fixtures for treasury_derivatives_currencyoptionstrategys
INSERT OR IGNORE INTO treasury_derivatives_currencyoptionstrategys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUR-0001", "Primary Operational CurrencyOptionStrategy 1", 24500.00, 150.0, "ACTIVE", "uuid-currencyoptionstrategy-01"),
    (2, "CUR-0002", "Secondary Corporate CurrencyOptionStrategy 2", 18200.50, 80.0, "ACTIVE", "uuid-currencyoptionstrategy-02"),
    (3, "CUR-0003", "Consolidated Branch CurrencyOptionStrategy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-currencyoptionstrategy-03"),
    (4, "CUR-0004", "Enterprise Audited CurrencyOptionStrategy 4", 32800.00, 210.0, "ACTIVE", "uuid-currencyoptionstrategy-04"),
    (5, "CUR-0005", "Executive Strategic CurrencyOptionStrategy 5", 65000.00, 400.0, "ACTIVE", "uuid-currencyoptionstrategy-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_marktomarketvaluations (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_marktomarketvaluations_code ON treasury_derivatives_marktomarketvaluations(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_marktomarketvaluations_org_status ON treasury_derivatives_marktomarketvaluations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_marktomarketvaluations_priority ON treasury_derivatives_marktomarketvaluations(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_marktomarketvaluations_created_at ON treasury_derivatives_marktomarketvaluations(created_at);

-- Operational seed data fixtures for treasury_derivatives_marktomarketvaluations
INSERT OR IGNORE INTO treasury_derivatives_marktomarketvaluations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAR-0001", "Primary Operational MarkToMarketValuation 1", 24500.00, 150.0, "ACTIVE", "uuid-marktomarketvaluation-01"),
    (2, "MAR-0002", "Secondary Corporate MarkToMarketValuation 2", 18200.50, 80.0, "ACTIVE", "uuid-marktomarketvaluation-02"),
    (3, "MAR-0003", "Consolidated Branch MarkToMarketValuation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-marktomarketvaluation-03"),
    (4, "MAR-0004", "Enterprise Audited MarkToMarketValuation 4", 32800.00, 210.0, "ACTIVE", "uuid-marktomarketvaluation-04"),
    (5, "MAR-0005", "Executive Strategic MarkToMarketValuation 5", 65000.00, 400.0, "ACTIVE", "uuid-marktomarketvaluation-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_isdamasteragreements (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_isdamasteragreements_code ON treasury_derivatives_isdamasteragreements(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_isdamasteragreements_org_status ON treasury_derivatives_isdamasteragreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_isdamasteragreements_priority ON treasury_derivatives_isdamasteragreements(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_isdamasteragreements_created_at ON treasury_derivatives_isdamasteragreements(created_at);

-- Operational seed data fixtures for treasury_derivatives_isdamasteragreements
INSERT OR IGNORE INTO treasury_derivatives_isdamasteragreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ISD-0001", "Primary Operational ISDAMasterAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-isdamasteragreement-01"),
    (2, "ISD-0002", "Secondary Corporate ISDAMasterAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-isdamasteragreement-02"),
    (3, "ISD-0003", "Consolidated Branch ISDAMasterAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-isdamasteragreement-03"),
    (4, "ISD-0004", "Enterprise Audited ISDAMasterAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-isdamasteragreement-04"),
    (5, "ISD-0005", "Executive Strategic ISDAMasterAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-isdamasteragreement-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_collateralmargincalls (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_collateralmargincalls_code ON treasury_derivatives_collateralmargincalls(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_collateralmargincalls_org_status ON treasury_derivatives_collateralmargincalls(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_collateralmargincalls_priority ON treasury_derivatives_collateralmargincalls(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_collateralmargincalls_created_at ON treasury_derivatives_collateralmargincalls(created_at);

-- Operational seed data fixtures for treasury_derivatives_collateralmargincalls
INSERT OR IGNORE INTO treasury_derivatives_collateralmargincalls (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COL-0001", "Primary Operational CollateralMarginCall 1", 24500.00, 150.0, "ACTIVE", "uuid-collateralmargincall-01"),
    (2, "COL-0002", "Secondary Corporate CollateralMarginCall 2", 18200.50, 80.0, "ACTIVE", "uuid-collateralmargincall-02"),
    (3, "COL-0003", "Consolidated Branch CollateralMarginCall 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-collateralmargincall-03"),
    (4, "COL-0004", "Enterprise Audited CollateralMarginCall 4", 32800.00, 210.0, "ACTIVE", "uuid-collateralmargincall-04"),
    (5, "COL-0005", "Executive Strategic CollateralMarginCall 5", 65000.00, 400.0, "ACTIVE", "uuid-collateralmargincall-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_creditdefaultswapspreads (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_creditdefaultswapspreads_code ON treasury_derivatives_creditdefaultswapspreads(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_creditdefaultswapspreads_org_status ON treasury_derivatives_creditdefaultswapspreads(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_creditdefaultswapspreads_priority ON treasury_derivatives_creditdefaultswapspreads(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_creditdefaultswapspreads_created_at ON treasury_derivatives_creditdefaultswapspreads(created_at);

-- Operational seed data fixtures for treasury_derivatives_creditdefaultswapspreads
INSERT OR IGNORE INTO treasury_derivatives_creditdefaultswapspreads (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CRE-0001", "Primary Operational CreditDefaultSwapSpread 1", 24500.00, 150.0, "ACTIVE", "uuid-creditdefaultswapspread-01"),
    (2, "CRE-0002", "Secondary Corporate CreditDefaultSwapSpread 2", 18200.50, 80.0, "ACTIVE", "uuid-creditdefaultswapspread-02"),
    (3, "CRE-0003", "Consolidated Branch CreditDefaultSwapSpread 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-creditdefaultswapspread-03"),
    (4, "CRE-0004", "Enterprise Audited CreditDefaultSwapSpread 4", 32800.00, 210.0, "ACTIVE", "uuid-creditdefaultswapspread-04"),
    (5, "CRE-0005", "Executive Strategic CreditDefaultSwapSpread 5", 65000.00, 400.0, "ACTIVE", "uuid-creditdefaultswapspread-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_hedgeeffectivenesstests (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_hedgeeffectivenesstests_code ON treasury_derivatives_hedgeeffectivenesstests(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_hedgeeffectivenesstests_org_status ON treasury_derivatives_hedgeeffectivenesstests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_hedgeeffectivenesstests_priority ON treasury_derivatives_hedgeeffectivenesstests(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_hedgeeffectivenesstests_created_at ON treasury_derivatives_hedgeeffectivenesstests(created_at);

-- Operational seed data fixtures for treasury_derivatives_hedgeeffectivenesstests
INSERT OR IGNORE INTO treasury_derivatives_hedgeeffectivenesstests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HED-0001", "Primary Operational HedgeEffectivenessTest 1", 24500.00, 150.0, "ACTIVE", "uuid-hedgeeffectivenesstest-01"),
    (2, "HED-0002", "Secondary Corporate HedgeEffectivenessTest 2", 18200.50, 80.0, "ACTIVE", "uuid-hedgeeffectivenesstest-02"),
    (3, "HED-0003", "Consolidated Branch HedgeEffectivenessTest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hedgeeffectivenesstest-03"),
    (4, "HED-0004", "Enterprise Audited HedgeEffectivenessTest 4", 32800.00, 210.0, "ACTIVE", "uuid-hedgeeffectivenesstest-04"),
    (5, "HED-0005", "Executive Strategic HedgeEffectivenessTest 5", 65000.00, 400.0, "ACTIVE", "uuid-hedgeeffectivenesstest-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_greeksrisksensitivitys (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_greeksrisksensitivitys_code ON treasury_derivatives_greeksrisksensitivitys(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_greeksrisksensitivitys_org_status ON treasury_derivatives_greeksrisksensitivitys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_greeksrisksensitivitys_priority ON treasury_derivatives_greeksrisksensitivitys(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_greeksrisksensitivitys_created_at ON treasury_derivatives_greeksrisksensitivitys(created_at);

-- Operational seed data fixtures for treasury_derivatives_greeksrisksensitivitys
INSERT OR IGNORE INTO treasury_derivatives_greeksrisksensitivitys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GRE-0001", "Primary Operational GreeksRiskSensitivity 1", 24500.00, 150.0, "ACTIVE", "uuid-greeksrisksensitivity-01"),
    (2, "GRE-0002", "Secondary Corporate GreeksRiskSensitivity 2", 18200.50, 80.0, "ACTIVE", "uuid-greeksrisksensitivity-02"),
    (3, "GRE-0003", "Consolidated Branch GreeksRiskSensitivity 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-greeksrisksensitivity-03"),
    (4, "GRE-0004", "Enterprise Audited GreeksRiskSensitivity 4", 32800.00, 210.0, "ACTIVE", "uuid-greeksrisksensitivity-04"),
    (5, "GRE-0005", "Executive Strategic GreeksRiskSensitivity 5", 65000.00, 400.0, "ACTIVE", "uuid-greeksrisksensitivity-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_counterpartycreditrisks (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_counterpartycreditrisks_code ON treasury_derivatives_counterpartycreditrisks(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_counterpartycreditrisks_org_status ON treasury_derivatives_counterpartycreditrisks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_counterpartycreditrisks_priority ON treasury_derivatives_counterpartycreditrisks(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_counterpartycreditrisks_created_at ON treasury_derivatives_counterpartycreditrisks(created_at);

-- Operational seed data fixtures for treasury_derivatives_counterpartycreditrisks
INSERT OR IGNORE INTO treasury_derivatives_counterpartycreditrisks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COU-0001", "Primary Operational CounterpartyCreditRisk 1", 24500.00, 150.0, "ACTIVE", "uuid-counterpartycreditrisk-01"),
    (2, "COU-0002", "Secondary Corporate CounterpartyCreditRisk 2", 18200.50, 80.0, "ACTIVE", "uuid-counterpartycreditrisk-02"),
    (3, "COU-0003", "Consolidated Branch CounterpartyCreditRisk 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-counterpartycreditrisk-03"),
    (4, "COU-0004", "Enterprise Audited CounterpartyCreditRisk 4", 32800.00, 210.0, "ACTIVE", "uuid-counterpartycreditrisk-04"),
    (5, "COU-0005", "Executive Strategic CounterpartyCreditRisk 5", 65000.00, 400.0, "ACTIVE", "uuid-counterpartycreditrisk-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_yieldcurveinterpolations (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_yieldcurveinterpolations_code ON treasury_derivatives_yieldcurveinterpolations(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_yieldcurveinterpolations_org_status ON treasury_derivatives_yieldcurveinterpolations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_yieldcurveinterpolations_priority ON treasury_derivatives_yieldcurveinterpolations(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_yieldcurveinterpolations_created_at ON treasury_derivatives_yieldcurveinterpolations(created_at);

-- Operational seed data fixtures for treasury_derivatives_yieldcurveinterpolations
INSERT OR IGNORE INTO treasury_derivatives_yieldcurveinterpolations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "YIE-0001", "Primary Operational YieldCurveInterpolation 1", 24500.00, 150.0, "ACTIVE", "uuid-yieldcurveinterpolation-01"),
    (2, "YIE-0002", "Secondary Corporate YieldCurveInterpolation 2", 18200.50, 80.0, "ACTIVE", "uuid-yieldcurveinterpolation-02"),
    (3, "YIE-0003", "Consolidated Branch YieldCurveInterpolation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-yieldcurveinterpolation-03"),
    (4, "YIE-0004", "Enterprise Audited YieldCurveInterpolation 4", 32800.00, 210.0, "ACTIVE", "uuid-yieldcurveinterpolation-04"),
    (5, "YIE-0005", "Executive Strategic YieldCurveInterpolation 5", 65000.00, 400.0, "ACTIVE", "uuid-yieldcurveinterpolation-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_derivativessettlemententrys (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_derivativessettlemententrys_code ON treasury_derivatives_derivativessettlemententrys(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_derivativessettlemententrys_org_status ON treasury_derivatives_derivativessettlemententrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_derivativessettlemententrys_priority ON treasury_derivatives_derivativessettlemententrys(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_derivativessettlemententrys_created_at ON treasury_derivatives_derivativessettlemententrys(created_at);

-- Operational seed data fixtures for treasury_derivatives_derivativessettlemententrys
INSERT OR IGNORE INTO treasury_derivatives_derivativessettlemententrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DER-0001", "Primary Operational DerivativesSettlementEntry 1", 24500.00, 150.0, "ACTIVE", "uuid-derivativessettlemententry-01"),
    (2, "DER-0002", "Secondary Corporate DerivativesSettlementEntry 2", 18200.50, 80.0, "ACTIVE", "uuid-derivativessettlemententry-02"),
    (3, "DER-0003", "Consolidated Branch DerivativesSettlementEntry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-derivativessettlemententry-03"),
    (4, "DER-0004", "Enterprise Audited DerivativesSettlementEntry 4", 32800.00, 210.0, "ACTIVE", "uuid-derivativessettlemententry-04"),
    (5, "DER-0005", "Executive Strategic DerivativesSettlementEntry 5", 65000.00, 400.0, "ACTIVE", "uuid-derivativessettlemententry-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_treasuryexposureforecasts (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_treasuryexposureforecasts_code ON treasury_derivatives_treasuryexposureforecasts(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_treasuryexposureforecasts_org_status ON treasury_derivatives_treasuryexposureforecasts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_treasuryexposureforecasts_priority ON treasury_derivatives_treasuryexposureforecasts(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_treasuryexposureforecasts_created_at ON treasury_derivatives_treasuryexposureforecasts(created_at);

-- Operational seed data fixtures for treasury_derivatives_treasuryexposureforecasts
INSERT OR IGNORE INTO treasury_derivatives_treasuryexposureforecasts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRE-0001", "Primary Operational TreasuryExposureForecast 1", 24500.00, 150.0, "ACTIVE", "uuid-treasuryexposureforecast-01"),
    (2, "TRE-0002", "Secondary Corporate TreasuryExposureForecast 2", 18200.50, 80.0, "ACTIVE", "uuid-treasuryexposureforecast-02"),
    (3, "TRE-0003", "Consolidated Branch TreasuryExposureForecast 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-treasuryexposureforecast-03"),
    (4, "TRE-0004", "Enterprise Audited TreasuryExposureForecast 4", 32800.00, 210.0, "ACTIVE", "uuid-treasuryexposureforecast-04"),
    (5, "TRE-0005", "Executive Strategic TreasuryExposureForecast 5", 65000.00, 400.0, "ACTIVE", "uuid-treasuryexposureforecast-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_regulatoryemirfilings (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_regulatoryemirfilings_code ON treasury_derivatives_regulatoryemirfilings(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_regulatoryemirfilings_org_status ON treasury_derivatives_regulatoryemirfilings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_regulatoryemirfilings_priority ON treasury_derivatives_regulatoryemirfilings(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_regulatoryemirfilings_created_at ON treasury_derivatives_regulatoryemirfilings(created_at);

-- Operational seed data fixtures for treasury_derivatives_regulatoryemirfilings
INSERT OR IGNORE INTO treasury_derivatives_regulatoryemirfilings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REG-0001", "Primary Operational RegulatoryEMIRFiling 1", 24500.00, 150.0, "ACTIVE", "uuid-regulatoryemirfiling-01"),
    (2, "REG-0002", "Secondary Corporate RegulatoryEMIRFiling 2", 18200.50, 80.0, "ACTIVE", "uuid-regulatoryemirfiling-02"),
    (3, "REG-0003", "Consolidated Branch RegulatoryEMIRFiling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-regulatoryemirfiling-03"),
    (4, "REG-0004", "Enterprise Audited RegulatoryEMIRFiling 4", 32800.00, 210.0, "ACTIVE", "uuid-regulatoryemirfiling-04"),
    (5, "REG-0005", "Executive Strategic RegulatoryEMIRFiling 5", 65000.00, 400.0, "ACTIVE", "uuid-regulatoryemirfiling-05");

CREATE TABLE IF NOT EXISTS treasury_derivatives_basisriskmeasurements (
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

CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_basisriskmeasurements_code ON treasury_derivatives_basisriskmeasurements(code);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_basisriskmeasurements_org_status ON treasury_derivatives_basisriskmeasurements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_basisriskmeasurements_priority ON treasury_derivatives_basisriskmeasurements(priority);
CREATE INDEX IF NOT EXISTS idx_treasury_derivatives_basisriskmeasurements_created_at ON treasury_derivatives_basisriskmeasurements(created_at);

-- Operational seed data fixtures for treasury_derivatives_basisriskmeasurements
INSERT OR IGNORE INTO treasury_derivatives_basisriskmeasurements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BAS-0001", "Primary Operational BasisRiskMeasurement 1", 24500.00, 150.0, "ACTIVE", "uuid-basisriskmeasurement-01"),
    (2, "BAS-0002", "Secondary Corporate BasisRiskMeasurement 2", 18200.50, 80.0, "ACTIVE", "uuid-basisriskmeasurement-02"),
    (3, "BAS-0003", "Consolidated Branch BasisRiskMeasurement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-basisriskmeasurement-03"),
    (4, "BAS-0004", "Enterprise Audited BasisRiskMeasurement 4", 32800.00, 210.0, "ACTIVE", "uuid-basisriskmeasurement-04"),
    (5, "BAS-0005", "Executive Strategic BasisRiskMeasurement 5", 65000.00, 400.0, "ACTIVE", "uuid-basisriskmeasurement-05");

