-- SmartERP Enterprise Titan Migration 046: Data Pipeline, ETL & Data Lake Federation DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS data_pipeline_datapipelinedefinitions (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_datapipelinedefinitions_code ON data_pipeline_datapipelinedefinitions(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datapipelinedefinitions_org_status ON data_pipeline_datapipelinedefinitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datapipelinedefinitions_priority ON data_pipeline_datapipelinedefinitions(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datapipelinedefinitions_created_at ON data_pipeline_datapipelinedefinitions(created_at);

-- Operational seed data fixtures for data_pipeline_datapipelinedefinitions
INSERT OR IGNORE INTO data_pipeline_datapipelinedefinitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataPipelineDefinition 1", 24500.00, 150.0, "ACTIVE", "uuid-datapipelinedefinition-01"),
    (2, "DAT-0002", "Secondary Corporate DataPipelineDefinition 2", 18200.50, 80.0, "ACTIVE", "uuid-datapipelinedefinition-02"),
    (3, "DAT-0003", "Consolidated Branch DataPipelineDefinition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-datapipelinedefinition-03"),
    (4, "DAT-0004", "Enterprise Audited DataPipelineDefinition 4", 32800.00, 210.0, "ACTIVE", "uuid-datapipelinedefinition-04"),
    (5, "DAT-0005", "Executive Strategic DataPipelineDefinition 5", 65000.00, 400.0, "ACTIVE", "uuid-datapipelinedefinition-05");

CREATE TABLE IF NOT EXISTS data_pipeline_etljobexecutionruns (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_etljobexecutionruns_code ON data_pipeline_etljobexecutionruns(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_etljobexecutionruns_org_status ON data_pipeline_etljobexecutionruns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_etljobexecutionruns_priority ON data_pipeline_etljobexecutionruns(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_etljobexecutionruns_created_at ON data_pipeline_etljobexecutionruns(created_at);

-- Operational seed data fixtures for data_pipeline_etljobexecutionruns
INSERT OR IGNORE INTO data_pipeline_etljobexecutionruns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ETL-0001", "Primary Operational ETLJobExecutionRun 1", 24500.00, 150.0, "ACTIVE", "uuid-etljobexecutionrun-01"),
    (2, "ETL-0002", "Secondary Corporate ETLJobExecutionRun 2", 18200.50, 80.0, "ACTIVE", "uuid-etljobexecutionrun-02"),
    (3, "ETL-0003", "Consolidated Branch ETLJobExecutionRun 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-etljobexecutionrun-03"),
    (4, "ETL-0004", "Enterprise Audited ETLJobExecutionRun 4", 32800.00, 210.0, "ACTIVE", "uuid-etljobexecutionrun-04"),
    (5, "ETL-0005", "Executive Strategic ETLJobExecutionRun 5", 65000.00, 400.0, "ACTIVE", "uuid-etljobexecutionrun-05");

CREATE TABLE IF NOT EXISTS data_pipeline_datasourceconnections (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasourceconnections_code ON data_pipeline_datasourceconnections(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasourceconnections_org_status ON data_pipeline_datasourceconnections(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasourceconnections_priority ON data_pipeline_datasourceconnections(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasourceconnections_created_at ON data_pipeline_datasourceconnections(created_at);

-- Operational seed data fixtures for data_pipeline_datasourceconnections
INSERT OR IGNORE INTO data_pipeline_datasourceconnections (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataSourceConnection 1", 24500.00, 150.0, "ACTIVE", "uuid-datasourceconnection-01"),
    (2, "DAT-0002", "Secondary Corporate DataSourceConnection 2", 18200.50, 80.0, "ACTIVE", "uuid-datasourceconnection-02"),
    (3, "DAT-0003", "Consolidated Branch DataSourceConnection 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-datasourceconnection-03"),
    (4, "DAT-0004", "Enterprise Audited DataSourceConnection 4", 32800.00, 210.0, "ACTIVE", "uuid-datasourceconnection-04"),
    (5, "DAT-0005", "Executive Strategic DataSourceConnection 5", 65000.00, 400.0, "ACTIVE", "uuid-datasourceconnection-05");

CREATE TABLE IF NOT EXISTS data_pipeline_datasinkdestinations (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasinkdestinations_code ON data_pipeline_datasinkdestinations(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasinkdestinations_org_status ON data_pipeline_datasinkdestinations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasinkdestinations_priority ON data_pipeline_datasinkdestinations(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datasinkdestinations_created_at ON data_pipeline_datasinkdestinations(created_at);

-- Operational seed data fixtures for data_pipeline_datasinkdestinations
INSERT OR IGNORE INTO data_pipeline_datasinkdestinations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataSinkDestination 1", 24500.00, 150.0, "ACTIVE", "uuid-datasinkdestination-01"),
    (2, "DAT-0002", "Secondary Corporate DataSinkDestination 2", 18200.50, 80.0, "ACTIVE", "uuid-datasinkdestination-02"),
    (3, "DAT-0003", "Consolidated Branch DataSinkDestination 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-datasinkdestination-03"),
    (4, "DAT-0004", "Enterprise Audited DataSinkDestination 4", 32800.00, 210.0, "ACTIVE", "uuid-datasinkdestination-04"),
    (5, "DAT-0005", "Executive Strategic DataSinkDestination 5", 65000.00, 400.0, "ACTIVE", "uuid-datasinkdestination-05");

CREATE TABLE IF NOT EXISTS data_pipeline_schemaregistrycontracts (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_schemaregistrycontracts_code ON data_pipeline_schemaregistrycontracts(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_schemaregistrycontracts_org_status ON data_pipeline_schemaregistrycontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_schemaregistrycontracts_priority ON data_pipeline_schemaregistrycontracts(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_schemaregistrycontracts_created_at ON data_pipeline_schemaregistrycontracts(created_at);

-- Operational seed data fixtures for data_pipeline_schemaregistrycontracts
INSERT OR IGNORE INTO data_pipeline_schemaregistrycontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SCH-0001", "Primary Operational SchemaRegistryContract 1", 24500.00, 150.0, "ACTIVE", "uuid-schemaregistrycontract-01"),
    (2, "SCH-0002", "Secondary Corporate SchemaRegistryContract 2", 18200.50, 80.0, "ACTIVE", "uuid-schemaregistrycontract-02"),
    (3, "SCH-0003", "Consolidated Branch SchemaRegistryContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-schemaregistrycontract-03"),
    (4, "SCH-0004", "Enterprise Audited SchemaRegistryContract 4", 32800.00, 210.0, "ACTIVE", "uuid-schemaregistrycontract-04"),
    (5, "SCH-0005", "Executive Strategic SchemaRegistryContract 5", 65000.00, 400.0, "ACTIVE", "uuid-schemaregistrycontract-05");

CREATE TABLE IF NOT EXISTS data_pipeline_partitioningstrategyrules (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_partitioningstrategyrules_code ON data_pipeline_partitioningstrategyrules(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_partitioningstrategyrules_org_status ON data_pipeline_partitioningstrategyrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_partitioningstrategyrules_priority ON data_pipeline_partitioningstrategyrules(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_partitioningstrategyrules_created_at ON data_pipeline_partitioningstrategyrules(created_at);

-- Operational seed data fixtures for data_pipeline_partitioningstrategyrules
INSERT OR IGNORE INTO data_pipeline_partitioningstrategyrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartitioningStrategyRule 1", 24500.00, 150.0, "ACTIVE", "uuid-partitioningstrategyrule-01"),
    (2, "PAR-0002", "Secondary Corporate PartitioningStrategyRule 2", 18200.50, 80.0, "ACTIVE", "uuid-partitioningstrategyrule-02"),
    (3, "PAR-0003", "Consolidated Branch PartitioningStrategyRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partitioningstrategyrule-03"),
    (4, "PAR-0004", "Enterprise Audited PartitioningStrategyRule 4", 32800.00, 210.0, "ACTIVE", "uuid-partitioningstrategyrule-04"),
    (5, "PAR-0005", "Executive Strategic PartitioningStrategyRule 5", 65000.00, 400.0, "ACTIVE", "uuid-partitioningstrategyrule-05");

CREATE TABLE IF NOT EXISTS data_pipeline_dataqualitycheckrules (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_dataqualitycheckrules_code ON data_pipeline_dataqualitycheckrules(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_dataqualitycheckrules_org_status ON data_pipeline_dataqualitycheckrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_dataqualitycheckrules_priority ON data_pipeline_dataqualitycheckrules(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_dataqualitycheckrules_created_at ON data_pipeline_dataqualitycheckrules(created_at);

-- Operational seed data fixtures for data_pipeline_dataqualitycheckrules
INSERT OR IGNORE INTO data_pipeline_dataqualitycheckrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataQualityCheckRule 1", 24500.00, 150.0, "ACTIVE", "uuid-dataqualitycheckrule-01"),
    (2, "DAT-0002", "Secondary Corporate DataQualityCheckRule 2", 18200.50, 80.0, "ACTIVE", "uuid-dataqualitycheckrule-02"),
    (3, "DAT-0003", "Consolidated Branch DataQualityCheckRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dataqualitycheckrule-03"),
    (4, "DAT-0004", "Enterprise Audited DataQualityCheckRule 4", 32800.00, 210.0, "ACTIVE", "uuid-dataqualitycheckrule-04"),
    (5, "DAT-0005", "Executive Strategic DataQualityCheckRule 5", 65000.00, 400.0, "ACTIVE", "uuid-dataqualitycheckrule-05");

CREATE TABLE IF NOT EXISTS data_pipeline_transformationdataflows (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_transformationdataflows_code ON data_pipeline_transformationdataflows(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_transformationdataflows_org_status ON data_pipeline_transformationdataflows(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_transformationdataflows_priority ON data_pipeline_transformationdataflows(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_transformationdataflows_created_at ON data_pipeline_transformationdataflows(created_at);

-- Operational seed data fixtures for data_pipeline_transformationdataflows
INSERT OR IGNORE INTO data_pipeline_transformationdataflows (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TransformationDataflow 1", 24500.00, 150.0, "ACTIVE", "uuid-transformationdataflow-01"),
    (2, "TRA-0002", "Secondary Corporate TransformationDataflow 2", 18200.50, 80.0, "ACTIVE", "uuid-transformationdataflow-02"),
    (3, "TRA-0003", "Consolidated Branch TransformationDataflow 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-transformationdataflow-03"),
    (4, "TRA-0004", "Enterprise Audited TransformationDataflow 4", 32800.00, 210.0, "ACTIVE", "uuid-transformationdataflow-04"),
    (5, "TRA-0005", "Executive Strategic TransformationDataflow 5", 65000.00, 400.0, "ACTIVE", "uuid-transformationdataflow-05");

CREATE TABLE IF NOT EXISTS data_pipeline_incrementalsyncwatermarks (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_incrementalsyncwatermarks_code ON data_pipeline_incrementalsyncwatermarks(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_incrementalsyncwatermarks_org_status ON data_pipeline_incrementalsyncwatermarks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_incrementalsyncwatermarks_priority ON data_pipeline_incrementalsyncwatermarks(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_incrementalsyncwatermarks_created_at ON data_pipeline_incrementalsyncwatermarks(created_at);

-- Operational seed data fixtures for data_pipeline_incrementalsyncwatermarks
INSERT OR IGNORE INTO data_pipeline_incrementalsyncwatermarks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INC-0001", "Primary Operational IncrementalSyncWatermark 1", 24500.00, 150.0, "ACTIVE", "uuid-incrementalsyncwatermark-01"),
    (2, "INC-0002", "Secondary Corporate IncrementalSyncWatermark 2", 18200.50, 80.0, "ACTIVE", "uuid-incrementalsyncwatermark-02"),
    (3, "INC-0003", "Consolidated Branch IncrementalSyncWatermark 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-incrementalsyncwatermark-03"),
    (4, "INC-0004", "Enterprise Audited IncrementalSyncWatermark 4", 32800.00, 210.0, "ACTIVE", "uuid-incrementalsyncwatermark-04"),
    (5, "INC-0005", "Executive Strategic IncrementalSyncWatermark 5", 65000.00, 400.0, "ACTIVE", "uuid-incrementalsyncwatermark-05");

CREATE TABLE IF NOT EXISTS data_pipeline_pipelinealertnotifications (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinealertnotifications_code ON data_pipeline_pipelinealertnotifications(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinealertnotifications_org_status ON data_pipeline_pipelinealertnotifications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinealertnotifications_priority ON data_pipeline_pipelinealertnotifications(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinealertnotifications_created_at ON data_pipeline_pipelinealertnotifications(created_at);

-- Operational seed data fixtures for data_pipeline_pipelinealertnotifications
INSERT OR IGNORE INTO data_pipeline_pipelinealertnotifications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PIP-0001", "Primary Operational PipelineAlertNotification 1", 24500.00, 150.0, "ACTIVE", "uuid-pipelinealertnotification-01"),
    (2, "PIP-0002", "Secondary Corporate PipelineAlertNotification 2", 18200.50, 80.0, "ACTIVE", "uuid-pipelinealertnotification-02"),
    (3, "PIP-0003", "Consolidated Branch PipelineAlertNotification 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-pipelinealertnotification-03"),
    (4, "PIP-0004", "Enterprise Audited PipelineAlertNotification 4", 32800.00, 210.0, "ACTIVE", "uuid-pipelinealertnotification-04"),
    (5, "PIP-0005", "Executive Strategic PipelineAlertNotification 5", 65000.00, 400.0, "ACTIVE", "uuid-pipelinealertnotification-05");

CREATE TABLE IF NOT EXISTS data_pipeline_datalakestoragebuckets (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalakestoragebuckets_code ON data_pipeline_datalakestoragebuckets(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalakestoragebuckets_org_status ON data_pipeline_datalakestoragebuckets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalakestoragebuckets_priority ON data_pipeline_datalakestoragebuckets(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalakestoragebuckets_created_at ON data_pipeline_datalakestoragebuckets(created_at);

-- Operational seed data fixtures for data_pipeline_datalakestoragebuckets
INSERT OR IGNORE INTO data_pipeline_datalakestoragebuckets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataLakeStorageBucket 1", 24500.00, 150.0, "ACTIVE", "uuid-datalakestoragebucket-01"),
    (2, "DAT-0002", "Secondary Corporate DataLakeStorageBucket 2", 18200.50, 80.0, "ACTIVE", "uuid-datalakestoragebucket-02"),
    (3, "DAT-0003", "Consolidated Branch DataLakeStorageBucket 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-datalakestoragebucket-03"),
    (4, "DAT-0004", "Enterprise Audited DataLakeStorageBucket 4", 32800.00, 210.0, "ACTIVE", "uuid-datalakestoragebucket-04"),
    (5, "DAT-0005", "Executive Strategic DataLakeStorageBucket 5", 65000.00, 400.0, "ACTIVE", "uuid-datalakestoragebucket-05");

CREATE TABLE IF NOT EXISTS data_pipeline_columnmaskingpolicys (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_columnmaskingpolicys_code ON data_pipeline_columnmaskingpolicys(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_columnmaskingpolicys_org_status ON data_pipeline_columnmaskingpolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_columnmaskingpolicys_priority ON data_pipeline_columnmaskingpolicys(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_columnmaskingpolicys_created_at ON data_pipeline_columnmaskingpolicys(created_at);

-- Operational seed data fixtures for data_pipeline_columnmaskingpolicys
INSERT OR IGNORE INTO data_pipeline_columnmaskingpolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COL-0001", "Primary Operational ColumnMaskingPolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-columnmaskingpolicy-01"),
    (2, "COL-0002", "Secondary Corporate ColumnMaskingPolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-columnmaskingpolicy-02"),
    (3, "COL-0003", "Consolidated Branch ColumnMaskingPolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-columnmaskingpolicy-03"),
    (4, "COL-0004", "Enterprise Audited ColumnMaskingPolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-columnmaskingpolicy-04"),
    (5, "COL-0005", "Executive Strategic ColumnMaskingPolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-columnmaskingpolicy-05");

CREATE TABLE IF NOT EXISTS data_pipeline_datalineageedges (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalineageedges_code ON data_pipeline_datalineageedges(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalineageedges_org_status ON data_pipeline_datalineageedges(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalineageedges_priority ON data_pipeline_datalineageedges(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_datalineageedges_created_at ON data_pipeline_datalineageedges(created_at);

-- Operational seed data fixtures for data_pipeline_datalineageedges
INSERT OR IGNORE INTO data_pipeline_datalineageedges (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DAT-0001", "Primary Operational DataLineageEdge 1", 24500.00, 150.0, "ACTIVE", "uuid-datalineageedge-01"),
    (2, "DAT-0002", "Secondary Corporate DataLineageEdge 2", 18200.50, 80.0, "ACTIVE", "uuid-datalineageedge-02"),
    (3, "DAT-0003", "Consolidated Branch DataLineageEdge 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-datalineageedge-03"),
    (4, "DAT-0004", "Enterprise Audited DataLineageEdge 4", 32800.00, 210.0, "ACTIVE", "uuid-datalineageedge-04"),
    (5, "DAT-0005", "Executive Strategic DataLineageEdge 5", 65000.00, 400.0, "ACTIVE", "uuid-datalineageedge-05");

CREATE TABLE IF NOT EXISTS data_pipeline_backfillexecutionjobs (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_backfillexecutionjobs_code ON data_pipeline_backfillexecutionjobs(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_backfillexecutionjobs_org_status ON data_pipeline_backfillexecutionjobs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_backfillexecutionjobs_priority ON data_pipeline_backfillexecutionjobs(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_backfillexecutionjobs_created_at ON data_pipeline_backfillexecutionjobs(created_at);

-- Operational seed data fixtures for data_pipeline_backfillexecutionjobs
INSERT OR IGNORE INTO data_pipeline_backfillexecutionjobs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BAC-0001", "Primary Operational BackfillExecutionJob 1", 24500.00, 150.0, "ACTIVE", "uuid-backfillexecutionjob-01"),
    (2, "BAC-0002", "Secondary Corporate BackfillExecutionJob 2", 18200.50, 80.0, "ACTIVE", "uuid-backfillexecutionjob-02"),
    (3, "BAC-0003", "Consolidated Branch BackfillExecutionJob 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-backfillexecutionjob-03"),
    (4, "BAC-0004", "Enterprise Audited BackfillExecutionJob 4", 32800.00, 210.0, "ACTIVE", "uuid-backfillexecutionjob-04"),
    (5, "BAC-0005", "Executive Strategic BackfillExecutionJob 5", 65000.00, 400.0, "ACTIVE", "uuid-backfillexecutionjob-05");

CREATE TABLE IF NOT EXISTS data_pipeline_pipelinethroughputmetrics (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinethroughputmetrics_code ON data_pipeline_pipelinethroughputmetrics(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinethroughputmetrics_org_status ON data_pipeline_pipelinethroughputmetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinethroughputmetrics_priority ON data_pipeline_pipelinethroughputmetrics(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_pipelinethroughputmetrics_created_at ON data_pipeline_pipelinethroughputmetrics(created_at);

-- Operational seed data fixtures for data_pipeline_pipelinethroughputmetrics
INSERT OR IGNORE INTO data_pipeline_pipelinethroughputmetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PIP-0001", "Primary Operational PipelineThroughputMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-pipelinethroughputmetric-01"),
    (2, "PIP-0002", "Secondary Corporate PipelineThroughputMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-pipelinethroughputmetric-02"),
    (3, "PIP-0003", "Consolidated Branch PipelineThroughputMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-pipelinethroughputmetric-03"),
    (4, "PIP-0004", "Enterprise Audited PipelineThroughputMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-pipelinethroughputmetric-04"),
    (5, "PIP-0005", "Executive Strategic PipelineThroughputMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-pipelinethroughputmetric-05");

CREATE TABLE IF NOT EXISTS data_pipeline_streamingtopicoffsets (
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

CREATE INDEX IF NOT EXISTS idx_data_pipeline_streamingtopicoffsets_code ON data_pipeline_streamingtopicoffsets(code);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_streamingtopicoffsets_org_status ON data_pipeline_streamingtopicoffsets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_streamingtopicoffsets_priority ON data_pipeline_streamingtopicoffsets(priority);
CREATE INDEX IF NOT EXISTS idx_data_pipeline_streamingtopicoffsets_created_at ON data_pipeline_streamingtopicoffsets(created_at);

-- Operational seed data fixtures for data_pipeline_streamingtopicoffsets
INSERT OR IGNORE INTO data_pipeline_streamingtopicoffsets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STR-0001", "Primary Operational StreamingTopicOffset 1", 24500.00, 150.0, "ACTIVE", "uuid-streamingtopicoffset-01"),
    (2, "STR-0002", "Secondary Corporate StreamingTopicOffset 2", 18200.50, 80.0, "ACTIVE", "uuid-streamingtopicoffset-02"),
    (3, "STR-0003", "Consolidated Branch StreamingTopicOffset 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-streamingtopicoffset-03"),
    (4, "STR-0004", "Enterprise Audited StreamingTopicOffset 4", 32800.00, 210.0, "ACTIVE", "uuid-streamingtopicoffset-04"),
    (5, "STR-0005", "Executive Strategic StreamingTopicOffset 5", 65000.00, 400.0, "ACTIVE", "uuid-streamingtopicoffset-05");

