-- SmartERP Enterprise Titan Migration 017: Fleet Telematics & Route Optimization DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS fleet_management_fleetvehicles (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetvehicles_code ON fleet_management_fleetvehicles(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetvehicles_org_status ON fleet_management_fleetvehicles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetvehicles_priority ON fleet_management_fleetvehicles(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetvehicles_created_at ON fleet_management_fleetvehicles(created_at);

-- Operational seed data fixtures for fleet_management_fleetvehicles
INSERT OR IGNORE INTO fleet_management_fleetvehicles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FLE-0001", "Primary Operational FleetVehicle 1", 24500.00, 150.0, "ACTIVE", "uuid-fleetvehicle-01"),
    (2, "FLE-0002", "Secondary Corporate FleetVehicle 2", 18200.50, 80.0, "ACTIVE", "uuid-fleetvehicle-02"),
    (3, "FLE-0003", "Consolidated Branch FleetVehicle 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fleetvehicle-03"),
    (4, "FLE-0004", "Enterprise Audited FleetVehicle 4", 32800.00, 210.0, "ACTIVE", "uuid-fleetvehicle-04"),
    (5, "FLE-0005", "Executive Strategic FleetVehicle 5", 65000.00, 400.0, "ACTIVE", "uuid-fleetvehicle-05");

CREATE TABLE IF NOT EXISTS fleet_management_driverprofiles (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_driverprofiles_code ON fleet_management_driverprofiles(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_driverprofiles_org_status ON fleet_management_driverprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_driverprofiles_priority ON fleet_management_driverprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_driverprofiles_created_at ON fleet_management_driverprofiles(created_at);

-- Operational seed data fixtures for fleet_management_driverprofiles
INSERT OR IGNORE INTO fleet_management_driverprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DRI-0001", "Primary Operational DriverProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-driverprofile-01"),
    (2, "DRI-0002", "Secondary Corporate DriverProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-driverprofile-02"),
    (3, "DRI-0003", "Consolidated Branch DriverProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-driverprofile-03"),
    (4, "DRI-0004", "Enterprise Audited DriverProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-driverprofile-04"),
    (5, "DRI-0005", "Executive Strategic DriverProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-driverprofile-05");

CREATE TABLE IF NOT EXISTS fleet_management_vehicletelematicslogs (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_vehicletelematicslogs_code ON fleet_management_vehicletelematicslogs(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_vehicletelematicslogs_org_status ON fleet_management_vehicletelematicslogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_vehicletelematicslogs_priority ON fleet_management_vehicletelematicslogs(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_vehicletelematicslogs_created_at ON fleet_management_vehicletelematicslogs(created_at);

-- Operational seed data fixtures for fleet_management_vehicletelematicslogs
INSERT OR IGNORE INTO fleet_management_vehicletelematicslogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEH-0001", "Primary Operational VehicleTelematicsLog 1", 24500.00, 150.0, "ACTIVE", "uuid-vehicletelematicslog-01"),
    (2, "VEH-0002", "Secondary Corporate VehicleTelematicsLog 2", 18200.50, 80.0, "ACTIVE", "uuid-vehicletelematicslog-02"),
    (3, "VEH-0003", "Consolidated Branch VehicleTelematicsLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vehicletelematicslog-03"),
    (4, "VEH-0004", "Enterprise Audited VehicleTelematicsLog 4", 32800.00, 210.0, "ACTIVE", "uuid-vehicletelematicslog-04"),
    (5, "VEH-0005", "Executive Strategic VehicleTelematicsLog 5", 65000.00, 400.0, "ACTIVE", "uuid-vehicletelematicslog-05");

CREATE TABLE IF NOT EXISTS fleet_management_odometerreadings (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_odometerreadings_code ON fleet_management_odometerreadings(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_odometerreadings_org_status ON fleet_management_odometerreadings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_odometerreadings_priority ON fleet_management_odometerreadings(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_odometerreadings_created_at ON fleet_management_odometerreadings(created_at);

-- Operational seed data fixtures for fleet_management_odometerreadings
INSERT OR IGNORE INTO fleet_management_odometerreadings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ODO-0001", "Primary Operational OdometerReading 1", 24500.00, 150.0, "ACTIVE", "uuid-odometerreading-01"),
    (2, "ODO-0002", "Secondary Corporate OdometerReading 2", 18200.50, 80.0, "ACTIVE", "uuid-odometerreading-02"),
    (3, "ODO-0003", "Consolidated Branch OdometerReading 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-odometerreading-03"),
    (4, "ODO-0004", "Enterprise Audited OdometerReading 4", 32800.00, 210.0, "ACTIVE", "uuid-odometerreading-04"),
    (5, "ODO-0005", "Executive Strategic OdometerReading 5", 65000.00, 400.0, "ACTIVE", "uuid-odometerreading-05");

CREATE TABLE IF NOT EXISTS fleet_management_fuelconsumptionlogs (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_fuelconsumptionlogs_code ON fleet_management_fuelconsumptionlogs(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fuelconsumptionlogs_org_status ON fleet_management_fuelconsumptionlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fuelconsumptionlogs_priority ON fleet_management_fuelconsumptionlogs(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fuelconsumptionlogs_created_at ON fleet_management_fuelconsumptionlogs(created_at);

-- Operational seed data fixtures for fleet_management_fuelconsumptionlogs
INSERT OR IGNORE INTO fleet_management_fuelconsumptionlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FUE-0001", "Primary Operational FuelConsumptionLog 1", 24500.00, 150.0, "ACTIVE", "uuid-fuelconsumptionlog-01"),
    (2, "FUE-0002", "Secondary Corporate FuelConsumptionLog 2", 18200.50, 80.0, "ACTIVE", "uuid-fuelconsumptionlog-02"),
    (3, "FUE-0003", "Consolidated Branch FuelConsumptionLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fuelconsumptionlog-03"),
    (4, "FUE-0004", "Enterprise Audited FuelConsumptionLog 4", 32800.00, 210.0, "ACTIVE", "uuid-fuelconsumptionlog-04"),
    (5, "FUE-0005", "Executive Strategic FuelConsumptionLog 5", 65000.00, 400.0, "ACTIVE", "uuid-fuelconsumptionlog-05");

CREATE TABLE IF NOT EXISTS fleet_management_fleetserviceschedules (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetserviceschedules_code ON fleet_management_fleetserviceschedules(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetserviceschedules_org_status ON fleet_management_fleetserviceschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetserviceschedules_priority ON fleet_management_fleetserviceschedules(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetserviceschedules_created_at ON fleet_management_fleetserviceschedules(created_at);

-- Operational seed data fixtures for fleet_management_fleetserviceschedules
INSERT OR IGNORE INTO fleet_management_fleetserviceschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FLE-0001", "Primary Operational FleetServiceSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-fleetserviceschedule-01"),
    (2, "FLE-0002", "Secondary Corporate FleetServiceSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-fleetserviceschedule-02"),
    (3, "FLE-0003", "Consolidated Branch FleetServiceSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fleetserviceschedule-03"),
    (4, "FLE-0004", "Enterprise Audited FleetServiceSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-fleetserviceschedule-04"),
    (5, "FLE-0005", "Executive Strategic FleetServiceSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-fleetserviceschedule-05");

CREATE TABLE IF NOT EXISTS fleet_management_repairworkorders (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_repairworkorders_code ON fleet_management_repairworkorders(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_repairworkorders_org_status ON fleet_management_repairworkorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_repairworkorders_priority ON fleet_management_repairworkorders(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_repairworkorders_created_at ON fleet_management_repairworkorders(created_at);

-- Operational seed data fixtures for fleet_management_repairworkorders
INSERT OR IGNORE INTO fleet_management_repairworkorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REP-0001", "Primary Operational RepairWorkOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-repairworkorder-01"),
    (2, "REP-0002", "Secondary Corporate RepairWorkOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-repairworkorder-02"),
    (3, "REP-0003", "Consolidated Branch RepairWorkOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-repairworkorder-03"),
    (4, "REP-0004", "Enterprise Audited RepairWorkOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-repairworkorder-04"),
    (5, "REP-0005", "Executive Strategic RepairWorkOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-repairworkorder-05");

CREATE TABLE IF NOT EXISTS fleet_management_tirewearlogs (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_tirewearlogs_code ON fleet_management_tirewearlogs(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_tirewearlogs_org_status ON fleet_management_tirewearlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_tirewearlogs_priority ON fleet_management_tirewearlogs(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_tirewearlogs_created_at ON fleet_management_tirewearlogs(created_at);

-- Operational seed data fixtures for fleet_management_tirewearlogs
INSERT OR IGNORE INTO fleet_management_tirewearlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIR-0001", "Primary Operational TireWearLog 1", 24500.00, 150.0, "ACTIVE", "uuid-tirewearlog-01"),
    (2, "TIR-0002", "Secondary Corporate TireWearLog 2", 18200.50, 80.0, "ACTIVE", "uuid-tirewearlog-02"),
    (3, "TIR-0003", "Consolidated Branch TireWearLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tirewearlog-03"),
    (4, "TIR-0004", "Enterprise Audited TireWearLog 4", 32800.00, 210.0, "ACTIVE", "uuid-tirewearlog-04"),
    (5, "TIR-0005", "Executive Strategic TireWearLog 5", 65000.00, 400.0, "ACTIVE", "uuid-tirewearlog-05");

CREATE TABLE IF NOT EXISTS fleet_management_inspectionpretrips (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_inspectionpretrips_code ON fleet_management_inspectionpretrips(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_inspectionpretrips_org_status ON fleet_management_inspectionpretrips(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_inspectionpretrips_priority ON fleet_management_inspectionpretrips(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_inspectionpretrips_created_at ON fleet_management_inspectionpretrips(created_at);

-- Operational seed data fixtures for fleet_management_inspectionpretrips
INSERT OR IGNORE INTO fleet_management_inspectionpretrips (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INS-0001", "Primary Operational InspectionPreTrip 1", 24500.00, 150.0, "ACTIVE", "uuid-inspectionpretrip-01"),
    (2, "INS-0002", "Secondary Corporate InspectionPreTrip 2", 18200.50, 80.0, "ACTIVE", "uuid-inspectionpretrip-02"),
    (3, "INS-0003", "Consolidated Branch InspectionPreTrip 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inspectionpretrip-03"),
    (4, "INS-0004", "Enterprise Audited InspectionPreTrip 4", 32800.00, 210.0, "ACTIVE", "uuid-inspectionpretrip-04"),
    (5, "INS-0005", "Executive Strategic InspectionPreTrip 5", 65000.00, 400.0, "ACTIVE", "uuid-inspectionpretrip-05");

CREATE TABLE IF NOT EXISTS fleet_management_routeoptimizationruns (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_routeoptimizationruns_code ON fleet_management_routeoptimizationruns(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_routeoptimizationruns_org_status ON fleet_management_routeoptimizationruns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_routeoptimizationruns_priority ON fleet_management_routeoptimizationruns(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_routeoptimizationruns_created_at ON fleet_management_routeoptimizationruns(created_at);

-- Operational seed data fixtures for fleet_management_routeoptimizationruns
INSERT OR IGNORE INTO fleet_management_routeoptimizationruns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ROU-0001", "Primary Operational RouteOptimizationRun 1", 24500.00, 150.0, "ACTIVE", "uuid-routeoptimizationrun-01"),
    (2, "ROU-0002", "Secondary Corporate RouteOptimizationRun 2", 18200.50, 80.0, "ACTIVE", "uuid-routeoptimizationrun-02"),
    (3, "ROU-0003", "Consolidated Branch RouteOptimizationRun 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-routeoptimizationrun-03"),
    (4, "ROU-0004", "Enterprise Audited RouteOptimizationRun 4", 32800.00, 210.0, "ACTIVE", "uuid-routeoptimizationrun-04"),
    (5, "ROU-0005", "Executive Strategic RouteOptimizationRun 5", 65000.00, 400.0, "ACTIVE", "uuid-routeoptimizationrun-05");

CREATE TABLE IF NOT EXISTS fleet_management_geofencezones (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_geofencezones_code ON fleet_management_geofencezones(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_geofencezones_org_status ON fleet_management_geofencezones(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_geofencezones_priority ON fleet_management_geofencezones(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_geofencezones_created_at ON fleet_management_geofencezones(created_at);

-- Operational seed data fixtures for fleet_management_geofencezones
INSERT OR IGNORE INTO fleet_management_geofencezones (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GEO-0001", "Primary Operational GeofenceZone 1", 24500.00, 150.0, "ACTIVE", "uuid-geofencezone-01"),
    (2, "GEO-0002", "Secondary Corporate GeofenceZone 2", 18200.50, 80.0, "ACTIVE", "uuid-geofencezone-02"),
    (3, "GEO-0003", "Consolidated Branch GeofenceZone 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-geofencezone-03"),
    (4, "GEO-0004", "Enterprise Audited GeofenceZone 4", 32800.00, 210.0, "ACTIVE", "uuid-geofencezone-04"),
    (5, "GEO-0005", "Executive Strategic GeofenceZone 5", 65000.00, 400.0, "ACTIVE", "uuid-geofencezone-05");

CREATE TABLE IF NOT EXISTS fleet_management_speedingviolations (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_speedingviolations_code ON fleet_management_speedingviolations(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_speedingviolations_org_status ON fleet_management_speedingviolations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_speedingviolations_priority ON fleet_management_speedingviolations(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_speedingviolations_created_at ON fleet_management_speedingviolations(created_at);

-- Operational seed data fixtures for fleet_management_speedingviolations
INSERT OR IGNORE INTO fleet_management_speedingviolations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SPE-0001", "Primary Operational SpeedingViolation 1", 24500.00, 150.0, "ACTIVE", "uuid-speedingviolation-01"),
    (2, "SPE-0002", "Secondary Corporate SpeedingViolation 2", 18200.50, 80.0, "ACTIVE", "uuid-speedingviolation-02"),
    (3, "SPE-0003", "Consolidated Branch SpeedingViolation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-speedingviolation-03"),
    (4, "SPE-0004", "Enterprise Audited SpeedingViolation 4", 32800.00, 210.0, "ACTIVE", "uuid-speedingviolation-04"),
    (5, "SPE-0005", "Executive Strategic SpeedingViolation 5", 65000.00, 400.0, "ACTIVE", "uuid-speedingviolation-05");

CREATE TABLE IF NOT EXISTS fleet_management_accidentreports (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_accidentreports_code ON fleet_management_accidentreports(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_accidentreports_org_status ON fleet_management_accidentreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_accidentreports_priority ON fleet_management_accidentreports(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_accidentreports_created_at ON fleet_management_accidentreports(created_at);

-- Operational seed data fixtures for fleet_management_accidentreports
INSERT OR IGNORE INTO fleet_management_accidentreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACC-0001", "Primary Operational AccidentReport 1", 24500.00, 150.0, "ACTIVE", "uuid-accidentreport-01"),
    (2, "ACC-0002", "Secondary Corporate AccidentReport 2", 18200.50, 80.0, "ACTIVE", "uuid-accidentreport-02"),
    (3, "ACC-0003", "Consolidated Branch AccidentReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-accidentreport-03"),
    (4, "ACC-0004", "Enterprise Audited AccidentReport 4", 32800.00, 210.0, "ACTIVE", "uuid-accidentreport-04"),
    (5, "ACC-0005", "Executive Strategic AccidentReport 5", 65000.00, 400.0, "ACTIVE", "uuid-accidentreport-05");

CREATE TABLE IF NOT EXISTS fleet_management_fleetinsuranceclaims (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetinsuranceclaims_code ON fleet_management_fleetinsuranceclaims(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetinsuranceclaims_org_status ON fleet_management_fleetinsuranceclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetinsuranceclaims_priority ON fleet_management_fleetinsuranceclaims(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_fleetinsuranceclaims_created_at ON fleet_management_fleetinsuranceclaims(created_at);

-- Operational seed data fixtures for fleet_management_fleetinsuranceclaims
INSERT OR IGNORE INTO fleet_management_fleetinsuranceclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FLE-0001", "Primary Operational FleetInsuranceClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-fleetinsuranceclaim-01"),
    (2, "FLE-0002", "Secondary Corporate FleetInsuranceClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-fleetinsuranceclaim-02"),
    (3, "FLE-0003", "Consolidated Branch FleetInsuranceClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fleetinsuranceclaim-03"),
    (4, "FLE-0004", "Enterprise Audited FleetInsuranceClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-fleetinsuranceclaim-04"),
    (5, "FLE-0005", "Executive Strategic FleetInsuranceClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-fleetinsuranceclaim-05");

CREATE TABLE IF NOT EXISTS fleet_management_permitlicenserenewals (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_permitlicenserenewals_code ON fleet_management_permitlicenserenewals(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_permitlicenserenewals_org_status ON fleet_management_permitlicenserenewals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_permitlicenserenewals_priority ON fleet_management_permitlicenserenewals(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_permitlicenserenewals_created_at ON fleet_management_permitlicenserenewals(created_at);

-- Operational seed data fixtures for fleet_management_permitlicenserenewals
INSERT OR IGNORE INTO fleet_management_permitlicenserenewals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PER-0001", "Primary Operational PermitLicenseRenewal 1", 24500.00, 150.0, "ACTIVE", "uuid-permitlicenserenewal-01"),
    (2, "PER-0002", "Secondary Corporate PermitLicenseRenewal 2", 18200.50, 80.0, "ACTIVE", "uuid-permitlicenserenewal-02"),
    (3, "PER-0003", "Consolidated Branch PermitLicenseRenewal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-permitlicenserenewal-03"),
    (4, "PER-0004", "Enterprise Audited PermitLicenseRenewal 4", 32800.00, 210.0, "ACTIVE", "uuid-permitlicenserenewal-04"),
    (5, "PER-0005", "Executive Strategic PermitLicenseRenewal 5", 65000.00, 400.0, "ACTIVE", "uuid-permitlicenserenewal-05");

CREATE TABLE IF NOT EXISTS fleet_management_depotstations (
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

CREATE INDEX IF NOT EXISTS idx_fleet_management_depotstations_code ON fleet_management_depotstations(code);
CREATE INDEX IF NOT EXISTS idx_fleet_management_depotstations_org_status ON fleet_management_depotstations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_fleet_management_depotstations_priority ON fleet_management_depotstations(priority);
CREATE INDEX IF NOT EXISTS idx_fleet_management_depotstations_created_at ON fleet_management_depotstations(created_at);

-- Operational seed data fixtures for fleet_management_depotstations
INSERT OR IGNORE INTO fleet_management_depotstations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DepotStation 1", 24500.00, 150.0, "ACTIVE", "uuid-depotstation-01"),
    (2, "DEP-0002", "Secondary Corporate DepotStation 2", 18200.50, 80.0, "ACTIVE", "uuid-depotstation-02"),
    (3, "DEP-0003", "Consolidated Branch DepotStation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-depotstation-03"),
    (4, "DEP-0004", "Enterprise Audited DepotStation 4", 32800.00, 210.0, "ACTIVE", "uuid-depotstation-04"),
    (5, "DEP-0005", "Executive Strategic DepotStation 5", 65000.00, 400.0, "ACTIVE", "uuid-depotstation-05");

