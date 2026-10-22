-- SmartERP Enterprise Titan Migration 002: Manufacturing Resource Planning (MRP II) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS manufacturing_workorders (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_workorders_code ON manufacturing_workorders(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_workorders_org_status ON manufacturing_workorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_workorders_priority ON manufacturing_workorders(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_workorders_created_at ON manufacturing_workorders(created_at);

-- Operational seed data fixtures for manufacturing_workorders
INSERT OR IGNORE INTO manufacturing_workorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WOR-0001", "Primary Operational WorkOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-workorder-01"),
    (2, "WOR-0002", "Secondary Corporate WorkOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-workorder-02"),
    (3, "WOR-0003", "Consolidated Branch WorkOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-workorder-03"),
    (4, "WOR-0004", "Enterprise Audited WorkOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-workorder-04"),
    (5, "WOR-0005", "Executive Strategic WorkOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-workorder-05");

CREATE TABLE IF NOT EXISTS manufacturing_billofmaterials (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_billofmaterials_code ON manufacturing_billofmaterials(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_billofmaterials_org_status ON manufacturing_billofmaterials(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_billofmaterials_priority ON manufacturing_billofmaterials(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_billofmaterials_created_at ON manufacturing_billofmaterials(created_at);

-- Operational seed data fixtures for manufacturing_billofmaterials
INSERT OR IGNORE INTO manufacturing_billofmaterials (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BIL-0001", "Primary Operational BillOfMaterial 1", 24500.00, 150.0, "ACTIVE", "uuid-billofmaterial-01"),
    (2, "BIL-0002", "Secondary Corporate BillOfMaterial 2", 18200.50, 80.0, "ACTIVE", "uuid-billofmaterial-02"),
    (3, "BIL-0003", "Consolidated Branch BillOfMaterial 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-billofmaterial-03"),
    (4, "BIL-0004", "Enterprise Audited BillOfMaterial 4", 32800.00, 210.0, "ACTIVE", "uuid-billofmaterial-04"),
    (5, "BIL-0005", "Executive Strategic BillOfMaterial 5", 65000.00, 400.0, "ACTIVE", "uuid-billofmaterial-05");

CREATE TABLE IF NOT EXISTS manufacturing_operations (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_operations_code ON manufacturing_operations(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_operations_org_status ON manufacturing_operations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_operations_priority ON manufacturing_operations(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_operations_created_at ON manufacturing_operations(created_at);

-- Operational seed data fixtures for manufacturing_operations
INSERT OR IGNORE INTO manufacturing_operations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OPE-0001", "Primary Operational Operation 1", 24500.00, 150.0, "ACTIVE", "uuid-operation-01"),
    (2, "OPE-0002", "Secondary Corporate Operation 2", 18200.50, 80.0, "ACTIVE", "uuid-operation-02"),
    (3, "OPE-0003", "Consolidated Branch Operation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-operation-03"),
    (4, "OPE-0004", "Enterprise Audited Operation 4", 32800.00, 210.0, "ACTIVE", "uuid-operation-04"),
    (5, "OPE-0005", "Executive Strategic Operation 5", 65000.00, 400.0, "ACTIVE", "uuid-operation-05");

CREATE TABLE IF NOT EXISTS manufacturing_workcenters (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_workcenters_code ON manufacturing_workcenters(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_workcenters_org_status ON manufacturing_workcenters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_workcenters_priority ON manufacturing_workcenters(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_workcenters_created_at ON manufacturing_workcenters(created_at);

-- Operational seed data fixtures for manufacturing_workcenters
INSERT OR IGNORE INTO manufacturing_workcenters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WOR-0001", "Primary Operational WorkCenter 1", 24500.00, 150.0, "ACTIVE", "uuid-workcenter-01"),
    (2, "WOR-0002", "Secondary Corporate WorkCenter 2", 18200.50, 80.0, "ACTIVE", "uuid-workcenter-02"),
    (3, "WOR-0003", "Consolidated Branch WorkCenter 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-workcenter-03"),
    (4, "WOR-0004", "Enterprise Audited WorkCenter 4", 32800.00, 210.0, "ACTIVE", "uuid-workcenter-04"),
    (5, "WOR-0005", "Executive Strategic WorkCenter 5", 65000.00, 400.0, "ACTIVE", "uuid-workcenter-05");

CREATE TABLE IF NOT EXISTS manufacturing_routings (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_routings_code ON manufacturing_routings(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_routings_org_status ON manufacturing_routings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_routings_priority ON manufacturing_routings(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_routings_created_at ON manufacturing_routings(created_at);

-- Operational seed data fixtures for manufacturing_routings
INSERT OR IGNORE INTO manufacturing_routings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ROU-0001", "Primary Operational Routing 1", 24500.00, 150.0, "ACTIVE", "uuid-routing-01"),
    (2, "ROU-0002", "Secondary Corporate Routing 2", 18200.50, 80.0, "ACTIVE", "uuid-routing-02"),
    (3, "ROU-0003", "Consolidated Branch Routing 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-routing-03"),
    (4, "ROU-0004", "Enterprise Audited Routing 4", 32800.00, 210.0, "ACTIVE", "uuid-routing-04"),
    (5, "ROU-0005", "Executive Strategic Routing 5", 65000.00, 400.0, "ACTIVE", "uuid-routing-05");

CREATE TABLE IF NOT EXISTS manufacturing_productionschedules (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_productionschedules_code ON manufacturing_productionschedules(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_productionschedules_org_status ON manufacturing_productionschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_productionschedules_priority ON manufacturing_productionschedules(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_productionschedules_created_at ON manufacturing_productionschedules(created_at);

-- Operational seed data fixtures for manufacturing_productionschedules
INSERT OR IGNORE INTO manufacturing_productionschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProductionSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-productionschedule-01"),
    (2, "PRO-0002", "Secondary Corporate ProductionSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-productionschedule-02"),
    (3, "PRO-0003", "Consolidated Branch ProductionSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-productionschedule-03"),
    (4, "PRO-0004", "Enterprise Audited ProductionSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-productionschedule-04"),
    (5, "PRO-0005", "Executive Strategic ProductionSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-productionschedule-05");

CREATE TABLE IF NOT EXISTS manufacturing_scraprecords (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_scraprecords_code ON manufacturing_scraprecords(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_scraprecords_org_status ON manufacturing_scraprecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_scraprecords_priority ON manufacturing_scraprecords(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_scraprecords_created_at ON manufacturing_scraprecords(created_at);

-- Operational seed data fixtures for manufacturing_scraprecords
INSERT OR IGNORE INTO manufacturing_scraprecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SCR-0001", "Primary Operational ScrapRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-scraprecord-01"),
    (2, "SCR-0002", "Secondary Corporate ScrapRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-scraprecord-02"),
    (3, "SCR-0003", "Consolidated Branch ScrapRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-scraprecord-03"),
    (4, "SCR-0004", "Enterprise Audited ScrapRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-scraprecord-04"),
    (5, "SCR-0005", "Executive Strategic ScrapRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-scraprecord-05");

CREATE TABLE IF NOT EXISTS manufacturing_qualitychecks (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_qualitychecks_code ON manufacturing_qualitychecks(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_qualitychecks_org_status ON manufacturing_qualitychecks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_qualitychecks_priority ON manufacturing_qualitychecks(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_qualitychecks_created_at ON manufacturing_qualitychecks(created_at);

-- Operational seed data fixtures for manufacturing_qualitychecks
INSERT OR IGNORE INTO manufacturing_qualitychecks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "QUA-0001", "Primary Operational QualityCheck 1", 24500.00, 150.0, "ACTIVE", "uuid-qualitycheck-01"),
    (2, "QUA-0002", "Secondary Corporate QualityCheck 2", 18200.50, 80.0, "ACTIVE", "uuid-qualitycheck-02"),
    (3, "QUA-0003", "Consolidated Branch QualityCheck 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-qualitycheck-03"),
    (4, "QUA-0004", "Enterprise Audited QualityCheck 4", 32800.00, 210.0, "ACTIVE", "uuid-qualitycheck-04"),
    (5, "QUA-0005", "Executive Strategic QualityCheck 5", 65000.00, 400.0, "ACTIVE", "uuid-qualitycheck-05");

CREATE TABLE IF NOT EXISTS manufacturing_machinedowntimes (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_machinedowntimes_code ON manufacturing_machinedowntimes(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_machinedowntimes_org_status ON manufacturing_machinedowntimes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_machinedowntimes_priority ON manufacturing_machinedowntimes(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_machinedowntimes_created_at ON manufacturing_machinedowntimes(created_at);

-- Operational seed data fixtures for manufacturing_machinedowntimes
INSERT OR IGNORE INTO manufacturing_machinedowntimes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAC-0001", "Primary Operational MachineDowntime 1", 24500.00, 150.0, "ACTIVE", "uuid-machinedowntime-01"),
    (2, "MAC-0002", "Secondary Corporate MachineDowntime 2", 18200.50, 80.0, "ACTIVE", "uuid-machinedowntime-02"),
    (3, "MAC-0003", "Consolidated Branch MachineDowntime 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-machinedowntime-03"),
    (4, "MAC-0004", "Enterprise Audited MachineDowntime 4", 32800.00, 210.0, "ACTIVE", "uuid-machinedowntime-04"),
    (5, "MAC-0005", "Executive Strategic MachineDowntime 5", 65000.00, 400.0, "ACTIVE", "uuid-machinedowntime-05");

CREATE TABLE IF NOT EXISTS manufacturing_toolingassets (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_toolingassets_code ON manufacturing_toolingassets(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_toolingassets_org_status ON manufacturing_toolingassets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_toolingassets_priority ON manufacturing_toolingassets(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_toolingassets_created_at ON manufacturing_toolingassets(created_at);

-- Operational seed data fixtures for manufacturing_toolingassets
INSERT OR IGNORE INTO manufacturing_toolingassets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TOO-0001", "Primary Operational ToolingAsset 1", 24500.00, 150.0, "ACTIVE", "uuid-toolingasset-01"),
    (2, "TOO-0002", "Secondary Corporate ToolingAsset 2", 18200.50, 80.0, "ACTIVE", "uuid-toolingasset-02"),
    (3, "TOO-0003", "Consolidated Branch ToolingAsset 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-toolingasset-03"),
    (4, "TOO-0004", "Enterprise Audited ToolingAsset 4", 32800.00, 210.0, "ACTIVE", "uuid-toolingasset-04"),
    (5, "TOO-0005", "Executive Strategic ToolingAsset 5", 65000.00, 400.0, "ACTIVE", "uuid-toolingasset-05");

CREATE TABLE IF NOT EXISTS manufacturing_materialrequisitions (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_materialrequisitions_code ON manufacturing_materialrequisitions(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_materialrequisitions_org_status ON manufacturing_materialrequisitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_materialrequisitions_priority ON manufacturing_materialrequisitions(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_materialrequisitions_created_at ON manufacturing_materialrequisitions(created_at);

-- Operational seed data fixtures for manufacturing_materialrequisitions
INSERT OR IGNORE INTO manufacturing_materialrequisitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAT-0001", "Primary Operational MaterialRequisition 1", 24500.00, 150.0, "ACTIVE", "uuid-materialrequisition-01"),
    (2, "MAT-0002", "Secondary Corporate MaterialRequisition 2", 18200.50, 80.0, "ACTIVE", "uuid-materialrequisition-02"),
    (3, "MAT-0003", "Consolidated Branch MaterialRequisition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-materialrequisition-03"),
    (4, "MAT-0004", "Enterprise Audited MaterialRequisition 4", 32800.00, 210.0, "ACTIVE", "uuid-materialrequisition-04"),
    (5, "MAT-0005", "Executive Strategic MaterialRequisition 5", 65000.00, 400.0, "ACTIVE", "uuid-materialrequisition-05");

CREATE TABLE IF NOT EXISTS manufacturing_ecos (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_ecos_code ON manufacturing_ecos(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_ecos_org_status ON manufacturing_ecos(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_ecos_priority ON manufacturing_ecos(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_ecos_created_at ON manufacturing_ecos(created_at);

-- Operational seed data fixtures for manufacturing_ecos
INSERT OR IGNORE INTO manufacturing_ecos (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ECO-0001", "Primary Operational ECO 1", 24500.00, 150.0, "ACTIVE", "uuid-eco-01"),
    (2, "ECO-0002", "Secondary Corporate ECO 2", 18200.50, 80.0, "ACTIVE", "uuid-eco-02"),
    (3, "ECO-0003", "Consolidated Branch ECO 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-eco-03"),
    (4, "ECO-0004", "Enterprise Audited ECO 4", 32800.00, 210.0, "ACTIVE", "uuid-eco-04"),
    (5, "ECO-0005", "Executive Strategic ECO 5", 65000.00, 400.0, "ACTIVE", "uuid-eco-05");

CREATE TABLE IF NOT EXISTS manufacturing_standardcosts (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_standardcosts_code ON manufacturing_standardcosts(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_standardcosts_org_status ON manufacturing_standardcosts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_standardcosts_priority ON manufacturing_standardcosts(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_standardcosts_created_at ON manufacturing_standardcosts(created_at);

-- Operational seed data fixtures for manufacturing_standardcosts
INSERT OR IGNORE INTO manufacturing_standardcosts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StandardCost 1", 24500.00, 150.0, "ACTIVE", "uuid-standardcost-01"),
    (2, "STA-0002", "Secondary Corporate StandardCost 2", 18200.50, 80.0, "ACTIVE", "uuid-standardcost-02"),
    (3, "STA-0003", "Consolidated Branch StandardCost 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-standardcost-03"),
    (4, "STA-0004", "Enterprise Audited StandardCost 4", 32800.00, 210.0, "ACTIVE", "uuid-standardcost-04"),
    (5, "STA-0005", "Executive Strategic StandardCost 5", 65000.00, 400.0, "ACTIVE", "uuid-standardcost-05");

CREATE TABLE IF NOT EXISTS manufacturing_assemblylines (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_assemblylines_code ON manufacturing_assemblylines(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_assemblylines_org_status ON manufacturing_assemblylines(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_assemblylines_priority ON manufacturing_assemblylines(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_assemblylines_created_at ON manufacturing_assemblylines(created_at);

-- Operational seed data fixtures for manufacturing_assemblylines
INSERT OR IGNORE INTO manufacturing_assemblylines (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssemblyLine 1", 24500.00, 150.0, "ACTIVE", "uuid-assemblyline-01"),
    (2, "ASS-0002", "Secondary Corporate AssemblyLine 2", 18200.50, 80.0, "ACTIVE", "uuid-assemblyline-02"),
    (3, "ASS-0003", "Consolidated Branch AssemblyLine 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assemblyline-03"),
    (4, "ASS-0004", "Enterprise Audited AssemblyLine 4", 32800.00, 210.0, "ACTIVE", "uuid-assemblyline-04"),
    (5, "ASS-0005", "Executive Strategic AssemblyLine 5", 65000.00, 400.0, "ACTIVE", "uuid-assemblyline-05");

CREATE TABLE IF NOT EXISTS manufacturing_shiftoutputs (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_shiftoutputs_code ON manufacturing_shiftoutputs(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_shiftoutputs_org_status ON manufacturing_shiftoutputs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_shiftoutputs_priority ON manufacturing_shiftoutputs(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_shiftoutputs_created_at ON manufacturing_shiftoutputs(created_at);

-- Operational seed data fixtures for manufacturing_shiftoutputs
INSERT OR IGNORE INTO manufacturing_shiftoutputs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational ShiftOutput 1", 24500.00, 150.0, "ACTIVE", "uuid-shiftoutput-01"),
    (2, "SHI-0002", "Secondary Corporate ShiftOutput 2", 18200.50, 80.0, "ACTIVE", "uuid-shiftoutput-02"),
    (3, "SHI-0003", "Consolidated Branch ShiftOutput 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shiftoutput-03"),
    (4, "SHI-0004", "Enterprise Audited ShiftOutput 4", 32800.00, 210.0, "ACTIVE", "uuid-shiftoutput-04"),
    (5, "SHI-0005", "Executive Strategic ShiftOutput 5", 65000.00, 400.0, "ACTIVE", "uuid-shiftoutput-05");

CREATE TABLE IF NOT EXISTS manufacturing_wipstocks (
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

CREATE INDEX IF NOT EXISTS idx_manufacturing_wipstocks_code ON manufacturing_wipstocks(code);
CREATE INDEX IF NOT EXISTS idx_manufacturing_wipstocks_org_status ON manufacturing_wipstocks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_manufacturing_wipstocks_priority ON manufacturing_wipstocks(priority);
CREATE INDEX IF NOT EXISTS idx_manufacturing_wipstocks_created_at ON manufacturing_wipstocks(created_at);

-- Operational seed data fixtures for manufacturing_wipstocks
INSERT OR IGNORE INTO manufacturing_wipstocks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WIP-0001", "Primary Operational WIPStock 1", 24500.00, 150.0, "ACTIVE", "uuid-wipstock-01"),
    (2, "WIP-0002", "Secondary Corporate WIPStock 2", 18200.50, 80.0, "ACTIVE", "uuid-wipstock-02"),
    (3, "WIP-0003", "Consolidated Branch WIPStock 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-wipstock-03"),
    (4, "WIP-0004", "Enterprise Audited WIPStock 4", 32800.00, 210.0, "ACTIVE", "uuid-wipstock-04"),
    (5, "WIP-0005", "Executive Strategic WIPStock 5", 65000.00, 400.0, "ACTIVE", "uuid-wipstock-05");

