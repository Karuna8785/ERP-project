-- SmartERP Enterprise Titan Migration 043: Enterprise Knowledge Base & Standard Operations DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS knowledge_base_knowledgebasearticles (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgebasearticles_code ON knowledge_base_knowledgebasearticles(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgebasearticles_org_status ON knowledge_base_knowledgebasearticles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgebasearticles_priority ON knowledge_base_knowledgebasearticles(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgebasearticles_created_at ON knowledge_base_knowledgebasearticles(created_at);

-- Operational seed data fixtures for knowledge_base_knowledgebasearticles
INSERT OR IGNORE INTO knowledge_base_knowledgebasearticles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "KNO-0001", "Primary Operational KnowledgeBaseArticle 1", 24500.00, 150.0, "ACTIVE", "uuid-knowledgebasearticle-01"),
    (2, "KNO-0002", "Secondary Corporate KnowledgeBaseArticle 2", 18200.50, 80.0, "ACTIVE", "uuid-knowledgebasearticle-02"),
    (3, "KNO-0003", "Consolidated Branch KnowledgeBaseArticle 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-knowledgebasearticle-03"),
    (4, "KNO-0004", "Enterprise Audited KnowledgeBaseArticle 4", 32800.00, 210.0, "ACTIVE", "uuid-knowledgebasearticle-04"),
    (5, "KNO-0005", "Executive Strategic KnowledgeBaseArticle 5", 65000.00, 400.0, "ACTIVE", "uuid-knowledgebasearticle-05");

CREATE TABLE IF NOT EXISTS knowledge_base_standardoperatingprocedures (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_standardoperatingprocedures_code ON knowledge_base_standardoperatingprocedures(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_standardoperatingprocedures_org_status ON knowledge_base_standardoperatingprocedures(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_standardoperatingprocedures_priority ON knowledge_base_standardoperatingprocedures(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_standardoperatingprocedures_created_at ON knowledge_base_standardoperatingprocedures(created_at);

-- Operational seed data fixtures for knowledge_base_standardoperatingprocedures
INSERT OR IGNORE INTO knowledge_base_standardoperatingprocedures (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StandardOperatingProcedure 1", 24500.00, 150.0, "ACTIVE", "uuid-standardoperatingprocedure-01"),
    (2, "STA-0002", "Secondary Corporate StandardOperatingProcedure 2", 18200.50, 80.0, "ACTIVE", "uuid-standardoperatingprocedure-02"),
    (3, "STA-0003", "Consolidated Branch StandardOperatingProcedure 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-standardoperatingprocedure-03"),
    (4, "STA-0004", "Enterprise Audited StandardOperatingProcedure 4", 32800.00, 210.0, "ACTIVE", "uuid-standardoperatingprocedure-04"),
    (5, "STA-0005", "Executive Strategic StandardOperatingProcedure 5", 65000.00, 400.0, "ACTIVE", "uuid-standardoperatingprocedure-05");

CREATE TABLE IF NOT EXISTS knowledge_base_knowledgecategorytopics (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgecategorytopics_code ON knowledge_base_knowledgecategorytopics(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgecategorytopics_org_status ON knowledge_base_knowledgecategorytopics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgecategorytopics_priority ON knowledge_base_knowledgecategorytopics(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgecategorytopics_created_at ON knowledge_base_knowledgecategorytopics(created_at);

-- Operational seed data fixtures for knowledge_base_knowledgecategorytopics
INSERT OR IGNORE INTO knowledge_base_knowledgecategorytopics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "KNO-0001", "Primary Operational KnowledgeCategoryTopic 1", 24500.00, 150.0, "ACTIVE", "uuid-knowledgecategorytopic-01"),
    (2, "KNO-0002", "Secondary Corporate KnowledgeCategoryTopic 2", 18200.50, 80.0, "ACTIVE", "uuid-knowledgecategorytopic-02"),
    (3, "KNO-0003", "Consolidated Branch KnowledgeCategoryTopic 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-knowledgecategorytopic-03"),
    (4, "KNO-0004", "Enterprise Audited KnowledgeCategoryTopic 4", 32800.00, 210.0, "ACTIVE", "uuid-knowledgecategorytopic-04"),
    (5, "KNO-0005", "Executive Strategic KnowledgeCategoryTopic 5", 65000.00, 400.0, "ACTIVE", "uuid-knowledgecategorytopic-05");

CREATE TABLE IF NOT EXISTS knowledge_base_contentreviewworkflows (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_contentreviewworkflows_code ON knowledge_base_contentreviewworkflows(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_contentreviewworkflows_org_status ON knowledge_base_contentreviewworkflows(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_contentreviewworkflows_priority ON knowledge_base_contentreviewworkflows(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_contentreviewworkflows_created_at ON knowledge_base_contentreviewworkflows(created_at);

-- Operational seed data fixtures for knowledge_base_contentreviewworkflows
INSERT OR IGNORE INTO knowledge_base_contentreviewworkflows (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CON-0001", "Primary Operational ContentReviewWorkflow 1", 24500.00, 150.0, "ACTIVE", "uuid-contentreviewworkflow-01"),
    (2, "CON-0002", "Secondary Corporate ContentReviewWorkflow 2", 18200.50, 80.0, "ACTIVE", "uuid-contentreviewworkflow-02"),
    (3, "CON-0003", "Consolidated Branch ContentReviewWorkflow 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-contentreviewworkflow-03"),
    (4, "CON-0004", "Enterprise Audited ContentReviewWorkflow 4", 32800.00, 210.0, "ACTIVE", "uuid-contentreviewworkflow-04"),
    (5, "CON-0005", "Executive Strategic ContentReviewWorkflow 5", 65000.00, 400.0, "ACTIVE", "uuid-contentreviewworkflow-05");

CREATE TABLE IF NOT EXISTS knowledge_base_articlefeedbackvotes (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_articlefeedbackvotes_code ON knowledge_base_articlefeedbackvotes(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_articlefeedbackvotes_org_status ON knowledge_base_articlefeedbackvotes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_articlefeedbackvotes_priority ON knowledge_base_articlefeedbackvotes(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_articlefeedbackvotes_created_at ON knowledge_base_articlefeedbackvotes(created_at);

-- Operational seed data fixtures for knowledge_base_articlefeedbackvotes
INSERT OR IGNORE INTO knowledge_base_articlefeedbackvotes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ART-0001", "Primary Operational ArticleFeedbackVote 1", 24500.00, 150.0, "ACTIVE", "uuid-articlefeedbackvote-01"),
    (2, "ART-0002", "Secondary Corporate ArticleFeedbackVote 2", 18200.50, 80.0, "ACTIVE", "uuid-articlefeedbackvote-02"),
    (3, "ART-0003", "Consolidated Branch ArticleFeedbackVote 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-articlefeedbackvote-03"),
    (4, "ART-0004", "Enterprise Audited ArticleFeedbackVote 4", 32800.00, 210.0, "ACTIVE", "uuid-articlefeedbackvote-04"),
    (5, "ART-0005", "Executive Strategic ArticleFeedbackVote 5", 65000.00, 400.0, "ACTIVE", "uuid-articlefeedbackvote-05");

CREATE TABLE IF NOT EXISTS knowledge_base_searchqueryanalyticss (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_searchqueryanalyticss_code ON knowledge_base_searchqueryanalyticss(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_searchqueryanalyticss_org_status ON knowledge_base_searchqueryanalyticss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_searchqueryanalyticss_priority ON knowledge_base_searchqueryanalyticss(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_searchqueryanalyticss_created_at ON knowledge_base_searchqueryanalyticss(created_at);

-- Operational seed data fixtures for knowledge_base_searchqueryanalyticss
INSERT OR IGNORE INTO knowledge_base_searchqueryanalyticss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SEA-0001", "Primary Operational SearchQueryAnalytics 1", 24500.00, 150.0, "ACTIVE", "uuid-searchqueryanalytics-01"),
    (2, "SEA-0002", "Secondary Corporate SearchQueryAnalytics 2", 18200.50, 80.0, "ACTIVE", "uuid-searchqueryanalytics-02"),
    (3, "SEA-0003", "Consolidated Branch SearchQueryAnalytics 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-searchqueryanalytics-03"),
    (4, "SEA-0004", "Enterprise Audited SearchQueryAnalytics 4", 32800.00, 210.0, "ACTIVE", "uuid-searchqueryanalytics-04"),
    (5, "SEA-0005", "Executive Strategic SearchQueryAnalytics 5", 65000.00, 400.0, "ACTIVE", "uuid-searchqueryanalytics-05");

CREATE TABLE IF NOT EXISTS knowledge_base_technicalfaqitems (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_technicalfaqitems_code ON knowledge_base_technicalfaqitems(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_technicalfaqitems_org_status ON knowledge_base_technicalfaqitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_technicalfaqitems_priority ON knowledge_base_technicalfaqitems(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_technicalfaqitems_created_at ON knowledge_base_technicalfaqitems(created_at);

-- Operational seed data fixtures for knowledge_base_technicalfaqitems
INSERT OR IGNORE INTO knowledge_base_technicalfaqitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEC-0001", "Primary Operational TechnicalFaqItem 1", 24500.00, 150.0, "ACTIVE", "uuid-technicalfaqitem-01"),
    (2, "TEC-0002", "Secondary Corporate TechnicalFaqItem 2", 18200.50, 80.0, "ACTIVE", "uuid-technicalfaqitem-02"),
    (3, "TEC-0003", "Consolidated Branch TechnicalFaqItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-technicalfaqitem-03"),
    (4, "TEC-0004", "Enterprise Audited TechnicalFaqItem 4", 32800.00, 210.0, "ACTIVE", "uuid-technicalfaqitem-04"),
    (5, "TEC-0005", "Executive Strategic TechnicalFaqItem 5", 65000.00, 400.0, "ACTIVE", "uuid-technicalfaqitem-05");

CREATE TABLE IF NOT EXISTS knowledge_base_troubleshootingguides (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_troubleshootingguides_code ON knowledge_base_troubleshootingguides(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_troubleshootingguides_org_status ON knowledge_base_troubleshootingguides(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_troubleshootingguides_priority ON knowledge_base_troubleshootingguides(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_troubleshootingguides_created_at ON knowledge_base_troubleshootingguides(created_at);

-- Operational seed data fixtures for knowledge_base_troubleshootingguides
INSERT OR IGNORE INTO knowledge_base_troubleshootingguides (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRO-0001", "Primary Operational TroubleshootingGuide 1", 24500.00, 150.0, "ACTIVE", "uuid-troubleshootingguide-01"),
    (2, "TRO-0002", "Secondary Corporate TroubleshootingGuide 2", 18200.50, 80.0, "ACTIVE", "uuid-troubleshootingguide-02"),
    (3, "TRO-0003", "Consolidated Branch TroubleshootingGuide 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-troubleshootingguide-03"),
    (4, "TRO-0004", "Enterprise Audited TroubleshootingGuide 4", 32800.00, 210.0, "ACTIVE", "uuid-troubleshootingguide-04"),
    (5, "TRO-0005", "Executive Strategic TroubleshootingGuide 5", 65000.00, 400.0, "ACTIVE", "uuid-troubleshootingguide-05");

CREATE TABLE IF NOT EXISTS knowledge_base_translationlocalizations (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_translationlocalizations_code ON knowledge_base_translationlocalizations(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_translationlocalizations_org_status ON knowledge_base_translationlocalizations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_translationlocalizations_priority ON knowledge_base_translationlocalizations(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_translationlocalizations_created_at ON knowledge_base_translationlocalizations(created_at);

-- Operational seed data fixtures for knowledge_base_translationlocalizations
INSERT OR IGNORE INTO knowledge_base_translationlocalizations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TranslationLocalization 1", 24500.00, 150.0, "ACTIVE", "uuid-translationlocalization-01"),
    (2, "TRA-0002", "Secondary Corporate TranslationLocalization 2", 18200.50, 80.0, "ACTIVE", "uuid-translationlocalization-02"),
    (3, "TRA-0003", "Consolidated Branch TranslationLocalization 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-translationlocalization-03"),
    (4, "TRA-0004", "Enterprise Audited TranslationLocalization 4", 32800.00, 210.0, "ACTIVE", "uuid-translationlocalization-04"),
    (5, "TRA-0005", "Executive Strategic TranslationLocalization 5", 65000.00, 400.0, "ACTIVE", "uuid-translationlocalization-05");

CREATE TABLE IF NOT EXISTS knowledge_base_articleattachmentfiles (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_articleattachmentfiles_code ON knowledge_base_articleattachmentfiles(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_articleattachmentfiles_org_status ON knowledge_base_articleattachmentfiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_articleattachmentfiles_priority ON knowledge_base_articleattachmentfiles(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_articleattachmentfiles_created_at ON knowledge_base_articleattachmentfiles(created_at);

-- Operational seed data fixtures for knowledge_base_articleattachmentfiles
INSERT OR IGNORE INTO knowledge_base_articleattachmentfiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ART-0001", "Primary Operational ArticleAttachmentFile 1", 24500.00, 150.0, "ACTIVE", "uuid-articleattachmentfile-01"),
    (2, "ART-0002", "Secondary Corporate ArticleAttachmentFile 2", 18200.50, 80.0, "ACTIVE", "uuid-articleattachmentfile-02"),
    (3, "ART-0003", "Consolidated Branch ArticleAttachmentFile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-articleattachmentfile-03"),
    (4, "ART-0004", "Enterprise Audited ArticleAttachmentFile 4", 32800.00, 210.0, "ACTIVE", "uuid-articleattachmentfile-04"),
    (5, "ART-0005", "Executive Strategic ArticleAttachmentFile 5", 65000.00, 400.0, "ACTIVE", "uuid-articleattachmentfile-05");

CREATE TABLE IF NOT EXISTS knowledge_base_internalwikipages (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_internalwikipages_code ON knowledge_base_internalwikipages(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_internalwikipages_org_status ON knowledge_base_internalwikipages(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_internalwikipages_priority ON knowledge_base_internalwikipages(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_internalwikipages_created_at ON knowledge_base_internalwikipages(created_at);

-- Operational seed data fixtures for knowledge_base_internalwikipages
INSERT OR IGNORE INTO knowledge_base_internalwikipages (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INT-0001", "Primary Operational InternalWikiPage 1", 24500.00, 150.0, "ACTIVE", "uuid-internalwikipage-01"),
    (2, "INT-0002", "Secondary Corporate InternalWikiPage 2", 18200.50, 80.0, "ACTIVE", "uuid-internalwikipage-02"),
    (3, "INT-0003", "Consolidated Branch InternalWikiPage 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-internalwikipage-03"),
    (4, "INT-0004", "Enterprise Audited InternalWikiPage 4", 32800.00, 210.0, "ACTIVE", "uuid-internalwikipage-04"),
    (5, "INT-0005", "Executive Strategic InternalWikiPage 5", 65000.00, 400.0, "ACTIVE", "uuid-internalwikipage-05");

CREATE TABLE IF NOT EXISTS knowledge_base_knowledgegraphnodes (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgegraphnodes_code ON knowledge_base_knowledgegraphnodes(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgegraphnodes_org_status ON knowledge_base_knowledgegraphnodes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgegraphnodes_priority ON knowledge_base_knowledgegraphnodes(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_knowledgegraphnodes_created_at ON knowledge_base_knowledgegraphnodes(created_at);

-- Operational seed data fixtures for knowledge_base_knowledgegraphnodes
INSERT OR IGNORE INTO knowledge_base_knowledgegraphnodes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "KNO-0001", "Primary Operational KnowledgeGraphNode 1", 24500.00, 150.0, "ACTIVE", "uuid-knowledgegraphnode-01"),
    (2, "KNO-0002", "Secondary Corporate KnowledgeGraphNode 2", 18200.50, 80.0, "ACTIVE", "uuid-knowledgegraphnode-02"),
    (3, "KNO-0003", "Consolidated Branch KnowledgeGraphNode 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-knowledgegraphnode-03"),
    (4, "KNO-0004", "Enterprise Audited KnowledgeGraphNode 4", 32800.00, 210.0, "ACTIVE", "uuid-knowledgegraphnode-04"),
    (5, "KNO-0005", "Executive Strategic KnowledgeGraphNode 5", 65000.00, 400.0, "ACTIVE", "uuid-knowledgegraphnode-05");

CREATE TABLE IF NOT EXISTS knowledge_base_revisionhistorylogs (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_revisionhistorylogs_code ON knowledge_base_revisionhistorylogs(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_revisionhistorylogs_org_status ON knowledge_base_revisionhistorylogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_revisionhistorylogs_priority ON knowledge_base_revisionhistorylogs(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_revisionhistorylogs_created_at ON knowledge_base_revisionhistorylogs(created_at);

-- Operational seed data fixtures for knowledge_base_revisionhistorylogs
INSERT OR IGNORE INTO knowledge_base_revisionhistorylogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REV-0001", "Primary Operational RevisionHistoryLog 1", 24500.00, 150.0, "ACTIVE", "uuid-revisionhistorylog-01"),
    (2, "REV-0002", "Secondary Corporate RevisionHistoryLog 2", 18200.50, 80.0, "ACTIVE", "uuid-revisionhistorylog-02"),
    (3, "REV-0003", "Consolidated Branch RevisionHistoryLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-revisionhistorylog-03"),
    (4, "REV-0004", "Enterprise Audited RevisionHistoryLog 4", 32800.00, 210.0, "ACTIVE", "uuid-revisionhistorylog-04"),
    (5, "REV-0005", "Executive Strategic RevisionHistoryLog 5", 65000.00, 400.0, "ACTIVE", "uuid-revisionhistorylog-05");

CREATE TABLE IF NOT EXISTS knowledge_base_expertauthordirectorys (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_expertauthordirectorys_code ON knowledge_base_expertauthordirectorys(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_expertauthordirectorys_org_status ON knowledge_base_expertauthordirectorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_expertauthordirectorys_priority ON knowledge_base_expertauthordirectorys(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_expertauthordirectorys_created_at ON knowledge_base_expertauthordirectorys(created_at);

-- Operational seed data fixtures for knowledge_base_expertauthordirectorys
INSERT OR IGNORE INTO knowledge_base_expertauthordirectorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExpertAuthorDirectory 1", 24500.00, 150.0, "ACTIVE", "uuid-expertauthordirectory-01"),
    (2, "EXP-0002", "Secondary Corporate ExpertAuthorDirectory 2", 18200.50, 80.0, "ACTIVE", "uuid-expertauthordirectory-02"),
    (3, "EXP-0003", "Consolidated Branch ExpertAuthorDirectory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-expertauthordirectory-03"),
    (4, "EXP-0004", "Enterprise Audited ExpertAuthorDirectory 4", 32800.00, 210.0, "ACTIVE", "uuid-expertauthordirectory-04"),
    (5, "EXP-0005", "Executive Strategic ExpertAuthorDirectory 5", 65000.00, 400.0, "ACTIVE", "uuid-expertauthordirectory-05");

CREATE TABLE IF NOT EXISTS knowledge_base_deprecatednotices (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_deprecatednotices_code ON knowledge_base_deprecatednotices(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_deprecatednotices_org_status ON knowledge_base_deprecatednotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_deprecatednotices_priority ON knowledge_base_deprecatednotices(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_deprecatednotices_created_at ON knowledge_base_deprecatednotices(created_at);

-- Operational seed data fixtures for knowledge_base_deprecatednotices
INSERT OR IGNORE INTO knowledge_base_deprecatednotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DeprecatedNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-deprecatednotice-01"),
    (2, "DEP-0002", "Secondary Corporate DeprecatedNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-deprecatednotice-02"),
    (3, "DEP-0003", "Consolidated Branch DeprecatedNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-deprecatednotice-03"),
    (4, "DEP-0004", "Enterprise Audited DeprecatedNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-deprecatednotice-04"),
    (5, "DEP-0005", "Executive Strategic DeprecatedNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-deprecatednotice-05");

CREATE TABLE IF NOT EXISTS knowledge_base_accessvisibilitytiers (
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

CREATE INDEX IF NOT EXISTS idx_knowledge_base_accessvisibilitytiers_code ON knowledge_base_accessvisibilitytiers(code);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_accessvisibilitytiers_org_status ON knowledge_base_accessvisibilitytiers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_accessvisibilitytiers_priority ON knowledge_base_accessvisibilitytiers(priority);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_accessvisibilitytiers_created_at ON knowledge_base_accessvisibilitytiers(created_at);

-- Operational seed data fixtures for knowledge_base_accessvisibilitytiers
INSERT OR IGNORE INTO knowledge_base_accessvisibilitytiers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACC-0001", "Primary Operational AccessVisibilityTier 1", 24500.00, 150.0, "ACTIVE", "uuid-accessvisibilitytier-01"),
    (2, "ACC-0002", "Secondary Corporate AccessVisibilityTier 2", 18200.50, 80.0, "ACTIVE", "uuid-accessvisibilitytier-02"),
    (3, "ACC-0003", "Consolidated Branch AccessVisibilityTier 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-accessvisibilitytier-03"),
    (4, "ACC-0004", "Enterprise Audited AccessVisibilityTier 4", 32800.00, 210.0, "ACTIVE", "uuid-accessvisibilitytier-04"),
    (5, "ACC-0005", "Executive Strategic AccessVisibilityTier 5", 65000.00, 400.0, "ACTIVE", "uuid-accessvisibilitytier-05");

