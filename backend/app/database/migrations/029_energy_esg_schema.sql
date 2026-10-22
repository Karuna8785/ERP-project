-- SmartERP Enterprise Titan Migration 029: Corporate Sustainability & ESG Energy Tracking DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS energy_esg_energymeterlogs (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_energymeterlogs_code ON energy_esg_energymeterlogs(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_energymeterlogs_org_status ON energy_esg_energymeterlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_energymeterlogs_priority ON energy_esg_energymeterlogs(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_energymeterlogs_created_at ON energy_esg_energymeterlogs(created_at);

-- Operational seed data fixtures for energy_esg_energymeterlogs
INSERT OR IGNORE INTO energy_esg_energymeterlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ENE-0001", "Primary Operational EnergyMeterLog 1", 24500.00, 150.0, "ACTIVE", "uuid-energymeterlog-01"),
    (2, "ENE-0002", "Secondary Corporate EnergyMeterLog 2", 18200.50, 80.0, "ACTIVE", "uuid-energymeterlog-02"),
    (3, "ENE-0003", "Consolidated Branch EnergyMeterLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-energymeterlog-03"),
    (4, "ENE-0004", "Enterprise Audited EnergyMeterLog 4", 32800.00, 210.0, "ACTIVE", "uuid-energymeterlog-04"),
    (5, "ENE-0005", "Executive Strategic EnergyMeterLog 5", 65000.00, 400.0, "ACTIVE", "uuid-energymeterlog-05");

CREATE TABLE IF NOT EXISTS energy_esg_carbonemissionrecords (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_carbonemissionrecords_code ON energy_esg_carbonemissionrecords(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_carbonemissionrecords_org_status ON energy_esg_carbonemissionrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_carbonemissionrecords_priority ON energy_esg_carbonemissionrecords(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_carbonemissionrecords_created_at ON energy_esg_carbonemissionrecords(created_at);

-- Operational seed data fixtures for energy_esg_carbonemissionrecords
INSERT OR IGNORE INTO energy_esg_carbonemissionrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAR-0001", "Primary Operational CarbonEmissionRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-carbonemissionrecord-01"),
    (2, "CAR-0002", "Secondary Corporate CarbonEmissionRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-carbonemissionrecord-02"),
    (3, "CAR-0003", "Consolidated Branch CarbonEmissionRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-carbonemissionrecord-03"),
    (4, "CAR-0004", "Enterprise Audited CarbonEmissionRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-carbonemissionrecord-04"),
    (5, "CAR-0005", "Executive Strategic CarbonEmissionRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-carbonemissionrecord-05");

CREATE TABLE IF NOT EXISTS energy_esg_renewablecredits (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_renewablecredits_code ON energy_esg_renewablecredits(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_renewablecredits_org_status ON energy_esg_renewablecredits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_renewablecredits_priority ON energy_esg_renewablecredits(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_renewablecredits_created_at ON energy_esg_renewablecredits(created_at);

-- Operational seed data fixtures for energy_esg_renewablecredits
INSERT OR IGNORE INTO energy_esg_renewablecredits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REN-0001", "Primary Operational RenewableCredit 1", 24500.00, 150.0, "ACTIVE", "uuid-renewablecredit-01"),
    (2, "REN-0002", "Secondary Corporate RenewableCredit 2", 18200.50, 80.0, "ACTIVE", "uuid-renewablecredit-02"),
    (3, "REN-0003", "Consolidated Branch RenewableCredit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-renewablecredit-03"),
    (4, "REN-0004", "Enterprise Audited RenewableCredit 4", 32800.00, 210.0, "ACTIVE", "uuid-renewablecredit-04"),
    (5, "REN-0005", "Executive Strategic RenewableCredit 5", 65000.00, 400.0, "ACTIVE", "uuid-renewablecredit-05");

CREATE TABLE IF NOT EXISTS energy_esg_waterconsumptionlogs (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_waterconsumptionlogs_code ON energy_esg_waterconsumptionlogs(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_waterconsumptionlogs_org_status ON energy_esg_waterconsumptionlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_waterconsumptionlogs_priority ON energy_esg_waterconsumptionlogs(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_waterconsumptionlogs_created_at ON energy_esg_waterconsumptionlogs(created_at);

-- Operational seed data fixtures for energy_esg_waterconsumptionlogs
INSERT OR IGNORE INTO energy_esg_waterconsumptionlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAT-0001", "Primary Operational WaterConsumptionLog 1", 24500.00, 150.0, "ACTIVE", "uuid-waterconsumptionlog-01"),
    (2, "WAT-0002", "Secondary Corporate WaterConsumptionLog 2", 18200.50, 80.0, "ACTIVE", "uuid-waterconsumptionlog-02"),
    (3, "WAT-0003", "Consolidated Branch WaterConsumptionLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-waterconsumptionlog-03"),
    (4, "WAT-0004", "Enterprise Audited WaterConsumptionLog 4", 32800.00, 210.0, "ACTIVE", "uuid-waterconsumptionlog-04"),
    (5, "WAT-0005", "Executive Strategic WaterConsumptionLog 5", 65000.00, 400.0, "ACTIVE", "uuid-waterconsumptionlog-05");

CREATE TABLE IF NOT EXISTS energy_esg_wastedisposalmanifests (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_wastedisposalmanifests_code ON energy_esg_wastedisposalmanifests(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_wastedisposalmanifests_org_status ON energy_esg_wastedisposalmanifests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_wastedisposalmanifests_priority ON energy_esg_wastedisposalmanifests(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_wastedisposalmanifests_created_at ON energy_esg_wastedisposalmanifests(created_at);

-- Operational seed data fixtures for energy_esg_wastedisposalmanifests
INSERT OR IGNORE INTO energy_esg_wastedisposalmanifests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAS-0001", "Primary Operational WasteDisposalManifest 1", 24500.00, 150.0, "ACTIVE", "uuid-wastedisposalmanifest-01"),
    (2, "WAS-0002", "Secondary Corporate WasteDisposalManifest 2", 18200.50, 80.0, "ACTIVE", "uuid-wastedisposalmanifest-02"),
    (3, "WAS-0003", "Consolidated Branch WasteDisposalManifest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-wastedisposalmanifest-03"),
    (4, "WAS-0004", "Enterprise Audited WasteDisposalManifest 4", 32800.00, 210.0, "ACTIVE", "uuid-wastedisposalmanifest-04"),
    (5, "WAS-0005", "Executive Strategic WasteDisposalManifest 5", 65000.00, 400.0, "ACTIVE", "uuid-wastedisposalmanifest-05");

CREATE TABLE IF NOT EXISTS energy_esg_hazardousmaterialtracks (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_hazardousmaterialtracks_code ON energy_esg_hazardousmaterialtracks(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_hazardousmaterialtracks_org_status ON energy_esg_hazardousmaterialtracks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_hazardousmaterialtracks_priority ON energy_esg_hazardousmaterialtracks(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_hazardousmaterialtracks_created_at ON energy_esg_hazardousmaterialtracks(created_at);

-- Operational seed data fixtures for energy_esg_hazardousmaterialtracks
INSERT OR IGNORE INTO energy_esg_hazardousmaterialtracks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HAZ-0001", "Primary Operational HazardousMaterialTrack 1", 24500.00, 150.0, "ACTIVE", "uuid-hazardousmaterialtrack-01"),
    (2, "HAZ-0002", "Secondary Corporate HazardousMaterialTrack 2", 18200.50, 80.0, "ACTIVE", "uuid-hazardousmaterialtrack-02"),
    (3, "HAZ-0003", "Consolidated Branch HazardousMaterialTrack 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hazardousmaterialtrack-03"),
    (4, "HAZ-0004", "Enterprise Audited HazardousMaterialTrack 4", 32800.00, 210.0, "ACTIVE", "uuid-hazardousmaterialtrack-04"),
    (5, "HAZ-0005", "Executive Strategic HazardousMaterialTrack 5", 65000.00, 400.0, "ACTIVE", "uuid-hazardousmaterialtrack-05");

CREATE TABLE IF NOT EXISTS energy_esg_esgcompliancemetrics (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_esgcompliancemetrics_code ON energy_esg_esgcompliancemetrics(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_esgcompliancemetrics_org_status ON energy_esg_esgcompliancemetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_esgcompliancemetrics_priority ON energy_esg_esgcompliancemetrics(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_esgcompliancemetrics_created_at ON energy_esg_esgcompliancemetrics(created_at);

-- Operational seed data fixtures for energy_esg_esgcompliancemetrics
INSERT OR IGNORE INTO energy_esg_esgcompliancemetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ESG-0001", "Primary Operational ESGComplianceMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-esgcompliancemetric-01"),
    (2, "ESG-0002", "Secondary Corporate ESGComplianceMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-esgcompliancemetric-02"),
    (3, "ESG-0003", "Consolidated Branch ESGComplianceMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-esgcompliancemetric-03"),
    (4, "ESG-0004", "Enterprise Audited ESGComplianceMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-esgcompliancemetric-04"),
    (5, "ESG-0005", "Executive Strategic ESGComplianceMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-esgcompliancemetric-05");

CREATE TABLE IF NOT EXISTS energy_esg_sustainabilityinitiatives (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_sustainabilityinitiatives_code ON energy_esg_sustainabilityinitiatives(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_sustainabilityinitiatives_org_status ON energy_esg_sustainabilityinitiatives(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_sustainabilityinitiatives_priority ON energy_esg_sustainabilityinitiatives(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_sustainabilityinitiatives_created_at ON energy_esg_sustainabilityinitiatives(created_at);

-- Operational seed data fixtures for energy_esg_sustainabilityinitiatives
INSERT OR IGNORE INTO energy_esg_sustainabilityinitiatives (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUS-0001", "Primary Operational SustainabilityInitiative 1", 24500.00, 150.0, "ACTIVE", "uuid-sustainabilityinitiative-01"),
    (2, "SUS-0002", "Secondary Corporate SustainabilityInitiative 2", 18200.50, 80.0, "ACTIVE", "uuid-sustainabilityinitiative-02"),
    (3, "SUS-0003", "Consolidated Branch SustainabilityInitiative 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sustainabilityinitiative-03"),
    (4, "SUS-0004", "Enterprise Audited SustainabilityInitiative 4", 32800.00, 210.0, "ACTIVE", "uuid-sustainabilityinitiative-04"),
    (5, "SUS-0005", "Executive Strategic SustainabilityInitiative 5", 65000.00, 400.0, "ACTIVE", "uuid-sustainabilityinitiative-05");

CREATE TABLE IF NOT EXISTS energy_esg_greenhousegasscope1s (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope1s_code ON energy_esg_greenhousegasscope1s(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope1s_org_status ON energy_esg_greenhousegasscope1s(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope1s_priority ON energy_esg_greenhousegasscope1s(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope1s_created_at ON energy_esg_greenhousegasscope1s(created_at);

-- Operational seed data fixtures for energy_esg_greenhousegasscope1s
INSERT OR IGNORE INTO energy_esg_greenhousegasscope1s (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GRE-0001", "Primary Operational GreenhouseGasScope1 1", 24500.00, 150.0, "ACTIVE", "uuid-greenhousegasscope1-01"),
    (2, "GRE-0002", "Secondary Corporate GreenhouseGasScope1 2", 18200.50, 80.0, "ACTIVE", "uuid-greenhousegasscope1-02"),
    (3, "GRE-0003", "Consolidated Branch GreenhouseGasScope1 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-greenhousegasscope1-03"),
    (4, "GRE-0004", "Enterprise Audited GreenhouseGasScope1 4", 32800.00, 210.0, "ACTIVE", "uuid-greenhousegasscope1-04"),
    (5, "GRE-0005", "Executive Strategic GreenhouseGasScope1 5", 65000.00, 400.0, "ACTIVE", "uuid-greenhousegasscope1-05");

CREATE TABLE IF NOT EXISTS energy_esg_greenhousegasscope2s (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope2s_code ON energy_esg_greenhousegasscope2s(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope2s_org_status ON energy_esg_greenhousegasscope2s(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope2s_priority ON energy_esg_greenhousegasscope2s(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope2s_created_at ON energy_esg_greenhousegasscope2s(created_at);

-- Operational seed data fixtures for energy_esg_greenhousegasscope2s
INSERT OR IGNORE INTO energy_esg_greenhousegasscope2s (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GRE-0001", "Primary Operational GreenhouseGasScope2 1", 24500.00, 150.0, "ACTIVE", "uuid-greenhousegasscope2-01"),
    (2, "GRE-0002", "Secondary Corporate GreenhouseGasScope2 2", 18200.50, 80.0, "ACTIVE", "uuid-greenhousegasscope2-02"),
    (3, "GRE-0003", "Consolidated Branch GreenhouseGasScope2 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-greenhousegasscope2-03"),
    (4, "GRE-0004", "Enterprise Audited GreenhouseGasScope2 4", 32800.00, 210.0, "ACTIVE", "uuid-greenhousegasscope2-04"),
    (5, "GRE-0005", "Executive Strategic GreenhouseGasScope2 5", 65000.00, 400.0, "ACTIVE", "uuid-greenhousegasscope2-05");

CREATE TABLE IF NOT EXISTS energy_esg_greenhousegasscope3s (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope3s_code ON energy_esg_greenhousegasscope3s(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope3s_org_status ON energy_esg_greenhousegasscope3s(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope3s_priority ON energy_esg_greenhousegasscope3s(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_greenhousegasscope3s_created_at ON energy_esg_greenhousegasscope3s(created_at);

-- Operational seed data fixtures for energy_esg_greenhousegasscope3s
INSERT OR IGNORE INTO energy_esg_greenhousegasscope3s (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GRE-0001", "Primary Operational GreenhouseGasScope3 1", 24500.00, 150.0, "ACTIVE", "uuid-greenhousegasscope3-01"),
    (2, "GRE-0002", "Secondary Corporate GreenhouseGasScope3 2", 18200.50, 80.0, "ACTIVE", "uuid-greenhousegasscope3-02"),
    (3, "GRE-0003", "Consolidated Branch GreenhouseGasScope3 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-greenhousegasscope3-03"),
    (4, "GRE-0004", "Enterprise Audited GreenhouseGasScope3 4", 32800.00, 210.0, "ACTIVE", "uuid-greenhousegasscope3-04"),
    (5, "GRE-0005", "Executive Strategic GreenhouseGasScope3 5", 65000.00, 400.0, "ACTIVE", "uuid-greenhousegasscope3-05");

CREATE TABLE IF NOT EXISTS energy_esg_energyauditreports (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_energyauditreports_code ON energy_esg_energyauditreports(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_energyauditreports_org_status ON energy_esg_energyauditreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_energyauditreports_priority ON energy_esg_energyauditreports(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_energyauditreports_created_at ON energy_esg_energyauditreports(created_at);

-- Operational seed data fixtures for energy_esg_energyauditreports
INSERT OR IGNORE INTO energy_esg_energyauditreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ENE-0001", "Primary Operational EnergyAuditReport 1", 24500.00, 150.0, "ACTIVE", "uuid-energyauditreport-01"),
    (2, "ENE-0002", "Secondary Corporate EnergyAuditReport 2", 18200.50, 80.0, "ACTIVE", "uuid-energyauditreport-02"),
    (3, "ENE-0003", "Consolidated Branch EnergyAuditReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-energyauditreport-03"),
    (4, "ENE-0004", "Enterprise Audited EnergyAuditReport 4", 32800.00, 210.0, "ACTIVE", "uuid-energyauditreport-04"),
    (5, "ENE-0005", "Executive Strategic EnergyAuditReport 5", 65000.00, 400.0, "ACTIVE", "uuid-energyauditreport-05");

CREATE TABLE IF NOT EXISTS energy_esg_vendoresgscorecards (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_vendoresgscorecards_code ON energy_esg_vendoresgscorecards(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_vendoresgscorecards_org_status ON energy_esg_vendoresgscorecards(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_vendoresgscorecards_priority ON energy_esg_vendoresgscorecards(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_vendoresgscorecards_created_at ON energy_esg_vendoresgscorecards(created_at);

-- Operational seed data fixtures for energy_esg_vendoresgscorecards
INSERT OR IGNORE INTO energy_esg_vendoresgscorecards (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorESGScorecard 1", 24500.00, 150.0, "ACTIVE", "uuid-vendoresgscorecard-01"),
    (2, "VEN-0002", "Secondary Corporate VendorESGScorecard 2", 18200.50, 80.0, "ACTIVE", "uuid-vendoresgscorecard-02"),
    (3, "VEN-0003", "Consolidated Branch VendorESGScorecard 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendoresgscorecard-03"),
    (4, "VEN-0004", "Enterprise Audited VendorESGScorecard 4", 32800.00, 210.0, "ACTIVE", "uuid-vendoresgscorecard-04"),
    (5, "VEN-0005", "Executive Strategic VendorESGScorecard 5", 65000.00, 400.0, "ACTIVE", "uuid-vendoresgscorecard-05");

CREATE TABLE IF NOT EXISTS energy_esg_regulatorycarbonfilings (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_regulatorycarbonfilings_code ON energy_esg_regulatorycarbonfilings(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_regulatorycarbonfilings_org_status ON energy_esg_regulatorycarbonfilings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_regulatorycarbonfilings_priority ON energy_esg_regulatorycarbonfilings(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_regulatorycarbonfilings_created_at ON energy_esg_regulatorycarbonfilings(created_at);

-- Operational seed data fixtures for energy_esg_regulatorycarbonfilings
INSERT OR IGNORE INTO energy_esg_regulatorycarbonfilings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REG-0001", "Primary Operational RegulatoryCarbonFiling 1", 24500.00, 150.0, "ACTIVE", "uuid-regulatorycarbonfiling-01"),
    (2, "REG-0002", "Secondary Corporate RegulatoryCarbonFiling 2", 18200.50, 80.0, "ACTIVE", "uuid-regulatorycarbonfiling-02"),
    (3, "REG-0003", "Consolidated Branch RegulatoryCarbonFiling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-regulatorycarbonfiling-03"),
    (4, "REG-0004", "Enterprise Audited RegulatoryCarbonFiling 4", 32800.00, 210.0, "ACTIVE", "uuid-regulatorycarbonfiling-04"),
    (5, "REG-0005", "Executive Strategic RegulatoryCarbonFiling 5", 65000.00, 400.0, "ACTIVE", "uuid-regulatorycarbonfiling-05");

CREATE TABLE IF NOT EXISTS energy_esg_offsetcertificates (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_offsetcertificates_code ON energy_esg_offsetcertificates(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_offsetcertificates_org_status ON energy_esg_offsetcertificates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_offsetcertificates_priority ON energy_esg_offsetcertificates(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_offsetcertificates_created_at ON energy_esg_offsetcertificates(created_at);

-- Operational seed data fixtures for energy_esg_offsetcertificates
INSERT OR IGNORE INTO energy_esg_offsetcertificates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OFF-0001", "Primary Operational OffsetCertificate 1", 24500.00, 150.0, "ACTIVE", "uuid-offsetcertificate-01"),
    (2, "OFF-0002", "Secondary Corporate OffsetCertificate 2", 18200.50, 80.0, "ACTIVE", "uuid-offsetcertificate-02"),
    (3, "OFF-0003", "Consolidated Branch OffsetCertificate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-offsetcertificate-03"),
    (4, "OFF-0004", "Enterprise Audited OffsetCertificate 4", 32800.00, 210.0, "ACTIVE", "uuid-offsetcertificate-04"),
    (5, "OFF-0005", "Executive Strategic OffsetCertificate 5", 65000.00, 400.0, "ACTIVE", "uuid-offsetcertificate-05");

CREATE TABLE IF NOT EXISTS energy_esg_communityimpactprojects (
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

CREATE INDEX IF NOT EXISTS idx_energy_esg_communityimpactprojects_code ON energy_esg_communityimpactprojects(code);
CREATE INDEX IF NOT EXISTS idx_energy_esg_communityimpactprojects_org_status ON energy_esg_communityimpactprojects(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_energy_esg_communityimpactprojects_priority ON energy_esg_communityimpactprojects(priority);
CREATE INDEX IF NOT EXISTS idx_energy_esg_communityimpactprojects_created_at ON energy_esg_communityimpactprojects(created_at);

-- Operational seed data fixtures for energy_esg_communityimpactprojects
INSERT OR IGNORE INTO energy_esg_communityimpactprojects (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CommunityImpactProject 1", 24500.00, 150.0, "ACTIVE", "uuid-communityimpactproject-01"),
    (2, "COM-0002", "Secondary Corporate CommunityImpactProject 2", 18200.50, 80.0, "ACTIVE", "uuid-communityimpactproject-02"),
    (3, "COM-0003", "Consolidated Branch CommunityImpactProject 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-communityimpactproject-03"),
    (4, "COM-0004", "Enterprise Audited CommunityImpactProject 4", 32800.00, 210.0, "ACTIVE", "uuid-communityimpactproject-04"),
    (5, "COM-0005", "Executive Strategic CommunityImpactProject 5", 65000.00, 400.0, "ACTIVE", "uuid-communityimpactproject-05");

