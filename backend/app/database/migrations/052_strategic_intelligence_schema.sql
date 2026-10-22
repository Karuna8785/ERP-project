-- SmartERP Enterprise Titan Migration 052: Market Landscaping & Competitive Intelligence DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS strategic_intelligence_marketresearchreports (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketresearchreports_code ON strategic_intelligence_marketresearchreports(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketresearchreports_org_status ON strategic_intelligence_marketresearchreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketresearchreports_priority ON strategic_intelligence_marketresearchreports(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketresearchreports_created_at ON strategic_intelligence_marketresearchreports(created_at);

-- Operational seed data fixtures for strategic_intelligence_marketresearchreports
INSERT OR IGNORE INTO strategic_intelligence_marketresearchreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAR-0001", "Primary Operational MarketResearchReport 1", 24500.00, 150.0, "ACTIVE", "uuid-marketresearchreport-01"),
    (2, "MAR-0002", "Secondary Corporate MarketResearchReport 2", 18200.50, 80.0, "ACTIVE", "uuid-marketresearchreport-02"),
    (3, "MAR-0003", "Consolidated Branch MarketResearchReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-marketresearchreport-03"),
    (4, "MAR-0004", "Enterprise Audited MarketResearchReport 4", 32800.00, 210.0, "ACTIVE", "uuid-marketresearchreport-04"),
    (5, "MAR-0005", "Executive Strategic MarketResearchReport 5", 65000.00, 400.0, "ACTIVE", "uuid-marketresearchreport-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_competitorproductbenchmarks (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_competitorproductbenchmarks_code ON strategic_intelligence_competitorproductbenchmarks(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_competitorproductbenchmarks_org_status ON strategic_intelligence_competitorproductbenchmarks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_competitorproductbenchmarks_priority ON strategic_intelligence_competitorproductbenchmarks(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_competitorproductbenchmarks_created_at ON strategic_intelligence_competitorproductbenchmarks(created_at);

-- Operational seed data fixtures for strategic_intelligence_competitorproductbenchmarks
INSERT OR IGNORE INTO strategic_intelligence_competitorproductbenchmarks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CompetitorProductBenchmark 1", 24500.00, 150.0, "ACTIVE", "uuid-competitorproductbenchmark-01"),
    (2, "COM-0002", "Secondary Corporate CompetitorProductBenchmark 2", 18200.50, 80.0, "ACTIVE", "uuid-competitorproductbenchmark-02"),
    (3, "COM-0003", "Consolidated Branch CompetitorProductBenchmark 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-competitorproductbenchmark-03"),
    (4, "COM-0004", "Enterprise Audited CompetitorProductBenchmark 4", 32800.00, 210.0, "ACTIVE", "uuid-competitorproductbenchmark-04"),
    (5, "COM-0005", "Executive Strategic CompetitorProductBenchmark 5", 65000.00, 400.0, "ACTIVE", "uuid-competitorproductbenchmark-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_swotanalysismatrixs (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_swotanalysismatrixs_code ON strategic_intelligence_swotanalysismatrixs(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_swotanalysismatrixs_org_status ON strategic_intelligence_swotanalysismatrixs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_swotanalysismatrixs_priority ON strategic_intelligence_swotanalysismatrixs(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_swotanalysismatrixs_created_at ON strategic_intelligence_swotanalysismatrixs(created_at);

-- Operational seed data fixtures for strategic_intelligence_swotanalysismatrixs
INSERT OR IGNORE INTO strategic_intelligence_swotanalysismatrixs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SWO-0001", "Primary Operational SWOTAnalysisMatrix 1", 24500.00, 150.0, "ACTIVE", "uuid-swotanalysismatrix-01"),
    (2, "SWO-0002", "Secondary Corporate SWOTAnalysisMatrix 2", 18200.50, 80.0, "ACTIVE", "uuid-swotanalysismatrix-02"),
    (3, "SWO-0003", "Consolidated Branch SWOTAnalysisMatrix 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-swotanalysismatrix-03"),
    (4, "SWO-0004", "Enterprise Audited SWOTAnalysisMatrix 4", 32800.00, 210.0, "ACTIVE", "uuid-swotanalysismatrix-04"),
    (5, "SWO-0005", "Executive Strategic SWOTAnalysisMatrix 5", 65000.00, 400.0, "ACTIVE", "uuid-swotanalysismatrix-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_industrytrendsignals (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_industrytrendsignals_code ON strategic_intelligence_industrytrendsignals(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_industrytrendsignals_org_status ON strategic_intelligence_industrytrendsignals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_industrytrendsignals_priority ON strategic_intelligence_industrytrendsignals(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_industrytrendsignals_created_at ON strategic_intelligence_industrytrendsignals(created_at);

-- Operational seed data fixtures for strategic_intelligence_industrytrendsignals
INSERT OR IGNORE INTO strategic_intelligence_industrytrendsignals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "IND-0001", "Primary Operational IndustryTrendSignal 1", 24500.00, 150.0, "ACTIVE", "uuid-industrytrendsignal-01"),
    (2, "IND-0002", "Secondary Corporate IndustryTrendSignal 2", 18200.50, 80.0, "ACTIVE", "uuid-industrytrendsignal-02"),
    (3, "IND-0003", "Consolidated Branch IndustryTrendSignal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-industrytrendsignal-03"),
    (4, "IND-0004", "Enterprise Audited IndustryTrendSignal 4", 32800.00, 210.0, "ACTIVE", "uuid-industrytrendsignal-04"),
    (5, "IND-0005", "Executive Strategic IndustryTrendSignal 5", 65000.00, 400.0, "ACTIVE", "uuid-industrytrendsignal-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_patentlandscapestudys (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_patentlandscapestudys_code ON strategic_intelligence_patentlandscapestudys(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_patentlandscapestudys_org_status ON strategic_intelligence_patentlandscapestudys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_patentlandscapestudys_priority ON strategic_intelligence_patentlandscapestudys(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_patentlandscapestudys_created_at ON strategic_intelligence_patentlandscapestudys(created_at);

-- Operational seed data fixtures for strategic_intelligence_patentlandscapestudys
INSERT OR IGNORE INTO strategic_intelligence_patentlandscapestudys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAT-0001", "Primary Operational PatentLandscapeStudy 1", 24500.00, 150.0, "ACTIVE", "uuid-patentlandscapestudy-01"),
    (2, "PAT-0002", "Secondary Corporate PatentLandscapeStudy 2", 18200.50, 80.0, "ACTIVE", "uuid-patentlandscapestudy-02"),
    (3, "PAT-0003", "Consolidated Branch PatentLandscapeStudy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-patentlandscapestudy-03"),
    (4, "PAT-0004", "Enterprise Audited PatentLandscapeStudy 4", 32800.00, 210.0, "ACTIVE", "uuid-patentlandscapestudy-04"),
    (5, "PAT-0005", "Executive Strategic PatentLandscapeStudy 5", 65000.00, 400.0, "ACTIVE", "uuid-patentlandscapestudy-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_pricingintelligencedatas (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_pricingintelligencedatas_code ON strategic_intelligence_pricingintelligencedatas(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_pricingintelligencedatas_org_status ON strategic_intelligence_pricingintelligencedatas(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_pricingintelligencedatas_priority ON strategic_intelligence_pricingintelligencedatas(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_pricingintelligencedatas_created_at ON strategic_intelligence_pricingintelligencedatas(created_at);

-- Operational seed data fixtures for strategic_intelligence_pricingintelligencedatas
INSERT OR IGNORE INTO strategic_intelligence_pricingintelligencedatas (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PricingIntelligenceData 1", 24500.00, 150.0, "ACTIVE", "uuid-pricingintelligencedata-01"),
    (2, "PRI-0002", "Secondary Corporate PricingIntelligenceData 2", 18200.50, 80.0, "ACTIVE", "uuid-pricingintelligencedata-02"),
    (3, "PRI-0003", "Consolidated Branch PricingIntelligenceData 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-pricingintelligencedata-03"),
    (4, "PRI-0004", "Enterprise Audited PricingIntelligenceData 4", 32800.00, 210.0, "ACTIVE", "uuid-pricingintelligencedata-04"),
    (5, "PRI-0005", "Executive Strategic PricingIntelligenceData 5", 65000.00, 400.0, "ACTIVE", "uuid-pricingintelligencedata-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_customerwinlossinterviews (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_customerwinlossinterviews_code ON strategic_intelligence_customerwinlossinterviews(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_customerwinlossinterviews_org_status ON strategic_intelligence_customerwinlossinterviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_customerwinlossinterviews_priority ON strategic_intelligence_customerwinlossinterviews(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_customerwinlossinterviews_created_at ON strategic_intelligence_customerwinlossinterviews(created_at);

-- Operational seed data fixtures for strategic_intelligence_customerwinlossinterviews
INSERT OR IGNORE INTO strategic_intelligence_customerwinlossinterviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerWinLossInterview 1", 24500.00, 150.0, "ACTIVE", "uuid-customerwinlossinterview-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerWinLossInterview 2", 18200.50, 80.0, "ACTIVE", "uuid-customerwinlossinterview-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerWinLossInterview 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerwinlossinterview-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerWinLossInterview 4", 32800.00, 210.0, "ACTIVE", "uuid-customerwinlossinterview-04"),
    (5, "CUS-0005", "Executive Strategic CustomerWinLossInterview 5", 65000.00, 400.0, "ACTIVE", "uuid-customerwinlossinterview-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_marketshareestimates (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketshareestimates_code ON strategic_intelligence_marketshareestimates(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketshareestimates_org_status ON strategic_intelligence_marketshareestimates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketshareestimates_priority ON strategic_intelligence_marketshareestimates(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_marketshareestimates_created_at ON strategic_intelligence_marketshareestimates(created_at);

-- Operational seed data fixtures for strategic_intelligence_marketshareestimates
INSERT OR IGNORE INTO strategic_intelligence_marketshareestimates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAR-0001", "Primary Operational MarketShareEstimate 1", 24500.00, 150.0, "ACTIVE", "uuid-marketshareestimate-01"),
    (2, "MAR-0002", "Secondary Corporate MarketShareEstimate 2", 18200.50, 80.0, "ACTIVE", "uuid-marketshareestimate-02"),
    (3, "MAR-0003", "Consolidated Branch MarketShareEstimate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-marketshareestimate-03"),
    (4, "MAR-0004", "Enterprise Audited MarketShareEstimate 4", 32800.00, 210.0, "ACTIVE", "uuid-marketshareestimate-04"),
    (5, "MAR-0005", "Executive Strategic MarketShareEstimate 5", 65000.00, 400.0, "ACTIVE", "uuid-marketshareestimate-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_strategicpartnershipopps (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_strategicpartnershipopps_code ON strategic_intelligence_strategicpartnershipopps(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_strategicpartnershipopps_org_status ON strategic_intelligence_strategicpartnershipopps(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_strategicpartnershipopps_priority ON strategic_intelligence_strategicpartnershipopps(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_strategicpartnershipopps_created_at ON strategic_intelligence_strategicpartnershipopps(created_at);

-- Operational seed data fixtures for strategic_intelligence_strategicpartnershipopps
INSERT OR IGNORE INTO strategic_intelligence_strategicpartnershipopps (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STR-0001", "Primary Operational StrategicPartnershipOpp 1", 24500.00, 150.0, "ACTIVE", "uuid-strategicpartnershipopp-01"),
    (2, "STR-0002", "Secondary Corporate StrategicPartnershipOpp 2", 18200.50, 80.0, "ACTIVE", "uuid-strategicpartnershipopp-02"),
    (3, "STR-0003", "Consolidated Branch StrategicPartnershipOpp 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-strategicpartnershipopp-03"),
    (4, "STR-0004", "Enterprise Audited StrategicPartnershipOpp 4", 32800.00, 210.0, "ACTIVE", "uuid-strategicpartnershipopp-04"),
    (5, "STR-0005", "Executive Strategic StrategicPartnershipOpp 5", 65000.00, 400.0, "ACTIVE", "uuid-strategicpartnershipopp-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_macroeconomicindicators (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_macroeconomicindicators_code ON strategic_intelligence_macroeconomicindicators(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_macroeconomicindicators_org_status ON strategic_intelligence_macroeconomicindicators(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_macroeconomicindicators_priority ON strategic_intelligence_macroeconomicindicators(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_macroeconomicindicators_created_at ON strategic_intelligence_macroeconomicindicators(created_at);

-- Operational seed data fixtures for strategic_intelligence_macroeconomicindicators
INSERT OR IGNORE INTO strategic_intelligence_macroeconomicindicators (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MAC-0001", "Primary Operational MacroeconomicIndicator 1", 24500.00, 150.0, "ACTIVE", "uuid-macroeconomicindicator-01"),
    (2, "MAC-0002", "Secondary Corporate MacroeconomicIndicator 2", 18200.50, 80.0, "ACTIVE", "uuid-macroeconomicindicator-02"),
    (3, "MAC-0003", "Consolidated Branch MacroeconomicIndicator 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-macroeconomicindicator-03"),
    (4, "MAC-0004", "Enterprise Audited MacroeconomicIndicator 4", 32800.00, 210.0, "ACTIVE", "uuid-macroeconomicindicator-04"),
    (5, "MAC-0005", "Executive Strategic MacroeconomicIndicator 5", 65000.00, 400.0, "ACTIVE", "uuid-macroeconomicindicator-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_disruptivethreatalerts (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_disruptivethreatalerts_code ON strategic_intelligence_disruptivethreatalerts(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_disruptivethreatalerts_org_status ON strategic_intelligence_disruptivethreatalerts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_disruptivethreatalerts_priority ON strategic_intelligence_disruptivethreatalerts(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_disruptivethreatalerts_created_at ON strategic_intelligence_disruptivethreatalerts(created_at);

-- Operational seed data fixtures for strategic_intelligence_disruptivethreatalerts
INSERT OR IGNORE INTO strategic_intelligence_disruptivethreatalerts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DisruptiveThreatAlert 1", 24500.00, 150.0, "ACTIVE", "uuid-disruptivethreatalert-01"),
    (2, "DIS-0002", "Secondary Corporate DisruptiveThreatAlert 2", 18200.50, 80.0, "ACTIVE", "uuid-disruptivethreatalert-02"),
    (3, "DIS-0003", "Consolidated Branch DisruptiveThreatAlert 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-disruptivethreatalert-03"),
    (4, "DIS-0004", "Enterprise Audited DisruptiveThreatAlert 4", 32800.00, 210.0, "ACTIVE", "uuid-disruptivethreatalert-04"),
    (5, "DIS-0005", "Executive Strategic DisruptiveThreatAlert 5", 65000.00, 400.0, "ACTIVE", "uuid-disruptivethreatalert-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_acquisitiontargetprofiles (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_acquisitiontargetprofiles_code ON strategic_intelligence_acquisitiontargetprofiles(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_acquisitiontargetprofiles_org_status ON strategic_intelligence_acquisitiontargetprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_acquisitiontargetprofiles_priority ON strategic_intelligence_acquisitiontargetprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_acquisitiontargetprofiles_created_at ON strategic_intelligence_acquisitiontargetprofiles(created_at);

-- Operational seed data fixtures for strategic_intelligence_acquisitiontargetprofiles
INSERT OR IGNORE INTO strategic_intelligence_acquisitiontargetprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACQ-0001", "Primary Operational AcquisitionTargetProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-acquisitiontargetprofile-01"),
    (2, "ACQ-0002", "Secondary Corporate AcquisitionTargetProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-acquisitiontargetprofile-02"),
    (3, "ACQ-0003", "Consolidated Branch AcquisitionTargetProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-acquisitiontargetprofile-03"),
    (4, "ACQ-0004", "Enterprise Audited AcquisitionTargetProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-acquisitiontargetprofile-04"),
    (5, "ACQ-0005", "Executive Strategic AcquisitionTargetProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-acquisitiontargetprofile-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_brandperceptionindexs (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_brandperceptionindexs_code ON strategic_intelligence_brandperceptionindexs(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_brandperceptionindexs_org_status ON strategic_intelligence_brandperceptionindexs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_brandperceptionindexs_priority ON strategic_intelligence_brandperceptionindexs(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_brandperceptionindexs_created_at ON strategic_intelligence_brandperceptionindexs(created_at);

-- Operational seed data fixtures for strategic_intelligence_brandperceptionindexs
INSERT OR IGNORE INTO strategic_intelligence_brandperceptionindexs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BRA-0001", "Primary Operational BrandPerceptionIndex 1", 24500.00, 150.0, "ACTIVE", "uuid-brandperceptionindex-01"),
    (2, "BRA-0002", "Secondary Corporate BrandPerceptionIndex 2", 18200.50, 80.0, "ACTIVE", "uuid-brandperceptionindex-02"),
    (3, "BRA-0003", "Consolidated Branch BrandPerceptionIndex 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-brandperceptionindex-03"),
    (4, "BRA-0004", "Enterprise Audited BrandPerceptionIndex 4", 32800.00, 210.0, "ACTIVE", "uuid-brandperceptionindex-04"),
    (5, "BRA-0005", "Executive Strategic BrandPerceptionIndex 5", 65000.00, 400.0, "ACTIVE", "uuid-brandperceptionindex-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_valuechainmappings (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_valuechainmappings_code ON strategic_intelligence_valuechainmappings(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_valuechainmappings_org_status ON strategic_intelligence_valuechainmappings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_valuechainmappings_priority ON strategic_intelligence_valuechainmappings(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_valuechainmappings_created_at ON strategic_intelligence_valuechainmappings(created_at);

-- Operational seed data fixtures for strategic_intelligence_valuechainmappings
INSERT OR IGNORE INTO strategic_intelligence_valuechainmappings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VAL-0001", "Primary Operational ValueChainMapping 1", 24500.00, 150.0, "ACTIVE", "uuid-valuechainmapping-01"),
    (2, "VAL-0002", "Secondary Corporate ValueChainMapping 2", 18200.50, 80.0, "ACTIVE", "uuid-valuechainmapping-02"),
    (3, "VAL-0003", "Consolidated Branch ValueChainMapping 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-valuechainmapping-03"),
    (4, "VAL-0004", "Enterprise Audited ValueChainMapping 4", 32800.00, 210.0, "ACTIVE", "uuid-valuechainmapping-04"),
    (5, "VAL-0005", "Executive Strategic ValueChainMapping 5", 65000.00, 400.0, "ACTIVE", "uuid-valuechainmapping-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_scenariosimulationmodels (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_scenariosimulationmodels_code ON strategic_intelligence_scenariosimulationmodels(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_scenariosimulationmodels_org_status ON strategic_intelligence_scenariosimulationmodels(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_scenariosimulationmodels_priority ON strategic_intelligence_scenariosimulationmodels(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_scenariosimulationmodels_created_at ON strategic_intelligence_scenariosimulationmodels(created_at);

-- Operational seed data fixtures for strategic_intelligence_scenariosimulationmodels
INSERT OR IGNORE INTO strategic_intelligence_scenariosimulationmodels (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SCE-0001", "Primary Operational ScenarioSimulationModel 1", 24500.00, 150.0, "ACTIVE", "uuid-scenariosimulationmodel-01"),
    (2, "SCE-0002", "Secondary Corporate ScenarioSimulationModel 2", 18200.50, 80.0, "ACTIVE", "uuid-scenariosimulationmodel-02"),
    (3, "SCE-0003", "Consolidated Branch ScenarioSimulationModel 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-scenariosimulationmodel-03"),
    (4, "SCE-0004", "Enterprise Audited ScenarioSimulationModel 4", 32800.00, 210.0, "ACTIVE", "uuid-scenariosimulationmodel-04"),
    (5, "SCE-0005", "Executive Strategic ScenarioSimulationModel 5", 65000.00, 400.0, "ACTIVE", "uuid-scenariosimulationmodel-05");

CREATE TABLE IF NOT EXISTS strategic_intelligence_executivebriefingbriefs (
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

CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_executivebriefingbriefs_code ON strategic_intelligence_executivebriefingbriefs(code);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_executivebriefingbriefs_org_status ON strategic_intelligence_executivebriefingbriefs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_executivebriefingbriefs_priority ON strategic_intelligence_executivebriefingbriefs(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_intelligence_executivebriefingbriefs_created_at ON strategic_intelligence_executivebriefingbriefs(created_at);

-- Operational seed data fixtures for strategic_intelligence_executivebriefingbriefs
INSERT OR IGNORE INTO strategic_intelligence_executivebriefingbriefs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutiveBriefingBrief 1", 24500.00, 150.0, "ACTIVE", "uuid-executivebriefingbrief-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutiveBriefingBrief 2", 18200.50, 80.0, "ACTIVE", "uuid-executivebriefingbrief-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutiveBriefingBrief 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executivebriefingbrief-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutiveBriefingBrief 4", 32800.00, 210.0, "ACTIVE", "uuid-executivebriefingbrief-04"),
    (5, "EXE-0005", "Executive Strategic ExecutiveBriefingBrief 5", 65000.00, 400.0, "ACTIVE", "uuid-executivebriefingbrief-05");

