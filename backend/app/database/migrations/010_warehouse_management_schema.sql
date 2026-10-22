-- SmartERP Enterprise Titan Migration 010: Advanced Warehouse Management (WMS) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS warehouse_management_warehousezones (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_warehousezones_code ON warehouse_management_warehousezones(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_warehousezones_org_status ON warehouse_management_warehousezones(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_warehousezones_priority ON warehouse_management_warehousezones(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_warehousezones_created_at ON warehouse_management_warehousezones(created_at);

-- Operational seed data fixtures for warehouse_management_warehousezones
INSERT OR IGNORE INTO warehouse_management_warehousezones (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAR-0001", "Primary Operational WarehouseZone 1", 24500.00, 150.0, "ACTIVE", "uuid-warehousezone-01"),
    (2, "WAR-0002", "Secondary Corporate WarehouseZone 2", 18200.50, 80.0, "ACTIVE", "uuid-warehousezone-02"),
    (3, "WAR-0003", "Consolidated Branch WarehouseZone 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-warehousezone-03"),
    (4, "WAR-0004", "Enterprise Audited WarehouseZone 4", 32800.00, 210.0, "ACTIVE", "uuid-warehousezone-04"),
    (5, "WAR-0005", "Executive Strategic WarehouseZone 5", 65000.00, 400.0, "ACTIVE", "uuid-warehousezone-05");

CREATE TABLE IF NOT EXISTS warehouse_management_storageaisles (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_storageaisles_code ON warehouse_management_storageaisles(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_storageaisles_org_status ON warehouse_management_storageaisles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_storageaisles_priority ON warehouse_management_storageaisles(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_storageaisles_created_at ON warehouse_management_storageaisles(created_at);

-- Operational seed data fixtures for warehouse_management_storageaisles
INSERT OR IGNORE INTO warehouse_management_storageaisles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STO-0001", "Primary Operational StorageAisle 1", 24500.00, 150.0, "ACTIVE", "uuid-storageaisle-01"),
    (2, "STO-0002", "Secondary Corporate StorageAisle 2", 18200.50, 80.0, "ACTIVE", "uuid-storageaisle-02"),
    (3, "STO-0003", "Consolidated Branch StorageAisle 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-storageaisle-03"),
    (4, "STO-0004", "Enterprise Audited StorageAisle 4", 32800.00, 210.0, "ACTIVE", "uuid-storageaisle-04"),
    (5, "STO-0005", "Executive Strategic StorageAisle 5", 65000.00, 400.0, "ACTIVE", "uuid-storageaisle-05");

CREATE TABLE IF NOT EXISTS warehouse_management_rackbinlocations (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_rackbinlocations_code ON warehouse_management_rackbinlocations(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_rackbinlocations_org_status ON warehouse_management_rackbinlocations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_rackbinlocations_priority ON warehouse_management_rackbinlocations(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_rackbinlocations_created_at ON warehouse_management_rackbinlocations(created_at);

-- Operational seed data fixtures for warehouse_management_rackbinlocations
INSERT OR IGNORE INTO warehouse_management_rackbinlocations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RAC-0001", "Primary Operational RackBinLocation 1", 24500.00, 150.0, "ACTIVE", "uuid-rackbinlocation-01"),
    (2, "RAC-0002", "Secondary Corporate RackBinLocation 2", 18200.50, 80.0, "ACTIVE", "uuid-rackbinlocation-02"),
    (3, "RAC-0003", "Consolidated Branch RackBinLocation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-rackbinlocation-03"),
    (4, "RAC-0004", "Enterprise Audited RackBinLocation 4", 32800.00, 210.0, "ACTIVE", "uuid-rackbinlocation-04"),
    (5, "RAC-0005", "Executive Strategic RackBinLocation 5", 65000.00, 400.0, "ACTIVE", "uuid-rackbinlocation-05");

CREATE TABLE IF NOT EXISTS warehouse_management_stockpallets (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_stockpallets_code ON warehouse_management_stockpallets(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_stockpallets_org_status ON warehouse_management_stockpallets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_stockpallets_priority ON warehouse_management_stockpallets(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_stockpallets_created_at ON warehouse_management_stockpallets(created_at);

-- Operational seed data fixtures for warehouse_management_stockpallets
INSERT OR IGNORE INTO warehouse_management_stockpallets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STO-0001", "Primary Operational StockPallet 1", 24500.00, 150.0, "ACTIVE", "uuid-stockpallet-01"),
    (2, "STO-0002", "Secondary Corporate StockPallet 2", 18200.50, 80.0, "ACTIVE", "uuid-stockpallet-02"),
    (3, "STO-0003", "Consolidated Branch StockPallet 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-stockpallet-03"),
    (4, "STO-0004", "Enterprise Audited StockPallet 4", 32800.00, 210.0, "ACTIVE", "uuid-stockpallet-04"),
    (5, "STO-0005", "Executive Strategic StockPallet 5", 65000.00, 400.0, "ACTIVE", "uuid-stockpallet-05");

CREATE TABLE IF NOT EXISTS warehouse_management_wavepickingplans (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_wavepickingplans_code ON warehouse_management_wavepickingplans(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_wavepickingplans_org_status ON warehouse_management_wavepickingplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_wavepickingplans_priority ON warehouse_management_wavepickingplans(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_wavepickingplans_created_at ON warehouse_management_wavepickingplans(created_at);

-- Operational seed data fixtures for warehouse_management_wavepickingplans
INSERT OR IGNORE INTO warehouse_management_wavepickingplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAV-0001", "Primary Operational WavePickingPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-wavepickingplan-01"),
    (2, "WAV-0002", "Secondary Corporate WavePickingPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-wavepickingplan-02"),
    (3, "WAV-0003", "Consolidated Branch WavePickingPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-wavepickingplan-03"),
    (4, "WAV-0004", "Enterprise Audited WavePickingPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-wavepickingplan-04"),
    (5, "WAV-0005", "Executive Strategic WavePickingPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-wavepickingplan-05");

CREATE TABLE IF NOT EXISTS warehouse_management_putawaytasks (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_putawaytasks_code ON warehouse_management_putawaytasks(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_putawaytasks_org_status ON warehouse_management_putawaytasks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_putawaytasks_priority ON warehouse_management_putawaytasks(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_putawaytasks_created_at ON warehouse_management_putawaytasks(created_at);

-- Operational seed data fixtures for warehouse_management_putawaytasks
INSERT OR IGNORE INTO warehouse_management_putawaytasks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PUT-0001", "Primary Operational PutawayTask 1", 24500.00, 150.0, "ACTIVE", "uuid-putawaytask-01"),
    (2, "PUT-0002", "Secondary Corporate PutawayTask 2", 18200.50, 80.0, "ACTIVE", "uuid-putawaytask-02"),
    (3, "PUT-0003", "Consolidated Branch PutawayTask 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-putawaytask-03"),
    (4, "PUT-0004", "Enterprise Audited PutawayTask 4", 32800.00, 210.0, "ACTIVE", "uuid-putawaytask-04"),
    (5, "PUT-0005", "Executive Strategic PutawayTask 5", 65000.00, 400.0, "ACTIVE", "uuid-putawaytask-05");

CREATE TABLE IF NOT EXISTS warehouse_management_cyclecountsheets (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_cyclecountsheets_code ON warehouse_management_cyclecountsheets(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_cyclecountsheets_org_status ON warehouse_management_cyclecountsheets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_cyclecountsheets_priority ON warehouse_management_cyclecountsheets(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_cyclecountsheets_created_at ON warehouse_management_cyclecountsheets(created_at);

-- Operational seed data fixtures for warehouse_management_cyclecountsheets
INSERT OR IGNORE INTO warehouse_management_cyclecountsheets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CYC-0001", "Primary Operational CycleCountSheet 1", 24500.00, 150.0, "ACTIVE", "uuid-cyclecountsheet-01"),
    (2, "CYC-0002", "Secondary Corporate CycleCountSheet 2", 18200.50, 80.0, "ACTIVE", "uuid-cyclecountsheet-02"),
    (3, "CYC-0003", "Consolidated Branch CycleCountSheet 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cyclecountsheet-03"),
    (4, "CYC-0004", "Enterprise Audited CycleCountSheet 4", 32800.00, 210.0, "ACTIVE", "uuid-cyclecountsheet-04"),
    (5, "CYC-0005", "Executive Strategic CycleCountSheet 5", 65000.00, 400.0, "ACTIVE", "uuid-cyclecountsheet-05");

CREATE TABLE IF NOT EXISTS warehouse_management_bintransferorders (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_bintransferorders_code ON warehouse_management_bintransferorders(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_bintransferorders_org_status ON warehouse_management_bintransferorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_bintransferorders_priority ON warehouse_management_bintransferorders(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_bintransferorders_created_at ON warehouse_management_bintransferorders(created_at);

-- Operational seed data fixtures for warehouse_management_bintransferorders
INSERT OR IGNORE INTO warehouse_management_bintransferorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BIN-0001", "Primary Operational BinTransferOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-bintransferorder-01"),
    (2, "BIN-0002", "Secondary Corporate BinTransferOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-bintransferorder-02"),
    (3, "BIN-0003", "Consolidated Branch BinTransferOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bintransferorder-03"),
    (4, "BIN-0004", "Enterprise Audited BinTransferOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-bintransferorder-04"),
    (5, "BIN-0005", "Executive Strategic BinTransferOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-bintransferorder-05");

CREATE TABLE IF NOT EXISTS warehouse_management_crossdockroutes (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_crossdockroutes_code ON warehouse_management_crossdockroutes(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_crossdockroutes_org_status ON warehouse_management_crossdockroutes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_crossdockroutes_priority ON warehouse_management_crossdockroutes(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_crossdockroutes_created_at ON warehouse_management_crossdockroutes(created_at);

-- Operational seed data fixtures for warehouse_management_crossdockroutes
INSERT OR IGNORE INTO warehouse_management_crossdockroutes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CRO-0001", "Primary Operational CrossDockRoute 1", 24500.00, 150.0, "ACTIVE", "uuid-crossdockroute-01"),
    (2, "CRO-0002", "Secondary Corporate CrossDockRoute 2", 18200.50, 80.0, "ACTIVE", "uuid-crossdockroute-02"),
    (3, "CRO-0003", "Consolidated Branch CrossDockRoute 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-crossdockroute-03"),
    (4, "CRO-0004", "Enterprise Audited CrossDockRoute 4", 32800.00, 210.0, "ACTIVE", "uuid-crossdockroute-04"),
    (5, "CRO-0005", "Executive Strategic CrossDockRoute 5", 65000.00, 400.0, "ACTIVE", "uuid-crossdockroute-05");

CREATE TABLE IF NOT EXISTS warehouse_management_lpntags (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_lpntags_code ON warehouse_management_lpntags(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_lpntags_org_status ON warehouse_management_lpntags(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_lpntags_priority ON warehouse_management_lpntags(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_lpntags_created_at ON warehouse_management_lpntags(created_at);

-- Operational seed data fixtures for warehouse_management_lpntags
INSERT OR IGNORE INTO warehouse_management_lpntags (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LPN-0001", "Primary Operational LPNTag 1", 24500.00, 150.0, "ACTIVE", "uuid-lpntag-01"),
    (2, "LPN-0002", "Secondary Corporate LPNTag 2", 18200.50, 80.0, "ACTIVE", "uuid-lpntag-02"),
    (3, "LPN-0003", "Consolidated Branch LPNTag 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-lpntag-03"),
    (4, "LPN-0004", "Enterprise Audited LPNTag 4", 32800.00, 210.0, "ACTIVE", "uuid-lpntag-04"),
    (5, "LPN-0005", "Executive Strategic LPNTag 5", 65000.00, 400.0, "ACTIVE", "uuid-lpntag-05");

CREATE TABLE IF NOT EXISTS warehouse_management_packagingstations (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_packagingstations_code ON warehouse_management_packagingstations(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_packagingstations_org_status ON warehouse_management_packagingstations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_packagingstations_priority ON warehouse_management_packagingstations(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_packagingstations_created_at ON warehouse_management_packagingstations(created_at);

-- Operational seed data fixtures for warehouse_management_packagingstations
INSERT OR IGNORE INTO warehouse_management_packagingstations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAC-0001", "Primary Operational PackagingStation 1", 24500.00, 150.0, "ACTIVE", "uuid-packagingstation-01"),
    (2, "PAC-0002", "Secondary Corporate PackagingStation 2", 18200.50, 80.0, "ACTIVE", "uuid-packagingstation-02"),
    (3, "PAC-0003", "Consolidated Branch PackagingStation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-packagingstation-03"),
    (4, "PAC-0004", "Enterprise Audited PackagingStation 4", 32800.00, 210.0, "ACTIVE", "uuid-packagingstation-04"),
    (5, "PAC-0005", "Executive Strategic PackagingStation 5", 65000.00, 400.0, "ACTIVE", "uuid-packagingstation-05");

CREATE TABLE IF NOT EXISTS warehouse_management_dockdoorassignments (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_dockdoorassignments_code ON warehouse_management_dockdoorassignments(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_dockdoorassignments_org_status ON warehouse_management_dockdoorassignments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_dockdoorassignments_priority ON warehouse_management_dockdoorassignments(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_dockdoorassignments_created_at ON warehouse_management_dockdoorassignments(created_at);

-- Operational seed data fixtures for warehouse_management_dockdoorassignments
INSERT OR IGNORE INTO warehouse_management_dockdoorassignments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DockDoorAssignment 1", 24500.00, 150.0, "ACTIVE", "uuid-dockdoorassignment-01"),
    (2, "DOC-0002", "Secondary Corporate DockDoorAssignment 2", 18200.50, 80.0, "ACTIVE", "uuid-dockdoorassignment-02"),
    (3, "DOC-0003", "Consolidated Branch DockDoorAssignment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dockdoorassignment-03"),
    (4, "DOC-0004", "Enterprise Audited DockDoorAssignment 4", 32800.00, 210.0, "ACTIVE", "uuid-dockdoorassignment-04"),
    (5, "DOC-0005", "Executive Strategic DockDoorAssignment 5", 65000.00, 400.0, "ACTIVE", "uuid-dockdoorassignment-05");

CREATE TABLE IF NOT EXISTS warehouse_management_kittingorders (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_kittingorders_code ON warehouse_management_kittingorders(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_kittingorders_org_status ON warehouse_management_kittingorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_kittingorders_priority ON warehouse_management_kittingorders(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_kittingorders_created_at ON warehouse_management_kittingorders(created_at);

-- Operational seed data fixtures for warehouse_management_kittingorders
INSERT OR IGNORE INTO warehouse_management_kittingorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "KIT-0001", "Primary Operational KittingOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-kittingorder-01"),
    (2, "KIT-0002", "Secondary Corporate KittingOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-kittingorder-02"),
    (3, "KIT-0003", "Consolidated Branch KittingOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-kittingorder-03"),
    (4, "KIT-0004", "Enterprise Audited KittingOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-kittingorder-04"),
    (5, "KIT-0005", "Executive Strategic KittingOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-kittingorder-05");

CREATE TABLE IF NOT EXISTS warehouse_management_dekittingjobs (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_dekittingjobs_code ON warehouse_management_dekittingjobs(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_dekittingjobs_org_status ON warehouse_management_dekittingjobs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_dekittingjobs_priority ON warehouse_management_dekittingjobs(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_dekittingjobs_created_at ON warehouse_management_dekittingjobs(created_at);

-- Operational seed data fixtures for warehouse_management_dekittingjobs
INSERT OR IGNORE INTO warehouse_management_dekittingjobs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEK-0001", "Primary Operational DeKittingJob 1", 24500.00, 150.0, "ACTIVE", "uuid-dekittingjob-01"),
    (2, "DEK-0002", "Secondary Corporate DeKittingJob 2", 18200.50, 80.0, "ACTIVE", "uuid-dekittingjob-02"),
    (3, "DEK-0003", "Consolidated Branch DeKittingJob 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dekittingjob-03"),
    (4, "DEK-0004", "Enterprise Audited DeKittingJob 4", 32800.00, 210.0, "ACTIVE", "uuid-dekittingjob-04"),
    (5, "DEK-0005", "Executive Strategic DeKittingJob 5", 65000.00, 400.0, "ACTIVE", "uuid-dekittingjob-05");

CREATE TABLE IF NOT EXISTS warehouse_management_hazardclassifications (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_hazardclassifications_code ON warehouse_management_hazardclassifications(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_hazardclassifications_org_status ON warehouse_management_hazardclassifications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_hazardclassifications_priority ON warehouse_management_hazardclassifications(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_hazardclassifications_created_at ON warehouse_management_hazardclassifications(created_at);

-- Operational seed data fixtures for warehouse_management_hazardclassifications
INSERT OR IGNORE INTO warehouse_management_hazardclassifications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HAZ-0001", "Primary Operational HazardClassification 1", 24500.00, 150.0, "ACTIVE", "uuid-hazardclassification-01"),
    (2, "HAZ-0002", "Secondary Corporate HazardClassification 2", 18200.50, 80.0, "ACTIVE", "uuid-hazardclassification-02"),
    (3, "HAZ-0003", "Consolidated Branch HazardClassification 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hazardclassification-03"),
    (4, "HAZ-0004", "Enterprise Audited HazardClassification 4", 32800.00, 210.0, "ACTIVE", "uuid-hazardclassification-04"),
    (5, "HAZ-0005", "Executive Strategic HazardClassification 5", 65000.00, 400.0, "ACTIVE", "uuid-hazardclassification-05");

CREATE TABLE IF NOT EXISTS warehouse_management_templogrecords (
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

CREATE INDEX IF NOT EXISTS idx_warehouse_management_templogrecords_code ON warehouse_management_templogrecords(code);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_templogrecords_org_status ON warehouse_management_templogrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_templogrecords_priority ON warehouse_management_templogrecords(priority);
CREATE INDEX IF NOT EXISTS idx_warehouse_management_templogrecords_created_at ON warehouse_management_templogrecords(created_at);

-- Operational seed data fixtures for warehouse_management_templogrecords
INSERT OR IGNORE INTO warehouse_management_templogrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEM-0001", "Primary Operational TempLogRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-templogrecord-01"),
    (2, "TEM-0002", "Secondary Corporate TempLogRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-templogrecord-02"),
    (3, "TEM-0003", "Consolidated Branch TempLogRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-templogrecord-03"),
    (4, "TEM-0004", "Enterprise Audited TempLogRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-templogrecord-04"),
    (5, "TEM-0005", "Executive Strategic TempLogRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-templogrecord-05");

