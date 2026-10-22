-- SmartERP Enterprise Titan Migration 045: Enterprise API Gateway & Integration Hub DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS api_gateway_apiendpointdefinitions (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_apiendpointdefinitions_code ON api_gateway_apiendpointdefinitions(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiendpointdefinitions_org_status ON api_gateway_apiendpointdefinitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiendpointdefinitions_priority ON api_gateway_apiendpointdefinitions(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiendpointdefinitions_created_at ON api_gateway_apiendpointdefinitions(created_at);

-- Operational seed data fixtures for api_gateway_apiendpointdefinitions
INSERT OR IGNORE INTO api_gateway_apiendpointdefinitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "API-0001", "Primary Operational APIEndpointDefinition 1", 24500.00, 150.0, "ACTIVE", "uuid-apiendpointdefinition-01"),
    (2, "API-0002", "Secondary Corporate APIEndpointDefinition 2", 18200.50, 80.0, "ACTIVE", "uuid-apiendpointdefinition-02"),
    (3, "API-0003", "Consolidated Branch APIEndpointDefinition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-apiendpointdefinition-03"),
    (4, "API-0004", "Enterprise Audited APIEndpointDefinition 4", 32800.00, 210.0, "ACTIVE", "uuid-apiendpointdefinition-04"),
    (5, "API-0005", "Executive Strategic APIEndpointDefinition 5", 65000.00, 400.0, "ACTIVE", "uuid-apiendpointdefinition-05");

CREATE TABLE IF NOT EXISTS api_gateway_apiconsumerapplications (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_apiconsumerapplications_code ON api_gateway_apiconsumerapplications(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiconsumerapplications_org_status ON api_gateway_apiconsumerapplications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiconsumerapplications_priority ON api_gateway_apiconsumerapplications(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiconsumerapplications_created_at ON api_gateway_apiconsumerapplications(created_at);

-- Operational seed data fixtures for api_gateway_apiconsumerapplications
INSERT OR IGNORE INTO api_gateway_apiconsumerapplications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "API-0001", "Primary Operational APIConsumerApplication 1", 24500.00, 150.0, "ACTIVE", "uuid-apiconsumerapplication-01"),
    (2, "API-0002", "Secondary Corporate APIConsumerApplication 2", 18200.50, 80.0, "ACTIVE", "uuid-apiconsumerapplication-02"),
    (3, "API-0003", "Consolidated Branch APIConsumerApplication 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-apiconsumerapplication-03"),
    (4, "API-0004", "Enterprise Audited APIConsumerApplication 4", 32800.00, 210.0, "ACTIVE", "uuid-apiconsumerapplication-04"),
    (5, "API-0005", "Executive Strategic APIConsumerApplication 5", 65000.00, 400.0, "ACTIVE", "uuid-apiconsumerapplication-05");

CREATE TABLE IF NOT EXISTS api_gateway_apikeycredentials (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_apikeycredentials_code ON api_gateway_apikeycredentials(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apikeycredentials_org_status ON api_gateway_apikeycredentials(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apikeycredentials_priority ON api_gateway_apikeycredentials(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apikeycredentials_created_at ON api_gateway_apikeycredentials(created_at);

-- Operational seed data fixtures for api_gateway_apikeycredentials
INSERT OR IGNORE INTO api_gateway_apikeycredentials (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "API-0001", "Primary Operational APIKeyCredential 1", 24500.00, 150.0, "ACTIVE", "uuid-apikeycredential-01"),
    (2, "API-0002", "Secondary Corporate APIKeyCredential 2", 18200.50, 80.0, "ACTIVE", "uuid-apikeycredential-02"),
    (3, "API-0003", "Consolidated Branch APIKeyCredential 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-apikeycredential-03"),
    (4, "API-0004", "Enterprise Audited APIKeyCredential 4", 32800.00, 210.0, "ACTIVE", "uuid-apikeycredential-04"),
    (5, "API-0005", "Executive Strategic APIKeyCredential 5", 65000.00, 400.0, "ACTIVE", "uuid-apikeycredential-05");

CREATE TABLE IF NOT EXISTS api_gateway_ratelimitquotarules (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_ratelimitquotarules_code ON api_gateway_ratelimitquotarules(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_ratelimitquotarules_org_status ON api_gateway_ratelimitquotarules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_ratelimitquotarules_priority ON api_gateway_ratelimitquotarules(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_ratelimitquotarules_created_at ON api_gateway_ratelimitquotarules(created_at);

-- Operational seed data fixtures for api_gateway_ratelimitquotarules
INSERT OR IGNORE INTO api_gateway_ratelimitquotarules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RAT-0001", "Primary Operational RateLimitQuotaRule 1", 24500.00, 150.0, "ACTIVE", "uuid-ratelimitquotarule-01"),
    (2, "RAT-0002", "Secondary Corporate RateLimitQuotaRule 2", 18200.50, 80.0, "ACTIVE", "uuid-ratelimitquotarule-02"),
    (3, "RAT-0003", "Consolidated Branch RateLimitQuotaRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ratelimitquotarule-03"),
    (4, "RAT-0004", "Enterprise Audited RateLimitQuotaRule 4", 32800.00, 210.0, "ACTIVE", "uuid-ratelimitquotarule-04"),
    (5, "RAT-0005", "Executive Strategic RateLimitQuotaRule 5", 65000.00, 400.0, "ACTIVE", "uuid-ratelimitquotarule-05");

CREATE TABLE IF NOT EXISTS api_gateway_oauthscopepermissions (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_oauthscopepermissions_code ON api_gateway_oauthscopepermissions(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_oauthscopepermissions_org_status ON api_gateway_oauthscopepermissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_oauthscopepermissions_priority ON api_gateway_oauthscopepermissions(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_oauthscopepermissions_created_at ON api_gateway_oauthscopepermissions(created_at);

-- Operational seed data fixtures for api_gateway_oauthscopepermissions
INSERT OR IGNORE INTO api_gateway_oauthscopepermissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OAU-0001", "Primary Operational OAuthScopePermission 1", 24500.00, 150.0, "ACTIVE", "uuid-oauthscopepermission-01"),
    (2, "OAU-0002", "Secondary Corporate OAuthScopePermission 2", 18200.50, 80.0, "ACTIVE", "uuid-oauthscopepermission-02"),
    (3, "OAU-0003", "Consolidated Branch OAuthScopePermission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-oauthscopepermission-03"),
    (4, "OAU-0004", "Enterprise Audited OAuthScopePermission 4", 32800.00, 210.0, "ACTIVE", "uuid-oauthscopepermission-04"),
    (5, "OAU-0005", "Executive Strategic OAuthScopePermission 5", 65000.00, 400.0, "ACTIVE", "uuid-oauthscopepermission-05");

CREATE TABLE IF NOT EXISTS api_gateway_webhooksubscriptiontargets (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_webhooksubscriptiontargets_code ON api_gateway_webhooksubscriptiontargets(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_webhooksubscriptiontargets_org_status ON api_gateway_webhooksubscriptiontargets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_webhooksubscriptiontargets_priority ON api_gateway_webhooksubscriptiontargets(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_webhooksubscriptiontargets_created_at ON api_gateway_webhooksubscriptiontargets(created_at);

-- Operational seed data fixtures for api_gateway_webhooksubscriptiontargets
INSERT OR IGNORE INTO api_gateway_webhooksubscriptiontargets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WEB-0001", "Primary Operational WebhookSubscriptionTarget 1", 24500.00, 150.0, "ACTIVE", "uuid-webhooksubscriptiontarget-01"),
    (2, "WEB-0002", "Secondary Corporate WebhookSubscriptionTarget 2", 18200.50, 80.0, "ACTIVE", "uuid-webhooksubscriptiontarget-02"),
    (3, "WEB-0003", "Consolidated Branch WebhookSubscriptionTarget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-webhooksubscriptiontarget-03"),
    (4, "WEB-0004", "Enterprise Audited WebhookSubscriptionTarget 4", 32800.00, 210.0, "ACTIVE", "uuid-webhooksubscriptiontarget-04"),
    (5, "WEB-0005", "Executive Strategic WebhookSubscriptionTarget 5", 65000.00, 400.0, "ACTIVE", "uuid-webhooksubscriptiontarget-05");

CREATE TABLE IF NOT EXISTS api_gateway_payloadtransformationmaps (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_payloadtransformationmaps_code ON api_gateway_payloadtransformationmaps(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_payloadtransformationmaps_org_status ON api_gateway_payloadtransformationmaps(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_payloadtransformationmaps_priority ON api_gateway_payloadtransformationmaps(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_payloadtransformationmaps_created_at ON api_gateway_payloadtransformationmaps(created_at);

-- Operational seed data fixtures for api_gateway_payloadtransformationmaps
INSERT OR IGNORE INTO api_gateway_payloadtransformationmaps (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAY-0001", "Primary Operational PayloadTransformationMap 1", 24500.00, 150.0, "ACTIVE", "uuid-payloadtransformationmap-01"),
    (2, "PAY-0002", "Secondary Corporate PayloadTransformationMap 2", 18200.50, 80.0, "ACTIVE", "uuid-payloadtransformationmap-02"),
    (3, "PAY-0003", "Consolidated Branch PayloadTransformationMap 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-payloadtransformationmap-03"),
    (4, "PAY-0004", "Enterprise Audited PayloadTransformationMap 4", 32800.00, 210.0, "ACTIVE", "uuid-payloadtransformationmap-04"),
    (5, "PAY-0005", "Executive Strategic PayloadTransformationMap 5", 65000.00, 400.0, "ACTIVE", "uuid-payloadtransformationmap-05");

CREATE TABLE IF NOT EXISTS api_gateway_gatewaytrafficmetrics (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_gatewaytrafficmetrics_code ON api_gateway_gatewaytrafficmetrics(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_gatewaytrafficmetrics_org_status ON api_gateway_gatewaytrafficmetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_gatewaytrafficmetrics_priority ON api_gateway_gatewaytrafficmetrics(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_gatewaytrafficmetrics_created_at ON api_gateway_gatewaytrafficmetrics(created_at);

-- Operational seed data fixtures for api_gateway_gatewaytrafficmetrics
INSERT OR IGNORE INTO api_gateway_gatewaytrafficmetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GAT-0001", "Primary Operational GatewayTrafficMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-gatewaytrafficmetric-01"),
    (2, "GAT-0002", "Secondary Corporate GatewayTrafficMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-gatewaytrafficmetric-02"),
    (3, "GAT-0003", "Consolidated Branch GatewayTrafficMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-gatewaytrafficmetric-03"),
    (4, "GAT-0004", "Enterprise Audited GatewayTrafficMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-gatewaytrafficmetric-04"),
    (5, "GAT-0005", "Executive Strategic GatewayTrafficMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-gatewaytrafficmetric-05");

CREATE TABLE IF NOT EXISTS api_gateway_securityfirewallrules (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_securityfirewallrules_code ON api_gateway_securityfirewallrules(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_securityfirewallrules_org_status ON api_gateway_securityfirewallrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_securityfirewallrules_priority ON api_gateway_securityfirewallrules(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_securityfirewallrules_created_at ON api_gateway_securityfirewallrules(created_at);

-- Operational seed data fixtures for api_gateway_securityfirewallrules
INSERT OR IGNORE INTO api_gateway_securityfirewallrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEC-0001", "Primary Operational SecurityFirewallRule 1", 24500.00, 150.0, "ACTIVE", "uuid-securityfirewallrule-01"),
    (2, "SEC-0002", "Secondary Corporate SecurityFirewallRule 2", 18200.50, 80.0, "ACTIVE", "uuid-securityfirewallrule-02"),
    (3, "SEC-0003", "Consolidated Branch SecurityFirewallRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-securityfirewallrule-03"),
    (4, "SEC-0004", "Enterprise Audited SecurityFirewallRule 4", 32800.00, 210.0, "ACTIVE", "uuid-securityfirewallrule-04"),
    (5, "SEC-0005", "Executive Strategic SecurityFirewallRule 5", 65000.00, 400.0, "ACTIVE", "uuid-securityfirewallrule-05");

CREATE TABLE IF NOT EXISTS api_gateway_ipallowlistentrys (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_ipallowlistentrys_code ON api_gateway_ipallowlistentrys(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_ipallowlistentrys_org_status ON api_gateway_ipallowlistentrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_ipallowlistentrys_priority ON api_gateway_ipallowlistentrys(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_ipallowlistentrys_created_at ON api_gateway_ipallowlistentrys(created_at);

-- Operational seed data fixtures for api_gateway_ipallowlistentrys
INSERT OR IGNORE INTO api_gateway_ipallowlistentrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "IPA-0001", "Primary Operational IPAllowlistEntry 1", 24500.00, 150.0, "ACTIVE", "uuid-ipallowlistentry-01"),
    (2, "IPA-0002", "Secondary Corporate IPAllowlistEntry 2", 18200.50, 80.0, "ACTIVE", "uuid-ipallowlistentry-02"),
    (3, "IPA-0003", "Consolidated Branch IPAllowlistEntry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ipallowlistentry-03"),
    (4, "IPA-0004", "Enterprise Audited IPAllowlistEntry 4", 32800.00, 210.0, "ACTIVE", "uuid-ipallowlistentry-04"),
    (5, "IPA-0005", "Executive Strategic IPAllowlistEntry 5", 65000.00, 400.0, "ACTIVE", "uuid-ipallowlistentry-05");

CREATE TABLE IF NOT EXISTS api_gateway_circuitbreakerstates (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_circuitbreakerstates_code ON api_gateway_circuitbreakerstates(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_circuitbreakerstates_org_status ON api_gateway_circuitbreakerstates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_circuitbreakerstates_priority ON api_gateway_circuitbreakerstates(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_circuitbreakerstates_created_at ON api_gateway_circuitbreakerstates(created_at);

-- Operational seed data fixtures for api_gateway_circuitbreakerstates
INSERT OR IGNORE INTO api_gateway_circuitbreakerstates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CIR-0001", "Primary Operational CircuitBreakerState 1", 24500.00, 150.0, "ACTIVE", "uuid-circuitbreakerstate-01"),
    (2, "CIR-0002", "Secondary Corporate CircuitBreakerState 2", 18200.50, 80.0, "ACTIVE", "uuid-circuitbreakerstate-02"),
    (3, "CIR-0003", "Consolidated Branch CircuitBreakerState 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-circuitbreakerstate-03"),
    (4, "CIR-0004", "Enterprise Audited CircuitBreakerState 4", 32800.00, 210.0, "ACTIVE", "uuid-circuitbreakerstate-04"),
    (5, "CIR-0005", "Executive Strategic CircuitBreakerState 5", 65000.00, 400.0, "ACTIVE", "uuid-circuitbreakerstate-05");

CREATE TABLE IF NOT EXISTS api_gateway_apiversionreleases (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_apiversionreleases_code ON api_gateway_apiversionreleases(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiversionreleases_org_status ON api_gateway_apiversionreleases(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiversionreleases_priority ON api_gateway_apiversionreleases(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_apiversionreleases_created_at ON api_gateway_apiversionreleases(created_at);

-- Operational seed data fixtures for api_gateway_apiversionreleases
INSERT OR IGNORE INTO api_gateway_apiversionreleases (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "API-0001", "Primary Operational APIVersionRelease 1", 24500.00, 150.0, "ACTIVE", "uuid-apiversionrelease-01"),
    (2, "API-0002", "Secondary Corporate APIVersionRelease 2", 18200.50, 80.0, "ACTIVE", "uuid-apiversionrelease-02"),
    (3, "API-0003", "Consolidated Branch APIVersionRelease 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-apiversionrelease-03"),
    (4, "API-0004", "Enterprise Audited APIVersionRelease 4", 32800.00, 210.0, "ACTIVE", "uuid-apiversionrelease-04"),
    (5, "API-0005", "Executive Strategic APIVersionRelease 5", 65000.00, 400.0, "ACTIVE", "uuid-apiversionrelease-05");

CREATE TABLE IF NOT EXISTS api_gateway_requestresponseauditlogs (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_requestresponseauditlogs_code ON api_gateway_requestresponseauditlogs(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_requestresponseauditlogs_org_status ON api_gateway_requestresponseauditlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_requestresponseauditlogs_priority ON api_gateway_requestresponseauditlogs(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_requestresponseauditlogs_created_at ON api_gateway_requestresponseauditlogs(created_at);

-- Operational seed data fixtures for api_gateway_requestresponseauditlogs
INSERT OR IGNORE INTO api_gateway_requestresponseauditlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REQ-0001", "Primary Operational RequestResponseAuditLog 1", 24500.00, 150.0, "ACTIVE", "uuid-requestresponseauditlog-01"),
    (2, "REQ-0002", "Secondary Corporate RequestResponseAuditLog 2", 18200.50, 80.0, "ACTIVE", "uuid-requestresponseauditlog-02"),
    (3, "REQ-0003", "Consolidated Branch RequestResponseAuditLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-requestresponseauditlog-03"),
    (4, "REQ-0004", "Enterprise Audited RequestResponseAuditLog 4", 32800.00, 210.0, "ACTIVE", "uuid-requestresponseauditlog-04"),
    (5, "REQ-0005", "Executive Strategic RequestResponseAuditLog 5", 65000.00, 400.0, "ACTIVE", "uuid-requestresponseauditlog-05");

CREATE TABLE IF NOT EXISTS api_gateway_mockresponsetemplates (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_mockresponsetemplates_code ON api_gateway_mockresponsetemplates(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_mockresponsetemplates_org_status ON api_gateway_mockresponsetemplates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_mockresponsetemplates_priority ON api_gateway_mockresponsetemplates(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_mockresponsetemplates_created_at ON api_gateway_mockresponsetemplates(created_at);

-- Operational seed data fixtures for api_gateway_mockresponsetemplates
INSERT OR IGNORE INTO api_gateway_mockresponsetemplates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MOC-0001", "Primary Operational MockResponseTemplate 1", 24500.00, 150.0, "ACTIVE", "uuid-mockresponsetemplate-01"),
    (2, "MOC-0002", "Secondary Corporate MockResponseTemplate 2", 18200.50, 80.0, "ACTIVE", "uuid-mockresponsetemplate-02"),
    (3, "MOC-0003", "Consolidated Branch MockResponseTemplate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-mockresponsetemplate-03"),
    (4, "MOC-0004", "Enterprise Audited MockResponseTemplate 4", 32800.00, 210.0, "ACTIVE", "uuid-mockresponsetemplate-04"),
    (5, "MOC-0005", "Executive Strategic MockResponseTemplate 5", 65000.00, 400.0, "ACTIVE", "uuid-mockresponsetemplate-05");

CREATE TABLE IF NOT EXISTS api_gateway_integrationconnectors (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_integrationconnectors_code ON api_gateway_integrationconnectors(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_integrationconnectors_org_status ON api_gateway_integrationconnectors(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_integrationconnectors_priority ON api_gateway_integrationconnectors(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_integrationconnectors_created_at ON api_gateway_integrationconnectors(created_at);

-- Operational seed data fixtures for api_gateway_integrationconnectors
INSERT OR IGNORE INTO api_gateway_integrationconnectors (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INT-0001", "Primary Operational IntegrationConnector 1", 24500.00, 150.0, "ACTIVE", "uuid-integrationconnector-01"),
    (2, "INT-0002", "Secondary Corporate IntegrationConnector 2", 18200.50, 80.0, "ACTIVE", "uuid-integrationconnector-02"),
    (3, "INT-0003", "Consolidated Branch IntegrationConnector 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-integrationconnector-03"),
    (4, "INT-0004", "Enterprise Audited IntegrationConnector 4", 32800.00, 210.0, "ACTIVE", "uuid-integrationconnector-04"),
    (5, "INT-0005", "Executive Strategic IntegrationConnector 5", 65000.00, 400.0, "ACTIVE", "uuid-integrationconnector-05");

CREATE TABLE IF NOT EXISTS api_gateway_servicemeshproxys (
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

CREATE INDEX IF NOT EXISTS idx_api_gateway_servicemeshproxys_code ON api_gateway_servicemeshproxys(code);
CREATE INDEX IF NOT EXISTS idx_api_gateway_servicemeshproxys_org_status ON api_gateway_servicemeshproxys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_api_gateway_servicemeshproxys_priority ON api_gateway_servicemeshproxys(priority);
CREATE INDEX IF NOT EXISTS idx_api_gateway_servicemeshproxys_created_at ON api_gateway_servicemeshproxys(created_at);

-- Operational seed data fixtures for api_gateway_servicemeshproxys
INSERT OR IGNORE INTO api_gateway_servicemeshproxys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceMeshProxy 1", 24500.00, 150.0, "ACTIVE", "uuid-servicemeshproxy-01"),
    (2, "SER-0002", "Secondary Corporate ServiceMeshProxy 2", 18200.50, 80.0, "ACTIVE", "uuid-servicemeshproxy-02"),
    (3, "SER-0003", "Consolidated Branch ServiceMeshProxy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicemeshproxy-03"),
    (4, "SER-0004", "Enterprise Audited ServiceMeshProxy 4", 32800.00, 210.0, "ACTIVE", "uuid-servicemeshproxy-04"),
    (5, "SER-0005", "Executive Strategic ServiceMeshProxy 5", 65000.00, 400.0, "ACTIVE", "uuid-servicemeshproxy-05");

