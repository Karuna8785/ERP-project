-- SmartERP Enterprise Titan Migration 019: Field Service & Dispatch Automation DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS field_service_serviceworkorders (
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

CREATE INDEX IF NOT EXISTS idx_field_service_serviceworkorders_code ON field_service_serviceworkorders(code);
CREATE INDEX IF NOT EXISTS idx_field_service_serviceworkorders_org_status ON field_service_serviceworkorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_serviceworkorders_priority ON field_service_serviceworkorders(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_serviceworkorders_created_at ON field_service_serviceworkorders(created_at);

-- Operational seed data fixtures for field_service_serviceworkorders
INSERT OR IGNORE INTO field_service_serviceworkorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceWorkOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-serviceworkorder-01"),
    (2, "SER-0002", "Secondary Corporate ServiceWorkOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-serviceworkorder-02"),
    (3, "SER-0003", "Consolidated Branch ServiceWorkOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-serviceworkorder-03"),
    (4, "SER-0004", "Enterprise Audited ServiceWorkOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-serviceworkorder-04"),
    (5, "SER-0005", "Executive Strategic ServiceWorkOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-serviceworkorder-05");

CREATE TABLE IF NOT EXISTS field_service_technicianprofiles (
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

CREATE INDEX IF NOT EXISTS idx_field_service_technicianprofiles_code ON field_service_technicianprofiles(code);
CREATE INDEX IF NOT EXISTS idx_field_service_technicianprofiles_org_status ON field_service_technicianprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_technicianprofiles_priority ON field_service_technicianprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_technicianprofiles_created_at ON field_service_technicianprofiles(created_at);

-- Operational seed data fixtures for field_service_technicianprofiles
INSERT OR IGNORE INTO field_service_technicianprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEC-0001", "Primary Operational TechnicianProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-technicianprofile-01"),
    (2, "TEC-0002", "Secondary Corporate TechnicianProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-technicianprofile-02"),
    (3, "TEC-0003", "Consolidated Branch TechnicianProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-technicianprofile-03"),
    (4, "TEC-0004", "Enterprise Audited TechnicianProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-technicianprofile-04"),
    (5, "TEC-0005", "Executive Strategic TechnicianProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-technicianprofile-05");

CREATE TABLE IF NOT EXISTS field_service_skillcertifications (
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

CREATE INDEX IF NOT EXISTS idx_field_service_skillcertifications_code ON field_service_skillcertifications(code);
CREATE INDEX IF NOT EXISTS idx_field_service_skillcertifications_org_status ON field_service_skillcertifications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_skillcertifications_priority ON field_service_skillcertifications(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_skillcertifications_created_at ON field_service_skillcertifications(created_at);

-- Operational seed data fixtures for field_service_skillcertifications
INSERT OR IGNORE INTO field_service_skillcertifications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SKI-0001", "Primary Operational SkillCertification 1", 24500.00, 150.0, "ACTIVE", "uuid-skillcertification-01"),
    (2, "SKI-0002", "Secondary Corporate SkillCertification 2", 18200.50, 80.0, "ACTIVE", "uuid-skillcertification-02"),
    (3, "SKI-0003", "Consolidated Branch SkillCertification 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-skillcertification-03"),
    (4, "SKI-0004", "Enterprise Audited SkillCertification 4", 32800.00, 210.0, "ACTIVE", "uuid-skillcertification-04"),
    (5, "SKI-0005", "Executive Strategic SkillCertification 5", 65000.00, 400.0, "ACTIVE", "uuid-skillcertification-05");

CREATE TABLE IF NOT EXISTS field_service_dispatchassignments (
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

CREATE INDEX IF NOT EXISTS idx_field_service_dispatchassignments_code ON field_service_dispatchassignments(code);
CREATE INDEX IF NOT EXISTS idx_field_service_dispatchassignments_org_status ON field_service_dispatchassignments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_dispatchassignments_priority ON field_service_dispatchassignments(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_dispatchassignments_created_at ON field_service_dispatchassignments(created_at);

-- Operational seed data fixtures for field_service_dispatchassignments
INSERT OR IGNORE INTO field_service_dispatchassignments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DispatchAssignment 1", 24500.00, 150.0, "ACTIVE", "uuid-dispatchassignment-01"),
    (2, "DIS-0002", "Secondary Corporate DispatchAssignment 2", 18200.50, 80.0, "ACTIVE", "uuid-dispatchassignment-02"),
    (3, "DIS-0003", "Consolidated Branch DispatchAssignment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dispatchassignment-03"),
    (4, "DIS-0004", "Enterprise Audited DispatchAssignment 4", 32800.00, 210.0, "ACTIVE", "uuid-dispatchassignment-04"),
    (5, "DIS-0005", "Executive Strategic DispatchAssignment 5", 65000.00, 400.0, "ACTIVE", "uuid-dispatchassignment-05");

CREATE TABLE IF NOT EXISTS field_service_routewayfindings (
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

CREATE INDEX IF NOT EXISTS idx_field_service_routewayfindings_code ON field_service_routewayfindings(code);
CREATE INDEX IF NOT EXISTS idx_field_service_routewayfindings_org_status ON field_service_routewayfindings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_routewayfindings_priority ON field_service_routewayfindings(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_routewayfindings_created_at ON field_service_routewayfindings(created_at);

-- Operational seed data fixtures for field_service_routewayfindings
INSERT OR IGNORE INTO field_service_routewayfindings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ROU-0001", "Primary Operational RouteWayfinding 1", 24500.00, 150.0, "ACTIVE", "uuid-routewayfinding-01"),
    (2, "ROU-0002", "Secondary Corporate RouteWayfinding 2", 18200.50, 80.0, "ACTIVE", "uuid-routewayfinding-02"),
    (3, "ROU-0003", "Consolidated Branch RouteWayfinding 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-routewayfinding-03"),
    (4, "ROU-0004", "Enterprise Audited RouteWayfinding 4", 32800.00, 210.0, "ACTIVE", "uuid-routewayfinding-04"),
    (5, "ROU-0005", "Executive Strategic RouteWayfinding 5", 65000.00, 400.0, "ACTIVE", "uuid-routewayfinding-05");

CREATE TABLE IF NOT EXISTS field_service_partsrequirements (
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

CREATE INDEX IF NOT EXISTS idx_field_service_partsrequirements_code ON field_service_partsrequirements(code);
CREATE INDEX IF NOT EXISTS idx_field_service_partsrequirements_org_status ON field_service_partsrequirements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_partsrequirements_priority ON field_service_partsrequirements(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_partsrequirements_created_at ON field_service_partsrequirements(created_at);

-- Operational seed data fixtures for field_service_partsrequirements
INSERT OR IGNORE INTO field_service_partsrequirements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartsRequirement 1", 24500.00, 150.0, "ACTIVE", "uuid-partsrequirement-01"),
    (2, "PAR-0002", "Secondary Corporate PartsRequirement 2", 18200.50, 80.0, "ACTIVE", "uuid-partsrequirement-02"),
    (3, "PAR-0003", "Consolidated Branch PartsRequirement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partsrequirement-03"),
    (4, "PAR-0004", "Enterprise Audited PartsRequirement 4", 32800.00, 210.0, "ACTIVE", "uuid-partsrequirement-04"),
    (5, "PAR-0005", "Executive Strategic PartsRequirement 5", 65000.00, 400.0, "ACTIVE", "uuid-partsrequirement-05");

CREATE TABLE IF NOT EXISTS field_service_vaninventorystocks (
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

CREATE INDEX IF NOT EXISTS idx_field_service_vaninventorystocks_code ON field_service_vaninventorystocks(code);
CREATE INDEX IF NOT EXISTS idx_field_service_vaninventorystocks_org_status ON field_service_vaninventorystocks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_vaninventorystocks_priority ON field_service_vaninventorystocks(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_vaninventorystocks_created_at ON field_service_vaninventorystocks(created_at);

-- Operational seed data fixtures for field_service_vaninventorystocks
INSERT OR IGNORE INTO field_service_vaninventorystocks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VAN-0001", "Primary Operational VanInventoryStock 1", 24500.00, 150.0, "ACTIVE", "uuid-vaninventorystock-01"),
    (2, "VAN-0002", "Secondary Corporate VanInventoryStock 2", 18200.50, 80.0, "ACTIVE", "uuid-vaninventorystock-02"),
    (3, "VAN-0003", "Consolidated Branch VanInventoryStock 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vaninventorystock-03"),
    (4, "VAN-0004", "Enterprise Audited VanInventoryStock 4", 32800.00, 210.0, "ACTIVE", "uuid-vaninventorystock-04"),
    (5, "VAN-0005", "Executive Strategic VanInventoryStock 5", 65000.00, 400.0, "ACTIVE", "uuid-vaninventorystock-05");

CREATE TABLE IF NOT EXISTS field_service_servicereportsignatures (
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

CREATE INDEX IF NOT EXISTS idx_field_service_servicereportsignatures_code ON field_service_servicereportsignatures(code);
CREATE INDEX IF NOT EXISTS idx_field_service_servicereportsignatures_org_status ON field_service_servicereportsignatures(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_servicereportsignatures_priority ON field_service_servicereportsignatures(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_servicereportsignatures_created_at ON field_service_servicereportsignatures(created_at);

-- Operational seed data fixtures for field_service_servicereportsignatures
INSERT OR IGNORE INTO field_service_servicereportsignatures (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceReportSignature 1", 24500.00, 150.0, "ACTIVE", "uuid-servicereportsignature-01"),
    (2, "SER-0002", "Secondary Corporate ServiceReportSignature 2", 18200.50, 80.0, "ACTIVE", "uuid-servicereportsignature-02"),
    (3, "SER-0003", "Consolidated Branch ServiceReportSignature 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicereportsignature-03"),
    (4, "SER-0004", "Enterprise Audited ServiceReportSignature 4", 32800.00, 210.0, "ACTIVE", "uuid-servicereportsignature-04"),
    (5, "SER-0005", "Executive Strategic ServiceReportSignature 5", 65000.00, 400.0, "ACTIVE", "uuid-servicereportsignature-05");

CREATE TABLE IF NOT EXISTS field_service_customerfeedbackratings (
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

CREATE INDEX IF NOT EXISTS idx_field_service_customerfeedbackratings_code ON field_service_customerfeedbackratings(code);
CREATE INDEX IF NOT EXISTS idx_field_service_customerfeedbackratings_org_status ON field_service_customerfeedbackratings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_customerfeedbackratings_priority ON field_service_customerfeedbackratings(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_customerfeedbackratings_created_at ON field_service_customerfeedbackratings(created_at);

-- Operational seed data fixtures for field_service_customerfeedbackratings
INSERT OR IGNORE INTO field_service_customerfeedbackratings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerFeedbackRating 1", 24500.00, 150.0, "ACTIVE", "uuid-customerfeedbackrating-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerFeedbackRating 2", 18200.50, 80.0, "ACTIVE", "uuid-customerfeedbackrating-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerFeedbackRating 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerfeedbackrating-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerFeedbackRating 4", 32800.00, 210.0, "ACTIVE", "uuid-customerfeedbackrating-04"),
    (5, "CUS-0005", "Executive Strategic CustomerFeedbackRating 5", 65000.00, 400.0, "ACTIVE", "uuid-customerfeedbackrating-05");

CREATE TABLE IF NOT EXISTS field_service_emergencycallouts (
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

CREATE INDEX IF NOT EXISTS idx_field_service_emergencycallouts_code ON field_service_emergencycallouts(code);
CREATE INDEX IF NOT EXISTS idx_field_service_emergencycallouts_org_status ON field_service_emergencycallouts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_emergencycallouts_priority ON field_service_emergencycallouts(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_emergencycallouts_created_at ON field_service_emergencycallouts(created_at);

-- Operational seed data fixtures for field_service_emergencycallouts
INSERT OR IGNORE INTO field_service_emergencycallouts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EME-0001", "Primary Operational EmergencyCallout 1", 24500.00, 150.0, "ACTIVE", "uuid-emergencycallout-01"),
    (2, "EME-0002", "Secondary Corporate EmergencyCallout 2", 18200.50, 80.0, "ACTIVE", "uuid-emergencycallout-02"),
    (3, "EME-0003", "Consolidated Branch EmergencyCallout 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-emergencycallout-03"),
    (4, "EME-0004", "Enterprise Audited EmergencyCallout 4", 32800.00, 210.0, "ACTIVE", "uuid-emergencycallout-04"),
    (5, "EME-0005", "Executive Strategic EmergencyCallout 5", 65000.00, 400.0, "ACTIVE", "uuid-emergencycallout-05");

CREATE TABLE IF NOT EXISTS field_service_maintenancechecklists (
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

CREATE INDEX IF NOT EXISTS idx_field_service_maintenancechecklists_code ON field_service_maintenancechecklists(code);
CREATE INDEX IF NOT EXISTS idx_field_service_maintenancechecklists_org_status ON field_service_maintenancechecklists(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_maintenancechecklists_priority ON field_service_maintenancechecklists(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_maintenancechecklists_created_at ON field_service_maintenancechecklists(created_at);

-- Operational seed data fixtures for field_service_maintenancechecklists
INSERT OR IGNORE INTO field_service_maintenancechecklists (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAI-0001", "Primary Operational MaintenanceChecklist 1", 24500.00, 150.0, "ACTIVE", "uuid-maintenancechecklist-01"),
    (2, "MAI-0002", "Secondary Corporate MaintenanceChecklist 2", 18200.50, 80.0, "ACTIVE", "uuid-maintenancechecklist-02"),
    (3, "MAI-0003", "Consolidated Branch MaintenanceChecklist 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-maintenancechecklist-03"),
    (4, "MAI-0004", "Enterprise Audited MaintenanceChecklist 4", 32800.00, 210.0, "ACTIVE", "uuid-maintenancechecklist-04"),
    (5, "MAI-0005", "Executive Strategic MaintenanceChecklist 5", 65000.00, 400.0, "ACTIVE", "uuid-maintenancechecklist-05");

CREATE TABLE IF NOT EXISTS field_service_warrantyentitlements (
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

CREATE INDEX IF NOT EXISTS idx_field_service_warrantyentitlements_code ON field_service_warrantyentitlements(code);
CREATE INDEX IF NOT EXISTS idx_field_service_warrantyentitlements_org_status ON field_service_warrantyentitlements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_warrantyentitlements_priority ON field_service_warrantyentitlements(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_warrantyentitlements_created_at ON field_service_warrantyentitlements(created_at);

-- Operational seed data fixtures for field_service_warrantyentitlements
INSERT OR IGNORE INTO field_service_warrantyentitlements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAR-0001", "Primary Operational WarrantyEntitlement 1", 24500.00, 150.0, "ACTIVE", "uuid-warrantyentitlement-01"),
    (2, "WAR-0002", "Secondary Corporate WarrantyEntitlement 2", 18200.50, 80.0, "ACTIVE", "uuid-warrantyentitlement-02"),
    (3, "WAR-0003", "Consolidated Branch WarrantyEntitlement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-warrantyentitlement-03"),
    (4, "WAR-0004", "Enterprise Audited WarrantyEntitlement 4", 32800.00, 210.0, "ACTIVE", "uuid-warrantyentitlement-04"),
    (5, "WAR-0005", "Executive Strategic WarrantyEntitlement 5", 65000.00, 400.0, "ACTIVE", "uuid-warrantyentitlement-05");

CREATE TABLE IF NOT EXISTS field_service_servicelevelbreachalerts (
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

CREATE INDEX IF NOT EXISTS idx_field_service_servicelevelbreachalerts_code ON field_service_servicelevelbreachalerts(code);
CREATE INDEX IF NOT EXISTS idx_field_service_servicelevelbreachalerts_org_status ON field_service_servicelevelbreachalerts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_servicelevelbreachalerts_priority ON field_service_servicelevelbreachalerts(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_servicelevelbreachalerts_created_at ON field_service_servicelevelbreachalerts(created_at);

-- Operational seed data fixtures for field_service_servicelevelbreachalerts
INSERT OR IGNORE INTO field_service_servicelevelbreachalerts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceLevelBreachAlert 1", 24500.00, 150.0, "ACTIVE", "uuid-servicelevelbreachalert-01"),
    (2, "SER-0002", "Secondary Corporate ServiceLevelBreachAlert 2", 18200.50, 80.0, "ACTIVE", "uuid-servicelevelbreachalert-02"),
    (3, "SER-0003", "Consolidated Branch ServiceLevelBreachAlert 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicelevelbreachalert-03"),
    (4, "SER-0004", "Enterprise Audited ServiceLevelBreachAlert 4", 32800.00, 210.0, "ACTIVE", "uuid-servicelevelbreachalert-04"),
    (5, "SER-0005", "Executive Strategic ServiceLevelBreachAlert 5", 65000.00, 400.0, "ACTIVE", "uuid-servicelevelbreachalert-05");

CREATE TABLE IF NOT EXISTS field_service_timeonsitelogs (
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

CREATE INDEX IF NOT EXISTS idx_field_service_timeonsitelogs_code ON field_service_timeonsitelogs(code);
CREATE INDEX IF NOT EXISTS idx_field_service_timeonsitelogs_org_status ON field_service_timeonsitelogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_timeonsitelogs_priority ON field_service_timeonsitelogs(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_timeonsitelogs_created_at ON field_service_timeonsitelogs(created_at);

-- Operational seed data fixtures for field_service_timeonsitelogs
INSERT OR IGNORE INTO field_service_timeonsitelogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIM-0001", "Primary Operational TimeOnSiteLog 1", 24500.00, 150.0, "ACTIVE", "uuid-timeonsitelog-01"),
    (2, "TIM-0002", "Secondary Corporate TimeOnSiteLog 2", 18200.50, 80.0, "ACTIVE", "uuid-timeonsitelog-02"),
    (3, "TIM-0003", "Consolidated Branch TimeOnSiteLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-timeonsitelog-03"),
    (4, "TIM-0004", "Enterprise Audited TimeOnSiteLog 4", 32800.00, 210.0, "ACTIVE", "uuid-timeonsitelog-04"),
    (5, "TIM-0005", "Executive Strategic TimeOnSiteLog 5", 65000.00, 400.0, "ACTIVE", "uuid-timeonsitelog-05");

CREATE TABLE IF NOT EXISTS field_service_equipmentassethistorys (
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

CREATE INDEX IF NOT EXISTS idx_field_service_equipmentassethistorys_code ON field_service_equipmentassethistorys(code);
CREATE INDEX IF NOT EXISTS idx_field_service_equipmentassethistorys_org_status ON field_service_equipmentassethistorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_equipmentassethistorys_priority ON field_service_equipmentassethistorys(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_equipmentassethistorys_created_at ON field_service_equipmentassethistorys(created_at);

-- Operational seed data fixtures for field_service_equipmentassethistorys
INSERT OR IGNORE INTO field_service_equipmentassethistorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EQU-0001", "Primary Operational EquipmentAssetHistory 1", 24500.00, 150.0, "ACTIVE", "uuid-equipmentassethistory-01"),
    (2, "EQU-0002", "Secondary Corporate EquipmentAssetHistory 2", 18200.50, 80.0, "ACTIVE", "uuid-equipmentassethistory-02"),
    (3, "EQU-0003", "Consolidated Branch EquipmentAssetHistory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-equipmentassethistory-03"),
    (4, "EQU-0004", "Enterprise Audited EquipmentAssetHistory 4", 32800.00, 210.0, "ACTIVE", "uuid-equipmentassethistory-04"),
    (5, "EQU-0005", "Executive Strategic EquipmentAssetHistory 5", 65000.00, 400.0, "ACTIVE", "uuid-equipmentassethistory-05");

CREATE TABLE IF NOT EXISTS field_service_fieldexpenseclaims (
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

CREATE INDEX IF NOT EXISTS idx_field_service_fieldexpenseclaims_code ON field_service_fieldexpenseclaims(code);
CREATE INDEX IF NOT EXISTS idx_field_service_fieldexpenseclaims_org_status ON field_service_fieldexpenseclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_field_service_fieldexpenseclaims_priority ON field_service_fieldexpenseclaims(priority);
CREATE INDEX IF NOT EXISTS idx_field_service_fieldexpenseclaims_created_at ON field_service_fieldexpenseclaims(created_at);

-- Operational seed data fixtures for field_service_fieldexpenseclaims
INSERT OR IGNORE INTO field_service_fieldexpenseclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FIE-0001", "Primary Operational FieldExpenseClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-fieldexpenseclaim-01"),
    (2, "FIE-0002", "Secondary Corporate FieldExpenseClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-fieldexpenseclaim-02"),
    (3, "FIE-0003", "Consolidated Branch FieldExpenseClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fieldexpenseclaim-03"),
    (4, "FIE-0004", "Enterprise Audited FieldExpenseClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-fieldexpenseclaim-04"),
    (5, "FIE-0005", "Executive Strategic FieldExpenseClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-fieldexpenseclaim-05");

