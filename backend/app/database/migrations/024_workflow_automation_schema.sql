-- SmartERP Enterprise Titan Migration 024: BPMN Business Process Automation DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS workflow_automation_processdefinitions (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_processdefinitions_code ON workflow_automation_processdefinitions(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processdefinitions_org_status ON workflow_automation_processdefinitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processdefinitions_priority ON workflow_automation_processdefinitions(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processdefinitions_created_at ON workflow_automation_processdefinitions(created_at);

-- Operational seed data fixtures for workflow_automation_processdefinitions
INSERT OR IGNORE INTO workflow_automation_processdefinitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProcessDefinition 1", 24500.00, 150.0, "ACTIVE", "uuid-processdefinition-01"),
    (2, "PRO-0002", "Secondary Corporate ProcessDefinition 2", 18200.50, 80.0, "ACTIVE", "uuid-processdefinition-02"),
    (3, "PRO-0003", "Consolidated Branch ProcessDefinition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-processdefinition-03"),
    (4, "PRO-0004", "Enterprise Audited ProcessDefinition 4", 32800.00, 210.0, "ACTIVE", "uuid-processdefinition-04"),
    (5, "PRO-0005", "Executive Strategic ProcessDefinition 5", 65000.00, 400.0, "ACTIVE", "uuid-processdefinition-05");

CREATE TABLE IF NOT EXISTS workflow_automation_processinstances (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_processinstances_code ON workflow_automation_processinstances(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processinstances_org_status ON workflow_automation_processinstances(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processinstances_priority ON workflow_automation_processinstances(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processinstances_created_at ON workflow_automation_processinstances(created_at);

-- Operational seed data fixtures for workflow_automation_processinstances
INSERT OR IGNORE INTO workflow_automation_processinstances (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProcessInstance 1", 24500.00, 150.0, "ACTIVE", "uuid-processinstance-01"),
    (2, "PRO-0002", "Secondary Corporate ProcessInstance 2", 18200.50, 80.0, "ACTIVE", "uuid-processinstance-02"),
    (3, "PRO-0003", "Consolidated Branch ProcessInstance 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-processinstance-03"),
    (4, "PRO-0004", "Enterprise Audited ProcessInstance 4", 32800.00, 210.0, "ACTIVE", "uuid-processinstance-04"),
    (5, "PRO-0005", "Executive Strategic ProcessInstance 5", 65000.00, 400.0, "ACTIVE", "uuid-processinstance-05");

CREATE TABLE IF NOT EXISTS workflow_automation_activitytaskinstances (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_activitytaskinstances_code ON workflow_automation_activitytaskinstances(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_activitytaskinstances_org_status ON workflow_automation_activitytaskinstances(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_activitytaskinstances_priority ON workflow_automation_activitytaskinstances(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_activitytaskinstances_created_at ON workflow_automation_activitytaskinstances(created_at);

-- Operational seed data fixtures for workflow_automation_activitytaskinstances
INSERT OR IGNORE INTO workflow_automation_activitytaskinstances (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACT-0001", "Primary Operational ActivityTaskInstance 1", 24500.00, 150.0, "ACTIVE", "uuid-activitytaskinstance-01"),
    (2, "ACT-0002", "Secondary Corporate ActivityTaskInstance 2", 18200.50, 80.0, "ACTIVE", "uuid-activitytaskinstance-02"),
    (3, "ACT-0003", "Consolidated Branch ActivityTaskInstance 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-activitytaskinstance-03"),
    (4, "ACT-0004", "Enterprise Audited ActivityTaskInstance 4", 32800.00, 210.0, "ACTIVE", "uuid-activitytaskinstance-04"),
    (5, "ACT-0005", "Executive Strategic ActivityTaskInstance 5", 65000.00, 400.0, "ACTIVE", "uuid-activitytaskinstance-05");

CREATE TABLE IF NOT EXISTS workflow_automation_executiontokens (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_executiontokens_code ON workflow_automation_executiontokens(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_executiontokens_org_status ON workflow_automation_executiontokens(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_executiontokens_priority ON workflow_automation_executiontokens(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_executiontokens_created_at ON workflow_automation_executiontokens(created_at);

-- Operational seed data fixtures for workflow_automation_executiontokens
INSERT OR IGNORE INTO workflow_automation_executiontokens (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutionToken 1", 24500.00, 150.0, "ACTIVE", "uuid-executiontoken-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutionToken 2", 18200.50, 80.0, "ACTIVE", "uuid-executiontoken-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutionToken 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executiontoken-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutionToken 4", 32800.00, 210.0, "ACTIVE", "uuid-executiontoken-04"),
    (5, "EXE-0005", "Executive Strategic ExecutionToken 5", 65000.00, 400.0, "ACTIVE", "uuid-executiontoken-05");

CREATE TABLE IF NOT EXISTS workflow_automation_gatewayconditiondecisions (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_gatewayconditiondecisions_code ON workflow_automation_gatewayconditiondecisions(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_gatewayconditiondecisions_org_status ON workflow_automation_gatewayconditiondecisions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_gatewayconditiondecisions_priority ON workflow_automation_gatewayconditiondecisions(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_gatewayconditiondecisions_created_at ON workflow_automation_gatewayconditiondecisions(created_at);

-- Operational seed data fixtures for workflow_automation_gatewayconditiondecisions
INSERT OR IGNORE INTO workflow_automation_gatewayconditiondecisions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GAT-0001", "Primary Operational GatewayConditionDecision 1", 24500.00, 150.0, "ACTIVE", "uuid-gatewayconditiondecision-01"),
    (2, "GAT-0002", "Secondary Corporate GatewayConditionDecision 2", 18200.50, 80.0, "ACTIVE", "uuid-gatewayconditiondecision-02"),
    (3, "GAT-0003", "Consolidated Branch GatewayConditionDecision 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-gatewayconditiondecision-03"),
    (4, "GAT-0004", "Enterprise Audited GatewayConditionDecision 4", 32800.00, 210.0, "ACTIVE", "uuid-gatewayconditiondecision-04"),
    (5, "GAT-0005", "Executive Strategic GatewayConditionDecision 5", 65000.00, 400.0, "ACTIVE", "uuid-gatewayconditiondecision-05");

CREATE TABLE IF NOT EXISTS workflow_automation_timereventsubscriptions (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_timereventsubscriptions_code ON workflow_automation_timereventsubscriptions(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_timereventsubscriptions_org_status ON workflow_automation_timereventsubscriptions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_timereventsubscriptions_priority ON workflow_automation_timereventsubscriptions(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_timereventsubscriptions_created_at ON workflow_automation_timereventsubscriptions(created_at);

-- Operational seed data fixtures for workflow_automation_timereventsubscriptions
INSERT OR IGNORE INTO workflow_automation_timereventsubscriptions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIM-0001", "Primary Operational TimerEventSubscription 1", 24500.00, 150.0, "ACTIVE", "uuid-timereventsubscription-01"),
    (2, "TIM-0002", "Secondary Corporate TimerEventSubscription 2", 18200.50, 80.0, "ACTIVE", "uuid-timereventsubscription-02"),
    (3, "TIM-0003", "Consolidated Branch TimerEventSubscription 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-timereventsubscription-03"),
    (4, "TIM-0004", "Enterprise Audited TimerEventSubscription 4", 32800.00, 210.0, "ACTIVE", "uuid-timereventsubscription-04"),
    (5, "TIM-0005", "Executive Strategic TimerEventSubscription 5", 65000.00, 400.0, "ACTIVE", "uuid-timereventsubscription-05");

CREATE TABLE IF NOT EXISTS workflow_automation_usertaskassignments (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_usertaskassignments_code ON workflow_automation_usertaskassignments(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_usertaskassignments_org_status ON workflow_automation_usertaskassignments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_usertaskassignments_priority ON workflow_automation_usertaskassignments(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_usertaskassignments_created_at ON workflow_automation_usertaskassignments(created_at);

-- Operational seed data fixtures for workflow_automation_usertaskassignments
INSERT OR IGNORE INTO workflow_automation_usertaskassignments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USE-0001", "Primary Operational UserTaskAssignment 1", 24500.00, 150.0, "ACTIVE", "uuid-usertaskassignment-01"),
    (2, "USE-0002", "Secondary Corporate UserTaskAssignment 2", 18200.50, 80.0, "ACTIVE", "uuid-usertaskassignment-02"),
    (3, "USE-0003", "Consolidated Branch UserTaskAssignment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-usertaskassignment-03"),
    (4, "USE-0004", "Enterprise Audited UserTaskAssignment 4", 32800.00, 210.0, "ACTIVE", "uuid-usertaskassignment-04"),
    (5, "USE-0005", "Executive Strategic UserTaskAssignment 5", 65000.00, 400.0, "ACTIVE", "uuid-usertaskassignment-05");

CREATE TABLE IF NOT EXISTS workflow_automation_escalationtriggerrules (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_escalationtriggerrules_code ON workflow_automation_escalationtriggerrules(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_escalationtriggerrules_org_status ON workflow_automation_escalationtriggerrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_escalationtriggerrules_priority ON workflow_automation_escalationtriggerrules(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_escalationtriggerrules_created_at ON workflow_automation_escalationtriggerrules(created_at);

-- Operational seed data fixtures for workflow_automation_escalationtriggerrules
INSERT OR IGNORE INTO workflow_automation_escalationtriggerrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ESC-0001", "Primary Operational EscalationTriggerRule 1", 24500.00, 150.0, "ACTIVE", "uuid-escalationtriggerrule-01"),
    (2, "ESC-0002", "Secondary Corporate EscalationTriggerRule 2", 18200.50, 80.0, "ACTIVE", "uuid-escalationtriggerrule-02"),
    (3, "ESC-0003", "Consolidated Branch EscalationTriggerRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-escalationtriggerrule-03"),
    (4, "ESC-0004", "Enterprise Audited EscalationTriggerRule 4", 32800.00, 210.0, "ACTIVE", "uuid-escalationtriggerrule-04"),
    (5, "ESC-0005", "Executive Strategic EscalationTriggerRule 5", 65000.00, 400.0, "ACTIVE", "uuid-escalationtriggerrule-05");

CREATE TABLE IF NOT EXISTS workflow_automation_variablescopestorages (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_variablescopestorages_code ON workflow_automation_variablescopestorages(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_variablescopestorages_org_status ON workflow_automation_variablescopestorages(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_variablescopestorages_priority ON workflow_automation_variablescopestorages(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_variablescopestorages_created_at ON workflow_automation_variablescopestorages(created_at);

-- Operational seed data fixtures for workflow_automation_variablescopestorages
INSERT OR IGNORE INTO workflow_automation_variablescopestorages (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VAR-0001", "Primary Operational VariableScopeStorage 1", 24500.00, 150.0, "ACTIVE", "uuid-variablescopestorage-01"),
    (2, "VAR-0002", "Secondary Corporate VariableScopeStorage 2", 18200.50, 80.0, "ACTIVE", "uuid-variablescopestorage-02"),
    (3, "VAR-0003", "Consolidated Branch VariableScopeStorage 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-variablescopestorage-03"),
    (4, "VAR-0004", "Enterprise Audited VariableScopeStorage 4", 32800.00, 210.0, "ACTIVE", "uuid-variablescopestorage-04"),
    (5, "VAR-0005", "Executive Strategic VariableScopeStorage 5", 65000.00, 400.0, "ACTIVE", "uuid-variablescopestorage-05");

CREATE TABLE IF NOT EXISTS workflow_automation_processhistoryaudits (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_processhistoryaudits_code ON workflow_automation_processhistoryaudits(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processhistoryaudits_org_status ON workflow_automation_processhistoryaudits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processhistoryaudits_priority ON workflow_automation_processhistoryaudits(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processhistoryaudits_created_at ON workflow_automation_processhistoryaudits(created_at);

-- Operational seed data fixtures for workflow_automation_processhistoryaudits
INSERT OR IGNORE INTO workflow_automation_processhistoryaudits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProcessHistoryAudit 1", 24500.00, 150.0, "ACTIVE", "uuid-processhistoryaudit-01"),
    (2, "PRO-0002", "Secondary Corporate ProcessHistoryAudit 2", 18200.50, 80.0, "ACTIVE", "uuid-processhistoryaudit-02"),
    (3, "PRO-0003", "Consolidated Branch ProcessHistoryAudit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-processhistoryaudit-03"),
    (4, "PRO-0004", "Enterprise Audited ProcessHistoryAudit 4", 32800.00, 210.0, "ACTIVE", "uuid-processhistoryaudit-04"),
    (5, "PRO-0005", "Executive Strategic ProcessHistoryAudit 5", 65000.00, 400.0, "ACTIVE", "uuid-processhistoryaudit-05");

CREATE TABLE IF NOT EXISTS workflow_automation_messagecatchevents (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_messagecatchevents_code ON workflow_automation_messagecatchevents(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_messagecatchevents_org_status ON workflow_automation_messagecatchevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_messagecatchevents_priority ON workflow_automation_messagecatchevents(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_messagecatchevents_created_at ON workflow_automation_messagecatchevents(created_at);

-- Operational seed data fixtures for workflow_automation_messagecatchevents
INSERT OR IGNORE INTO workflow_automation_messagecatchevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MES-0001", "Primary Operational MessageCatchEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-messagecatchevent-01"),
    (2, "MES-0002", "Secondary Corporate MessageCatchEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-messagecatchevent-02"),
    (3, "MES-0003", "Consolidated Branch MessageCatchEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-messagecatchevent-03"),
    (4, "MES-0004", "Enterprise Audited MessageCatchEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-messagecatchevent-04"),
    (5, "MES-0005", "Executive Strategic MessageCatchEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-messagecatchevent-05");

CREATE TABLE IF NOT EXISTS workflow_automation_signalthrowevents (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_signalthrowevents_code ON workflow_automation_signalthrowevents(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_signalthrowevents_org_status ON workflow_automation_signalthrowevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_signalthrowevents_priority ON workflow_automation_signalthrowevents(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_signalthrowevents_created_at ON workflow_automation_signalthrowevents(created_at);

-- Operational seed data fixtures for workflow_automation_signalthrowevents
INSERT OR IGNORE INTO workflow_automation_signalthrowevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SIG-0001", "Primary Operational SignalThrowEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-signalthrowevent-01"),
    (2, "SIG-0002", "Secondary Corporate SignalThrowEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-signalthrowevent-02"),
    (3, "SIG-0003", "Consolidated Branch SignalThrowEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-signalthrowevent-03"),
    (4, "SIG-0004", "Enterprise Audited SignalThrowEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-signalthrowevent-04"),
    (5, "SIG-0005", "Executive Strategic SignalThrowEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-signalthrowevent-05");

CREATE TABLE IF NOT EXISTS workflow_automation_subprocessscopes (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_subprocessscopes_code ON workflow_automation_subprocessscopes(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_subprocessscopes_org_status ON workflow_automation_subprocessscopes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_subprocessscopes_priority ON workflow_automation_subprocessscopes(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_subprocessscopes_created_at ON workflow_automation_subprocessscopes(created_at);

-- Operational seed data fixtures for workflow_automation_subprocessscopes
INSERT OR IGNORE INTO workflow_automation_subprocessscopes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUB-0001", "Primary Operational SubProcessScope 1", 24500.00, 150.0, "ACTIVE", "uuid-subprocessscope-01"),
    (2, "SUB-0002", "Secondary Corporate SubProcessScope 2", 18200.50, 80.0, "ACTIVE", "uuid-subprocessscope-02"),
    (3, "SUB-0003", "Consolidated Branch SubProcessScope 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-subprocessscope-03"),
    (4, "SUB-0004", "Enterprise Audited SubProcessScope 4", 32800.00, 210.0, "ACTIVE", "uuid-subprocessscope-04"),
    (5, "SUB-0005", "Executive Strategic SubProcessScope 5", 65000.00, 400.0, "ACTIVE", "uuid-subprocessscope-05");

CREATE TABLE IF NOT EXISTS workflow_automation_compensationhandlers (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_compensationhandlers_code ON workflow_automation_compensationhandlers(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_compensationhandlers_org_status ON workflow_automation_compensationhandlers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_compensationhandlers_priority ON workflow_automation_compensationhandlers(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_compensationhandlers_created_at ON workflow_automation_compensationhandlers(created_at);

-- Operational seed data fixtures for workflow_automation_compensationhandlers
INSERT OR IGNORE INTO workflow_automation_compensationhandlers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CompensationHandler 1", 24500.00, 150.0, "ACTIVE", "uuid-compensationhandler-01"),
    (2, "COM-0002", "Secondary Corporate CompensationHandler 2", 18200.50, 80.0, "ACTIVE", "uuid-compensationhandler-02"),
    (3, "COM-0003", "Consolidated Branch CompensationHandler 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-compensationhandler-03"),
    (4, "COM-0004", "Enterprise Audited CompensationHandler 4", 32800.00, 210.0, "ACTIVE", "uuid-compensationhandler-04"),
    (5, "COM-0005", "Executive Strategic CompensationHandler 5", 65000.00, 400.0, "ACTIVE", "uuid-compensationhandler-05");

CREATE TABLE IF NOT EXISTS workflow_automation_processmetricsanalyticss (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_processmetricsanalyticss_code ON workflow_automation_processmetricsanalyticss(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processmetricsanalyticss_org_status ON workflow_automation_processmetricsanalyticss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processmetricsanalyticss_priority ON workflow_automation_processmetricsanalyticss(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_processmetricsanalyticss_created_at ON workflow_automation_processmetricsanalyticss(created_at);

-- Operational seed data fixtures for workflow_automation_processmetricsanalyticss
INSERT OR IGNORE INTO workflow_automation_processmetricsanalyticss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProcessMetricsAnalytics 1", 24500.00, 150.0, "ACTIVE", "uuid-processmetricsanalytics-01"),
    (2, "PRO-0002", "Secondary Corporate ProcessMetricsAnalytics 2", 18200.50, 80.0, "ACTIVE", "uuid-processmetricsanalytics-02"),
    (3, "PRO-0003", "Consolidated Branch ProcessMetricsAnalytics 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-processmetricsanalytics-03"),
    (4, "PRO-0004", "Enterprise Audited ProcessMetricsAnalytics 4", 32800.00, 210.0, "ACTIVE", "uuid-processmetricsanalytics-04"),
    (5, "PRO-0005", "Executive Strategic ProcessMetricsAnalytics 5", 65000.00, 400.0, "ACTIVE", "uuid-processmetricsanalytics-05");

CREATE TABLE IF NOT EXISTS workflow_automation_deploymentpackages (
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

CREATE INDEX IF NOT EXISTS idx_workflow_automation_deploymentpackages_code ON workflow_automation_deploymentpackages(code);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_deploymentpackages_org_status ON workflow_automation_deploymentpackages(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_deploymentpackages_priority ON workflow_automation_deploymentpackages(priority);
CREATE INDEX IF NOT EXISTS idx_workflow_automation_deploymentpackages_created_at ON workflow_automation_deploymentpackages(created_at);

-- Operational seed data fixtures for workflow_automation_deploymentpackages
INSERT OR IGNORE INTO workflow_automation_deploymentpackages (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DeploymentPackage 1", 24500.00, 150.0, "ACTIVE", "uuid-deploymentpackage-01"),
    (2, "DEP-0002", "Secondary Corporate DeploymentPackage 2", 18200.50, 80.0, "ACTIVE", "uuid-deploymentpackage-02"),
    (3, "DEP-0003", "Consolidated Branch DeploymentPackage 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-deploymentpackage-03"),
    (4, "DEP-0004", "Enterprise Audited DeploymentPackage 4", 32800.00, 210.0, "ACTIVE", "uuid-deploymentpackage-04"),
    (5, "DEP-0005", "Executive Strategic DeploymentPackage 5", 65000.00, 400.0, "ACTIVE", "uuid-deploymentpackage-05");

