-- SmartERP Enterprise Titan Migration 030: Facilities & Corporate Real Estate DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS facilities_management_facilitybuildings (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_facilitybuildings_code ON facilities_management_facilitybuildings(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_facilitybuildings_org_status ON facilities_management_facilitybuildings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_facilitybuildings_priority ON facilities_management_facilitybuildings(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_facilitybuildings_created_at ON facilities_management_facilitybuildings(created_at);

-- Operational seed data fixtures for facilities_management_facilitybuildings
INSERT OR IGNORE INTO facilities_management_facilitybuildings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FAC-0001", "Primary Operational FacilityBuilding 1", 24500.00, 150.0, "ACTIVE", "uuid-facilitybuilding-01"),
    (2, "FAC-0002", "Secondary Corporate FacilityBuilding 2", 18200.50, 80.0, "ACTIVE", "uuid-facilitybuilding-02"),
    (3, "FAC-0003", "Consolidated Branch FacilityBuilding 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-facilitybuilding-03"),
    (4, "FAC-0004", "Enterprise Audited FacilityBuilding 4", 32800.00, 210.0, "ACTIVE", "uuid-facilitybuilding-04"),
    (5, "FAC-0005", "Executive Strategic FacilityBuilding 5", 65000.00, 400.0, "ACTIVE", "uuid-facilitybuilding-05");

CREATE TABLE IF NOT EXISTS facilities_management_officefloorwings (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_officefloorwings_code ON facilities_management_officefloorwings(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_officefloorwings_org_status ON facilities_management_officefloorwings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_officefloorwings_priority ON facilities_management_officefloorwings(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_officefloorwings_created_at ON facilities_management_officefloorwings(created_at);

-- Operational seed data fixtures for facilities_management_officefloorwings
INSERT OR IGNORE INTO facilities_management_officefloorwings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OFF-0001", "Primary Operational OfficeFloorWing 1", 24500.00, 150.0, "ACTIVE", "uuid-officefloorwing-01"),
    (2, "OFF-0002", "Secondary Corporate OfficeFloorWing 2", 18200.50, 80.0, "ACTIVE", "uuid-officefloorwing-02"),
    (3, "OFF-0003", "Consolidated Branch OfficeFloorWing 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-officefloorwing-03"),
    (4, "OFF-0004", "Enterprise Audited OfficeFloorWing 4", 32800.00, 210.0, "ACTIVE", "uuid-officefloorwing-04"),
    (5, "OFF-0005", "Executive Strategic OfficeFloorWing 5", 65000.00, 400.0, "ACTIVE", "uuid-officefloorwing-05");

CREATE TABLE IF NOT EXISTS facilities_management_roomdeskallocations (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_roomdeskallocations_code ON facilities_management_roomdeskallocations(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_roomdeskallocations_org_status ON facilities_management_roomdeskallocations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_roomdeskallocations_priority ON facilities_management_roomdeskallocations(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_roomdeskallocations_created_at ON facilities_management_roomdeskallocations(created_at);

-- Operational seed data fixtures for facilities_management_roomdeskallocations
INSERT OR IGNORE INTO facilities_management_roomdeskallocations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ROO-0001", "Primary Operational RoomDeskAllocation 1", 24500.00, 150.0, "ACTIVE", "uuid-roomdeskallocation-01"),
    (2, "ROO-0002", "Secondary Corporate RoomDeskAllocation 2", 18200.50, 80.0, "ACTIVE", "uuid-roomdeskallocation-02"),
    (3, "ROO-0003", "Consolidated Branch RoomDeskAllocation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-roomdeskallocation-03"),
    (4, "ROO-0004", "Enterprise Audited RoomDeskAllocation 4", 32800.00, 210.0, "ACTIVE", "uuid-roomdeskallocation-04"),
    (5, "ROO-0005", "Executive Strategic RoomDeskAllocation 5", 65000.00, 400.0, "ACTIVE", "uuid-roomdeskallocation-05");

CREATE TABLE IF NOT EXISTS facilities_management_hvaccontrolschedules (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_hvaccontrolschedules_code ON facilities_management_hvaccontrolschedules(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_hvaccontrolschedules_org_status ON facilities_management_hvaccontrolschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_hvaccontrolschedules_priority ON facilities_management_hvaccontrolschedules(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_hvaccontrolschedules_created_at ON facilities_management_hvaccontrolschedules(created_at);

-- Operational seed data fixtures for facilities_management_hvaccontrolschedules
INSERT OR IGNORE INTO facilities_management_hvaccontrolschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HVA-0001", "Primary Operational HVACControlSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-hvaccontrolschedule-01"),
    (2, "HVA-0002", "Secondary Corporate HVACControlSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-hvaccontrolschedule-02"),
    (3, "HVA-0003", "Consolidated Branch HVACControlSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hvaccontrolschedule-03"),
    (4, "HVA-0004", "Enterprise Audited HVACControlSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-hvaccontrolschedule-04"),
    (5, "HVA-0005", "Executive Strategic HVACControlSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-hvaccontrolschedule-05");

CREATE TABLE IF NOT EXISTS facilities_management_physicalbadgeaccesslogs (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_physicalbadgeaccesslogs_code ON facilities_management_physicalbadgeaccesslogs(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_physicalbadgeaccesslogs_org_status ON facilities_management_physicalbadgeaccesslogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_physicalbadgeaccesslogs_priority ON facilities_management_physicalbadgeaccesslogs(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_physicalbadgeaccesslogs_created_at ON facilities_management_physicalbadgeaccesslogs(created_at);

-- Operational seed data fixtures for facilities_management_physicalbadgeaccesslogs
INSERT OR IGNORE INTO facilities_management_physicalbadgeaccesslogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PHY-0001", "Primary Operational PhysicalBadgeAccessLog 1", 24500.00, 150.0, "ACTIVE", "uuid-physicalbadgeaccesslog-01"),
    (2, "PHY-0002", "Secondary Corporate PhysicalBadgeAccessLog 2", 18200.50, 80.0, "ACTIVE", "uuid-physicalbadgeaccesslog-02"),
    (3, "PHY-0003", "Consolidated Branch PhysicalBadgeAccessLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-physicalbadgeaccesslog-03"),
    (4, "PHY-0004", "Enterprise Audited PhysicalBadgeAccessLog 4", 32800.00, 210.0, "ACTIVE", "uuid-physicalbadgeaccesslog-04"),
    (5, "PHY-0005", "Executive Strategic PhysicalBadgeAccessLog 5", 65000.00, 400.0, "ACTIVE", "uuid-physicalbadgeaccesslog-05");

CREATE TABLE IF NOT EXISTS facilities_management_securityvisitorpasss (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_securityvisitorpasss_code ON facilities_management_securityvisitorpasss(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_securityvisitorpasss_org_status ON facilities_management_securityvisitorpasss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_securityvisitorpasss_priority ON facilities_management_securityvisitorpasss(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_securityvisitorpasss_created_at ON facilities_management_securityvisitorpasss(created_at);

-- Operational seed data fixtures for facilities_management_securityvisitorpasss
INSERT OR IGNORE INTO facilities_management_securityvisitorpasss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEC-0001", "Primary Operational SecurityVisitorPass 1", 24500.00, 150.0, "ACTIVE", "uuid-securityvisitorpass-01"),
    (2, "SEC-0002", "Secondary Corporate SecurityVisitorPass 2", 18200.50, 80.0, "ACTIVE", "uuid-securityvisitorpass-02"),
    (3, "SEC-0003", "Consolidated Branch SecurityVisitorPass 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-securityvisitorpass-03"),
    (4, "SEC-0004", "Enterprise Audited SecurityVisitorPass 4", 32800.00, 210.0, "ACTIVE", "uuid-securityvisitorpass-04"),
    (5, "SEC-0005", "Executive Strategic SecurityVisitorPass 5", 65000.00, 400.0, "ACTIVE", "uuid-securityvisitorpass-05");

CREATE TABLE IF NOT EXISTS facilities_management_janitorialtasklogs (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_janitorialtasklogs_code ON facilities_management_janitorialtasklogs(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_janitorialtasklogs_org_status ON facilities_management_janitorialtasklogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_janitorialtasklogs_priority ON facilities_management_janitorialtasklogs(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_janitorialtasklogs_created_at ON facilities_management_janitorialtasklogs(created_at);

-- Operational seed data fixtures for facilities_management_janitorialtasklogs
INSERT OR IGNORE INTO facilities_management_janitorialtasklogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "JAN-0001", "Primary Operational JanitorialTaskLog 1", 24500.00, 150.0, "ACTIVE", "uuid-janitorialtasklog-01"),
    (2, "JAN-0002", "Secondary Corporate JanitorialTaskLog 2", 18200.50, 80.0, "ACTIVE", "uuid-janitorialtasklog-02"),
    (3, "JAN-0003", "Consolidated Branch JanitorialTaskLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-janitorialtasklog-03"),
    (4, "JAN-0004", "Enterprise Audited JanitorialTaskLog 4", 32800.00, 210.0, "ACTIVE", "uuid-janitorialtasklog-04"),
    (5, "JAN-0005", "Executive Strategic JanitorialTaskLog 5", 65000.00, 400.0, "ACTIVE", "uuid-janitorialtasklog-05");

CREATE TABLE IF NOT EXISTS facilities_management_leasespacecontracts (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_leasespacecontracts_code ON facilities_management_leasespacecontracts(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_leasespacecontracts_org_status ON facilities_management_leasespacecontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_leasespacecontracts_priority ON facilities_management_leasespacecontracts(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_leasespacecontracts_created_at ON facilities_management_leasespacecontracts(created_at);

-- Operational seed data fixtures for facilities_management_leasespacecontracts
INSERT OR IGNORE INTO facilities_management_leasespacecontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeaseSpaceContract 1", 24500.00, 150.0, "ACTIVE", "uuid-leasespacecontract-01"),
    (2, "LEA-0002", "Secondary Corporate LeaseSpaceContract 2", 18200.50, 80.0, "ACTIVE", "uuid-leasespacecontract-02"),
    (3, "LEA-0003", "Consolidated Branch LeaseSpaceContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leasespacecontract-03"),
    (4, "LEA-0004", "Enterprise Audited LeaseSpaceContract 4", 32800.00, 210.0, "ACTIVE", "uuid-leasespacecontract-04"),
    (5, "LEA-0005", "Executive Strategic LeaseSpaceContract 5", 65000.00, 400.0, "ACTIVE", "uuid-leasespacecontract-05");

CREATE TABLE IF NOT EXISTS facilities_management_emergencyevacuationplans (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_emergencyevacuationplans_code ON facilities_management_emergencyevacuationplans(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_emergencyevacuationplans_org_status ON facilities_management_emergencyevacuationplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_emergencyevacuationplans_priority ON facilities_management_emergencyevacuationplans(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_emergencyevacuationplans_created_at ON facilities_management_emergencyevacuationplans(created_at);

-- Operational seed data fixtures for facilities_management_emergencyevacuationplans
INSERT OR IGNORE INTO facilities_management_emergencyevacuationplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EME-0001", "Primary Operational EmergencyEvacuationPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-emergencyevacuationplan-01"),
    (2, "EME-0002", "Secondary Corporate EmergencyEvacuationPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-emergencyevacuationplan-02"),
    (3, "EME-0003", "Consolidated Branch EmergencyEvacuationPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-emergencyevacuationplan-03"),
    (4, "EME-0004", "Enterprise Audited EmergencyEvacuationPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-emergencyevacuationplan-04"),
    (5, "EME-0005", "Executive Strategic EmergencyEvacuationPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-emergencyevacuationplan-05");

CREATE TABLE IF NOT EXISTS facilities_management_utilitymeterrecords (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_utilitymeterrecords_code ON facilities_management_utilitymeterrecords(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_utilitymeterrecords_org_status ON facilities_management_utilitymeterrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_utilitymeterrecords_priority ON facilities_management_utilitymeterrecords(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_utilitymeterrecords_created_at ON facilities_management_utilitymeterrecords(created_at);

-- Operational seed data fixtures for facilities_management_utilitymeterrecords
INSERT OR IGNORE INTO facilities_management_utilitymeterrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "UTI-0001", "Primary Operational UtilityMeterRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-utilitymeterrecord-01"),
    (2, "UTI-0002", "Secondary Corporate UtilityMeterRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-utilitymeterrecord-02"),
    (3, "UTI-0003", "Consolidated Branch UtilityMeterRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-utilitymeterrecord-03"),
    (4, "UTI-0004", "Enterprise Audited UtilityMeterRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-utilitymeterrecord-04"),
    (5, "UTI-0005", "Executive Strategic UtilityMeterRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-utilitymeterrecord-05");

CREATE TABLE IF NOT EXISTS facilities_management_parkingslotallocations (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_parkingslotallocations_code ON facilities_management_parkingslotallocations(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_parkingslotallocations_org_status ON facilities_management_parkingslotallocations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_parkingslotallocations_priority ON facilities_management_parkingslotallocations(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_parkingslotallocations_created_at ON facilities_management_parkingslotallocations(created_at);

-- Operational seed data fixtures for facilities_management_parkingslotallocations
INSERT OR IGNORE INTO facilities_management_parkingslotallocations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational ParkingSlotAllocation 1", 24500.00, 150.0, "ACTIVE", "uuid-parkingslotallocation-01"),
    (2, "PAR-0002", "Secondary Corporate ParkingSlotAllocation 2", 18200.50, 80.0, "ACTIVE", "uuid-parkingslotallocation-02"),
    (3, "PAR-0003", "Consolidated Branch ParkingSlotAllocation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-parkingslotallocation-03"),
    (4, "PAR-0004", "Enterprise Audited ParkingSlotAllocation 4", 32800.00, 210.0, "ACTIVE", "uuid-parkingslotallocation-04"),
    (5, "PAR-0005", "Executive Strategic ParkingSlotAllocation 5", 65000.00, 400.0, "ACTIVE", "uuid-parkingslotallocation-05");

CREATE TABLE IF NOT EXISTS facilities_management_assettaglocations (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_assettaglocations_code ON facilities_management_assettaglocations(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_assettaglocations_org_status ON facilities_management_assettaglocations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_assettaglocations_priority ON facilities_management_assettaglocations(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_assettaglocations_created_at ON facilities_management_assettaglocations(created_at);

-- Operational seed data fixtures for facilities_management_assettaglocations
INSERT OR IGNORE INTO facilities_management_assettaglocations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetTagLocation 1", 24500.00, 150.0, "ACTIVE", "uuid-assettaglocation-01"),
    (2, "ASS-0002", "Secondary Corporate AssetTagLocation 2", 18200.50, 80.0, "ACTIVE", "uuid-assettaglocation-02"),
    (3, "ASS-0003", "Consolidated Branch AssetTagLocation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assettaglocation-03"),
    (4, "ASS-0004", "Enterprise Audited AssetTagLocation 4", 32800.00, 210.0, "ACTIVE", "uuid-assettaglocation-04"),
    (5, "ASS-0005", "Executive Strategic AssetTagLocation 5", 65000.00, 400.0, "ACTIVE", "uuid-assettaglocation-05");

CREATE TABLE IF NOT EXISTS facilities_management_incidenthazardnotices (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_incidenthazardnotices_code ON facilities_management_incidenthazardnotices(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_incidenthazardnotices_org_status ON facilities_management_incidenthazardnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_incidenthazardnotices_priority ON facilities_management_incidenthazardnotices(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_incidenthazardnotices_created_at ON facilities_management_incidenthazardnotices(created_at);

-- Operational seed data fixtures for facilities_management_incidenthazardnotices
INSERT OR IGNORE INTO facilities_management_incidenthazardnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INC-0001", "Primary Operational IncidentHazardNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-incidenthazardnotice-01"),
    (2, "INC-0002", "Secondary Corporate IncidentHazardNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-incidenthazardnotice-02"),
    (3, "INC-0003", "Consolidated Branch IncidentHazardNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-incidenthazardnotice-03"),
    (4, "INC-0004", "Enterprise Audited IncidentHazardNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-incidenthazardnotice-04"),
    (5, "INC-0005", "Executive Strategic IncidentHazardNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-incidenthazardnotice-05");

CREATE TABLE IF NOT EXISTS facilities_management_mailroompackagelogs (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_mailroompackagelogs_code ON facilities_management_mailroompackagelogs(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_mailroompackagelogs_org_status ON facilities_management_mailroompackagelogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_mailroompackagelogs_priority ON facilities_management_mailroompackagelogs(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_mailroompackagelogs_created_at ON facilities_management_mailroompackagelogs(created_at);

-- Operational seed data fixtures for facilities_management_mailroompackagelogs
INSERT OR IGNORE INTO facilities_management_mailroompackagelogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAI-0001", "Primary Operational MailroomPackageLog 1", 24500.00, 150.0, "ACTIVE", "uuid-mailroompackagelog-01"),
    (2, "MAI-0002", "Secondary Corporate MailroomPackageLog 2", 18200.50, 80.0, "ACTIVE", "uuid-mailroompackagelog-02"),
    (3, "MAI-0003", "Consolidated Branch MailroomPackageLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-mailroompackagelog-03"),
    (4, "MAI-0004", "Enterprise Audited MailroomPackageLog 4", 32800.00, 210.0, "ACTIVE", "uuid-mailroompackagelog-04"),
    (5, "MAI-0005", "Executive Strategic MailroomPackageLog 5", 65000.00, 400.0, "ACTIVE", "uuid-mailroompackagelog-05");

CREATE TABLE IF NOT EXISTS facilities_management_cateringrequestorders (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_cateringrequestorders_code ON facilities_management_cateringrequestorders(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_cateringrequestorders_org_status ON facilities_management_cateringrequestorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_cateringrequestorders_priority ON facilities_management_cateringrequestorders(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_cateringrequestorders_created_at ON facilities_management_cateringrequestorders(created_at);

-- Operational seed data fixtures for facilities_management_cateringrequestorders
INSERT OR IGNORE INTO facilities_management_cateringrequestorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAT-0001", "Primary Operational CateringRequestOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-cateringrequestorder-01"),
    (2, "CAT-0002", "Secondary Corporate CateringRequestOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-cateringrequestorder-02"),
    (3, "CAT-0003", "Consolidated Branch CateringRequestOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cateringrequestorder-03"),
    (4, "CAT-0004", "Enterprise Audited CateringRequestOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-cateringrequestorder-04"),
    (5, "CAT-0005", "Executive Strategic CateringRequestOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-cateringrequestorder-05");

CREATE TABLE IF NOT EXISTS facilities_management_facilityexpensecharges (
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

CREATE INDEX IF NOT EXISTS idx_facilities_management_facilityexpensecharges_code ON facilities_management_facilityexpensecharges(code);
CREATE INDEX IF NOT EXISTS idx_facilities_management_facilityexpensecharges_org_status ON facilities_management_facilityexpensecharges(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_facilities_management_facilityexpensecharges_priority ON facilities_management_facilityexpensecharges(priority);
CREATE INDEX IF NOT EXISTS idx_facilities_management_facilityexpensecharges_created_at ON facilities_management_facilityexpensecharges(created_at);

-- Operational seed data fixtures for facilities_management_facilityexpensecharges
INSERT OR IGNORE INTO facilities_management_facilityexpensecharges (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FAC-0001", "Primary Operational FacilityExpenseCharge 1", 24500.00, 150.0, "ACTIVE", "uuid-facilityexpensecharge-01"),
    (2, "FAC-0002", "Secondary Corporate FacilityExpenseCharge 2", 18200.50, 80.0, "ACTIVE", "uuid-facilityexpensecharge-02"),
    (3, "FAC-0003", "Consolidated Branch FacilityExpenseCharge 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-facilityexpensecharge-03"),
    (4, "FAC-0004", "Enterprise Audited FacilityExpenseCharge 4", 32800.00, 210.0, "ACTIVE", "uuid-facilityexpensecharge-04"),
    (5, "FAC-0005", "Executive Strategic FacilityExpenseCharge 5", 65000.00, 400.0, "ACTIVE", "uuid-facilityexpensecharge-05");

