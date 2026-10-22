-- SmartERP Enterprise Titan Migration 013: Enterprise Fixed Asset Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS fixed_assets_assetmasters (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetmasters_code ON fixed_assets_assetmasters(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetmasters_org_status ON fixed_assets_assetmasters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetmasters_priority ON fixed_assets_assetmasters(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetmasters_created_at ON fixed_assets_assetmasters(created_at);

-- Operational seed data fixtures for fixed_assets_assetmasters
INSERT OR IGNORE INTO fixed_assets_assetmasters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetMaster 1", 24500.00, 150.0, "ACTIVE", "uuid-assetmaster-01"),
    (2, "ASS-0002", "Secondary Corporate AssetMaster 2", 18200.50, 80.0, "ACTIVE", "uuid-assetmaster-02"),
    (3, "ASS-0003", "Consolidated Branch AssetMaster 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assetmaster-03"),
    (4, "ASS-0004", "Enterprise Audited AssetMaster 4", 32800.00, 210.0, "ACTIVE", "uuid-assetmaster-04"),
    (5, "ASS-0005", "Executive Strategic AssetMaster 5", 65000.00, 400.0, "ACTIVE", "uuid-assetmaster-05");

CREATE TABLE IF NOT EXISTS fixed_assets_assetcategorys (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetcategorys_code ON fixed_assets_assetcategorys(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetcategorys_org_status ON fixed_assets_assetcategorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetcategorys_priority ON fixed_assets_assetcategorys(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetcategorys_created_at ON fixed_assets_assetcategorys(created_at);

-- Operational seed data fixtures for fixed_assets_assetcategorys
INSERT OR IGNORE INTO fixed_assets_assetcategorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetCategory 1", 24500.00, 150.0, "ACTIVE", "uuid-assetcategory-01"),
    (2, "ASS-0002", "Secondary Corporate AssetCategory 2", 18200.50, 80.0, "ACTIVE", "uuid-assetcategory-02"),
    (3, "ASS-0003", "Consolidated Branch AssetCategory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assetcategory-03"),
    (4, "ASS-0004", "Enterprise Audited AssetCategory 4", 32800.00, 210.0, "ACTIVE", "uuid-assetcategory-04"),
    (5, "ASS-0005", "Executive Strategic AssetCategory 5", 65000.00, 400.0, "ACTIVE", "uuid-assetcategory-05");

CREATE TABLE IF NOT EXISTS fixed_assets_depreciationschedules (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationschedules_code ON fixed_assets_depreciationschedules(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationschedules_org_status ON fixed_assets_depreciationschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationschedules_priority ON fixed_assets_depreciationschedules(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationschedules_created_at ON fixed_assets_depreciationschedules(created_at);

-- Operational seed data fixtures for fixed_assets_depreciationschedules
INSERT OR IGNORE INTO fixed_assets_depreciationschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DepreciationSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-depreciationschedule-01"),
    (2, "DEP-0002", "Secondary Corporate DepreciationSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-depreciationschedule-02"),
    (3, "DEP-0003", "Consolidated Branch DepreciationSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-depreciationschedule-03"),
    (4, "DEP-0004", "Enterprise Audited DepreciationSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-depreciationschedule-04"),
    (5, "DEP-0005", "Executive Strategic DepreciationSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-depreciationschedule-05");

CREATE TABLE IF NOT EXISTS fixed_assets_depreciationruns (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationruns_code ON fixed_assets_depreciationruns(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationruns_org_status ON fixed_assets_depreciationruns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationruns_priority ON fixed_assets_depreciationruns(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_depreciationruns_created_at ON fixed_assets_depreciationruns(created_at);

-- Operational seed data fixtures for fixed_assets_depreciationruns
INSERT OR IGNORE INTO fixed_assets_depreciationruns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DepreciationRun 1", 24500.00, 150.0, "ACTIVE", "uuid-depreciationrun-01"),
    (2, "DEP-0002", "Secondary Corporate DepreciationRun 2", 18200.50, 80.0, "ACTIVE", "uuid-depreciationrun-02"),
    (3, "DEP-0003", "Consolidated Branch DepreciationRun 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-depreciationrun-03"),
    (4, "DEP-0004", "Enterprise Audited DepreciationRun 4", 32800.00, 210.0, "ACTIVE", "uuid-depreciationrun-04"),
    (5, "DEP-0005", "Executive Strategic DepreciationRun 5", 65000.00, 400.0, "ACTIVE", "uuid-depreciationrun-05");

CREATE TABLE IF NOT EXISTS fixed_assets_assetrevaluations (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetrevaluations_code ON fixed_assets_assetrevaluations(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetrevaluations_org_status ON fixed_assets_assetrevaluations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetrevaluations_priority ON fixed_assets_assetrevaluations(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetrevaluations_created_at ON fixed_assets_assetrevaluations(created_at);

-- Operational seed data fixtures for fixed_assets_assetrevaluations
INSERT OR IGNORE INTO fixed_assets_assetrevaluations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetRevaluation 1", 24500.00, 150.0, "ACTIVE", "uuid-assetrevaluation-01"),
    (2, "ASS-0002", "Secondary Corporate AssetRevaluation 2", 18200.50, 80.0, "ACTIVE", "uuid-assetrevaluation-02"),
    (3, "ASS-0003", "Consolidated Branch AssetRevaluation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assetrevaluation-03"),
    (4, "ASS-0004", "Enterprise Audited AssetRevaluation 4", 32800.00, 210.0, "ACTIVE", "uuid-assetrevaluation-04"),
    (5, "ASS-0005", "Executive Strategic AssetRevaluation 5", 65000.00, 400.0, "ACTIVE", "uuid-assetrevaluation-05");

CREATE TABLE IF NOT EXISTS fixed_assets_assetimpairments (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetimpairments_code ON fixed_assets_assetimpairments(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetimpairments_org_status ON fixed_assets_assetimpairments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetimpairments_priority ON fixed_assets_assetimpairments(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetimpairments_created_at ON fixed_assets_assetimpairments(created_at);

-- Operational seed data fixtures for fixed_assets_assetimpairments
INSERT OR IGNORE INTO fixed_assets_assetimpairments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetImpairment 1", 24500.00, 150.0, "ACTIVE", "uuid-assetimpairment-01"),
    (2, "ASS-0002", "Secondary Corporate AssetImpairment 2", 18200.50, 80.0, "ACTIVE", "uuid-assetimpairment-02"),
    (3, "ASS-0003", "Consolidated Branch AssetImpairment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assetimpairment-03"),
    (4, "ASS-0004", "Enterprise Audited AssetImpairment 4", 32800.00, 210.0, "ACTIVE", "uuid-assetimpairment-04"),
    (5, "ASS-0005", "Executive Strategic AssetImpairment 5", 65000.00, 400.0, "ACTIVE", "uuid-assetimpairment-05");

CREATE TABLE IF NOT EXISTS fixed_assets_maintenanceschedules (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_maintenanceschedules_code ON fixed_assets_maintenanceschedules(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_maintenanceschedules_org_status ON fixed_assets_maintenanceschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_maintenanceschedules_priority ON fixed_assets_maintenanceschedules(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_maintenanceschedules_created_at ON fixed_assets_maintenanceschedules(created_at);

-- Operational seed data fixtures for fixed_assets_maintenanceschedules
INSERT OR IGNORE INTO fixed_assets_maintenanceschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAI-0001", "Primary Operational MaintenanceSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-maintenanceschedule-01"),
    (2, "MAI-0002", "Secondary Corporate MaintenanceSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-maintenanceschedule-02"),
    (3, "MAI-0003", "Consolidated Branch MaintenanceSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-maintenanceschedule-03"),
    (4, "MAI-0004", "Enterprise Audited MaintenanceSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-maintenanceschedule-04"),
    (5, "MAI-0005", "Executive Strategic MaintenanceSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-maintenanceschedule-05");

CREATE TABLE IF NOT EXISTS fixed_assets_workorderassets (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_workorderassets_code ON fixed_assets_workorderassets(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_workorderassets_org_status ON fixed_assets_workorderassets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_workorderassets_priority ON fixed_assets_workorderassets(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_workorderassets_created_at ON fixed_assets_workorderassets(created_at);

-- Operational seed data fixtures for fixed_assets_workorderassets
INSERT OR IGNORE INTO fixed_assets_workorderassets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WOR-0001", "Primary Operational WorkOrderAsset 1", 24500.00, 150.0, "ACTIVE", "uuid-workorderasset-01"),
    (2, "WOR-0002", "Secondary Corporate WorkOrderAsset 2", 18200.50, 80.0, "ACTIVE", "uuid-workorderasset-02"),
    (3, "WOR-0003", "Consolidated Branch WorkOrderAsset 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-workorderasset-03"),
    (4, "WOR-0004", "Enterprise Audited WorkOrderAsset 4", 32800.00, 210.0, "ACTIVE", "uuid-workorderasset-04"),
    (5, "WOR-0005", "Executive Strategic WorkOrderAsset 5", 65000.00, 400.0, "ACTIVE", "uuid-workorderasset-05");

CREATE TABLE IF NOT EXISTS fixed_assets_assetdisposals (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetdisposals_code ON fixed_assets_assetdisposals(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetdisposals_org_status ON fixed_assets_assetdisposals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetdisposals_priority ON fixed_assets_assetdisposals(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assetdisposals_created_at ON fixed_assets_assetdisposals(created_at);

-- Operational seed data fixtures for fixed_assets_assetdisposals
INSERT OR IGNORE INTO fixed_assets_assetdisposals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetDisposal 1", 24500.00, 150.0, "ACTIVE", "uuid-assetdisposal-01"),
    (2, "ASS-0002", "Secondary Corporate AssetDisposal 2", 18200.50, 80.0, "ACTIVE", "uuid-assetdisposal-02"),
    (3, "ASS-0003", "Consolidated Branch AssetDisposal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assetdisposal-03"),
    (4, "ASS-0004", "Enterprise Audited AssetDisposal 4", 32800.00, 210.0, "ACTIVE", "uuid-assetdisposal-04"),
    (5, "ASS-0005", "Executive Strategic AssetDisposal 5", 65000.00, 400.0, "ACTIVE", "uuid-assetdisposal-05");

CREATE TABLE IF NOT EXISTS fixed_assets_assettransferlogs (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_assettransferlogs_code ON fixed_assets_assettransferlogs(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assettransferlogs_org_status ON fixed_assets_assettransferlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assettransferlogs_priority ON fixed_assets_assettransferlogs(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_assettransferlogs_created_at ON fixed_assets_assettransferlogs(created_at);

-- Operational seed data fixtures for fixed_assets_assettransferlogs
INSERT OR IGNORE INTO fixed_assets_assettransferlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetTransferLog 1", 24500.00, 150.0, "ACTIVE", "uuid-assettransferlog-01"),
    (2, "ASS-0002", "Secondary Corporate AssetTransferLog 2", 18200.50, 80.0, "ACTIVE", "uuid-assettransferlog-02"),
    (3, "ASS-0003", "Consolidated Branch AssetTransferLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assettransferlog-03"),
    (4, "ASS-0004", "Enterprise Audited AssetTransferLog 4", 32800.00, 210.0, "ACTIVE", "uuid-assettransferlog-04"),
    (5, "ASS-0005", "Executive Strategic AssetTransferLog 5", 65000.00, 400.0, "ACTIVE", "uuid-assettransferlog-05");

CREATE TABLE IF NOT EXISTS fixed_assets_physicalverifications (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_physicalverifications_code ON fixed_assets_physicalverifications(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_physicalverifications_org_status ON fixed_assets_physicalverifications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_physicalverifications_priority ON fixed_assets_physicalverifications(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_physicalverifications_created_at ON fixed_assets_physicalverifications(created_at);

-- Operational seed data fixtures for fixed_assets_physicalverifications
INSERT OR IGNORE INTO fixed_assets_physicalverifications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PHY-0001", "Primary Operational PhysicalVerification 1", 24500.00, 150.0, "ACTIVE", "uuid-physicalverification-01"),
    (2, "PHY-0002", "Secondary Corporate PhysicalVerification 2", 18200.50, 80.0, "ACTIVE", "uuid-physicalverification-02"),
    (3, "PHY-0003", "Consolidated Branch PhysicalVerification 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-physicalverification-03"),
    (4, "PHY-0004", "Enterprise Audited PhysicalVerification 4", 32800.00, 210.0, "ACTIVE", "uuid-physicalverification-04"),
    (5, "PHY-0005", "Executive Strategic PhysicalVerification 5", 65000.00, 400.0, "ACTIVE", "uuid-physicalverification-05");

CREATE TABLE IF NOT EXISTS fixed_assets_warrantyagreements (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_warrantyagreements_code ON fixed_assets_warrantyagreements(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_warrantyagreements_org_status ON fixed_assets_warrantyagreements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_warrantyagreements_priority ON fixed_assets_warrantyagreements(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_warrantyagreements_created_at ON fixed_assets_warrantyagreements(created_at);

-- Operational seed data fixtures for fixed_assets_warrantyagreements
INSERT OR IGNORE INTO fixed_assets_warrantyagreements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAR-0001", "Primary Operational WarrantyAgreement 1", 24500.00, 150.0, "ACTIVE", "uuid-warrantyagreement-01"),
    (2, "WAR-0002", "Secondary Corporate WarrantyAgreement 2", 18200.50, 80.0, "ACTIVE", "uuid-warrantyagreement-02"),
    (3, "WAR-0003", "Consolidated Branch WarrantyAgreement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-warrantyagreement-03"),
    (4, "WAR-0004", "Enterprise Audited WarrantyAgreement 4", 32800.00, 210.0, "ACTIVE", "uuid-warrantyagreement-04"),
    (5, "WAR-0005", "Executive Strategic WarrantyAgreement 5", 65000.00, 400.0, "ACTIVE", "uuid-warrantyagreement-05");

CREATE TABLE IF NOT EXISTS fixed_assets_insurancepolicys (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_insurancepolicys_code ON fixed_assets_insurancepolicys(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_insurancepolicys_org_status ON fixed_assets_insurancepolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_insurancepolicys_priority ON fixed_assets_insurancepolicys(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_insurancepolicys_created_at ON fixed_assets_insurancepolicys(created_at);

-- Operational seed data fixtures for fixed_assets_insurancepolicys
INSERT OR IGNORE INTO fixed_assets_insurancepolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INS-0001", "Primary Operational InsurancePolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-insurancepolicy-01"),
    (2, "INS-0002", "Secondary Corporate InsurancePolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-insurancepolicy-02"),
    (3, "INS-0003", "Consolidated Branch InsurancePolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-insurancepolicy-03"),
    (4, "INS-0004", "Enterprise Audited InsurancePolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-insurancepolicy-04"),
    (5, "INS-0005", "Executive Strategic InsurancePolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-insurancepolicy-05");

CREATE TABLE IF NOT EXISTS fixed_assets_leaseschedules (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_leaseschedules_code ON fixed_assets_leaseschedules(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_leaseschedules_org_status ON fixed_assets_leaseschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_leaseschedules_priority ON fixed_assets_leaseschedules(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_leaseschedules_created_at ON fixed_assets_leaseschedules(created_at);

-- Operational seed data fixtures for fixed_assets_leaseschedules
INSERT OR IGNORE INTO fixed_assets_leaseschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeaseSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-leaseschedule-01"),
    (2, "LEA-0002", "Secondary Corporate LeaseSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-leaseschedule-02"),
    (3, "LEA-0003", "Consolidated Branch LeaseSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leaseschedule-03"),
    (4, "LEA-0004", "Enterprise Audited LeaseSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-leaseschedule-04"),
    (5, "LEA-0005", "Executive Strategic LeaseSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-leaseschedule-05");

CREATE TABLE IF NOT EXISTS fixed_assets_componentassets (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_componentassets_code ON fixed_assets_componentassets(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_componentassets_org_status ON fixed_assets_componentassets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_componentassets_priority ON fixed_assets_componentassets(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_componentassets_created_at ON fixed_assets_componentassets(created_at);

-- Operational seed data fixtures for fixed_assets_componentassets
INSERT OR IGNORE INTO fixed_assets_componentassets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational ComponentAsset 1", 24500.00, 150.0, "ACTIVE", "uuid-componentasset-01"),
    (2, "COM-0002", "Secondary Corporate ComponentAsset 2", 18200.50, 80.0, "ACTIVE", "uuid-componentasset-02"),
    (3, "COM-0003", "Consolidated Branch ComponentAsset 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-componentasset-03"),
    (4, "COM-0004", "Enterprise Audited ComponentAsset 4", 32800.00, 210.0, "ACTIVE", "uuid-componentasset-04"),
    (5, "COM-0005", "Executive Strategic ComponentAsset 5", 65000.00, 400.0, "ACTIVE", "uuid-componentasset-05");

CREATE TABLE IF NOT EXISTS fixed_assets_disposalproceedss (
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

CREATE INDEX IF NOT EXISTS idx_fixed_assets_disposalproceedss_code ON fixed_assets_disposalproceedss(code);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_disposalproceedss_org_status ON fixed_assets_disposalproceedss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_disposalproceedss_priority ON fixed_assets_disposalproceedss(priority);
CREATE INDEX IF NOT EXISTS idx_fixed_assets_disposalproceedss_created_at ON fixed_assets_disposalproceedss(created_at);

-- Operational seed data fixtures for fixed_assets_disposalproceedss
INSERT OR IGNORE INTO fixed_assets_disposalproceedss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DisposalProceeds 1", 24500.00, 150.0, "ACTIVE", "uuid-disposalproceeds-01"),
    (2, "DIS-0002", "Secondary Corporate DisposalProceeds 2", 18200.50, 80.0, "ACTIVE", "uuid-disposalproceeds-02"),
    (3, "DIS-0003", "Consolidated Branch DisposalProceeds 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-disposalproceeds-03"),
    (4, "DIS-0004", "Enterprise Audited DisposalProceeds 4", 32800.00, 210.0, "ACTIVE", "uuid-disposalproceeds-04"),
    (5, "DIS-0005", "Executive Strategic DisposalProceeds 5", 65000.00, 400.0, "ACTIVE", "uuid-disposalproceeds-05");

