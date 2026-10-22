-- SmartERP Enterprise Titan Migration 023: Customer Self-Service & Commerce Portal DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS customer_portal_customerportalaccounts (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_customerportalaccounts_code ON customer_portal_customerportalaccounts(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_customerportalaccounts_org_status ON customer_portal_customerportalaccounts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_customerportalaccounts_priority ON customer_portal_customerportalaccounts(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_customerportalaccounts_created_at ON customer_portal_customerportalaccounts(created_at);

-- Operational seed data fixtures for customer_portal_customerportalaccounts
INSERT OR IGNORE INTO customer_portal_customerportalaccounts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerPortalAccount 1", 24500.00, 150.0, "ACTIVE", "uuid-customerportalaccount-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerPortalAccount 2", 18200.50, 80.0, "ACTIVE", "uuid-customerportalaccount-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerPortalAccount 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerportalaccount-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerPortalAccount 4", 32800.00, 210.0, "ACTIVE", "uuid-customerportalaccount-04"),
    (5, "CUS-0005", "Executive Strategic CustomerPortalAccount 5", 65000.00, 400.0, "ACTIVE", "uuid-customerportalaccount-05");

CREATE TABLE IF NOT EXISTS customer_portal_selfserviceorders (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_selfserviceorders_code ON customer_portal_selfserviceorders(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_selfserviceorders_org_status ON customer_portal_selfserviceorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_selfserviceorders_priority ON customer_portal_selfserviceorders(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_selfserviceorders_created_at ON customer_portal_selfserviceorders(created_at);

-- Operational seed data fixtures for customer_portal_selfserviceorders
INSERT OR IGNORE INTO customer_portal_selfserviceorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEL-0001", "Primary Operational SelfServiceOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-selfserviceorder-01"),
    (2, "SEL-0002", "Secondary Corporate SelfServiceOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-selfserviceorder-02"),
    (3, "SEL-0003", "Consolidated Branch SelfServiceOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-selfserviceorder-03"),
    (4, "SEL-0004", "Enterprise Audited SelfServiceOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-selfserviceorder-04"),
    (5, "SEL-0005", "Executive Strategic SelfServiceOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-selfserviceorder-05");

CREATE TABLE IF NOT EXISTS customer_portal_portalinvoiceviews (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_portalinvoiceviews_code ON customer_portal_portalinvoiceviews(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_portalinvoiceviews_org_status ON customer_portal_portalinvoiceviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_portalinvoiceviews_priority ON customer_portal_portalinvoiceviews(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_portalinvoiceviews_created_at ON customer_portal_portalinvoiceviews(created_at);

-- Operational seed data fixtures for customer_portal_portalinvoiceviews
INSERT OR IGNORE INTO customer_portal_portalinvoiceviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "POR-0001", "Primary Operational PortalInvoiceView 1", 24500.00, 150.0, "ACTIVE", "uuid-portalinvoiceview-01"),
    (2, "POR-0002", "Secondary Corporate PortalInvoiceView 2", 18200.50, 80.0, "ACTIVE", "uuid-portalinvoiceview-02"),
    (3, "POR-0003", "Consolidated Branch PortalInvoiceView 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-portalinvoiceview-03"),
    (4, "POR-0004", "Enterprise Audited PortalInvoiceView 4", 32800.00, 210.0, "ACTIVE", "uuid-portalinvoiceview-04"),
    (5, "POR-0005", "Executive Strategic PortalInvoiceView 5", 65000.00, 400.0, "ACTIVE", "uuid-portalinvoiceview-05");

CREATE TABLE IF NOT EXISTS customer_portal_statementofaccountrequests (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_statementofaccountrequests_code ON customer_portal_statementofaccountrequests(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_statementofaccountrequests_org_status ON customer_portal_statementofaccountrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_statementofaccountrequests_priority ON customer_portal_statementofaccountrequests(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_statementofaccountrequests_created_at ON customer_portal_statementofaccountrequests(created_at);

-- Operational seed data fixtures for customer_portal_statementofaccountrequests
INSERT OR IGNORE INTO customer_portal_statementofaccountrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StatementOfAccountRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-statementofaccountrequest-01"),
    (2, "STA-0002", "Secondary Corporate StatementOfAccountRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-statementofaccountrequest-02"),
    (3, "STA-0003", "Consolidated Branch StatementOfAccountRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-statementofaccountrequest-03"),
    (4, "STA-0004", "Enterprise Audited StatementOfAccountRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-statementofaccountrequest-04"),
    (5, "STA-0005", "Executive Strategic StatementOfAccountRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-statementofaccountrequest-05");

CREATE TABLE IF NOT EXISTS customer_portal_onlinepaymenttransactions (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_onlinepaymenttransactions_code ON customer_portal_onlinepaymenttransactions(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_onlinepaymenttransactions_org_status ON customer_portal_onlinepaymenttransactions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_onlinepaymenttransactions_priority ON customer_portal_onlinepaymenttransactions(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_onlinepaymenttransactions_created_at ON customer_portal_onlinepaymenttransactions(created_at);

-- Operational seed data fixtures for customer_portal_onlinepaymenttransactions
INSERT OR IGNORE INTO customer_portal_onlinepaymenttransactions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ONL-0001", "Primary Operational OnlinePaymentTransaction 1", 24500.00, 150.0, "ACTIVE", "uuid-onlinepaymenttransaction-01"),
    (2, "ONL-0002", "Secondary Corporate OnlinePaymentTransaction 2", 18200.50, 80.0, "ACTIVE", "uuid-onlinepaymenttransaction-02"),
    (3, "ONL-0003", "Consolidated Branch OnlinePaymentTransaction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-onlinepaymenttransaction-03"),
    (4, "ONL-0004", "Enterprise Audited OnlinePaymentTransaction 4", 32800.00, 210.0, "ACTIVE", "uuid-onlinepaymenttransaction-04"),
    (5, "ONL-0005", "Executive Strategic OnlinePaymentTransaction 5", 65000.00, 400.0, "ACTIVE", "uuid-onlinepaymenttransaction-05");

CREATE TABLE IF NOT EXISTS customer_portal_supportticketsubmissions (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_supportticketsubmissions_code ON customer_portal_supportticketsubmissions(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_supportticketsubmissions_org_status ON customer_portal_supportticketsubmissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_supportticketsubmissions_priority ON customer_portal_supportticketsubmissions(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_supportticketsubmissions_created_at ON customer_portal_supportticketsubmissions(created_at);

-- Operational seed data fixtures for customer_portal_supportticketsubmissions
INSERT OR IGNORE INTO customer_portal_supportticketsubmissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupportTicketSubmission 1", 24500.00, 150.0, "ACTIVE", "uuid-supportticketsubmission-01"),
    (2, "SUP-0002", "Secondary Corporate SupportTicketSubmission 2", 18200.50, 80.0, "ACTIVE", "uuid-supportticketsubmission-02"),
    (3, "SUP-0003", "Consolidated Branch SupportTicketSubmission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supportticketsubmission-03"),
    (4, "SUP-0004", "Enterprise Audited SupportTicketSubmission 4", 32800.00, 210.0, "ACTIVE", "uuid-supportticketsubmission-04"),
    (5, "SUP-0005", "Executive Strategic SupportTicketSubmission 5", 65000.00, 400.0, "ACTIVE", "uuid-supportticketsubmission-05");

CREATE TABLE IF NOT EXISTS customer_portal_productcatalogbrowsers (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_productcatalogbrowsers_code ON customer_portal_productcatalogbrowsers(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_productcatalogbrowsers_org_status ON customer_portal_productcatalogbrowsers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_productcatalogbrowsers_priority ON customer_portal_productcatalogbrowsers(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_productcatalogbrowsers_created_at ON customer_portal_productcatalogbrowsers(created_at);

-- Operational seed data fixtures for customer_portal_productcatalogbrowsers
INSERT OR IGNORE INTO customer_portal_productcatalogbrowsers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProductCatalogBrowser 1", 24500.00, 150.0, "ACTIVE", "uuid-productcatalogbrowser-01"),
    (2, "PRO-0002", "Secondary Corporate ProductCatalogBrowser 2", 18200.50, 80.0, "ACTIVE", "uuid-productcatalogbrowser-02"),
    (3, "PRO-0003", "Consolidated Branch ProductCatalogBrowser 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-productcatalogbrowser-03"),
    (4, "PRO-0004", "Enterprise Audited ProductCatalogBrowser 4", 32800.00, 210.0, "ACTIVE", "uuid-productcatalogbrowser-04"),
    (5, "PRO-0005", "Executive Strategic ProductCatalogBrowser 5", 65000.00, 400.0, "ACTIVE", "uuid-productcatalogbrowser-05");

CREATE TABLE IF NOT EXISTS customer_portal_savedordertemplates (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_savedordertemplates_code ON customer_portal_savedordertemplates(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_savedordertemplates_org_status ON customer_portal_savedordertemplates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_savedordertemplates_priority ON customer_portal_savedordertemplates(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_savedordertemplates_created_at ON customer_portal_savedordertemplates(created_at);

-- Operational seed data fixtures for customer_portal_savedordertemplates
INSERT OR IGNORE INTO customer_portal_savedordertemplates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAV-0001", "Primary Operational SavedOrderTemplate 1", 24500.00, 150.0, "ACTIVE", "uuid-savedordertemplate-01"),
    (2, "SAV-0002", "Secondary Corporate SavedOrderTemplate 2", 18200.50, 80.0, "ACTIVE", "uuid-savedordertemplate-02"),
    (3, "SAV-0003", "Consolidated Branch SavedOrderTemplate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-savedordertemplate-03"),
    (4, "SAV-0004", "Enterprise Audited SavedOrderTemplate 4", 32800.00, 210.0, "ACTIVE", "uuid-savedordertemplate-04"),
    (5, "SAV-0005", "Executive Strategic SavedOrderTemplate 5", 65000.00, 400.0, "ACTIVE", "uuid-savedordertemplate-05");

CREATE TABLE IF NOT EXISTS customer_portal_pricequoterequests (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_pricequoterequests_code ON customer_portal_pricequoterequests(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_pricequoterequests_org_status ON customer_portal_pricequoterequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_pricequoterequests_priority ON customer_portal_pricequoterequests(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_pricequoterequests_created_at ON customer_portal_pricequoterequests(created_at);

-- Operational seed data fixtures for customer_portal_pricequoterequests
INSERT OR IGNORE INTO customer_portal_pricequoterequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PriceQuoteRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-pricequoterequest-01"),
    (2, "PRI-0002", "Secondary Corporate PriceQuoteRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-pricequoterequest-02"),
    (3, "PRI-0003", "Consolidated Branch PriceQuoteRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-pricequoterequest-03"),
    (4, "PRI-0004", "Enterprise Audited PriceQuoteRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-pricequoterequest-04"),
    (5, "PRI-0005", "Executive Strategic PriceQuoteRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-pricequoterequest-05");

CREATE TABLE IF NOT EXISTS customer_portal_shipmenttrackinglookups (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_shipmenttrackinglookups_code ON customer_portal_shipmenttrackinglookups(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_shipmenttrackinglookups_org_status ON customer_portal_shipmenttrackinglookups(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_shipmenttrackinglookups_priority ON customer_portal_shipmenttrackinglookups(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_shipmenttrackinglookups_created_at ON customer_portal_shipmenttrackinglookups(created_at);

-- Operational seed data fixtures for customer_portal_shipmenttrackinglookups
INSERT OR IGNORE INTO customer_portal_shipmenttrackinglookups (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational ShipmentTrackingLookup 1", 24500.00, 150.0, "ACTIVE", "uuid-shipmenttrackinglookup-01"),
    (2, "SHI-0002", "Secondary Corporate ShipmentTrackingLookup 2", 18200.50, 80.0, "ACTIVE", "uuid-shipmenttrackinglookup-02"),
    (3, "SHI-0003", "Consolidated Branch ShipmentTrackingLookup 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shipmenttrackinglookup-03"),
    (4, "SHI-0004", "Enterprise Audited ShipmentTrackingLookup 4", 32800.00, 210.0, "ACTIVE", "uuid-shipmenttrackinglookup-04"),
    (5, "SHI-0005", "Executive Strategic ShipmentTrackingLookup 5", 65000.00, 400.0, "ACTIVE", "uuid-shipmenttrackinglookup-05");

CREATE TABLE IF NOT EXISTS customer_portal_documentdownloadhistorys (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_documentdownloadhistorys_code ON customer_portal_documentdownloadhistorys(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_documentdownloadhistorys_org_status ON customer_portal_documentdownloadhistorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_documentdownloadhistorys_priority ON customer_portal_documentdownloadhistorys(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_documentdownloadhistorys_created_at ON customer_portal_documentdownloadhistorys(created_at);

-- Operational seed data fixtures for customer_portal_documentdownloadhistorys
INSERT OR IGNORE INTO customer_portal_documentdownloadhistorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentDownloadHistory 1", 24500.00, 150.0, "ACTIVE", "uuid-documentdownloadhistory-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentDownloadHistory 2", 18200.50, 80.0, "ACTIVE", "uuid-documentdownloadhistory-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentDownloadHistory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documentdownloadhistory-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentDownloadHistory 4", 32800.00, 210.0, "ACTIVE", "uuid-documentdownloadhistory-04"),
    (5, "DOC-0005", "Executive Strategic DocumentDownloadHistory 5", 65000.00, 400.0, "ACTIVE", "uuid-documentdownloadhistory-05");

CREATE TABLE IF NOT EXISTS customer_portal_returnrmarequests (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_returnrmarequests_code ON customer_portal_returnrmarequests(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_returnrmarequests_org_status ON customer_portal_returnrmarequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_returnrmarequests_priority ON customer_portal_returnrmarequests(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_returnrmarequests_created_at ON customer_portal_returnrmarequests(created_at);

-- Operational seed data fixtures for customer_portal_returnrmarequests
INSERT OR IGNORE INTO customer_portal_returnrmarequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational ReturnRMARequest 1", 24500.00, 150.0, "ACTIVE", "uuid-returnrmarequest-01"),
    (2, "RET-0002", "Secondary Corporate ReturnRMARequest 2", 18200.50, 80.0, "ACTIVE", "uuid-returnrmarequest-02"),
    (3, "RET-0003", "Consolidated Branch ReturnRMARequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-returnrmarequest-03"),
    (4, "RET-0004", "Enterprise Audited ReturnRMARequest 4", 32800.00, 210.0, "ACTIVE", "uuid-returnrmarequest-04"),
    (5, "RET-0005", "Executive Strategic ReturnRMARequest 5", 65000.00, 400.0, "ACTIVE", "uuid-returnrmarequest-05");

CREATE TABLE IF NOT EXISTS customer_portal_feedbackreviewsubmissions (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_feedbackreviewsubmissions_code ON customer_portal_feedbackreviewsubmissions(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_feedbackreviewsubmissions_org_status ON customer_portal_feedbackreviewsubmissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_feedbackreviewsubmissions_priority ON customer_portal_feedbackreviewsubmissions(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_feedbackreviewsubmissions_created_at ON customer_portal_feedbackreviewsubmissions(created_at);

-- Operational seed data fixtures for customer_portal_feedbackreviewsubmissions
INSERT OR IGNORE INTO customer_portal_feedbackreviewsubmissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FEE-0001", "Primary Operational FeedbackReviewSubmission 1", 24500.00, 150.0, "ACTIVE", "uuid-feedbackreviewsubmission-01"),
    (2, "FEE-0002", "Secondary Corporate FeedbackReviewSubmission 2", 18200.50, 80.0, "ACTIVE", "uuid-feedbackreviewsubmission-02"),
    (3, "FEE-0003", "Consolidated Branch FeedbackReviewSubmission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-feedbackreviewsubmission-03"),
    (4, "FEE-0004", "Enterprise Audited FeedbackReviewSubmission 4", 32800.00, 210.0, "ACTIVE", "uuid-feedbackreviewsubmission-04"),
    (5, "FEE-0005", "Executive Strategic FeedbackReviewSubmission 5", 65000.00, 400.0, "ACTIVE", "uuid-feedbackreviewsubmission-05");

CREATE TABLE IF NOT EXISTS customer_portal_loyaltyrewardredemptions (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_loyaltyrewardredemptions_code ON customer_portal_loyaltyrewardredemptions(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_loyaltyrewardredemptions_org_status ON customer_portal_loyaltyrewardredemptions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_loyaltyrewardredemptions_priority ON customer_portal_loyaltyrewardredemptions(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_loyaltyrewardredemptions_created_at ON customer_portal_loyaltyrewardredemptions(created_at);

-- Operational seed data fixtures for customer_portal_loyaltyrewardredemptions
INSERT OR IGNORE INTO customer_portal_loyaltyrewardredemptions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LOY-0001", "Primary Operational LoyaltyRewardRedemption 1", 24500.00, 150.0, "ACTIVE", "uuid-loyaltyrewardredemption-01"),
    (2, "LOY-0002", "Secondary Corporate LoyaltyRewardRedemption 2", 18200.50, 80.0, "ACTIVE", "uuid-loyaltyrewardredemption-02"),
    (3, "LOY-0003", "Consolidated Branch LoyaltyRewardRedemption 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-loyaltyrewardredemption-03"),
    (4, "LOY-0004", "Enterprise Audited LoyaltyRewardRedemption 4", 32800.00, 210.0, "ACTIVE", "uuid-loyaltyrewardredemption-04"),
    (5, "LOY-0005", "Executive Strategic LoyaltyRewardRedemption 5", 65000.00, 400.0, "ACTIVE", "uuid-loyaltyrewardredemption-05");

CREATE TABLE IF NOT EXISTS customer_portal_accountmanagercontacts (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_accountmanagercontacts_code ON customer_portal_accountmanagercontacts(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_accountmanagercontacts_org_status ON customer_portal_accountmanagercontacts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_accountmanagercontacts_priority ON customer_portal_accountmanagercontacts(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_accountmanagercontacts_created_at ON customer_portal_accountmanagercontacts(created_at);

-- Operational seed data fixtures for customer_portal_accountmanagercontacts
INSERT OR IGNORE INTO customer_portal_accountmanagercontacts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACC-0001", "Primary Operational AccountManagerContact 1", 24500.00, 150.0, "ACTIVE", "uuid-accountmanagercontact-01"),
    (2, "ACC-0002", "Secondary Corporate AccountManagerContact 2", 18200.50, 80.0, "ACTIVE", "uuid-accountmanagercontact-02"),
    (3, "ACC-0003", "Consolidated Branch AccountManagerContact 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-accountmanagercontact-03"),
    (4, "ACC-0004", "Enterprise Audited AccountManagerContact 4", 32800.00, 210.0, "ACTIVE", "uuid-accountmanagercontact-04"),
    (5, "ACC-0005", "Executive Strategic AccountManagerContact 5", 65000.00, 400.0, "ACTIVE", "uuid-accountmanagercontact-05");

CREATE TABLE IF NOT EXISTS customer_portal_subscriptionselfmanagements (
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

CREATE INDEX IF NOT EXISTS idx_customer_portal_subscriptionselfmanagements_code ON customer_portal_subscriptionselfmanagements(code);
CREATE INDEX IF NOT EXISTS idx_customer_portal_subscriptionselfmanagements_org_status ON customer_portal_subscriptionselfmanagements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_portal_subscriptionselfmanagements_priority ON customer_portal_subscriptionselfmanagements(priority);
CREATE INDEX IF NOT EXISTS idx_customer_portal_subscriptionselfmanagements_created_at ON customer_portal_subscriptionselfmanagements(created_at);

-- Operational seed data fixtures for customer_portal_subscriptionselfmanagements
INSERT OR IGNORE INTO customer_portal_subscriptionselfmanagements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUB-0001", "Primary Operational SubscriptionSelfManagement 1", 24500.00, 150.0, "ACTIVE", "uuid-subscriptionselfmanagement-01"),
    (2, "SUB-0002", "Secondary Corporate SubscriptionSelfManagement 2", 18200.50, 80.0, "ACTIVE", "uuid-subscriptionselfmanagement-02"),
    (3, "SUB-0003", "Consolidated Branch SubscriptionSelfManagement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-subscriptionselfmanagement-03"),
    (4, "SUB-0004", "Enterprise Audited SubscriptionSelfManagement 4", 32800.00, 210.0, "ACTIVE", "uuid-subscriptionselfmanagement-04"),
    (5, "SUB-0005", "Executive Strategic SubscriptionSelfManagement 5", 65000.00, 400.0, "ACTIVE", "uuid-subscriptionselfmanagement-05");

