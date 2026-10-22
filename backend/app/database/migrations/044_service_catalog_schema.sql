-- SmartERP Enterprise Titan Migration 044: ITIL Service Catalog & Enterprise Requests DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS service_catalog_servicecatalogitems (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecatalogitems_code ON service_catalog_servicecatalogitems(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecatalogitems_org_status ON service_catalog_servicecatalogitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecatalogitems_priority ON service_catalog_servicecatalogitems(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecatalogitems_created_at ON service_catalog_servicecatalogitems(created_at);

-- Operational seed data fixtures for service_catalog_servicecatalogitems
INSERT OR IGNORE INTO service_catalog_servicecatalogitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceCatalogItem 1", 24500.00, 150.0, "ACTIVE", "uuid-servicecatalogitem-01"),
    (2, "SER-0002", "Secondary Corporate ServiceCatalogItem 2", 18200.50, 80.0, "ACTIVE", "uuid-servicecatalogitem-02"),
    (3, "SER-0003", "Consolidated Branch ServiceCatalogItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicecatalogitem-03"),
    (4, "SER-0004", "Enterprise Audited ServiceCatalogItem 4", 32800.00, 210.0, "ACTIVE", "uuid-servicecatalogitem-04"),
    (5, "SER-0005", "Executive Strategic ServiceCatalogItem 5", 65000.00, 400.0, "ACTIVE", "uuid-servicecatalogitem-05");

CREATE TABLE IF NOT EXISTS service_catalog_servicecategorygroups (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecategorygroups_code ON service_catalog_servicecategorygroups(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecategorygroups_org_status ON service_catalog_servicecategorygroups(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecategorygroups_priority ON service_catalog_servicecategorygroups(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicecategorygroups_created_at ON service_catalog_servicecategorygroups(created_at);

-- Operational seed data fixtures for service_catalog_servicecategorygroups
INSERT OR IGNORE INTO service_catalog_servicecategorygroups (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceCategoryGroup 1", 24500.00, 150.0, "ACTIVE", "uuid-servicecategorygroup-01"),
    (2, "SER-0002", "Secondary Corporate ServiceCategoryGroup 2", 18200.50, 80.0, "ACTIVE", "uuid-servicecategorygroup-02"),
    (3, "SER-0003", "Consolidated Branch ServiceCategoryGroup 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicecategorygroup-03"),
    (4, "SER-0004", "Enterprise Audited ServiceCategoryGroup 4", 32800.00, 210.0, "ACTIVE", "uuid-servicecategorygroup-04"),
    (5, "SER-0005", "Executive Strategic ServiceCategoryGroup 5", 65000.00, 400.0, "ACTIVE", "uuid-servicecategorygroup-05");

CREATE TABLE IF NOT EXISTS service_catalog_serviceorderrequests (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_serviceorderrequests_code ON service_catalog_serviceorderrequests(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_serviceorderrequests_org_status ON service_catalog_serviceorderrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_serviceorderrequests_priority ON service_catalog_serviceorderrequests(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_serviceorderrequests_created_at ON service_catalog_serviceorderrequests(created_at);

-- Operational seed data fixtures for service_catalog_serviceorderrequests
INSERT OR IGNORE INTO service_catalog_serviceorderrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceOrderRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-serviceorderrequest-01"),
    (2, "SER-0002", "Secondary Corporate ServiceOrderRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-serviceorderrequest-02"),
    (3, "SER-0003", "Consolidated Branch ServiceOrderRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-serviceorderrequest-03"),
    (4, "SER-0004", "Enterprise Audited ServiceOrderRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-serviceorderrequest-04"),
    (5, "SER-0005", "Executive Strategic ServiceOrderRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-serviceorderrequest-05");

CREATE TABLE IF NOT EXISTS service_catalog_approvalhierarchypaths (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_approvalhierarchypaths_code ON service_catalog_approvalhierarchypaths(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_approvalhierarchypaths_org_status ON service_catalog_approvalhierarchypaths(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_approvalhierarchypaths_priority ON service_catalog_approvalhierarchypaths(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_approvalhierarchypaths_created_at ON service_catalog_approvalhierarchypaths(created_at);

-- Operational seed data fixtures for service_catalog_approvalhierarchypaths
INSERT OR IGNORE INTO service_catalog_approvalhierarchypaths (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "APP-0001", "Primary Operational ApprovalHierarchyPath 1", 24500.00, 150.0, "ACTIVE", "uuid-approvalhierarchypath-01"),
    (2, "APP-0002", "Secondary Corporate ApprovalHierarchyPath 2", 18200.50, 80.0, "ACTIVE", "uuid-approvalhierarchypath-02"),
    (3, "APP-0003", "Consolidated Branch ApprovalHierarchyPath 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-approvalhierarchypath-03"),
    (4, "APP-0004", "Enterprise Audited ApprovalHierarchyPath 4", 32800.00, 210.0, "ACTIVE", "uuid-approvalhierarchypath-04"),
    (5, "APP-0005", "Executive Strategic ApprovalHierarchyPath 5", 65000.00, 400.0, "ACTIVE", "uuid-approvalhierarchypath-05");

CREATE TABLE IF NOT EXISTS service_catalog_fulfillmenttasksteps (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_fulfillmenttasksteps_code ON service_catalog_fulfillmenttasksteps(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_fulfillmenttasksteps_org_status ON service_catalog_fulfillmenttasksteps(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_fulfillmenttasksteps_priority ON service_catalog_fulfillmenttasksteps(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_fulfillmenttasksteps_created_at ON service_catalog_fulfillmenttasksteps(created_at);

-- Operational seed data fixtures for service_catalog_fulfillmenttasksteps
INSERT OR IGNORE INTO service_catalog_fulfillmenttasksteps (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FUL-0001", "Primary Operational FulfillmentTaskStep 1", 24500.00, 150.0, "ACTIVE", "uuid-fulfillmenttaskstep-01"),
    (2, "FUL-0002", "Secondary Corporate FulfillmentTaskStep 2", 18200.50, 80.0, "ACTIVE", "uuid-fulfillmenttaskstep-02"),
    (3, "FUL-0003", "Consolidated Branch FulfillmentTaskStep 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fulfillmenttaskstep-03"),
    (4, "FUL-0004", "Enterprise Audited FulfillmentTaskStep 4", 32800.00, 210.0, "ACTIVE", "uuid-fulfillmenttaskstep-04"),
    (5, "FUL-0005", "Executive Strategic FulfillmentTaskStep 5", 65000.00, 400.0, "ACTIVE", "uuid-fulfillmenttaskstep-05");

CREATE TABLE IF NOT EXISTS service_catalog_slacommitmenttargets (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_slacommitmenttargets_code ON service_catalog_slacommitmenttargets(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_slacommitmenttargets_org_status ON service_catalog_slacommitmenttargets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_slacommitmenttargets_priority ON service_catalog_slacommitmenttargets(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_slacommitmenttargets_created_at ON service_catalog_slacommitmenttargets(created_at);

-- Operational seed data fixtures for service_catalog_slacommitmenttargets
INSERT OR IGNORE INTO service_catalog_slacommitmenttargets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SLA-0001", "Primary Operational SLACommitmentTarget 1", 24500.00, 150.0, "ACTIVE", "uuid-slacommitmenttarget-01"),
    (2, "SLA-0002", "Secondary Corporate SLACommitmentTarget 2", 18200.50, 80.0, "ACTIVE", "uuid-slacommitmenttarget-02"),
    (3, "SLA-0003", "Consolidated Branch SLACommitmentTarget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-slacommitmenttarget-03"),
    (4, "SLA-0004", "Enterprise Audited SLACommitmentTarget 4", 32800.00, 210.0, "ACTIVE", "uuid-slacommitmenttarget-04"),
    (5, "SLA-0005", "Executive Strategic SLACommitmentTarget 5", 65000.00, 400.0, "ACTIVE", "uuid-slacommitmenttarget-05");

CREATE TABLE IF NOT EXISTS service_catalog_hardwareprovisioningorders (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_hardwareprovisioningorders_code ON service_catalog_hardwareprovisioningorders(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_hardwareprovisioningorders_org_status ON service_catalog_hardwareprovisioningorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_hardwareprovisioningorders_priority ON service_catalog_hardwareprovisioningorders(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_hardwareprovisioningorders_created_at ON service_catalog_hardwareprovisioningorders(created_at);

-- Operational seed data fixtures for service_catalog_hardwareprovisioningorders
INSERT OR IGNORE INTO service_catalog_hardwareprovisioningorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HAR-0001", "Primary Operational HardwareProvisioningOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-hardwareprovisioningorder-01"),
    (2, "HAR-0002", "Secondary Corporate HardwareProvisioningOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-hardwareprovisioningorder-02"),
    (3, "HAR-0003", "Consolidated Branch HardwareProvisioningOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hardwareprovisioningorder-03"),
    (4, "HAR-0004", "Enterprise Audited HardwareProvisioningOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-hardwareprovisioningorder-04"),
    (5, "HAR-0005", "Executive Strategic HardwareProvisioningOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-hardwareprovisioningorder-05");

CREATE TABLE IF NOT EXISTS service_catalog_softwarelicenserequests (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_softwarelicenserequests_code ON service_catalog_softwarelicenserequests(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_softwarelicenserequests_org_status ON service_catalog_softwarelicenserequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_softwarelicenserequests_priority ON service_catalog_softwarelicenserequests(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_softwarelicenserequests_created_at ON service_catalog_softwarelicenserequests(created_at);

-- Operational seed data fixtures for service_catalog_softwarelicenserequests
INSERT OR IGNORE INTO service_catalog_softwarelicenserequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SOF-0001", "Primary Operational SoftwareLicenseRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-softwarelicenserequest-01"),
    (2, "SOF-0002", "Secondary Corporate SoftwareLicenseRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-softwarelicenserequest-02"),
    (3, "SOF-0003", "Consolidated Branch SoftwareLicenseRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-softwarelicenserequest-03"),
    (4, "SOF-0004", "Enterprise Audited SoftwareLicenseRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-softwarelicenserequest-04"),
    (5, "SOF-0005", "Executive Strategic SoftwareLicenseRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-softwarelicenserequest-05");

CREATE TABLE IF NOT EXISTS service_catalog_cloudresourcequotas (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_cloudresourcequotas_code ON service_catalog_cloudresourcequotas(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_cloudresourcequotas_org_status ON service_catalog_cloudresourcequotas(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_cloudresourcequotas_priority ON service_catalog_cloudresourcequotas(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_cloudresourcequotas_created_at ON service_catalog_cloudresourcequotas(created_at);

-- Operational seed data fixtures for service_catalog_cloudresourcequotas
INSERT OR IGNORE INTO service_catalog_cloudresourcequotas (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CLO-0001", "Primary Operational CloudResourceQuota 1", 24500.00, 150.0, "ACTIVE", "uuid-cloudresourcequota-01"),
    (2, "CLO-0002", "Secondary Corporate CloudResourceQuota 2", 18200.50, 80.0, "ACTIVE", "uuid-cloudresourcequota-02"),
    (3, "CLO-0003", "Consolidated Branch CloudResourceQuota 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cloudresourcequota-03"),
    (4, "CLO-0004", "Enterprise Audited CloudResourceQuota 4", 32800.00, 210.0, "ACTIVE", "uuid-cloudresourcequota-04"),
    (5, "CLO-0005", "Executive Strategic CloudResourceQuota 5", 65000.00, 400.0, "ACTIVE", "uuid-cloudresourcequota-05");

CREATE TABLE IF NOT EXISTS service_catalog_employeeaccessrequests (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_employeeaccessrequests_code ON service_catalog_employeeaccessrequests(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_employeeaccessrequests_org_status ON service_catalog_employeeaccessrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_employeeaccessrequests_priority ON service_catalog_employeeaccessrequests(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_employeeaccessrequests_created_at ON service_catalog_employeeaccessrequests(created_at);

-- Operational seed data fixtures for service_catalog_employeeaccessrequests
INSERT OR IGNORE INTO service_catalog_employeeaccessrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EMP-0001", "Primary Operational EmployeeAccessRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-employeeaccessrequest-01"),
    (2, "EMP-0002", "Secondary Corporate EmployeeAccessRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-employeeaccessrequest-02"),
    (3, "EMP-0003", "Consolidated Branch EmployeeAccessRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-employeeaccessrequest-03"),
    (4, "EMP-0004", "Enterprise Audited EmployeeAccessRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-employeeaccessrequest-04"),
    (5, "EMP-0005", "Executive Strategic EmployeeAccessRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-employeeaccessrequest-05");

CREATE TABLE IF NOT EXISTS service_catalog_costcenterchargebacks (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_costcenterchargebacks_code ON service_catalog_costcenterchargebacks(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_costcenterchargebacks_org_status ON service_catalog_costcenterchargebacks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_costcenterchargebacks_priority ON service_catalog_costcenterchargebacks(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_costcenterchargebacks_created_at ON service_catalog_costcenterchargebacks(created_at);

-- Operational seed data fixtures for service_catalog_costcenterchargebacks
INSERT OR IGNORE INTO service_catalog_costcenterchargebacks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COS-0001", "Primary Operational CostCenterChargeback 1", 24500.00, 150.0, "ACTIVE", "uuid-costcenterchargeback-01"),
    (2, "COS-0002", "Secondary Corporate CostCenterChargeback 2", 18200.50, 80.0, "ACTIVE", "uuid-costcenterchargeback-02"),
    (3, "COS-0003", "Consolidated Branch CostCenterChargeback 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-costcenterchargeback-03"),
    (4, "COS-0004", "Enterprise Audited CostCenterChargeback 4", 32800.00, 210.0, "ACTIVE", "uuid-costcenterchargeback-04"),
    (5, "COS-0005", "Executive Strategic CostCenterChargeback 5", 65000.00, 400.0, "ACTIVE", "uuid-costcenterchargeback-05");

CREATE TABLE IF NOT EXISTS service_catalog_servicedeskticketlinks (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_servicedeskticketlinks_code ON service_catalog_servicedeskticketlinks(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicedeskticketlinks_org_status ON service_catalog_servicedeskticketlinks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicedeskticketlinks_priority ON service_catalog_servicedeskticketlinks(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_servicedeskticketlinks_created_at ON service_catalog_servicedeskticketlinks(created_at);

-- Operational seed data fixtures for service_catalog_servicedeskticketlinks
INSERT OR IGNORE INTO service_catalog_servicedeskticketlinks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceDeskTicketLink 1", 24500.00, 150.0, "ACTIVE", "uuid-servicedeskticketlink-01"),
    (2, "SER-0002", "Secondary Corporate ServiceDeskTicketLink 2", 18200.50, 80.0, "ACTIVE", "uuid-servicedeskticketlink-02"),
    (3, "SER-0003", "Consolidated Branch ServiceDeskTicketLink 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicedeskticketlink-03"),
    (4, "SER-0004", "Enterprise Audited ServiceDeskTicketLink 4", 32800.00, 210.0, "ACTIVE", "uuid-servicedeskticketlink-04"),
    (5, "SER-0005", "Executive Strategic ServiceDeskTicketLink 5", 65000.00, 400.0, "ACTIVE", "uuid-servicedeskticketlink-05");

CREATE TABLE IF NOT EXISTS service_catalog_catalogitemdependencys (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_catalogitemdependencys_code ON service_catalog_catalogitemdependencys(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_catalogitemdependencys_org_status ON service_catalog_catalogitemdependencys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_catalogitemdependencys_priority ON service_catalog_catalogitemdependencys(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_catalogitemdependencys_created_at ON service_catalog_catalogitemdependencys(created_at);

-- Operational seed data fixtures for service_catalog_catalogitemdependencys
INSERT OR IGNORE INTO service_catalog_catalogitemdependencys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAT-0001", "Primary Operational CatalogItemDependency 1", 24500.00, 150.0, "ACTIVE", "uuid-catalogitemdependency-01"),
    (2, "CAT-0002", "Secondary Corporate CatalogItemDependency 2", 18200.50, 80.0, "ACTIVE", "uuid-catalogitemdependency-02"),
    (3, "CAT-0003", "Consolidated Branch CatalogItemDependency 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-catalogitemdependency-03"),
    (4, "CAT-0004", "Enterprise Audited CatalogItemDependency 4", 32800.00, 210.0, "ACTIVE", "uuid-catalogitemdependency-04"),
    (5, "CAT-0005", "Executive Strategic CatalogItemDependency 5", 65000.00, 400.0, "ACTIVE", "uuid-catalogitemdependency-05");

CREATE TABLE IF NOT EXISTS service_catalog_userentitlementrules (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_userentitlementrules_code ON service_catalog_userentitlementrules(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_userentitlementrules_org_status ON service_catalog_userentitlementrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_userentitlementrules_priority ON service_catalog_userentitlementrules(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_userentitlementrules_created_at ON service_catalog_userentitlementrules(created_at);

-- Operational seed data fixtures for service_catalog_userentitlementrules
INSERT OR IGNORE INTO service_catalog_userentitlementrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USE-0001", "Primary Operational UserEntitlementRule 1", 24500.00, 150.0, "ACTIVE", "uuid-userentitlementrule-01"),
    (2, "USE-0002", "Secondary Corporate UserEntitlementRule 2", 18200.50, 80.0, "ACTIVE", "uuid-userentitlementrule-02"),
    (3, "USE-0003", "Consolidated Branch UserEntitlementRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-userentitlementrule-03"),
    (4, "USE-0004", "Enterprise Audited UserEntitlementRule 4", 32800.00, 210.0, "ACTIVE", "uuid-userentitlementrule-04"),
    (5, "USE-0005", "Executive Strategic UserEntitlementRule 5", 65000.00, 400.0, "ACTIVE", "uuid-userentitlementrule-05");

CREATE TABLE IF NOT EXISTS service_catalog_requestsatisfactionscores (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_requestsatisfactionscores_code ON service_catalog_requestsatisfactionscores(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_requestsatisfactionscores_org_status ON service_catalog_requestsatisfactionscores(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_requestsatisfactionscores_priority ON service_catalog_requestsatisfactionscores(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_requestsatisfactionscores_created_at ON service_catalog_requestsatisfactionscores(created_at);

-- Operational seed data fixtures for service_catalog_requestsatisfactionscores
INSERT OR IGNORE INTO service_catalog_requestsatisfactionscores (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REQ-0001", "Primary Operational RequestSatisfactionScore 1", 24500.00, 150.0, "ACTIVE", "uuid-requestsatisfactionscore-01"),
    (2, "REQ-0002", "Secondary Corporate RequestSatisfactionScore 2", 18200.50, 80.0, "ACTIVE", "uuid-requestsatisfactionscore-02"),
    (3, "REQ-0003", "Consolidated Branch RequestSatisfactionScore 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-requestsatisfactionscore-03"),
    (4, "REQ-0004", "Enterprise Audited RequestSatisfactionScore 4", 32800.00, 210.0, "ACTIVE", "uuid-requestsatisfactionscore-04"),
    (5, "REQ-0005", "Executive Strategic RequestSatisfactionScore 5", 65000.00, 400.0, "ACTIVE", "uuid-requestsatisfactionscore-05");

CREATE TABLE IF NOT EXISTS service_catalog_recurringserviceorders (
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

CREATE INDEX IF NOT EXISTS idx_service_catalog_recurringserviceorders_code ON service_catalog_recurringserviceorders(code);
CREATE INDEX IF NOT EXISTS idx_service_catalog_recurringserviceorders_org_status ON service_catalog_recurringserviceorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_service_catalog_recurringserviceorders_priority ON service_catalog_recurringserviceorders(priority);
CREATE INDEX IF NOT EXISTS idx_service_catalog_recurringserviceorders_created_at ON service_catalog_recurringserviceorders(created_at);

-- Operational seed data fixtures for service_catalog_recurringserviceorders
INSERT OR IGNORE INTO service_catalog_recurringserviceorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REC-0001", "Primary Operational RecurringServiceOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-recurringserviceorder-01"),
    (2, "REC-0002", "Secondary Corporate RecurringServiceOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-recurringserviceorder-02"),
    (3, "REC-0003", "Consolidated Branch RecurringServiceOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-recurringserviceorder-03"),
    (4, "REC-0004", "Enterprise Audited RecurringServiceOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-recurringserviceorder-04"),
    (5, "REC-0005", "Executive Strategic RecurringServiceOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-recurringserviceorder-05");

