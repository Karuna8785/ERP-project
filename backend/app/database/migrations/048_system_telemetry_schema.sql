-- SmartERP Enterprise Titan Migration 048: Distributed Telemetry & APM Observability DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS system_telemetry_servicehealthcheckprobes (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_servicehealthcheckprobes_code ON system_telemetry_servicehealthcheckprobes(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_servicehealthcheckprobes_org_status ON system_telemetry_servicehealthcheckprobes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_servicehealthcheckprobes_priority ON system_telemetry_servicehealthcheckprobes(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_servicehealthcheckprobes_created_at ON system_telemetry_servicehealthcheckprobes(created_at);

-- Operational seed data fixtures for system_telemetry_servicehealthcheckprobes
INSERT OR IGNORE INTO system_telemetry_servicehealthcheckprobes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceHealthCheckProbe 1", 24500.00, 150.0, "ACTIVE", "uuid-servicehealthcheckprobe-01"),
    (2, "SER-0002", "Secondary Corporate ServiceHealthCheckProbe 2", 18200.50, 80.0, "ACTIVE", "uuid-servicehealthcheckprobe-02"),
    (3, "SER-0003", "Consolidated Branch ServiceHealthCheckProbe 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicehealthcheckprobe-03"),
    (4, "SER-0004", "Enterprise Audited ServiceHealthCheckProbe 4", 32800.00, 210.0, "ACTIVE", "uuid-servicehealthcheckprobe-04"),
    (5, "SER-0005", "Executive Strategic ServiceHealthCheckProbe 5", 65000.00, 400.0, "ACTIVE", "uuid-servicehealthcheckprobe-05");

CREATE TABLE IF NOT EXISTS system_telemetry_apmmetrictimeseriess (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_apmmetrictimeseriess_code ON system_telemetry_apmmetrictimeseriess(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_apmmetrictimeseriess_org_status ON system_telemetry_apmmetrictimeseriess(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_apmmetrictimeseriess_priority ON system_telemetry_apmmetrictimeseriess(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_apmmetrictimeseriess_created_at ON system_telemetry_apmmetrictimeseriess(created_at);

-- Operational seed data fixtures for system_telemetry_apmmetrictimeseriess
INSERT OR IGNORE INTO system_telemetry_apmmetrictimeseriess (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "APM-0001", "Primary Operational APMMetricTimeseries 1", 24500.00, 150.0, "ACTIVE", "uuid-apmmetrictimeseries-01"),
    (2, "APM-0002", "Secondary Corporate APMMetricTimeseries 2", 18200.50, 80.0, "ACTIVE", "uuid-apmmetrictimeseries-02"),
    (3, "APM-0003", "Consolidated Branch APMMetricTimeseries 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-apmmetrictimeseries-03"),
    (4, "APM-0004", "Enterprise Audited APMMetricTimeseries 4", 32800.00, 210.0, "ACTIVE", "uuid-apmmetrictimeseries-04"),
    (5, "APM-0005", "Executive Strategic APMMetricTimeseries 5", 65000.00, 400.0, "ACTIVE", "uuid-apmmetrictimeseries-05");

CREATE TABLE IF NOT EXISTS system_telemetry_distributedtracespans (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_distributedtracespans_code ON system_telemetry_distributedtracespans(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_distributedtracespans_org_status ON system_telemetry_distributedtracespans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_distributedtracespans_priority ON system_telemetry_distributedtracespans(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_distributedtracespans_created_at ON system_telemetry_distributedtracespans(created_at);

-- Operational seed data fixtures for system_telemetry_distributedtracespans
INSERT OR IGNORE INTO system_telemetry_distributedtracespans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DistributedTraceSpan 1", 24500.00, 150.0, "ACTIVE", "uuid-distributedtracespan-01"),
    (2, "DIS-0002", "Secondary Corporate DistributedTraceSpan 2", 18200.50, 80.0, "ACTIVE", "uuid-distributedtracespan-02"),
    (3, "DIS-0003", "Consolidated Branch DistributedTraceSpan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-distributedtracespan-03"),
    (4, "DIS-0004", "Enterprise Audited DistributedTraceSpan 4", 32800.00, 210.0, "ACTIVE", "uuid-distributedtracespan-04"),
    (5, "DIS-0005", "Executive Strategic DistributedTraceSpan 5", 65000.00, 400.0, "ACTIVE", "uuid-distributedtracespan-05");

CREATE TABLE IF NOT EXISTS system_telemetry_errorcrashreports (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_errorcrashreports_code ON system_telemetry_errorcrashreports(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_errorcrashreports_org_status ON system_telemetry_errorcrashreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_errorcrashreports_priority ON system_telemetry_errorcrashreports(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_errorcrashreports_created_at ON system_telemetry_errorcrashreports(created_at);

-- Operational seed data fixtures for system_telemetry_errorcrashreports
INSERT OR IGNORE INTO system_telemetry_errorcrashreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ERR-0001", "Primary Operational ErrorCrashReport 1", 24500.00, 150.0, "ACTIVE", "uuid-errorcrashreport-01"),
    (2, "ERR-0002", "Secondary Corporate ErrorCrashReport 2", 18200.50, 80.0, "ACTIVE", "uuid-errorcrashreport-02"),
    (3, "ERR-0003", "Consolidated Branch ErrorCrashReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-errorcrashreport-03"),
    (4, "ERR-0004", "Enterprise Audited ErrorCrashReport 4", 32800.00, 210.0, "ACTIVE", "uuid-errorcrashreport-04"),
    (5, "ERR-0005", "Executive Strategic ErrorCrashReport 5", 65000.00, 400.0, "ACTIVE", "uuid-errorcrashreport-05");

CREATE TABLE IF NOT EXISTS system_telemetry_latencyslobudgets (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_latencyslobudgets_code ON system_telemetry_latencyslobudgets(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_latencyslobudgets_org_status ON system_telemetry_latencyslobudgets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_latencyslobudgets_priority ON system_telemetry_latencyslobudgets(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_latencyslobudgets_created_at ON system_telemetry_latencyslobudgets(created_at);

-- Operational seed data fixtures for system_telemetry_latencyslobudgets
INSERT OR IGNORE INTO system_telemetry_latencyslobudgets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LAT-0001", "Primary Operational LatencySLOBudget 1", 24500.00, 150.0, "ACTIVE", "uuid-latencyslobudget-01"),
    (2, "LAT-0002", "Secondary Corporate LatencySLOBudget 2", 18200.50, 80.0, "ACTIVE", "uuid-latencyslobudget-02"),
    (3, "LAT-0003", "Consolidated Branch LatencySLOBudget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-latencyslobudget-03"),
    (4, "LAT-0004", "Enterprise Audited LatencySLOBudget 4", 32800.00, 210.0, "ACTIVE", "uuid-latencyslobudget-04"),
    (5, "LAT-0005", "Executive Strategic LatencySLOBudget 5", 65000.00, 400.0, "ACTIVE", "uuid-latencyslobudget-05");

CREATE TABLE IF NOT EXISTS system_telemetry_servernodetelemetrys (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_servernodetelemetrys_code ON system_telemetry_servernodetelemetrys(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_servernodetelemetrys_org_status ON system_telemetry_servernodetelemetrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_servernodetelemetrys_priority ON system_telemetry_servernodetelemetrys(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_servernodetelemetrys_created_at ON system_telemetry_servernodetelemetrys(created_at);

-- Operational seed data fixtures for system_telemetry_servernodetelemetrys
INSERT OR IGNORE INTO system_telemetry_servernodetelemetrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServerNodeTelemetry 1", 24500.00, 150.0, "ACTIVE", "uuid-servernodetelemetry-01"),
    (2, "SER-0002", "Secondary Corporate ServerNodeTelemetry 2", 18200.50, 80.0, "ACTIVE", "uuid-servernodetelemetry-02"),
    (3, "SER-0003", "Consolidated Branch ServerNodeTelemetry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servernodetelemetry-03"),
    (4, "SER-0004", "Enterprise Audited ServerNodeTelemetry 4", 32800.00, 210.0, "ACTIVE", "uuid-servernodetelemetry-04"),
    (5, "SER-0005", "Executive Strategic ServerNodeTelemetry 5", 65000.00, 400.0, "ACTIVE", "uuid-servernodetelemetry-05");

CREATE TABLE IF NOT EXISTS system_telemetry_databasepoolmetrics (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_databasepoolmetrics_code ON system_telemetry_databasepoolmetrics(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_databasepoolmetrics_org_status ON system_telemetry_databasepoolmetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_databasepoolmetrics_priority ON system_telemetry_databasepoolmetrics(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_databasepoolmetrics_created_at ON system_telemetry_databasepoolmetrics(created_at);

-- Operational seed data fixtures for system_telemetry_databasepoolmetrics
INSERT OR IGNORE INTO system_telemetry_databasepoolmetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DatabasePoolMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-databasepoolmetric-01"),
    (2, "DAT-0002", "Secondary Corporate DatabasePoolMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-databasepoolmetric-02"),
    (3, "DAT-0003", "Consolidated Branch DatabasePoolMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-databasepoolmetric-03"),
    (4, "DAT-0004", "Enterprise Audited DatabasePoolMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-databasepoolmetric-04"),
    (5, "DAT-0005", "Executive Strategic DatabasePoolMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-databasepoolmetric-05");

CREATE TABLE IF NOT EXISTS system_telemetry_memoryheapsnapshots (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_memoryheapsnapshots_code ON system_telemetry_memoryheapsnapshots(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_memoryheapsnapshots_org_status ON system_telemetry_memoryheapsnapshots(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_memoryheapsnapshots_priority ON system_telemetry_memoryheapsnapshots(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_memoryheapsnapshots_created_at ON system_telemetry_memoryheapsnapshots(created_at);

-- Operational seed data fixtures for system_telemetry_memoryheapsnapshots
INSERT OR IGNORE INTO system_telemetry_memoryheapsnapshots (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MEM-0001", "Primary Operational MemoryHeapSnapshot 1", 24500.00, 150.0, "ACTIVE", "uuid-memoryheapsnapshot-01"),
    (2, "MEM-0002", "Secondary Corporate MemoryHeapSnapshot 2", 18200.50, 80.0, "ACTIVE", "uuid-memoryheapsnapshot-02"),
    (3, "MEM-0003", "Consolidated Branch MemoryHeapSnapshot 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-memoryheapsnapshot-03"),
    (4, "MEM-0004", "Enterprise Audited MemoryHeapSnapshot 4", 32800.00, 210.0, "ACTIVE", "uuid-memoryheapsnapshot-04"),
    (5, "MEM-0005", "Executive Strategic MemoryHeapSnapshot 5", 65000.00, 400.0, "ACTIVE", "uuid-memoryheapsnapshot-05");

CREATE TABLE IF NOT EXISTS system_telemetry_alertescalationrules (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_alertescalationrules_code ON system_telemetry_alertescalationrules(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_alertescalationrules_org_status ON system_telemetry_alertescalationrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_alertescalationrules_priority ON system_telemetry_alertescalationrules(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_alertescalationrules_created_at ON system_telemetry_alertescalationrules(created_at);

-- Operational seed data fixtures for system_telemetry_alertescalationrules
INSERT OR IGNORE INTO system_telemetry_alertescalationrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ALE-0001", "Primary Operational AlertEscalationRule 1", 24500.00, 150.0, "ACTIVE", "uuid-alertescalationrule-01"),
    (2, "ALE-0002", "Secondary Corporate AlertEscalationRule 2", 18200.50, 80.0, "ACTIVE", "uuid-alertescalationrule-02"),
    (3, "ALE-0003", "Consolidated Branch AlertEscalationRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-alertescalationrule-03"),
    (4, "ALE-0004", "Enterprise Audited AlertEscalationRule 4", 32800.00, 210.0, "ACTIVE", "uuid-alertescalationrule-04"),
    (5, "ALE-0005", "Executive Strategic AlertEscalationRule 5", 65000.00, 400.0, "ACTIVE", "uuid-alertescalationrule-05");

CREATE TABLE IF NOT EXISTS system_telemetry_incidentpostmortems (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_incidentpostmortems_code ON system_telemetry_incidentpostmortems(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_incidentpostmortems_org_status ON system_telemetry_incidentpostmortems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_incidentpostmortems_priority ON system_telemetry_incidentpostmortems(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_incidentpostmortems_created_at ON system_telemetry_incidentpostmortems(created_at);

-- Operational seed data fixtures for system_telemetry_incidentpostmortems
INSERT OR IGNORE INTO system_telemetry_incidentpostmortems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INC-0001", "Primary Operational IncidentPostMortem 1", 24500.00, 150.0, "ACTIVE", "uuid-incidentpostmortem-01"),
    (2, "INC-0002", "Secondary Corporate IncidentPostMortem 2", 18200.50, 80.0, "ACTIVE", "uuid-incidentpostmortem-02"),
    (3, "INC-0003", "Consolidated Branch IncidentPostMortem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-incidentpostmortem-03"),
    (4, "INC-0004", "Enterprise Audited IncidentPostMortem 4", 32800.00, 210.0, "ACTIVE", "uuid-incidentpostmortem-04"),
    (5, "INC-0005", "Executive Strategic IncidentPostMortem 5", 65000.00, 400.0, "ACTIVE", "uuid-incidentpostmortem-05");

CREATE TABLE IF NOT EXISTS system_telemetry_logstreamingsinks (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_logstreamingsinks_code ON system_telemetry_logstreamingsinks(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_logstreamingsinks_org_status ON system_telemetry_logstreamingsinks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_logstreamingsinks_priority ON system_telemetry_logstreamingsinks(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_logstreamingsinks_created_at ON system_telemetry_logstreamingsinks(created_at);

-- Operational seed data fixtures for system_telemetry_logstreamingsinks
INSERT OR IGNORE INTO system_telemetry_logstreamingsinks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LOG-0001", "Primary Operational LogStreamingSink 1", 24500.00, 150.0, "ACTIVE", "uuid-logstreamingsink-01"),
    (2, "LOG-0002", "Secondary Corporate LogStreamingSink 2", 18200.50, 80.0, "ACTIVE", "uuid-logstreamingsink-02"),
    (3, "LOG-0003", "Consolidated Branch LogStreamingSink 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-logstreamingsink-03"),
    (4, "LOG-0004", "Enterprise Audited LogStreamingSink 4", 32800.00, 210.0, "ACTIVE", "uuid-logstreamingsink-04"),
    (5, "LOG-0005", "Executive Strategic LogStreamingSink 5", 65000.00, 400.0, "ACTIVE", "uuid-logstreamingsink-05");

CREATE TABLE IF NOT EXISTS system_telemetry_syntheticsmonitorjobs (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_syntheticsmonitorjobs_code ON system_telemetry_syntheticsmonitorjobs(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_syntheticsmonitorjobs_org_status ON system_telemetry_syntheticsmonitorjobs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_syntheticsmonitorjobs_priority ON system_telemetry_syntheticsmonitorjobs(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_syntheticsmonitorjobs_created_at ON system_telemetry_syntheticsmonitorjobs(created_at);

-- Operational seed data fixtures for system_telemetry_syntheticsmonitorjobs
INSERT OR IGNORE INTO system_telemetry_syntheticsmonitorjobs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SYN-0001", "Primary Operational SyntheticsMonitorJob 1", 24500.00, 150.0, "ACTIVE", "uuid-syntheticsmonitorjob-01"),
    (2, "SYN-0002", "Secondary Corporate SyntheticsMonitorJob 2", 18200.50, 80.0, "ACTIVE", "uuid-syntheticsmonitorjob-02"),
    (3, "SYN-0003", "Consolidated Branch SyntheticsMonitorJob 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-syntheticsmonitorjob-03"),
    (4, "SYN-0004", "Enterprise Audited SyntheticsMonitorJob 4", 32800.00, 210.0, "ACTIVE", "uuid-syntheticsmonitorjob-04"),
    (5, "SYN-0005", "Executive Strategic SyntheticsMonitorJob 5", 65000.00, 400.0, "ACTIVE", "uuid-syntheticsmonitorjob-05");

CREATE TABLE IF NOT EXISTS system_telemetry_capacityplanningtrends (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_capacityplanningtrends_code ON system_telemetry_capacityplanningtrends(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_capacityplanningtrends_org_status ON system_telemetry_capacityplanningtrends(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_capacityplanningtrends_priority ON system_telemetry_capacityplanningtrends(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_capacityplanningtrends_created_at ON system_telemetry_capacityplanningtrends(created_at);

-- Operational seed data fixtures for system_telemetry_capacityplanningtrends
INSERT OR IGNORE INTO system_telemetry_capacityplanningtrends (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAP-0001", "Primary Operational CapacityPlanningTrend 1", 24500.00, 150.0, "ACTIVE", "uuid-capacityplanningtrend-01"),
    (2, "CAP-0002", "Secondary Corporate CapacityPlanningTrend 2", 18200.50, 80.0, "ACTIVE", "uuid-capacityplanningtrend-02"),
    (3, "CAP-0003", "Consolidated Branch CapacityPlanningTrend 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-capacityplanningtrend-03"),
    (4, "CAP-0004", "Enterprise Audited CapacityPlanningTrend 4", 32800.00, 210.0, "ACTIVE", "uuid-capacityplanningtrend-04"),
    (5, "CAP-0005", "Executive Strategic CapacityPlanningTrend 5", 65000.00, 400.0, "ACTIVE", "uuid-capacityplanningtrend-05");

CREATE TABLE IF NOT EXISTS system_telemetry_deploymentreleasemarkers (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_deploymentreleasemarkers_code ON system_telemetry_deploymentreleasemarkers(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_deploymentreleasemarkers_org_status ON system_telemetry_deploymentreleasemarkers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_deploymentreleasemarkers_priority ON system_telemetry_deploymentreleasemarkers(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_deploymentreleasemarkers_created_at ON system_telemetry_deploymentreleasemarkers(created_at);

-- Operational seed data fixtures for system_telemetry_deploymentreleasemarkers
INSERT OR IGNORE INTO system_telemetry_deploymentreleasemarkers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DeploymentReleaseMarker 1", 24500.00, 150.0, "ACTIVE", "uuid-deploymentreleasemarker-01"),
    (2, "DEP-0002", "Secondary Corporate DeploymentReleaseMarker 2", 18200.50, 80.0, "ACTIVE", "uuid-deploymentreleasemarker-02"),
    (3, "DEP-0003", "Consolidated Branch DeploymentReleaseMarker 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-deploymentreleasemarker-03"),
    (4, "DEP-0004", "Enterprise Audited DeploymentReleaseMarker 4", 32800.00, 210.0, "ACTIVE", "uuid-deploymentreleasemarker-04"),
    (5, "DEP-0005", "Executive Strategic DeploymentReleaseMarker 5", 65000.00, 400.0, "ACTIVE", "uuid-deploymentreleasemarker-05");

CREATE TABLE IF NOT EXISTS system_telemetry_telemetrydashboardwidgets (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_telemetrydashboardwidgets_code ON system_telemetry_telemetrydashboardwidgets(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_telemetrydashboardwidgets_org_status ON system_telemetry_telemetrydashboardwidgets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_telemetrydashboardwidgets_priority ON system_telemetry_telemetrydashboardwidgets(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_telemetrydashboardwidgets_created_at ON system_telemetry_telemetrydashboardwidgets(created_at);

-- Operational seed data fixtures for system_telemetry_telemetrydashboardwidgets
INSERT OR IGNORE INTO system_telemetry_telemetrydashboardwidgets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEL-0001", "Primary Operational TelemetryDashboardWidget 1", 24500.00, 150.0, "ACTIVE", "uuid-telemetrydashboardwidget-01"),
    (2, "TEL-0002", "Secondary Corporate TelemetryDashboardWidget 2", 18200.50, 80.0, "ACTIVE", "uuid-telemetrydashboardwidget-02"),
    (3, "TEL-0003", "Consolidated Branch TelemetryDashboardWidget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-telemetrydashboardwidget-03"),
    (4, "TEL-0004", "Enterprise Audited TelemetryDashboardWidget 4", 32800.00, 210.0, "ACTIVE", "uuid-telemetrydashboardwidget-04"),
    (5, "TEL-0005", "Executive Strategic TelemetryDashboardWidget 5", 65000.00, 400.0, "ACTIVE", "uuid-telemetrydashboardwidget-05");

CREATE TABLE IF NOT EXISTS system_telemetry_anomalydetectionalerts (
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

CREATE INDEX IF NOT EXISTS idx_system_telemetry_anomalydetectionalerts_code ON system_telemetry_anomalydetectionalerts(code);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_anomalydetectionalerts_org_status ON system_telemetry_anomalydetectionalerts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_anomalydetectionalerts_priority ON system_telemetry_anomalydetectionalerts(priority);
CREATE INDEX IF NOT EXISTS idx_system_telemetry_anomalydetectionalerts_created_at ON system_telemetry_anomalydetectionalerts(created_at);

-- Operational seed data fixtures for system_telemetry_anomalydetectionalerts
INSERT OR IGNORE INTO system_telemetry_anomalydetectionalerts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ANO-0001", "Primary Operational AnomalyDetectionAlert 1", 24500.00, 150.0, "ACTIVE", "uuid-anomalydetectionalert-01"),
    (2, "ANO-0002", "Secondary Corporate AnomalyDetectionAlert 2", 18200.50, 80.0, "ACTIVE", "uuid-anomalydetectionalert-02"),
    (3, "ANO-0003", "Consolidated Branch AnomalyDetectionAlert 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-anomalydetectionalert-03"),
    (4, "ANO-0004", "Enterprise Audited AnomalyDetectionAlert 4", 32800.00, 210.0, "ACTIVE", "uuid-anomalydetectionalert-04"),
    (5, "ANO-0005", "Executive Strategic AnomalyDetectionAlert 5", 65000.00, 400.0, "ACTIVE", "uuid-anomalydetectionalert-05");

