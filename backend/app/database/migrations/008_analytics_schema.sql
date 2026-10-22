-- SmartERP Enterprise Titan Migration 008: Executive Business Intelligence & OLAP DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS analytics_datacubes (
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

CREATE INDEX IF NOT EXISTS idx_analytics_datacubes_code ON analytics_datacubes(code);
CREATE INDEX IF NOT EXISTS idx_analytics_datacubes_org_status ON analytics_datacubes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_datacubes_priority ON analytics_datacubes(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_datacubes_created_at ON analytics_datacubes(created_at);

-- Operational seed data fixtures for analytics_datacubes
INSERT OR IGNORE INTO analytics_datacubes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataCube 1", 24500.00, 150.0, "ACTIVE", "uuid-datacube-01"),
    (2, "DAT-0002", "Secondary Corporate DataCube 2", 18200.50, 80.0, "ACTIVE", "uuid-datacube-02"),
    (3, "DAT-0003", "Consolidated Branch DataCube 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-datacube-03"),
    (4, "DAT-0004", "Enterprise Audited DataCube 4", 32800.00, 210.0, "ACTIVE", "uuid-datacube-04"),
    (5, "DAT-0005", "Executive Strategic DataCube 5", 65000.00, 400.0, "ACTIVE", "uuid-datacube-05");

CREATE TABLE IF NOT EXISTS analytics_metricdefinitions (
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

CREATE INDEX IF NOT EXISTS idx_analytics_metricdefinitions_code ON analytics_metricdefinitions(code);
CREATE INDEX IF NOT EXISTS idx_analytics_metricdefinitions_org_status ON analytics_metricdefinitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_metricdefinitions_priority ON analytics_metricdefinitions(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_metricdefinitions_created_at ON analytics_metricdefinitions(created_at);

-- Operational seed data fixtures for analytics_metricdefinitions
INSERT OR IGNORE INTO analytics_metricdefinitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MET-0001", "Primary Operational MetricDefinition 1", 24500.00, 150.0, "ACTIVE", "uuid-metricdefinition-01"),
    (2, "MET-0002", "Secondary Corporate MetricDefinition 2", 18200.50, 80.0, "ACTIVE", "uuid-metricdefinition-02"),
    (3, "MET-0003", "Consolidated Branch MetricDefinition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-metricdefinition-03"),
    (4, "MET-0004", "Enterprise Audited MetricDefinition 4", 32800.00, 210.0, "ACTIVE", "uuid-metricdefinition-04"),
    (5, "MET-0005", "Executive Strategic MetricDefinition 5", 65000.00, 400.0, "ACTIVE", "uuid-metricdefinition-05");

CREATE TABLE IF NOT EXISTS analytics_dimensionfilters (
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

CREATE INDEX IF NOT EXISTS idx_analytics_dimensionfilters_code ON analytics_dimensionfilters(code);
CREATE INDEX IF NOT EXISTS idx_analytics_dimensionfilters_org_status ON analytics_dimensionfilters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_dimensionfilters_priority ON analytics_dimensionfilters(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_dimensionfilters_created_at ON analytics_dimensionfilters(created_at);

-- Operational seed data fixtures for analytics_dimensionfilters
INSERT OR IGNORE INTO analytics_dimensionfilters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIM-0001", "Primary Operational DimensionFilter 1", 24500.00, 150.0, "ACTIVE", "uuid-dimensionfilter-01"),
    (2, "DIM-0002", "Secondary Corporate DimensionFilter 2", 18200.50, 80.0, "ACTIVE", "uuid-dimensionfilter-02"),
    (3, "DIM-0003", "Consolidated Branch DimensionFilter 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dimensionfilter-03"),
    (4, "DIM-0004", "Enterprise Audited DimensionFilter 4", 32800.00, 210.0, "ACTIVE", "uuid-dimensionfilter-04"),
    (5, "DIM-0005", "Executive Strategic DimensionFilter 5", 65000.00, 400.0, "ACTIVE", "uuid-dimensionfilter-05");

CREATE TABLE IF NOT EXISTS analytics_dashboardwidgets (
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

CREATE INDEX IF NOT EXISTS idx_analytics_dashboardwidgets_code ON analytics_dashboardwidgets(code);
CREATE INDEX IF NOT EXISTS idx_analytics_dashboardwidgets_org_status ON analytics_dashboardwidgets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_dashboardwidgets_priority ON analytics_dashboardwidgets(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_dashboardwidgets_created_at ON analytics_dashboardwidgets(created_at);

-- Operational seed data fixtures for analytics_dashboardwidgets
INSERT OR IGNORE INTO analytics_dashboardwidgets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAS-0001", "Primary Operational DashboardWidget 1", 24500.00, 150.0, "ACTIVE", "uuid-dashboardwidget-01"),
    (2, "DAS-0002", "Secondary Corporate DashboardWidget 2", 18200.50, 80.0, "ACTIVE", "uuid-dashboardwidget-02"),
    (3, "DAS-0003", "Consolidated Branch DashboardWidget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dashboardwidget-03"),
    (4, "DAS-0004", "Enterprise Audited DashboardWidget 4", 32800.00, 210.0, "ACTIVE", "uuid-dashboardwidget-04"),
    (5, "DAS-0005", "Executive Strategic DashboardWidget 5", 65000.00, 400.0, "ACTIVE", "uuid-dashboardwidget-05");

CREATE TABLE IF NOT EXISTS analytics_cohortanalysiss (
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

CREATE INDEX IF NOT EXISTS idx_analytics_cohortanalysiss_code ON analytics_cohortanalysiss(code);
CREATE INDEX IF NOT EXISTS idx_analytics_cohortanalysiss_org_status ON analytics_cohortanalysiss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_cohortanalysiss_priority ON analytics_cohortanalysiss(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_cohortanalysiss_created_at ON analytics_cohortanalysiss(created_at);

-- Operational seed data fixtures for analytics_cohortanalysiss
INSERT OR IGNORE INTO analytics_cohortanalysiss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COH-0001", "Primary Operational CohortAnalysis 1", 24500.00, 150.0, "ACTIVE", "uuid-cohortanalysis-01"),
    (2, "COH-0002", "Secondary Corporate CohortAnalysis 2", 18200.50, 80.0, "ACTIVE", "uuid-cohortanalysis-02"),
    (3, "COH-0003", "Consolidated Branch CohortAnalysis 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cohortanalysis-03"),
    (4, "COH-0004", "Enterprise Audited CohortAnalysis 4", 32800.00, 210.0, "ACTIVE", "uuid-cohortanalysis-04"),
    (5, "COH-0005", "Executive Strategic CohortAnalysis 5", 65000.00, 400.0, "ACTIVE", "uuid-cohortanalysis-05");

CREATE TABLE IF NOT EXISTS analytics_forecastmodels (
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

CREATE INDEX IF NOT EXISTS idx_analytics_forecastmodels_code ON analytics_forecastmodels(code);
CREATE INDEX IF NOT EXISTS idx_analytics_forecastmodels_org_status ON analytics_forecastmodels(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_forecastmodels_priority ON analytics_forecastmodels(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_forecastmodels_created_at ON analytics_forecastmodels(created_at);

-- Operational seed data fixtures for analytics_forecastmodels
INSERT OR IGNORE INTO analytics_forecastmodels (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FOR-0001", "Primary Operational ForecastModel 1", 24500.00, 150.0, "ACTIVE", "uuid-forecastmodel-01"),
    (2, "FOR-0002", "Secondary Corporate ForecastModel 2", 18200.50, 80.0, "ACTIVE", "uuid-forecastmodel-02"),
    (3, "FOR-0003", "Consolidated Branch ForecastModel 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-forecastmodel-03"),
    (4, "FOR-0004", "Enterprise Audited ForecastModel 4", 32800.00, 210.0, "ACTIVE", "uuid-forecastmodel-04"),
    (5, "FOR-0005", "Executive Strategic ForecastModel 5", 65000.00, 400.0, "ACTIVE", "uuid-forecastmodel-05");

CREATE TABLE IF NOT EXISTS analytics_anomalyalerts (
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

CREATE INDEX IF NOT EXISTS idx_analytics_anomalyalerts_code ON analytics_anomalyalerts(code);
CREATE INDEX IF NOT EXISTS idx_analytics_anomalyalerts_org_status ON analytics_anomalyalerts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_anomalyalerts_priority ON analytics_anomalyalerts(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_anomalyalerts_created_at ON analytics_anomalyalerts(created_at);

-- Operational seed data fixtures for analytics_anomalyalerts
INSERT OR IGNORE INTO analytics_anomalyalerts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ANO-0001", "Primary Operational AnomalyAlert 1", 24500.00, 150.0, "ACTIVE", "uuid-anomalyalert-01"),
    (2, "ANO-0002", "Secondary Corporate AnomalyAlert 2", 18200.50, 80.0, "ACTIVE", "uuid-anomalyalert-02"),
    (3, "ANO-0003", "Consolidated Branch AnomalyAlert 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-anomalyalert-03"),
    (4, "ANO-0004", "Enterprise Audited AnomalyAlert 4", 32800.00, 210.0, "ACTIVE", "uuid-anomalyalert-04"),
    (5, "ANO-0005", "Executive Strategic AnomalyAlert 5", 65000.00, 400.0, "ACTIVE", "uuid-anomalyalert-05");

CREATE TABLE IF NOT EXISTS analytics_executivekpis (
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

CREATE INDEX IF NOT EXISTS idx_analytics_executivekpis_code ON analytics_executivekpis(code);
CREATE INDEX IF NOT EXISTS idx_analytics_executivekpis_org_status ON analytics_executivekpis(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_executivekpis_priority ON analytics_executivekpis(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_executivekpis_created_at ON analytics_executivekpis(created_at);

-- Operational seed data fixtures for analytics_executivekpis
INSERT OR IGNORE INTO analytics_executivekpis (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutiveKPI 1", 24500.00, 150.0, "ACTIVE", "uuid-executivekpi-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutiveKPI 2", 18200.50, 80.0, "ACTIVE", "uuid-executivekpi-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutiveKPI 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executivekpi-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutiveKPI 4", 32800.00, 210.0, "ACTIVE", "uuid-executivekpi-04"),
    (5, "EXE-0005", "Executive Strategic ExecutiveKPI 5", 65000.00, 400.0, "ACTIVE", "uuid-executivekpi-05");

CREATE TABLE IF NOT EXISTS analytics_reportschedules (
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

CREATE INDEX IF NOT EXISTS idx_analytics_reportschedules_code ON analytics_reportschedules(code);
CREATE INDEX IF NOT EXISTS idx_analytics_reportschedules_org_status ON analytics_reportschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_reportschedules_priority ON analytics_reportschedules(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_reportschedules_created_at ON analytics_reportschedules(created_at);

-- Operational seed data fixtures for analytics_reportschedules
INSERT OR IGNORE INTO analytics_reportschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REP-0001", "Primary Operational ReportSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-reportschedule-01"),
    (2, "REP-0002", "Secondary Corporate ReportSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-reportschedule-02"),
    (3, "REP-0003", "Consolidated Branch ReportSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-reportschedule-03"),
    (4, "REP-0004", "Enterprise Audited ReportSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-reportschedule-04"),
    (5, "REP-0005", "Executive Strategic ReportSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-reportschedule-05");

CREATE TABLE IF NOT EXISTS analytics_userretentions (
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

CREATE INDEX IF NOT EXISTS idx_analytics_userretentions_code ON analytics_userretentions(code);
CREATE INDEX IF NOT EXISTS idx_analytics_userretentions_org_status ON analytics_userretentions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_userretentions_priority ON analytics_userretentions(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_userretentions_created_at ON analytics_userretentions(created_at);

-- Operational seed data fixtures for analytics_userretentions
INSERT OR IGNORE INTO analytics_userretentions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USE-0001", "Primary Operational UserRetention 1", 24500.00, 150.0, "ACTIVE", "uuid-userretention-01"),
    (2, "USE-0002", "Secondary Corporate UserRetention 2", 18200.50, 80.0, "ACTIVE", "uuid-userretention-02"),
    (3, "USE-0003", "Consolidated Branch UserRetention 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-userretention-03"),
    (4, "USE-0004", "Enterprise Audited UserRetention 4", 32800.00, 210.0, "ACTIVE", "uuid-userretention-04"),
    (5, "USE-0005", "Executive Strategic UserRetention 5", 65000.00, 400.0, "ACTIVE", "uuid-userretention-05");

CREATE TABLE IF NOT EXISTS analytics_ltvprojections (
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

CREATE INDEX IF NOT EXISTS idx_analytics_ltvprojections_code ON analytics_ltvprojections(code);
CREATE INDEX IF NOT EXISTS idx_analytics_ltvprojections_org_status ON analytics_ltvprojections(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_ltvprojections_priority ON analytics_ltvprojections(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_ltvprojections_created_at ON analytics_ltvprojections(created_at);

-- Operational seed data fixtures for analytics_ltvprojections
INSERT OR IGNORE INTO analytics_ltvprojections (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LTV-0001", "Primary Operational LTVProjection 1", 24500.00, 150.0, "ACTIVE", "uuid-ltvprojection-01"),
    (2, "LTV-0002", "Secondary Corporate LTVProjection 2", 18200.50, 80.0, "ACTIVE", "uuid-ltvprojection-02"),
    (3, "LTV-0003", "Consolidated Branch LTVProjection 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ltvprojection-03"),
    (4, "LTV-0004", "Enterprise Audited LTVProjection 4", 32800.00, 210.0, "ACTIVE", "uuid-ltvprojection-04"),
    (5, "LTV-0005", "Executive Strategic LTVProjection 5", 65000.00, 400.0, "ACTIVE", "uuid-ltvprojection-05");

CREATE TABLE IF NOT EXISTS analytics_inventoryturnovers (
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

CREATE INDEX IF NOT EXISTS idx_analytics_inventoryturnovers_code ON analytics_inventoryturnovers(code);
CREATE INDEX IF NOT EXISTS idx_analytics_inventoryturnovers_org_status ON analytics_inventoryturnovers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_inventoryturnovers_priority ON analytics_inventoryturnovers(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_inventoryturnovers_created_at ON analytics_inventoryturnovers(created_at);

-- Operational seed data fixtures for analytics_inventoryturnovers
INSERT OR IGNORE INTO analytics_inventoryturnovers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INV-0001", "Primary Operational InventoryTurnover 1", 24500.00, 150.0, "ACTIVE", "uuid-inventoryturnover-01"),
    (2, "INV-0002", "Secondary Corporate InventoryTurnover 2", 18200.50, 80.0, "ACTIVE", "uuid-inventoryturnover-02"),
    (3, "INV-0003", "Consolidated Branch InventoryTurnover 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inventoryturnover-03"),
    (4, "INV-0004", "Enterprise Audited InventoryTurnover 4", 32800.00, 210.0, "ACTIVE", "uuid-inventoryturnover-04"),
    (5, "INV-0005", "Executive Strategic InventoryTurnover 5", 65000.00, 400.0, "ACTIVE", "uuid-inventoryturnover-05");

CREATE TABLE IF NOT EXISTS analytics_salesattainments (
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

CREATE INDEX IF NOT EXISTS idx_analytics_salesattainments_code ON analytics_salesattainments(code);
CREATE INDEX IF NOT EXISTS idx_analytics_salesattainments_org_status ON analytics_salesattainments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_salesattainments_priority ON analytics_salesattainments(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_salesattainments_created_at ON analytics_salesattainments(created_at);

-- Operational seed data fixtures for analytics_salesattainments
INSERT OR IGNORE INTO analytics_salesattainments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAL-0001", "Primary Operational SalesAttainment 1", 24500.00, 150.0, "ACTIVE", "uuid-salesattainment-01"),
    (2, "SAL-0002", "Secondary Corporate SalesAttainment 2", 18200.50, 80.0, "ACTIVE", "uuid-salesattainment-02"),
    (3, "SAL-0003", "Consolidated Branch SalesAttainment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-salesattainment-03"),
    (4, "SAL-0004", "Enterprise Audited SalesAttainment 4", 32800.00, 210.0, "ACTIVE", "uuid-salesattainment-04"),
    (5, "SAL-0005", "Executive Strategic SalesAttainment 5", 65000.00, 400.0, "ACTIVE", "uuid-salesattainment-05");

CREATE TABLE IF NOT EXISTS analytics_financialspreads (
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

CREATE INDEX IF NOT EXISTS idx_analytics_financialspreads_code ON analytics_financialspreads(code);
CREATE INDEX IF NOT EXISTS idx_analytics_financialspreads_org_status ON analytics_financialspreads(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_financialspreads_priority ON analytics_financialspreads(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_financialspreads_created_at ON analytics_financialspreads(created_at);

-- Operational seed data fixtures for analytics_financialspreads
INSERT OR IGNORE INTO analytics_financialspreads (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FIN-0001", "Primary Operational FinancialSpread 1", 24500.00, 150.0, "ACTIVE", "uuid-financialspread-01"),
    (2, "FIN-0002", "Secondary Corporate FinancialSpread 2", 18200.50, 80.0, "ACTIVE", "uuid-financialspread-02"),
    (3, "FIN-0003", "Consolidated Branch FinancialSpread 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-financialspread-03"),
    (4, "FIN-0004", "Enterprise Audited FinancialSpread 4", 32800.00, 210.0, "ACTIVE", "uuid-financialspread-04"),
    (5, "FIN-0005", "Executive Strategic FinancialSpread 5", 65000.00, 400.0, "ACTIVE", "uuid-financialspread-05");

CREATE TABLE IF NOT EXISTS analytics_benchmarkcomparisons (
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

CREATE INDEX IF NOT EXISTS idx_analytics_benchmarkcomparisons_code ON analytics_benchmarkcomparisons(code);
CREATE INDEX IF NOT EXISTS idx_analytics_benchmarkcomparisons_org_status ON analytics_benchmarkcomparisons(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_benchmarkcomparisons_priority ON analytics_benchmarkcomparisons(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_benchmarkcomparisons_created_at ON analytics_benchmarkcomparisons(created_at);

-- Operational seed data fixtures for analytics_benchmarkcomparisons
INSERT OR IGNORE INTO analytics_benchmarkcomparisons (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BEN-0001", "Primary Operational BenchmarkComparison 1", 24500.00, 150.0, "ACTIVE", "uuid-benchmarkcomparison-01"),
    (2, "BEN-0002", "Secondary Corporate BenchmarkComparison 2", 18200.50, 80.0, "ACTIVE", "uuid-benchmarkcomparison-02"),
    (3, "BEN-0003", "Consolidated Branch BenchmarkComparison 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-benchmarkcomparison-03"),
    (4, "BEN-0004", "Enterprise Audited BenchmarkComparison 4", 32800.00, 210.0, "ACTIVE", "uuid-benchmarkcomparison-04"),
    (5, "BEN-0005", "Executive Strategic BenchmarkComparison 5", 65000.00, 400.0, "ACTIVE", "uuid-benchmarkcomparison-05");

CREATE TABLE IF NOT EXISTS analytics_exportjobs (
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

CREATE INDEX IF NOT EXISTS idx_analytics_exportjobs_code ON analytics_exportjobs(code);
CREATE INDEX IF NOT EXISTS idx_analytics_exportjobs_org_status ON analytics_exportjobs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_analytics_exportjobs_priority ON analytics_exportjobs(priority);
CREATE INDEX IF NOT EXISTS idx_analytics_exportjobs_created_at ON analytics_exportjobs(created_at);

-- Operational seed data fixtures for analytics_exportjobs
INSERT OR IGNORE INTO analytics_exportjobs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExportJob 1", 24500.00, 150.0, "ACTIVE", "uuid-exportjob-01"),
    (2, "EXP-0002", "Secondary Corporate ExportJob 2", 18200.50, 80.0, "ACTIVE", "uuid-exportjob-02"),
    (3, "EXP-0003", "Consolidated Branch ExportJob 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-exportjob-03"),
    (4, "EXP-0004", "Enterprise Audited ExportJob 4", 32800.00, 210.0, "ACTIVE", "uuid-exportjob-04"),
    (5, "EXP-0005", "Executive Strategic ExportJob 5", 65000.00, 400.0, "ACTIVE", "uuid-exportjob-05");

