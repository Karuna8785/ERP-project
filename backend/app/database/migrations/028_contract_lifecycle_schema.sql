-- SmartERP Enterprise Titan Migration 028: Enterprise Contract Lifecycle Management (CLM) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS contract_lifecycle_masterserviceagreements (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_masterserviceagreements_code ON contract_lifecycle_masterserviceagreements(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_masterserviceagreements_org_status ON contract_lifecycle_masterserviceagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_masterserviceagreements_priority ON contract_lifecycle_masterserviceagreements(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_masterserviceagreements_created_at ON contract_lifecycle_masterserviceagreements(created_at);

-- Operational seed data fixtures for contract_lifecycle_masterserviceagreements
INSERT OR IGNORE INTO contract_lifecycle_masterserviceagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAS-0001", "Primary Operational MasterServiceAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-masterserviceagreement-01"),
    (2, "MAS-0002", "Secondary Corporate MasterServiceAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-masterserviceagreement-02"),
    (3, "MAS-0003", "Consolidated Branch MasterServiceAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-masterserviceagreement-03"),
    (4, "MAS-0004", "Enterprise Audited MasterServiceAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-masterserviceagreement-04"),
    (5, "MAS-0005", "Executive Strategic MasterServiceAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-masterserviceagreement-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_nondisclosureagreements (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_nondisclosureagreements_code ON contract_lifecycle_nondisclosureagreements(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_nondisclosureagreements_org_status ON contract_lifecycle_nondisclosureagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_nondisclosureagreements_priority ON contract_lifecycle_nondisclosureagreements(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_nondisclosureagreements_created_at ON contract_lifecycle_nondisclosureagreements(created_at);

-- Operational seed data fixtures for contract_lifecycle_nondisclosureagreements
INSERT OR IGNORE INTO contract_lifecycle_nondisclosureagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "NON-0001", "Primary Operational NonDisclosureAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-nondisclosureagreement-01"),
    (2, "NON-0002", "Secondary Corporate NonDisclosureAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-nondisclosureagreement-02"),
    (3, "NON-0003", "Consolidated Branch NonDisclosureAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-nondisclosureagreement-03"),
    (4, "NON-0004", "Enterprise Audited NonDisclosureAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-nondisclosureagreement-04"),
    (5, "NON-0005", "Executive Strategic NonDisclosureAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-nondisclosureagreement-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_statementofworks (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_statementofworks_code ON contract_lifecycle_statementofworks(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_statementofworks_org_status ON contract_lifecycle_statementofworks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_statementofworks_priority ON contract_lifecycle_statementofworks(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_statementofworks_created_at ON contract_lifecycle_statementofworks(created_at);

-- Operational seed data fixtures for contract_lifecycle_statementofworks
INSERT OR IGNORE INTO contract_lifecycle_statementofworks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StatementOfWork 1", 24500.00, 150.0, "ACTIVE", "uuid-statementofwork-01"),
    (2, "STA-0002", "Secondary Corporate StatementOfWork 2", 18200.50, 80.0, "ACTIVE", "uuid-statementofwork-02"),
    (3, "STA-0003", "Consolidated Branch StatementOfWork 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-statementofwork-03"),
    (4, "STA-0004", "Enterprise Audited StatementOfWork 4", 32800.00, 210.0, "ACTIVE", "uuid-statementofwork-04"),
    (5, "STA-0005", "Executive Strategic StatementOfWork 5", 65000.00, 400.0, "ACTIVE", "uuid-statementofwork-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_contractamendments (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractamendments_code ON contract_lifecycle_contractamendments(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractamendments_org_status ON contract_lifecycle_contractamendments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractamendments_priority ON contract_lifecycle_contractamendments(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractamendments_created_at ON contract_lifecycle_contractamendments(created_at);

-- Operational seed data fixtures for contract_lifecycle_contractamendments
INSERT OR IGNORE INTO contract_lifecycle_contractamendments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContractAmendment 1", 24500.00, 150.0, "ACTIVE", "uuid-contractamendment-01"),
    (2, "CON-0002", "Secondary Corporate ContractAmendment 2", 18200.50, 80.0, "ACTIVE", "uuid-contractamendment-02"),
    (3, "CON-0003", "Consolidated Branch ContractAmendment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-contractamendment-03"),
    (4, "CON-0004", "Enterprise Audited ContractAmendment 4", 32800.00, 210.0, "ACTIVE", "uuid-contractamendment-04"),
    (5, "CON-0005", "Executive Strategic ContractAmendment 5", 65000.00, 400.0, "ACTIVE", "uuid-contractamendment-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_clauselibraryitems (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_clauselibraryitems_code ON contract_lifecycle_clauselibraryitems(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_clauselibraryitems_org_status ON contract_lifecycle_clauselibraryitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_clauselibraryitems_priority ON contract_lifecycle_clauselibraryitems(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_clauselibraryitems_created_at ON contract_lifecycle_clauselibraryitems(created_at);

-- Operational seed data fixtures for contract_lifecycle_clauselibraryitems
INSERT OR IGNORE INTO contract_lifecycle_clauselibraryitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CLA-0001", "Primary Operational ClauseLibraryItem 1", 24500.00, 150.0, "ACTIVE", "uuid-clauselibraryitem-01"),
    (2, "CLA-0002", "Secondary Corporate ClauseLibraryItem 2", 18200.50, 80.0, "ACTIVE", "uuid-clauselibraryitem-02"),
    (3, "CLA-0003", "Consolidated Branch ClauseLibraryItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-clauselibraryitem-03"),
    (4, "CLA-0004", "Enterprise Audited ClauseLibraryItem 4", 32800.00, 210.0, "ACTIVE", "uuid-clauselibraryitem-04"),
    (5, "CLA-0005", "Executive Strategic ClauseLibraryItem 5", 65000.00, 400.0, "ACTIVE", "uuid-clauselibraryitem-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_contractobligations (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractobligations_code ON contract_lifecycle_contractobligations(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractobligations_org_status ON contract_lifecycle_contractobligations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractobligations_priority ON contract_lifecycle_contractobligations(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractobligations_created_at ON contract_lifecycle_contractobligations(created_at);

-- Operational seed data fixtures for contract_lifecycle_contractobligations
INSERT OR IGNORE INTO contract_lifecycle_contractobligations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContractObligation 1", 24500.00, 150.0, "ACTIVE", "uuid-contractobligation-01"),
    (2, "CON-0002", "Secondary Corporate ContractObligation 2", 18200.50, 80.0, "ACTIVE", "uuid-contractobligation-02"),
    (3, "CON-0003", "Consolidated Branch ContractObligation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-contractobligation-03"),
    (4, "CON-0004", "Enterprise Audited ContractObligation 4", 32800.00, 210.0, "ACTIVE", "uuid-contractobligation-04"),
    (5, "CON-0005", "Executive Strategic ContractObligation 5", 65000.00, 400.0, "ACTIVE", "uuid-contractobligation-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_milestonepaymentterms (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_milestonepaymentterms_code ON contract_lifecycle_milestonepaymentterms(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_milestonepaymentterms_org_status ON contract_lifecycle_milestonepaymentterms(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_milestonepaymentterms_priority ON contract_lifecycle_milestonepaymentterms(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_milestonepaymentterms_created_at ON contract_lifecycle_milestonepaymentterms(created_at);

-- Operational seed data fixtures for contract_lifecycle_milestonepaymentterms
INSERT OR IGNORE INTO contract_lifecycle_milestonepaymentterms (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MIL-0001", "Primary Operational MilestonePaymentTerm 1", 24500.00, 150.0, "ACTIVE", "uuid-milestonepaymentterm-01"),
    (2, "MIL-0002", "Secondary Corporate MilestonePaymentTerm 2", 18200.50, 80.0, "ACTIVE", "uuid-milestonepaymentterm-02"),
    (3, "MIL-0003", "Consolidated Branch MilestonePaymentTerm 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-milestonepaymentterm-03"),
    (4, "MIL-0004", "Enterprise Audited MilestonePaymentTerm 4", 32800.00, 210.0, "ACTIVE", "uuid-milestonepaymentterm-04"),
    (5, "MIL-0005", "Executive Strategic MilestonePaymentTerm 5", 65000.00, 400.0, "ACTIVE", "uuid-milestonepaymentterm-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_renewalnoticeevents (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_renewalnoticeevents_code ON contract_lifecycle_renewalnoticeevents(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_renewalnoticeevents_org_status ON contract_lifecycle_renewalnoticeevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_renewalnoticeevents_priority ON contract_lifecycle_renewalnoticeevents(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_renewalnoticeevents_created_at ON contract_lifecycle_renewalnoticeevents(created_at);

-- Operational seed data fixtures for contract_lifecycle_renewalnoticeevents
INSERT OR IGNORE INTO contract_lifecycle_renewalnoticeevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REN-0001", "Primary Operational RenewalNoticeEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-renewalnoticeevent-01"),
    (2, "REN-0002", "Secondary Corporate RenewalNoticeEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-renewalnoticeevent-02"),
    (3, "REN-0003", "Consolidated Branch RenewalNoticeEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-renewalnoticeevent-03"),
    (4, "REN-0004", "Enterprise Audited RenewalNoticeEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-renewalnoticeevent-04"),
    (5, "REN-0005", "Executive Strategic RenewalNoticeEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-renewalnoticeevent-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_contractriskassessments (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractriskassessments_code ON contract_lifecycle_contractriskassessments(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractriskassessments_org_status ON contract_lifecycle_contractriskassessments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractriskassessments_priority ON contract_lifecycle_contractriskassessments(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractriskassessments_created_at ON contract_lifecycle_contractriskassessments(created_at);

-- Operational seed data fixtures for contract_lifecycle_contractriskassessments
INSERT OR IGNORE INTO contract_lifecycle_contractriskassessments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContractRiskAssessment 1", 24500.00, 150.0, "ACTIVE", "uuid-contractriskassessment-01"),
    (2, "CON-0002", "Secondary Corporate ContractRiskAssessment 2", 18200.50, 80.0, "ACTIVE", "uuid-contractriskassessment-02"),
    (3, "CON-0003", "Consolidated Branch ContractRiskAssessment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-contractriskassessment-03"),
    (4, "CON-0004", "Enterprise Audited ContractRiskAssessment 4", 32800.00, 210.0, "ACTIVE", "uuid-contractriskassessment-04"),
    (5, "CON-0005", "Executive Strategic ContractRiskAssessment 5", 65000.00, 400.0, "ACTIVE", "uuid-contractriskassessment-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_legalredlineversions (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_legalredlineversions_code ON contract_lifecycle_legalredlineversions(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_legalredlineversions_org_status ON contract_lifecycle_legalredlineversions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_legalredlineversions_priority ON contract_lifecycle_legalredlineversions(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_legalredlineversions_created_at ON contract_lifecycle_legalredlineversions(created_at);

-- Operational seed data fixtures for contract_lifecycle_legalredlineversions
INSERT OR IGNORE INTO contract_lifecycle_legalredlineversions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEG-0001", "Primary Operational LegalRedlineVersion 1", 24500.00, 150.0, "ACTIVE", "uuid-legalredlineversion-01"),
    (2, "LEG-0002", "Secondary Corporate LegalRedlineVersion 2", 18200.50, 80.0, "ACTIVE", "uuid-legalredlineversion-02"),
    (3, "LEG-0003", "Consolidated Branch LegalRedlineVersion 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-legalredlineversion-03"),
    (4, "LEG-0004", "Enterprise Audited LegalRedlineVersion 4", 32800.00, 210.0, "ACTIVE", "uuid-legalredlineversion-04"),
    (5, "LEG-0005", "Executive Strategic LegalRedlineVersion 5", 65000.00, 400.0, "ACTIVE", "uuid-legalredlineversion-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_signatoryapprovalmatrixs (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_signatoryapprovalmatrixs_code ON contract_lifecycle_signatoryapprovalmatrixs(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_signatoryapprovalmatrixs_org_status ON contract_lifecycle_signatoryapprovalmatrixs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_signatoryapprovalmatrixs_priority ON contract_lifecycle_signatoryapprovalmatrixs(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_signatoryapprovalmatrixs_created_at ON contract_lifecycle_signatoryapprovalmatrixs(created_at);

-- Operational seed data fixtures for contract_lifecycle_signatoryapprovalmatrixs
INSERT OR IGNORE INTO contract_lifecycle_signatoryapprovalmatrixs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SIG-0001", "Primary Operational SignatoryApprovalMatrix 1", 24500.00, 150.0, "ACTIVE", "uuid-signatoryapprovalmatrix-01"),
    (2, "SIG-0002", "Secondary Corporate SignatoryApprovalMatrix 2", 18200.50, 80.0, "ACTIVE", "uuid-signatoryapprovalmatrix-02"),
    (3, "SIG-0003", "Consolidated Branch SignatoryApprovalMatrix 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-signatoryapprovalmatrix-03"),
    (4, "SIG-0004", "Enterprise Audited SignatoryApprovalMatrix 4", 32800.00, 210.0, "ACTIVE", "uuid-signatoryapprovalmatrix-04"),
    (5, "SIG-0005", "Executive Strategic SignatoryApprovalMatrix 5", 65000.00, 400.0, "ACTIVE", "uuid-signatoryapprovalmatrix-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_terminationnotices (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_terminationnotices_code ON contract_lifecycle_terminationnotices(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_terminationnotices_org_status ON contract_lifecycle_terminationnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_terminationnotices_priority ON contract_lifecycle_terminationnotices(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_terminationnotices_created_at ON contract_lifecycle_terminationnotices(created_at);

-- Operational seed data fixtures for contract_lifecycle_terminationnotices
INSERT OR IGNORE INTO contract_lifecycle_terminationnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TER-0001", "Primary Operational TerminationNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-terminationnotice-01"),
    (2, "TER-0002", "Secondary Corporate TerminationNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-terminationnotice-02"),
    (3, "TER-0003", "Consolidated Branch TerminationNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-terminationnotice-03"),
    (4, "TER-0004", "Enterprise Audited TerminationNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-terminationnotice-04"),
    (5, "TER-0005", "Executive Strategic TerminationNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-terminationnotice-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_slacompliancechecks (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_slacompliancechecks_code ON contract_lifecycle_slacompliancechecks(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_slacompliancechecks_org_status ON contract_lifecycle_slacompliancechecks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_slacompliancechecks_priority ON contract_lifecycle_slacompliancechecks(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_slacompliancechecks_created_at ON contract_lifecycle_slacompliancechecks(created_at);

-- Operational seed data fixtures for contract_lifecycle_slacompliancechecks
INSERT OR IGNORE INTO contract_lifecycle_slacompliancechecks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SLA-0001", "Primary Operational SLAComplianceCheck 1", 24500.00, 150.0, "ACTIVE", "uuid-slacompliancecheck-01"),
    (2, "SLA-0002", "Secondary Corporate SLAComplianceCheck 2", 18200.50, 80.0, "ACTIVE", "uuid-slacompliancecheck-02"),
    (3, "SLA-0003", "Consolidated Branch SLAComplianceCheck 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-slacompliancecheck-03"),
    (4, "SLA-0004", "Enterprise Audited SLAComplianceCheck 4", 32800.00, 210.0, "ACTIVE", "uuid-slacompliancecheck-04"),
    (5, "SLA-0005", "Executive Strategic SLAComplianceCheck 5", 65000.00, 400.0, "ACTIVE", "uuid-slacompliancecheck-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_contractrepositoryindexs (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractrepositoryindexs_code ON contract_lifecycle_contractrepositoryindexs(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractrepositoryindexs_org_status ON contract_lifecycle_contractrepositoryindexs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractrepositoryindexs_priority ON contract_lifecycle_contractrepositoryindexs(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_contractrepositoryindexs_created_at ON contract_lifecycle_contractrepositoryindexs(created_at);

-- Operational seed data fixtures for contract_lifecycle_contractrepositoryindexs
INSERT OR IGNORE INTO contract_lifecycle_contractrepositoryindexs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContractRepositoryIndex 1", 24500.00, 150.0, "ACTIVE", "uuid-contractrepositoryindex-01"),
    (2, "CON-0002", "Secondary Corporate ContractRepositoryIndex 2", 18200.50, 80.0, "ACTIVE", "uuid-contractrepositoryindex-02"),
    (3, "CON-0003", "Consolidated Branch ContractRepositoryIndex 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-contractrepositoryindex-03"),
    (4, "CON-0004", "Enterprise Audited ContractRepositoryIndex 4", 32800.00, 210.0, "ACTIVE", "uuid-contractrepositoryindex-04"),
    (5, "CON-0005", "Executive Strategic ContractRepositoryIndex 5", 65000.00, 400.0, "ACTIVE", "uuid-contractrepositoryindex-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_vendorcontractlinks (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_vendorcontractlinks_code ON contract_lifecycle_vendorcontractlinks(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_vendorcontractlinks_org_status ON contract_lifecycle_vendorcontractlinks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_vendorcontractlinks_priority ON contract_lifecycle_vendorcontractlinks(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_vendorcontractlinks_created_at ON contract_lifecycle_vendorcontractlinks(created_at);

-- Operational seed data fixtures for contract_lifecycle_vendorcontractlinks
INSERT OR IGNORE INTO contract_lifecycle_vendorcontractlinks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorContractLink 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorcontractlink-01"),
    (2, "VEN-0002", "Secondary Corporate VendorContractLink 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorcontractlink-02"),
    (3, "VEN-0003", "Consolidated Branch VendorContractLink 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorcontractlink-03"),
    (4, "VEN-0004", "Enterprise Audited VendorContractLink 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorcontractlink-04"),
    (5, "VEN-0005", "Executive Strategic VendorContractLink 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorcontractlink-05");

CREATE TABLE IF NOT EXISTS contract_lifecycle_customercontractlinks (
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

CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_customercontractlinks_code ON contract_lifecycle_customercontractlinks(code);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_customercontractlinks_org_status ON contract_lifecycle_customercontractlinks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_customercontractlinks_priority ON contract_lifecycle_customercontractlinks(priority);
CREATE INDEX IF NOT EXISTS idx_contract_lifecycle_customercontractlinks_created_at ON contract_lifecycle_customercontractlinks(created_at);

-- Operational seed data fixtures for contract_lifecycle_customercontractlinks
INSERT OR IGNORE INTO contract_lifecycle_customercontractlinks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerContractLink 1", 24500.00, 150.0, "ACTIVE", "uuid-customercontractlink-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerContractLink 2", 18200.50, 80.0, "ACTIVE", "uuid-customercontractlink-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerContractLink 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customercontractlink-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerContractLink 4", 32800.00, 210.0, "ACTIVE", "uuid-customercontractlink-04"),
    (5, "CUS-0005", "Executive Strategic CustomerContractLink 5", 65000.00, 400.0, "ACTIVE", "uuid-customercontractlink-05");

