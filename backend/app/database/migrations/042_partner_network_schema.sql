-- SmartERP Enterprise Titan Migration 042: Partner Relationship Management (PRM) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS partner_network_channelpartnerprofiles (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_channelpartnerprofiles_code ON partner_network_channelpartnerprofiles(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelpartnerprofiles_org_status ON partner_network_channelpartnerprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelpartnerprofiles_priority ON partner_network_channelpartnerprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelpartnerprofiles_created_at ON partner_network_channelpartnerprofiles(created_at);

-- Operational seed data fixtures for partner_network_channelpartnerprofiles
INSERT OR IGNORE INTO partner_network_channelpartnerprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHA-0001", "Primary Operational ChannelPartnerProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-channelpartnerprofile-01"),
    (2, "CHA-0002", "Secondary Corporate ChannelPartnerProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-channelpartnerprofile-02"),
    (3, "CHA-0003", "Consolidated Branch ChannelPartnerProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-channelpartnerprofile-03"),
    (4, "CHA-0004", "Enterprise Audited ChannelPartnerProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-channelpartnerprofile-04"),
    (5, "CHA-0005", "Executive Strategic ChannelPartnerProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-channelpartnerprofile-05");

CREATE TABLE IF NOT EXISTS partner_network_partnertierlevels (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_partnertierlevels_code ON partner_network_partnertierlevels(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnertierlevels_org_status ON partner_network_partnertierlevels(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnertierlevels_priority ON partner_network_partnertierlevels(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnertierlevels_created_at ON partner_network_partnertierlevels(created_at);

-- Operational seed data fixtures for partner_network_partnertierlevels
INSERT OR IGNORE INTO partner_network_partnertierlevels (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartnerTierLevel 1", 24500.00, 150.0, "ACTIVE", "uuid-partnertierlevel-01"),
    (2, "PAR-0002", "Secondary Corporate PartnerTierLevel 2", 18200.50, 80.0, "ACTIVE", "uuid-partnertierlevel-02"),
    (3, "PAR-0003", "Consolidated Branch PartnerTierLevel 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partnertierlevel-03"),
    (4, "PAR-0004", "Enterprise Audited PartnerTierLevel 4", 32800.00, 210.0, "ACTIVE", "uuid-partnertierlevel-04"),
    (5, "PAR-0005", "Executive Strategic PartnerTierLevel 5", 65000.00, 400.0, "ACTIVE", "uuid-partnertierlevel-05");

CREATE TABLE IF NOT EXISTS partner_network_dealregistrationleads (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_dealregistrationleads_code ON partner_network_dealregistrationleads(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_dealregistrationleads_org_status ON partner_network_dealregistrationleads(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_dealregistrationleads_priority ON partner_network_dealregistrationleads(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_dealregistrationleads_created_at ON partner_network_dealregistrationleads(created_at);

-- Operational seed data fixtures for partner_network_dealregistrationleads
INSERT OR IGNORE INTO partner_network_dealregistrationleads (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEA-0001", "Primary Operational DealRegistrationLead 1", 24500.00, 150.0, "ACTIVE", "uuid-dealregistrationlead-01"),
    (2, "DEA-0002", "Secondary Corporate DealRegistrationLead 2", 18200.50, 80.0, "ACTIVE", "uuid-dealregistrationlead-02"),
    (3, "DEA-0003", "Consolidated Branch DealRegistrationLead 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dealregistrationlead-03"),
    (4, "DEA-0004", "Enterprise Audited DealRegistrationLead 4", 32800.00, 210.0, "ACTIVE", "uuid-dealregistrationlead-04"),
    (5, "DEA-0005", "Executive Strategic DealRegistrationLead 5", 65000.00, 400.0, "ACTIVE", "uuid-dealregistrationlead-05");

CREATE TABLE IF NOT EXISTS partner_network_mdfmarketfundrequests (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_mdfmarketfundrequests_code ON partner_network_mdfmarketfundrequests(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_mdfmarketfundrequests_org_status ON partner_network_mdfmarketfundrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_mdfmarketfundrequests_priority ON partner_network_mdfmarketfundrequests(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_mdfmarketfundrequests_created_at ON partner_network_mdfmarketfundrequests(created_at);

-- Operational seed data fixtures for partner_network_mdfmarketfundrequests
INSERT OR IGNORE INTO partner_network_mdfmarketfundrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MDF-0001", "Primary Operational MDFMarketFundRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-mdfmarketfundrequest-01"),
    (2, "MDF-0002", "Secondary Corporate MDFMarketFundRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-mdfmarketfundrequest-02"),
    (3, "MDF-0003", "Consolidated Branch MDFMarketFundRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-mdfmarketfundrequest-03"),
    (4, "MDF-0004", "Enterprise Audited MDFMarketFundRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-mdfmarketfundrequest-04"),
    (5, "MDF-0005", "Executive Strategic MDFMarketFundRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-mdfmarketfundrequest-05");

CREATE TABLE IF NOT EXISTS partner_network_comarketingcampaigns (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_comarketingcampaigns_code ON partner_network_comarketingcampaigns(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_comarketingcampaigns_org_status ON partner_network_comarketingcampaigns(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_comarketingcampaigns_priority ON partner_network_comarketingcampaigns(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_comarketingcampaigns_created_at ON partner_network_comarketingcampaigns(created_at);

-- Operational seed data fixtures for partner_network_comarketingcampaigns
INSERT OR IGNORE INTO partner_network_comarketingcampaigns (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CoMarketingCampaign 1", 24500.00, 150.0, "ACTIVE", "uuid-comarketingcampaign-01"),
    (2, "COM-0002", "Secondary Corporate CoMarketingCampaign 2", 18200.50, 80.0, "ACTIVE", "uuid-comarketingcampaign-02"),
    (3, "COM-0003", "Consolidated Branch CoMarketingCampaign 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-comarketingcampaign-03"),
    (4, "COM-0004", "Enterprise Audited CoMarketingCampaign 4", 32800.00, 210.0, "ACTIVE", "uuid-comarketingcampaign-04"),
    (5, "COM-0005", "Executive Strategic CoMarketingCampaign 5", 65000.00, 400.0, "ACTIVE", "uuid-comarketingcampaign-05");

CREATE TABLE IF NOT EXISTS partner_network_partnercommissionpayouts (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_partnercommissionpayouts_code ON partner_network_partnercommissionpayouts(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnercommissionpayouts_org_status ON partner_network_partnercommissionpayouts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnercommissionpayouts_priority ON partner_network_partnercommissionpayouts(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnercommissionpayouts_created_at ON partner_network_partnercommissionpayouts(created_at);

-- Operational seed data fixtures for partner_network_partnercommissionpayouts
INSERT OR IGNORE INTO partner_network_partnercommissionpayouts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartnerCommissionPayout 1", 24500.00, 150.0, "ACTIVE", "uuid-partnercommissionpayout-01"),
    (2, "PAR-0002", "Secondary Corporate PartnerCommissionPayout 2", 18200.50, 80.0, "ACTIVE", "uuid-partnercommissionpayout-02"),
    (3, "PAR-0003", "Consolidated Branch PartnerCommissionPayout 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partnercommissionpayout-03"),
    (4, "PAR-0004", "Enterprise Audited PartnerCommissionPayout 4", 32800.00, 210.0, "ACTIVE", "uuid-partnercommissionpayout-04"),
    (5, "PAR-0005", "Executive Strategic PartnerCommissionPayout 5", 65000.00, 400.0, "ACTIVE", "uuid-partnercommissionpayout-05");

CREATE TABLE IF NOT EXISTS partner_network_certificationcredentials (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_certificationcredentials_code ON partner_network_certificationcredentials(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_certificationcredentials_org_status ON partner_network_certificationcredentials(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_certificationcredentials_priority ON partner_network_certificationcredentials(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_certificationcredentials_created_at ON partner_network_certificationcredentials(created_at);

-- Operational seed data fixtures for partner_network_certificationcredentials
INSERT OR IGNORE INTO partner_network_certificationcredentials (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CER-0001", "Primary Operational CertificationCredential 1", 24500.00, 150.0, "ACTIVE", "uuid-certificationcredential-01"),
    (2, "CER-0002", "Secondary Corporate CertificationCredential 2", 18200.50, 80.0, "ACTIVE", "uuid-certificationcredential-02"),
    (3, "CER-0003", "Consolidated Branch CertificationCredential 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-certificationcredential-03"),
    (4, "CER-0004", "Enterprise Audited CertificationCredential 4", 32800.00, 210.0, "ACTIVE", "uuid-certificationcredential-04"),
    (5, "CER-0005", "Executive Strategic CertificationCredential 5", 65000.00, 400.0, "ACTIVE", "uuid-certificationcredential-05");

CREATE TABLE IF NOT EXISTS partner_network_partnersalesgoals (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_partnersalesgoals_code ON partner_network_partnersalesgoals(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnersalesgoals_org_status ON partner_network_partnersalesgoals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnersalesgoals_priority ON partner_network_partnersalesgoals(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnersalesgoals_created_at ON partner_network_partnersalesgoals(created_at);

-- Operational seed data fixtures for partner_network_partnersalesgoals
INSERT OR IGNORE INTO partner_network_partnersalesgoals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartnerSalesGoal 1", 24500.00, 150.0, "ACTIVE", "uuid-partnersalesgoal-01"),
    (2, "PAR-0002", "Secondary Corporate PartnerSalesGoal 2", 18200.50, 80.0, "ACTIVE", "uuid-partnersalesgoal-02"),
    (3, "PAR-0003", "Consolidated Branch PartnerSalesGoal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partnersalesgoal-03"),
    (4, "PAR-0004", "Enterprise Audited PartnerSalesGoal 4", 32800.00, 210.0, "ACTIVE", "uuid-partnersalesgoal-04"),
    (5, "PAR-0005", "Executive Strategic PartnerSalesGoal 5", 65000.00, 400.0, "ACTIVE", "uuid-partnersalesgoal-05");

CREATE TABLE IF NOT EXISTS partner_network_reselleragreementcontracts (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_reselleragreementcontracts_code ON partner_network_reselleragreementcontracts(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_reselleragreementcontracts_org_status ON partner_network_reselleragreementcontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_reselleragreementcontracts_priority ON partner_network_reselleragreementcontracts(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_reselleragreementcontracts_created_at ON partner_network_reselleragreementcontracts(created_at);

-- Operational seed data fixtures for partner_network_reselleragreementcontracts
INSERT OR IGNORE INTO partner_network_reselleragreementcontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RES-0001", "Primary Operational ResellerAgreementContract 1", 24500.00, 150.0, "ACTIVE", "uuid-reselleragreementcontract-01"),
    (2, "RES-0002", "Secondary Corporate ResellerAgreementContract 2", 18200.50, 80.0, "ACTIVE", "uuid-reselleragreementcontract-02"),
    (3, "RES-0003", "Consolidated Branch ResellerAgreementContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-reselleragreementcontract-03"),
    (4, "RES-0004", "Enterprise Audited ResellerAgreementContract 4", 32800.00, 210.0, "ACTIVE", "uuid-reselleragreementcontract-04"),
    (5, "RES-0005", "Executive Strategic ResellerAgreementContract 5", 65000.00, 400.0, "ACTIVE", "uuid-reselleragreementcontract-05");

CREATE TABLE IF NOT EXISTS partner_network_leaddistributionrules (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_leaddistributionrules_code ON partner_network_leaddistributionrules(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_leaddistributionrules_org_status ON partner_network_leaddistributionrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_leaddistributionrules_priority ON partner_network_leaddistributionrules(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_leaddistributionrules_created_at ON partner_network_leaddistributionrules(created_at);

-- Operational seed data fixtures for partner_network_leaddistributionrules
INSERT OR IGNORE INTO partner_network_leaddistributionrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEA-0001", "Primary Operational LeadDistributionRule 1", 24500.00, 150.0, "ACTIVE", "uuid-leaddistributionrule-01"),
    (2, "LEA-0002", "Secondary Corporate LeadDistributionRule 2", 18200.50, 80.0, "ACTIVE", "uuid-leaddistributionrule-02"),
    (3, "LEA-0003", "Consolidated Branch LeadDistributionRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-leaddistributionrule-03"),
    (4, "LEA-0004", "Enterprise Audited LeadDistributionRule 4", 32800.00, 210.0, "ACTIVE", "uuid-leaddistributionrule-04"),
    (5, "LEA-0005", "Executive Strategic LeadDistributionRule 5", 65000.00, 400.0, "ACTIVE", "uuid-leaddistributionrule-05");

CREATE TABLE IF NOT EXISTS partner_network_partnerportalcredentials (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_partnerportalcredentials_code ON partner_network_partnerportalcredentials(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnerportalcredentials_org_status ON partner_network_partnerportalcredentials(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnerportalcredentials_priority ON partner_network_partnerportalcredentials(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnerportalcredentials_created_at ON partner_network_partnerportalcredentials(created_at);

-- Operational seed data fixtures for partner_network_partnerportalcredentials
INSERT OR IGNORE INTO partner_network_partnerportalcredentials (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartnerPortalCredential 1", 24500.00, 150.0, "ACTIVE", "uuid-partnerportalcredential-01"),
    (2, "PAR-0002", "Secondary Corporate PartnerPortalCredential 2", 18200.50, 80.0, "ACTIVE", "uuid-partnerportalcredential-02"),
    (3, "PAR-0003", "Consolidated Branch PartnerPortalCredential 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partnerportalcredential-03"),
    (4, "PAR-0004", "Enterprise Audited PartnerPortalCredential 4", 32800.00, 210.0, "ACTIVE", "uuid-partnerportalcredential-04"),
    (5, "PAR-0005", "Executive Strategic PartnerPortalCredential 5", 65000.00, 400.0, "ACTIVE", "uuid-partnerportalcredential-05");

CREATE TABLE IF NOT EXISTS partner_network_channelconflictdisputes (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_channelconflictdisputes_code ON partner_network_channelconflictdisputes(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelconflictdisputes_org_status ON partner_network_channelconflictdisputes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelconflictdisputes_priority ON partner_network_channelconflictdisputes(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelconflictdisputes_created_at ON partner_network_channelconflictdisputes(created_at);

-- Operational seed data fixtures for partner_network_channelconflictdisputes
INSERT OR IGNORE INTO partner_network_channelconflictdisputes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHA-0001", "Primary Operational ChannelConflictDispute 1", 24500.00, 150.0, "ACTIVE", "uuid-channelconflictdispute-01"),
    (2, "CHA-0002", "Secondary Corporate ChannelConflictDispute 2", 18200.50, 80.0, "ACTIVE", "uuid-channelconflictdispute-02"),
    (3, "CHA-0003", "Consolidated Branch ChannelConflictDispute 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-channelconflictdispute-03"),
    (4, "CHA-0004", "Enterprise Audited ChannelConflictDispute 4", 32800.00, 210.0, "ACTIVE", "uuid-channelconflictdispute-04"),
    (5, "CHA-0005", "Executive Strategic ChannelConflictDispute 5", 65000.00, 400.0, "ACTIVE", "uuid-channelconflictdispute-05");

CREATE TABLE IF NOT EXISTS partner_network_territorypartnerexclusivitys (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_territorypartnerexclusivitys_code ON partner_network_territorypartnerexclusivitys(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_territorypartnerexclusivitys_org_status ON partner_network_territorypartnerexclusivitys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_territorypartnerexclusivitys_priority ON partner_network_territorypartnerexclusivitys(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_territorypartnerexclusivitys_created_at ON partner_network_territorypartnerexclusivitys(created_at);

-- Operational seed data fixtures for partner_network_territorypartnerexclusivitys
INSERT OR IGNORE INTO partner_network_territorypartnerexclusivitys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TER-0001", "Primary Operational TerritoryPartnerExclusivity 1", 24500.00, 150.0, "ACTIVE", "uuid-territorypartnerexclusivity-01"),
    (2, "TER-0002", "Secondary Corporate TerritoryPartnerExclusivity 2", 18200.50, 80.0, "ACTIVE", "uuid-territorypartnerexclusivity-02"),
    (3, "TER-0003", "Consolidated Branch TerritoryPartnerExclusivity 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-territorypartnerexclusivity-03"),
    (4, "TER-0004", "Enterprise Audited TerritoryPartnerExclusivity 4", 32800.00, 210.0, "ACTIVE", "uuid-territorypartnerexclusivity-04"),
    (5, "TER-0005", "Executive Strategic TerritoryPartnerExclusivity 5", 65000.00, 400.0, "ACTIVE", "uuid-territorypartnerexclusivity-05");

CREATE TABLE IF NOT EXISTS partner_network_partnertrainingprogresss (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_partnertrainingprogresss_code ON partner_network_partnertrainingprogresss(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnertrainingprogresss_org_status ON partner_network_partnertrainingprogresss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnertrainingprogresss_priority ON partner_network_partnertrainingprogresss(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_partnertrainingprogresss_created_at ON partner_network_partnertrainingprogresss(created_at);

-- Operational seed data fixtures for partner_network_partnertrainingprogresss
INSERT OR IGNORE INTO partner_network_partnertrainingprogresss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAR-0001", "Primary Operational PartnerTrainingProgress 1", 24500.00, 150.0, "ACTIVE", "uuid-partnertrainingprogress-01"),
    (2, "PAR-0002", "Secondary Corporate PartnerTrainingProgress 2", 18200.50, 80.0, "ACTIVE", "uuid-partnertrainingprogress-02"),
    (3, "PAR-0003", "Consolidated Branch PartnerTrainingProgress 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-partnertrainingprogress-03"),
    (4, "PAR-0004", "Enterprise Audited PartnerTrainingProgress 4", 32800.00, 210.0, "ACTIVE", "uuid-partnertrainingprogress-04"),
    (5, "PAR-0005", "Executive Strategic PartnerTrainingProgress 5", 65000.00, 400.0, "ACTIVE", "uuid-partnertrainingprogress-05");

CREATE TABLE IF NOT EXISTS partner_network_jointsolutionlistings (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_jointsolutionlistings_code ON partner_network_jointsolutionlistings(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_jointsolutionlistings_org_status ON partner_network_jointsolutionlistings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_jointsolutionlistings_priority ON partner_network_jointsolutionlistings(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_jointsolutionlistings_created_at ON partner_network_jointsolutionlistings(created_at);

-- Operational seed data fixtures for partner_network_jointsolutionlistings
INSERT OR IGNORE INTO partner_network_jointsolutionlistings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "JOI-0001", "Primary Operational JointSolutionListing 1", 24500.00, 150.0, "ACTIVE", "uuid-jointsolutionlisting-01"),
    (2, "JOI-0002", "Secondary Corporate JointSolutionListing 2", 18200.50, 80.0, "ACTIVE", "uuid-jointsolutionlisting-02"),
    (3, "JOI-0003", "Consolidated Branch JointSolutionListing 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-jointsolutionlisting-03"),
    (4, "JOI-0004", "Enterprise Audited JointSolutionListing 4", 32800.00, 210.0, "ACTIVE", "uuid-jointsolutionlisting-04"),
    (5, "JOI-0005", "Executive Strategic JointSolutionListing 5", 65000.00, 400.0, "ACTIVE", "uuid-jointsolutionlisting-05");

CREATE TABLE IF NOT EXISTS partner_network_channelrevenueforecasts (
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

CREATE INDEX IF NOT EXISTS idx_partner_network_channelrevenueforecasts_code ON partner_network_channelrevenueforecasts(code);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelrevenueforecasts_org_status ON partner_network_channelrevenueforecasts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelrevenueforecasts_priority ON partner_network_channelrevenueforecasts(priority);
CREATE INDEX IF NOT EXISTS idx_partner_network_channelrevenueforecasts_created_at ON partner_network_channelrevenueforecasts(created_at);

-- Operational seed data fixtures for partner_network_channelrevenueforecasts
INSERT OR IGNORE INTO partner_network_channelrevenueforecasts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHA-0001", "Primary Operational ChannelRevenueForecast 1", 24500.00, 150.0, "ACTIVE", "uuid-channelrevenueforecast-01"),
    (2, "CHA-0002", "Secondary Corporate ChannelRevenueForecast 2", 18200.50, 80.0, "ACTIVE", "uuid-channelrevenueforecast-02"),
    (3, "CHA-0003", "Consolidated Branch ChannelRevenueForecast 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-channelrevenueforecast-03"),
    (4, "CHA-0004", "Enterprise Audited ChannelRevenueForecast 4", 32800.00, 210.0, "ACTIVE", "uuid-channelrevenueforecast-04"),
    (5, "CHA-0005", "Executive Strategic ChannelRevenueForecast 5", 65000.00, 400.0, "ACTIVE", "uuid-channelrevenueforecast-05");

