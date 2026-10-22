-- SmartERP Enterprise Titan Migration 033: Dynamic Pricing & Revenue Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS pricing_promotions_pricelistmasters (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricelistmasters_code ON pricing_promotions_pricelistmasters(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricelistmasters_org_status ON pricing_promotions_pricelistmasters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricelistmasters_priority ON pricing_promotions_pricelistmasters(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricelistmasters_created_at ON pricing_promotions_pricelistmasters(created_at);

-- Operational seed data fixtures for pricing_promotions_pricelistmasters
INSERT OR IGNORE INTO pricing_promotions_pricelistmasters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PriceListMaster 1", 24500.00, 150.0, "ACTIVE", "uuid-pricelistmaster-01"),
    (2, "PRI-0002", "Secondary Corporate PriceListMaster 2", 18200.50, 80.0, "ACTIVE", "uuid-pricelistmaster-02"),
    (3, "PRI-0003", "Consolidated Branch PriceListMaster 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-pricelistmaster-03"),
    (4, "PRI-0004", "Enterprise Audited PriceListMaster 4", 32800.00, 210.0, "ACTIVE", "uuid-pricelistmaster-04"),
    (5, "PRI-0005", "Executive Strategic PriceListMaster 5", 65000.00, 400.0, "ACTIVE", "uuid-pricelistmaster-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_tieredvolumediscounts (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_tieredvolumediscounts_code ON pricing_promotions_tieredvolumediscounts(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_tieredvolumediscounts_org_status ON pricing_promotions_tieredvolumediscounts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_tieredvolumediscounts_priority ON pricing_promotions_tieredvolumediscounts(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_tieredvolumediscounts_created_at ON pricing_promotions_tieredvolumediscounts(created_at);

-- Operational seed data fixtures for pricing_promotions_tieredvolumediscounts
INSERT OR IGNORE INTO pricing_promotions_tieredvolumediscounts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIE-0001", "Primary Operational TieredVolumeDiscount 1", 24500.00, 150.0, "ACTIVE", "uuid-tieredvolumediscount-01"),
    (2, "TIE-0002", "Secondary Corporate TieredVolumeDiscount 2", 18200.50, 80.0, "ACTIVE", "uuid-tieredvolumediscount-02"),
    (3, "TIE-0003", "Consolidated Branch TieredVolumeDiscount 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tieredvolumediscount-03"),
    (4, "TIE-0004", "Enterprise Audited TieredVolumeDiscount 4", 32800.00, 210.0, "ACTIVE", "uuid-tieredvolumediscount-04"),
    (5, "TIE-0005", "Executive Strategic TieredVolumeDiscount 5", 65000.00, 400.0, "ACTIVE", "uuid-tieredvolumediscount-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_promotionalcampaigns (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalcampaigns_code ON pricing_promotions_promotionalcampaigns(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalcampaigns_org_status ON pricing_promotions_promotionalcampaigns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalcampaigns_priority ON pricing_promotions_promotionalcampaigns(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalcampaigns_created_at ON pricing_promotions_promotionalcampaigns(created_at);

-- Operational seed data fixtures for pricing_promotions_promotionalcampaigns
INSERT OR IGNORE INTO pricing_promotions_promotionalcampaigns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational PromotionalCampaign 1", 24500.00, 150.0, "ACTIVE", "uuid-promotionalcampaign-01"),
    (2, "PRO-0002", "Secondary Corporate PromotionalCampaign 2", 18200.50, 80.0, "ACTIVE", "uuid-promotionalcampaign-02"),
    (3, "PRO-0003", "Consolidated Branch PromotionalCampaign 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-promotionalcampaign-03"),
    (4, "PRO-0004", "Enterprise Audited PromotionalCampaign 4", 32800.00, 210.0, "ACTIVE", "uuid-promotionalcampaign-04"),
    (5, "PRO-0005", "Executive Strategic PromotionalCampaign 5", 65000.00, 400.0, "ACTIVE", "uuid-promotionalcampaign-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_customerrebateagreements (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_customerrebateagreements_code ON pricing_promotions_customerrebateagreements(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_customerrebateagreements_org_status ON pricing_promotions_customerrebateagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_customerrebateagreements_priority ON pricing_promotions_customerrebateagreements(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_customerrebateagreements_created_at ON pricing_promotions_customerrebateagreements(created_at);

-- Operational seed data fixtures for pricing_promotions_customerrebateagreements
INSERT OR IGNORE INTO pricing_promotions_customerrebateagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerRebateAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-customerrebateagreement-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerRebateAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-customerrebateagreement-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerRebateAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerrebateagreement-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerRebateAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-customerrebateagreement-04"),
    (5, "CUS-0005", "Executive Strategic CustomerRebateAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-customerrebateagreement-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_couponcoderegistrys (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_couponcoderegistrys_code ON pricing_promotions_couponcoderegistrys(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_couponcoderegistrys_org_status ON pricing_promotions_couponcoderegistrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_couponcoderegistrys_priority ON pricing_promotions_couponcoderegistrys(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_couponcoderegistrys_created_at ON pricing_promotions_couponcoderegistrys(created_at);

-- Operational seed data fixtures for pricing_promotions_couponcoderegistrys
INSERT OR IGNORE INTO pricing_promotions_couponcoderegistrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COU-0001", "Primary Operational CouponCodeRegistry 1", 24500.00, 150.0, "ACTIVE", "uuid-couponcoderegistry-01"),
    (2, "COU-0002", "Secondary Corporate CouponCodeRegistry 2", 18200.50, 80.0, "ACTIVE", "uuid-couponcoderegistry-02"),
    (3, "COU-0003", "Consolidated Branch CouponCodeRegistry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-couponcoderegistry-03"),
    (4, "COU-0004", "Enterprise Audited CouponCodeRegistry 4", 32800.00, 210.0, "ACTIVE", "uuid-couponcoderegistry-04"),
    (5, "COU-0005", "Executive Strategic CouponCodeRegistry 5", 65000.00, 400.0, "ACTIVE", "uuid-couponcoderegistry-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_competitorpricemonitors (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_competitorpricemonitors_code ON pricing_promotions_competitorpricemonitors(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_competitorpricemonitors_org_status ON pricing_promotions_competitorpricemonitors(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_competitorpricemonitors_priority ON pricing_promotions_competitorpricemonitors(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_competitorpricemonitors_created_at ON pricing_promotions_competitorpricemonitors(created_at);

-- Operational seed data fixtures for pricing_promotions_competitorpricemonitors
INSERT OR IGNORE INTO pricing_promotions_competitorpricemonitors (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CompetitorPriceMonitor 1", 24500.00, 150.0, "ACTIVE", "uuid-competitorpricemonitor-01"),
    (2, "COM-0002", "Secondary Corporate CompetitorPriceMonitor 2", 18200.50, 80.0, "ACTIVE", "uuid-competitorpricemonitor-02"),
    (3, "COM-0003", "Consolidated Branch CompetitorPriceMonitor 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-competitorpricemonitor-03"),
    (4, "COM-0004", "Enterprise Audited CompetitorPriceMonitor 4", 32800.00, 210.0, "ACTIVE", "uuid-competitorpricemonitor-04"),
    (5, "COM-0005", "Executive Strategic CompetitorPriceMonitor 5", 65000.00, 400.0, "ACTIVE", "uuid-competitorpricemonitor-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_marginfloorthresholds (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_marginfloorthresholds_code ON pricing_promotions_marginfloorthresholds(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_marginfloorthresholds_org_status ON pricing_promotions_marginfloorthresholds(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_marginfloorthresholds_priority ON pricing_promotions_marginfloorthresholds(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_marginfloorthresholds_created_at ON pricing_promotions_marginfloorthresholds(created_at);

-- Operational seed data fixtures for pricing_promotions_marginfloorthresholds
INSERT OR IGNORE INTO pricing_promotions_marginfloorthresholds (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAR-0001", "Primary Operational MarginFloorThreshold 1", 24500.00, 150.0, "ACTIVE", "uuid-marginfloorthreshold-01"),
    (2, "MAR-0002", "Secondary Corporate MarginFloorThreshold 2", 18200.50, 80.0, "ACTIVE", "uuid-marginfloorthreshold-02"),
    (3, "MAR-0003", "Consolidated Branch MarginFloorThreshold 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-marginfloorthreshold-03"),
    (4, "MAR-0004", "Enterprise Audited MarginFloorThreshold 4", 32800.00, 210.0, "ACTIVE", "uuid-marginfloorthreshold-04"),
    (5, "MAR-0005", "Executive Strategic MarginFloorThreshold 5", 65000.00, 400.0, "ACTIVE", "uuid-marginfloorthreshold-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_currencyexchangeraterules (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_currencyexchangeraterules_code ON pricing_promotions_currencyexchangeraterules(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_currencyexchangeraterules_org_status ON pricing_promotions_currencyexchangeraterules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_currencyexchangeraterules_priority ON pricing_promotions_currencyexchangeraterules(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_currencyexchangeraterules_created_at ON pricing_promotions_currencyexchangeraterules(created_at);

-- Operational seed data fixtures for pricing_promotions_currencyexchangeraterules
INSERT OR IGNORE INTO pricing_promotions_currencyexchangeraterules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUR-0001", "Primary Operational CurrencyExchangeRateRule 1", 24500.00, 150.0, "ACTIVE", "uuid-currencyexchangeraterule-01"),
    (2, "CUR-0002", "Secondary Corporate CurrencyExchangeRateRule 2", 18200.50, 80.0, "ACTIVE", "uuid-currencyexchangeraterule-02"),
    (3, "CUR-0003", "Consolidated Branch CurrencyExchangeRateRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-currencyexchangeraterule-03"),
    (4, "CUR-0004", "Enterprise Audited CurrencyExchangeRateRule 4", 32800.00, 210.0, "ACTIVE", "uuid-currencyexchangeraterule-04"),
    (5, "CUR-0005", "Executive Strategic CurrencyExchangeRateRule 5", 65000.00, 400.0, "ACTIVE", "uuid-currencyexchangeraterule-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_dynamicsurgemultipliers (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_dynamicsurgemultipliers_code ON pricing_promotions_dynamicsurgemultipliers(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_dynamicsurgemultipliers_org_status ON pricing_promotions_dynamicsurgemultipliers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_dynamicsurgemultipliers_priority ON pricing_promotions_dynamicsurgemultipliers(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_dynamicsurgemultipliers_created_at ON pricing_promotions_dynamicsurgemultipliers(created_at);

-- Operational seed data fixtures for pricing_promotions_dynamicsurgemultipliers
INSERT OR IGNORE INTO pricing_promotions_dynamicsurgemultipliers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DYN-0001", "Primary Operational DynamicSurgeMultiplier 1", 24500.00, 150.0, "ACTIVE", "uuid-dynamicsurgemultiplier-01"),
    (2, "DYN-0002", "Secondary Corporate DynamicSurgeMultiplier 2", 18200.50, 80.0, "ACTIVE", "uuid-dynamicsurgemultiplier-02"),
    (3, "DYN-0003", "Consolidated Branch DynamicSurgeMultiplier 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dynamicsurgemultiplier-03"),
    (4, "DYN-0004", "Enterprise Audited DynamicSurgeMultiplier 4", 32800.00, 210.0, "ACTIVE", "uuid-dynamicsurgemultiplier-04"),
    (5, "DYN-0005", "Executive Strategic DynamicSurgeMultiplier 5", 65000.00, 400.0, "ACTIVE", "uuid-dynamicsurgemultiplier-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_bundlepackagerules (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_bundlepackagerules_code ON pricing_promotions_bundlepackagerules(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_bundlepackagerules_org_status ON pricing_promotions_bundlepackagerules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_bundlepackagerules_priority ON pricing_promotions_bundlepackagerules(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_bundlepackagerules_created_at ON pricing_promotions_bundlepackagerules(created_at);

-- Operational seed data fixtures for pricing_promotions_bundlepackagerules
INSERT OR IGNORE INTO pricing_promotions_bundlepackagerules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BUN-0001", "Primary Operational BundlePackageRule 1", 24500.00, 150.0, "ACTIVE", "uuid-bundlepackagerule-01"),
    (2, "BUN-0002", "Secondary Corporate BundlePackageRule 2", 18200.50, 80.0, "ACTIVE", "uuid-bundlepackagerule-02"),
    (3, "BUN-0003", "Consolidated Branch BundlePackageRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bundlepackagerule-03"),
    (4, "BUN-0004", "Enterprise Audited BundlePackageRule 4", 32800.00, 210.0, "ACTIVE", "uuid-bundlepackagerule-04"),
    (5, "BUN-0005", "Executive Strategic BundlePackageRule 5", 65000.00, 400.0, "ACTIVE", "uuid-bundlepackagerule-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_channelpriceoverrides (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_channelpriceoverrides_code ON pricing_promotions_channelpriceoverrides(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_channelpriceoverrides_org_status ON pricing_promotions_channelpriceoverrides(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_channelpriceoverrides_priority ON pricing_promotions_channelpriceoverrides(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_channelpriceoverrides_created_at ON pricing_promotions_channelpriceoverrides(created_at);

-- Operational seed data fixtures for pricing_promotions_channelpriceoverrides
INSERT OR IGNORE INTO pricing_promotions_channelpriceoverrides (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHA-0001", "Primary Operational ChannelPriceOverride 1", 24500.00, 150.0, "ACTIVE", "uuid-channelpriceoverride-01"),
    (2, "CHA-0002", "Secondary Corporate ChannelPriceOverride 2", 18200.50, 80.0, "ACTIVE", "uuid-channelpriceoverride-02"),
    (3, "CHA-0003", "Consolidated Branch ChannelPriceOverride 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-channelpriceoverride-03"),
    (4, "CHA-0004", "Enterprise Audited ChannelPriceOverride 4", 32800.00, 210.0, "ACTIVE", "uuid-channelpriceoverride-04"),
    (5, "CHA-0005", "Executive Strategic ChannelPriceOverride 5", 65000.00, 400.0, "ACTIVE", "uuid-channelpriceoverride-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_pricechangeapprovals (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricechangeapprovals_code ON pricing_promotions_pricechangeapprovals(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricechangeapprovals_org_status ON pricing_promotions_pricechangeapprovals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricechangeapprovals_priority ON pricing_promotions_pricechangeapprovals(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_pricechangeapprovals_created_at ON pricing_promotions_pricechangeapprovals(created_at);

-- Operational seed data fixtures for pricing_promotions_pricechangeapprovals
INSERT OR IGNORE INTO pricing_promotions_pricechangeapprovals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PriceChangeApproval 1", 24500.00, 150.0, "ACTIVE", "uuid-pricechangeapproval-01"),
    (2, "PRI-0002", "Secondary Corporate PriceChangeApproval 2", 18200.50, 80.0, "ACTIVE", "uuid-pricechangeapproval-02"),
    (3, "PRI-0003", "Consolidated Branch PriceChangeApproval 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-pricechangeapproval-03"),
    (4, "PRI-0004", "Enterprise Audited PriceChangeApproval 4", 32800.00, 210.0, "ACTIVE", "uuid-pricechangeapproval-04"),
    (5, "PRI-0005", "Executive Strategic PriceChangeApproval 5", 65000.00, 400.0, "ACTIVE", "uuid-pricechangeapproval-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_promotionalperformances (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalperformances_code ON pricing_promotions_promotionalperformances(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalperformances_org_status ON pricing_promotions_promotionalperformances(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalperformances_priority ON pricing_promotions_promotionalperformances(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_promotionalperformances_created_at ON pricing_promotions_promotionalperformances(created_at);

-- Operational seed data fixtures for pricing_promotions_promotionalperformances
INSERT OR IGNORE INTO pricing_promotions_promotionalperformances (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational PromotionalPerformance 1", 24500.00, 150.0, "ACTIVE", "uuid-promotionalperformance-01"),
    (2, "PRO-0002", "Secondary Corporate PromotionalPerformance 2", 18200.50, 80.0, "ACTIVE", "uuid-promotionalperformance-02"),
    (3, "PRO-0003", "Consolidated Branch PromotionalPerformance 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-promotionalperformance-03"),
    (4, "PRO-0004", "Enterprise Audited PromotionalPerformance 4", 32800.00, 210.0, "ACTIVE", "uuid-promotionalperformance-04"),
    (5, "PRO-0005", "Executive Strategic PromotionalPerformance 5", 65000.00, 400.0, "ACTIVE", "uuid-promotionalperformance-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_markdownschedules (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_markdownschedules_code ON pricing_promotions_markdownschedules(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_markdownschedules_org_status ON pricing_promotions_markdownschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_markdownschedules_priority ON pricing_promotions_markdownschedules(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_markdownschedules_created_at ON pricing_promotions_markdownschedules(created_at);

-- Operational seed data fixtures for pricing_promotions_markdownschedules
INSERT OR IGNORE INTO pricing_promotions_markdownschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAR-0001", "Primary Operational MarkdownSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-markdownschedule-01"),
    (2, "MAR-0002", "Secondary Corporate MarkdownSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-markdownschedule-02"),
    (3, "MAR-0003", "Consolidated Branch MarkdownSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-markdownschedule-03"),
    (4, "MAR-0004", "Enterprise Audited MarkdownSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-markdownschedule-04"),
    (5, "MAR-0005", "Executive Strategic MarkdownSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-markdownschedule-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_loyaltypointsrules (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_loyaltypointsrules_code ON pricing_promotions_loyaltypointsrules(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_loyaltypointsrules_org_status ON pricing_promotions_loyaltypointsrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_loyaltypointsrules_priority ON pricing_promotions_loyaltypointsrules(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_loyaltypointsrules_created_at ON pricing_promotions_loyaltypointsrules(created_at);

-- Operational seed data fixtures for pricing_promotions_loyaltypointsrules
INSERT OR IGNORE INTO pricing_promotions_loyaltypointsrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LOY-0001", "Primary Operational LoyaltyPointsRule 1", 24500.00, 150.0, "ACTIVE", "uuid-loyaltypointsrule-01"),
    (2, "LOY-0002", "Secondary Corporate LoyaltyPointsRule 2", 18200.50, 80.0, "ACTIVE", "uuid-loyaltypointsrule-02"),
    (3, "LOY-0003", "Consolidated Branch LoyaltyPointsRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-loyaltypointsrule-03"),
    (4, "LOY-0004", "Enterprise Audited LoyaltyPointsRule 4", 32800.00, 210.0, "ACTIVE", "uuid-loyaltypointsrule-04"),
    (5, "LOY-0005", "Executive Strategic LoyaltyPointsRule 5", 65000.00, 400.0, "ACTIVE", "uuid-loyaltypointsrule-05");

CREATE TABLE IF NOT EXISTS pricing_promotions_priceexceptionaudits (
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

CREATE INDEX IF NOT EXISTS idx_pricing_promotions_priceexceptionaudits_code ON pricing_promotions_priceexceptionaudits(code);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_priceexceptionaudits_org_status ON pricing_promotions_priceexceptionaudits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_priceexceptionaudits_priority ON pricing_promotions_priceexceptionaudits(priority);
CREATE INDEX IF NOT EXISTS idx_pricing_promotions_priceexceptionaudits_created_at ON pricing_promotions_priceexceptionaudits(created_at);

-- Operational seed data fixtures for pricing_promotions_priceexceptionaudits
INSERT OR IGNORE INTO pricing_promotions_priceexceptionaudits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PriceExceptionAudit 1", 24500.00, 150.0, "ACTIVE", "uuid-priceexceptionaudit-01"),
    (2, "PRI-0002", "Secondary Corporate PriceExceptionAudit 2", 18200.50, 80.0, "ACTIVE", "uuid-priceexceptionaudit-02"),
    (3, "PRI-0003", "Consolidated Branch PriceExceptionAudit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-priceexceptionaudit-03"),
    (4, "PRI-0004", "Enterprise Audited PriceExceptionAudit 4", 32800.00, 210.0, "ACTIVE", "uuid-priceexceptionaudit-04"),
    (5, "PRI-0005", "Executive Strategic PriceExceptionAudit 5", 65000.00, 400.0, "ACTIVE", "uuid-priceexceptionaudit-05");

