-- SmartERP Enterprise Titan Migration 009: Strategic Procurement & Sourcing DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS procurement_advanced_sourcingrequests (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_sourcingrequests_code ON procurement_advanced_sourcingrequests(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_sourcingrequests_org_status ON procurement_advanced_sourcingrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_sourcingrequests_priority ON procurement_advanced_sourcingrequests(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_sourcingrequests_created_at ON procurement_advanced_sourcingrequests(created_at);

-- Operational seed data fixtures for procurement_advanced_sourcingrequests
INSERT OR IGNORE INTO procurement_advanced_sourcingrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SOU-0001", "Primary Operational SourcingRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-sourcingrequest-01"),
    (2, "SOU-0002", "Secondary Corporate SourcingRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-sourcingrequest-02"),
    (3, "SOU-0003", "Consolidated Branch SourcingRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sourcingrequest-03"),
    (4, "SOU-0004", "Enterprise Audited SourcingRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-sourcingrequest-04"),
    (5, "SOU-0005", "Executive Strategic SourcingRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-sourcingrequest-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_vendorquotes (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorquotes_code ON procurement_advanced_vendorquotes(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorquotes_org_status ON procurement_advanced_vendorquotes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorquotes_priority ON procurement_advanced_vendorquotes(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorquotes_created_at ON procurement_advanced_vendorquotes(created_at);

-- Operational seed data fixtures for procurement_advanced_vendorquotes
INSERT OR IGNORE INTO procurement_advanced_vendorquotes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorQuote 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorquote-01"),
    (2, "VEN-0002", "Secondary Corporate VendorQuote 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorquote-02"),
    (3, "VEN-0003", "Consolidated Branch VendorQuote 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorquote-03"),
    (4, "VEN-0004", "Enterprise Audited VendorQuote 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorquote-04"),
    (5, "VEN-0005", "Executive Strategic VendorQuote 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorquote-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_bidcomparisons (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_bidcomparisons_code ON procurement_advanced_bidcomparisons(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_bidcomparisons_org_status ON procurement_advanced_bidcomparisons(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_bidcomparisons_priority ON procurement_advanced_bidcomparisons(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_bidcomparisons_created_at ON procurement_advanced_bidcomparisons(created_at);

-- Operational seed data fixtures for procurement_advanced_bidcomparisons
INSERT OR IGNORE INTO procurement_advanced_bidcomparisons (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BID-0001", "Primary Operational BidComparison 1", 24500.00, 150.0, "ACTIVE", "uuid-bidcomparison-01"),
    (2, "BID-0002", "Secondary Corporate BidComparison 2", 18200.50, 80.0, "ACTIVE", "uuid-bidcomparison-02"),
    (3, "BID-0003", "Consolidated Branch BidComparison 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bidcomparison-03"),
    (4, "BID-0004", "Enterprise Audited BidComparison 4", 32800.00, 210.0, "ACTIVE", "uuid-bidcomparison-04"),
    (5, "BID-0005", "Executive Strategic BidComparison 5", 65000.00, 400.0, "ACTIVE", "uuid-bidcomparison-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_contractagreements (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_contractagreements_code ON procurement_advanced_contractagreements(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_contractagreements_org_status ON procurement_advanced_contractagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_contractagreements_priority ON procurement_advanced_contractagreements(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_contractagreements_created_at ON procurement_advanced_contractagreements(created_at);

-- Operational seed data fixtures for procurement_advanced_contractagreements
INSERT OR IGNORE INTO procurement_advanced_contractagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContractAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-contractagreement-01"),
    (2, "CON-0002", "Secondary Corporate ContractAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-contractagreement-02"),
    (3, "CON-0003", "Consolidated Branch ContractAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-contractagreement-03"),
    (4, "CON-0004", "Enterprise Audited ContractAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-contractagreement-04"),
    (5, "CON-0005", "Executive Strategic ContractAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-contractagreement-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_purchaserequisitions (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchaserequisitions_code ON procurement_advanced_purchaserequisitions(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchaserequisitions_org_status ON procurement_advanced_purchaserequisitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchaserequisitions_priority ON procurement_advanced_purchaserequisitions(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchaserequisitions_created_at ON procurement_advanced_purchaserequisitions(created_at);

-- Operational seed data fixtures for procurement_advanced_purchaserequisitions
INSERT OR IGNORE INTO procurement_advanced_purchaserequisitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PUR-0001", "Primary Operational PurchaseRequisition 1", 24500.00, 150.0, "ACTIVE", "uuid-purchaserequisition-01"),
    (2, "PUR-0002", "Secondary Corporate PurchaseRequisition 2", 18200.50, 80.0, "ACTIVE", "uuid-purchaserequisition-02"),
    (3, "PUR-0003", "Consolidated Branch PurchaseRequisition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-purchaserequisition-03"),
    (4, "PUR-0004", "Enterprise Audited PurchaseRequisition 4", 32800.00, 210.0, "ACTIVE", "uuid-purchaserequisition-04"),
    (5, "PUR-0005", "Executive Strategic PurchaseRequisition 5", 65000.00, 400.0, "ACTIVE", "uuid-purchaserequisition-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_blanketpos (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_blanketpos_code ON procurement_advanced_blanketpos(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_blanketpos_org_status ON procurement_advanced_blanketpos(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_blanketpos_priority ON procurement_advanced_blanketpos(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_blanketpos_created_at ON procurement_advanced_blanketpos(created_at);

-- Operational seed data fixtures for procurement_advanced_blanketpos
INSERT OR IGNORE INTO procurement_advanced_blanketpos (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BLA-0001", "Primary Operational BlanketPO 1", 24500.00, 150.0, "ACTIVE", "uuid-blanketpo-01"),
    (2, "BLA-0002", "Secondary Corporate BlanketPO 2", 18200.50, 80.0, "ACTIVE", "uuid-blanketpo-02"),
    (3, "BLA-0003", "Consolidated Branch BlanketPO 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-blanketpo-03"),
    (4, "BLA-0004", "Enterprise Audited BlanketPO 4", 32800.00, 210.0, "ACTIVE", "uuid-blanketpo-04"),
    (5, "BLA-0005", "Executive Strategic BlanketPO 5", 65000.00, 400.0, "ACTIVE", "uuid-blanketpo-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_vendorscorecards (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorscorecards_code ON procurement_advanced_vendorscorecards(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorscorecards_org_status ON procurement_advanced_vendorscorecards(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorscorecards_priority ON procurement_advanced_vendorscorecards(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_vendorscorecards_created_at ON procurement_advanced_vendorscorecards(created_at);

-- Operational seed data fixtures for procurement_advanced_vendorscorecards
INSERT OR IGNORE INTO procurement_advanced_vendorscorecards (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorScorecard 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorscorecard-01"),
    (2, "VEN-0002", "Secondary Corporate VendorScorecard 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorscorecard-02"),
    (3, "VEN-0003", "Consolidated Branch VendorScorecard 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorscorecard-03"),
    (4, "VEN-0004", "Enterprise Audited VendorScorecard 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorscorecard-04"),
    (5, "VEN-0005", "Executive Strategic VendorScorecard 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorscorecard-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_spendcategorys (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_spendcategorys_code ON procurement_advanced_spendcategorys(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_spendcategorys_org_status ON procurement_advanced_spendcategorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_spendcategorys_priority ON procurement_advanced_spendcategorys(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_spendcategorys_created_at ON procurement_advanced_spendcategorys(created_at);

-- Operational seed data fixtures for procurement_advanced_spendcategorys
INSERT OR IGNORE INTO procurement_advanced_spendcategorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SPE-0001", "Primary Operational SpendCategory 1", 24500.00, 150.0, "ACTIVE", "uuid-spendcategory-01"),
    (2, "SPE-0002", "Secondary Corporate SpendCategory 2", 18200.50, 80.0, "ACTIVE", "uuid-spendcategory-02"),
    (3, "SPE-0003", "Consolidated Branch SpendCategory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-spendcategory-03"),
    (4, "SPE-0004", "Enterprise Audited SpendCategory 4", 32800.00, 210.0, "ACTIVE", "uuid-spendcategory-04"),
    (5, "SPE-0005", "Executive Strategic SpendCategory 5", 65000.00, 400.0, "ACTIVE", "uuid-spendcategory-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_procurementpolicys (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_procurementpolicys_code ON procurement_advanced_procurementpolicys(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_procurementpolicys_org_status ON procurement_advanced_procurementpolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_procurementpolicys_priority ON procurement_advanced_procurementpolicys(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_procurementpolicys_created_at ON procurement_advanced_procurementpolicys(created_at);

-- Operational seed data fixtures for procurement_advanced_procurementpolicys
INSERT OR IGNORE INTO procurement_advanced_procurementpolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProcurementPolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-procurementpolicy-01"),
    (2, "PRO-0002", "Secondary Corporate ProcurementPolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-procurementpolicy-02"),
    (3, "PRO-0003", "Consolidated Branch ProcurementPolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-procurementpolicy-03"),
    (4, "PRO-0004", "Enterprise Audited ProcurementPolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-procurementpolicy-04"),
    (5, "PRO-0005", "Executive Strategic ProcurementPolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-procurementpolicy-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_catalogitems (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_catalogitems_code ON procurement_advanced_catalogitems(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_catalogitems_org_status ON procurement_advanced_catalogitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_catalogitems_priority ON procurement_advanced_catalogitems(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_catalogitems_created_at ON procurement_advanced_catalogitems(created_at);

-- Operational seed data fixtures for procurement_advanced_catalogitems
INSERT OR IGNORE INTO procurement_advanced_catalogitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAT-0001", "Primary Operational CatalogItem 1", 24500.00, 150.0, "ACTIVE", "uuid-catalogitem-01"),
    (2, "CAT-0002", "Secondary Corporate CatalogItem 2", 18200.50, 80.0, "ACTIVE", "uuid-catalogitem-02"),
    (3, "CAT-0003", "Consolidated Branch CatalogItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-catalogitem-03"),
    (4, "CAT-0004", "Enterprise Audited CatalogItem 4", 32800.00, 210.0, "ACTIVE", "uuid-catalogitem-04"),
    (5, "CAT-0005", "Executive Strategic CatalogItem 5", 65000.00, 400.0, "ACTIVE", "uuid-catalogitem-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_suppliertiers (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_suppliertiers_code ON procurement_advanced_suppliertiers(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_suppliertiers_org_status ON procurement_advanced_suppliertiers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_suppliertiers_priority ON procurement_advanced_suppliertiers(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_suppliertiers_created_at ON procurement_advanced_suppliertiers(created_at);

-- Operational seed data fixtures for procurement_advanced_suppliertiers
INSERT OR IGNORE INTO procurement_advanced_suppliertiers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierTier 1", 24500.00, 150.0, "ACTIVE", "uuid-suppliertier-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierTier 2", 18200.50, 80.0, "ACTIVE", "uuid-suppliertier-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierTier 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-suppliertier-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierTier 4", 32800.00, 210.0, "ACTIVE", "uuid-suppliertier-04"),
    (5, "SUP-0005", "Executive Strategic SupplierTier 5", 65000.00, 400.0, "ACTIVE", "uuid-suppliertier-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_rebateprograms (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_rebateprograms_code ON procurement_advanced_rebateprograms(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_rebateprograms_org_status ON procurement_advanced_rebateprograms(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_rebateprograms_priority ON procurement_advanced_rebateprograms(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_rebateprograms_created_at ON procurement_advanced_rebateprograms(created_at);

-- Operational seed data fixtures for procurement_advanced_rebateprograms
INSERT OR IGNORE INTO procurement_advanced_rebateprograms (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REB-0001", "Primary Operational RebateProgram 1", 24500.00, 150.0, "ACTIVE", "uuid-rebateprogram-01"),
    (2, "REB-0002", "Secondary Corporate RebateProgram 2", 18200.50, 80.0, "ACTIVE", "uuid-rebateprogram-02"),
    (3, "REB-0003", "Consolidated Branch RebateProgram 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-rebateprogram-03"),
    (4, "REB-0004", "Enterprise Audited RebateProgram 4", 32800.00, 210.0, "ACTIVE", "uuid-rebateprogram-04"),
    (5, "REB-0005", "Executive Strategic RebateProgram 5", 65000.00, 400.0, "ACTIVE", "uuid-rebateprogram-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_freightrateagreements (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_freightrateagreements_code ON procurement_advanced_freightrateagreements(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_freightrateagreements_org_status ON procurement_advanced_freightrateagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_freightrateagreements_priority ON procurement_advanced_freightrateagreements(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_freightrateagreements_created_at ON procurement_advanced_freightrateagreements(created_at);

-- Operational seed data fixtures for procurement_advanced_freightrateagreements
INSERT OR IGNORE INTO procurement_advanced_freightrateagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FRE-0001", "Primary Operational FreightRateAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-freightrateagreement-01"),
    (2, "FRE-0002", "Secondary Corporate FreightRateAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-freightrateagreement-02"),
    (3, "FRE-0003", "Consolidated Branch FreightRateAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-freightrateagreement-03"),
    (4, "FRE-0004", "Enterprise Audited FreightRateAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-freightrateagreement-04"),
    (5, "FRE-0005", "Executive Strategic FreightRateAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-freightrateagreement-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_importpermits (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_importpermits_code ON procurement_advanced_importpermits(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_importpermits_org_status ON procurement_advanced_importpermits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_importpermits_priority ON procurement_advanced_importpermits(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_importpermits_created_at ON procurement_advanced_importpermits(created_at);

-- Operational seed data fixtures for procurement_advanced_importpermits
INSERT OR IGNORE INTO procurement_advanced_importpermits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "IMP-0001", "Primary Operational ImportPermit 1", 24500.00, 150.0, "ACTIVE", "uuid-importpermit-01"),
    (2, "IMP-0002", "Secondary Corporate ImportPermit 2", 18200.50, 80.0, "ACTIVE", "uuid-importpermit-02"),
    (3, "IMP-0003", "Consolidated Branch ImportPermit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-importpermit-03"),
    (4, "IMP-0004", "Enterprise Audited ImportPermit 4", 32800.00, 210.0, "ACTIVE", "uuid-importpermit-04"),
    (5, "IMP-0005", "Executive Strategic ImportPermit 5", 65000.00, 400.0, "ACTIVE", "uuid-importpermit-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_purchasereturns (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchasereturns_code ON procurement_advanced_purchasereturns(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchasereturns_org_status ON procurement_advanced_purchasereturns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchasereturns_priority ON procurement_advanced_purchasereturns(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_purchasereturns_created_at ON procurement_advanced_purchasereturns(created_at);

-- Operational seed data fixtures for procurement_advanced_purchasereturns
INSERT OR IGNORE INTO procurement_advanced_purchasereturns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PUR-0001", "Primary Operational PurchaseReturn 1", 24500.00, 150.0, "ACTIVE", "uuid-purchasereturn-01"),
    (2, "PUR-0002", "Secondary Corporate PurchaseReturn 2", 18200.50, 80.0, "ACTIVE", "uuid-purchasereturn-02"),
    (3, "PUR-0003", "Consolidated Branch PurchaseReturn 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-purchasereturn-03"),
    (4, "PUR-0004", "Enterprise Audited PurchaseReturn 4", 32800.00, 210.0, "ACTIVE", "uuid-purchasereturn-04"),
    (5, "PUR-0005", "Executive Strategic PurchaseReturn 5", 65000.00, 400.0, "ACTIVE", "uuid-purchasereturn-05");

CREATE TABLE IF NOT EXISTS procurement_advanced_paymentschedules (
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

CREATE INDEX IF NOT EXISTS idx_procurement_advanced_paymentschedules_code ON procurement_advanced_paymentschedules(code);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_paymentschedules_org_status ON procurement_advanced_paymentschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_paymentschedules_priority ON procurement_advanced_paymentschedules(priority);
CREATE INDEX IF NOT EXISTS idx_procurement_advanced_paymentschedules_created_at ON procurement_advanced_paymentschedules(created_at);

-- Operational seed data fixtures for procurement_advanced_paymentschedules
INSERT OR IGNORE INTO procurement_advanced_paymentschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAY-0001", "Primary Operational PaymentSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-paymentschedule-01"),
    (2, "PAY-0002", "Secondary Corporate PaymentSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-paymentschedule-02"),
    (3, "PAY-0003", "Consolidated Branch PaymentSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-paymentschedule-03"),
    (4, "PAY-0004", "Enterprise Audited PaymentSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-paymentschedule-04"),
    (5, "PAY-0005", "Executive Strategic PaymentSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-paymentschedule-05");

