-- SmartERP Enterprise Titan Migration 016: Quality Management & CAPA Engine DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS quality_assurance_inspectionplantemplates (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_inspectionplantemplates_code ON quality_assurance_inspectionplantemplates(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_inspectionplantemplates_org_status ON quality_assurance_inspectionplantemplates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_inspectionplantemplates_priority ON quality_assurance_inspectionplantemplates(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_inspectionplantemplates_created_at ON quality_assurance_inspectionplantemplates(created_at);

-- Operational seed data fixtures for quality_assurance_inspectionplantemplates
INSERT OR IGNORE INTO quality_assurance_inspectionplantemplates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INS-0001", "Primary Operational InspectionPlanTemplate 1", 24500.00, 150.0, "ACTIVE", "uuid-inspectionplantemplate-01"),
    (2, "INS-0002", "Secondary Corporate InspectionPlanTemplate 2", 18200.50, 80.0, "ACTIVE", "uuid-inspectionplantemplate-02"),
    (3, "INS-0003", "Consolidated Branch InspectionPlanTemplate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inspectionplantemplate-03"),
    (4, "INS-0004", "Enterprise Audited InspectionPlanTemplate 4", 32800.00, 210.0, "ACTIVE", "uuid-inspectionplantemplate-04"),
    (5, "INS-0005", "Executive Strategic InspectionPlanTemplate 5", 65000.00, 400.0, "ACTIVE", "uuid-inspectionplantemplate-05");

CREATE TABLE IF NOT EXISTS quality_assurance_incominginspectionrecords (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_incominginspectionrecords_code ON quality_assurance_incominginspectionrecords(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_incominginspectionrecords_org_status ON quality_assurance_incominginspectionrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_incominginspectionrecords_priority ON quality_assurance_incominginspectionrecords(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_incominginspectionrecords_created_at ON quality_assurance_incominginspectionrecords(created_at);

-- Operational seed data fixtures for quality_assurance_incominginspectionrecords
INSERT OR IGNORE INTO quality_assurance_incominginspectionrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INC-0001", "Primary Operational IncomingInspectionRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-incominginspectionrecord-01"),
    (2, "INC-0002", "Secondary Corporate IncomingInspectionRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-incominginspectionrecord-02"),
    (3, "INC-0003", "Consolidated Branch IncomingInspectionRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-incominginspectionrecord-03"),
    (4, "INC-0004", "Enterprise Audited IncomingInspectionRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-incominginspectionrecord-04"),
    (5, "INC-0005", "Executive Strategic IncomingInspectionRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-incominginspectionrecord-05");

CREATE TABLE IF NOT EXISTS quality_assurance_inprocessaudits (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_inprocessaudits_code ON quality_assurance_inprocessaudits(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_inprocessaudits_org_status ON quality_assurance_inprocessaudits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_inprocessaudits_priority ON quality_assurance_inprocessaudits(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_inprocessaudits_created_at ON quality_assurance_inprocessaudits(created_at);

-- Operational seed data fixtures for quality_assurance_inprocessaudits
INSERT OR IGNORE INTO quality_assurance_inprocessaudits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INP-0001", "Primary Operational InProcessAudit 1", 24500.00, 150.0, "ACTIVE", "uuid-inprocessaudit-01"),
    (2, "INP-0002", "Secondary Corporate InProcessAudit 2", 18200.50, 80.0, "ACTIVE", "uuid-inprocessaudit-02"),
    (3, "INP-0003", "Consolidated Branch InProcessAudit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inprocessaudit-03"),
    (4, "INP-0004", "Enterprise Audited InProcessAudit 4", 32800.00, 210.0, "ACTIVE", "uuid-inprocessaudit-04"),
    (5, "INP-0005", "Executive Strategic InProcessAudit 5", 65000.00, 400.0, "ACTIVE", "uuid-inprocessaudit-05");

CREATE TABLE IF NOT EXISTS quality_assurance_finalreleaseinspections (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_finalreleaseinspections_code ON quality_assurance_finalreleaseinspections(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_finalreleaseinspections_org_status ON quality_assurance_finalreleaseinspections(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_finalreleaseinspections_priority ON quality_assurance_finalreleaseinspections(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_finalreleaseinspections_created_at ON quality_assurance_finalreleaseinspections(created_at);

-- Operational seed data fixtures for quality_assurance_finalreleaseinspections
INSERT OR IGNORE INTO quality_assurance_finalreleaseinspections (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FIN-0001", "Primary Operational FinalReleaseInspection 1", 24500.00, 150.0, "ACTIVE", "uuid-finalreleaseinspection-01"),
    (2, "FIN-0002", "Secondary Corporate FinalReleaseInspection 2", 18200.50, 80.0, "ACTIVE", "uuid-finalreleaseinspection-02"),
    (3, "FIN-0003", "Consolidated Branch FinalReleaseInspection 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-finalreleaseinspection-03"),
    (4, "FIN-0004", "Enterprise Audited FinalReleaseInspection 4", 32800.00, 210.0, "ACTIVE", "uuid-finalreleaseinspection-04"),
    (5, "FIN-0005", "Executive Strategic FinalReleaseInspection 5", 65000.00, 400.0, "ACTIVE", "uuid-finalreleaseinspection-05");

CREATE TABLE IF NOT EXISTS quality_assurance_nonconformancereports (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_nonconformancereports_code ON quality_assurance_nonconformancereports(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_nonconformancereports_org_status ON quality_assurance_nonconformancereports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_nonconformancereports_priority ON quality_assurance_nonconformancereports(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_nonconformancereports_created_at ON quality_assurance_nonconformancereports(created_at);

-- Operational seed data fixtures for quality_assurance_nonconformancereports
INSERT OR IGNORE INTO quality_assurance_nonconformancereports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "NON-0001", "Primary Operational NonConformanceReport 1", 24500.00, 150.0, "ACTIVE", "uuid-nonconformancereport-01"),
    (2, "NON-0002", "Secondary Corporate NonConformanceReport 2", 18200.50, 80.0, "ACTIVE", "uuid-nonconformancereport-02"),
    (3, "NON-0003", "Consolidated Branch NonConformanceReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-nonconformancereport-03"),
    (4, "NON-0004", "Enterprise Audited NonConformanceReport 4", 32800.00, 210.0, "ACTIVE", "uuid-nonconformancereport-04"),
    (5, "NON-0005", "Executive Strategic NonConformanceReport 5", 65000.00, 400.0, "ACTIVE", "uuid-nonconformancereport-05");

CREATE TABLE IF NOT EXISTS quality_assurance_correctiveactionplans (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_correctiveactionplans_code ON quality_assurance_correctiveactionplans(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_correctiveactionplans_org_status ON quality_assurance_correctiveactionplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_correctiveactionplans_priority ON quality_assurance_correctiveactionplans(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_correctiveactionplans_created_at ON quality_assurance_correctiveactionplans(created_at);

-- Operational seed data fixtures for quality_assurance_correctiveactionplans
INSERT OR IGNORE INTO quality_assurance_correctiveactionplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COR-0001", "Primary Operational CorrectiveActionPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-correctiveactionplan-01"),
    (2, "COR-0002", "Secondary Corporate CorrectiveActionPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-correctiveactionplan-02"),
    (3, "COR-0003", "Consolidated Branch CorrectiveActionPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-correctiveactionplan-03"),
    (4, "COR-0004", "Enterprise Audited CorrectiveActionPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-correctiveactionplan-04"),
    (5, "COR-0005", "Executive Strategic CorrectiveActionPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-correctiveactionplan-05");

CREATE TABLE IF NOT EXISTS quality_assurance_preventiveactionitems (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_preventiveactionitems_code ON quality_assurance_preventiveactionitems(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_preventiveactionitems_org_status ON quality_assurance_preventiveactionitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_preventiveactionitems_priority ON quality_assurance_preventiveactionitems(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_preventiveactionitems_created_at ON quality_assurance_preventiveactionitems(created_at);

-- Operational seed data fixtures for quality_assurance_preventiveactionitems
INSERT OR IGNORE INTO quality_assurance_preventiveactionitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRE-0001", "Primary Operational PreventiveActionItem 1", 24500.00, 150.0, "ACTIVE", "uuid-preventiveactionitem-01"),
    (2, "PRE-0002", "Secondary Corporate PreventiveActionItem 2", 18200.50, 80.0, "ACTIVE", "uuid-preventiveactionitem-02"),
    (3, "PRE-0003", "Consolidated Branch PreventiveActionItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-preventiveactionitem-03"),
    (4, "PRE-0004", "Enterprise Audited PreventiveActionItem 4", 32800.00, 210.0, "ACTIVE", "uuid-preventiveactionitem-04"),
    (5, "PRE-0005", "Executive Strategic PreventiveActionItem 5", 65000.00, 400.0, "ACTIVE", "uuid-preventiveactionitem-05");

CREATE TABLE IF NOT EXISTS quality_assurance_rootcauseanalysiss (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_rootcauseanalysiss_code ON quality_assurance_rootcauseanalysiss(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_rootcauseanalysiss_org_status ON quality_assurance_rootcauseanalysiss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_rootcauseanalysiss_priority ON quality_assurance_rootcauseanalysiss(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_rootcauseanalysiss_created_at ON quality_assurance_rootcauseanalysiss(created_at);

-- Operational seed data fixtures for quality_assurance_rootcauseanalysiss
INSERT OR IGNORE INTO quality_assurance_rootcauseanalysiss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ROO-0001", "Primary Operational RootCauseAnalysis 1", 24500.00, 150.0, "ACTIVE", "uuid-rootcauseanalysis-01"),
    (2, "ROO-0002", "Secondary Corporate RootCauseAnalysis 2", 18200.50, 80.0, "ACTIVE", "uuid-rootcauseanalysis-02"),
    (3, "ROO-0003", "Consolidated Branch RootCauseAnalysis 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-rootcauseanalysis-03"),
    (4, "ROO-0004", "Enterprise Audited RootCauseAnalysis 4", 32800.00, 210.0, "ACTIVE", "uuid-rootcauseanalysis-04"),
    (5, "ROO-0005", "Executive Strategic RootCauseAnalysis 5", 65000.00, 400.0, "ACTIVE", "uuid-rootcauseanalysis-05");

CREATE TABLE IF NOT EXISTS quality_assurance_calibrationschedules (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_calibrationschedules_code ON quality_assurance_calibrationschedules(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_calibrationschedules_org_status ON quality_assurance_calibrationschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_calibrationschedules_priority ON quality_assurance_calibrationschedules(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_calibrationschedules_created_at ON quality_assurance_calibrationschedules(created_at);

-- Operational seed data fixtures for quality_assurance_calibrationschedules
INSERT OR IGNORE INTO quality_assurance_calibrationschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAL-0001", "Primary Operational CalibrationSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-calibrationschedule-01"),
    (2, "CAL-0002", "Secondary Corporate CalibrationSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-calibrationschedule-02"),
    (3, "CAL-0003", "Consolidated Branch CalibrationSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-calibrationschedule-03"),
    (4, "CAL-0004", "Enterprise Audited CalibrationSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-calibrationschedule-04"),
    (5, "CAL-0005", "Executive Strategic CalibrationSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-calibrationschedule-05");

CREATE TABLE IF NOT EXISTS quality_assurance_gaugetools (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_gaugetools_code ON quality_assurance_gaugetools(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_gaugetools_org_status ON quality_assurance_gaugetools(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_gaugetools_priority ON quality_assurance_gaugetools(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_gaugetools_created_at ON quality_assurance_gaugetools(created_at);

-- Operational seed data fixtures for quality_assurance_gaugetools
INSERT OR IGNORE INTO quality_assurance_gaugetools (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GAU-0001", "Primary Operational GaugeTool 1", 24500.00, 150.0, "ACTIVE", "uuid-gaugetool-01"),
    (2, "GAU-0002", "Secondary Corporate GaugeTool 2", 18200.50, 80.0, "ACTIVE", "uuid-gaugetool-02"),
    (3, "GAU-0003", "Consolidated Branch GaugeTool 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-gaugetool-03"),
    (4, "GAU-0004", "Enterprise Audited GaugeTool 4", 32800.00, 210.0, "ACTIVE", "uuid-gaugetool-04"),
    (5, "GAU-0005", "Executive Strategic GaugeTool 5", 65000.00, 400.0, "ACTIVE", "uuid-gaugetool-05");

CREATE TABLE IF NOT EXISTS quality_assurance_samplingstandardrules (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_samplingstandardrules_code ON quality_assurance_samplingstandardrules(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_samplingstandardrules_org_status ON quality_assurance_samplingstandardrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_samplingstandardrules_priority ON quality_assurance_samplingstandardrules(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_samplingstandardrules_created_at ON quality_assurance_samplingstandardrules(created_at);

-- Operational seed data fixtures for quality_assurance_samplingstandardrules
INSERT OR IGNORE INTO quality_assurance_samplingstandardrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAM-0001", "Primary Operational SamplingStandardRule 1", 24500.00, 150.0, "ACTIVE", "uuid-samplingstandardrule-01"),
    (2, "SAM-0002", "Secondary Corporate SamplingStandardRule 2", 18200.50, 80.0, "ACTIVE", "uuid-samplingstandardrule-02"),
    (3, "SAM-0003", "Consolidated Branch SamplingStandardRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-samplingstandardrule-03"),
    (4, "SAM-0004", "Enterprise Audited SamplingStandardRule 4", 32800.00, 210.0, "ACTIVE", "uuid-samplingstandardrule-04"),
    (5, "SAM-0005", "Executive Strategic SamplingStandardRule 5", 65000.00, 400.0, "ACTIVE", "uuid-samplingstandardrule-05");

CREATE TABLE IF NOT EXISTS quality_assurance_supplierqualityaudits (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_supplierqualityaudits_code ON quality_assurance_supplierqualityaudits(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_supplierqualityaudits_org_status ON quality_assurance_supplierqualityaudits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_supplierqualityaudits_priority ON quality_assurance_supplierqualityaudits(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_supplierqualityaudits_created_at ON quality_assurance_supplierqualityaudits(created_at);

-- Operational seed data fixtures for quality_assurance_supplierqualityaudits
INSERT OR IGNORE INTO quality_assurance_supplierqualityaudits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierQualityAudit 1", 24500.00, 150.0, "ACTIVE", "uuid-supplierqualityaudit-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierQualityAudit 2", 18200.50, 80.0, "ACTIVE", "uuid-supplierqualityaudit-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierQualityAudit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supplierqualityaudit-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierQualityAudit 4", 32800.00, 210.0, "ACTIVE", "uuid-supplierqualityaudit-04"),
    (5, "SUP-0005", "Executive Strategic SupplierQualityAudit 5", 65000.00, 400.0, "ACTIVE", "uuid-supplierqualityaudit-05");

CREATE TABLE IF NOT EXISTS quality_assurance_customercomplaintqas (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_customercomplaintqas_code ON quality_assurance_customercomplaintqas(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_customercomplaintqas_org_status ON quality_assurance_customercomplaintqas(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_customercomplaintqas_priority ON quality_assurance_customercomplaintqas(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_customercomplaintqas_created_at ON quality_assurance_customercomplaintqas(created_at);

-- Operational seed data fixtures for quality_assurance_customercomplaintqas
INSERT OR IGNORE INTO quality_assurance_customercomplaintqas (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerComplaintQA 1", 24500.00, 150.0, "ACTIVE", "uuid-customercomplaintqa-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerComplaintQA 2", 18200.50, 80.0, "ACTIVE", "uuid-customercomplaintqa-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerComplaintQA 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customercomplaintqa-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerComplaintQA 4", 32800.00, 210.0, "ACTIVE", "uuid-customercomplaintqa-04"),
    (5, "CUS-0005", "Executive Strategic CustomerComplaintQA 5", 65000.00, 400.0, "ACTIVE", "uuid-customercomplaintqa-05");

CREATE TABLE IF NOT EXISTS quality_assurance_certificateofanalysiss (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_certificateofanalysiss_code ON quality_assurance_certificateofanalysiss(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_certificateofanalysiss_org_status ON quality_assurance_certificateofanalysiss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_certificateofanalysiss_priority ON quality_assurance_certificateofanalysiss(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_certificateofanalysiss_created_at ON quality_assurance_certificateofanalysiss(created_at);

-- Operational seed data fixtures for quality_assurance_certificateofanalysiss
INSERT OR IGNORE INTO quality_assurance_certificateofanalysiss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CER-0001", "Primary Operational CertificateOfAnalysis 1", 24500.00, 150.0, "ACTIVE", "uuid-certificateofanalysis-01"),
    (2, "CER-0002", "Secondary Corporate CertificateOfAnalysis 2", 18200.50, 80.0, "ACTIVE", "uuid-certificateofanalysis-02"),
    (3, "CER-0003", "Consolidated Branch CertificateOfAnalysis 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-certificateofanalysis-03"),
    (4, "CER-0004", "Enterprise Audited CertificateOfAnalysis 4", 32800.00, 210.0, "ACTIVE", "uuid-certificateofanalysis-04"),
    (5, "CER-0005", "Executive Strategic CertificateOfAnalysis 5", 65000.00, 400.0, "ACTIVE", "uuid-certificateofanalysis-05");

CREATE TABLE IF NOT EXISTS quality_assurance_stabilitystudys (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_stabilitystudys_code ON quality_assurance_stabilitystudys(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_stabilitystudys_org_status ON quality_assurance_stabilitystudys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_stabilitystudys_priority ON quality_assurance_stabilitystudys(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_stabilitystudys_created_at ON quality_assurance_stabilitystudys(created_at);

-- Operational seed data fixtures for quality_assurance_stabilitystudys
INSERT OR IGNORE INTO quality_assurance_stabilitystudys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StabilityStudy 1", 24500.00, 150.0, "ACTIVE", "uuid-stabilitystudy-01"),
    (2, "STA-0002", "Secondary Corporate StabilityStudy 2", 18200.50, 80.0, "ACTIVE", "uuid-stabilitystudy-02"),
    (3, "STA-0003", "Consolidated Branch StabilityStudy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-stabilitystudy-03"),
    (4, "STA-0004", "Enterprise Audited StabilityStudy 4", 32800.00, 210.0, "ACTIVE", "uuid-stabilitystudy-04"),
    (5, "STA-0005", "Executive Strategic StabilityStudy 5", 65000.00, 400.0, "ACTIVE", "uuid-stabilitystudy-05");

CREATE TABLE IF NOT EXISTS quality_assurance_regulatoryauditinspections (
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

CREATE INDEX IF NOT EXISTS idx_quality_assurance_regulatoryauditinspections_code ON quality_assurance_regulatoryauditinspections(code);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_regulatoryauditinspections_org_status ON quality_assurance_regulatoryauditinspections(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_regulatoryauditinspections_priority ON quality_assurance_regulatoryauditinspections(priority);
CREATE INDEX IF NOT EXISTS idx_quality_assurance_regulatoryauditinspections_created_at ON quality_assurance_regulatoryauditinspections(created_at);

-- Operational seed data fixtures for quality_assurance_regulatoryauditinspections
INSERT OR IGNORE INTO quality_assurance_regulatoryauditinspections (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REG-0001", "Primary Operational RegulatoryAuditInspection 1", 24500.00, 150.0, "ACTIVE", "uuid-regulatoryauditinspection-01"),
    (2, "REG-0002", "Secondary Corporate RegulatoryAuditInspection 2", 18200.50, 80.0, "ACTIVE", "uuid-regulatoryauditinspection-02"),
    (3, "REG-0003", "Consolidated Branch RegulatoryAuditInspection 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-regulatoryauditinspection-03"),
    (4, "REG-0004", "Enterprise Audited RegulatoryAuditInspection 4", 32800.00, 210.0, "ACTIVE", "uuid-regulatoryauditinspection-04"),
    (5, "REG-0005", "Executive Strategic RegulatoryAuditInspection 5", 65000.00, 400.0, "ACTIVE", "uuid-regulatoryauditinspection-05");

