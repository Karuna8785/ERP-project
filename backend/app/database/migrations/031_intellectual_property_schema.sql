-- SmartERP Enterprise Titan Migration 031: Intellectual Property & Patent Portfolio DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS intellectual_property_patentapplications (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentapplications_code ON intellectual_property_patentapplications(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentapplications_org_status ON intellectual_property_patentapplications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentapplications_priority ON intellectual_property_patentapplications(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentapplications_created_at ON intellectual_property_patentapplications(created_at);

-- Operational seed data fixtures for intellectual_property_patentapplications
INSERT OR IGNORE INTO intellectual_property_patentapplications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAT-0001", "Primary Operational PatentApplication 1", 24500.00, 150.0, "ACTIVE", "uuid-patentapplication-01"),
    (2, "PAT-0002", "Secondary Corporate PatentApplication 2", 18200.50, 80.0, "ACTIVE", "uuid-patentapplication-02"),
    (3, "PAT-0003", "Consolidated Branch PatentApplication 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-patentapplication-03"),
    (4, "PAT-0004", "Enterprise Audited PatentApplication 4", 32800.00, 210.0, "ACTIVE", "uuid-patentapplication-04"),
    (5, "PAT-0005", "Executive Strategic PatentApplication 5", 65000.00, 400.0, "ACTIVE", "uuid-patentapplication-05");

CREATE TABLE IF NOT EXISTS intellectual_property_trademarkregistrations (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_trademarkregistrations_code ON intellectual_property_trademarkregistrations(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_trademarkregistrations_org_status ON intellectual_property_trademarkregistrations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_trademarkregistrations_priority ON intellectual_property_trademarkregistrations(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_trademarkregistrations_created_at ON intellectual_property_trademarkregistrations(created_at);

-- Operational seed data fixtures for intellectual_property_trademarkregistrations
INSERT OR IGNORE INTO intellectual_property_trademarkregistrations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TrademarkRegistration 1", 24500.00, 150.0, "ACTIVE", "uuid-trademarkregistration-01"),
    (2, "TRA-0002", "Secondary Corporate TrademarkRegistration 2", 18200.50, 80.0, "ACTIVE", "uuid-trademarkregistration-02"),
    (3, "TRA-0003", "Consolidated Branch TrademarkRegistration 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-trademarkregistration-03"),
    (4, "TRA-0004", "Enterprise Audited TrademarkRegistration 4", 32800.00, 210.0, "ACTIVE", "uuid-trademarkregistration-04"),
    (5, "TRA-0005", "Executive Strategic TrademarkRegistration 5", 65000.00, 400.0, "ACTIVE", "uuid-trademarkregistration-05");

CREATE TABLE IF NOT EXISTS intellectual_property_copyrightfilings (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_copyrightfilings_code ON intellectual_property_copyrightfilings(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_copyrightfilings_org_status ON intellectual_property_copyrightfilings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_copyrightfilings_priority ON intellectual_property_copyrightfilings(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_copyrightfilings_created_at ON intellectual_property_copyrightfilings(created_at);

-- Operational seed data fixtures for intellectual_property_copyrightfilings
INSERT OR IGNORE INTO intellectual_property_copyrightfilings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COP-0001", "Primary Operational CopyrightFiling 1", 24500.00, 150.0, "ACTIVE", "uuid-copyrightfiling-01"),
    (2, "COP-0002", "Secondary Corporate CopyrightFiling 2", 18200.50, 80.0, "ACTIVE", "uuid-copyrightfiling-02"),
    (3, "COP-0003", "Consolidated Branch CopyrightFiling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-copyrightfiling-03"),
    (4, "COP-0004", "Enterprise Audited CopyrightFiling 4", 32800.00, 210.0, "ACTIVE", "uuid-copyrightfiling-04"),
    (5, "COP-0005", "Executive Strategic CopyrightFiling 5", 65000.00, 400.0, "ACTIVE", "uuid-copyrightfiling-05");

CREATE TABLE IF NOT EXISTS intellectual_property_tradesecretinventorys (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_tradesecretinventorys_code ON intellectual_property_tradesecretinventorys(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_tradesecretinventorys_org_status ON intellectual_property_tradesecretinventorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_tradesecretinventorys_priority ON intellectual_property_tradesecretinventorys(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_tradesecretinventorys_created_at ON intellectual_property_tradesecretinventorys(created_at);

-- Operational seed data fixtures for intellectual_property_tradesecretinventorys
INSERT OR IGNORE INTO intellectual_property_tradesecretinventorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TradeSecretInventory 1", 24500.00, 150.0, "ACTIVE", "uuid-tradesecretinventory-01"),
    (2, "TRA-0002", "Secondary Corporate TradeSecretInventory 2", 18200.50, 80.0, "ACTIVE", "uuid-tradesecretinventory-02"),
    (3, "TRA-0003", "Consolidated Branch TradeSecretInventory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tradesecretinventory-03"),
    (4, "TRA-0004", "Enterprise Audited TradeSecretInventory 4", 32800.00, 210.0, "ACTIVE", "uuid-tradesecretinventory-04"),
    (5, "TRA-0005", "Executive Strategic TradeSecretInventory 5", 65000.00, 400.0, "ACTIVE", "uuid-tradesecretinventory-05");

CREATE TABLE IF NOT EXISTS intellectual_property_inventiondisclosures (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_inventiondisclosures_code ON intellectual_property_inventiondisclosures(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_inventiondisclosures_org_status ON intellectual_property_inventiondisclosures(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_inventiondisclosures_priority ON intellectual_property_inventiondisclosures(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_inventiondisclosures_created_at ON intellectual_property_inventiondisclosures(created_at);

-- Operational seed data fixtures for intellectual_property_inventiondisclosures
INSERT OR IGNORE INTO intellectual_property_inventiondisclosures (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INV-0001", "Primary Operational InventionDisclosure 1", 24500.00, 150.0, "ACTIVE", "uuid-inventiondisclosure-01"),
    (2, "INV-0002", "Secondary Corporate InventionDisclosure 2", 18200.50, 80.0, "ACTIVE", "uuid-inventiondisclosure-02"),
    (3, "INV-0003", "Consolidated Branch InventionDisclosure 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inventiondisclosure-03"),
    (4, "INV-0004", "Enterprise Audited InventionDisclosure 4", 32800.00, 210.0, "ACTIVE", "uuid-inventiondisclosure-04"),
    (5, "INV-0005", "Executive Strategic InventionDisclosure 5", 65000.00, 400.0, "ACTIVE", "uuid-inventiondisclosure-05");

CREATE TABLE IF NOT EXISTS intellectual_property_patentofficeactions (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentofficeactions_code ON intellectual_property_patentofficeactions(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentofficeactions_org_status ON intellectual_property_patentofficeactions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentofficeactions_priority ON intellectual_property_patentofficeactions(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentofficeactions_created_at ON intellectual_property_patentofficeactions(created_at);

-- Operational seed data fixtures for intellectual_property_patentofficeactions
INSERT OR IGNORE INTO intellectual_property_patentofficeactions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAT-0001", "Primary Operational PatentOfficeAction 1", 24500.00, 150.0, "ACTIVE", "uuid-patentofficeaction-01"),
    (2, "PAT-0002", "Secondary Corporate PatentOfficeAction 2", 18200.50, 80.0, "ACTIVE", "uuid-patentofficeaction-02"),
    (3, "PAT-0003", "Consolidated Branch PatentOfficeAction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-patentofficeaction-03"),
    (4, "PAT-0004", "Enterprise Audited PatentOfficeAction 4", 32800.00, 210.0, "ACTIVE", "uuid-patentofficeaction-04"),
    (5, "PAT-0005", "Executive Strategic PatentOfficeAction 5", 65000.00, 400.0, "ACTIVE", "uuid-patentofficeaction-05");

CREATE TABLE IF NOT EXISTS intellectual_property_iproyaltyagreements (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_iproyaltyagreements_code ON intellectual_property_iproyaltyagreements(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_iproyaltyagreements_org_status ON intellectual_property_iproyaltyagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_iproyaltyagreements_priority ON intellectual_property_iproyaltyagreements(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_iproyaltyagreements_created_at ON intellectual_property_iproyaltyagreements(created_at);

-- Operational seed data fixtures for intellectual_property_iproyaltyagreements
INSERT OR IGNORE INTO intellectual_property_iproyaltyagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "IPR-0001", "Primary Operational IPRoyaltyAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-iproyaltyagreement-01"),
    (2, "IPR-0002", "Secondary Corporate IPRoyaltyAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-iproyaltyagreement-02"),
    (3, "IPR-0003", "Consolidated Branch IPRoyaltyAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-iproyaltyagreement-03"),
    (4, "IPR-0004", "Enterprise Audited IPRoyaltyAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-iproyaltyagreement-04"),
    (5, "IPR-0005", "Executive Strategic IPRoyaltyAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-iproyaltyagreement-05");

CREATE TABLE IF NOT EXISTS intellectual_property_licensegrantrights (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_licensegrantrights_code ON intellectual_property_licensegrantrights(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_licensegrantrights_org_status ON intellectual_property_licensegrantrights(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_licensegrantrights_priority ON intellectual_property_licensegrantrights(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_licensegrantrights_created_at ON intellectual_property_licensegrantrights(created_at);

-- Operational seed data fixtures for intellectual_property_licensegrantrights
INSERT OR IGNORE INTO intellectual_property_licensegrantrights (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LIC-0001", "Primary Operational LicenseGrantRight 1", 24500.00, 150.0, "ACTIVE", "uuid-licensegrantright-01"),
    (2, "LIC-0002", "Secondary Corporate LicenseGrantRight 2", 18200.50, 80.0, "ACTIVE", "uuid-licensegrantright-02"),
    (3, "LIC-0003", "Consolidated Branch LicenseGrantRight 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-licensegrantright-03"),
    (4, "LIC-0004", "Enterprise Audited LicenseGrantRight 4", 32800.00, 210.0, "ACTIVE", "uuid-licensegrantright-04"),
    (5, "LIC-0005", "Executive Strategic LicenseGrantRight 5", 65000.00, 400.0, "ACTIVE", "uuid-licensegrantright-05");

CREATE TABLE IF NOT EXISTS intellectual_property_priorartsearchs (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_priorartsearchs_code ON intellectual_property_priorartsearchs(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_priorartsearchs_org_status ON intellectual_property_priorartsearchs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_priorartsearchs_priority ON intellectual_property_priorartsearchs(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_priorartsearchs_created_at ON intellectual_property_priorartsearchs(created_at);

-- Operational seed data fixtures for intellectual_property_priorartsearchs
INSERT OR IGNORE INTO intellectual_property_priorartsearchs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PriorArtSearch 1", 24500.00, 150.0, "ACTIVE", "uuid-priorartsearch-01"),
    (2, "PRI-0002", "Secondary Corporate PriorArtSearch 2", 18200.50, 80.0, "ACTIVE", "uuid-priorartsearch-02"),
    (3, "PRI-0003", "Consolidated Branch PriorArtSearch 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-priorartsearch-03"),
    (4, "PRI-0004", "Enterprise Audited PriorArtSearch 4", 32800.00, 210.0, "ACTIVE", "uuid-priorartsearch-04"),
    (5, "PRI-0005", "Executive Strategic PriorArtSearch 5", 65000.00, 400.0, "ACTIVE", "uuid-priorartsearch-05");

CREATE TABLE IF NOT EXISTS intellectual_property_infringementmonitorings (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_infringementmonitorings_code ON intellectual_property_infringementmonitorings(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_infringementmonitorings_org_status ON intellectual_property_infringementmonitorings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_infringementmonitorings_priority ON intellectual_property_infringementmonitorings(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_infringementmonitorings_created_at ON intellectual_property_infringementmonitorings(created_at);

-- Operational seed data fixtures for intellectual_property_infringementmonitorings
INSERT OR IGNORE INTO intellectual_property_infringementmonitorings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INF-0001", "Primary Operational InfringementMonitoring 1", 24500.00, 150.0, "ACTIVE", "uuid-infringementmonitoring-01"),
    (2, "INF-0002", "Secondary Corporate InfringementMonitoring 2", 18200.50, 80.0, "ACTIVE", "uuid-infringementmonitoring-02"),
    (3, "INF-0003", "Consolidated Branch InfringementMonitoring 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-infringementmonitoring-03"),
    (4, "INF-0004", "Enterprise Audited InfringementMonitoring 4", 32800.00, 210.0, "ACTIVE", "uuid-infringementmonitoring-04"),
    (5, "INF-0005", "Executive Strategic InfringementMonitoring 5", 65000.00, 400.0, "ACTIVE", "uuid-infringementmonitoring-05");

CREATE TABLE IF NOT EXISTS intellectual_property_externalpatentcounsels (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_externalpatentcounsels_code ON intellectual_property_externalpatentcounsels(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_externalpatentcounsels_org_status ON intellectual_property_externalpatentcounsels(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_externalpatentcounsels_priority ON intellectual_property_externalpatentcounsels(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_externalpatentcounsels_created_at ON intellectual_property_externalpatentcounsels(created_at);

-- Operational seed data fixtures for intellectual_property_externalpatentcounsels
INSERT OR IGNORE INTO intellectual_property_externalpatentcounsels (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXT-0001", "Primary Operational ExternalPatentCounsel 1", 24500.00, 150.0, "ACTIVE", "uuid-externalpatentcounsel-01"),
    (2, "EXT-0002", "Secondary Corporate ExternalPatentCounsel 2", 18200.50, 80.0, "ACTIVE", "uuid-externalpatentcounsel-02"),
    (3, "EXT-0003", "Consolidated Branch ExternalPatentCounsel 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-externalpatentcounsel-03"),
    (4, "EXT-0004", "Enterprise Audited ExternalPatentCounsel 4", 32800.00, 210.0, "ACTIVE", "uuid-externalpatentcounsel-04"),
    (5, "EXT-0005", "Executive Strategic ExternalPatentCounsel 5", 65000.00, 400.0, "ACTIVE", "uuid-externalpatentcounsel-05");

CREATE TABLE IF NOT EXISTS intellectual_property_annuityfeeschedules (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_annuityfeeschedules_code ON intellectual_property_annuityfeeschedules(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_annuityfeeschedules_org_status ON intellectual_property_annuityfeeschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_annuityfeeschedules_priority ON intellectual_property_annuityfeeschedules(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_annuityfeeschedules_created_at ON intellectual_property_annuityfeeschedules(created_at);

-- Operational seed data fixtures for intellectual_property_annuityfeeschedules
INSERT OR IGNORE INTO intellectual_property_annuityfeeschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ANN-0001", "Primary Operational AnnuityFeeSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-annuityfeeschedule-01"),
    (2, "ANN-0002", "Secondary Corporate AnnuityFeeSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-annuityfeeschedule-02"),
    (3, "ANN-0003", "Consolidated Branch AnnuityFeeSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-annuityfeeschedule-03"),
    (4, "ANN-0004", "Enterprise Audited AnnuityFeeSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-annuityfeeschedule-04"),
    (5, "ANN-0005", "Executive Strategic AnnuityFeeSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-annuityfeeschedule-05");

CREATE TABLE IF NOT EXISTS intellectual_property_jointdevelopmentpacts (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_jointdevelopmentpacts_code ON intellectual_property_jointdevelopmentpacts(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_jointdevelopmentpacts_org_status ON intellectual_property_jointdevelopmentpacts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_jointdevelopmentpacts_priority ON intellectual_property_jointdevelopmentpacts(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_jointdevelopmentpacts_created_at ON intellectual_property_jointdevelopmentpacts(created_at);

-- Operational seed data fixtures for intellectual_property_jointdevelopmentpacts
INSERT OR IGNORE INTO intellectual_property_jointdevelopmentpacts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "JOI-0001", "Primary Operational JointDevelopmentPact 1", 24500.00, 150.0, "ACTIVE", "uuid-jointdevelopmentpact-01"),
    (2, "JOI-0002", "Secondary Corporate JointDevelopmentPact 2", 18200.50, 80.0, "ACTIVE", "uuid-jointdevelopmentpact-02"),
    (3, "JOI-0003", "Consolidated Branch JointDevelopmentPact 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-jointdevelopmentpact-03"),
    (4, "JOI-0004", "Enterprise Audited JointDevelopmentPact 4", 32800.00, 210.0, "ACTIVE", "uuid-jointdevelopmentpact-04"),
    (5, "JOI-0005", "Executive Strategic JointDevelopmentPact 5", 65000.00, 400.0, "ACTIVE", "uuid-jointdevelopmentpact-05");

CREATE TABLE IF NOT EXISTS intellectual_property_patentfamilymappings (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentfamilymappings_code ON intellectual_property_patentfamilymappings(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentfamilymappings_org_status ON intellectual_property_patentfamilymappings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentfamilymappings_priority ON intellectual_property_patentfamilymappings(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_patentfamilymappings_created_at ON intellectual_property_patentfamilymappings(created_at);

-- Operational seed data fixtures for intellectual_property_patentfamilymappings
INSERT OR IGNORE INTO intellectual_property_patentfamilymappings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAT-0001", "Primary Operational PatentFamilyMapping 1", 24500.00, 150.0, "ACTIVE", "uuid-patentfamilymapping-01"),
    (2, "PAT-0002", "Secondary Corporate PatentFamilyMapping 2", 18200.50, 80.0, "ACTIVE", "uuid-patentfamilymapping-02"),
    (3, "PAT-0003", "Consolidated Branch PatentFamilyMapping 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-patentfamilymapping-03"),
    (4, "PAT-0004", "Enterprise Audited PatentFamilyMapping 4", 32800.00, 210.0, "ACTIVE", "uuid-patentfamilymapping-04"),
    (5, "PAT-0005", "Executive Strategic PatentFamilyMapping 5", 65000.00, 400.0, "ACTIVE", "uuid-patentfamilymapping-05");

CREATE TABLE IF NOT EXISTS intellectual_property_commercialvaluations (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_commercialvaluations_code ON intellectual_property_commercialvaluations(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_commercialvaluations_org_status ON intellectual_property_commercialvaluations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_commercialvaluations_priority ON intellectual_property_commercialvaluations(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_commercialvaluations_created_at ON intellectual_property_commercialvaluations(created_at);

-- Operational seed data fixtures for intellectual_property_commercialvaluations
INSERT OR IGNORE INTO intellectual_property_commercialvaluations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CommercialValuation 1", 24500.00, 150.0, "ACTIVE", "uuid-commercialvaluation-01"),
    (2, "COM-0002", "Secondary Corporate CommercialValuation 2", 18200.50, 80.0, "ACTIVE", "uuid-commercialvaluation-02"),
    (3, "COM-0003", "Consolidated Branch CommercialValuation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-commercialvaluation-03"),
    (4, "COM-0004", "Enterprise Audited CommercialValuation 4", 32800.00, 210.0, "ACTIVE", "uuid-commercialvaluation-04"),
    (5, "COM-0005", "Executive Strategic CommercialValuation 5", 65000.00, 400.0, "ACTIVE", "uuid-commercialvaluation-05");

CREATE TABLE IF NOT EXISTS intellectual_property_technologytransfers (
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

CREATE INDEX IF NOT EXISTS idx_intellectual_property_technologytransfers_code ON intellectual_property_technologytransfers(code);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_technologytransfers_org_status ON intellectual_property_technologytransfers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_technologytransfers_priority ON intellectual_property_technologytransfers(priority);
CREATE INDEX IF NOT EXISTS idx_intellectual_property_technologytransfers_created_at ON intellectual_property_technologytransfers(created_at);

-- Operational seed data fixtures for intellectual_property_technologytransfers
INSERT OR IGNORE INTO intellectual_property_technologytransfers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEC-0001", "Primary Operational TechnologyTransfer 1", 24500.00, 150.0, "ACTIVE", "uuid-technologytransfer-01"),
    (2, "TEC-0002", "Secondary Corporate TechnologyTransfer 2", 18200.50, 80.0, "ACTIVE", "uuid-technologytransfer-02"),
    (3, "TEC-0003", "Consolidated Branch TechnologyTransfer 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-technologytransfer-03"),
    (4, "TEC-0004", "Enterprise Audited TechnologyTransfer 4", 32800.00, 210.0, "ACTIVE", "uuid-technologytransfer-04"),
    (5, "TEC-0005", "Executive Strategic TechnologyTransfer 5", 65000.00, 400.0, "ACTIVE", "uuid-technologytransfer-05");

