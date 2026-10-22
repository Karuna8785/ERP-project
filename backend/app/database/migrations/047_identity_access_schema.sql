-- SmartERP Enterprise Titan Migration 047: Identity & Access Management (IAM / SSO) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS identity_access_useridentityprofiles (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_useridentityprofiles_code ON identity_access_useridentityprofiles(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_useridentityprofiles_org_status ON identity_access_useridentityprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_useridentityprofiles_priority ON identity_access_useridentityprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_useridentityprofiles_created_at ON identity_access_useridentityprofiles(created_at);

-- Operational seed data fixtures for identity_access_useridentityprofiles
INSERT OR IGNORE INTO identity_access_useridentityprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USE-0001", "Primary Operational UserIdentityProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-useridentityprofile-01"),
    (2, "USE-0002", "Secondary Corporate UserIdentityProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-useridentityprofile-02"),
    (3, "USE-0003", "Consolidated Branch UserIdentityProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-useridentityprofile-03"),
    (4, "USE-0004", "Enterprise Audited UserIdentityProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-useridentityprofile-04"),
    (5, "USE-0005", "Executive Strategic UserIdentityProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-useridentityprofile-05");

CREATE TABLE IF NOT EXISTS identity_access_directoryservicegroups (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_directoryservicegroups_code ON identity_access_directoryservicegroups(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_directoryservicegroups_org_status ON identity_access_directoryservicegroups(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_directoryservicegroups_priority ON identity_access_directoryservicegroups(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_directoryservicegroups_created_at ON identity_access_directoryservicegroups(created_at);

-- Operational seed data fixtures for identity_access_directoryservicegroups
INSERT OR IGNORE INTO identity_access_directoryservicegroups (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIR-0001", "Primary Operational DirectoryServiceGroup 1", 24500.00, 150.0, "ACTIVE", "uuid-directoryservicegroup-01"),
    (2, "DIR-0002", "Secondary Corporate DirectoryServiceGroup 2", 18200.50, 80.0, "ACTIVE", "uuid-directoryservicegroup-02"),
    (3, "DIR-0003", "Consolidated Branch DirectoryServiceGroup 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-directoryservicegroup-03"),
    (4, "DIR-0004", "Enterprise Audited DirectoryServiceGroup 4", 32800.00, 210.0, "ACTIVE", "uuid-directoryservicegroup-04"),
    (5, "DIR-0005", "Executive Strategic DirectoryServiceGroup 5", 65000.00, 400.0, "ACTIVE", "uuid-directoryservicegroup-05");

CREATE TABLE IF NOT EXISTS identity_access_ssoidentityproviders (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_ssoidentityproviders_code ON identity_access_ssoidentityproviders(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_ssoidentityproviders_org_status ON identity_access_ssoidentityproviders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_ssoidentityproviders_priority ON identity_access_ssoidentityproviders(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_ssoidentityproviders_created_at ON identity_access_ssoidentityproviders(created_at);

-- Operational seed data fixtures for identity_access_ssoidentityproviders
INSERT OR IGNORE INTO identity_access_ssoidentityproviders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SSO-0001", "Primary Operational SSOIdentityProvider 1", 24500.00, 150.0, "ACTIVE", "uuid-ssoidentityprovider-01"),
    (2, "SSO-0002", "Secondary Corporate SSOIdentityProvider 2", 18200.50, 80.0, "ACTIVE", "uuid-ssoidentityprovider-02"),
    (3, "SSO-0003", "Consolidated Branch SSOIdentityProvider 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ssoidentityprovider-03"),
    (4, "SSO-0004", "Enterprise Audited SSOIdentityProvider 4", 32800.00, 210.0, "ACTIVE", "uuid-ssoidentityprovider-04"),
    (5, "SSO-0005", "Executive Strategic SSOIdentityProvider 5", 65000.00, 400.0, "ACTIVE", "uuid-ssoidentityprovider-05");

CREATE TABLE IF NOT EXISTS identity_access_samlmetadataconfigs (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_samlmetadataconfigs_code ON identity_access_samlmetadataconfigs(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_samlmetadataconfigs_org_status ON identity_access_samlmetadataconfigs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_samlmetadataconfigs_priority ON identity_access_samlmetadataconfigs(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_samlmetadataconfigs_created_at ON identity_access_samlmetadataconfigs(created_at);

-- Operational seed data fixtures for identity_access_samlmetadataconfigs
INSERT OR IGNORE INTO identity_access_samlmetadataconfigs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAM-0001", "Primary Operational SAMLMetadataConfig 1", 24500.00, 150.0, "ACTIVE", "uuid-samlmetadataconfig-01"),
    (2, "SAM-0002", "Secondary Corporate SAMLMetadataConfig 2", 18200.50, 80.0, "ACTIVE", "uuid-samlmetadataconfig-02"),
    (3, "SAM-0003", "Consolidated Branch SAMLMetadataConfig 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-samlmetadataconfig-03"),
    (4, "SAM-0004", "Enterprise Audited SAMLMetadataConfig 4", 32800.00, 210.0, "ACTIVE", "uuid-samlmetadataconfig-04"),
    (5, "SAM-0005", "Executive Strategic SAMLMetadataConfig 5", 65000.00, 400.0, "ACTIVE", "uuid-samlmetadataconfig-05");

CREATE TABLE IF NOT EXISTS identity_access_scimprovisioningrules (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_scimprovisioningrules_code ON identity_access_scimprovisioningrules(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_scimprovisioningrules_org_status ON identity_access_scimprovisioningrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_scimprovisioningrules_priority ON identity_access_scimprovisioningrules(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_scimprovisioningrules_created_at ON identity_access_scimprovisioningrules(created_at);

-- Operational seed data fixtures for identity_access_scimprovisioningrules
INSERT OR IGNORE INTO identity_access_scimprovisioningrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SCI-0001", "Primary Operational SCIMProvisioningRule 1", 24500.00, 150.0, "ACTIVE", "uuid-scimprovisioningrule-01"),
    (2, "SCI-0002", "Secondary Corporate SCIMProvisioningRule 2", 18200.50, 80.0, "ACTIVE", "uuid-scimprovisioningrule-02"),
    (3, "SCI-0003", "Consolidated Branch SCIMProvisioningRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-scimprovisioningrule-03"),
    (4, "SCI-0004", "Enterprise Audited SCIMProvisioningRule 4", 32800.00, 210.0, "ACTIVE", "uuid-scimprovisioningrule-04"),
    (5, "SCI-0005", "Executive Strategic SCIMProvisioningRule 5", 65000.00, 400.0, "ACTIVE", "uuid-scimprovisioningrule-05");

CREATE TABLE IF NOT EXISTS identity_access_mfatokendevices (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_mfatokendevices_code ON identity_access_mfatokendevices(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_mfatokendevices_org_status ON identity_access_mfatokendevices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_mfatokendevices_priority ON identity_access_mfatokendevices(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_mfatokendevices_created_at ON identity_access_mfatokendevices(created_at);

-- Operational seed data fixtures for identity_access_mfatokendevices
INSERT OR IGNORE INTO identity_access_mfatokendevices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MFA-0001", "Primary Operational MFATokenDevice 1", 24500.00, 150.0, "ACTIVE", "uuid-mfatokendevice-01"),
    (2, "MFA-0002", "Secondary Corporate MFATokenDevice 2", 18200.50, 80.0, "ACTIVE", "uuid-mfatokendevice-02"),
    (3, "MFA-0003", "Consolidated Branch MFATokenDevice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-mfatokendevice-03"),
    (4, "MFA-0004", "Enterprise Audited MFATokenDevice 4", 32800.00, 210.0, "ACTIVE", "uuid-mfatokendevice-04"),
    (5, "MFA-0005", "Executive Strategic MFATokenDevice 5", 65000.00, 400.0, "ACTIVE", "uuid-mfatokendevice-05");

CREATE TABLE IF NOT EXISTS identity_access_passwordpolicyrules (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_passwordpolicyrules_code ON identity_access_passwordpolicyrules(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_passwordpolicyrules_org_status ON identity_access_passwordpolicyrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_passwordpolicyrules_priority ON identity_access_passwordpolicyrules(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_passwordpolicyrules_created_at ON identity_access_passwordpolicyrules(created_at);

-- Operational seed data fixtures for identity_access_passwordpolicyrules
INSERT OR IGNORE INTO identity_access_passwordpolicyrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAS-0001", "Primary Operational PasswordPolicyRule 1", 24500.00, 150.0, "ACTIVE", "uuid-passwordpolicyrule-01"),
    (2, "PAS-0002", "Secondary Corporate PasswordPolicyRule 2", 18200.50, 80.0, "ACTIVE", "uuid-passwordpolicyrule-02"),
    (3, "PAS-0003", "Consolidated Branch PasswordPolicyRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-passwordpolicyrule-03"),
    (4, "PAS-0004", "Enterprise Audited PasswordPolicyRule 4", 32800.00, 210.0, "ACTIVE", "uuid-passwordpolicyrule-04"),
    (5, "PAS-0005", "Executive Strategic PasswordPolicyRule 5", 65000.00, 400.0, "ACTIVE", "uuid-passwordpolicyrule-05");

CREATE TABLE IF NOT EXISTS identity_access_sessiontokenregistrys (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_sessiontokenregistrys_code ON identity_access_sessiontokenregistrys(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_sessiontokenregistrys_org_status ON identity_access_sessiontokenregistrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_sessiontokenregistrys_priority ON identity_access_sessiontokenregistrys(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_sessiontokenregistrys_created_at ON identity_access_sessiontokenregistrys(created_at);

-- Operational seed data fixtures for identity_access_sessiontokenregistrys
INSERT OR IGNORE INTO identity_access_sessiontokenregistrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SES-0001", "Primary Operational SessionTokenRegistry 1", 24500.00, 150.0, "ACTIVE", "uuid-sessiontokenregistry-01"),
    (2, "SES-0002", "Secondary Corporate SessionTokenRegistry 2", 18200.50, 80.0, "ACTIVE", "uuid-sessiontokenregistry-02"),
    (3, "SES-0003", "Consolidated Branch SessionTokenRegistry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sessiontokenregistry-03"),
    (4, "SES-0004", "Enterprise Audited SessionTokenRegistry 4", 32800.00, 210.0, "ACTIVE", "uuid-sessiontokenregistry-04"),
    (5, "SES-0005", "Executive Strategic SessionTokenRegistry 5", 65000.00, 400.0, "ACTIVE", "uuid-sessiontokenregistry-05");

CREATE TABLE IF NOT EXISTS identity_access_roleassignmentscopes (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_roleassignmentscopes_code ON identity_access_roleassignmentscopes(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_roleassignmentscopes_org_status ON identity_access_roleassignmentscopes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_roleassignmentscopes_priority ON identity_access_roleassignmentscopes(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_roleassignmentscopes_created_at ON identity_access_roleassignmentscopes(created_at);

-- Operational seed data fixtures for identity_access_roleassignmentscopes
INSERT OR IGNORE INTO identity_access_roleassignmentscopes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ROL-0001", "Primary Operational RoleAssignmentScope 1", 24500.00, 150.0, "ACTIVE", "uuid-roleassignmentscope-01"),
    (2, "ROL-0002", "Secondary Corporate RoleAssignmentScope 2", 18200.50, 80.0, "ACTIVE", "uuid-roleassignmentscope-02"),
    (3, "ROL-0003", "Consolidated Branch RoleAssignmentScope 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-roleassignmentscope-03"),
    (4, "ROL-0004", "Enterprise Audited RoleAssignmentScope 4", 32800.00, 210.0, "ACTIVE", "uuid-roleassignmentscope-04"),
    (5, "ROL-0005", "Executive Strategic RoleAssignmentScope 5", 65000.00, 400.0, "ACTIVE", "uuid-roleassignmentscope-05");

CREATE TABLE IF NOT EXISTS identity_access_emergencyaccountbreakglasss (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_emergencyaccountbreakglasss_code ON identity_access_emergencyaccountbreakglasss(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_emergencyaccountbreakglasss_org_status ON identity_access_emergencyaccountbreakglasss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_emergencyaccountbreakglasss_priority ON identity_access_emergencyaccountbreakglasss(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_emergencyaccountbreakglasss_created_at ON identity_access_emergencyaccountbreakglasss(created_at);

-- Operational seed data fixtures for identity_access_emergencyaccountbreakglasss
INSERT OR IGNORE INTO identity_access_emergencyaccountbreakglasss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EME-0001", "Primary Operational EmergencyAccountBreakGlass 1", 24500.00, 150.0, "ACTIVE", "uuid-emergencyaccountbreakglass-01"),
    (2, "EME-0002", "Secondary Corporate EmergencyAccountBreakGlass 2", 18200.50, 80.0, "ACTIVE", "uuid-emergencyaccountbreakglass-02"),
    (3, "EME-0003", "Consolidated Branch EmergencyAccountBreakGlass 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-emergencyaccountbreakglass-03"),
    (4, "EME-0004", "Enterprise Audited EmergencyAccountBreakGlass 4", 32800.00, 210.0, "ACTIVE", "uuid-emergencyaccountbreakglass-04"),
    (5, "EME-0005", "Executive Strategic EmergencyAccountBreakGlass 5", 65000.00, 400.0, "ACTIVE", "uuid-emergencyaccountbreakglass-05");

CREATE TABLE IF NOT EXISTS identity_access_oauthclientapplications (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_oauthclientapplications_code ON identity_access_oauthclientapplications(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_oauthclientapplications_org_status ON identity_access_oauthclientapplications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_oauthclientapplications_priority ON identity_access_oauthclientapplications(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_oauthclientapplications_created_at ON identity_access_oauthclientapplications(created_at);

-- Operational seed data fixtures for identity_access_oauthclientapplications
INSERT OR IGNORE INTO identity_access_oauthclientapplications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OAU-0001", "Primary Operational OAuthClientApplication 1", 24500.00, 150.0, "ACTIVE", "uuid-oauthclientapplication-01"),
    (2, "OAU-0002", "Secondary Corporate OAuthClientApplication 2", 18200.50, 80.0, "ACTIVE", "uuid-oauthclientapplication-02"),
    (3, "OAU-0003", "Consolidated Branch OAuthClientApplication 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-oauthclientapplication-03"),
    (4, "OAU-0004", "Enterprise Audited OAuthClientApplication 4", 32800.00, 210.0, "ACTIVE", "uuid-oauthclientapplication-04"),
    (5, "OAU-0005", "Executive Strategic OAuthClientApplication 5", 65000.00, 400.0, "ACTIVE", "uuid-oauthclientapplication-05");

CREATE TABLE IF NOT EXISTS identity_access_userconsentrecords (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_userconsentrecords_code ON identity_access_userconsentrecords(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_userconsentrecords_org_status ON identity_access_userconsentrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_userconsentrecords_priority ON identity_access_userconsentrecords(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_userconsentrecords_created_at ON identity_access_userconsentrecords(created_at);

-- Operational seed data fixtures for identity_access_userconsentrecords
INSERT OR IGNORE INTO identity_access_userconsentrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USE-0001", "Primary Operational UserConsentRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-userconsentrecord-01"),
    (2, "USE-0002", "Secondary Corporate UserConsentRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-userconsentrecord-02"),
    (3, "USE-0003", "Consolidated Branch UserConsentRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-userconsentrecord-03"),
    (4, "USE-0004", "Enterprise Audited UserConsentRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-userconsentrecord-04"),
    (5, "USE-0005", "Executive Strategic UserConsentRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-userconsentrecord-05");

CREATE TABLE IF NOT EXISTS identity_access_accessreviewattestations (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_accessreviewattestations_code ON identity_access_accessreviewattestations(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_accessreviewattestations_org_status ON identity_access_accessreviewattestations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_accessreviewattestations_priority ON identity_access_accessreviewattestations(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_accessreviewattestations_created_at ON identity_access_accessreviewattestations(created_at);

-- Operational seed data fixtures for identity_access_accessreviewattestations
INSERT OR IGNORE INTO identity_access_accessreviewattestations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACC-0001", "Primary Operational AccessReviewAttestation 1", 24500.00, 150.0, "ACTIVE", "uuid-accessreviewattestation-01"),
    (2, "ACC-0002", "Secondary Corporate AccessReviewAttestation 2", 18200.50, 80.0, "ACTIVE", "uuid-accessreviewattestation-02"),
    (3, "ACC-0003", "Consolidated Branch AccessReviewAttestation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-accessreviewattestation-03"),
    (4, "ACC-0004", "Enterprise Audited AccessReviewAttestation 4", 32800.00, 210.0, "ACTIVE", "uuid-accessreviewattestation-04"),
    (5, "ACC-0005", "Executive Strategic AccessReviewAttestation 5", 65000.00, 400.0, "ACTIVE", "uuid-accessreviewattestation-05");

CREATE TABLE IF NOT EXISTS identity_access_authenticationauditlogs (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_authenticationauditlogs_code ON identity_access_authenticationauditlogs(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_authenticationauditlogs_org_status ON identity_access_authenticationauditlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_authenticationauditlogs_priority ON identity_access_authenticationauditlogs(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_authenticationauditlogs_created_at ON identity_access_authenticationauditlogs(created_at);

-- Operational seed data fixtures for identity_access_authenticationauditlogs
INSERT OR IGNORE INTO identity_access_authenticationauditlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "AUT-0001", "Primary Operational AuthenticationAuditLog 1", 24500.00, 150.0, "ACTIVE", "uuid-authenticationauditlog-01"),
    (2, "AUT-0002", "Secondary Corporate AuthenticationAuditLog 2", 18200.50, 80.0, "ACTIVE", "uuid-authenticationauditlog-02"),
    (3, "AUT-0003", "Consolidated Branch AuthenticationAuditLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-authenticationauditlog-03"),
    (4, "AUT-0004", "Enterprise Audited AuthenticationAuditLog 4", 32800.00, 210.0, "ACTIVE", "uuid-authenticationauditlog-04"),
    (5, "AUT-0005", "Executive Strategic AuthenticationAuditLog 5", 65000.00, 400.0, "ACTIVE", "uuid-authenticationauditlog-05");

CREATE TABLE IF NOT EXISTS identity_access_securitykeywebauthns (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_securitykeywebauthns_code ON identity_access_securitykeywebauthns(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_securitykeywebauthns_org_status ON identity_access_securitykeywebauthns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_securitykeywebauthns_priority ON identity_access_securitykeywebauthns(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_securitykeywebauthns_created_at ON identity_access_securitykeywebauthns(created_at);

-- Operational seed data fixtures for identity_access_securitykeywebauthns
INSERT OR IGNORE INTO identity_access_securitykeywebauthns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEC-0001", "Primary Operational SecurityKeyWebAuthn 1", 24500.00, 150.0, "ACTIVE", "uuid-securitykeywebauthn-01"),
    (2, "SEC-0002", "Secondary Corporate SecurityKeyWebAuthn 2", 18200.50, 80.0, "ACTIVE", "uuid-securitykeywebauthn-02"),
    (3, "SEC-0003", "Consolidated Branch SecurityKeyWebAuthn 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-securitykeywebauthn-03"),
    (4, "SEC-0004", "Enterprise Audited SecurityKeyWebAuthn 4", 32800.00, 210.0, "ACTIVE", "uuid-securitykeywebauthn-04"),
    (5, "SEC-0005", "Executive Strategic SecurityKeyWebAuthn 5", 65000.00, 400.0, "ACTIVE", "uuid-securitykeywebauthn-05");

CREATE TABLE IF NOT EXISTS identity_access_tenantdomainmappings (
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

CREATE INDEX IF NOT EXISTS idx_identity_access_tenantdomainmappings_code ON identity_access_tenantdomainmappings(code);
CREATE INDEX IF NOT EXISTS idx_identity_access_tenantdomainmappings_org_status ON identity_access_tenantdomainmappings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_identity_access_tenantdomainmappings_priority ON identity_access_tenantdomainmappings(priority);
CREATE INDEX IF NOT EXISTS idx_identity_access_tenantdomainmappings_created_at ON identity_access_tenantdomainmappings(created_at);

-- Operational seed data fixtures for identity_access_tenantdomainmappings
INSERT OR IGNORE INTO identity_access_tenantdomainmappings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEN-0001", "Primary Operational TenantDomainMapping 1", 24500.00, 150.0, "ACTIVE", "uuid-tenantdomainmapping-01"),
    (2, "TEN-0002", "Secondary Corporate TenantDomainMapping 2", 18200.50, 80.0, "ACTIVE", "uuid-tenantdomainmapping-02"),
    (3, "TEN-0003", "Consolidated Branch TenantDomainMapping 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tenantdomainmapping-03"),
    (4, "TEN-0004", "Enterprise Audited TenantDomainMapping 4", 32800.00, 210.0, "ACTIVE", "uuid-tenantdomainmapping-04"),
    (5, "TEN-0005", "Executive Strategic TenantDomainMapping 5", 65000.00, 400.0, "ACTIVE", "uuid-tenantdomainmapping-05");

