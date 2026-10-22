-- SmartERP Enterprise Titan Migration 026: Industrial Plant & CMMS Asset Maintenance DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS asset_maintenance_maintenanceworkorders (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenanceworkorders_code ON asset_maintenance_maintenanceworkorders(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenanceworkorders_org_status ON asset_maintenance_maintenanceworkorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenanceworkorders_priority ON asset_maintenance_maintenanceworkorders(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenanceworkorders_created_at ON asset_maintenance_maintenanceworkorders(created_at);

-- Operational seed data fixtures for asset_maintenance_maintenanceworkorders
INSERT OR IGNORE INTO asset_maintenance_maintenanceworkorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAI-0001", "Primary Operational MaintenanceWorkOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-maintenanceworkorder-01"),
    (2, "MAI-0002", "Secondary Corporate MaintenanceWorkOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-maintenanceworkorder-02"),
    (3, "MAI-0003", "Consolidated Branch MaintenanceWorkOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-maintenanceworkorder-03"),
    (4, "MAI-0004", "Enterprise Audited MaintenanceWorkOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-maintenanceworkorder-04"),
    (5, "MAI-0005", "Executive Strategic MaintenanceWorkOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-maintenanceworkorder-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_preventiveplans (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_preventiveplans_code ON asset_maintenance_preventiveplans(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_preventiveplans_org_status ON asset_maintenance_preventiveplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_preventiveplans_priority ON asset_maintenance_preventiveplans(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_preventiveplans_created_at ON asset_maintenance_preventiveplans(created_at);

-- Operational seed data fixtures for asset_maintenance_preventiveplans
INSERT OR IGNORE INTO asset_maintenance_preventiveplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRE-0001", "Primary Operational PreventivePlan 1", 24500.00, 150.0, "ACTIVE", "uuid-preventiveplan-01"),
    (2, "PRE-0002", "Secondary Corporate PreventivePlan 2", 18200.50, 80.0, "ACTIVE", "uuid-preventiveplan-02"),
    (3, "PRE-0003", "Consolidated Branch PreventivePlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-preventiveplan-03"),
    (4, "PRE-0004", "Enterprise Audited PreventivePlan 4", 32800.00, 210.0, "ACTIVE", "uuid-preventiveplan-04"),
    (5, "PRE-0005", "Executive Strategic PreventivePlan 5", 65000.00, 400.0, "ACTIVE", "uuid-preventiveplan-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_assetmeterreadings (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_assetmeterreadings_code ON asset_maintenance_assetmeterreadings(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_assetmeterreadings_org_status ON asset_maintenance_assetmeterreadings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_assetmeterreadings_priority ON asset_maintenance_assetmeterreadings(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_assetmeterreadings_created_at ON asset_maintenance_assetmeterreadings(created_at);

-- Operational seed data fixtures for asset_maintenance_assetmeterreadings
INSERT OR IGNORE INTO asset_maintenance_assetmeterreadings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ASS-0001", "Primary Operational AssetMeterReading 1", 24500.00, 150.0, "ACTIVE", "uuid-assetmeterreading-01"),
    (2, "ASS-0002", "Secondary Corporate AssetMeterReading 2", 18200.50, 80.0, "ACTIVE", "uuid-assetmeterreading-02"),
    (3, "ASS-0003", "Consolidated Branch AssetMeterReading 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-assetmeterreading-03"),
    (4, "ASS-0004", "Enterprise Audited AssetMeterReading 4", 32800.00, 210.0, "ACTIVE", "uuid-assetmeterreading-04"),
    (5, "ASS-0005", "Executive Strategic AssetMeterReading 5", 65000.00, 400.0, "ACTIVE", "uuid-assetmeterreading-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_equipmentfailurelogs (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentfailurelogs_code ON asset_maintenance_equipmentfailurelogs(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentfailurelogs_org_status ON asset_maintenance_equipmentfailurelogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentfailurelogs_priority ON asset_maintenance_equipmentfailurelogs(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentfailurelogs_created_at ON asset_maintenance_equipmentfailurelogs(created_at);

-- Operational seed data fixtures for asset_maintenance_equipmentfailurelogs
INSERT OR IGNORE INTO asset_maintenance_equipmentfailurelogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EQU-0001", "Primary Operational EquipmentFailureLog 1", 24500.00, 150.0, "ACTIVE", "uuid-equipmentfailurelog-01"),
    (2, "EQU-0002", "Secondary Corporate EquipmentFailureLog 2", 18200.50, 80.0, "ACTIVE", "uuid-equipmentfailurelog-02"),
    (3, "EQU-0003", "Consolidated Branch EquipmentFailureLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-equipmentfailurelog-03"),
    (4, "EQU-0004", "Enterprise Audited EquipmentFailureLog 4", 32800.00, 210.0, "ACTIVE", "uuid-equipmentfailurelog-04"),
    (5, "EQU-0005", "Executive Strategic EquipmentFailureLog 5", 65000.00, 400.0, "ACTIVE", "uuid-equipmentfailurelog-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_sparepartinventorys (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_sparepartinventorys_code ON asset_maintenance_sparepartinventorys(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_sparepartinventorys_org_status ON asset_maintenance_sparepartinventorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_sparepartinventorys_priority ON asset_maintenance_sparepartinventorys(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_sparepartinventorys_created_at ON asset_maintenance_sparepartinventorys(created_at);

-- Operational seed data fixtures for asset_maintenance_sparepartinventorys
INSERT OR IGNORE INTO asset_maintenance_sparepartinventorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SPA-0001", "Primary Operational SparePartInventory 1", 24500.00, 150.0, "ACTIVE", "uuid-sparepartinventory-01"),
    (2, "SPA-0002", "Secondary Corporate SparePartInventory 2", 18200.50, 80.0, "ACTIVE", "uuid-sparepartinventory-02"),
    (3, "SPA-0003", "Consolidated Branch SparePartInventory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sparepartinventory-03"),
    (4, "SPA-0004", "Enterprise Audited SparePartInventory 4", 32800.00, 210.0, "ACTIVE", "uuid-sparepartinventory-04"),
    (5, "SPA-0005", "Executive Strategic SparePartInventory 5", 65000.00, 400.0, "ACTIVE", "uuid-sparepartinventory-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_maintenancetechnicians (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancetechnicians_code ON asset_maintenance_maintenancetechnicians(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancetechnicians_org_status ON asset_maintenance_maintenancetechnicians(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancetechnicians_priority ON asset_maintenance_maintenancetechnicians(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancetechnicians_created_at ON asset_maintenance_maintenancetechnicians(created_at);

-- Operational seed data fixtures for asset_maintenance_maintenancetechnicians
INSERT OR IGNORE INTO asset_maintenance_maintenancetechnicians (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAI-0001", "Primary Operational MaintenanceTechnician 1", 24500.00, 150.0, "ACTIVE", "uuid-maintenancetechnician-01"),
    (2, "MAI-0002", "Secondary Corporate MaintenanceTechnician 2", 18200.50, 80.0, "ACTIVE", "uuid-maintenancetechnician-02"),
    (3, "MAI-0003", "Consolidated Branch MaintenanceTechnician 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-maintenancetechnician-03"),
    (4, "MAI-0004", "Enterprise Audited MaintenanceTechnician 4", 32800.00, 210.0, "ACTIVE", "uuid-maintenancetechnician-04"),
    (5, "MAI-0005", "Executive Strategic MaintenanceTechnician 5", 65000.00, 400.0, "ACTIVE", "uuid-maintenancetechnician-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_toolcalibrationlogs (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_toolcalibrationlogs_code ON asset_maintenance_toolcalibrationlogs(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_toolcalibrationlogs_org_status ON asset_maintenance_toolcalibrationlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_toolcalibrationlogs_priority ON asset_maintenance_toolcalibrationlogs(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_toolcalibrationlogs_created_at ON asset_maintenance_toolcalibrationlogs(created_at);

-- Operational seed data fixtures for asset_maintenance_toolcalibrationlogs
INSERT OR IGNORE INTO asset_maintenance_toolcalibrationlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TOO-0001", "Primary Operational ToolCalibrationLog 1", 24500.00, 150.0, "ACTIVE", "uuid-toolcalibrationlog-01"),
    (2, "TOO-0002", "Secondary Corporate ToolCalibrationLog 2", 18200.50, 80.0, "ACTIVE", "uuid-toolcalibrationlog-02"),
    (3, "TOO-0003", "Consolidated Branch ToolCalibrationLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-toolcalibrationlog-03"),
    (4, "TOO-0004", "Enterprise Audited ToolCalibrationLog 4", 32800.00, 210.0, "ACTIVE", "uuid-toolcalibrationlog-04"),
    (5, "TOO-0005", "Executive Strategic ToolCalibrationLog 5", 65000.00, 400.0, "ACTIVE", "uuid-toolcalibrationlog-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_downtimeincidents (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_downtimeincidents_code ON asset_maintenance_downtimeincidents(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_downtimeincidents_org_status ON asset_maintenance_downtimeincidents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_downtimeincidents_priority ON asset_maintenance_downtimeincidents(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_downtimeincidents_created_at ON asset_maintenance_downtimeincidents(created_at);

-- Operational seed data fixtures for asset_maintenance_downtimeincidents
INSERT OR IGNORE INTO asset_maintenance_downtimeincidents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOW-0001", "Primary Operational DowntimeIncident 1", 24500.00, 150.0, "ACTIVE", "uuid-downtimeincident-01"),
    (2, "DOW-0002", "Secondary Corporate DowntimeIncident 2", 18200.50, 80.0, "ACTIVE", "uuid-downtimeincident-02"),
    (3, "DOW-0003", "Consolidated Branch DowntimeIncident 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-downtimeincident-03"),
    (4, "DOW-0004", "Enterprise Audited DowntimeIncident 4", 32800.00, 210.0, "ACTIVE", "uuid-downtimeincident-04"),
    (5, "DOW-0005", "Executive Strategic DowntimeIncident 5", 65000.00, 400.0, "ACTIVE", "uuid-downtimeincident-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_lubricationroutes (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_lubricationroutes_code ON asset_maintenance_lubricationroutes(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_lubricationroutes_org_status ON asset_maintenance_lubricationroutes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_lubricationroutes_priority ON asset_maintenance_lubricationroutes(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_lubricationroutes_created_at ON asset_maintenance_lubricationroutes(created_at);

-- Operational seed data fixtures for asset_maintenance_lubricationroutes
INSERT OR IGNORE INTO asset_maintenance_lubricationroutes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LUB-0001", "Primary Operational LubricationRoute 1", 24500.00, 150.0, "ACTIVE", "uuid-lubricationroute-01"),
    (2, "LUB-0002", "Secondary Corporate LubricationRoute 2", 18200.50, 80.0, "ACTIVE", "uuid-lubricationroute-02"),
    (3, "LUB-0003", "Consolidated Branch LubricationRoute 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-lubricationroute-03"),
    (4, "LUB-0004", "Enterprise Audited LubricationRoute 4", 32800.00, 210.0, "ACTIVE", "uuid-lubricationroute-04"),
    (5, "LUB-0005", "Executive Strategic LubricationRoute 5", 65000.00, 400.0, "ACTIVE", "uuid-lubricationroute-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_safetyworkpermits (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_safetyworkpermits_code ON asset_maintenance_safetyworkpermits(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_safetyworkpermits_org_status ON asset_maintenance_safetyworkpermits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_safetyworkpermits_priority ON asset_maintenance_safetyworkpermits(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_safetyworkpermits_created_at ON asset_maintenance_safetyworkpermits(created_at);

-- Operational seed data fixtures for asset_maintenance_safetyworkpermits
INSERT OR IGNORE INTO asset_maintenance_safetyworkpermits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAF-0001", "Primary Operational SafetyWorkPermit 1", 24500.00, 150.0, "ACTIVE", "uuid-safetyworkpermit-01"),
    (2, "SAF-0002", "Secondary Corporate SafetyWorkPermit 2", 18200.50, 80.0, "ACTIVE", "uuid-safetyworkpermit-02"),
    (3, "SAF-0003", "Consolidated Branch SafetyWorkPermit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-safetyworkpermit-03"),
    (4, "SAF-0004", "Enterprise Audited SafetyWorkPermit 4", 32800.00, 210.0, "ACTIVE", "uuid-safetyworkpermit-04"),
    (5, "SAF-0005", "Executive Strategic SafetyWorkPermit 5", 65000.00, 400.0, "ACTIVE", "uuid-safetyworkpermit-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_vibrationanalysiss (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vibrationanalysiss_code ON asset_maintenance_vibrationanalysiss(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vibrationanalysiss_org_status ON asset_maintenance_vibrationanalysiss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vibrationanalysiss_priority ON asset_maintenance_vibrationanalysiss(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vibrationanalysiss_created_at ON asset_maintenance_vibrationanalysiss(created_at);

-- Operational seed data fixtures for asset_maintenance_vibrationanalysiss
INSERT OR IGNORE INTO asset_maintenance_vibrationanalysiss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VIB-0001", "Primary Operational VibrationAnalysis 1", 24500.00, 150.0, "ACTIVE", "uuid-vibrationanalysis-01"),
    (2, "VIB-0002", "Secondary Corporate VibrationAnalysis 2", 18200.50, 80.0, "ACTIVE", "uuid-vibrationanalysis-02"),
    (3, "VIB-0003", "Consolidated Branch VibrationAnalysis 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vibrationanalysis-03"),
    (4, "VIB-0004", "Enterprise Audited VibrationAnalysis 4", 32800.00, 210.0, "ACTIVE", "uuid-vibrationanalysis-04"),
    (5, "VIB-0005", "Executive Strategic VibrationAnalysis 5", 65000.00, 400.0, "ACTIVE", "uuid-vibrationanalysis-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_thermalinspections (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_thermalinspections_code ON asset_maintenance_thermalinspections(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_thermalinspections_org_status ON asset_maintenance_thermalinspections(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_thermalinspections_priority ON asset_maintenance_thermalinspections(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_thermalinspections_created_at ON asset_maintenance_thermalinspections(created_at);

-- Operational seed data fixtures for asset_maintenance_thermalinspections
INSERT OR IGNORE INTO asset_maintenance_thermalinspections (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "THE-0001", "Primary Operational ThermalInspection 1", 24500.00, 150.0, "ACTIVE", "uuid-thermalinspection-01"),
    (2, "THE-0002", "Secondary Corporate ThermalInspection 2", 18200.50, 80.0, "ACTIVE", "uuid-thermalinspection-02"),
    (3, "THE-0003", "Consolidated Branch ThermalInspection 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-thermalinspection-03"),
    (4, "THE-0004", "Enterprise Audited ThermalInspection 4", 32800.00, 210.0, "ACTIVE", "uuid-thermalinspection-04"),
    (5, "THE-0005", "Executive Strategic ThermalInspection 5", 65000.00, 400.0, "ACTIVE", "uuid-thermalinspection-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_workorderfeedbacks (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_workorderfeedbacks_code ON asset_maintenance_workorderfeedbacks(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_workorderfeedbacks_org_status ON asset_maintenance_workorderfeedbacks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_workorderfeedbacks_priority ON asset_maintenance_workorderfeedbacks(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_workorderfeedbacks_created_at ON asset_maintenance_workorderfeedbacks(created_at);

-- Operational seed data fixtures for asset_maintenance_workorderfeedbacks
INSERT OR IGNORE INTO asset_maintenance_workorderfeedbacks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WOR-0001", "Primary Operational WorkOrderFeedback 1", 24500.00, 150.0, "ACTIVE", "uuid-workorderfeedback-01"),
    (2, "WOR-0002", "Secondary Corporate WorkOrderFeedback 2", 18200.50, 80.0, "ACTIVE", "uuid-workorderfeedback-02"),
    (3, "WOR-0003", "Consolidated Branch WorkOrderFeedback 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-workorderfeedback-03"),
    (4, "WOR-0004", "Enterprise Audited WorkOrderFeedback 4", 32800.00, 210.0, "ACTIVE", "uuid-workorderfeedback-04"),
    (5, "WOR-0005", "Executive Strategic WorkOrderFeedback 5", 65000.00, 400.0, "ACTIVE", "uuid-workorderfeedback-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_vendorservicecontracts (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vendorservicecontracts_code ON asset_maintenance_vendorservicecontracts(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vendorservicecontracts_org_status ON asset_maintenance_vendorservicecontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vendorservicecontracts_priority ON asset_maintenance_vendorservicecontracts(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_vendorservicecontracts_created_at ON asset_maintenance_vendorservicecontracts(created_at);

-- Operational seed data fixtures for asset_maintenance_vendorservicecontracts
INSERT OR IGNORE INTO asset_maintenance_vendorservicecontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorServiceContract 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorservicecontract-01"),
    (2, "VEN-0002", "Secondary Corporate VendorServiceContract 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorservicecontract-02"),
    (3, "VEN-0003", "Consolidated Branch VendorServiceContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorservicecontract-03"),
    (4, "VEN-0004", "Enterprise Audited VendorServiceContract 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorservicecontract-04"),
    (5, "VEN-0005", "Executive Strategic VendorServiceContract 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorservicecontract-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_equipmentbillofmaterials (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentbillofmaterials_code ON asset_maintenance_equipmentbillofmaterials(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentbillofmaterials_org_status ON asset_maintenance_equipmentbillofmaterials(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentbillofmaterials_priority ON asset_maintenance_equipmentbillofmaterials(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_equipmentbillofmaterials_created_at ON asset_maintenance_equipmentbillofmaterials(created_at);

-- Operational seed data fixtures for asset_maintenance_equipmentbillofmaterials
INSERT OR IGNORE INTO asset_maintenance_equipmentbillofmaterials (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EQU-0001", "Primary Operational EquipmentBillOfMaterial 1", 24500.00, 150.0, "ACTIVE", "uuid-equipmentbillofmaterial-01"),
    (2, "EQU-0002", "Secondary Corporate EquipmentBillOfMaterial 2", 18200.50, 80.0, "ACTIVE", "uuid-equipmentbillofmaterial-02"),
    (3, "EQU-0003", "Consolidated Branch EquipmentBillOfMaterial 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-equipmentbillofmaterial-03"),
    (4, "EQU-0004", "Enterprise Audited EquipmentBillOfMaterial 4", 32800.00, 210.0, "ACTIVE", "uuid-equipmentbillofmaterial-04"),
    (5, "EQU-0005", "Executive Strategic EquipmentBillOfMaterial 5", 65000.00, 400.0, "ACTIVE", "uuid-equipmentbillofmaterial-05");

CREATE TABLE IF NOT EXISTS asset_maintenance_maintenancekpis (
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

CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancekpis_code ON asset_maintenance_maintenancekpis(code);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancekpis_org_status ON asset_maintenance_maintenancekpis(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancekpis_priority ON asset_maintenance_maintenancekpis(priority);
CREATE INDEX IF NOT EXISTS idx_asset_maintenance_maintenancekpis_created_at ON asset_maintenance_maintenancekpis(created_at);

-- Operational seed data fixtures for asset_maintenance_maintenancekpis
INSERT OR IGNORE INTO asset_maintenance_maintenancekpis (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAI-0001", "Primary Operational MaintenanceKPI 1", 24500.00, 150.0, "ACTIVE", "uuid-maintenancekpi-01"),
    (2, "MAI-0002", "Secondary Corporate MaintenanceKPI 2", 18200.50, 80.0, "ACTIVE", "uuid-maintenancekpi-02"),
    (3, "MAI-0003", "Consolidated Branch MaintenanceKPI 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-maintenancekpi-03"),
    (4, "MAI-0004", "Enterprise Audited MaintenanceKPI 4", 32800.00, 210.0, "ACTIVE", "uuid-maintenancekpi-04"),
    (5, "MAI-0005", "Executive Strategic MaintenanceKPI 5", 65000.00, 400.0, "ACTIVE", "uuid-maintenancekpi-05");

