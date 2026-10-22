-- SmartERP Enterprise Titan Migration 055: Customer Experience (CX) & Sentiment Analytics DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS customer_experience_customerjourneymapstages (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_customerjourneymapstages_code ON customer_experience_customerjourneymapstages(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerjourneymapstages_org_status ON customer_experience_customerjourneymapstages(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerjourneymapstages_priority ON customer_experience_customerjourneymapstages(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerjourneymapstages_created_at ON customer_experience_customerjourneymapstages(created_at);

-- Operational seed data fixtures for customer_experience_customerjourneymapstages
INSERT OR IGNORE INTO customer_experience_customerjourneymapstages (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerJourneyMapStage 1", 24500.00, 150.0, "ACTIVE", "uuid-customerjourneymapstage-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerJourneyMapStage 2", 18200.50, 80.0, "ACTIVE", "uuid-customerjourneymapstage-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerJourneyMapStage 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerjourneymapstage-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerJourneyMapStage 4", 32800.00, 210.0, "ACTIVE", "uuid-customerjourneymapstage-04"),
    (5, "CUS-0005", "Executive Strategic CustomerJourneyMapStage 5", 65000.00, 400.0, "ACTIVE", "uuid-customerjourneymapstage-05");

CREATE TABLE IF NOT EXISTS customer_experience_csatsurveysubmissions (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_csatsurveysubmissions_code ON customer_experience_csatsurveysubmissions(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_csatsurveysubmissions_org_status ON customer_experience_csatsurveysubmissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_csatsurveysubmissions_priority ON customer_experience_csatsurveysubmissions(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_csatsurveysubmissions_created_at ON customer_experience_csatsurveysubmissions(created_at);

-- Operational seed data fixtures for customer_experience_csatsurveysubmissions
INSERT OR IGNORE INTO customer_experience_csatsurveysubmissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CSA-0001", "Primary Operational CSATSurveySubmission 1", 24500.00, 150.0, "ACTIVE", "uuid-csatsurveysubmission-01"),
    (2, "CSA-0002", "Secondary Corporate CSATSurveySubmission 2", 18200.50, 80.0, "ACTIVE", "uuid-csatsurveysubmission-02"),
    (3, "CSA-0003", "Consolidated Branch CSATSurveySubmission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-csatsurveysubmission-03"),
    (4, "CSA-0004", "Enterprise Audited CSATSurveySubmission 4", 32800.00, 210.0, "ACTIVE", "uuid-csatsurveysubmission-04"),
    (5, "CSA-0005", "Executive Strategic CSATSurveySubmission 5", 65000.00, 400.0, "ACTIVE", "uuid-csatsurveysubmission-05");

CREATE TABLE IF NOT EXISTS customer_experience_npsscorecardmetrics (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_npsscorecardmetrics_code ON customer_experience_npsscorecardmetrics(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_npsscorecardmetrics_org_status ON customer_experience_npsscorecardmetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_npsscorecardmetrics_priority ON customer_experience_npsscorecardmetrics(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_npsscorecardmetrics_created_at ON customer_experience_npsscorecardmetrics(created_at);

-- Operational seed data fixtures for customer_experience_npsscorecardmetrics
INSERT OR IGNORE INTO customer_experience_npsscorecardmetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "NPS-0001", "Primary Operational NPSScorecardMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-npsscorecardmetric-01"),
    (2, "NPS-0002", "Secondary Corporate NPSScorecardMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-npsscorecardmetric-02"),
    (3, "NPS-0003", "Consolidated Branch NPSScorecardMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-npsscorecardmetric-03"),
    (4, "NPS-0004", "Enterprise Audited NPSScorecardMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-npsscorecardmetric-04"),
    (5, "NPS-0005", "Executive Strategic NPSScorecardMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-npsscorecardmetric-05");

CREATE TABLE IF NOT EXISTS customer_experience_sentimentnlpanalysiss (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_sentimentnlpanalysiss_code ON customer_experience_sentimentnlpanalysiss(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_sentimentnlpanalysiss_org_status ON customer_experience_sentimentnlpanalysiss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_sentimentnlpanalysiss_priority ON customer_experience_sentimentnlpanalysiss(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_sentimentnlpanalysiss_created_at ON customer_experience_sentimentnlpanalysiss(created_at);

-- Operational seed data fixtures for customer_experience_sentimentnlpanalysiss
INSERT OR IGNORE INTO customer_experience_sentimentnlpanalysiss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEN-0001", "Primary Operational SentimentNLPAnalysis 1", 24500.00, 150.0, "ACTIVE", "uuid-sentimentnlpanalysis-01"),
    (2, "SEN-0002", "Secondary Corporate SentimentNLPAnalysis 2", 18200.50, 80.0, "ACTIVE", "uuid-sentimentnlpanalysis-02"),
    (3, "SEN-0003", "Consolidated Branch SentimentNLPAnalysis 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sentimentnlpanalysis-03"),
    (4, "SEN-0004", "Enterprise Audited SentimentNLPAnalysis 4", 32800.00, 210.0, "ACTIVE", "uuid-sentimentnlpanalysis-04"),
    (5, "SEN-0005", "Executive Strategic SentimentNLPAnalysis 5", 65000.00, 400.0, "ACTIVE", "uuid-sentimentnlpanalysis-05");

CREATE TABLE IF NOT EXISTS customer_experience_customereffortscorecess (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_customereffortscorecess_code ON customer_experience_customereffortscorecess(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customereffortscorecess_org_status ON customer_experience_customereffortscorecess(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customereffortscorecess_priority ON customer_experience_customereffortscorecess(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customereffortscorecess_created_at ON customer_experience_customereffortscorecess(created_at);

-- Operational seed data fixtures for customer_experience_customereffortscorecess
INSERT OR IGNORE INTO customer_experience_customereffortscorecess (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerEffortScoreCES 1", 24500.00, 150.0, "ACTIVE", "uuid-customereffortscoreces-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerEffortScoreCES 2", 18200.50, 80.0, "ACTIVE", "uuid-customereffortscoreces-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerEffortScoreCES 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customereffortscoreces-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerEffortScoreCES 4", 32800.00, 210.0, "ACTIVE", "uuid-customereffortscoreces-04"),
    (5, "CUS-0005", "Executive Strategic CustomerEffortScoreCES 5", 65000.00, 400.0, "ACTIVE", "uuid-customereffortscoreces-05");

CREATE TABLE IF NOT EXISTS customer_experience_voiceofcustomerfeedbacks (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_voiceofcustomerfeedbacks_code ON customer_experience_voiceofcustomerfeedbacks(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_voiceofcustomerfeedbacks_org_status ON customer_experience_voiceofcustomerfeedbacks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_voiceofcustomerfeedbacks_priority ON customer_experience_voiceofcustomerfeedbacks(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_voiceofcustomerfeedbacks_created_at ON customer_experience_voiceofcustomerfeedbacks(created_at);

-- Operational seed data fixtures for customer_experience_voiceofcustomerfeedbacks
INSERT OR IGNORE INTO customer_experience_voiceofcustomerfeedbacks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VOI-0001", "Primary Operational VoiceOfCustomerFeedback 1", 24500.00, 150.0, "ACTIVE", "uuid-voiceofcustomerfeedback-01"),
    (2, "VOI-0002", "Secondary Corporate VoiceOfCustomerFeedback 2", 18200.50, 80.0, "ACTIVE", "uuid-voiceofcustomerfeedback-02"),
    (3, "VOI-0003", "Consolidated Branch VoiceOfCustomerFeedback 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-voiceofcustomerfeedback-03"),
    (4, "VOI-0004", "Enterprise Audited VoiceOfCustomerFeedback 4", 32800.00, 210.0, "ACTIVE", "uuid-voiceofcustomerfeedback-04"),
    (5, "VOI-0005", "Executive Strategic VoiceOfCustomerFeedback 5", 65000.00, 400.0, "ACTIVE", "uuid-voiceofcustomerfeedback-05");

CREATE TABLE IF NOT EXISTS customer_experience_omnichanneltouchpointevents (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_omnichanneltouchpointevents_code ON customer_experience_omnichanneltouchpointevents(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_omnichanneltouchpointevents_org_status ON customer_experience_omnichanneltouchpointevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_omnichanneltouchpointevents_priority ON customer_experience_omnichanneltouchpointevents(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_omnichanneltouchpointevents_created_at ON customer_experience_omnichanneltouchpointevents(created_at);

-- Operational seed data fixtures for customer_experience_omnichanneltouchpointevents
INSERT OR IGNORE INTO customer_experience_omnichanneltouchpointevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OMN-0001", "Primary Operational OmnichannelTouchpointEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-omnichanneltouchpointevent-01"),
    (2, "OMN-0002", "Secondary Corporate OmnichannelTouchpointEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-omnichanneltouchpointevent-02"),
    (3, "OMN-0003", "Consolidated Branch OmnichannelTouchpointEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-omnichanneltouchpointevent-03"),
    (4, "OMN-0004", "Enterprise Audited OmnichannelTouchpointEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-omnichanneltouchpointevent-04"),
    (5, "OMN-0005", "Executive Strategic OmnichannelTouchpointEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-omnichanneltouchpointevent-05");

CREATE TABLE IF NOT EXISTS customer_experience_customerchurnpredictions (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_customerchurnpredictions_code ON customer_experience_customerchurnpredictions(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerchurnpredictions_org_status ON customer_experience_customerchurnpredictions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerchurnpredictions_priority ON customer_experience_customerchurnpredictions(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerchurnpredictions_created_at ON customer_experience_customerchurnpredictions(created_at);

-- Operational seed data fixtures for customer_experience_customerchurnpredictions
INSERT OR IGNORE INTO customer_experience_customerchurnpredictions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerChurnPrediction 1", 24500.00, 150.0, "ACTIVE", "uuid-customerchurnprediction-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerChurnPrediction 2", 18200.50, 80.0, "ACTIVE", "uuid-customerchurnprediction-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerChurnPrediction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerchurnprediction-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerChurnPrediction 4", 32800.00, 210.0, "ACTIVE", "uuid-customerchurnprediction-04"),
    (5, "CUS-0005", "Executive Strategic CustomerChurnPrediction 5", 65000.00, 400.0, "ACTIVE", "uuid-customerchurnprediction-05");

CREATE TABLE IF NOT EXISTS customer_experience_supportresolutiontimekpis (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_supportresolutiontimekpis_code ON customer_experience_supportresolutiontimekpis(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_supportresolutiontimekpis_org_status ON customer_experience_supportresolutiontimekpis(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_supportresolutiontimekpis_priority ON customer_experience_supportresolutiontimekpis(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_supportresolutiontimekpis_created_at ON customer_experience_supportresolutiontimekpis(created_at);

-- Operational seed data fixtures for customer_experience_supportresolutiontimekpis
INSERT OR IGNORE INTO customer_experience_supportresolutiontimekpis (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupportResolutionTimeKPI 1", 24500.00, 150.0, "ACTIVE", "uuid-supportresolutiontimekpi-01"),
    (2, "SUP-0002", "Secondary Corporate SupportResolutionTimeKPI 2", 18200.50, 80.0, "ACTIVE", "uuid-supportresolutiontimekpi-02"),
    (3, "SUP-0003", "Consolidated Branch SupportResolutionTimeKPI 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supportresolutiontimekpi-03"),
    (4, "SUP-0004", "Enterprise Audited SupportResolutionTimeKPI 4", 32800.00, 210.0, "ACTIVE", "uuid-supportresolutiontimekpi-04"),
    (5, "SUP-0005", "Executive Strategic SupportResolutionTimeKPI 5", 65000.00, 400.0, "ACTIVE", "uuid-supportresolutiontimekpi-05");

CREATE TABLE IF NOT EXISTS customer_experience_personalizationprofiles (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_personalizationprofiles_code ON customer_experience_personalizationprofiles(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_personalizationprofiles_org_status ON customer_experience_personalizationprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_personalizationprofiles_priority ON customer_experience_personalizationprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_personalizationprofiles_created_at ON customer_experience_personalizationprofiles(created_at);

-- Operational seed data fixtures for customer_experience_personalizationprofiles
INSERT OR IGNORE INTO customer_experience_personalizationprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PER-0001", "Primary Operational PersonalizationProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-personalizationprofile-01"),
    (2, "PER-0002", "Secondary Corporate PersonalizationProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-personalizationprofile-02"),
    (3, "PER-0003", "Consolidated Branch PersonalizationProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-personalizationprofile-03"),
    (4, "PER-0004", "Enterprise Audited PersonalizationProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-personalizationprofile-04"),
    (5, "PER-0005", "Executive Strategic PersonalizationProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-personalizationprofile-05");

CREATE TABLE IF NOT EXISTS customer_experience_experiencegapincidents (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_experiencegapincidents_code ON customer_experience_experiencegapincidents(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_experiencegapincidents_org_status ON customer_experience_experiencegapincidents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_experiencegapincidents_priority ON customer_experience_experiencegapincidents(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_experiencegapincidents_created_at ON customer_experience_experiencegapincidents(created_at);

-- Operational seed data fixtures for customer_experience_experiencegapincidents
INSERT OR IGNORE INTO customer_experience_experiencegapincidents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExperienceGapIncident 1", 24500.00, 150.0, "ACTIVE", "uuid-experiencegapincident-01"),
    (2, "EXP-0002", "Secondary Corporate ExperienceGapIncident 2", 18200.50, 80.0, "ACTIVE", "uuid-experiencegapincident-02"),
    (3, "EXP-0003", "Consolidated Branch ExperienceGapIncident 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-experiencegapincident-03"),
    (4, "EXP-0004", "Enterprise Audited ExperienceGapIncident 4", 32800.00, 210.0, "ACTIVE", "uuid-experiencegapincident-04"),
    (5, "EXP-0005", "Executive Strategic ExperienceGapIncident 5", 65000.00, 400.0, "ACTIVE", "uuid-experiencegapincident-05");

CREATE TABLE IF NOT EXISTS customer_experience_advocatereferralrecords (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_advocatereferralrecords_code ON customer_experience_advocatereferralrecords(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_advocatereferralrecords_org_status ON customer_experience_advocatereferralrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_advocatereferralrecords_priority ON customer_experience_advocatereferralrecords(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_advocatereferralrecords_created_at ON customer_experience_advocatereferralrecords(created_at);

-- Operational seed data fixtures for customer_experience_advocatereferralrecords
INSERT OR IGNORE INTO customer_experience_advocatereferralrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ADV-0001", "Primary Operational AdvocateReferralRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-advocatereferralrecord-01"),
    (2, "ADV-0002", "Secondary Corporate AdvocateReferralRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-advocatereferralrecord-02"),
    (3, "ADV-0003", "Consolidated Branch AdvocateReferralRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-advocatereferralrecord-03"),
    (4, "ADV-0004", "Enterprise Audited AdvocateReferralRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-advocatereferralrecord-04"),
    (5, "ADV-0005", "Executive Strategic AdvocateReferralRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-advocatereferralrecord-05");

CREATE TABLE IF NOT EXISTS customer_experience_retentioncampaigntriggers (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_retentioncampaigntriggers_code ON customer_experience_retentioncampaigntriggers(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_retentioncampaigntriggers_org_status ON customer_experience_retentioncampaigntriggers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_retentioncampaigntriggers_priority ON customer_experience_retentioncampaigntriggers(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_retentioncampaigntriggers_created_at ON customer_experience_retentioncampaigntriggers(created_at);

-- Operational seed data fixtures for customer_experience_retentioncampaigntriggers
INSERT OR IGNORE INTO customer_experience_retentioncampaigntriggers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational RetentionCampaignTrigger 1", 24500.00, 150.0, "ACTIVE", "uuid-retentioncampaigntrigger-01"),
    (2, "RET-0002", "Secondary Corporate RetentionCampaignTrigger 2", 18200.50, 80.0, "ACTIVE", "uuid-retentioncampaigntrigger-02"),
    (3, "RET-0003", "Consolidated Branch RetentionCampaignTrigger 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-retentioncampaigntrigger-03"),
    (4, "RET-0004", "Enterprise Audited RetentionCampaignTrigger 4", 32800.00, 210.0, "ACTIVE", "uuid-retentioncampaigntrigger-04"),
    (5, "RET-0005", "Executive Strategic RetentionCampaignTrigger 5", 65000.00, 400.0, "ACTIVE", "uuid-retentioncampaigntrigger-05");

CREATE TABLE IF NOT EXISTS customer_experience_feedbackcategorizationrules (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_feedbackcategorizationrules_code ON customer_experience_feedbackcategorizationrules(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_feedbackcategorizationrules_org_status ON customer_experience_feedbackcategorizationrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_feedbackcategorizationrules_priority ON customer_experience_feedbackcategorizationrules(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_feedbackcategorizationrules_created_at ON customer_experience_feedbackcategorizationrules(created_at);

-- Operational seed data fixtures for customer_experience_feedbackcategorizationrules
INSERT OR IGNORE INTO customer_experience_feedbackcategorizationrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FEE-0001", "Primary Operational FeedbackCategorizationRule 1", 24500.00, 150.0, "ACTIVE", "uuid-feedbackcategorizationrule-01"),
    (2, "FEE-0002", "Secondary Corporate FeedbackCategorizationRule 2", 18200.50, 80.0, "ACTIVE", "uuid-feedbackcategorizationrule-02"),
    (3, "FEE-0003", "Consolidated Branch FeedbackCategorizationRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-feedbackcategorizationrule-03"),
    (4, "FEE-0004", "Enterprise Audited FeedbackCategorizationRule 4", 32800.00, 210.0, "ACTIVE", "uuid-feedbackcategorizationrule-04"),
    (5, "FEE-0005", "Executive Strategic FeedbackCategorizationRule 5", 65000.00, 400.0, "ACTIVE", "uuid-feedbackcategorizationrule-05");

CREATE TABLE IF NOT EXISTS customer_experience_customerdelightactions (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_customerdelightactions_code ON customer_experience_customerdelightactions(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerdelightactions_org_status ON customer_experience_customerdelightactions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerdelightactions_priority ON customer_experience_customerdelightactions(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_customerdelightactions_created_at ON customer_experience_customerdelightactions(created_at);

-- Operational seed data fixtures for customer_experience_customerdelightactions
INSERT OR IGNORE INTO customer_experience_customerdelightactions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerDelightAction 1", 24500.00, 150.0, "ACTIVE", "uuid-customerdelightaction-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerDelightAction 2", 18200.50, 80.0, "ACTIVE", "uuid-customerdelightaction-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerDelightAction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerdelightaction-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerDelightAction 4", 32800.00, 210.0, "ACTIVE", "uuid-customerdelightaction-04"),
    (5, "CUS-0005", "Executive Strategic CustomerDelightAction 5", 65000.00, 400.0, "ACTIVE", "uuid-customerdelightaction-05");

CREATE TABLE IF NOT EXISTS customer_experience_executivecxscorecards (
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

CREATE INDEX IF NOT EXISTS idx_customer_experience_executivecxscorecards_code ON customer_experience_executivecxscorecards(code);
CREATE INDEX IF NOT EXISTS idx_customer_experience_executivecxscorecards_org_status ON customer_experience_executivecxscorecards(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customer_experience_executivecxscorecards_priority ON customer_experience_executivecxscorecards(priority);
CREATE INDEX IF NOT EXISTS idx_customer_experience_executivecxscorecards_created_at ON customer_experience_executivecxscorecards(created_at);

-- Operational seed data fixtures for customer_experience_executivecxscorecards
INSERT OR IGNORE INTO customer_experience_executivecxscorecards (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXE-0001", "Primary Operational ExecutiveCXScorecard 1", 24500.00, 150.0, "ACTIVE", "uuid-executivecxscorecard-01"),
    (2, "EXE-0002", "Secondary Corporate ExecutiveCXScorecard 2", 18200.50, 80.0, "ACTIVE", "uuid-executivecxscorecard-02"),
    (3, "EXE-0003", "Consolidated Branch ExecutiveCXScorecard 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-executivecxscorecard-03"),
    (4, "EXE-0004", "Enterprise Audited ExecutiveCXScorecard 4", 32800.00, 210.0, "ACTIVE", "uuid-executivecxscorecard-04"),
    (5, "EXE-0005", "Executive Strategic ExecutiveCXScorecard 5", 65000.00, 400.0, "ACTIVE", "uuid-executivecxscorecard-05");

