-- SmartERP Enterprise Titan Migration 007: Governance, Risk & Compliance (GRC) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS compliance_auditfindings (
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

CREATE INDEX IF NOT EXISTS idx_compliance_auditfindings_code ON compliance_auditfindings(code);
CREATE INDEX IF NOT EXISTS idx_compliance_auditfindings_org_status ON compliance_auditfindings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_auditfindings_priority ON compliance_auditfindings(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_auditfindings_created_at ON compliance_auditfindings(created_at);

-- Operational seed data fixtures for compliance_auditfindings
INSERT OR IGNORE INTO compliance_auditfindings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "AUD-0001", "Primary Operational AuditFinding 1", 24500.00, 150.0, "ACTIVE", "uuid-auditfinding-01"),
    (2, "AUD-0002", "Secondary Corporate AuditFinding 2", 18200.50, 80.0, "ACTIVE", "uuid-auditfinding-02"),
    (3, "AUD-0003", "Consolidated Branch AuditFinding 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-auditfinding-03"),
    (4, "AUD-0004", "Enterprise Audited AuditFinding 4", 32800.00, 210.0, "ACTIVE", "uuid-auditfinding-04"),
    (5, "AUD-0005", "Executive Strategic AuditFinding 5", 65000.00, 400.0, "ACTIVE", "uuid-auditfinding-05");

CREATE TABLE IF NOT EXISTS compliance_riskregisters (
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

CREATE INDEX IF NOT EXISTS idx_compliance_riskregisters_code ON compliance_riskregisters(code);
CREATE INDEX IF NOT EXISTS idx_compliance_riskregisters_org_status ON compliance_riskregisters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_riskregisters_priority ON compliance_riskregisters(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_riskregisters_created_at ON compliance_riskregisters(created_at);

-- Operational seed data fixtures for compliance_riskregisters
INSERT OR IGNORE INTO compliance_riskregisters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RIS-0001", "Primary Operational RiskRegister 1", 24500.00, 150.0, "ACTIVE", "uuid-riskregister-01"),
    (2, "RIS-0002", "Secondary Corporate RiskRegister 2", 18200.50, 80.0, "ACTIVE", "uuid-riskregister-02"),
    (3, "RIS-0003", "Consolidated Branch RiskRegister 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-riskregister-03"),
    (4, "RIS-0004", "Enterprise Audited RiskRegister 4", 32800.00, 210.0, "ACTIVE", "uuid-riskregister-04"),
    (5, "RIS-0005", "Executive Strategic RiskRegister 5", 65000.00, 400.0, "ACTIVE", "uuid-riskregister-05");

CREATE TABLE IF NOT EXISTS compliance_controlactivitys (
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

CREATE INDEX IF NOT EXISTS idx_compliance_controlactivitys_code ON compliance_controlactivitys(code);
CREATE INDEX IF NOT EXISTS idx_compliance_controlactivitys_org_status ON compliance_controlactivitys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_controlactivitys_priority ON compliance_controlactivitys(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_controlactivitys_created_at ON compliance_controlactivitys(created_at);

-- Operational seed data fixtures for compliance_controlactivitys
INSERT OR IGNORE INTO compliance_controlactivitys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ControlActivity 1", 24500.00, 150.0, "ACTIVE", "uuid-controlactivity-01"),
    (2, "CON-0002", "Secondary Corporate ControlActivity 2", 18200.50, 80.0, "ACTIVE", "uuid-controlactivity-02"),
    (3, "CON-0003", "Consolidated Branch ControlActivity 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-controlactivity-03"),
    (4, "CON-0004", "Enterprise Audited ControlActivity 4", 32800.00, 210.0, "ACTIVE", "uuid-controlactivity-04"),
    (5, "CON-0005", "Executive Strategic ControlActivity 5", 65000.00, 400.0, "ACTIVE", "uuid-controlactivity-05");

CREATE TABLE IF NOT EXISTS compliance_compliancepolicys (
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

CREATE INDEX IF NOT EXISTS idx_compliance_compliancepolicys_code ON compliance_compliancepolicys(code);
CREATE INDEX IF NOT EXISTS idx_compliance_compliancepolicys_org_status ON compliance_compliancepolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_compliancepolicys_priority ON compliance_compliancepolicys(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_compliancepolicys_created_at ON compliance_compliancepolicys(created_at);

-- Operational seed data fixtures for compliance_compliancepolicys
INSERT OR IGNORE INTO compliance_compliancepolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CompliancePolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-compliancepolicy-01"),
    (2, "COM-0002", "Secondary Corporate CompliancePolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-compliancepolicy-02"),
    (3, "COM-0003", "Consolidated Branch CompliancePolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-compliancepolicy-03"),
    (4, "COM-0004", "Enterprise Audited CompliancePolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-compliancepolicy-04"),
    (5, "COM-0005", "Executive Strategic CompliancePolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-compliancepolicy-05");

CREATE TABLE IF NOT EXISTS compliance_accessreviews (
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

CREATE INDEX IF NOT EXISTS idx_compliance_accessreviews_code ON compliance_accessreviews(code);
CREATE INDEX IF NOT EXISTS idx_compliance_accessreviews_org_status ON compliance_accessreviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_accessreviews_priority ON compliance_accessreviews(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_accessreviews_created_at ON compliance_accessreviews(created_at);

-- Operational seed data fixtures for compliance_accessreviews
INSERT OR IGNORE INTO compliance_accessreviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACC-0001", "Primary Operational AccessReview 1", 24500.00, 150.0, "ACTIVE", "uuid-accessreview-01"),
    (2, "ACC-0002", "Secondary Corporate AccessReview 2", 18200.50, 80.0, "ACTIVE", "uuid-accessreview-02"),
    (3, "ACC-0003", "Consolidated Branch AccessReview 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-accessreview-03"),
    (4, "ACC-0004", "Enterprise Audited AccessReview 4", 32800.00, 210.0, "ACTIVE", "uuid-accessreview-04"),
    (5, "ACC-0005", "Executive Strategic AccessReview 5", 65000.00, 400.0, "ACTIVE", "uuid-accessreview-05");

CREATE TABLE IF NOT EXISTS compliance_dataretentionschedules (
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

CREATE INDEX IF NOT EXISTS idx_compliance_dataretentionschedules_code ON compliance_dataretentionschedules(code);
CREATE INDEX IF NOT EXISTS idx_compliance_dataretentionschedules_org_status ON compliance_dataretentionschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_dataretentionschedules_priority ON compliance_dataretentionschedules(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_dataretentionschedules_created_at ON compliance_dataretentionschedules(created_at);

-- Operational seed data fixtures for compliance_dataretentionschedules
INSERT OR IGNORE INTO compliance_dataretentionschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataRetentionSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-dataretentionschedule-01"),
    (2, "DAT-0002", "Secondary Corporate DataRetentionSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-dataretentionschedule-02"),
    (3, "DAT-0003", "Consolidated Branch DataRetentionSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dataretentionschedule-03"),
    (4, "DAT-0004", "Enterprise Audited DataRetentionSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-dataretentionschedule-04"),
    (5, "DAT-0005", "Executive Strategic DataRetentionSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-dataretentionschedule-05");

CREATE TABLE IF NOT EXISTS compliance_gdprrequests (
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

CREATE INDEX IF NOT EXISTS idx_compliance_gdprrequests_code ON compliance_gdprrequests(code);
CREATE INDEX IF NOT EXISTS idx_compliance_gdprrequests_org_status ON compliance_gdprrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_gdprrequests_priority ON compliance_gdprrequests(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_gdprrequests_created_at ON compliance_gdprrequests(created_at);

-- Operational seed data fixtures for compliance_gdprrequests
INSERT OR IGNORE INTO compliance_gdprrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GDP-0001", "Primary Operational GDPRRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-gdprrequest-01"),
    (2, "GDP-0002", "Secondary Corporate GDPRRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-gdprrequest-02"),
    (3, "GDP-0003", "Consolidated Branch GDPRRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-gdprrequest-03"),
    (4, "GDP-0004", "Enterprise Audited GDPRRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-gdprrequest-04"),
    (5, "GDP-0005", "Executive Strategic GDPRRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-gdprrequest-05");

CREATE TABLE IF NOT EXISTS compliance_soxcontrols (
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

CREATE INDEX IF NOT EXISTS idx_compliance_soxcontrols_code ON compliance_soxcontrols(code);
CREATE INDEX IF NOT EXISTS idx_compliance_soxcontrols_org_status ON compliance_soxcontrols(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_soxcontrols_priority ON compliance_soxcontrols(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_soxcontrols_created_at ON compliance_soxcontrols(created_at);

-- Operational seed data fixtures for compliance_soxcontrols
INSERT OR IGNORE INTO compliance_soxcontrols (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SOX-0001", "Primary Operational SOXControl 1", 24500.00, 150.0, "ACTIVE", "uuid-soxcontrol-01"),
    (2, "SOX-0002", "Secondary Corporate SOXControl 2", 18200.50, 80.0, "ACTIVE", "uuid-soxcontrol-02"),
    (3, "SOX-0003", "Consolidated Branch SOXControl 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-soxcontrol-03"),
    (4, "SOX-0004", "Enterprise Audited SOXControl 4", 32800.00, 210.0, "ACTIVE", "uuid-soxcontrol-04"),
    (5, "SOX-0005", "Executive Strategic SOXControl 5", 65000.00, 400.0, "ACTIVE", "uuid-soxcontrol-05");

CREATE TABLE IF NOT EXISTS compliance_isorequirements (
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

CREATE INDEX IF NOT EXISTS idx_compliance_isorequirements_code ON compliance_isorequirements(code);
CREATE INDEX IF NOT EXISTS idx_compliance_isorequirements_org_status ON compliance_isorequirements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_isorequirements_priority ON compliance_isorequirements(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_isorequirements_created_at ON compliance_isorequirements(created_at);

-- Operational seed data fixtures for compliance_isorequirements
INSERT OR IGNORE INTO compliance_isorequirements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ISO-0001", "Primary Operational ISORequirement 1", 24500.00, 150.0, "ACTIVE", "uuid-isorequirement-01"),
    (2, "ISO-0002", "Secondary Corporate ISORequirement 2", 18200.50, 80.0, "ACTIVE", "uuid-isorequirement-02"),
    (3, "ISO-0003", "Consolidated Branch ISORequirement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-isorequirement-03"),
    (4, "ISO-0004", "Enterprise Audited ISORequirement 4", 32800.00, 210.0, "ACTIVE", "uuid-isorequirement-04"),
    (5, "ISO-0005", "Executive Strategic ISORequirement 5", 65000.00, 400.0, "ACTIVE", "uuid-isorequirement-05");

CREATE TABLE IF NOT EXISTS compliance_vendorassessments (
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

CREATE INDEX IF NOT EXISTS idx_compliance_vendorassessments_code ON compliance_vendorassessments(code);
CREATE INDEX IF NOT EXISTS idx_compliance_vendorassessments_org_status ON compliance_vendorassessments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_vendorassessments_priority ON compliance_vendorassessments(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_vendorassessments_created_at ON compliance_vendorassessments(created_at);

-- Operational seed data fixtures for compliance_vendorassessments
INSERT OR IGNORE INTO compliance_vendorassessments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorAssessment 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorassessment-01"),
    (2, "VEN-0002", "Secondary Corporate VendorAssessment 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorassessment-02"),
    (3, "VEN-0003", "Consolidated Branch VendorAssessment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorassessment-03"),
    (4, "VEN-0004", "Enterprise Audited VendorAssessment 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorassessment-04"),
    (5, "VEN-0005", "Executive Strategic VendorAssessment 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorassessment-05");

CREATE TABLE IF NOT EXISTS compliance_policyacknowledgements (
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

CREATE INDEX IF NOT EXISTS idx_compliance_policyacknowledgements_code ON compliance_policyacknowledgements(code);
CREATE INDEX IF NOT EXISTS idx_compliance_policyacknowledgements_org_status ON compliance_policyacknowledgements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_policyacknowledgements_priority ON compliance_policyacknowledgements(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_policyacknowledgements_created_at ON compliance_policyacknowledgements(created_at);

-- Operational seed data fixtures for compliance_policyacknowledgements
INSERT OR IGNORE INTO compliance_policyacknowledgements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "POL-0001", "Primary Operational PolicyAcknowledgement 1", 24500.00, 150.0, "ACTIVE", "uuid-policyacknowledgement-01"),
    (2, "POL-0002", "Secondary Corporate PolicyAcknowledgement 2", 18200.50, 80.0, "ACTIVE", "uuid-policyacknowledgement-02"),
    (3, "POL-0003", "Consolidated Branch PolicyAcknowledgement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-policyacknowledgement-03"),
    (4, "POL-0004", "Enterprise Audited PolicyAcknowledgement 4", 32800.00, 210.0, "ACTIVE", "uuid-policyacknowledgement-04"),
    (5, "POL-0005", "Executive Strategic PolicyAcknowledgement 5", 65000.00, 400.0, "ACTIVE", "uuid-policyacknowledgement-05");

CREATE TABLE IF NOT EXISTS compliance_whistleblowerreports (
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

CREATE INDEX IF NOT EXISTS idx_compliance_whistleblowerreports_code ON compliance_whistleblowerreports(code);
CREATE INDEX IF NOT EXISTS idx_compliance_whistleblowerreports_org_status ON compliance_whistleblowerreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_whistleblowerreports_priority ON compliance_whistleblowerreports(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_whistleblowerreports_created_at ON compliance_whistleblowerreports(created_at);

-- Operational seed data fixtures for compliance_whistleblowerreports
INSERT OR IGNORE INTO compliance_whistleblowerreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WHI-0001", "Primary Operational WhistleblowerReport 1", 24500.00, 150.0, "ACTIVE", "uuid-whistleblowerreport-01"),
    (2, "WHI-0002", "Secondary Corporate WhistleblowerReport 2", 18200.50, 80.0, "ACTIVE", "uuid-whistleblowerreport-02"),
    (3, "WHI-0003", "Consolidated Branch WhistleblowerReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-whistleblowerreport-03"),
    (4, "WHI-0004", "Enterprise Audited WhistleblowerReport 4", 32800.00, 210.0, "ACTIVE", "uuid-whistleblowerreport-04"),
    (5, "WHI-0005", "Executive Strategic WhistleblowerReport 5", 65000.00, 400.0, "ACTIVE", "uuid-whistleblowerreport-05");

CREATE TABLE IF NOT EXISTS compliance_securityincidents (
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

CREATE INDEX IF NOT EXISTS idx_compliance_securityincidents_code ON compliance_securityincidents(code);
CREATE INDEX IF NOT EXISTS idx_compliance_securityincidents_org_status ON compliance_securityincidents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_securityincidents_priority ON compliance_securityincidents(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_securityincidents_created_at ON compliance_securityincidents(created_at);

-- Operational seed data fixtures for compliance_securityincidents
INSERT OR IGNORE INTO compliance_securityincidents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEC-0001", "Primary Operational SecurityIncident 1", 24500.00, 150.0, "ACTIVE", "uuid-securityincident-01"),
    (2, "SEC-0002", "Secondary Corporate SecurityIncident 2", 18200.50, 80.0, "ACTIVE", "uuid-securityincident-02"),
    (3, "SEC-0003", "Consolidated Branch SecurityIncident 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-securityincident-03"),
    (4, "SEC-0004", "Enterprise Audited SecurityIncident 4", 32800.00, 210.0, "ACTIVE", "uuid-securityincident-04"),
    (5, "SEC-0005", "Executive Strategic SecurityIncident 5", 65000.00, 400.0, "ACTIVE", "uuid-securityincident-05");

CREATE TABLE IF NOT EXISTS compliance_correctiveactions (
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

CREATE INDEX IF NOT EXISTS idx_compliance_correctiveactions_code ON compliance_correctiveactions(code);
CREATE INDEX IF NOT EXISTS idx_compliance_correctiveactions_org_status ON compliance_correctiveactions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_correctiveactions_priority ON compliance_correctiveactions(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_correctiveactions_created_at ON compliance_correctiveactions(created_at);

-- Operational seed data fixtures for compliance_correctiveactions
INSERT OR IGNORE INTO compliance_correctiveactions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COR-0001", "Primary Operational CorrectiveAction 1", 24500.00, 150.0, "ACTIVE", "uuid-correctiveaction-01"),
    (2, "COR-0002", "Secondary Corporate CorrectiveAction 2", 18200.50, 80.0, "ACTIVE", "uuid-correctiveaction-02"),
    (3, "COR-0003", "Consolidated Branch CorrectiveAction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-correctiveaction-03"),
    (4, "COR-0004", "Enterprise Audited CorrectiveAction 4", 32800.00, 210.0, "ACTIVE", "uuid-correctiveaction-04"),
    (5, "COR-0005", "Executive Strategic CorrectiveAction 5", 65000.00, 400.0, "ACTIVE", "uuid-correctiveaction-05");

CREATE TABLE IF NOT EXISTS compliance_evidenceattachments (
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

CREATE INDEX IF NOT EXISTS idx_compliance_evidenceattachments_code ON compliance_evidenceattachments(code);
CREATE INDEX IF NOT EXISTS idx_compliance_evidenceattachments_org_status ON compliance_evidenceattachments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_evidenceattachments_priority ON compliance_evidenceattachments(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_evidenceattachments_created_at ON compliance_evidenceattachments(created_at);

-- Operational seed data fixtures for compliance_evidenceattachments
INSERT OR IGNORE INTO compliance_evidenceattachments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EVI-0001", "Primary Operational EvidenceAttachment 1", 24500.00, 150.0, "ACTIVE", "uuid-evidenceattachment-01"),
    (2, "EVI-0002", "Secondary Corporate EvidenceAttachment 2", 18200.50, 80.0, "ACTIVE", "uuid-evidenceattachment-02"),
    (3, "EVI-0003", "Consolidated Branch EvidenceAttachment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-evidenceattachment-03"),
    (4, "EVI-0004", "Enterprise Audited EvidenceAttachment 4", 32800.00, 210.0, "ACTIVE", "uuid-evidenceattachment-04"),
    (5, "EVI-0005", "Executive Strategic EvidenceAttachment 5", 65000.00, 400.0, "ACTIVE", "uuid-evidenceattachment-05");

CREATE TABLE IF NOT EXISTS compliance_regulatoryfilings (
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

CREATE INDEX IF NOT EXISTS idx_compliance_regulatoryfilings_code ON compliance_regulatoryfilings(code);
CREATE INDEX IF NOT EXISTS idx_compliance_regulatoryfilings_org_status ON compliance_regulatoryfilings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_compliance_regulatoryfilings_priority ON compliance_regulatoryfilings(priority);
CREATE INDEX IF NOT EXISTS idx_compliance_regulatoryfilings_created_at ON compliance_regulatoryfilings(created_at);

-- Operational seed data fixtures for compliance_regulatoryfilings
INSERT OR IGNORE INTO compliance_regulatoryfilings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REG-0001", "Primary Operational RegulatoryFiling 1", 24500.00, 150.0, "ACTIVE", "uuid-regulatoryfiling-01"),
    (2, "REG-0002", "Secondary Corporate RegulatoryFiling 2", 18200.50, 80.0, "ACTIVE", "uuid-regulatoryfiling-02"),
    (3, "REG-0003", "Consolidated Branch RegulatoryFiling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-regulatoryfiling-03"),
    (4, "REG-0004", "Enterprise Audited RegulatoryFiling 4", 32800.00, 210.0, "ACTIVE", "uuid-regulatoryfiling-04"),
    (5, "REG-0005", "Executive Strategic RegulatoryFiling 5", 65000.00, 400.0, "ACTIVE", "uuid-regulatoryfiling-05");

