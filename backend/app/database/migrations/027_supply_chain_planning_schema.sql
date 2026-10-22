-- SmartERP Enterprise Titan Migration 027: Sales & Operations Planning (S&OP) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS supply_chain_planning_demandforecastplans (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_demandforecastplans_code ON supply_chain_planning_demandforecastplans(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_demandforecastplans_org_status ON supply_chain_planning_demandforecastplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_demandforecastplans_priority ON supply_chain_planning_demandforecastplans(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_demandforecastplans_created_at ON supply_chain_planning_demandforecastplans(created_at);

-- Operational seed data fixtures for supply_chain_planning_demandforecastplans
INSERT OR IGNORE INTO supply_chain_planning_demandforecastplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEM-0001", "Primary Operational DemandForecastPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-demandforecastplan-01"),
    (2, "DEM-0002", "Secondary Corporate DemandForecastPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-demandforecastplan-02"),
    (3, "DEM-0003", "Consolidated Branch DemandForecastPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-demandforecastplan-03"),
    (4, "DEM-0004", "Enterprise Audited DemandForecastPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-demandforecastplan-04"),
    (5, "DEM-0005", "Executive Strategic DemandForecastPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-demandforecastplan-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_supplyconstraintmodels (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_supplyconstraintmodels_code ON supply_chain_planning_supplyconstraintmodels(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_supplyconstraintmodels_org_status ON supply_chain_planning_supplyconstraintmodels(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_supplyconstraintmodels_priority ON supply_chain_planning_supplyconstraintmodels(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_supplyconstraintmodels_created_at ON supply_chain_planning_supplyconstraintmodels(created_at);

-- Operational seed data fixtures for supply_chain_planning_supplyconstraintmodels
INSERT OR IGNORE INTO supply_chain_planning_supplyconstraintmodels (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplyConstraintModel 1", 24500.00, 150.0, "ACTIVE", "uuid-supplyconstraintmodel-01"),
    (2, "SUP-0002", "Secondary Corporate SupplyConstraintModel 2", 18200.50, 80.0, "ACTIVE", "uuid-supplyconstraintmodel-02"),
    (3, "SUP-0003", "Consolidated Branch SupplyConstraintModel 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supplyconstraintmodel-03"),
    (4, "SUP-0004", "Enterprise Audited SupplyConstraintModel 4", 32800.00, 210.0, "ACTIVE", "uuid-supplyconstraintmodel-04"),
    (5, "SUP-0005", "Executive Strategic SupplyConstraintModel 5", 65000.00, 400.0, "ACTIVE", "uuid-supplyconstraintmodel-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_safetystockthresholds (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_safetystockthresholds_code ON supply_chain_planning_safetystockthresholds(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_safetystockthresholds_org_status ON supply_chain_planning_safetystockthresholds(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_safetystockthresholds_priority ON supply_chain_planning_safetystockthresholds(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_safetystockthresholds_created_at ON supply_chain_planning_safetystockthresholds(created_at);

-- Operational seed data fixtures for supply_chain_planning_safetystockthresholds
INSERT OR IGNORE INTO supply_chain_planning_safetystockthresholds (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAF-0001", "Primary Operational SafetyStockThreshold 1", 24500.00, 150.0, "ACTIVE", "uuid-safetystockthreshold-01"),
    (2, "SAF-0002", "Secondary Corporate SafetyStockThreshold 2", 18200.50, 80.0, "ACTIVE", "uuid-safetystockthreshold-02"),
    (3, "SAF-0003", "Consolidated Branch SafetyStockThreshold 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-safetystockthreshold-03"),
    (4, "SAF-0004", "Enterprise Audited SafetyStockThreshold 4", 32800.00, 210.0, "ACTIVE", "uuid-safetystockthreshold-04"),
    (5, "SAF-0005", "Executive Strategic SafetyStockThreshold 5", 65000.00, 400.0, "ACTIVE", "uuid-safetystockthreshold-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_productioncapacitylimits (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_productioncapacitylimits_code ON supply_chain_planning_productioncapacitylimits(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_productioncapacitylimits_org_status ON supply_chain_planning_productioncapacitylimits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_productioncapacitylimits_priority ON supply_chain_planning_productioncapacitylimits(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_productioncapacitylimits_created_at ON supply_chain_planning_productioncapacitylimits(created_at);

-- Operational seed data fixtures for supply_chain_planning_productioncapacitylimits
INSERT OR IGNORE INTO supply_chain_planning_productioncapacitylimits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProductionCapacityLimit 1", 24500.00, 150.0, "ACTIVE", "uuid-productioncapacitylimit-01"),
    (2, "PRO-0002", "Secondary Corporate ProductionCapacityLimit 2", 18200.50, 80.0, "ACTIVE", "uuid-productioncapacitylimit-02"),
    (3, "PRO-0003", "Consolidated Branch ProductionCapacityLimit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-productioncapacitylimit-03"),
    (4, "PRO-0004", "Enterprise Audited ProductionCapacityLimit 4", 32800.00, 210.0, "ACTIVE", "uuid-productioncapacitylimit-04"),
    (5, "PRO-0005", "Executive Strategic ProductionCapacityLimit 5", 65000.00, 400.0, "ACTIVE", "uuid-productioncapacitylimit-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_leadtimevariabilitys (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_leadtimevariabilitys_code ON supply_chain_planning_leadtimevariabilitys(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_leadtimevariabilitys_org_status ON supply_chain_planning_leadtimevariabilitys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_leadtimevariabilitys_priority ON supply_chain_planning_leadtimevariabilitys(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_leadtimevariabilitys_created_at ON supply_chain_planning_leadtimevariabilitys(created_at);

-- Operational seed data fixtures for supply_chain_planning_leadtimevariabilitys
INSERT OR IGNORE INTO supply_chain_planning_leadtimevariabilitys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeadTimeVariability 1", 24500.00, 150.0, "ACTIVE", "uuid-leadtimevariability-01"),
    (2, "LEA-0002", "Secondary Corporate LeadTimeVariability 2", 18200.50, 80.0, "ACTIVE", "uuid-leadtimevariability-02"),
    (3, "LEA-0003", "Consolidated Branch LeadTimeVariability 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leadtimevariability-03"),
    (4, "LEA-0004", "Enterprise Audited LeadTimeVariability 4", 32800.00, 210.0, "ACTIVE", "uuid-leadtimevariability-04"),
    (5, "LEA-0005", "Executive Strategic LeadTimeVariability 5", 65000.00, 400.0, "ACTIVE", "uuid-leadtimevariability-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_materialrequirementplans (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_materialrequirementplans_code ON supply_chain_planning_materialrequirementplans(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_materialrequirementplans_org_status ON supply_chain_planning_materialrequirementplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_materialrequirementplans_priority ON supply_chain_planning_materialrequirementplans(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_materialrequirementplans_created_at ON supply_chain_planning_materialrequirementplans(created_at);

-- Operational seed data fixtures for supply_chain_planning_materialrequirementplans
INSERT OR IGNORE INTO supply_chain_planning_materialrequirementplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAT-0001", "Primary Operational MaterialRequirementPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-materialrequirementplan-01"),
    (2, "MAT-0002", "Secondary Corporate MaterialRequirementPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-materialrequirementplan-02"),
    (3, "MAT-0003", "Consolidated Branch MaterialRequirementPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-materialrequirementplan-03"),
    (4, "MAT-0004", "Enterprise Audited MaterialRequirementPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-materialrequirementplan-04"),
    (5, "MAT-0005", "Executive Strategic MaterialRequirementPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-materialrequirementplan-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_distributionplans (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_distributionplans_code ON supply_chain_planning_distributionplans(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_distributionplans_org_status ON supply_chain_planning_distributionplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_distributionplans_priority ON supply_chain_planning_distributionplans(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_distributionplans_created_at ON supply_chain_planning_distributionplans(created_at);

-- Operational seed data fixtures for supply_chain_planning_distributionplans
INSERT OR IGNORE INTO supply_chain_planning_distributionplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DistributionPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-distributionplan-01"),
    (2, "DIS-0002", "Secondary Corporate DistributionPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-distributionplan-02"),
    (3, "DIS-0003", "Consolidated Branch DistributionPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-distributionplan-03"),
    (4, "DIS-0004", "Enterprise Audited DistributionPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-distributionplan-04"),
    (5, "DIS-0005", "Executive Strategic DistributionPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-distributionplan-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_stockallocationrules (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_stockallocationrules_code ON supply_chain_planning_stockallocationrules(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_stockallocationrules_org_status ON supply_chain_planning_stockallocationrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_stockallocationrules_priority ON supply_chain_planning_stockallocationrules(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_stockallocationrules_created_at ON supply_chain_planning_stockallocationrules(created_at);

-- Operational seed data fixtures for supply_chain_planning_stockallocationrules
INSERT OR IGNORE INTO supply_chain_planning_stockallocationrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STO-0001", "Primary Operational StockAllocationRule 1", 24500.00, 150.0, "ACTIVE", "uuid-stockallocationrule-01"),
    (2, "STO-0002", "Secondary Corporate StockAllocationRule 2", 18200.50, 80.0, "ACTIVE", "uuid-stockallocationrule-02"),
    (3, "STO-0003", "Consolidated Branch StockAllocationRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-stockallocationrule-03"),
    (4, "STO-0004", "Enterprise Audited StockAllocationRule 4", 32800.00, 210.0, "ACTIVE", "uuid-stockallocationrule-04"),
    (5, "STO-0005", "Executive Strategic StockAllocationRule 5", 65000.00, 400.0, "ACTIVE", "uuid-stockallocationrule-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_suppliercommitments (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_suppliercommitments_code ON supply_chain_planning_suppliercommitments(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_suppliercommitments_org_status ON supply_chain_planning_suppliercommitments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_suppliercommitments_priority ON supply_chain_planning_suppliercommitments(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_suppliercommitments_created_at ON supply_chain_planning_suppliercommitments(created_at);

-- Operational seed data fixtures for supply_chain_planning_suppliercommitments
INSERT OR IGNORE INTO supply_chain_planning_suppliercommitments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierCommitment 1", 24500.00, 150.0, "ACTIVE", "uuid-suppliercommitment-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierCommitment 2", 18200.50, 80.0, "ACTIVE", "uuid-suppliercommitment-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierCommitment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-suppliercommitment-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierCommitment 4", 32800.00, 210.0, "ACTIVE", "uuid-suppliercommitment-04"),
    (5, "SUP-0005", "Executive Strategic SupplierCommitment 5", 65000.00, 400.0, "ACTIVE", "uuid-suppliercommitment-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_forecastaccuracymetrics (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_forecastaccuracymetrics_code ON supply_chain_planning_forecastaccuracymetrics(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_forecastaccuracymetrics_org_status ON supply_chain_planning_forecastaccuracymetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_forecastaccuracymetrics_priority ON supply_chain_planning_forecastaccuracymetrics(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_forecastaccuracymetrics_created_at ON supply_chain_planning_forecastaccuracymetrics(created_at);

-- Operational seed data fixtures for supply_chain_planning_forecastaccuracymetrics
INSERT OR IGNORE INTO supply_chain_planning_forecastaccuracymetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FOR-0001", "Primary Operational ForecastAccuracyMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-forecastaccuracymetric-01"),
    (2, "FOR-0002", "Secondary Corporate ForecastAccuracyMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-forecastaccuracymetric-02"),
    (3, "FOR-0003", "Consolidated Branch ForecastAccuracyMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-forecastaccuracymetric-03"),
    (4, "FOR-0004", "Enterprise Audited ForecastAccuracyMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-forecastaccuracymetric-04"),
    (5, "FOR-0005", "Executive Strategic ForecastAccuracyMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-forecastaccuracymetric-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_inventorybufferzones (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_inventorybufferzones_code ON supply_chain_planning_inventorybufferzones(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_inventorybufferzones_org_status ON supply_chain_planning_inventorybufferzones(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_inventorybufferzones_priority ON supply_chain_planning_inventorybufferzones(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_inventorybufferzones_created_at ON supply_chain_planning_inventorybufferzones(created_at);

-- Operational seed data fixtures for supply_chain_planning_inventorybufferzones
INSERT OR IGNORE INTO supply_chain_planning_inventorybufferzones (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INV-0001", "Primary Operational InventoryBufferZone 1", 24500.00, 150.0, "ACTIVE", "uuid-inventorybufferzone-01"),
    (2, "INV-0002", "Secondary Corporate InventoryBufferZone 2", 18200.50, 80.0, "ACTIVE", "uuid-inventorybufferzone-02"),
    (3, "INV-0003", "Consolidated Branch InventoryBufferZone 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inventorybufferzone-03"),
    (4, "INV-0004", "Enterprise Audited InventoryBufferZone 4", 32800.00, 210.0, "ACTIVE", "uuid-inventorybufferzone-04"),
    (5, "INV-0005", "Executive Strategic InventoryBufferZone 5", 65000.00, 400.0, "ACTIVE", "uuid-inventorybufferzone-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_masterproductionschedules (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_masterproductionschedules_code ON supply_chain_planning_masterproductionschedules(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_masterproductionschedules_org_status ON supply_chain_planning_masterproductionschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_masterproductionschedules_priority ON supply_chain_planning_masterproductionschedules(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_masterproductionschedules_created_at ON supply_chain_planning_masterproductionschedules(created_at);

-- Operational seed data fixtures for supply_chain_planning_masterproductionschedules
INSERT OR IGNORE INTO supply_chain_planning_masterproductionschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAS-0001", "Primary Operational MasterProductionSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-masterproductionschedule-01"),
    (2, "MAS-0002", "Secondary Corporate MasterProductionSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-masterproductionschedule-02"),
    (3, "MAS-0003", "Consolidated Branch MasterProductionSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-masterproductionschedule-03"),
    (4, "MAS-0004", "Enterprise Audited MasterProductionSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-masterproductionschedule-04"),
    (5, "MAS-0005", "Executive Strategic MasterProductionSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-masterproductionschedule-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_bottleneckworkstations (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_bottleneckworkstations_code ON supply_chain_planning_bottleneckworkstations(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_bottleneckworkstations_org_status ON supply_chain_planning_bottleneckworkstations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_bottleneckworkstations_priority ON supply_chain_planning_bottleneckworkstations(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_bottleneckworkstations_created_at ON supply_chain_planning_bottleneckworkstations(created_at);

-- Operational seed data fixtures for supply_chain_planning_bottleneckworkstations
INSERT OR IGNORE INTO supply_chain_planning_bottleneckworkstations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BOT-0001", "Primary Operational BottleneckWorkstation 1", 24500.00, 150.0, "ACTIVE", "uuid-bottleneckworkstation-01"),
    (2, "BOT-0002", "Secondary Corporate BottleneckWorkstation 2", 18200.50, 80.0, "ACTIVE", "uuid-bottleneckworkstation-02"),
    (3, "BOT-0003", "Consolidated Branch BottleneckWorkstation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bottleneckworkstation-03"),
    (4, "BOT-0004", "Enterprise Audited BottleneckWorkstation 4", 32800.00, 210.0, "ACTIVE", "uuid-bottleneckworkstation-04"),
    (5, "BOT-0005", "Executive Strategic BottleneckWorkstation 5", 65000.00, 400.0, "ACTIVE", "uuid-bottleneckworkstation-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_scenariocomparisons (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_scenariocomparisons_code ON supply_chain_planning_scenariocomparisons(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_scenariocomparisons_org_status ON supply_chain_planning_scenariocomparisons(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_scenariocomparisons_priority ON supply_chain_planning_scenariocomparisons(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_scenariocomparisons_created_at ON supply_chain_planning_scenariocomparisons(created_at);

-- Operational seed data fixtures for supply_chain_planning_scenariocomparisons
INSERT OR IGNORE INTO supply_chain_planning_scenariocomparisons (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SCE-0001", "Primary Operational ScenarioComparison 1", 24500.00, 150.0, "ACTIVE", "uuid-scenariocomparison-01"),
    (2, "SCE-0002", "Secondary Corporate ScenarioComparison 2", 18200.50, 80.0, "ACTIVE", "uuid-scenariocomparison-02"),
    (3, "SCE-0003", "Consolidated Branch ScenarioComparison 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-scenariocomparison-03"),
    (4, "SCE-0004", "Enterprise Audited ScenarioComparison 4", 32800.00, 210.0, "ACTIVE", "uuid-scenariocomparison-04"),
    (5, "SCE-0005", "Executive Strategic ScenarioComparison 5", 65000.00, 400.0, "ACTIVE", "uuid-scenariocomparison-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_expeditedshipmentorders (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_expeditedshipmentorders_code ON supply_chain_planning_expeditedshipmentorders(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_expeditedshipmentorders_org_status ON supply_chain_planning_expeditedshipmentorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_expeditedshipmentorders_priority ON supply_chain_planning_expeditedshipmentorders(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_expeditedshipmentorders_created_at ON supply_chain_planning_expeditedshipmentorders(created_at);

-- Operational seed data fixtures for supply_chain_planning_expeditedshipmentorders
INSERT OR IGNORE INTO supply_chain_planning_expeditedshipmentorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExpeditedShipmentOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-expeditedshipmentorder-01"),
    (2, "EXP-0002", "Secondary Corporate ExpeditedShipmentOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-expeditedshipmentorder-02"),
    (3, "EXP-0003", "Consolidated Branch ExpeditedShipmentOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-expeditedshipmentorder-03"),
    (4, "EXP-0004", "Enterprise Audited ExpeditedShipmentOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-expeditedshipmentorder-04"),
    (5, "EXP-0005", "Executive Strategic ExpeditedShipmentOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-expeditedshipmentorder-05");

CREATE TABLE IF NOT EXISTS supply_chain_planning_executivesopconsensuss (
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

CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_executivesopconsensuss_code ON supply_chain_planning_executivesopconsensuss(code);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_executivesopconsensuss_org_status ON supply_chain_planning_executivesopconsensuss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_executivesopconsensuss_priority ON supply_chain_planning_executivesopconsensuss(priority);
CREATE INDEX IF NOT EXISTS idx_supply_chain_planning_executivesopconsensuss_created_at ON supply_chain_planning_executivesopconsensuss(created_at);

-- Operational seed data fixtures for supply_chain_planning_executivesopconsensuss
INSERT OR IGNORE INTO supply_chain_planning_executivesopconsensuss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutiveSOPConsensus 1", 24500.00, 150.0, "ACTIVE", "uuid-executivesopconsensus-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutiveSOPConsensus 2", 18200.50, 80.0, "ACTIVE", "uuid-executivesopconsensus-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutiveSOPConsensus 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executivesopconsensus-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutiveSOPConsensus 4", 32800.00, 210.0, "ACTIVE", "uuid-executivesopconsensus-04"),
    (5, "EXE-0005", "Executive Strategic ExecutiveSOPConsensus 5", 65000.00, 400.0, "ACTIVE", "uuid-executivesopconsensus-05");

