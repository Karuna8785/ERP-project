-- SmartERP Enterprise Titan Migration 001: Supply Chain & Fleet Logistics DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS logistics_shipments (
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

CREATE INDEX IF NOT EXISTS idx_logistics_shipments_code ON logistics_shipments(code);
CREATE INDEX IF NOT EXISTS idx_logistics_shipments_org_status ON logistics_shipments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_shipments_priority ON logistics_shipments(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_shipments_created_at ON logistics_shipments(created_at);

-- Operational seed data fixtures for logistics_shipments
INSERT OR IGNORE INTO logistics_shipments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational Shipment 1", 24500.00, 150.0, "ACTIVE", "uuid-shipment-01"),
    (2, "SHI-0002", "Secondary Corporate Shipment 2", 18200.50, 80.0, "ACTIVE", "uuid-shipment-02"),
    (3, "SHI-0003", "Consolidated Branch Shipment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shipment-03"),
    (4, "SHI-0004", "Enterprise Audited Shipment 4", 32800.00, 210.0, "ACTIVE", "uuid-shipment-04"),
    (5, "SHI-0005", "Executive Strategic Shipment 5", 65000.00, 400.0, "ACTIVE", "uuid-shipment-05");

CREATE TABLE IF NOT EXISTS logistics_carriers (
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

CREATE INDEX IF NOT EXISTS idx_logistics_carriers_code ON logistics_carriers(code);
CREATE INDEX IF NOT EXISTS idx_logistics_carriers_org_status ON logistics_carriers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_carriers_priority ON logistics_carriers(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_carriers_created_at ON logistics_carriers(created_at);

-- Operational seed data fixtures for logistics_carriers
INSERT OR IGNORE INTO logistics_carriers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAR-0001", "Primary Operational Carrier 1", 24500.00, 150.0, "ACTIVE", "uuid-carrier-01"),
    (2, "CAR-0002", "Secondary Corporate Carrier 2", 18200.50, 80.0, "ACTIVE", "uuid-carrier-02"),
    (3, "CAR-0003", "Consolidated Branch Carrier 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-carrier-03"),
    (4, "CAR-0004", "Enterprise Audited Carrier 4", 32800.00, 210.0, "ACTIVE", "uuid-carrier-04"),
    (5, "CAR-0005", "Executive Strategic Carrier 5", 65000.00, 400.0, "ACTIVE", "uuid-carrier-05");

CREATE TABLE IF NOT EXISTS logistics_routes (
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

CREATE INDEX IF NOT EXISTS idx_logistics_routes_code ON logistics_routes(code);
CREATE INDEX IF NOT EXISTS idx_logistics_routes_org_status ON logistics_routes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_routes_priority ON logistics_routes(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_routes_created_at ON logistics_routes(created_at);

-- Operational seed data fixtures for logistics_routes
INSERT OR IGNORE INTO logistics_routes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ROU-0001", "Primary Operational Route 1", 24500.00, 150.0, "ACTIVE", "uuid-route-01"),
    (2, "ROU-0002", "Secondary Corporate Route 2", 18200.50, 80.0, "ACTIVE", "uuid-route-02"),
    (3, "ROU-0003", "Consolidated Branch Route 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-route-03"),
    (4, "ROU-0004", "Enterprise Audited Route 4", 32800.00, 210.0, "ACTIVE", "uuid-route-04"),
    (5, "ROU-0005", "Executive Strategic Route 5", 65000.00, 400.0, "ACTIVE", "uuid-route-05");

CREATE TABLE IF NOT EXISTS logistics_vehicles (
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

CREATE INDEX IF NOT EXISTS idx_logistics_vehicles_code ON logistics_vehicles(code);
CREATE INDEX IF NOT EXISTS idx_logistics_vehicles_org_status ON logistics_vehicles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_vehicles_priority ON logistics_vehicles(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_vehicles_created_at ON logistics_vehicles(created_at);

-- Operational seed data fixtures for logistics_vehicles
INSERT OR IGNORE INTO logistics_vehicles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEH-0001", "Primary Operational Vehicle 1", 24500.00, 150.0, "ACTIVE", "uuid-vehicle-01"),
    (2, "VEH-0002", "Secondary Corporate Vehicle 2", 18200.50, 80.0, "ACTIVE", "uuid-vehicle-02"),
    (3, "VEH-0003", "Consolidated Branch Vehicle 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vehicle-03"),
    (4, "VEH-0004", "Enterprise Audited Vehicle 4", 32800.00, 210.0, "ACTIVE", "uuid-vehicle-04"),
    (5, "VEH-0005", "Executive Strategic Vehicle 5", 65000.00, 400.0, "ACTIVE", "uuid-vehicle-05");

CREATE TABLE IF NOT EXISTS logistics_drivers (
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

CREATE INDEX IF NOT EXISTS idx_logistics_drivers_code ON logistics_drivers(code);
CREATE INDEX IF NOT EXISTS idx_logistics_drivers_org_status ON logistics_drivers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_drivers_priority ON logistics_drivers(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_drivers_created_at ON logistics_drivers(created_at);

-- Operational seed data fixtures for logistics_drivers
INSERT OR IGNORE INTO logistics_drivers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DRI-0001", "Primary Operational Driver 1", 24500.00, 150.0, "ACTIVE", "uuid-driver-01"),
    (2, "DRI-0002", "Secondary Corporate Driver 2", 18200.50, 80.0, "ACTIVE", "uuid-driver-02"),
    (3, "DRI-0003", "Consolidated Branch Driver 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-driver-03"),
    (4, "DRI-0004", "Enterprise Audited Driver 4", 32800.00, 210.0, "ACTIVE", "uuid-driver-04"),
    (5, "DRI-0005", "Executive Strategic Driver 5", 65000.00, 400.0, "ACTIVE", "uuid-driver-05");

CREATE TABLE IF NOT EXISTS logistics_deliverystops (
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

CREATE INDEX IF NOT EXISTS idx_logistics_deliverystops_code ON logistics_deliverystops(code);
CREATE INDEX IF NOT EXISTS idx_logistics_deliverystops_org_status ON logistics_deliverystops(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_deliverystops_priority ON logistics_deliverystops(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_deliverystops_created_at ON logistics_deliverystops(created_at);

-- Operational seed data fixtures for logistics_deliverystops
INSERT OR IGNORE INTO logistics_deliverystops (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEL-0001", "Primary Operational DeliveryStop 1", 24500.00, 150.0, "ACTIVE", "uuid-deliverystop-01"),
    (2, "DEL-0002", "Secondary Corporate DeliveryStop 2", 18200.50, 80.0, "ACTIVE", "uuid-deliverystop-02"),
    (3, "DEL-0003", "Consolidated Branch DeliveryStop 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-deliverystop-03"),
    (4, "DEL-0004", "Enterprise Audited DeliveryStop 4", 32800.00, 210.0, "ACTIVE", "uuid-deliverystop-04"),
    (5, "DEL-0005", "Executive Strategic DeliveryStop 5", 65000.00, 400.0, "ACTIVE", "uuid-deliverystop-05");

CREATE TABLE IF NOT EXISTS logistics_freightbills (
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

CREATE INDEX IF NOT EXISTS idx_logistics_freightbills_code ON logistics_freightbills(code);
CREATE INDEX IF NOT EXISTS idx_logistics_freightbills_org_status ON logistics_freightbills(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_freightbills_priority ON logistics_freightbills(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_freightbills_created_at ON logistics_freightbills(created_at);

-- Operational seed data fixtures for logistics_freightbills
INSERT OR IGNORE INTO logistics_freightbills (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FRE-0001", "Primary Operational FreightBill 1", 24500.00, 150.0, "ACTIVE", "uuid-freightbill-01"),
    (2, "FRE-0002", "Secondary Corporate FreightBill 2", 18200.50, 80.0, "ACTIVE", "uuid-freightbill-02"),
    (3, "FRE-0003", "Consolidated Branch FreightBill 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-freightbill-03"),
    (4, "FRE-0004", "Enterprise Audited FreightBill 4", 32800.00, 210.0, "ACTIVE", "uuid-freightbill-04"),
    (5, "FRE-0005", "Executive Strategic FreightBill 5", 65000.00, 400.0, "ACTIVE", "uuid-freightbill-05");

CREATE TABLE IF NOT EXISTS logistics_waybills (
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

CREATE INDEX IF NOT EXISTS idx_logistics_waybills_code ON logistics_waybills(code);
CREATE INDEX IF NOT EXISTS idx_logistics_waybills_org_status ON logistics_waybills(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_waybills_priority ON logistics_waybills(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_waybills_created_at ON logistics_waybills(created_at);

-- Operational seed data fixtures for logistics_waybills
INSERT OR IGNORE INTO logistics_waybills (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAY-0001", "Primary Operational Waybill 1", 24500.00, 150.0, "ACTIVE", "uuid-waybill-01"),
    (2, "WAY-0002", "Secondary Corporate Waybill 2", 18200.50, 80.0, "ACTIVE", "uuid-waybill-02"),
    (3, "WAY-0003", "Consolidated Branch Waybill 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-waybill-03"),
    (4, "WAY-0004", "Enterprise Audited Waybill 4", 32800.00, 210.0, "ACTIVE", "uuid-waybill-04"),
    (5, "WAY-0005", "Executive Strategic Waybill 5", 65000.00, 400.0, "ACTIVE", "uuid-waybill-05");

CREATE TABLE IF NOT EXISTS logistics_containers (
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

CREATE INDEX IF NOT EXISTS idx_logistics_containers_code ON logistics_containers(code);
CREATE INDEX IF NOT EXISTS idx_logistics_containers_org_status ON logistics_containers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_containers_priority ON logistics_containers(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_containers_created_at ON logistics_containers(created_at);

-- Operational seed data fixtures for logistics_containers
INSERT OR IGNORE INTO logistics_containers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational Container 1", 24500.00, 150.0, "ACTIVE", "uuid-container-01"),
    (2, "CON-0002", "Secondary Corporate Container 2", 18200.50, 80.0, "ACTIVE", "uuid-container-02"),
    (3, "CON-0003", "Consolidated Branch Container 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-container-03"),
    (4, "CON-0004", "Enterprise Audited Container 4", 32800.00, 210.0, "ACTIVE", "uuid-container-04"),
    (5, "CON-0005", "Executive Strategic Container 5", 65000.00, 400.0, "ACTIVE", "uuid-container-05");

CREATE TABLE IF NOT EXISTS logistics_dispatchorders (
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

CREATE INDEX IF NOT EXISTS idx_logistics_dispatchorders_code ON logistics_dispatchorders(code);
CREATE INDEX IF NOT EXISTS idx_logistics_dispatchorders_org_status ON logistics_dispatchorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_dispatchorders_priority ON logistics_dispatchorders(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_dispatchorders_created_at ON logistics_dispatchorders(created_at);

-- Operational seed data fixtures for logistics_dispatchorders
INSERT OR IGNORE INTO logistics_dispatchorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DispatchOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-dispatchorder-01"),
    (2, "DIS-0002", "Secondary Corporate DispatchOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-dispatchorder-02"),
    (3, "DIS-0003", "Consolidated Branch DispatchOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dispatchorder-03"),
    (4, "DIS-0004", "Enterprise Audited DispatchOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-dispatchorder-04"),
    (5, "DIS-0005", "Executive Strategic DispatchOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-dispatchorder-05");

CREATE TABLE IF NOT EXISTS logistics_fuellogs (
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

CREATE INDEX IF NOT EXISTS idx_logistics_fuellogs_code ON logistics_fuellogs(code);
CREATE INDEX IF NOT EXISTS idx_logistics_fuellogs_org_status ON logistics_fuellogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_fuellogs_priority ON logistics_fuellogs(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_fuellogs_created_at ON logistics_fuellogs(created_at);

-- Operational seed data fixtures for logistics_fuellogs
INSERT OR IGNORE INTO logistics_fuellogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FUE-0001", "Primary Operational FuelLog 1", 24500.00, 150.0, "ACTIVE", "uuid-fuellog-01"),
    (2, "FUE-0002", "Secondary Corporate FuelLog 2", 18200.50, 80.0, "ACTIVE", "uuid-fuellog-02"),
    (3, "FUE-0003", "Consolidated Branch FuelLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fuellog-03"),
    (4, "FUE-0004", "Enterprise Audited FuelLog 4", 32800.00, 210.0, "ACTIVE", "uuid-fuellog-04"),
    (5, "FUE-0005", "Executive Strategic FuelLog 5", 65000.00, 400.0, "ACTIVE", "uuid-fuellog-05");

CREATE TABLE IF NOT EXISTS logistics_tollreceipts (
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

CREATE INDEX IF NOT EXISTS idx_logistics_tollreceipts_code ON logistics_tollreceipts(code);
CREATE INDEX IF NOT EXISTS idx_logistics_tollreceipts_org_status ON logistics_tollreceipts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_tollreceipts_priority ON logistics_tollreceipts(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_tollreceipts_created_at ON logistics_tollreceipts(created_at);

-- Operational seed data fixtures for logistics_tollreceipts
INSERT OR IGNORE INTO logistics_tollreceipts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TOL-0001", "Primary Operational TollReceipt 1", 24500.00, 150.0, "ACTIVE", "uuid-tollreceipt-01"),
    (2, "TOL-0002", "Secondary Corporate TollReceipt 2", 18200.50, 80.0, "ACTIVE", "uuid-tollreceipt-02"),
    (3, "TOL-0003", "Consolidated Branch TollReceipt 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tollreceipt-03"),
    (4, "TOL-0004", "Enterprise Audited TollReceipt 4", 32800.00, 210.0, "ACTIVE", "uuid-tollreceipt-04"),
    (5, "TOL-0005", "Executive Strategic TollReceipt 5", 65000.00, 400.0, "ACTIVE", "uuid-tollreceipt-05");

CREATE TABLE IF NOT EXISTS logistics_maintenancelogs (
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

CREATE INDEX IF NOT EXISTS idx_logistics_maintenancelogs_code ON logistics_maintenancelogs(code);
CREATE INDEX IF NOT EXISTS idx_logistics_maintenancelogs_org_status ON logistics_maintenancelogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_maintenancelogs_priority ON logistics_maintenancelogs(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_maintenancelogs_created_at ON logistics_maintenancelogs(created_at);

-- Operational seed data fixtures for logistics_maintenancelogs
INSERT OR IGNORE INTO logistics_maintenancelogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAI-0001", "Primary Operational MaintenanceLog 1", 24500.00, 150.0, "ACTIVE", "uuid-maintenancelog-01"),
    (2, "MAI-0002", "Secondary Corporate MaintenanceLog 2", 18200.50, 80.0, "ACTIVE", "uuid-maintenancelog-02"),
    (3, "MAI-0003", "Consolidated Branch MaintenanceLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-maintenancelog-03"),
    (4, "MAI-0004", "Enterprise Audited MaintenanceLog 4", 32800.00, 210.0, "ACTIVE", "uuid-maintenancelog-04"),
    (5, "MAI-0005", "Executive Strategic MaintenanceLog 5", 65000.00, 400.0, "ACTIVE", "uuid-maintenancelog-05");

CREATE TABLE IF NOT EXISTS logistics_gpspings (
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

CREATE INDEX IF NOT EXISTS idx_logistics_gpspings_code ON logistics_gpspings(code);
CREATE INDEX IF NOT EXISTS idx_logistics_gpspings_org_status ON logistics_gpspings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_gpspings_priority ON logistics_gpspings(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_gpspings_created_at ON logistics_gpspings(created_at);

-- Operational seed data fixtures for logistics_gpspings
INSERT OR IGNORE INTO logistics_gpspings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GPS-0001", "Primary Operational GPSPing 1", 24500.00, 150.0, "ACTIVE", "uuid-gpsping-01"),
    (2, "GPS-0002", "Secondary Corporate GPSPing 2", 18200.50, 80.0, "ACTIVE", "uuid-gpsping-02"),
    (3, "GPS-0003", "Consolidated Branch GPSPing 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-gpsping-03"),
    (4, "GPS-0004", "Enterprise Audited GPSPing 4", 32800.00, 210.0, "ACTIVE", "uuid-gpsping-04"),
    (5, "GPS-0005", "Executive Strategic GPSPing 5", 65000.00, 400.0, "ACTIVE", "uuid-gpsping-05");

CREATE TABLE IF NOT EXISTS logistics_dockschedules (
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

CREATE INDEX IF NOT EXISTS idx_logistics_dockschedules_code ON logistics_dockschedules(code);
CREATE INDEX IF NOT EXISTS idx_logistics_dockschedules_org_status ON logistics_dockschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_dockschedules_priority ON logistics_dockschedules(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_dockschedules_created_at ON logistics_dockschedules(created_at);

-- Operational seed data fixtures for logistics_dockschedules
INSERT OR IGNORE INTO logistics_dockschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DockSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-dockschedule-01"),
    (2, "DOC-0002", "Secondary Corporate DockSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-dockschedule-02"),
    (3, "DOC-0003", "Consolidated Branch DockSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dockschedule-03"),
    (4, "DOC-0004", "Enterprise Audited DockSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-dockschedule-04"),
    (5, "DOC-0005", "Executive Strategic DockSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-dockschedule-05");

CREATE TABLE IF NOT EXISTS logistics_customsdocs (
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

CREATE INDEX IF NOT EXISTS idx_logistics_customsdocs_code ON logistics_customsdocs(code);
CREATE INDEX IF NOT EXISTS idx_logistics_customsdocs_org_status ON logistics_customsdocs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_logistics_customsdocs_priority ON logistics_customsdocs(priority);
CREATE INDEX IF NOT EXISTS idx_logistics_customsdocs_created_at ON logistics_customsdocs(created_at);

-- Operational seed data fixtures for logistics_customsdocs
INSERT OR IGNORE INTO logistics_customsdocs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomsDoc 1", 24500.00, 150.0, "ACTIVE", "uuid-customsdoc-01"),
    (2, "CUS-0002", "Secondary Corporate CustomsDoc 2", 18200.50, 80.0, "ACTIVE", "uuid-customsdoc-02"),
    (3, "CUS-0003", "Consolidated Branch CustomsDoc 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customsdoc-03"),
    (4, "CUS-0004", "Enterprise Audited CustomsDoc 4", 32800.00, 210.0, "ACTIVE", "uuid-customsdoc-04"),
    (5, "CUS-0005", "Executive Strategic CustomsDoc 5", 65000.00, 400.0, "ACTIVE", "uuid-customsdoc-05");

