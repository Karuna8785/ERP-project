-- SmartERP Enterprise Titan Migration 034: Automated Inventory Replenishment & Min-Max DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS inventory_replenishment_replenishmentpolicys (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentpolicys_code ON inventory_replenishment_replenishmentpolicys(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentpolicys_org_status ON inventory_replenishment_replenishmentpolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentpolicys_priority ON inventory_replenishment_replenishmentpolicys(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentpolicys_created_at ON inventory_replenishment_replenishmentpolicys(created_at);

-- Operational seed data fixtures for inventory_replenishment_replenishmentpolicys
INSERT OR IGNORE INTO inventory_replenishment_replenishmentpolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REP-0001", "Primary Operational ReplenishmentPolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-replenishmentpolicy-01"),
    (2, "REP-0002", "Secondary Corporate ReplenishmentPolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-replenishmentpolicy-02"),
    (3, "REP-0003", "Consolidated Branch ReplenishmentPolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-replenishmentpolicy-03"),
    (4, "REP-0004", "Enterprise Audited ReplenishmentPolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-replenishmentpolicy-04"),
    (5, "REP-0005", "Executive Strategic ReplenishmentPolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-replenishmentpolicy-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_economicorderquantitys (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_economicorderquantitys_code ON inventory_replenishment_economicorderquantitys(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_economicorderquantitys_org_status ON inventory_replenishment_economicorderquantitys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_economicorderquantitys_priority ON inventory_replenishment_economicorderquantitys(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_economicorderquantitys_created_at ON inventory_replenishment_economicorderquantitys(created_at);

-- Operational seed data fixtures for inventory_replenishment_economicorderquantitys
INSERT OR IGNORE INTO inventory_replenishment_economicorderquantitys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ECO-0001", "Primary Operational EconomicOrderQuantity 1", 24500.00, 150.0, "ACTIVE", "uuid-economicorderquantity-01"),
    (2, "ECO-0002", "Secondary Corporate EconomicOrderQuantity 2", 18200.50, 80.0, "ACTIVE", "uuid-economicorderquantity-02"),
    (3, "ECO-0003", "Consolidated Branch EconomicOrderQuantity 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-economicorderquantity-03"),
    (4, "ECO-0004", "Enterprise Audited EconomicOrderQuantity 4", 32800.00, 210.0, "ACTIVE", "uuid-economicorderquantity-04"),
    (5, "ECO-0005", "Executive Strategic EconomicOrderQuantity 5", 65000.00, 400.0, "ACTIVE", "uuid-economicorderquantity-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_reorderpointrules (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_reorderpointrules_code ON inventory_replenishment_reorderpointrules(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_reorderpointrules_org_status ON inventory_replenishment_reorderpointrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_reorderpointrules_priority ON inventory_replenishment_reorderpointrules(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_reorderpointrules_created_at ON inventory_replenishment_reorderpointrules(created_at);

-- Operational seed data fixtures for inventory_replenishment_reorderpointrules
INSERT OR IGNORE INTO inventory_replenishment_reorderpointrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REO-0001", "Primary Operational ReorderPointRule 1", 24500.00, 150.0, "ACTIVE", "uuid-reorderpointrule-01"),
    (2, "REO-0002", "Secondary Corporate ReorderPointRule 2", 18200.50, 80.0, "ACTIVE", "uuid-reorderpointrule-02"),
    (3, "REO-0003", "Consolidated Branch ReorderPointRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-reorderpointrule-03"),
    (4, "REO-0004", "Enterprise Audited ReorderPointRule 4", 32800.00, 210.0, "ACTIVE", "uuid-reorderpointrule-04"),
    (5, "REO-0005", "Executive Strategic ReorderPointRule 5", 65000.00, 400.0, "ACTIVE", "uuid-reorderpointrule-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_safetystockcalculations (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_safetystockcalculations_code ON inventory_replenishment_safetystockcalculations(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_safetystockcalculations_org_status ON inventory_replenishment_safetystockcalculations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_safetystockcalculations_priority ON inventory_replenishment_safetystockcalculations(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_safetystockcalculations_created_at ON inventory_replenishment_safetystockcalculations(created_at);

-- Operational seed data fixtures for inventory_replenishment_safetystockcalculations
INSERT OR IGNORE INTO inventory_replenishment_safetystockcalculations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAF-0001", "Primary Operational SafetyStockCalculation 1", 24500.00, 150.0, "ACTIVE", "uuid-safetystockcalculation-01"),
    (2, "SAF-0002", "Secondary Corporate SafetyStockCalculation 2", 18200.50, 80.0, "ACTIVE", "uuid-safetystockcalculation-02"),
    (3, "SAF-0003", "Consolidated Branch SafetyStockCalculation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-safetystockcalculation-03"),
    (4, "SAF-0004", "Enterprise Audited SafetyStockCalculation 4", 32800.00, 210.0, "ACTIVE", "uuid-safetystockcalculation-04"),
    (5, "SAF-0005", "Executive Strategic SafetyStockCalculation 5", 65000.00, 400.0, "ACTIVE", "uuid-safetystockcalculation-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_velocityclassificationabcs (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_velocityclassificationabcs_code ON inventory_replenishment_velocityclassificationabcs(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_velocityclassificationabcs_org_status ON inventory_replenishment_velocityclassificationabcs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_velocityclassificationabcs_priority ON inventory_replenishment_velocityclassificationabcs(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_velocityclassificationabcs_created_at ON inventory_replenishment_velocityclassificationabcs(created_at);

-- Operational seed data fixtures for inventory_replenishment_velocityclassificationabcs
INSERT OR IGNORE INTO inventory_replenishment_velocityclassificationabcs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEL-0001", "Primary Operational VelocityClassificationABC 1", 24500.00, 150.0, "ACTIVE", "uuid-velocityclassificationabc-01"),
    (2, "VEL-0002", "Secondary Corporate VelocityClassificationABC 2", 18200.50, 80.0, "ACTIVE", "uuid-velocityclassificationabc-02"),
    (3, "VEL-0003", "Consolidated Branch VelocityClassificationABC 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-velocityclassificationabc-03"),
    (4, "VEL-0004", "Enterprise Audited VelocityClassificationABC 4", 32800.00, 210.0, "ACTIVE", "uuid-velocityclassificationabc-04"),
    (5, "VEL-0005", "Executive Strategic VelocityClassificationABC 5", 65000.00, 400.0, "ACTIVE", "uuid-velocityclassificationabc-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_supplierleadtimeprofiles (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_supplierleadtimeprofiles_code ON inventory_replenishment_supplierleadtimeprofiles(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_supplierleadtimeprofiles_org_status ON inventory_replenishment_supplierleadtimeprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_supplierleadtimeprofiles_priority ON inventory_replenishment_supplierleadtimeprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_supplierleadtimeprofiles_created_at ON inventory_replenishment_supplierleadtimeprofiles(created_at);

-- Operational seed data fixtures for inventory_replenishment_supplierleadtimeprofiles
INSERT OR IGNORE INTO inventory_replenishment_supplierleadtimeprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierLeadTimeProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-supplierleadtimeprofile-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierLeadTimeProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-supplierleadtimeprofile-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierLeadTimeProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supplierleadtimeprofile-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierLeadTimeProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-supplierleadtimeprofile-04"),
    (5, "SUP-0005", "Executive Strategic SupplierLeadTimeProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-supplierleadtimeprofile-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_transferreplenishmentorders (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_transferreplenishmentorders_code ON inventory_replenishment_transferreplenishmentorders(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_transferreplenishmentorders_org_status ON inventory_replenishment_transferreplenishmentorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_transferreplenishmentorders_priority ON inventory_replenishment_transferreplenishmentorders(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_transferreplenishmentorders_created_at ON inventory_replenishment_transferreplenishmentorders(created_at);

-- Operational seed data fixtures for inventory_replenishment_transferreplenishmentorders
INSERT OR IGNORE INTO inventory_replenishment_transferreplenishmentorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TransferReplenishmentOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-transferreplenishmentorder-01"),
    (2, "TRA-0002", "Secondary Corporate TransferReplenishmentOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-transferreplenishmentorder-02"),
    (3, "TRA-0003", "Consolidated Branch TransferReplenishmentOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-transferreplenishmentorder-03"),
    (4, "TRA-0004", "Enterprise Audited TransferReplenishmentOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-transferreplenishmentorder-04"),
    (5, "TRA-0005", "Executive Strategic TransferReplenishmentOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-transferreplenishmentorder-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_stockoutalertnotices (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_stockoutalertnotices_code ON inventory_replenishment_stockoutalertnotices(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_stockoutalertnotices_org_status ON inventory_replenishment_stockoutalertnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_stockoutalertnotices_priority ON inventory_replenishment_stockoutalertnotices(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_stockoutalertnotices_created_at ON inventory_replenishment_stockoutalertnotices(created_at);

-- Operational seed data fixtures for inventory_replenishment_stockoutalertnotices
INSERT OR IGNORE INTO inventory_replenishment_stockoutalertnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STO-0001", "Primary Operational StockoutAlertNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-stockoutalertnotice-01"),
    (2, "STO-0002", "Secondary Corporate StockoutAlertNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-stockoutalertnotice-02"),
    (3, "STO-0003", "Consolidated Branch StockoutAlertNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-stockoutalertnotice-03"),
    (4, "STO-0004", "Enterprise Audited StockoutAlertNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-stockoutalertnotice-04"),
    (5, "STO-0005", "Executive Strategic StockoutAlertNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-stockoutalertnotice-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_excessinventoryflags (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_excessinventoryflags_code ON inventory_replenishment_excessinventoryflags(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_excessinventoryflags_org_status ON inventory_replenishment_excessinventoryflags(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_excessinventoryflags_priority ON inventory_replenishment_excessinventoryflags(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_excessinventoryflags_created_at ON inventory_replenishment_excessinventoryflags(created_at);

-- Operational seed data fixtures for inventory_replenishment_excessinventoryflags
INSERT OR IGNORE INTO inventory_replenishment_excessinventoryflags (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXC-0001", "Primary Operational ExcessInventoryFlag 1", 24500.00, 150.0, "ACTIVE", "uuid-excessinventoryflag-01"),
    (2, "EXC-0002", "Secondary Corporate ExcessInventoryFlag 2", 18200.50, 80.0, "ACTIVE", "uuid-excessinventoryflag-02"),
    (3, "EXC-0003", "Consolidated Branch ExcessInventoryFlag 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-excessinventoryflag-03"),
    (4, "EXC-0004", "Enterprise Audited ExcessInventoryFlag 4", 32800.00, 210.0, "ACTIVE", "uuid-excessinventoryflag-04"),
    (5, "EXC-0005", "Executive Strategic ExcessInventoryFlag 5", 65000.00, 400.0, "ACTIVE", "uuid-excessinventoryflag-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_seasonaldemandfactors (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_seasonaldemandfactors_code ON inventory_replenishment_seasonaldemandfactors(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_seasonaldemandfactors_org_status ON inventory_replenishment_seasonaldemandfactors(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_seasonaldemandfactors_priority ON inventory_replenishment_seasonaldemandfactors(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_seasonaldemandfactors_created_at ON inventory_replenishment_seasonaldemandfactors(created_at);

-- Operational seed data fixtures for inventory_replenishment_seasonaldemandfactors
INSERT OR IGNORE INTO inventory_replenishment_seasonaldemandfactors (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEA-0001", "Primary Operational SeasonalDemandFactor 1", 24500.00, 150.0, "ACTIVE", "uuid-seasonaldemandfactor-01"),
    (2, "SEA-0002", "Secondary Corporate SeasonalDemandFactor 2", 18200.50, 80.0, "ACTIVE", "uuid-seasonaldemandfactor-02"),
    (3, "SEA-0003", "Consolidated Branch SeasonalDemandFactor 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-seasonaldemandfactor-03"),
    (4, "SEA-0004", "Enterprise Audited SeasonalDemandFactor 4", 32800.00, 210.0, "ACTIVE", "uuid-seasonaldemandfactor-04"),
    (5, "SEA-0005", "Executive Strategic SeasonalDemandFactor 5", 65000.00, 400.0, "ACTIVE", "uuid-seasonaldemandfactor-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_bufferstockreserves (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_bufferstockreserves_code ON inventory_replenishment_bufferstockreserves(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_bufferstockreserves_org_status ON inventory_replenishment_bufferstockreserves(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_bufferstockreserves_priority ON inventory_replenishment_bufferstockreserves(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_bufferstockreserves_created_at ON inventory_replenishment_bufferstockreserves(created_at);

-- Operational seed data fixtures for inventory_replenishment_bufferstockreserves
INSERT OR IGNORE INTO inventory_replenishment_bufferstockreserves (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BUF-0001", "Primary Operational BufferStockReserve 1", 24500.00, 150.0, "ACTIVE", "uuid-bufferstockreserve-01"),
    (2, "BUF-0002", "Secondary Corporate BufferStockReserve 2", 18200.50, 80.0, "ACTIVE", "uuid-bufferstockreserve-02"),
    (3, "BUF-0003", "Consolidated Branch BufferStockReserve 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bufferstockreserve-03"),
    (4, "BUF-0004", "Enterprise Audited BufferStockReserve 4", 32800.00, 210.0, "ACTIVE", "uuid-bufferstockreserve-04"),
    (5, "BUF-0005", "Executive Strategic BufferStockReserve 5", 65000.00, 400.0, "ACTIVE", "uuid-bufferstockreserve-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_vendormanagedinventorys (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_vendormanagedinventorys_code ON inventory_replenishment_vendormanagedinventorys(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_vendormanagedinventorys_org_status ON inventory_replenishment_vendormanagedinventorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_vendormanagedinventorys_priority ON inventory_replenishment_vendormanagedinventorys(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_vendormanagedinventorys_created_at ON inventory_replenishment_vendormanagedinventorys(created_at);

-- Operational seed data fixtures for inventory_replenishment_vendormanagedinventorys
INSERT OR IGNORE INTO inventory_replenishment_vendormanagedinventorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorManagedInventory 1", 24500.00, 150.0, "ACTIVE", "uuid-vendormanagedinventory-01"),
    (2, "VEN-0002", "Secondary Corporate VendorManagedInventory 2", 18200.50, 80.0, "ACTIVE", "uuid-vendormanagedinventory-02"),
    (3, "VEN-0003", "Consolidated Branch VendorManagedInventory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendormanagedinventory-03"),
    (4, "VEN-0004", "Enterprise Audited VendorManagedInventory 4", 32800.00, 210.0, "ACTIVE", "uuid-vendormanagedinventory-04"),
    (5, "VEN-0005", "Executive Strategic VendorManagedInventory 5", 65000.00, 400.0, "ACTIVE", "uuid-vendormanagedinventory-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_backorderpriorityqueues (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_backorderpriorityqueues_code ON inventory_replenishment_backorderpriorityqueues(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_backorderpriorityqueues_org_status ON inventory_replenishment_backorderpriorityqueues(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_backorderpriorityqueues_priority ON inventory_replenishment_backorderpriorityqueues(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_backorderpriorityqueues_created_at ON inventory_replenishment_backorderpriorityqueues(created_at);

-- Operational seed data fixtures for inventory_replenishment_backorderpriorityqueues
INSERT OR IGNORE INTO inventory_replenishment_backorderpriorityqueues (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BAC-0001", "Primary Operational BackorderPriorityQueue 1", 24500.00, 150.0, "ACTIVE", "uuid-backorderpriorityqueue-01"),
    (2, "BAC-0002", "Secondary Corporate BackorderPriorityQueue 2", 18200.50, 80.0, "ACTIVE", "uuid-backorderpriorityqueue-02"),
    (3, "BAC-0003", "Consolidated Branch BackorderPriorityQueue 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-backorderpriorityqueue-03"),
    (4, "BAC-0004", "Enterprise Audited BackorderPriorityQueue 4", 32800.00, 210.0, "ACTIVE", "uuid-backorderpriorityqueue-04"),
    (5, "BAC-0005", "Executive Strategic BackorderPriorityQueue 5", 65000.00, 400.0, "ACTIVE", "uuid-backorderpriorityqueue-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_multiechelonnetworks (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_multiechelonnetworks_code ON inventory_replenishment_multiechelonnetworks(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_multiechelonnetworks_org_status ON inventory_replenishment_multiechelonnetworks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_multiechelonnetworks_priority ON inventory_replenishment_multiechelonnetworks(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_multiechelonnetworks_created_at ON inventory_replenishment_multiechelonnetworks(created_at);

-- Operational seed data fixtures for inventory_replenishment_multiechelonnetworks
INSERT OR IGNORE INTO inventory_replenishment_multiechelonnetworks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MUL-0001", "Primary Operational MultiEchelonNetwork 1", 24500.00, 150.0, "ACTIVE", "uuid-multiechelonnetwork-01"),
    (2, "MUL-0002", "Secondary Corporate MultiEchelonNetwork 2", 18200.50, 80.0, "ACTIVE", "uuid-multiechelonnetwork-02"),
    (3, "MUL-0003", "Consolidated Branch MultiEchelonNetwork 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-multiechelonnetwork-03"),
    (4, "MUL-0004", "Enterprise Audited MultiEchelonNetwork 4", 32800.00, 210.0, "ACTIVE", "uuid-multiechelonnetwork-04"),
    (5, "MUL-0005", "Executive Strategic MultiEchelonNetwork 5", 65000.00, 400.0, "ACTIVE", "uuid-multiechelonnetwork-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_replenishmentrunlogs (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentrunlogs_code ON inventory_replenishment_replenishmentrunlogs(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentrunlogs_org_status ON inventory_replenishment_replenishmentrunlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentrunlogs_priority ON inventory_replenishment_replenishmentrunlogs(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_replenishmentrunlogs_created_at ON inventory_replenishment_replenishmentrunlogs(created_at);

-- Operational seed data fixtures for inventory_replenishment_replenishmentrunlogs
INSERT OR IGNORE INTO inventory_replenishment_replenishmentrunlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REP-0001", "Primary Operational ReplenishmentRunLog 1", 24500.00, 150.0, "ACTIVE", "uuid-replenishmentrunlog-01"),
    (2, "REP-0002", "Secondary Corporate ReplenishmentRunLog 2", 18200.50, 80.0, "ACTIVE", "uuid-replenishmentrunlog-02"),
    (3, "REP-0003", "Consolidated Branch ReplenishmentRunLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-replenishmentrunlog-03"),
    (4, "REP-0004", "Enterprise Audited ReplenishmentRunLog 4", 32800.00, 210.0, "ACTIVE", "uuid-replenishmentrunlog-04"),
    (5, "REP-0005", "Executive Strategic ReplenishmentRunLog 5", 65000.00, 400.0, "ACTIVE", "uuid-replenishmentrunlog-05");

CREATE TABLE IF NOT EXISTS inventory_replenishment_servicelevelgoals (
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

CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_servicelevelgoals_code ON inventory_replenishment_servicelevelgoals(code);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_servicelevelgoals_org_status ON inventory_replenishment_servicelevelgoals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_servicelevelgoals_priority ON inventory_replenishment_servicelevelgoals(priority);
CREATE INDEX IF NOT EXISTS idx_inventory_replenishment_servicelevelgoals_created_at ON inventory_replenishment_servicelevelgoals(created_at);

-- Operational seed data fixtures for inventory_replenishment_servicelevelgoals
INSERT OR IGNORE INTO inventory_replenishment_servicelevelgoals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceLevelGoal 1", 24500.00, 150.0, "ACTIVE", "uuid-servicelevelgoal-01"),
    (2, "SER-0002", "Secondary Corporate ServiceLevelGoal 2", 18200.50, 80.0, "ACTIVE", "uuid-servicelevelgoal-02"),
    (3, "SER-0003", "Consolidated Branch ServiceLevelGoal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicelevelgoal-03"),
    (4, "SER-0004", "Enterprise Audited ServiceLevelGoal 4", 32800.00, 210.0, "ACTIVE", "uuid-servicelevelgoal-04"),
    (5, "SER-0005", "Executive Strategic ServiceLevelGoal 5", 65000.00, 400.0, "ACTIVE", "uuid-servicelevelgoal-05");

