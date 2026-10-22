-- SmartERP Enterprise Titan Migration 051: Board Governance & Shareholder Proxy Resolutions DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS corporate_governance_boardresolutionvotes (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardresolutionvotes_code ON corporate_governance_boardresolutionvotes(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardresolutionvotes_org_status ON corporate_governance_boardresolutionvotes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardresolutionvotes_priority ON corporate_governance_boardresolutionvotes(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardresolutionvotes_created_at ON corporate_governance_boardresolutionvotes(created_at);

-- Operational seed data fixtures for corporate_governance_boardresolutionvotes
INSERT OR IGNORE INTO corporate_governance_boardresolutionvotes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BOA-0001", "Primary Operational BoardResolutionVote 1", 24500.00, 150.0, "ACTIVE", "uuid-boardresolutionvote-01"),
    (2, "BOA-0002", "Secondary Corporate BoardResolutionVote 2", 18200.50, 80.0, "ACTIVE", "uuid-boardresolutionvote-02"),
    (3, "BOA-0003", "Consolidated Branch BoardResolutionVote 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-boardresolutionvote-03"),
    (4, "BOA-0004", "Enterprise Audited BoardResolutionVote 4", 32800.00, 210.0, "ACTIVE", "uuid-boardresolutionvote-04"),
    (5, "BOA-0005", "Executive Strategic BoardResolutionVote 5", 65000.00, 400.0, "ACTIVE", "uuid-boardresolutionvote-05");

CREATE TABLE IF NOT EXISTS corporate_governance_shareholderproxyfilings (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproxyfilings_code ON corporate_governance_shareholderproxyfilings(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproxyfilings_org_status ON corporate_governance_shareholderproxyfilings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproxyfilings_priority ON corporate_governance_shareholderproxyfilings(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproxyfilings_created_at ON corporate_governance_shareholderproxyfilings(created_at);

-- Operational seed data fixtures for corporate_governance_shareholderproxyfilings
INSERT OR IGNORE INTO corporate_governance_shareholderproxyfilings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHA-0001", "Primary Operational ShareholderProxyFiling 1", 24500.00, 150.0, "ACTIVE", "uuid-shareholderproxyfiling-01"),
    (2, "SHA-0002", "Secondary Corporate ShareholderProxyFiling 2", 18200.50, 80.0, "ACTIVE", "uuid-shareholderproxyfiling-02"),
    (3, "SHA-0003", "Consolidated Branch ShareholderProxyFiling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shareholderproxyfiling-03"),
    (4, "SHA-0004", "Enterprise Audited ShareholderProxyFiling 4", 32800.00, 210.0, "ACTIVE", "uuid-shareholderproxyfiling-04"),
    (5, "SHA-0005", "Executive Strategic ShareholderProxyFiling 5", 65000.00, 400.0, "ACTIVE", "uuid-shareholderproxyfiling-05");

CREATE TABLE IF NOT EXISTS corporate_governance_committeemeetingcharters (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_committeemeetingcharters_code ON corporate_governance_committeemeetingcharters(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_committeemeetingcharters_org_status ON corporate_governance_committeemeetingcharters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_committeemeetingcharters_priority ON corporate_governance_committeemeetingcharters(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_committeemeetingcharters_created_at ON corporate_governance_committeemeetingcharters(created_at);

-- Operational seed data fixtures for corporate_governance_committeemeetingcharters
INSERT OR IGNORE INTO corporate_governance_committeemeetingcharters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CommitteeMeetingCharter 1", 24500.00, 150.0, "ACTIVE", "uuid-committeemeetingcharter-01"),
    (2, "COM-0002", "Secondary Corporate CommitteeMeetingCharter 2", 18200.50, 80.0, "ACTIVE", "uuid-committeemeetingcharter-02"),
    (3, "COM-0003", "Consolidated Branch CommitteeMeetingCharter 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-committeemeetingcharter-03"),
    (4, "COM-0004", "Enterprise Audited CommitteeMeetingCharter 4", 32800.00, 210.0, "ACTIVE", "uuid-committeemeetingcharter-04"),
    (5, "COM-0005", "Executive Strategic CommitteeMeetingCharter 5", 65000.00, 400.0, "ACTIVE", "uuid-committeemeetingcharter-05");

CREATE TABLE IF NOT EXISTS corporate_governance_directorfiduciarydutys (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_directorfiduciarydutys_code ON corporate_governance_directorfiduciarydutys(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_directorfiduciarydutys_org_status ON corporate_governance_directorfiduciarydutys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_directorfiduciarydutys_priority ON corporate_governance_directorfiduciarydutys(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_directorfiduciarydutys_created_at ON corporate_governance_directorfiduciarydutys(created_at);

-- Operational seed data fixtures for corporate_governance_directorfiduciarydutys
INSERT OR IGNORE INTO corporate_governance_directorfiduciarydutys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIR-0001", "Primary Operational DirectorFiduciaryDuty 1", 24500.00, 150.0, "ACTIVE", "uuid-directorfiduciaryduty-01"),
    (2, "DIR-0002", "Secondary Corporate DirectorFiduciaryDuty 2", 18200.50, 80.0, "ACTIVE", "uuid-directorfiduciaryduty-02"),
    (3, "DIR-0003", "Consolidated Branch DirectorFiduciaryDuty 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-directorfiduciaryduty-03"),
    (4, "DIR-0004", "Enterprise Audited DirectorFiduciaryDuty 4", 32800.00, 210.0, "ACTIVE", "uuid-directorfiduciaryduty-04"),
    (5, "DIR-0005", "Executive Strategic DirectorFiduciaryDuty 5", 65000.00, 400.0, "ACTIVE", "uuid-directorfiduciaryduty-05");

CREATE TABLE IF NOT EXISTS corporate_governance_annualgeneralmeetingnotices (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_annualgeneralmeetingnotices_code ON corporate_governance_annualgeneralmeetingnotices(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_annualgeneralmeetingnotices_org_status ON corporate_governance_annualgeneralmeetingnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_annualgeneralmeetingnotices_priority ON corporate_governance_annualgeneralmeetingnotices(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_annualgeneralmeetingnotices_created_at ON corporate_governance_annualgeneralmeetingnotices(created_at);

-- Operational seed data fixtures for corporate_governance_annualgeneralmeetingnotices
INSERT OR IGNORE INTO corporate_governance_annualgeneralmeetingnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ANN-0001", "Primary Operational AnnualGeneralMeetingNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-annualgeneralmeetingnotice-01"),
    (2, "ANN-0002", "Secondary Corporate AnnualGeneralMeetingNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-annualgeneralmeetingnotice-02"),
    (3, "ANN-0003", "Consolidated Branch AnnualGeneralMeetingNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-annualgeneralmeetingnotice-03"),
    (4, "ANN-0004", "Enterprise Audited AnnualGeneralMeetingNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-annualgeneralmeetingnotice-04"),
    (5, "ANN-0005", "Executive Strategic AnnualGeneralMeetingNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-annualgeneralmeetingnotice-05");

CREATE TABLE IF NOT EXISTS corporate_governance_executivesuccessionmatrixs (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_executivesuccessionmatrixs_code ON corporate_governance_executivesuccessionmatrixs(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_executivesuccessionmatrixs_org_status ON corporate_governance_executivesuccessionmatrixs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_executivesuccessionmatrixs_priority ON corporate_governance_executivesuccessionmatrixs(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_executivesuccessionmatrixs_created_at ON corporate_governance_executivesuccessionmatrixs(created_at);

-- Operational seed data fixtures for corporate_governance_executivesuccessionmatrixs
INSERT OR IGNORE INTO corporate_governance_executivesuccessionmatrixs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutiveSuccessionMatrix 1", 24500.00, 150.0, "ACTIVE", "uuid-executivesuccessionmatrix-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutiveSuccessionMatrix 2", 18200.50, 80.0, "ACTIVE", "uuid-executivesuccessionmatrix-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutiveSuccessionMatrix 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executivesuccessionmatrix-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutiveSuccessionMatrix 4", 32800.00, 210.0, "ACTIVE", "uuid-executivesuccessionmatrix-04"),
    (5, "EXE-0005", "Executive Strategic ExecutiveSuccessionMatrix 5", 65000.00, 400.0, "ACTIVE", "uuid-executivesuccessionmatrix-05");

CREATE TABLE IF NOT EXISTS corporate_governance_statutoryfilingdisclosures (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_statutoryfilingdisclosures_code ON corporate_governance_statutoryfilingdisclosures(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_statutoryfilingdisclosures_org_status ON corporate_governance_statutoryfilingdisclosures(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_statutoryfilingdisclosures_priority ON corporate_governance_statutoryfilingdisclosures(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_statutoryfilingdisclosures_created_at ON corporate_governance_statutoryfilingdisclosures(created_at);

-- Operational seed data fixtures for corporate_governance_statutoryfilingdisclosures
INSERT OR IGNORE INTO corporate_governance_statutoryfilingdisclosures (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StatutoryFilingDisclosure 1", 24500.00, 150.0, "ACTIVE", "uuid-statutoryfilingdisclosure-01"),
    (2, "STA-0002", "Secondary Corporate StatutoryFilingDisclosure 2", 18200.50, 80.0, "ACTIVE", "uuid-statutoryfilingdisclosure-02"),
    (3, "STA-0003", "Consolidated Branch StatutoryFilingDisclosure 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-statutoryfilingdisclosure-03"),
    (4, "STA-0004", "Enterprise Audited StatutoryFilingDisclosure 4", 32800.00, 210.0, "ACTIVE", "uuid-statutoryfilingdisclosure-04"),
    (5, "STA-0005", "Executive Strategic StatutoryFilingDisclosure 5", 65000.00, 400.0, "ACTIVE", "uuid-statutoryfilingdisclosure-05");

CREATE TABLE IF NOT EXISTS corporate_governance_conflictofinterestdeclarations (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_conflictofinterestdeclarations_code ON corporate_governance_conflictofinterestdeclarations(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_conflictofinterestdeclarations_org_status ON corporate_governance_conflictofinterestdeclarations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_conflictofinterestdeclarations_priority ON corporate_governance_conflictofinterestdeclarations(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_conflictofinterestdeclarations_created_at ON corporate_governance_conflictofinterestdeclarations(created_at);

-- Operational seed data fixtures for corporate_governance_conflictofinterestdeclarations
INSERT OR IGNORE INTO corporate_governance_conflictofinterestdeclarations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ConflictOfInterestDeclaration 1", 24500.00, 150.0, "ACTIVE", "uuid-conflictofinterestdeclaration-01"),
    (2, "CON-0002", "Secondary Corporate ConflictOfInterestDeclaration 2", 18200.50, 80.0, "ACTIVE", "uuid-conflictofinterestdeclaration-02"),
    (3, "CON-0003", "Consolidated Branch ConflictOfInterestDeclaration 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-conflictofinterestdeclaration-03"),
    (4, "CON-0004", "Enterprise Audited ConflictOfInterestDeclaration 4", 32800.00, 210.0, "ACTIVE", "uuid-conflictofinterestdeclaration-04"),
    (5, "CON-0005", "Executive Strategic ConflictOfInterestDeclaration 5", 65000.00, 400.0, "ACTIVE", "uuid-conflictofinterestdeclaration-05");

CREATE TABLE IF NOT EXISTS corporate_governance_shareholderproposalentrys (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproposalentrys_code ON corporate_governance_shareholderproposalentrys(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproposalentrys_org_status ON corporate_governance_shareholderproposalentrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproposalentrys_priority ON corporate_governance_shareholderproposalentrys(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_shareholderproposalentrys_created_at ON corporate_governance_shareholderproposalentrys(created_at);

-- Operational seed data fixtures for corporate_governance_shareholderproposalentrys
INSERT OR IGNORE INTO corporate_governance_shareholderproposalentrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHA-0001", "Primary Operational ShareholderProposalEntry 1", 24500.00, 150.0, "ACTIVE", "uuid-shareholderproposalentry-01"),
    (2, "SHA-0002", "Secondary Corporate ShareholderProposalEntry 2", 18200.50, 80.0, "ACTIVE", "uuid-shareholderproposalentry-02"),
    (3, "SHA-0003", "Consolidated Branch ShareholderProposalEntry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shareholderproposalentry-03"),
    (4, "SHA-0004", "Enterprise Audited ShareholderProposalEntry 4", 32800.00, 210.0, "ACTIVE", "uuid-shareholderproposalentry-04"),
    (5, "SHA-0005", "Executive Strategic ShareholderProposalEntry 5", 65000.00, 400.0, "ACTIVE", "uuid-shareholderproposalentry-05");

CREATE TABLE IF NOT EXISTS corporate_governance_minutesofmeetingdocs (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_minutesofmeetingdocs_code ON corporate_governance_minutesofmeetingdocs(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_minutesofmeetingdocs_org_status ON corporate_governance_minutesofmeetingdocs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_minutesofmeetingdocs_priority ON corporate_governance_minutesofmeetingdocs(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_minutesofmeetingdocs_created_at ON corporate_governance_minutesofmeetingdocs(created_at);

-- Operational seed data fixtures for corporate_governance_minutesofmeetingdocs
INSERT OR IGNORE INTO corporate_governance_minutesofmeetingdocs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MIN-0001", "Primary Operational MinutesOfMeetingDoc 1", 24500.00, 150.0, "ACTIVE", "uuid-minutesofmeetingdoc-01"),
    (2, "MIN-0002", "Secondary Corporate MinutesOfMeetingDoc 2", 18200.50, 80.0, "ACTIVE", "uuid-minutesofmeetingdoc-02"),
    (3, "MIN-0003", "Consolidated Branch MinutesOfMeetingDoc 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-minutesofmeetingdoc-03"),
    (4, "MIN-0004", "Enterprise Audited MinutesOfMeetingDoc 4", 32800.00, 210.0, "ACTIVE", "uuid-minutesofmeetingdoc-04"),
    (5, "MIN-0005", "Executive Strategic MinutesOfMeetingDoc 5", 65000.00, 400.0, "ACTIVE", "uuid-minutesofmeetingdoc-05");

CREATE TABLE IF NOT EXISTS corporate_governance_boardmemberevaluations (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardmemberevaluations_code ON corporate_governance_boardmemberevaluations(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardmemberevaluations_org_status ON corporate_governance_boardmemberevaluations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardmemberevaluations_priority ON corporate_governance_boardmemberevaluations(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_boardmemberevaluations_created_at ON corporate_governance_boardmemberevaluations(created_at);

-- Operational seed data fixtures for corporate_governance_boardmemberevaluations
INSERT OR IGNORE INTO corporate_governance_boardmemberevaluations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BOA-0001", "Primary Operational BoardMemberEvaluation 1", 24500.00, 150.0, "ACTIVE", "uuid-boardmemberevaluation-01"),
    (2, "BOA-0002", "Secondary Corporate BoardMemberEvaluation 2", 18200.50, 80.0, "ACTIVE", "uuid-boardmemberevaluation-02"),
    (3, "BOA-0003", "Consolidated Branch BoardMemberEvaluation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-boardmemberevaluation-03"),
    (4, "BOA-0004", "Enterprise Audited BoardMemberEvaluation 4", 32800.00, 210.0, "ACTIVE", "uuid-boardmemberevaluation-04"),
    (5, "BOA-0005", "Executive Strategic BoardMemberEvaluation 5", 65000.00, 400.0, "ACTIVE", "uuid-boardmemberevaluation-05");

CREATE TABLE IF NOT EXISTS corporate_governance_delegationofauthorityrules (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_delegationofauthorityrules_code ON corporate_governance_delegationofauthorityrules(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_delegationofauthorityrules_org_status ON corporate_governance_delegationofauthorityrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_delegationofauthorityrules_priority ON corporate_governance_delegationofauthorityrules(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_delegationofauthorityrules_created_at ON corporate_governance_delegationofauthorityrules(created_at);

-- Operational seed data fixtures for corporate_governance_delegationofauthorityrules
INSERT OR IGNORE INTO corporate_governance_delegationofauthorityrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEL-0001", "Primary Operational DelegationOfAuthorityRule 1", 24500.00, 150.0, "ACTIVE", "uuid-delegationofauthorityrule-01"),
    (2, "DEL-0002", "Secondary Corporate DelegationOfAuthorityRule 2", 18200.50, 80.0, "ACTIVE", "uuid-delegationofauthorityrule-02"),
    (3, "DEL-0003", "Consolidated Branch DelegationOfAuthorityRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-delegationofauthorityrule-03"),
    (4, "DEL-0004", "Enterprise Audited DelegationOfAuthorityRule 4", 32800.00, 210.0, "ACTIVE", "uuid-delegationofauthorityrule-04"),
    (5, "DEL-0005", "Executive Strategic DelegationOfAuthorityRule 5", 65000.00, 400.0, "ACTIVE", "uuid-delegationofauthorityrule-05");

CREATE TABLE IF NOT EXISTS corporate_governance_whistleblowertriagecases (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_whistleblowertriagecases_code ON corporate_governance_whistleblowertriagecases(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_whistleblowertriagecases_org_status ON corporate_governance_whistleblowertriagecases(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_whistleblowertriagecases_priority ON corporate_governance_whistleblowertriagecases(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_whistleblowertriagecases_created_at ON corporate_governance_whistleblowertriagecases(created_at);

-- Operational seed data fixtures for corporate_governance_whistleblowertriagecases
INSERT OR IGNORE INTO corporate_governance_whistleblowertriagecases (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WHI-0001", "Primary Operational WhistleblowerTriageCase 1", 24500.00, 150.0, "ACTIVE", "uuid-whistleblowertriagecase-01"),
    (2, "WHI-0002", "Secondary Corporate WhistleblowerTriageCase 2", 18200.50, 80.0, "ACTIVE", "uuid-whistleblowertriagecase-02"),
    (3, "WHI-0003", "Consolidated Branch WhistleblowerTriageCase 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-whistleblowertriagecase-03"),
    (4, "WHI-0004", "Enterprise Audited WhistleblowerTriageCase 4", 32800.00, 210.0, "ACTIVE", "uuid-whistleblowertriagecase-04"),
    (5, "WHI-0005", "Executive Strategic WhistleblowerTriageCase 5", 65000.00, 400.0, "ACTIVE", "uuid-whistleblowertriagecase-05");

CREATE TABLE IF NOT EXISTS corporate_governance_fiduciaryriskassessments (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_fiduciaryriskassessments_code ON corporate_governance_fiduciaryriskassessments(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_fiduciaryriskassessments_org_status ON corporate_governance_fiduciaryriskassessments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_fiduciaryriskassessments_priority ON corporate_governance_fiduciaryriskassessments(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_fiduciaryriskassessments_created_at ON corporate_governance_fiduciaryriskassessments(created_at);

-- Operational seed data fixtures for corporate_governance_fiduciaryriskassessments
INSERT OR IGNORE INTO corporate_governance_fiduciaryriskassessments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FID-0001", "Primary Operational FiduciaryRiskAssessment 1", 24500.00, 150.0, "ACTIVE", "uuid-fiduciaryriskassessment-01"),
    (2, "FID-0002", "Secondary Corporate FiduciaryRiskAssessment 2", 18200.50, 80.0, "ACTIVE", "uuid-fiduciaryriskassessment-02"),
    (3, "FID-0003", "Consolidated Branch FiduciaryRiskAssessment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fiduciaryriskassessment-03"),
    (4, "FID-0004", "Enterprise Audited FiduciaryRiskAssessment 4", 32800.00, 210.0, "ACTIVE", "uuid-fiduciaryriskassessment-04"),
    (5, "FID-0005", "Executive Strategic FiduciaryRiskAssessment 5", 65000.00, 400.0, "ACTIVE", "uuid-fiduciaryriskassessment-05");

CREATE TABLE IF NOT EXISTS corporate_governance_investorrelationsreleases (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_investorrelationsreleases_code ON corporate_governance_investorrelationsreleases(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_investorrelationsreleases_org_status ON corporate_governance_investorrelationsreleases(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_investorrelationsreleases_priority ON corporate_governance_investorrelationsreleases(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_investorrelationsreleases_created_at ON corporate_governance_investorrelationsreleases(created_at);

-- Operational seed data fixtures for corporate_governance_investorrelationsreleases
INSERT OR IGNORE INTO corporate_governance_investorrelationsreleases (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INV-0001", "Primary Operational InvestorRelationsRelease 1", 24500.00, 150.0, "ACTIVE", "uuid-investorrelationsrelease-01"),
    (2, "INV-0002", "Secondary Corporate InvestorRelationsRelease 2", 18200.50, 80.0, "ACTIVE", "uuid-investorrelationsrelease-02"),
    (3, "INV-0003", "Consolidated Branch InvestorRelationsRelease 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-investorrelationsrelease-03"),
    (4, "INV-0004", "Enterprise Audited InvestorRelationsRelease 4", 32800.00, 210.0, "ACTIVE", "uuid-investorrelationsrelease-04"),
    (5, "INV-0005", "Executive Strategic InvestorRelationsRelease 5", 65000.00, 400.0, "ACTIVE", "uuid-investorrelationsrelease-05");

CREATE TABLE IF NOT EXISTS corporate_governance_corporatesealregisters (
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

CREATE INDEX IF NOT EXISTS idx_corporate_governance_corporatesealregisters_code ON corporate_governance_corporatesealregisters(code);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_corporatesealregisters_org_status ON corporate_governance_corporatesealregisters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_corporatesealregisters_priority ON corporate_governance_corporatesealregisters(priority);
CREATE INDEX IF NOT EXISTS idx_corporate_governance_corporatesealregisters_created_at ON corporate_governance_corporatesealregisters(created_at);

-- Operational seed data fixtures for corporate_governance_corporatesealregisters
INSERT OR IGNORE INTO corporate_governance_corporatesealregisters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COR-0001", "Primary Operational CorporateSealRegister 1", 24500.00, 150.0, "ACTIVE", "uuid-corporatesealregister-01"),
    (2, "COR-0002", "Secondary Corporate CorporateSealRegister 2", 18200.50, 80.0, "ACTIVE", "uuid-corporatesealregister-02"),
    (3, "COR-0003", "Consolidated Branch CorporateSealRegister 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-corporatesealregister-03"),
    (4, "COR-0004", "Enterprise Audited CorporateSealRegister 4", 32800.00, 210.0, "ACTIVE", "uuid-corporatesealregister-04"),
    (5, "COR-0005", "Executive Strategic CorporateSealRegister 5", 65000.00, 400.0, "ACTIVE", "uuid-corporatesealregister-05");

