-- SmartERP Enterprise Titan Migration 032: Enterprise Legal Operations & Matter Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS legal_counsel_legalmattercases (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalmattercases_code ON legal_counsel_legalmattercases(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalmattercases_org_status ON legal_counsel_legalmattercases(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalmattercases_priority ON legal_counsel_legalmattercases(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalmattercases_created_at ON legal_counsel_legalmattercases(created_at);

-- Operational seed data fixtures for legal_counsel_legalmattercases
INSERT OR IGNORE INTO legal_counsel_legalmattercases (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEG-0001", "Primary Operational LegalMatterCase 1", 24500.00, 150.0, "ACTIVE", "uuid-legalmattercase-01"),
    (2, "LEG-0002", "Secondary Corporate LegalMatterCase 2", 18200.50, 80.0, "ACTIVE", "uuid-legalmattercase-02"),
    (3, "LEG-0003", "Consolidated Branch LegalMatterCase 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-legalmattercase-03"),
    (4, "LEG-0004", "Enterprise Audited LegalMatterCase 4", 32800.00, 210.0, "ACTIVE", "uuid-legalmattercase-04"),
    (5, "LEG-0005", "Executive Strategic LegalMatterCase 5", 65000.00, 400.0, "ACTIVE", "uuid-legalmattercase-05");

CREATE TABLE IF NOT EXISTS legal_counsel_litigationdockets (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_litigationdockets_code ON legal_counsel_litigationdockets(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_litigationdockets_org_status ON legal_counsel_litigationdockets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_litigationdockets_priority ON legal_counsel_litigationdockets(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_litigationdockets_created_at ON legal_counsel_litigationdockets(created_at);

-- Operational seed data fixtures for legal_counsel_litigationdockets
INSERT OR IGNORE INTO legal_counsel_litigationdockets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LIT-0001", "Primary Operational LitigationDocket 1", 24500.00, 150.0, "ACTIVE", "uuid-litigationdocket-01"),
    (2, "LIT-0002", "Secondary Corporate LitigationDocket 2", 18200.50, 80.0, "ACTIVE", "uuid-litigationdocket-02"),
    (3, "LIT-0003", "Consolidated Branch LitigationDocket 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-litigationdocket-03"),
    (4, "LIT-0004", "Enterprise Audited LitigationDocket 4", 32800.00, 210.0, "ACTIVE", "uuid-litigationdocket-04"),
    (5, "LIT-0005", "Executive Strategic LitigationDocket 5", 65000.00, 400.0, "ACTIVE", "uuid-litigationdocket-05");

CREATE TABLE IF NOT EXISTS legal_counsel_outsidecounselbillings (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_outsidecounselbillings_code ON legal_counsel_outsidecounselbillings(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_outsidecounselbillings_org_status ON legal_counsel_outsidecounselbillings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_outsidecounselbillings_priority ON legal_counsel_outsidecounselbillings(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_outsidecounselbillings_created_at ON legal_counsel_outsidecounselbillings(created_at);

-- Operational seed data fixtures for legal_counsel_outsidecounselbillings
INSERT OR IGNORE INTO legal_counsel_outsidecounselbillings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OUT-0001", "Primary Operational OutsideCounselBilling 1", 24500.00, 150.0, "ACTIVE", "uuid-outsidecounselbilling-01"),
    (2, "OUT-0002", "Secondary Corporate OutsideCounselBilling 2", 18200.50, 80.0, "ACTIVE", "uuid-outsidecounselbilling-02"),
    (3, "OUT-0003", "Consolidated Branch OutsideCounselBilling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-outsidecounselbilling-03"),
    (4, "OUT-0004", "Enterprise Audited OutsideCounselBilling 4", 32800.00, 210.0, "ACTIVE", "uuid-outsidecounselbilling-04"),
    (5, "OUT-0005", "Executive Strategic OutsideCounselBilling 5", 65000.00, 400.0, "ACTIVE", "uuid-outsidecounselbilling-05");

CREATE TABLE IF NOT EXISTS legal_counsel_legalholdorders (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalholdorders_code ON legal_counsel_legalholdorders(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalholdorders_org_status ON legal_counsel_legalholdorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalholdorders_priority ON legal_counsel_legalholdorders(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalholdorders_created_at ON legal_counsel_legalholdorders(created_at);

-- Operational seed data fixtures for legal_counsel_legalholdorders
INSERT OR IGNORE INTO legal_counsel_legalholdorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEG-0001", "Primary Operational LegalHoldOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-legalholdorder-01"),
    (2, "LEG-0002", "Secondary Corporate LegalHoldOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-legalholdorder-02"),
    (3, "LEG-0003", "Consolidated Branch LegalHoldOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-legalholdorder-03"),
    (4, "LEG-0004", "Enterprise Audited LegalHoldOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-legalholdorder-04"),
    (5, "LEG-0005", "Executive Strategic LegalHoldOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-legalholdorder-05");

CREATE TABLE IF NOT EXISTS legal_counsel_discoveryrequestesis (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_discoveryrequestesis_code ON legal_counsel_discoveryrequestesis(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_discoveryrequestesis_org_status ON legal_counsel_discoveryrequestesis(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_discoveryrequestesis_priority ON legal_counsel_discoveryrequestesis(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_discoveryrequestesis_created_at ON legal_counsel_discoveryrequestesis(created_at);

-- Operational seed data fixtures for legal_counsel_discoveryrequestesis
INSERT OR IGNORE INTO legal_counsel_discoveryrequestesis (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DiscoveryRequestEsi 1", 24500.00, 150.0, "ACTIVE", "uuid-discoveryrequestesi-01"),
    (2, "DIS-0002", "Secondary Corporate DiscoveryRequestEsi 2", 18200.50, 80.0, "ACTIVE", "uuid-discoveryrequestesi-02"),
    (3, "DIS-0003", "Consolidated Branch DiscoveryRequestEsi 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-discoveryrequestesi-03"),
    (4, "DIS-0004", "Enterprise Audited DiscoveryRequestEsi 4", 32800.00, 210.0, "ACTIVE", "uuid-discoveryrequestesi-04"),
    (5, "DIS-0005", "Executive Strategic DiscoveryRequestEsi 5", 65000.00, 400.0, "ACTIVE", "uuid-discoveryrequestesi-05");

CREATE TABLE IF NOT EXISTS legal_counsel_depositionschedules (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_depositionschedules_code ON legal_counsel_depositionschedules(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_depositionschedules_org_status ON legal_counsel_depositionschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_depositionschedules_priority ON legal_counsel_depositionschedules(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_depositionschedules_created_at ON legal_counsel_depositionschedules(created_at);

-- Operational seed data fixtures for legal_counsel_depositionschedules
INSERT OR IGNORE INTO legal_counsel_depositionschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DepositionSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-depositionschedule-01"),
    (2, "DEP-0002", "Secondary Corporate DepositionSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-depositionschedule-02"),
    (3, "DEP-0003", "Consolidated Branch DepositionSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-depositionschedule-03"),
    (4, "DEP-0004", "Enterprise Audited DepositionSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-depositionschedule-04"),
    (5, "DEP-0005", "Executive Strategic DepositionSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-depositionschedule-05");

CREATE TABLE IF NOT EXISTS legal_counsel_subpoenaresponses (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_subpoenaresponses_code ON legal_counsel_subpoenaresponses(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_subpoenaresponses_org_status ON legal_counsel_subpoenaresponses(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_subpoenaresponses_priority ON legal_counsel_subpoenaresponses(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_subpoenaresponses_created_at ON legal_counsel_subpoenaresponses(created_at);

-- Operational seed data fixtures for legal_counsel_subpoenaresponses
INSERT OR IGNORE INTO legal_counsel_subpoenaresponses (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUB-0001", "Primary Operational SubpoenaResponse 1", 24500.00, 150.0, "ACTIVE", "uuid-subpoenaresponse-01"),
    (2, "SUB-0002", "Secondary Corporate SubpoenaResponse 2", 18200.50, 80.0, "ACTIVE", "uuid-subpoenaresponse-02"),
    (3, "SUB-0003", "Consolidated Branch SubpoenaResponse 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-subpoenaresponse-03"),
    (4, "SUB-0004", "Enterprise Audited SubpoenaResponse 4", 32800.00, 210.0, "ACTIVE", "uuid-subpoenaresponse-04"),
    (5, "SUB-0005", "Executive Strategic SubpoenaResponse 5", 65000.00, 400.0, "ACTIVE", "uuid-subpoenaresponse-05");

CREATE TABLE IF NOT EXISTS legal_counsel_settlementagreements (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_settlementagreements_code ON legal_counsel_settlementagreements(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_settlementagreements_org_status ON legal_counsel_settlementagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_settlementagreements_priority ON legal_counsel_settlementagreements(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_settlementagreements_created_at ON legal_counsel_settlementagreements(created_at);

-- Operational seed data fixtures for legal_counsel_settlementagreements
INSERT OR IGNORE INTO legal_counsel_settlementagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SET-0001", "Primary Operational SettlementAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-settlementagreement-01"),
    (2, "SET-0002", "Secondary Corporate SettlementAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-settlementagreement-02"),
    (3, "SET-0003", "Consolidated Branch SettlementAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-settlementagreement-03"),
    (4, "SET-0004", "Enterprise Audited SettlementAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-settlementagreement-04"),
    (5, "SET-0005", "Executive Strategic SettlementAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-settlementagreement-05");

CREATE TABLE IF NOT EXISTS legal_counsel_regulatoryinquirycases (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_regulatoryinquirycases_code ON legal_counsel_regulatoryinquirycases(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_regulatoryinquirycases_org_status ON legal_counsel_regulatoryinquirycases(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_regulatoryinquirycases_priority ON legal_counsel_regulatoryinquirycases(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_regulatoryinquirycases_created_at ON legal_counsel_regulatoryinquirycases(created_at);

-- Operational seed data fixtures for legal_counsel_regulatoryinquirycases
INSERT OR IGNORE INTO legal_counsel_regulatoryinquirycases (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REG-0001", "Primary Operational RegulatoryInquiryCase 1", 24500.00, 150.0, "ACTIVE", "uuid-regulatoryinquirycase-01"),
    (2, "REG-0002", "Secondary Corporate RegulatoryInquiryCase 2", 18200.50, 80.0, "ACTIVE", "uuid-regulatoryinquirycase-02"),
    (3, "REG-0003", "Consolidated Branch RegulatoryInquiryCase 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-regulatoryinquirycase-03"),
    (4, "REG-0004", "Enterprise Audited RegulatoryInquiryCase 4", 32800.00, 210.0, "ACTIVE", "uuid-regulatoryinquirycase-04"),
    (5, "REG-0005", "Executive Strategic RegulatoryInquiryCase 5", 65000.00, 400.0, "ACTIVE", "uuid-regulatoryinquirycase-05");

CREATE TABLE IF NOT EXISTS legal_counsel_courtfilingdocs (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_courtfilingdocs_code ON legal_counsel_courtfilingdocs(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_courtfilingdocs_org_status ON legal_counsel_courtfilingdocs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_courtfilingdocs_priority ON legal_counsel_courtfilingdocs(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_courtfilingdocs_created_at ON legal_counsel_courtfilingdocs(created_at);

-- Operational seed data fixtures for legal_counsel_courtfilingdocs
INSERT OR IGNORE INTO legal_counsel_courtfilingdocs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COU-0001", "Primary Operational CourtFilingDoc 1", 24500.00, 150.0, "ACTIVE", "uuid-courtfilingdoc-01"),
    (2, "COU-0002", "Secondary Corporate CourtFilingDoc 2", 18200.50, 80.0, "ACTIVE", "uuid-courtfilingdoc-02"),
    (3, "COU-0003", "Consolidated Branch CourtFilingDoc 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-courtfilingdoc-03"),
    (4, "COU-0004", "Enterprise Audited CourtFilingDoc 4", 32800.00, 210.0, "ACTIVE", "uuid-courtfilingdoc-04"),
    (5, "COU-0005", "Executive Strategic CourtFilingDoc 5", 65000.00, 400.0, "ACTIVE", "uuid-courtfilingdoc-05");

CREATE TABLE IF NOT EXISTS legal_counsel_legalbudgetforecasts (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalbudgetforecasts_code ON legal_counsel_legalbudgetforecasts(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalbudgetforecasts_org_status ON legal_counsel_legalbudgetforecasts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalbudgetforecasts_priority ON legal_counsel_legalbudgetforecasts(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalbudgetforecasts_created_at ON legal_counsel_legalbudgetforecasts(created_at);

-- Operational seed data fixtures for legal_counsel_legalbudgetforecasts
INSERT OR IGNORE INTO legal_counsel_legalbudgetforecasts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEG-0001", "Primary Operational LegalBudgetForecast 1", 24500.00, 150.0, "ACTIVE", "uuid-legalbudgetforecast-01"),
    (2, "LEG-0002", "Secondary Corporate LegalBudgetForecast 2", 18200.50, 80.0, "ACTIVE", "uuid-legalbudgetforecast-02"),
    (3, "LEG-0003", "Consolidated Branch LegalBudgetForecast 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-legalbudgetforecast-03"),
    (4, "LEG-0004", "Enterprise Audited LegalBudgetForecast 4", 32800.00, 210.0, "ACTIVE", "uuid-legalbudgetforecast-04"),
    (5, "LEG-0005", "Executive Strategic LegalBudgetForecast 5", 65000.00, 400.0, "ACTIVE", "uuid-legalbudgetforecast-05");

CREATE TABLE IF NOT EXISTS legal_counsel_legalspendinvoices (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalspendinvoices_code ON legal_counsel_legalspendinvoices(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalspendinvoices_org_status ON legal_counsel_legalspendinvoices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalspendinvoices_priority ON legal_counsel_legalspendinvoices(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_legalspendinvoices_created_at ON legal_counsel_legalspendinvoices(created_at);

-- Operational seed data fixtures for legal_counsel_legalspendinvoices
INSERT OR IGNORE INTO legal_counsel_legalspendinvoices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEG-0001", "Primary Operational LegalSpendInvoice 1", 24500.00, 150.0, "ACTIVE", "uuid-legalspendinvoice-01"),
    (2, "LEG-0002", "Secondary Corporate LegalSpendInvoice 2", 18200.50, 80.0, "ACTIVE", "uuid-legalspendinvoice-02"),
    (3, "LEG-0003", "Consolidated Branch LegalSpendInvoice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-legalspendinvoice-03"),
    (4, "LEG-0004", "Enterprise Audited LegalSpendInvoice 4", 32800.00, 210.0, "ACTIVE", "uuid-legalspendinvoice-04"),
    (5, "LEG-0005", "Executive Strategic LegalSpendInvoice 5", 65000.00, 400.0, "ACTIVE", "uuid-legalspendinvoice-05");

CREATE TABLE IF NOT EXISTS legal_counsel_expertwitnessretainers (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_expertwitnessretainers_code ON legal_counsel_expertwitnessretainers(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_expertwitnessretainers_org_status ON legal_counsel_expertwitnessretainers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_expertwitnessretainers_priority ON legal_counsel_expertwitnessretainers(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_expertwitnessretainers_created_at ON legal_counsel_expertwitnessretainers(created_at);

-- Operational seed data fixtures for legal_counsel_expertwitnessretainers
INSERT OR IGNORE INTO legal_counsel_expertwitnessretainers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExpertWitnessRetainer 1", 24500.00, 150.0, "ACTIVE", "uuid-expertwitnessretainer-01"),
    (2, "EXP-0002", "Secondary Corporate ExpertWitnessRetainer 2", 18200.50, 80.0, "ACTIVE", "uuid-expertwitnessretainer-02"),
    (3, "EXP-0003", "Consolidated Branch ExpertWitnessRetainer 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-expertwitnessretainer-03"),
    (4, "EXP-0004", "Enterprise Audited ExpertWitnessRetainer 4", 32800.00, 210.0, "ACTIVE", "uuid-expertwitnessretainer-04"),
    (5, "EXP-0005", "Executive Strategic ExpertWitnessRetainer 5", 65000.00, 400.0, "ACTIVE", "uuid-expertwitnessretainer-05");

CREATE TABLE IF NOT EXISTS legal_counsel_privilegelogdocuments (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_privilegelogdocuments_code ON legal_counsel_privilegelogdocuments(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_privilegelogdocuments_org_status ON legal_counsel_privilegelogdocuments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_privilegelogdocuments_priority ON legal_counsel_privilegelogdocuments(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_privilegelogdocuments_created_at ON legal_counsel_privilegelogdocuments(created_at);

-- Operational seed data fixtures for legal_counsel_privilegelogdocuments
INSERT OR IGNORE INTO legal_counsel_privilegelogdocuments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PrivilegeLogDocument 1", 24500.00, 150.0, "ACTIVE", "uuid-privilegelogdocument-01"),
    (2, "PRI-0002", "Secondary Corporate PrivilegeLogDocument 2", 18200.50, 80.0, "ACTIVE", "uuid-privilegelogdocument-02"),
    (3, "PRI-0003", "Consolidated Branch PrivilegeLogDocument 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-privilegelogdocument-03"),
    (4, "PRI-0004", "Enterprise Audited PrivilegeLogDocument 4", 32800.00, 210.0, "ACTIVE", "uuid-privilegelogdocument-04"),
    (5, "PRI-0005", "Executive Strategic PrivilegeLogDocument 5", 65000.00, 400.0, "ACTIVE", "uuid-privilegelogdocument-05");

CREATE TABLE IF NOT EXISTS legal_counsel_arbitrationproceedings (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_arbitrationproceedings_code ON legal_counsel_arbitrationproceedings(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_arbitrationproceedings_org_status ON legal_counsel_arbitrationproceedings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_arbitrationproceedings_priority ON legal_counsel_arbitrationproceedings(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_arbitrationproceedings_created_at ON legal_counsel_arbitrationproceedings(created_at);

-- Operational seed data fixtures for legal_counsel_arbitrationproceedings
INSERT OR IGNORE INTO legal_counsel_arbitrationproceedings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ARB-0001", "Primary Operational ArbitrationProceeding 1", 24500.00, 150.0, "ACTIVE", "uuid-arbitrationproceeding-01"),
    (2, "ARB-0002", "Secondary Corporate ArbitrationProceeding 2", 18200.50, 80.0, "ACTIVE", "uuid-arbitrationproceeding-02"),
    (3, "ARB-0003", "Consolidated Branch ArbitrationProceeding 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-arbitrationproceeding-03"),
    (4, "ARB-0004", "Enterprise Audited ArbitrationProceeding 4", 32800.00, 210.0, "ACTIVE", "uuid-arbitrationproceeding-04"),
    (5, "ARB-0005", "Executive Strategic ArbitrationProceeding 5", 65000.00, 400.0, "ACTIVE", "uuid-arbitrationproceeding-05");

CREATE TABLE IF NOT EXISTS legal_counsel_corporateresolutions (
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

CREATE INDEX IF NOT EXISTS idx_legal_counsel_corporateresolutions_code ON legal_counsel_corporateresolutions(code);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_corporateresolutions_org_status ON legal_counsel_corporateresolutions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_corporateresolutions_priority ON legal_counsel_corporateresolutions(priority);
CREATE INDEX IF NOT EXISTS idx_legal_counsel_corporateresolutions_created_at ON legal_counsel_corporateresolutions(created_at);

-- Operational seed data fixtures for legal_counsel_corporateresolutions
INSERT OR IGNORE INTO legal_counsel_corporateresolutions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COR-0001", "Primary Operational CorporateResolution 1", 24500.00, 150.0, "ACTIVE", "uuid-corporateresolution-01"),
    (2, "COR-0002", "Secondary Corporate CorporateResolution 2", 18200.50, 80.0, "ACTIVE", "uuid-corporateresolution-02"),
    (3, "COR-0003", "Consolidated Branch CorporateResolution 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-corporateresolution-03"),
    (4, "COR-0004", "Enterprise Audited CorporateResolution 4", 32800.00, 210.0, "ACTIVE", "uuid-corporateresolution-04"),
    (5, "COR-0005", "Executive Strategic CorporateResolution 5", 65000.00, 400.0, "ACTIVE", "uuid-corporateresolution-05");

