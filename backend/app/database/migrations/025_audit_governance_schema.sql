-- SmartERP Enterprise Titan Migration 025: Enterprise Audit Governance & SoD DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS audit_governance_segregationofdutiesrules (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_segregationofdutiesrules_code ON audit_governance_segregationofdutiesrules(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_segregationofdutiesrules_org_status ON audit_governance_segregationofdutiesrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_segregationofdutiesrules_priority ON audit_governance_segregationofdutiesrules(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_segregationofdutiesrules_created_at ON audit_governance_segregationofdutiesrules(created_at);

-- Operational seed data fixtures for audit_governance_segregationofdutiesrules
INSERT OR IGNORE INTO audit_governance_segregationofdutiesrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEG-0001", "Primary Operational SegregationOfDutiesRule 1", 24500.00, 150.0, "ACTIVE", "uuid-segregationofdutiesrule-01"),
    (2, "SEG-0002", "Secondary Corporate SegregationOfDutiesRule 2", 18200.50, 80.0, "ACTIVE", "uuid-segregationofdutiesrule-02"),
    (3, "SEG-0003", "Consolidated Branch SegregationOfDutiesRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-segregationofdutiesrule-03"),
    (4, "SEG-0004", "Enterprise Audited SegregationOfDutiesRule 4", 32800.00, 210.0, "ACTIVE", "uuid-segregationofdutiesrule-04"),
    (5, "SEG-0005", "Executive Strategic SegregationOfDutiesRule 5", 65000.00, 400.0, "ACTIVE", "uuid-segregationofdutiesrule-05");

CREATE TABLE IF NOT EXISTS audit_governance_sodviolationdetections (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_sodviolationdetections_code ON audit_governance_sodviolationdetections(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_sodviolationdetections_org_status ON audit_governance_sodviolationdetections(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_sodviolationdetections_priority ON audit_governance_sodviolationdetections(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_sodviolationdetections_created_at ON audit_governance_sodviolationdetections(created_at);

-- Operational seed data fixtures for audit_governance_sodviolationdetections
INSERT OR IGNORE INTO audit_governance_sodviolationdetections (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SOD-0001", "Primary Operational SoDViolationDetection 1", 24500.00, 150.0, "ACTIVE", "uuid-sodviolationdetection-01"),
    (2, "SOD-0002", "Secondary Corporate SoDViolationDetection 2", 18200.50, 80.0, "ACTIVE", "uuid-sodviolationdetection-02"),
    (3, "SOD-0003", "Consolidated Branch SoDViolationDetection 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sodviolationdetection-03"),
    (4, "SOD-0004", "Enterprise Audited SoDViolationDetection 4", 32800.00, 210.0, "ACTIVE", "uuid-sodviolationdetection-04"),
    (5, "SOD-0005", "Executive Strategic SoDViolationDetection 5", 65000.00, 400.0, "ACTIVE", "uuid-sodviolationdetection-05");

CREATE TABLE IF NOT EXISTS audit_governance_userrolematrixs (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_userrolematrixs_code ON audit_governance_userrolematrixs(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_userrolematrixs_org_status ON audit_governance_userrolematrixs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_userrolematrixs_priority ON audit_governance_userrolematrixs(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_userrolematrixs_created_at ON audit_governance_userrolematrixs(created_at);

-- Operational seed data fixtures for audit_governance_userrolematrixs
INSERT OR IGNORE INTO audit_governance_userrolematrixs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USE-0001", "Primary Operational UserRoleMatrix 1", 24500.00, 150.0, "ACTIVE", "uuid-userrolematrix-01"),
    (2, "USE-0002", "Secondary Corporate UserRoleMatrix 2", 18200.50, 80.0, "ACTIVE", "uuid-userrolematrix-02"),
    (3, "USE-0003", "Consolidated Branch UserRoleMatrix 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-userrolematrix-03"),
    (4, "USE-0004", "Enterprise Audited UserRoleMatrix 4", 32800.00, 210.0, "ACTIVE", "uuid-userrolematrix-04"),
    (5, "USE-0005", "Executive Strategic UserRoleMatrix 5", 65000.00, 400.0, "ACTIVE", "uuid-userrolematrix-05");

CREATE TABLE IF NOT EXISTS audit_governance_permissionentitlements (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_permissionentitlements_code ON audit_governance_permissionentitlements(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_permissionentitlements_org_status ON audit_governance_permissionentitlements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_permissionentitlements_priority ON audit_governance_permissionentitlements(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_permissionentitlements_created_at ON audit_governance_permissionentitlements(created_at);

-- Operational seed data fixtures for audit_governance_permissionentitlements
INSERT OR IGNORE INTO audit_governance_permissionentitlements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PER-0001", "Primary Operational PermissionEntitlement 1", 24500.00, 150.0, "ACTIVE", "uuid-permissionentitlement-01"),
    (2, "PER-0002", "Secondary Corporate PermissionEntitlement 2", 18200.50, 80.0, "ACTIVE", "uuid-permissionentitlement-02"),
    (3, "PER-0003", "Consolidated Branch PermissionEntitlement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-permissionentitlement-03"),
    (4, "PER-0004", "Enterprise Audited PermissionEntitlement 4", 32800.00, 210.0, "ACTIVE", "uuid-permissionentitlement-04"),
    (5, "PER-0005", "Executive Strategic PermissionEntitlement 5", 65000.00, 400.0, "ACTIVE", "uuid-permissionentitlement-05");

CREATE TABLE IF NOT EXISTS audit_governance_periodicaccessreviewcampaigns (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_periodicaccessreviewcampaigns_code ON audit_governance_periodicaccessreviewcampaigns(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_periodicaccessreviewcampaigns_org_status ON audit_governance_periodicaccessreviewcampaigns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_periodicaccessreviewcampaigns_priority ON audit_governance_periodicaccessreviewcampaigns(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_periodicaccessreviewcampaigns_created_at ON audit_governance_periodicaccessreviewcampaigns(created_at);

-- Operational seed data fixtures for audit_governance_periodicaccessreviewcampaigns
INSERT OR IGNORE INTO audit_governance_periodicaccessreviewcampaigns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PER-0001", "Primary Operational PeriodicAccessReviewCampaign 1", 24500.00, 150.0, "ACTIVE", "uuid-periodicaccessreviewcampaign-01"),
    (2, "PER-0002", "Secondary Corporate PeriodicAccessReviewCampaign 2", 18200.50, 80.0, "ACTIVE", "uuid-periodicaccessreviewcampaign-02"),
    (3, "PER-0003", "Consolidated Branch PeriodicAccessReviewCampaign 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-periodicaccessreviewcampaign-03"),
    (4, "PER-0004", "Enterprise Audited PeriodicAccessReviewCampaign 4", 32800.00, 210.0, "ACTIVE", "uuid-periodicaccessreviewcampaign-04"),
    (5, "PER-0005", "Executive Strategic PeriodicAccessReviewCampaign 5", 65000.00, 400.0, "ACTIVE", "uuid-periodicaccessreviewcampaign-05");

CREATE TABLE IF NOT EXISTS audit_governance_privilegedaccessrequests (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_privilegedaccessrequests_code ON audit_governance_privilegedaccessrequests(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_privilegedaccessrequests_org_status ON audit_governance_privilegedaccessrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_privilegedaccessrequests_priority ON audit_governance_privilegedaccessrequests(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_privilegedaccessrequests_created_at ON audit_governance_privilegedaccessrequests(created_at);

-- Operational seed data fixtures for audit_governance_privilegedaccessrequests
INSERT OR IGNORE INTO audit_governance_privilegedaccessrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PrivilegedAccessRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-privilegedaccessrequest-01"),
    (2, "PRI-0002", "Secondary Corporate PrivilegedAccessRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-privilegedaccessrequest-02"),
    (3, "PRI-0003", "Consolidated Branch PrivilegedAccessRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-privilegedaccessrequest-03"),
    (4, "PRI-0004", "Enterprise Audited PrivilegedAccessRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-privilegedaccessrequest-04"),
    (5, "PRI-0005", "Executive Strategic PrivilegedAccessRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-privilegedaccessrequest-05");

CREATE TABLE IF NOT EXISTS audit_governance_emergencyfirefighteraccesss (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_emergencyfirefighteraccesss_code ON audit_governance_emergencyfirefighteraccesss(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_emergencyfirefighteraccesss_org_status ON audit_governance_emergencyfirefighteraccesss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_emergencyfirefighteraccesss_priority ON audit_governance_emergencyfirefighteraccesss(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_emergencyfirefighteraccesss_created_at ON audit_governance_emergencyfirefighteraccesss(created_at);

-- Operational seed data fixtures for audit_governance_emergencyfirefighteraccesss
INSERT OR IGNORE INTO audit_governance_emergencyfirefighteraccesss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EME-0001", "Primary Operational EmergencyFirefighterAccess 1", 24500.00, 150.0, "ACTIVE", "uuid-emergencyfirefighteraccess-01"),
    (2, "EME-0002", "Secondary Corporate EmergencyFirefighterAccess 2", 18200.50, 80.0, "ACTIVE", "uuid-emergencyfirefighteraccess-02"),
    (3, "EME-0003", "Consolidated Branch EmergencyFirefighterAccess 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-emergencyfirefighteraccess-03"),
    (4, "EME-0004", "Enterprise Audited EmergencyFirefighterAccess 4", 32800.00, 210.0, "ACTIVE", "uuid-emergencyfirefighteraccess-04"),
    (5, "EME-0005", "Executive Strategic EmergencyFirefighterAccess 5", 65000.00, 400.0, "ACTIVE", "uuid-emergencyfirefighteraccess-05");

CREATE TABLE IF NOT EXISTS audit_governance_immutablesystemauditlogs (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_immutablesystemauditlogs_code ON audit_governance_immutablesystemauditlogs(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_immutablesystemauditlogs_org_status ON audit_governance_immutablesystemauditlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_immutablesystemauditlogs_priority ON audit_governance_immutablesystemauditlogs(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_immutablesystemauditlogs_created_at ON audit_governance_immutablesystemauditlogs(created_at);

-- Operational seed data fixtures for audit_governance_immutablesystemauditlogs
INSERT OR IGNORE INTO audit_governance_immutablesystemauditlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "IMM-0001", "Primary Operational ImmutableSystemAuditLog 1", 24500.00, 150.0, "ACTIVE", "uuid-immutablesystemauditlog-01"),
    (2, "IMM-0002", "Secondary Corporate ImmutableSystemAuditLog 2", 18200.50, 80.0, "ACTIVE", "uuid-immutablesystemauditlog-02"),
    (3, "IMM-0003", "Consolidated Branch ImmutableSystemAuditLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-immutablesystemauditlog-03"),
    (4, "IMM-0004", "Enterprise Audited ImmutableSystemAuditLog 4", 32800.00, 210.0, "ACTIVE", "uuid-immutablesystemauditlog-04"),
    (5, "IMM-0005", "Executive Strategic ImmutableSystemAuditLog 5", 65000.00, 400.0, "ACTIVE", "uuid-immutablesystemauditlog-05");

CREATE TABLE IF NOT EXISTS audit_governance_datachangecaptureevents (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_datachangecaptureevents_code ON audit_governance_datachangecaptureevents(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_datachangecaptureevents_org_status ON audit_governance_datachangecaptureevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_datachangecaptureevents_priority ON audit_governance_datachangecaptureevents(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_datachangecaptureevents_created_at ON audit_governance_datachangecaptureevents(created_at);

-- Operational seed data fixtures for audit_governance_datachangecaptureevents
INSERT OR IGNORE INTO audit_governance_datachangecaptureevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataChangeCaptureEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-datachangecaptureevent-01"),
    (2, "DAT-0002", "Secondary Corporate DataChangeCaptureEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-datachangecaptureevent-02"),
    (3, "DAT-0003", "Consolidated Branch DataChangeCaptureEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-datachangecaptureevent-03"),
    (4, "DAT-0004", "Enterprise Audited DataChangeCaptureEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-datachangecaptureevent-04"),
    (5, "DAT-0005", "Executive Strategic DataChangeCaptureEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-datachangecaptureevent-05");

CREATE TABLE IF NOT EXISTS audit_governance_securitypolicydefinitions (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_securitypolicydefinitions_code ON audit_governance_securitypolicydefinitions(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_securitypolicydefinitions_org_status ON audit_governance_securitypolicydefinitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_securitypolicydefinitions_priority ON audit_governance_securitypolicydefinitions(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_securitypolicydefinitions_created_at ON audit_governance_securitypolicydefinitions(created_at);

-- Operational seed data fixtures for audit_governance_securitypolicydefinitions
INSERT OR IGNORE INTO audit_governance_securitypolicydefinitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEC-0001", "Primary Operational SecurityPolicyDefinition 1", 24500.00, 150.0, "ACTIVE", "uuid-securitypolicydefinition-01"),
    (2, "SEC-0002", "Secondary Corporate SecurityPolicyDefinition 2", 18200.50, 80.0, "ACTIVE", "uuid-securitypolicydefinition-02"),
    (3, "SEC-0003", "Consolidated Branch SecurityPolicyDefinition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-securitypolicydefinition-03"),
    (4, "SEC-0004", "Enterprise Audited SecurityPolicyDefinition 4", 32800.00, 210.0, "ACTIVE", "uuid-securitypolicydefinition-04"),
    (5, "SEC-0005", "Executive Strategic SecurityPolicyDefinition 5", 65000.00, 400.0, "ACTIVE", "uuid-securitypolicydefinition-05");

CREATE TABLE IF NOT EXISTS audit_governance_sessionauthenticationlogs (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_sessionauthenticationlogs_code ON audit_governance_sessionauthenticationlogs(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_sessionauthenticationlogs_org_status ON audit_governance_sessionauthenticationlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_sessionauthenticationlogs_priority ON audit_governance_sessionauthenticationlogs(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_sessionauthenticationlogs_created_at ON audit_governance_sessionauthenticationlogs(created_at);

-- Operational seed data fixtures for audit_governance_sessionauthenticationlogs
INSERT OR IGNORE INTO audit_governance_sessionauthenticationlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SES-0001", "Primary Operational SessionAuthenticationLog 1", 24500.00, 150.0, "ACTIVE", "uuid-sessionauthenticationlog-01"),
    (2, "SES-0002", "Secondary Corporate SessionAuthenticationLog 2", 18200.50, 80.0, "ACTIVE", "uuid-sessionauthenticationlog-02"),
    (3, "SES-0003", "Consolidated Branch SessionAuthenticationLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sessionauthenticationlog-03"),
    (4, "SES-0004", "Enterprise Audited SessionAuthenticationLog 4", 32800.00, 210.0, "ACTIVE", "uuid-sessionauthenticationlog-04"),
    (5, "SES-0005", "Executive Strategic SessionAuthenticationLog 5", 65000.00, 400.0, "ACTIVE", "uuid-sessionauthenticationlog-05");

CREATE TABLE IF NOT EXISTS audit_governance_databasequeryauditlogs (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_databasequeryauditlogs_code ON audit_governance_databasequeryauditlogs(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_databasequeryauditlogs_org_status ON audit_governance_databasequeryauditlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_databasequeryauditlogs_priority ON audit_governance_databasequeryauditlogs(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_databasequeryauditlogs_created_at ON audit_governance_databasequeryauditlogs(created_at);

-- Operational seed data fixtures for audit_governance_databasequeryauditlogs
INSERT OR IGNORE INTO audit_governance_databasequeryauditlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DatabaseQueryAuditLog 1", 24500.00, 150.0, "ACTIVE", "uuid-databasequeryauditlog-01"),
    (2, "DAT-0002", "Secondary Corporate DatabaseQueryAuditLog 2", 18200.50, 80.0, "ACTIVE", "uuid-databasequeryauditlog-02"),
    (3, "DAT-0003", "Consolidated Branch DatabaseQueryAuditLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-databasequeryauditlog-03"),
    (4, "DAT-0004", "Enterprise Audited DatabaseQueryAuditLog 4", 32800.00, 210.0, "ACTIVE", "uuid-databasequeryauditlog-04"),
    (5, "DAT-0005", "Executive Strategic DatabaseQueryAuditLog 5", 65000.00, 400.0, "ACTIVE", "uuid-databasequeryauditlog-05");

CREATE TABLE IF NOT EXISTS audit_governance_exportactivitylogs (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_exportactivitylogs_code ON audit_governance_exportactivitylogs(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_exportactivitylogs_org_status ON audit_governance_exportactivitylogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_exportactivitylogs_priority ON audit_governance_exportactivitylogs(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_exportactivitylogs_created_at ON audit_governance_exportactivitylogs(created_at);

-- Operational seed data fixtures for audit_governance_exportactivitylogs
INSERT OR IGNORE INTO audit_governance_exportactivitylogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExportActivityLog 1", 24500.00, 150.0, "ACTIVE", "uuid-exportactivitylog-01"),
    (2, "EXP-0002", "Secondary Corporate ExportActivityLog 2", 18200.50, 80.0, "ACTIVE", "uuid-exportactivitylog-02"),
    (3, "EXP-0003", "Consolidated Branch ExportActivityLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-exportactivitylog-03"),
    (4, "EXP-0004", "Enterprise Audited ExportActivityLog 4", 32800.00, 210.0, "ACTIVE", "uuid-exportactivitylog-04"),
    (5, "EXP-0005", "Executive Strategic ExportActivityLog 5", 65000.00, 400.0, "ACTIVE", "uuid-exportactivitylog-05");

CREATE TABLE IF NOT EXISTS audit_governance_adminactionlogs (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_adminactionlogs_code ON audit_governance_adminactionlogs(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_adminactionlogs_org_status ON audit_governance_adminactionlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_adminactionlogs_priority ON audit_governance_adminactionlogs(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_adminactionlogs_created_at ON audit_governance_adminactionlogs(created_at);

-- Operational seed data fixtures for audit_governance_adminactionlogs
INSERT OR IGNORE INTO audit_governance_adminactionlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ADM-0001", "Primary Operational AdminActionLog 1", 24500.00, 150.0, "ACTIVE", "uuid-adminactionlog-01"),
    (2, "ADM-0002", "Secondary Corporate AdminActionLog 2", 18200.50, 80.0, "ACTIVE", "uuid-adminactionlog-02"),
    (3, "ADM-0003", "Consolidated Branch AdminActionLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-adminactionlog-03"),
    (4, "ADM-0004", "Enterprise Audited AdminActionLog 4", 32800.00, 210.0, "ACTIVE", "uuid-adminactionlog-04"),
    (5, "ADM-0005", "Executive Strategic AdminActionLog 5", 65000.00, 400.0, "ACTIVE", "uuid-adminactionlog-05");

CREATE TABLE IF NOT EXISTS audit_governance_certificationsignoffs (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_certificationsignoffs_code ON audit_governance_certificationsignoffs(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_certificationsignoffs_org_status ON audit_governance_certificationsignoffs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_certificationsignoffs_priority ON audit_governance_certificationsignoffs(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_certificationsignoffs_created_at ON audit_governance_certificationsignoffs(created_at);

-- Operational seed data fixtures for audit_governance_certificationsignoffs
INSERT OR IGNORE INTO audit_governance_certificationsignoffs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CER-0001", "Primary Operational CertificationSignoff 1", 24500.00, 150.0, "ACTIVE", "uuid-certificationsignoff-01"),
    (2, "CER-0002", "Secondary Corporate CertificationSignoff 2", 18200.50, 80.0, "ACTIVE", "uuid-certificationsignoff-02"),
    (3, "CER-0003", "Consolidated Branch CertificationSignoff 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-certificationsignoff-03"),
    (4, "CER-0004", "Enterprise Audited CertificationSignoff 4", 32800.00, 210.0, "ACTIVE", "uuid-certificationsignoff-04"),
    (5, "CER-0005", "Executive Strategic CertificationSignoff 5", 65000.00, 400.0, "ACTIVE", "uuid-certificationsignoff-05");

CREATE TABLE IF NOT EXISTS audit_governance_complianceexceptionwaivers (
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

CREATE INDEX IF NOT EXISTS idx_audit_governance_complianceexceptionwaivers_code ON audit_governance_complianceexceptionwaivers(code);
CREATE INDEX IF NOT EXISTS idx_audit_governance_complianceexceptionwaivers_org_status ON audit_governance_complianceexceptionwaivers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_governance_complianceexceptionwaivers_priority ON audit_governance_complianceexceptionwaivers(priority);
CREATE INDEX IF NOT EXISTS idx_audit_governance_complianceexceptionwaivers_created_at ON audit_governance_complianceexceptionwaivers(created_at);

-- Operational seed data fixtures for audit_governance_complianceexceptionwaivers
INSERT OR IGNORE INTO audit_governance_complianceexceptionwaivers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational ComplianceExceptionWaiver 1", 24500.00, 150.0, "ACTIVE", "uuid-complianceexceptionwaiver-01"),
    (2, "COM-0002", "Secondary Corporate ComplianceExceptionWaiver 2", 18200.50, 80.0, "ACTIVE", "uuid-complianceexceptionwaiver-02"),
    (3, "COM-0003", "Consolidated Branch ComplianceExceptionWaiver 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-complianceexceptionwaiver-03"),
    (4, "COM-0004", "Enterprise Audited ComplianceExceptionWaiver 4", 32800.00, 210.0, "ACTIVE", "uuid-complianceexceptionwaiver-04"),
    (5, "COM-0005", "Executive Strategic ComplianceExceptionWaiver 5", 65000.00, 400.0, "ACTIVE", "uuid-complianceexceptionwaiver-05");

