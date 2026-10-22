-- SmartERP Enterprise Titan Migration 054: Real-time IoT Telemetry & Supply Chain Visibility DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS supply_chain_visibility_iotsensortelemetrypings (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_iotsensortelemetrypings_code ON supply_chain_visibility_iotsensortelemetrypings(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_iotsensortelemetrypings_org_status ON supply_chain_visibility_iotsensortelemetrypings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_iotsensortelemetrypings_priority ON supply_chain_visibility_iotsensortelemetrypings(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_iotsensortelemetrypings_created_at ON supply_chain_visibility_iotsensortelemetrypings(created_at);

-- Operational seed data fixtures for supply_chain_visibility_iotsensortelemetrypings
INSERT OR IGNORE INTO supply_chain_visibility_iotsensortelemetrypings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "IOT-0001", "Primary Operational IoTSensorTelemetryPing 1", 24500.00, 150.0, "ACTIVE", "uuid-iotsensortelemetryping-01"),
    (2, "IOT-0002", "Secondary Corporate IoTSensorTelemetryPing 2", 18200.50, 80.0, "ACTIVE", "uuid-iotsensortelemetryping-02"),
    (3, "IOT-0003", "Consolidated Branch IoTSensorTelemetryPing 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-iotsensortelemetryping-03"),
    (4, "IOT-0004", "Enterprise Audited IoTSensorTelemetryPing 4", 32800.00, 210.0, "ACTIVE", "uuid-iotsensortelemetryping-04"),
    (5, "IOT-0005", "Executive Strategic IoTSensorTelemetryPing 5", 65000.00, 400.0, "ACTIVE", "uuid-iotsensortelemetryping-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_coldchaintemploggers (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_coldchaintemploggers_code ON supply_chain_visibility_coldchaintemploggers(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_coldchaintemploggers_org_status ON supply_chain_visibility_coldchaintemploggers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_coldchaintemploggers_priority ON supply_chain_visibility_coldchaintemploggers(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_coldchaintemploggers_created_at ON supply_chain_visibility_coldchaintemploggers(created_at);

-- Operational seed data fixtures for supply_chain_visibility_coldchaintemploggers
INSERT OR IGNORE INTO supply_chain_visibility_coldchaintemploggers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COL-0001", "Primary Operational ColdChainTempLogger 1", 24500.00, 150.0, "ACTIVE", "uuid-coldchaintemplogger-01"),
    (2, "COL-0002", "Secondary Corporate ColdChainTempLogger 2", 18200.50, 80.0, "ACTIVE", "uuid-coldchaintemplogger-02"),
    (3, "COL-0003", "Consolidated Branch ColdChainTempLogger 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-coldchaintemplogger-03"),
    (4, "COL-0004", "Enterprise Audited ColdChainTempLogger 4", 32800.00, 210.0, "ACTIVE", "uuid-coldchaintemplogger-04"),
    (5, "COL-0005", "Executive Strategic ColdChainTempLogger 5", 65000.00, 400.0, "ACTIVE", "uuid-coldchaintemplogger-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_rfidpalletscanrecords (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_rfidpalletscanrecords_code ON supply_chain_visibility_rfidpalletscanrecords(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_rfidpalletscanrecords_org_status ON supply_chain_visibility_rfidpalletscanrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_rfidpalletscanrecords_priority ON supply_chain_visibility_rfidpalletscanrecords(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_rfidpalletscanrecords_created_at ON supply_chain_visibility_rfidpalletscanrecords(created_at);

-- Operational seed data fixtures for supply_chain_visibility_rfidpalletscanrecords
INSERT OR IGNORE INTO supply_chain_visibility_rfidpalletscanrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RFI-0001", "Primary Operational RFIDPalletScanRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-rfidpalletscanrecord-01"),
    (2, "RFI-0002", "Secondary Corporate RFIDPalletScanRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-rfidpalletscanrecord-02"),
    (3, "RFI-0003", "Consolidated Branch RFIDPalletScanRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-rfidpalletscanrecord-03"),
    (4, "RFI-0004", "Enterprise Audited RFIDPalletScanRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-rfidpalletscanrecord-04"),
    (5, "RFI-0005", "Executive Strategic RFIDPalletScanRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-rfidpalletscanrecord-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_geofencetransitevents (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_geofencetransitevents_code ON supply_chain_visibility_geofencetransitevents(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_geofencetransitevents_org_status ON supply_chain_visibility_geofencetransitevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_geofencetransitevents_priority ON supply_chain_visibility_geofencetransitevents(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_geofencetransitevents_created_at ON supply_chain_visibility_geofencetransitevents(created_at);

-- Operational seed data fixtures for supply_chain_visibility_geofencetransitevents
INSERT OR IGNORE INTO supply_chain_visibility_geofencetransitevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GEO-0001", "Primary Operational GeofenceTransitEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-geofencetransitevent-01"),
    (2, "GEO-0002", "Secondary Corporate GeofenceTransitEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-geofencetransitevent-02"),
    (3, "GEO-0003", "Consolidated Branch GeofenceTransitEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-geofencetransitevent-03"),
    (4, "GEO-0004", "Enterprise Audited GeofenceTransitEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-geofencetransitevent-04"),
    (5, "GEO-0005", "Executive Strategic GeofenceTransitEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-geofencetransitevent-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_shipmentshocksensorlogs (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_shipmentshocksensorlogs_code ON supply_chain_visibility_shipmentshocksensorlogs(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_shipmentshocksensorlogs_org_status ON supply_chain_visibility_shipmentshocksensorlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_shipmentshocksensorlogs_priority ON supply_chain_visibility_shipmentshocksensorlogs(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_shipmentshocksensorlogs_created_at ON supply_chain_visibility_shipmentshocksensorlogs(created_at);

-- Operational seed data fixtures for supply_chain_visibility_shipmentshocksensorlogs
INSERT OR IGNORE INTO supply_chain_visibility_shipmentshocksensorlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational ShipmentShockSensorLog 1", 24500.00, 150.0, "ACTIVE", "uuid-shipmentshocksensorlog-01"),
    (2, "SHI-0002", "Secondary Corporate ShipmentShockSensorLog 2", 18200.50, 80.0, "ACTIVE", "uuid-shipmentshocksensorlog-02"),
    (3, "SHI-0003", "Consolidated Branch ShipmentShockSensorLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shipmentshocksensorlog-03"),
    (4, "SHI-0004", "Enterprise Audited ShipmentShockSensorLog 4", 32800.00, 210.0, "ACTIVE", "uuid-shipmentshocksensorlog-04"),
    (5, "SHI-0005", "Executive Strategic ShipmentShockSensorLog 5", 65000.00, 400.0, "ACTIVE", "uuid-shipmentshocksensorlog-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_containersealstatuss (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_containersealstatuss_code ON supply_chain_visibility_containersealstatuss(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_containersealstatuss_org_status ON supply_chain_visibility_containersealstatuss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_containersealstatuss_priority ON supply_chain_visibility_containersealstatuss(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_containersealstatuss_created_at ON supply_chain_visibility_containersealstatuss(created_at);

-- Operational seed data fixtures for supply_chain_visibility_containersealstatuss
INSERT OR IGNORE INTO supply_chain_visibility_containersealstatuss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContainerSealStatus 1", 24500.00, 150.0, "ACTIVE", "uuid-containersealstatus-01"),
    (2, "CON-0002", "Secondary Corporate ContainerSealStatus 2", 18200.50, 80.0, "ACTIVE", "uuid-containersealstatus-02"),
    (3, "CON-0003", "Consolidated Branch ContainerSealStatus 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-containersealstatus-03"),
    (4, "CON-0004", "Enterprise Audited ContainerSealStatus 4", 32800.00, 210.0, "ACTIVE", "uuid-containersealstatus-04"),
    (5, "CON-0005", "Executive Strategic ContainerSealStatus 5", 65000.00, 400.0, "ACTIVE", "uuid-containersealstatus-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_smartcontractescrowevents (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_smartcontractescrowevents_code ON supply_chain_visibility_smartcontractescrowevents(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_smartcontractescrowevents_org_status ON supply_chain_visibility_smartcontractescrowevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_smartcontractescrowevents_priority ON supply_chain_visibility_smartcontractescrowevents(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_smartcontractescrowevents_created_at ON supply_chain_visibility_smartcontractescrowevents(created_at);

-- Operational seed data fixtures for supply_chain_visibility_smartcontractescrowevents
INSERT OR IGNORE INTO supply_chain_visibility_smartcontractescrowevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SMA-0001", "Primary Operational SmartContractEscrowEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-smartcontractescrowevent-01"),
    (2, "SMA-0002", "Secondary Corporate SmartContractEscrowEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-smartcontractescrowevent-02"),
    (3, "SMA-0003", "Consolidated Branch SmartContractEscrowEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-smartcontractescrowevent-03"),
    (4, "SMA-0004", "Enterprise Audited SmartContractEscrowEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-smartcontractescrowevent-04"),
    (5, "SMA-0005", "Executive Strategic SmartContractEscrowEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-smartcontractescrowevent-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_carrierlocationwaypoints (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carrierlocationwaypoints_code ON supply_chain_visibility_carrierlocationwaypoints(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carrierlocationwaypoints_org_status ON supply_chain_visibility_carrierlocationwaypoints(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carrierlocationwaypoints_priority ON supply_chain_visibility_carrierlocationwaypoints(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carrierlocationwaypoints_created_at ON supply_chain_visibility_carrierlocationwaypoints(created_at);

-- Operational seed data fixtures for supply_chain_visibility_carrierlocationwaypoints
INSERT OR IGNORE INTO supply_chain_visibility_carrierlocationwaypoints (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAR-0001", "Primary Operational CarrierLocationWaypoint 1", 24500.00, 150.0, "ACTIVE", "uuid-carrierlocationwaypoint-01"),
    (2, "CAR-0002", "Secondary Corporate CarrierLocationWaypoint 2", 18200.50, 80.0, "ACTIVE", "uuid-carrierlocationwaypoint-02"),
    (3, "CAR-0003", "Consolidated Branch CarrierLocationWaypoint 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-carrierlocationwaypoint-03"),
    (4, "CAR-0004", "Enterprise Audited CarrierLocationWaypoint 4", 32800.00, 210.0, "ACTIVE", "uuid-carrierlocationwaypoint-04"),
    (5, "CAR-0005", "Executive Strategic CarrierLocationWaypoint 5", 65000.00, 400.0, "ACTIVE", "uuid-carrierlocationwaypoint-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_dwelltimeexceednotices (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_dwelltimeexceednotices_code ON supply_chain_visibility_dwelltimeexceednotices(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_dwelltimeexceednotices_org_status ON supply_chain_visibility_dwelltimeexceednotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_dwelltimeexceednotices_priority ON supply_chain_visibility_dwelltimeexceednotices(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_dwelltimeexceednotices_created_at ON supply_chain_visibility_dwelltimeexceednotices(created_at);

-- Operational seed data fixtures for supply_chain_visibility_dwelltimeexceednotices
INSERT OR IGNORE INTO supply_chain_visibility_dwelltimeexceednotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DWE-0001", "Primary Operational DwellTimeExceedNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-dwelltimeexceednotice-01"),
    (2, "DWE-0002", "Secondary Corporate DwellTimeExceedNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-dwelltimeexceednotice-02"),
    (3, "DWE-0003", "Consolidated Branch DwellTimeExceedNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dwelltimeexceednotice-03"),
    (4, "DWE-0004", "Enterprise Audited DwellTimeExceedNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-dwelltimeexceednotice-04"),
    (5, "DWE-0005", "Executive Strategic DwellTimeExceedNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-dwelltimeexceednotice-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_predictiveetaestimates (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_predictiveetaestimates_code ON supply_chain_visibility_predictiveetaestimates(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_predictiveetaestimates_org_status ON supply_chain_visibility_predictiveetaestimates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_predictiveetaestimates_priority ON supply_chain_visibility_predictiveetaestimates(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_predictiveetaestimates_created_at ON supply_chain_visibility_predictiveetaestimates(created_at);

-- Operational seed data fixtures for supply_chain_visibility_predictiveetaestimates
INSERT OR IGNORE INTO supply_chain_visibility_predictiveetaestimates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRE-0001", "Primary Operational PredictiveETAEstimate 1", 24500.00, 150.0, "ACTIVE", "uuid-predictiveetaestimate-01"),
    (2, "PRE-0002", "Secondary Corporate PredictiveETAEstimate 2", 18200.50, 80.0, "ACTIVE", "uuid-predictiveetaestimate-02"),
    (3, "PRE-0003", "Consolidated Branch PredictiveETAEstimate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-predictiveetaestimate-03"),
    (4, "PRE-0004", "Enterprise Audited PredictiveETAEstimate 4", 32800.00, 210.0, "ACTIVE", "uuid-predictiveetaestimate-04"),
    (5, "PRE-0005", "Executive Strategic PredictiveETAEstimate 5", 65000.00, 400.0, "ACTIVE", "uuid-predictiveetaestimate-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_carbonemissionwaypoints (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carbonemissionwaypoints_code ON supply_chain_visibility_carbonemissionwaypoints(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carbonemissionwaypoints_org_status ON supply_chain_visibility_carbonemissionwaypoints(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carbonemissionwaypoints_priority ON supply_chain_visibility_carbonemissionwaypoints(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_carbonemissionwaypoints_created_at ON supply_chain_visibility_carbonemissionwaypoints(created_at);

-- Operational seed data fixtures for supply_chain_visibility_carbonemissionwaypoints
INSERT OR IGNORE INTO supply_chain_visibility_carbonemissionwaypoints (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAR-0001", "Primary Operational CarbonEmissionWaypoint 1", 24500.00, 150.0, "ACTIVE", "uuid-carbonemissionwaypoint-01"),
    (2, "CAR-0002", "Secondary Corporate CarbonEmissionWaypoint 2", 18200.50, 80.0, "ACTIVE", "uuid-carbonemissionwaypoint-02"),
    (3, "CAR-0003", "Consolidated Branch CarbonEmissionWaypoint 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-carbonemissionwaypoint-03"),
    (4, "CAR-0004", "Enterprise Audited CarbonEmissionWaypoint 4", 32800.00, 210.0, "ACTIVE", "uuid-carbonemissionwaypoint-04"),
    (5, "CAR-0005", "Executive Strategic CarbonEmissionWaypoint 5", 65000.00, 400.0, "ACTIVE", "uuid-carbonemissionwaypoint-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_customsclearancemilestones (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_customsclearancemilestones_code ON supply_chain_visibility_customsclearancemilestones(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_customsclearancemilestones_org_status ON supply_chain_visibility_customsclearancemilestones(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_customsclearancemilestones_priority ON supply_chain_visibility_customsclearancemilestones(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_customsclearancemilestones_created_at ON supply_chain_visibility_customsclearancemilestones(created_at);

-- Operational seed data fixtures for supply_chain_visibility_customsclearancemilestones
INSERT OR IGNORE INTO supply_chain_visibility_customsclearancemilestones (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomsClearanceMilestone 1", 24500.00, 150.0, "ACTIVE", "uuid-customsclearancemilestone-01"),
    (2, "CUS-0002", "Secondary Corporate CustomsClearanceMilestone 2", 18200.50, 80.0, "ACTIVE", "uuid-customsclearancemilestone-02"),
    (3, "CUS-0003", "Consolidated Branch CustomsClearanceMilestone 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customsclearancemilestone-03"),
    (4, "CUS-0004", "Enterprise Audited CustomsClearanceMilestone 4", 32800.00, 210.0, "ACTIVE", "uuid-customsclearancemilestone-04"),
    (5, "CUS-0005", "Executive Strategic CustomsClearanceMilestone 5", 65000.00, 400.0, "ACTIVE", "uuid-customsclearancemilestone-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_tamperevidentincidents (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_tamperevidentincidents_code ON supply_chain_visibility_tamperevidentincidents(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_tamperevidentincidents_org_status ON supply_chain_visibility_tamperevidentincidents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_tamperevidentincidents_priority ON supply_chain_visibility_tamperevidentincidents(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_tamperevidentincidents_created_at ON supply_chain_visibility_tamperevidentincidents(created_at);

-- Operational seed data fixtures for supply_chain_visibility_tamperevidentincidents
INSERT OR IGNORE INTO supply_chain_visibility_tamperevidentincidents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAM-0001", "Primary Operational TamperEvidentIncident 1", 24500.00, 150.0, "ACTIVE", "uuid-tamperevidentincident-01"),
    (2, "TAM-0002", "Secondary Corporate TamperEvidentIncident 2", 18200.50, 80.0, "ACTIVE", "uuid-tamperevidentincident-02"),
    (3, "TAM-0003", "Consolidated Branch TamperEvidentIncident 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tamperevidentincident-03"),
    (4, "TAM-0004", "Enterprise Audited TamperEvidentIncident 4", 32800.00, 210.0, "ACTIVE", "uuid-tamperevidentincident-04"),
    (5, "TAM-0005", "Executive Strategic TamperEvidentIncident 5", 65000.00, 400.0, "ACTIVE", "uuid-tamperevidentincident-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_weatherdisruptionalerts (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_weatherdisruptionalerts_code ON supply_chain_visibility_weatherdisruptionalerts(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_weatherdisruptionalerts_org_status ON supply_chain_visibility_weatherdisruptionalerts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_weatherdisruptionalerts_priority ON supply_chain_visibility_weatherdisruptionalerts(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_weatherdisruptionalerts_created_at ON supply_chain_visibility_weatherdisruptionalerts(created_at);

-- Operational seed data fixtures for supply_chain_visibility_weatherdisruptionalerts
INSERT OR IGNORE INTO supply_chain_visibility_weatherdisruptionalerts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WEA-0001", "Primary Operational WeatherDisruptionAlert 1", 24500.00, 150.0, "ACTIVE", "uuid-weatherdisruptionalert-01"),
    (2, "WEA-0002", "Secondary Corporate WeatherDisruptionAlert 2", 18200.50, 80.0, "ACTIVE", "uuid-weatherdisruptionalert-02"),
    (3, "WEA-0003", "Consolidated Branch WeatherDisruptionAlert 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-weatherdisruptionalert-03"),
    (4, "WEA-0004", "Enterprise Audited WeatherDisruptionAlert 4", 32800.00, 210.0, "ACTIVE", "uuid-weatherdisruptionalert-04"),
    (5, "WEA-0005", "Executive Strategic WeatherDisruptionAlert 5", 65000.00, 400.0, "ACTIVE", "uuid-weatherdisruptionalert-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_multimodalhandovernotes (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_multimodalhandovernotes_code ON supply_chain_visibility_multimodalhandovernotes(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_multimodalhandovernotes_org_status ON supply_chain_visibility_multimodalhandovernotes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_multimodalhandovernotes_priority ON supply_chain_visibility_multimodalhandovernotes(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_multimodalhandovernotes_created_at ON supply_chain_visibility_multimodalhandovernotes(created_at);

-- Operational seed data fixtures for supply_chain_visibility_multimodalhandovernotes
INSERT OR IGNORE INTO supply_chain_visibility_multimodalhandovernotes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MUL-0001", "Primary Operational MultimodalHandoverNote 1", 24500.00, 150.0, "ACTIVE", "uuid-multimodalhandovernote-01"),
    (2, "MUL-0002", "Secondary Corporate MultimodalHandoverNote 2", 18200.50, 80.0, "ACTIVE", "uuid-multimodalhandovernote-02"),
    (3, "MUL-0003", "Consolidated Branch MultimodalHandoverNote 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-multimodalhandovernote-03"),
    (4, "MUL-0004", "Enterprise Audited MultimodalHandoverNote 4", 32800.00, 210.0, "ACTIVE", "uuid-multimodalhandovernote-04"),
    (5, "MUL-0005", "Executive Strategic MultimodalHandoverNote 5", 65000.00, 400.0, "ACTIVE", "uuid-multimodalhandovernote-05");

CREATE TABLE IF NOT EXISTS supply_chain_visibility_trackandtraceauditlogs (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_trackandtraceauditlogs_code ON supply_chain_visibility_trackandtraceauditlogs(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_trackandtraceauditlogs_org_status ON supply_chain_visibility_trackandtraceauditlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_trackandtraceauditlogs_priority ON supply_chain_visibility_trackandtraceauditlogs(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_visibility_trackandtraceauditlogs_created_at ON supply_chain_visibility_trackandtraceauditlogs(created_at);

-- Operational seed data fixtures for supply_chain_visibility_trackandtraceauditlogs
INSERT OR IGNORE INTO supply_chain_visibility_trackandtraceauditlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TrackAndTraceAuditLog 1", 24500.00, 150.0, "ACTIVE", "uuid-trackandtraceauditlog-01"),
    (2, "TRA-0002", "Secondary Corporate TrackAndTraceAuditLog 2", 18200.50, 80.0, "ACTIVE", "uuid-trackandtraceauditlog-02"),
    (3, "TRA-0003", "Consolidated Branch TrackAndTraceAuditLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-trackandtraceauditlog-03"),
    (4, "TRA-0004", "Enterprise Audited TrackAndTraceAuditLog 4", 32800.00, 210.0, "ACTIVE", "uuid-trackandtraceauditlog-04"),
    (5, "TRA-0005", "Executive Strategic TrackAndTraceAuditLog 5", 65000.00, 400.0, "ACTIVE", "uuid-trackandtraceauditlog-05");

