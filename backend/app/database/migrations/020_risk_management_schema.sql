-- SmartERP Enterprise Titan Migration 020: Enterprise Risk Management & KRI Matrix DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS risk_management_riskcategorydefinitions (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_riskcategorydefinitions_code ON risk_management_riskcategorydefinitions(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskcategorydefinitions_org_status ON risk_management_riskcategorydefinitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskcategorydefinitions_priority ON risk_management_riskcategorydefinitions(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskcategorydefinitions_created_at ON risk_management_riskcategorydefinitions(created_at);

-- Operational seed data fixtures for risk_management_riskcategorydefinitions
INSERT OR IGNORE INTO risk_management_riskcategorydefinitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RIS-0001", "Primary Operational RiskCategoryDefinition 1", 24500.00, 150.0, "ACTIVE", "uuid-riskcategorydefinition-01"),
    (2, "RIS-0002", "Secondary Corporate RiskCategoryDefinition 2", 18200.50, 80.0, "ACTIVE", "uuid-riskcategorydefinition-02"),
    (3, "RIS-0003", "Consolidated Branch RiskCategoryDefinition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-riskcategorydefinition-03"),
    (4, "RIS-0004", "Enterprise Audited RiskCategoryDefinition 4", 32800.00, 210.0, "ACTIVE", "uuid-riskcategorydefinition-04"),
    (5, "RIS-0005", "Executive Strategic RiskCategoryDefinition 5", 65000.00, 400.0, "ACTIVE", "uuid-riskcategorydefinition-05");

CREATE TABLE IF NOT EXISTS risk_management_riskregisteritems (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_riskregisteritems_code ON risk_management_riskregisteritems(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskregisteritems_org_status ON risk_management_riskregisteritems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskregisteritems_priority ON risk_management_riskregisteritems(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskregisteritems_created_at ON risk_management_riskregisteritems(created_at);

-- Operational seed data fixtures for risk_management_riskregisteritems
INSERT OR IGNORE INTO risk_management_riskregisteritems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RIS-0001", "Primary Operational RiskRegisterItem 1", 24500.00, 150.0, "ACTIVE", "uuid-riskregisteritem-01"),
    (2, "RIS-0002", "Secondary Corporate RiskRegisterItem 2", 18200.50, 80.0, "ACTIVE", "uuid-riskregisteritem-02"),
    (3, "RIS-0003", "Consolidated Branch RiskRegisterItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-riskregisteritem-03"),
    (4, "RIS-0004", "Enterprise Audited RiskRegisterItem 4", 32800.00, 210.0, "ACTIVE", "uuid-riskregisteritem-04"),
    (5, "RIS-0005", "Executive Strategic RiskRegisterItem 5", 65000.00, 400.0, "ACTIVE", "uuid-riskregisteritem-05");

CREATE TABLE IF NOT EXISTS risk_management_riskassessmentscores (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_riskassessmentscores_code ON risk_management_riskassessmentscores(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskassessmentscores_org_status ON risk_management_riskassessmentscores(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskassessmentscores_priority ON risk_management_riskassessmentscores(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskassessmentscores_created_at ON risk_management_riskassessmentscores(created_at);

-- Operational seed data fixtures for risk_management_riskassessmentscores
INSERT OR IGNORE INTO risk_management_riskassessmentscores (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RIS-0001", "Primary Operational RiskAssessmentScore 1", 24500.00, 150.0, "ACTIVE", "uuid-riskassessmentscore-01"),
    (2, "RIS-0002", "Secondary Corporate RiskAssessmentScore 2", 18200.50, 80.0, "ACTIVE", "uuid-riskassessmentscore-02"),
    (3, "RIS-0003", "Consolidated Branch RiskAssessmentScore 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-riskassessmentscore-03"),
    (4, "RIS-0004", "Enterprise Audited RiskAssessmentScore 4", 32800.00, 210.0, "ACTIVE", "uuid-riskassessmentscore-04"),
    (5, "RIS-0005", "Executive Strategic RiskAssessmentScore 5", 65000.00, 400.0, "ACTIVE", "uuid-riskassessmentscore-05");

CREATE TABLE IF NOT EXISTS risk_management_keyriskindicators (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_keyriskindicators_code ON risk_management_keyriskindicators(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_keyriskindicators_org_status ON risk_management_keyriskindicators(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_keyriskindicators_priority ON risk_management_keyriskindicators(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_keyriskindicators_created_at ON risk_management_keyriskindicators(created_at);

-- Operational seed data fixtures for risk_management_keyriskindicators
INSERT OR IGNORE INTO risk_management_keyriskindicators (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "KEY-0001", "Primary Operational KeyRiskIndicator 1", 24500.00, 150.0, "ACTIVE", "uuid-keyriskindicator-01"),
    (2, "KEY-0002", "Secondary Corporate KeyRiskIndicator 2", 18200.50, 80.0, "ACTIVE", "uuid-keyriskindicator-02"),
    (3, "KEY-0003", "Consolidated Branch KeyRiskIndicator 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-keyriskindicator-03"),
    (4, "KEY-0004", "Enterprise Audited KeyRiskIndicator 4", 32800.00, 210.0, "ACTIVE", "uuid-keyriskindicator-04"),
    (5, "KEY-0005", "Executive Strategic KeyRiskIndicator 5", 65000.00, 400.0, "ACTIVE", "uuid-keyriskindicator-05");

CREATE TABLE IF NOT EXISTS risk_management_krithresholdalerts (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_krithresholdalerts_code ON risk_management_krithresholdalerts(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_krithresholdalerts_org_status ON risk_management_krithresholdalerts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_krithresholdalerts_priority ON risk_management_krithresholdalerts(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_krithresholdalerts_created_at ON risk_management_krithresholdalerts(created_at);

-- Operational seed data fixtures for risk_management_krithresholdalerts
INSERT OR IGNORE INTO risk_management_krithresholdalerts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "KRI-0001", "Primary Operational KRIThresholdAlert 1", 24500.00, 150.0, "ACTIVE", "uuid-krithresholdalert-01"),
    (2, "KRI-0002", "Secondary Corporate KRIThresholdAlert 2", 18200.50, 80.0, "ACTIVE", "uuid-krithresholdalert-02"),
    (3, "KRI-0003", "Consolidated Branch KRIThresholdAlert 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-krithresholdalert-03"),
    (4, "KRI-0004", "Enterprise Audited KRIThresholdAlert 4", 32800.00, 210.0, "ACTIVE", "uuid-krithresholdalert-04"),
    (5, "KRI-0005", "Executive Strategic KRIThresholdAlert 5", 65000.00, 400.0, "ACTIVE", "uuid-krithresholdalert-05");

CREATE TABLE IF NOT EXISTS risk_management_riskmitigationstrategys (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_riskmitigationstrategys_code ON risk_management_riskmitigationstrategys(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskmitigationstrategys_org_status ON risk_management_riskmitigationstrategys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskmitigationstrategys_priority ON risk_management_riskmitigationstrategys(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskmitigationstrategys_created_at ON risk_management_riskmitigationstrategys(created_at);

-- Operational seed data fixtures for risk_management_riskmitigationstrategys
INSERT OR IGNORE INTO risk_management_riskmitigationstrategys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RIS-0001", "Primary Operational RiskMitigationStrategy 1", 24500.00, 150.0, "ACTIVE", "uuid-riskmitigationstrategy-01"),
    (2, "RIS-0002", "Secondary Corporate RiskMitigationStrategy 2", 18200.50, 80.0, "ACTIVE", "uuid-riskmitigationstrategy-02"),
    (3, "RIS-0003", "Consolidated Branch RiskMitigationStrategy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-riskmitigationstrategy-03"),
    (4, "RIS-0004", "Enterprise Audited RiskMitigationStrategy 4", 32800.00, 210.0, "ACTIVE", "uuid-riskmitigationstrategy-04"),
    (5, "RIS-0005", "Executive Strategic RiskMitigationStrategy 5", 65000.00, 400.0, "ACTIVE", "uuid-riskmitigationstrategy-05");

CREATE TABLE IF NOT EXISTS risk_management_actionownerassignments (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_actionownerassignments_code ON risk_management_actionownerassignments(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_actionownerassignments_org_status ON risk_management_actionownerassignments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_actionownerassignments_priority ON risk_management_actionownerassignments(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_actionownerassignments_created_at ON risk_management_actionownerassignments(created_at);

-- Operational seed data fixtures for risk_management_actionownerassignments
INSERT OR IGNORE INTO risk_management_actionownerassignments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACT-0001", "Primary Operational ActionOwnerAssignment 1", 24500.00, 150.0, "ACTIVE", "uuid-actionownerassignment-01"),
    (2, "ACT-0002", "Secondary Corporate ActionOwnerAssignment 2", 18200.50, 80.0, "ACTIVE", "uuid-actionownerassignment-02"),
    (3, "ACT-0003", "Consolidated Branch ActionOwnerAssignment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-actionownerassignment-03"),
    (4, "ACT-0004", "Enterprise Audited ActionOwnerAssignment 4", 32800.00, 210.0, "ACTIVE", "uuid-actionownerassignment-04"),
    (5, "ACT-0005", "Executive Strategic ActionOwnerAssignment 5", 65000.00, 400.0, "ACTIVE", "uuid-actionownerassignment-05");

CREATE TABLE IF NOT EXISTS risk_management_scenariostresstests (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_scenariostresstests_code ON risk_management_scenariostresstests(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_scenariostresstests_org_status ON risk_management_scenariostresstests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_scenariostresstests_priority ON risk_management_scenariostresstests(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_scenariostresstests_created_at ON risk_management_scenariostresstests(created_at);

-- Operational seed data fixtures for risk_management_scenariostresstests
INSERT OR IGNORE INTO risk_management_scenariostresstests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SCE-0001", "Primary Operational ScenarioStressTest 1", 24500.00, 150.0, "ACTIVE", "uuid-scenariostresstest-01"),
    (2, "SCE-0002", "Secondary Corporate ScenarioStressTest 2", 18200.50, 80.0, "ACTIVE", "uuid-scenariostresstest-02"),
    (3, "SCE-0003", "Consolidated Branch ScenarioStressTest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-scenariostresstest-03"),
    (4, "SCE-0004", "Enterprise Audited ScenarioStressTest 4", 32800.00, 210.0, "ACTIVE", "uuid-scenariostresstest-04"),
    (5, "SCE-0005", "Executive Strategic ScenarioStressTest 5", 65000.00, 400.0, "ACTIVE", "uuid-scenariostresstest-05");

CREATE TABLE IF NOT EXISTS risk_management_losseventincidents (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_losseventincidents_code ON risk_management_losseventincidents(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_losseventincidents_org_status ON risk_management_losseventincidents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_losseventincidents_priority ON risk_management_losseventincidents(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_losseventincidents_created_at ON risk_management_losseventincidents(created_at);

-- Operational seed data fixtures for risk_management_losseventincidents
INSERT OR IGNORE INTO risk_management_losseventincidents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LOS-0001", "Primary Operational LossEventIncident 1", 24500.00, 150.0, "ACTIVE", "uuid-losseventincident-01"),
    (2, "LOS-0002", "Secondary Corporate LossEventIncident 2", 18200.50, 80.0, "ACTIVE", "uuid-losseventincident-02"),
    (3, "LOS-0003", "Consolidated Branch LossEventIncident 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-losseventincident-03"),
    (4, "LOS-0004", "Enterprise Audited LossEventIncident 4", 32800.00, 210.0, "ACTIVE", "uuid-losseventincident-04"),
    (5, "LOS-0005", "Executive Strategic LossEventIncident 5", 65000.00, 400.0, "ACTIVE", "uuid-losseventincident-05");

CREATE TABLE IF NOT EXISTS risk_management_businesscontinuityplans (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_businesscontinuityplans_code ON risk_management_businesscontinuityplans(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_businesscontinuityplans_org_status ON risk_management_businesscontinuityplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_businesscontinuityplans_priority ON risk_management_businesscontinuityplans(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_businesscontinuityplans_created_at ON risk_management_businesscontinuityplans(created_at);

-- Operational seed data fixtures for risk_management_businesscontinuityplans
INSERT OR IGNORE INTO risk_management_businesscontinuityplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BUS-0001", "Primary Operational BusinessContinuityPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-businesscontinuityplan-01"),
    (2, "BUS-0002", "Secondary Corporate BusinessContinuityPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-businesscontinuityplan-02"),
    (3, "BUS-0003", "Consolidated Branch BusinessContinuityPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-businesscontinuityplan-03"),
    (4, "BUS-0004", "Enterprise Audited BusinessContinuityPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-businesscontinuityplan-04"),
    (5, "BUS-0005", "Executive Strategic BusinessContinuityPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-businesscontinuityplan-05");

CREATE TABLE IF NOT EXISTS risk_management_disasterrecoveryscenarios (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_disasterrecoveryscenarios_code ON risk_management_disasterrecoveryscenarios(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_disasterrecoveryscenarios_org_status ON risk_management_disasterrecoveryscenarios(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_disasterrecoveryscenarios_priority ON risk_management_disasterrecoveryscenarios(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_disasterrecoveryscenarios_created_at ON risk_management_disasterrecoveryscenarios(created_at);

-- Operational seed data fixtures for risk_management_disasterrecoveryscenarios
INSERT OR IGNORE INTO risk_management_disasterrecoveryscenarios (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DisasterRecoveryScenario 1", 24500.00, 150.0, "ACTIVE", "uuid-disasterrecoveryscenario-01"),
    (2, "DIS-0002", "Secondary Corporate DisasterRecoveryScenario 2", 18200.50, 80.0, "ACTIVE", "uuid-disasterrecoveryscenario-02"),
    (3, "DIS-0003", "Consolidated Branch DisasterRecoveryScenario 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-disasterrecoveryscenario-03"),
    (4, "DIS-0004", "Enterprise Audited DisasterRecoveryScenario 4", 32800.00, 210.0, "ACTIVE", "uuid-disasterrecoveryscenario-04"),
    (5, "DIS-0005", "Executive Strategic DisasterRecoveryScenario 5", 65000.00, 400.0, "ACTIVE", "uuid-disasterrecoveryscenario-05");

CREATE TABLE IF NOT EXISTS risk_management_residualriskevaluations (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_residualriskevaluations_code ON risk_management_residualriskevaluations(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_residualriskevaluations_org_status ON risk_management_residualriskevaluations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_residualriskevaluations_priority ON risk_management_residualriskevaluations(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_residualriskevaluations_created_at ON risk_management_residualriskevaluations(created_at);

-- Operational seed data fixtures for risk_management_residualriskevaluations
INSERT OR IGNORE INTO risk_management_residualriskevaluations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RES-0001", "Primary Operational ResidualRiskEvaluation 1", 24500.00, 150.0, "ACTIVE", "uuid-residualriskevaluation-01"),
    (2, "RES-0002", "Secondary Corporate ResidualRiskEvaluation 2", 18200.50, 80.0, "ACTIVE", "uuid-residualriskevaluation-02"),
    (3, "RES-0003", "Consolidated Branch ResidualRiskEvaluation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-residualriskevaluation-03"),
    (4, "RES-0004", "Enterprise Audited ResidualRiskEvaluation 4", 32800.00, 210.0, "ACTIVE", "uuid-residualriskevaluation-04"),
    (5, "RES-0005", "Executive Strategic ResidualRiskEvaluation 5", 65000.00, 400.0, "ACTIVE", "uuid-residualriskevaluation-05");

CREATE TABLE IF NOT EXISTS risk_management_riskappetitestatements (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_riskappetitestatements_code ON risk_management_riskappetitestatements(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskappetitestatements_org_status ON risk_management_riskappetitestatements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskappetitestatements_priority ON risk_management_riskappetitestatements(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskappetitestatements_created_at ON risk_management_riskappetitestatements(created_at);

-- Operational seed data fixtures for risk_management_riskappetitestatements
INSERT OR IGNORE INTO risk_management_riskappetitestatements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RIS-0001", "Primary Operational RiskAppetiteStatement 1", 24500.00, 150.0, "ACTIVE", "uuid-riskappetitestatement-01"),
    (2, "RIS-0002", "Secondary Corporate RiskAppetiteStatement 2", 18200.50, 80.0, "ACTIVE", "uuid-riskappetitestatement-02"),
    (3, "RIS-0003", "Consolidated Branch RiskAppetiteStatement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-riskappetitestatement-03"),
    (4, "RIS-0004", "Enterprise Audited RiskAppetiteStatement 4", 32800.00, 210.0, "ACTIVE", "uuid-riskappetitestatement-04"),
    (5, "RIS-0005", "Executive Strategic RiskAppetiteStatement 5", 65000.00, 400.0, "ACTIVE", "uuid-riskappetitestatement-05");

CREATE TABLE IF NOT EXISTS risk_management_insurancecoveragelinks (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_insurancecoveragelinks_code ON risk_management_insurancecoveragelinks(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_insurancecoveragelinks_org_status ON risk_management_insurancecoveragelinks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_insurancecoveragelinks_priority ON risk_management_insurancecoveragelinks(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_insurancecoveragelinks_created_at ON risk_management_insurancecoveragelinks(created_at);

-- Operational seed data fixtures for risk_management_insurancecoveragelinks
INSERT OR IGNORE INTO risk_management_insurancecoveragelinks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INS-0001", "Primary Operational InsuranceCoverageLink 1", 24500.00, 150.0, "ACTIVE", "uuid-insurancecoveragelink-01"),
    (2, "INS-0002", "Secondary Corporate InsuranceCoverageLink 2", 18200.50, 80.0, "ACTIVE", "uuid-insurancecoveragelink-02"),
    (3, "INS-0003", "Consolidated Branch InsuranceCoverageLink 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-insurancecoveragelink-03"),
    (4, "INS-0004", "Enterprise Audited InsuranceCoverageLink 4", 32800.00, 210.0, "ACTIVE", "uuid-insurancecoveragelink-04"),
    (5, "INS-0005", "Executive Strategic InsuranceCoverageLink 5", 65000.00, 400.0, "ACTIVE", "uuid-insurancecoveragelink-05");

CREATE TABLE IF NOT EXISTS risk_management_riskcommitteereports (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_riskcommitteereports_code ON risk_management_riskcommitteereports(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskcommitteereports_org_status ON risk_management_riskcommitteereports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskcommitteereports_priority ON risk_management_riskcommitteereports(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_riskcommitteereports_created_at ON risk_management_riskcommitteereports(created_at);

-- Operational seed data fixtures for risk_management_riskcommitteereports
INSERT OR IGNORE INTO risk_management_riskcommitteereports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RIS-0001", "Primary Operational RiskCommitteeReport 1", 24500.00, 150.0, "ACTIVE", "uuid-riskcommitteereport-01"),
    (2, "RIS-0002", "Secondary Corporate RiskCommitteeReport 2", 18200.50, 80.0, "ACTIVE", "uuid-riskcommitteereport-02"),
    (3, "RIS-0003", "Consolidated Branch RiskCommitteeReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-riskcommitteereport-03"),
    (4, "RIS-0004", "Enterprise Audited RiskCommitteeReport 4", 32800.00, 210.0, "ACTIVE", "uuid-riskcommitteereport-04"),
    (5, "RIS-0005", "Executive Strategic RiskCommitteeReport 5", 65000.00, 400.0, "ACTIVE", "uuid-riskcommitteereport-05");

CREATE TABLE IF NOT EXISTS risk_management_auditrecommendations (
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

CREATE INDEX IF NOT EXISTS idx_risk_management_auditrecommendations_code ON risk_management_auditrecommendations(code);
CREATE INDEX IF NOT EXISTS idx_risk_management_auditrecommendations_org_status ON risk_management_auditrecommendations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_risk_management_auditrecommendations_priority ON risk_management_auditrecommendations(priority);
CREATE INDEX IF NOT EXISTS idx_risk_management_auditrecommendations_created_at ON risk_management_auditrecommendations(created_at);

-- Operational seed data fixtures for risk_management_auditrecommendations
INSERT OR IGNORE INTO risk_management_auditrecommendations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "AUD-0001", "Primary Operational AuditRecommendation 1", 24500.00, 150.0, "ACTIVE", "uuid-auditrecommendation-01"),
    (2, "AUD-0002", "Secondary Corporate AuditRecommendation 2", 18200.50, 80.0, "ACTIVE", "uuid-auditrecommendation-02"),
    (3, "AUD-0003", "Consolidated Branch AuditRecommendation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-auditrecommendation-03"),
    (4, "AUD-0004", "Enterprise Audited AuditRecommendation 4", 32800.00, 210.0, "ACTIVE", "uuid-auditrecommendation-04"),
    (5, "AUD-0005", "Executive Strategic AuditRecommendation 5", 65000.00, 400.0, "ACTIVE", "uuid-auditrecommendation-05");

