-- SmartERP Enterprise Titan Migration 041: Customer Success & Retention Engineering DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS customer_success_customerhealthscores (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_customerhealthscores_code ON customer_success_customerhealthscores(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerhealthscores_org_status ON customer_success_customerhealthscores(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerhealthscores_priority ON customer_success_customerhealthscores(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerhealthscores_created_at ON customer_success_customerhealthscores(created_at);

-- Operational seed data fixtures for customer_success_customerhealthscores
INSERT OR IGNORE INTO customer_success_customerhealthscores (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerHealthScore 1", 24500.00, 150.0, "ACTIVE", "uuid-customerhealthscore-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerHealthScore 2", 18200.50, 80.0, "ACTIVE", "uuid-customerhealthscore-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerHealthScore 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerhealthscore-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerHealthScore 4", 32800.00, 210.0, "ACTIVE", "uuid-customerhealthscore-04"),
    (5, "CUS-0005", "Executive Strategic CustomerHealthScore 5", 65000.00, 400.0, "ACTIVE", "uuid-customerhealthscore-05");

CREATE TABLE IF NOT EXISTS customer_success_onboardingmilestoneplans (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_onboardingmilestoneplans_code ON customer_success_onboardingmilestoneplans(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_onboardingmilestoneplans_org_status ON customer_success_onboardingmilestoneplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_onboardingmilestoneplans_priority ON customer_success_onboardingmilestoneplans(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_onboardingmilestoneplans_created_at ON customer_success_onboardingmilestoneplans(created_at);

-- Operational seed data fixtures for customer_success_onboardingmilestoneplans
INSERT OR IGNORE INTO customer_success_onboardingmilestoneplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ONB-0001", "Primary Operational OnboardingMilestonePlan 1", 24500.00, 150.0, "ACTIVE", "uuid-onboardingmilestoneplan-01"),
    (2, "ONB-0002", "Secondary Corporate OnboardingMilestonePlan 2", 18200.50, 80.0, "ACTIVE", "uuid-onboardingmilestoneplan-02"),
    (3, "ONB-0003", "Consolidated Branch OnboardingMilestonePlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-onboardingmilestoneplan-03"),
    (4, "ONB-0004", "Enterprise Audited OnboardingMilestonePlan 4", 32800.00, 210.0, "ACTIVE", "uuid-onboardingmilestoneplan-04"),
    (5, "ONB-0005", "Executive Strategic OnboardingMilestonePlan 5", 65000.00, 400.0, "ACTIVE", "uuid-onboardingmilestoneplan-05");

CREATE TABLE IF NOT EXISTS customer_success_quarterlybusinessreviews (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_quarterlybusinessreviews_code ON customer_success_quarterlybusinessreviews(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_quarterlybusinessreviews_org_status ON customer_success_quarterlybusinessreviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_quarterlybusinessreviews_priority ON customer_success_quarterlybusinessreviews(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_quarterlybusinessreviews_created_at ON customer_success_quarterlybusinessreviews(created_at);

-- Operational seed data fixtures for customer_success_quarterlybusinessreviews
INSERT OR IGNORE INTO customer_success_quarterlybusinessreviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "QUA-0001", "Primary Operational QuarterlyBusinessReview 1", 24500.00, 150.0, "ACTIVE", "uuid-quarterlybusinessreview-01"),
    (2, "QUA-0002", "Secondary Corporate QuarterlyBusinessReview 2", 18200.50, 80.0, "ACTIVE", "uuid-quarterlybusinessreview-02"),
    (3, "QUA-0003", "Consolidated Branch QuarterlyBusinessReview 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-quarterlybusinessreview-03"),
    (4, "QUA-0004", "Enterprise Audited QuarterlyBusinessReview 4", 32800.00, 210.0, "ACTIVE", "uuid-quarterlybusinessreview-04"),
    (5, "QUA-0005", "Executive Strategic QuarterlyBusinessReview 5", 65000.00, 400.0, "ACTIVE", "uuid-quarterlybusinessreview-05");

CREATE TABLE IF NOT EXISTS customer_success_npsfeedbacksurveys (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_npsfeedbacksurveys_code ON customer_success_npsfeedbacksurveys(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_npsfeedbacksurveys_org_status ON customer_success_npsfeedbacksurveys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_npsfeedbacksurveys_priority ON customer_success_npsfeedbacksurveys(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_npsfeedbacksurveys_created_at ON customer_success_npsfeedbacksurveys(created_at);

-- Operational seed data fixtures for customer_success_npsfeedbacksurveys
INSERT OR IGNORE INTO customer_success_npsfeedbacksurveys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "NPS-0001", "Primary Operational NPSFeedbackSurvey 1", 24500.00, 150.0, "ACTIVE", "uuid-npsfeedbacksurvey-01"),
    (2, "NPS-0002", "Secondary Corporate NPSFeedbackSurvey 2", 18200.50, 80.0, "ACTIVE", "uuid-npsfeedbacksurvey-02"),
    (3, "NPS-0003", "Consolidated Branch NPSFeedbackSurvey 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-npsfeedbacksurvey-03"),
    (4, "NPS-0004", "Enterprise Audited NPSFeedbackSurvey 4", 32800.00, 210.0, "ACTIVE", "uuid-npsfeedbacksurvey-04"),
    (5, "NPS-0005", "Executive Strategic NPSFeedbackSurvey 5", 65000.00, 400.0, "ACTIVE", "uuid-npsfeedbacksurvey-05");

CREATE TABLE IF NOT EXISTS customer_success_churnearlywarningsignals (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_churnearlywarningsignals_code ON customer_success_churnearlywarningsignals(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_churnearlywarningsignals_org_status ON customer_success_churnearlywarningsignals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_churnearlywarningsignals_priority ON customer_success_churnearlywarningsignals(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_churnearlywarningsignals_created_at ON customer_success_churnearlywarningsignals(created_at);

-- Operational seed data fixtures for customer_success_churnearlywarningsignals
INSERT OR IGNORE INTO customer_success_churnearlywarningsignals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHU-0001", "Primary Operational ChurnEarlyWarningSignal 1", 24500.00, 150.0, "ACTIVE", "uuid-churnearlywarningsignal-01"),
    (2, "CHU-0002", "Secondary Corporate ChurnEarlyWarningSignal 2", 18200.50, 80.0, "ACTIVE", "uuid-churnearlywarningsignal-02"),
    (3, "CHU-0003", "Consolidated Branch ChurnEarlyWarningSignal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-churnearlywarningsignal-03"),
    (4, "CHU-0004", "Enterprise Audited ChurnEarlyWarningSignal 4", 32800.00, 210.0, "ACTIVE", "uuid-churnearlywarningsignal-04"),
    (5, "CHU-0005", "Executive Strategic ChurnEarlyWarningSignal 5", 65000.00, 400.0, "ACTIVE", "uuid-churnearlywarningsignal-05");

CREATE TABLE IF NOT EXISTS customer_success_accountexpansiondeals (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_accountexpansiondeals_code ON customer_success_accountexpansiondeals(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_accountexpansiondeals_org_status ON customer_success_accountexpansiondeals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_accountexpansiondeals_priority ON customer_success_accountexpansiondeals(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_accountexpansiondeals_created_at ON customer_success_accountexpansiondeals(created_at);

-- Operational seed data fixtures for customer_success_accountexpansiondeals
INSERT OR IGNORE INTO customer_success_accountexpansiondeals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACC-0001", "Primary Operational AccountExpansionDeal 1", 24500.00, 150.0, "ACTIVE", "uuid-accountexpansiondeal-01"),
    (2, "ACC-0002", "Secondary Corporate AccountExpansionDeal 2", 18200.50, 80.0, "ACTIVE", "uuid-accountexpansiondeal-02"),
    (3, "ACC-0003", "Consolidated Branch AccountExpansionDeal 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-accountexpansiondeal-03"),
    (4, "ACC-0004", "Enterprise Audited AccountExpansionDeal 4", 32800.00, 210.0, "ACTIVE", "uuid-accountexpansiondeal-04"),
    (5, "ACC-0005", "Executive Strategic AccountExpansionDeal 5", 65000.00, 400.0, "ACTIVE", "uuid-accountexpansiondeal-05");

CREATE TABLE IF NOT EXISTS customer_success_productadoptionmetrics (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_productadoptionmetrics_code ON customer_success_productadoptionmetrics(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_productadoptionmetrics_org_status ON customer_success_productadoptionmetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_productadoptionmetrics_priority ON customer_success_productadoptionmetrics(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_productadoptionmetrics_created_at ON customer_success_productadoptionmetrics(created_at);

-- Operational seed data fixtures for customer_success_productadoptionmetrics
INSERT OR IGNORE INTO customer_success_productadoptionmetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProductAdoptionMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-productadoptionmetric-01"),
    (2, "PRO-0002", "Secondary Corporate ProductAdoptionMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-productadoptionmetric-02"),
    (3, "PRO-0003", "Consolidated Branch ProductAdoptionMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-productadoptionmetric-03"),
    (4, "PRO-0004", "Enterprise Audited ProductAdoptionMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-productadoptionmetric-04"),
    (5, "PRO-0005", "Executive Strategic ProductAdoptionMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-productadoptionmetric-05");

CREATE TABLE IF NOT EXISTS customer_success_customerjourneytouchpoints (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_customerjourneytouchpoints_code ON customer_success_customerjourneytouchpoints(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerjourneytouchpoints_org_status ON customer_success_customerjourneytouchpoints(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerjourneytouchpoints_priority ON customer_success_customerjourneytouchpoints(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerjourneytouchpoints_created_at ON customer_success_customerjourneytouchpoints(created_at);

-- Operational seed data fixtures for customer_success_customerjourneytouchpoints
INSERT OR IGNORE INTO customer_success_customerjourneytouchpoints (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerJourneyTouchpoint 1", 24500.00, 150.0, "ACTIVE", "uuid-customerjourneytouchpoint-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerJourneyTouchpoint 2", 18200.50, 80.0, "ACTIVE", "uuid-customerjourneytouchpoint-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerJourneyTouchpoint 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerjourneytouchpoint-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerJourneyTouchpoint 4", 32800.00, 210.0, "ACTIVE", "uuid-customerjourneytouchpoint-04"),
    (5, "CUS-0005", "Executive Strategic CustomerJourneyTouchpoint 5", 65000.00, 400.0, "ACTIVE", "uuid-customerjourneytouchpoint-05");

CREATE TABLE IF NOT EXISTS customer_success_supportescalationflags (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_supportescalationflags_code ON customer_success_supportescalationflags(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_supportescalationflags_org_status ON customer_success_supportescalationflags(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_supportescalationflags_priority ON customer_success_supportescalationflags(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_supportescalationflags_created_at ON customer_success_supportescalationflags(created_at);

-- Operational seed data fixtures for customer_success_supportescalationflags
INSERT OR IGNORE INTO customer_success_supportescalationflags (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupportEscalationFlag 1", 24500.00, 150.0, "ACTIVE", "uuid-supportescalationflag-01"),
    (2, "SUP-0002", "Secondary Corporate SupportEscalationFlag 2", 18200.50, 80.0, "ACTIVE", "uuid-supportescalationflag-02"),
    (3, "SUP-0003", "Consolidated Branch SupportEscalationFlag 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supportescalationflag-03"),
    (4, "SUP-0004", "Enterprise Audited SupportEscalationFlag 4", 32800.00, 210.0, "ACTIVE", "uuid-supportescalationflag-04"),
    (5, "SUP-0005", "Executive Strategic SupportEscalationFlag 5", 65000.00, 400.0, "ACTIVE", "uuid-supportescalationflag-05");

CREATE TABLE IF NOT EXISTS customer_success_successplanobjectives (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_successplanobjectives_code ON customer_success_successplanobjectives(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_successplanobjectives_org_status ON customer_success_successplanobjectives(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_successplanobjectives_priority ON customer_success_successplanobjectives(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_successplanobjectives_created_at ON customer_success_successplanobjectives(created_at);

-- Operational seed data fixtures for customer_success_successplanobjectives
INSERT OR IGNORE INTO customer_success_successplanobjectives (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUC-0001", "Primary Operational SuccessPlanObjective 1", 24500.00, 150.0, "ACTIVE", "uuid-successplanobjective-01"),
    (2, "SUC-0002", "Secondary Corporate SuccessPlanObjective 2", 18200.50, 80.0, "ACTIVE", "uuid-successplanobjective-02"),
    (3, "SUC-0003", "Consolidated Branch SuccessPlanObjective 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-successplanobjective-03"),
    (4, "SUC-0004", "Enterprise Audited SuccessPlanObjective 4", 32800.00, 210.0, "ACTIVE", "uuid-successplanobjective-04"),
    (5, "SUC-0005", "Executive Strategic SuccessPlanObjective 5", 65000.00, 400.0, "ACTIVE", "uuid-successplanobjective-05");

CREATE TABLE IF NOT EXISTS customer_success_clientreferenceadvocates (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_clientreferenceadvocates_code ON customer_success_clientreferenceadvocates(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_clientreferenceadvocates_org_status ON customer_success_clientreferenceadvocates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_clientreferenceadvocates_priority ON customer_success_clientreferenceadvocates(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_clientreferenceadvocates_created_at ON customer_success_clientreferenceadvocates(created_at);

-- Operational seed data fixtures for customer_success_clientreferenceadvocates
INSERT OR IGNORE INTO customer_success_clientreferenceadvocates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CLI-0001", "Primary Operational ClientReferenceAdvocate 1", 24500.00, 150.0, "ACTIVE", "uuid-clientreferenceadvocate-01"),
    (2, "CLI-0002", "Secondary Corporate ClientReferenceAdvocate 2", 18200.50, 80.0, "ACTIVE", "uuid-clientreferenceadvocate-02"),
    (3, "CLI-0003", "Consolidated Branch ClientReferenceAdvocate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-clientreferenceadvocate-03"),
    (4, "CLI-0004", "Enterprise Audited ClientReferenceAdvocate 4", 32800.00, 210.0, "ACTIVE", "uuid-clientreferenceadvocate-04"),
    (5, "CLI-0005", "Executive Strategic ClientReferenceAdvocate 5", 65000.00, 400.0, "ACTIVE", "uuid-clientreferenceadvocate-05");

CREATE TABLE IF NOT EXISTS customer_success_renewalforecastpipelines (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_renewalforecastpipelines_code ON customer_success_renewalforecastpipelines(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_renewalforecastpipelines_org_status ON customer_success_renewalforecastpipelines(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_renewalforecastpipelines_priority ON customer_success_renewalforecastpipelines(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_renewalforecastpipelines_created_at ON customer_success_renewalforecastpipelines(created_at);

-- Operational seed data fixtures for customer_success_renewalforecastpipelines
INSERT OR IGNORE INTO customer_success_renewalforecastpipelines (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REN-0001", "Primary Operational RenewalForecastPipeline 1", 24500.00, 150.0, "ACTIVE", "uuid-renewalforecastpipeline-01"),
    (2, "REN-0002", "Secondary Corporate RenewalForecastPipeline 2", 18200.50, 80.0, "ACTIVE", "uuid-renewalforecastpipeline-02"),
    (3, "REN-0003", "Consolidated Branch RenewalForecastPipeline 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-renewalforecastpipeline-03"),
    (4, "REN-0004", "Enterprise Audited RenewalForecastPipeline 4", 32800.00, 210.0, "ACTIVE", "uuid-renewalforecastpipeline-04"),
    (5, "REN-0005", "Executive Strategic RenewalForecastPipeline 5", 65000.00, 400.0, "ACTIVE", "uuid-renewalforecastpipeline-05");

CREATE TABLE IF NOT EXISTS customer_success_productusageanalyticss (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_productusageanalyticss_code ON customer_success_productusageanalyticss(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_productusageanalyticss_org_status ON customer_success_productusageanalyticss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_productusageanalyticss_priority ON customer_success_productusageanalyticss(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_productusageanalyticss_created_at ON customer_success_productusageanalyticss(created_at);

-- Operational seed data fixtures for customer_success_productusageanalyticss
INSERT OR IGNORE INTO customer_success_productusageanalyticss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational ProductUsageAnalytics 1", 24500.00, 150.0, "ACTIVE", "uuid-productusageanalytics-01"),
    (2, "PRO-0002", "Secondary Corporate ProductUsageAnalytics 2", 18200.50, 80.0, "ACTIVE", "uuid-productusageanalytics-02"),
    (3, "PRO-0003", "Consolidated Branch ProductUsageAnalytics 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-productusageanalytics-03"),
    (4, "PRO-0004", "Enterprise Audited ProductUsageAnalytics 4", 32800.00, 210.0, "ACTIVE", "uuid-productusageanalytics-04"),
    (5, "PRO-0005", "Executive Strategic ProductUsageAnalytics 5", 65000.00, 400.0, "ACTIVE", "uuid-productusageanalytics-05");

CREATE TABLE IF NOT EXISTS customer_success_customerengagementscores (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_customerengagementscores_code ON customer_success_customerengagementscores(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerengagementscores_org_status ON customer_success_customerengagementscores(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerengagementscores_priority ON customer_success_customerengagementscores(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_customerengagementscores_created_at ON customer_success_customerengagementscores(created_at);

-- Operational seed data fixtures for customer_success_customerengagementscores
INSERT OR IGNORE INTO customer_success_customerengagementscores (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerEngagementScore 1", 24500.00, 150.0, "ACTIVE", "uuid-customerengagementscore-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerEngagementScore 2", 18200.50, 80.0, "ACTIVE", "uuid-customerengagementscore-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerEngagementScore 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerengagementscore-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerEngagementScore 4", 32800.00, 210.0, "ACTIVE", "uuid-customerengagementscore-04"),
    (5, "CUS-0005", "Executive Strategic CustomerEngagementScore 5", 65000.00, 400.0, "ACTIVE", "uuid-customerengagementscore-05");

CREATE TABLE IF NOT EXISTS customer_success_voiceofcustomerfeedbacks (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_voiceofcustomerfeedbacks_code ON customer_success_voiceofcustomerfeedbacks(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_voiceofcustomerfeedbacks_org_status ON customer_success_voiceofcustomerfeedbacks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_voiceofcustomerfeedbacks_priority ON customer_success_voiceofcustomerfeedbacks(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_voiceofcustomerfeedbacks_created_at ON customer_success_voiceofcustomerfeedbacks(created_at);

-- Operational seed data fixtures for customer_success_voiceofcustomerfeedbacks
INSERT OR IGNORE INTO customer_success_voiceofcustomerfeedbacks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VOI-0001", "Primary Operational VoiceOfCustomerFeedback 1", 24500.00, 150.0, "ACTIVE", "uuid-voiceofcustomerfeedback-01"),
    (2, "VOI-0002", "Secondary Corporate VoiceOfCustomerFeedback 2", 18200.50, 80.0, "ACTIVE", "uuid-voiceofcustomerfeedback-02"),
    (3, "VOI-0003", "Consolidated Branch VoiceOfCustomerFeedback 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-voiceofcustomerfeedback-03"),
    (4, "VOI-0004", "Enterprise Audited VoiceOfCustomerFeedback 4", 32800.00, 210.0, "ACTIVE", "uuid-voiceofcustomerfeedback-04"),
    (5, "VOI-0005", "Executive Strategic VoiceOfCustomerFeedback 5", 65000.00, 400.0, "ACTIVE", "uuid-voiceofcustomerfeedback-05");

CREATE TABLE IF NOT EXISTS customer_success_successexecutiveassignments (
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

CREATE INDEX IF NOT EXISTS idx_customer_success_successexecutiveassignments_code ON customer_success_successexecutiveassignments(code);
CREATE INDEX IF NOT EXISTS idx_customer_success_successexecutiveassignments_org_status ON customer_success_successexecutiveassignments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_success_successexecutiveassignments_priority ON customer_success_successexecutiveassignments(priority);
CREATE INDEX IF NOT EXISTS idx_customer_success_successexecutiveassignments_created_at ON customer_success_successexecutiveassignments(created_at);

-- Operational seed data fixtures for customer_success_successexecutiveassignments
INSERT OR IGNORE INTO customer_success_successexecutiveassignments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUC-0001", "Primary Operational SuccessExecutiveAssignment 1", 24500.00, 150.0, "ACTIVE", "uuid-successexecutiveassignment-01"),
    (2, "SUC-0002", "Secondary Corporate SuccessExecutiveAssignment 2", 18200.50, 80.0, "ACTIVE", "uuid-successexecutiveassignment-02"),
    (3, "SUC-0003", "Consolidated Branch SuccessExecutiveAssignment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-successexecutiveassignment-03"),
    (4, "SUC-0004", "Enterprise Audited SuccessExecutiveAssignment 4", 32800.00, 210.0, "ACTIVE", "uuid-successexecutiveassignment-04"),
    (5, "SUC-0005", "Executive Strategic SuccessExecutiveAssignment 5", 65000.00, 400.0, "ACTIVE", "uuid-successexecutiveassignment-05");

