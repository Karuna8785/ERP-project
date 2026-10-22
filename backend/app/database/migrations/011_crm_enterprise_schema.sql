-- SmartERP Enterprise Titan Migration 011: Enterprise CRM & Account Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS crm_enterprise_leadaccounts (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadaccounts_code ON crm_enterprise_leadaccounts(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadaccounts_org_status ON crm_enterprise_leadaccounts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadaccounts_priority ON crm_enterprise_leadaccounts(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadaccounts_created_at ON crm_enterprise_leadaccounts(created_at);

-- Operational seed data fixtures for crm_enterprise_leadaccounts
INSERT OR IGNORE INTO crm_enterprise_leadaccounts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeadAccount 1", 24500.00, 150.0, "ACTIVE", "uuid-leadaccount-01"),
    (2, "LEA-0002", "Secondary Corporate LeadAccount 2", 18200.50, 80.0, "ACTIVE", "uuid-leadaccount-02"),
    (3, "LEA-0003", "Consolidated Branch LeadAccount 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leadaccount-03"),
    (4, "LEA-0004", "Enterprise Audited LeadAccount 4", 32800.00, 210.0, "ACTIVE", "uuid-leadaccount-04"),
    (5, "LEA-0005", "Executive Strategic LeadAccount 5", 65000.00, 400.0, "ACTIVE", "uuid-leadaccount-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_contactpersons (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_contactpersons_code ON crm_enterprise_contactpersons(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_contactpersons_org_status ON crm_enterprise_contactpersons(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_contactpersons_priority ON crm_enterprise_contactpersons(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_contactpersons_created_at ON crm_enterprise_contactpersons(created_at);

-- Operational seed data fixtures for crm_enterprise_contactpersons
INSERT OR IGNORE INTO crm_enterprise_contactpersons (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContactPerson 1", 24500.00, 150.0, "ACTIVE", "uuid-contactperson-01"),
    (2, "CON-0002", "Secondary Corporate ContactPerson 2", 18200.50, 80.0, "ACTIVE", "uuid-contactperson-02"),
    (3, "CON-0003", "Consolidated Branch ContactPerson 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-contactperson-03"),
    (4, "CON-0004", "Enterprise Audited ContactPerson 4", 32800.00, 210.0, "ACTIVE", "uuid-contactperson-04"),
    (5, "CON-0005", "Executive Strategic ContactPerson 5", 65000.00, 400.0, "ACTIVE", "uuid-contactperson-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_opportunitydeals (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_opportunitydeals_code ON crm_enterprise_opportunitydeals(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_opportunitydeals_org_status ON crm_enterprise_opportunitydeals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_opportunitydeals_priority ON crm_enterprise_opportunitydeals(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_opportunitydeals_created_at ON crm_enterprise_opportunitydeals(created_at);

-- Operational seed data fixtures for crm_enterprise_opportunitydeals
INSERT OR IGNORE INTO crm_enterprise_opportunitydeals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OPP-0001", "Primary Operational OpportunityDeal 1", 24500.00, 150.0, "ACTIVE", "uuid-opportunitydeal-01"),
    (2, "OPP-0002", "Secondary Corporate OpportunityDeal 2", 18200.50, 80.0, "ACTIVE", "uuid-opportunitydeal-02"),
    (3, "OPP-0003", "Consolidated Branch OpportunityDeal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-opportunitydeal-03"),
    (4, "OPP-0004", "Enterprise Audited OpportunityDeal 4", 32800.00, 210.0, "ACTIVE", "uuid-opportunitydeal-04"),
    (5, "OPP-0005", "Executive Strategic OpportunityDeal 5", 65000.00, 400.0, "ACTIVE", "uuid-opportunitydeal-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_salespipelinestages (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salespipelinestages_code ON crm_enterprise_salespipelinestages(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salespipelinestages_org_status ON crm_enterprise_salespipelinestages(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salespipelinestages_priority ON crm_enterprise_salespipelinestages(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salespipelinestages_created_at ON crm_enterprise_salespipelinestages(created_at);

-- Operational seed data fixtures for crm_enterprise_salespipelinestages
INSERT OR IGNORE INTO crm_enterprise_salespipelinestages (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAL-0001", "Primary Operational SalesPipelineStage 1", 24500.00, 150.0, "ACTIVE", "uuid-salespipelinestage-01"),
    (2, "SAL-0002", "Secondary Corporate SalesPipelineStage 2", 18200.50, 80.0, "ACTIVE", "uuid-salespipelinestage-02"),
    (3, "SAL-0003", "Consolidated Branch SalesPipelineStage 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-salespipelinestage-03"),
    (4, "SAL-0004", "Enterprise Audited SalesPipelineStage 4", 32800.00, 210.0, "ACTIVE", "uuid-salespipelinestage-04"),
    (5, "SAL-0005", "Executive Strategic SalesPipelineStage 5", 65000.00, 400.0, "ACTIVE", "uuid-salespipelinestage-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_quoteproposals (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_quoteproposals_code ON crm_enterprise_quoteproposals(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_quoteproposals_org_status ON crm_enterprise_quoteproposals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_quoteproposals_priority ON crm_enterprise_quoteproposals(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_quoteproposals_created_at ON crm_enterprise_quoteproposals(created_at);

-- Operational seed data fixtures for crm_enterprise_quoteproposals
INSERT OR IGNORE INTO crm_enterprise_quoteproposals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "QUO-0001", "Primary Operational QuoteProposal 1", 24500.00, 150.0, "ACTIVE", "uuid-quoteproposal-01"),
    (2, "QUO-0002", "Secondary Corporate QuoteProposal 2", 18200.50, 80.0, "ACTIVE", "uuid-quoteproposal-02"),
    (3, "QUO-0003", "Consolidated Branch QuoteProposal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-quoteproposal-03"),
    (4, "QUO-0004", "Enterprise Audited QuoteProposal 4", 32800.00, 210.0, "ACTIVE", "uuid-quoteproposal-04"),
    (5, "QUO-0005", "Executive Strategic QuoteProposal 5", 65000.00, 400.0, "ACTIVE", "uuid-quoteproposal-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_territoryregions (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_territoryregions_code ON crm_enterprise_territoryregions(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_territoryregions_org_status ON crm_enterprise_territoryregions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_territoryregions_priority ON crm_enterprise_territoryregions(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_territoryregions_created_at ON crm_enterprise_territoryregions(created_at);

-- Operational seed data fixtures for crm_enterprise_territoryregions
INSERT OR IGNORE INTO crm_enterprise_territoryregions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TER-0001", "Primary Operational TerritoryRegion 1", 24500.00, 150.0, "ACTIVE", "uuid-territoryregion-01"),
    (2, "TER-0002", "Secondary Corporate TerritoryRegion 2", 18200.50, 80.0, "ACTIVE", "uuid-territoryregion-02"),
    (3, "TER-0003", "Consolidated Branch TerritoryRegion 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-territoryregion-03"),
    (4, "TER-0004", "Enterprise Audited TerritoryRegion 4", 32800.00, 210.0, "ACTIVE", "uuid-territoryregion-04"),
    (5, "TER-0005", "Executive Strategic TerritoryRegion 5", 65000.00, 400.0, "ACTIVE", "uuid-territoryregion-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_salesquotatargets (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salesquotatargets_code ON crm_enterprise_salesquotatargets(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salesquotatargets_org_status ON crm_enterprise_salesquotatargets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salesquotatargets_priority ON crm_enterprise_salesquotatargets(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_salesquotatargets_created_at ON crm_enterprise_salesquotatargets(created_at);

-- Operational seed data fixtures for crm_enterprise_salesquotatargets
INSERT OR IGNORE INTO crm_enterprise_salesquotatargets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAL-0001", "Primary Operational SalesQuotaTarget 1", 24500.00, 150.0, "ACTIVE", "uuid-salesquotatarget-01"),
    (2, "SAL-0002", "Secondary Corporate SalesQuotaTarget 2", 18200.50, 80.0, "ACTIVE", "uuid-salesquotatarget-02"),
    (3, "SAL-0003", "Consolidated Branch SalesQuotaTarget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-salesquotatarget-03"),
    (4, "SAL-0004", "Enterprise Audited SalesQuotaTarget 4", 32800.00, 210.0, "ACTIVE", "uuid-salesquotatarget-04"),
    (5, "SAL-0005", "Executive Strategic SalesQuotaTarget 5", 65000.00, 400.0, "ACTIVE", "uuid-salesquotatarget-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_competitoranalysiss (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_competitoranalysiss_code ON crm_enterprise_competitoranalysiss(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_competitoranalysiss_org_status ON crm_enterprise_competitoranalysiss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_competitoranalysiss_priority ON crm_enterprise_competitoranalysiss(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_competitoranalysiss_created_at ON crm_enterprise_competitoranalysiss(created_at);

-- Operational seed data fixtures for crm_enterprise_competitoranalysiss
INSERT OR IGNORE INTO crm_enterprise_competitoranalysiss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CompetitorAnalysis 1", 24500.00, 150.0, "ACTIVE", "uuid-competitoranalysis-01"),
    (2, "COM-0002", "Secondary Corporate CompetitorAnalysis 2", 18200.50, 80.0, "ACTIVE", "uuid-competitoranalysis-02"),
    (3, "COM-0003", "Consolidated Branch CompetitorAnalysis 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-competitoranalysis-03"),
    (4, "COM-0004", "Enterprise Audited CompetitorAnalysis 4", 32800.00, 210.0, "ACTIVE", "uuid-competitoranalysis-04"),
    (5, "COM-0005", "Executive Strategic CompetitorAnalysis 5", 65000.00, 400.0, "ACTIVE", "uuid-competitoranalysis-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_customertouchpoints (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customertouchpoints_code ON crm_enterprise_customertouchpoints(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customertouchpoints_org_status ON crm_enterprise_customertouchpoints(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customertouchpoints_priority ON crm_enterprise_customertouchpoints(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customertouchpoints_created_at ON crm_enterprise_customertouchpoints(created_at);

-- Operational seed data fixtures for crm_enterprise_customertouchpoints
INSERT OR IGNORE INTO crm_enterprise_customertouchpoints (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerTouchpoint 1", 24500.00, 150.0, "ACTIVE", "uuid-customertouchpoint-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerTouchpoint 2", 18200.50, 80.0, "ACTIVE", "uuid-customertouchpoint-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerTouchpoint 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customertouchpoint-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerTouchpoint 4", 32800.00, 210.0, "ACTIVE", "uuid-customertouchpoint-04"),
    (5, "CUS-0005", "Executive Strategic CustomerTouchpoint 5", 65000.00, 400.0, "ACTIVE", "uuid-customertouchpoint-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_campaigntrackings (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_campaigntrackings_code ON crm_enterprise_campaigntrackings(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_campaigntrackings_org_status ON crm_enterprise_campaigntrackings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_campaigntrackings_priority ON crm_enterprise_campaigntrackings(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_campaigntrackings_created_at ON crm_enterprise_campaigntrackings(created_at);

-- Operational seed data fixtures for crm_enterprise_campaigntrackings
INSERT OR IGNORE INTO crm_enterprise_campaigntrackings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAM-0001", "Primary Operational CampaignTracking 1", 24500.00, 150.0, "ACTIVE", "uuid-campaigntracking-01"),
    (2, "CAM-0002", "Secondary Corporate CampaignTracking 2", 18200.50, 80.0, "ACTIVE", "uuid-campaigntracking-02"),
    (3, "CAM-0003", "Consolidated Branch CampaignTracking 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-campaigntracking-03"),
    (4, "CAM-0004", "Enterprise Audited CampaignTracking 4", 32800.00, 210.0, "ACTIVE", "uuid-campaigntracking-04"),
    (5, "CAM-0005", "Executive Strategic CampaignTracking 5", 65000.00, 400.0, "ACTIVE", "uuid-campaigntracking-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_leadscoremetrics (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadscoremetrics_code ON crm_enterprise_leadscoremetrics(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadscoremetrics_org_status ON crm_enterprise_leadscoremetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadscoremetrics_priority ON crm_enterprise_leadscoremetrics(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_leadscoremetrics_created_at ON crm_enterprise_leadscoremetrics(created_at);

-- Operational seed data fixtures for crm_enterprise_leadscoremetrics
INSERT OR IGNORE INTO crm_enterprise_leadscoremetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeadScoreMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-leadscoremetric-01"),
    (2, "LEA-0002", "Secondary Corporate LeadScoreMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-leadscoremetric-02"),
    (3, "LEA-0003", "Consolidated Branch LeadScoreMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leadscoremetric-03"),
    (4, "LEA-0004", "Enterprise Audited LeadScoreMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-leadscoremetric-04"),
    (5, "LEA-0005", "Executive Strategic LeadScoreMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-leadscoremetric-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_dealcommissions (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_dealcommissions_code ON crm_enterprise_dealcommissions(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_dealcommissions_org_status ON crm_enterprise_dealcommissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_dealcommissions_priority ON crm_enterprise_dealcommissions(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_dealcommissions_created_at ON crm_enterprise_dealcommissions(created_at);

-- Operational seed data fixtures for crm_enterprise_dealcommissions
INSERT OR IGNORE INTO crm_enterprise_dealcommissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEA-0001", "Primary Operational DealCommission 1", 24500.00, 150.0, "ACTIVE", "uuid-dealcommission-01"),
    (2, "DEA-0002", "Secondary Corporate DealCommission 2", 18200.50, 80.0, "ACTIVE", "uuid-dealcommission-02"),
    (3, "DEA-0003", "Consolidated Branch DealCommission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dealcommission-03"),
    (4, "DEA-0004", "Enterprise Audited DealCommission 4", 32800.00, 210.0, "ACTIVE", "uuid-dealcommission-04"),
    (5, "DEA-0005", "Executive Strategic DealCommission 5", 65000.00, 400.0, "ACTIVE", "uuid-dealcommission-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_customerchurnrisks (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customerchurnrisks_code ON crm_enterprise_customerchurnrisks(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customerchurnrisks_org_status ON crm_enterprise_customerchurnrisks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customerchurnrisks_priority ON crm_enterprise_customerchurnrisks(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_customerchurnrisks_created_at ON crm_enterprise_customerchurnrisks(created_at);

-- Operational seed data fixtures for crm_enterprise_customerchurnrisks
INSERT OR IGNORE INTO crm_enterprise_customerchurnrisks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerChurnRisk 1", 24500.00, 150.0, "ACTIVE", "uuid-customerchurnrisk-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerChurnRisk 2", 18200.50, 80.0, "ACTIVE", "uuid-customerchurnrisk-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerChurnRisk 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerchurnrisk-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerChurnRisk 4", 32800.00, 210.0, "ACTIVE", "uuid-customerchurnrisk-04"),
    (5, "CUS-0005", "Executive Strategic CustomerChurnRisk 5", 65000.00, 400.0, "ACTIVE", "uuid-customerchurnrisk-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_meetingtranscripts (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_meetingtranscripts_code ON crm_enterprise_meetingtranscripts(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_meetingtranscripts_org_status ON crm_enterprise_meetingtranscripts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_meetingtranscripts_priority ON crm_enterprise_meetingtranscripts(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_meetingtranscripts_created_at ON crm_enterprise_meetingtranscripts(created_at);

-- Operational seed data fixtures for crm_enterprise_meetingtranscripts
INSERT OR IGNORE INTO crm_enterprise_meetingtranscripts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MEE-0001", "Primary Operational MeetingTranscript 1", 24500.00, 150.0, "ACTIVE", "uuid-meetingtranscript-01"),
    (2, "MEE-0002", "Secondary Corporate MeetingTranscript 2", 18200.50, 80.0, "ACTIVE", "uuid-meetingtranscript-02"),
    (3, "MEE-0003", "Consolidated Branch MeetingTranscript 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-meetingtranscript-03"),
    (4, "MEE-0004", "Enterprise Audited MeetingTranscript 4", 32800.00, 210.0, "ACTIVE", "uuid-meetingtranscript-04"),
    (5, "MEE-0005", "Executive Strategic MeetingTranscript 5", 65000.00, 400.0, "ACTIVE", "uuid-meetingtranscript-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_referralsources (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_referralsources_code ON crm_enterprise_referralsources(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_referralsources_org_status ON crm_enterprise_referralsources(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_referralsources_priority ON crm_enterprise_referralsources(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_referralsources_created_at ON crm_enterprise_referralsources(created_at);

-- Operational seed data fixtures for crm_enterprise_referralsources
INSERT OR IGNORE INTO crm_enterprise_referralsources (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REF-0001", "Primary Operational ReferralSource 1", 24500.00, 150.0, "ACTIVE", "uuid-referralsource-01"),
    (2, "REF-0002", "Secondary Corporate ReferralSource 2", 18200.50, 80.0, "ACTIVE", "uuid-referralsource-02"),
    (3, "REF-0003", "Consolidated Branch ReferralSource 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-referralsource-03"),
    (4, "REF-0004", "Enterprise Audited ReferralSource 4", 32800.00, 210.0, "ACTIVE", "uuid-referralsource-04"),
    (5, "REF-0005", "Executive Strategic ReferralSource 5", 65000.00, 400.0, "ACTIVE", "uuid-referralsource-05");

CREATE TABLE IF NOT EXISTS crm_enterprise_partnerchannels (
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

CREATE INDEX IF NOT EXISTS idx_crm_enterprise_partnerchannels_code ON crm_enterprise_partnerchannels(code);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_partnerchannels_org_status ON crm_enterprise_partnerchannels(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_partnerchannels_priority ON crm_enterprise_partnerchannels(priority);
CREATE INDEX IF NOT EXISTS idx_crm_enterprise_partnerchannels_created_at ON crm_enterprise_partnerchannels(created_at);

-- Operational seed data fixtures for crm_enterprise_partnerchannels
INSERT OR IGNORE INTO crm_enterprise_partnerchannels (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartnerChannel 1", 24500.00, 150.0, "ACTIVE", "uuid-partnerchannel-01"),
    (2, "PAR-0002", "Secondary Corporate PartnerChannel 2", 18200.50, 80.0, "ACTIVE", "uuid-partnerchannel-02"),
    (3, "PAR-0003", "Consolidated Branch PartnerChannel 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partnerchannel-03"),
    (4, "PAR-0004", "Enterprise Audited PartnerChannel 4", 32800.00, 210.0, "ACTIVE", "uuid-partnerchannel-04"),
    (5, "PAR-0005", "Executive Strategic PartnerChannel 5", 65000.00, 400.0, "ACTIVE", "uuid-partnerchannel-05");

