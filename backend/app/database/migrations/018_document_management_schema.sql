-- SmartERP Enterprise Titan Migration 018: Enterprise Document & Records Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS document_management_documentfolders (
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

CREATE INDEX IF NOT EXISTS idx_document_management_documentfolders_code ON document_management_documentfolders(code);
CREATE INDEX IF NOT EXISTS idx_document_management_documentfolders_org_status ON document_management_documentfolders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_documentfolders_priority ON document_management_documentfolders(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_documentfolders_created_at ON document_management_documentfolders(created_at);

-- Operational seed data fixtures for document_management_documentfolders
INSERT OR IGNORE INTO document_management_documentfolders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentFolder 1", 24500.00, 150.0, "ACTIVE", "uuid-documentfolder-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentFolder 2", 18200.50, 80.0, "ACTIVE", "uuid-documentfolder-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentFolder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documentfolder-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentFolder 4", 32800.00, 210.0, "ACTIVE", "uuid-documentfolder-04"),
    (5, "DOC-0005", "Executive Strategic DocumentFolder 5", 65000.00, 400.0, "ACTIVE", "uuid-documentfolder-05");

CREATE TABLE IF NOT EXISTS document_management_documentfiles (
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

CREATE INDEX IF NOT EXISTS idx_document_management_documentfiles_code ON document_management_documentfiles(code);
CREATE INDEX IF NOT EXISTS idx_document_management_documentfiles_org_status ON document_management_documentfiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_documentfiles_priority ON document_management_documentfiles(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_documentfiles_created_at ON document_management_documentfiles(created_at);

-- Operational seed data fixtures for document_management_documentfiles
INSERT OR IGNORE INTO document_management_documentfiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentFile 1", 24500.00, 150.0, "ACTIVE", "uuid-documentfile-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentFile 2", 18200.50, 80.0, "ACTIVE", "uuid-documentfile-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentFile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documentfile-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentFile 4", 32800.00, 210.0, "ACTIVE", "uuid-documentfile-04"),
    (5, "DOC-0005", "Executive Strategic DocumentFile 5", 65000.00, 400.0, "ACTIVE", "uuid-documentfile-05");

CREATE TABLE IF NOT EXISTS document_management_documentversions (
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

CREATE INDEX IF NOT EXISTS idx_document_management_documentversions_code ON document_management_documentversions(code);
CREATE INDEX IF NOT EXISTS idx_document_management_documentversions_org_status ON document_management_documentversions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_documentversions_priority ON document_management_documentversions(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_documentversions_created_at ON document_management_documentversions(created_at);

-- Operational seed data fixtures for document_management_documentversions
INSERT OR IGNORE INTO document_management_documentversions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentVersion 1", 24500.00, 150.0, "ACTIVE", "uuid-documentversion-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentVersion 2", 18200.50, 80.0, "ACTIVE", "uuid-documentversion-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentVersion 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documentversion-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentVersion 4", 32800.00, 210.0, "ACTIVE", "uuid-documentversion-04"),
    (5, "DOC-0005", "Executive Strategic DocumentVersion 5", 65000.00, 400.0, "ACTIVE", "uuid-documentversion-05");

CREATE TABLE IF NOT EXISTS document_management_documentmetadataschemas (
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

CREATE INDEX IF NOT EXISTS idx_document_management_documentmetadataschemas_code ON document_management_documentmetadataschemas(code);
CREATE INDEX IF NOT EXISTS idx_document_management_documentmetadataschemas_org_status ON document_management_documentmetadataschemas(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_documentmetadataschemas_priority ON document_management_documentmetadataschemas(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_documentmetadataschemas_created_at ON document_management_documentmetadataschemas(created_at);

-- Operational seed data fixtures for document_management_documentmetadataschemas
INSERT OR IGNORE INTO document_management_documentmetadataschemas (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentMetadataSchema 1", 24500.00, 150.0, "ACTIVE", "uuid-documentmetadataschema-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentMetadataSchema 2", 18200.50, 80.0, "ACTIVE", "uuid-documentmetadataschema-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentMetadataSchema 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documentmetadataschema-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentMetadataSchema 4", 32800.00, 210.0, "ACTIVE", "uuid-documentmetadataschema-04"),
    (5, "DOC-0005", "Executive Strategic DocumentMetadataSchema 5", 65000.00, 400.0, "ACTIVE", "uuid-documentmetadataschema-05");

CREATE TABLE IF NOT EXISTS document_management_accesscontrolacls (
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

CREATE INDEX IF NOT EXISTS idx_document_management_accesscontrolacls_code ON document_management_accesscontrolacls(code);
CREATE INDEX IF NOT EXISTS idx_document_management_accesscontrolacls_org_status ON document_management_accesscontrolacls(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_accesscontrolacls_priority ON document_management_accesscontrolacls(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_accesscontrolacls_created_at ON document_management_accesscontrolacls(created_at);

-- Operational seed data fixtures for document_management_accesscontrolacls
INSERT OR IGNORE INTO document_management_accesscontrolacls (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ACC-0001", "Primary Operational AccessControlACL 1", 24500.00, 150.0, "ACTIVE", "uuid-accesscontrolacl-01"),
    (2, "ACC-0002", "Secondary Corporate AccessControlACL 2", 18200.50, 80.0, "ACTIVE", "uuid-accesscontrolacl-02"),
    (3, "ACC-0003", "Consolidated Branch AccessControlACL 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-accesscontrolacl-03"),
    (4, "ACC-0004", "Enterprise Audited AccessControlACL 4", 32800.00, 210.0, "ACTIVE", "uuid-accesscontrolacl-04"),
    (5, "ACC-0005", "Executive Strategic AccessControlACL 5", 65000.00, 400.0, "ACTIVE", "uuid-accesscontrolacl-05");

CREATE TABLE IF NOT EXISTS document_management_documenttagtaxonomys (
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

CREATE INDEX IF NOT EXISTS idx_document_management_documenttagtaxonomys_code ON document_management_documenttagtaxonomys(code);
CREATE INDEX IF NOT EXISTS idx_document_management_documenttagtaxonomys_org_status ON document_management_documenttagtaxonomys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_documenttagtaxonomys_priority ON document_management_documenttagtaxonomys(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_documenttagtaxonomys_created_at ON document_management_documenttagtaxonomys(created_at);

-- Operational seed data fixtures for document_management_documenttagtaxonomys
INSERT OR IGNORE INTO document_management_documenttagtaxonomys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentTagTaxonomy 1", 24500.00, 150.0, "ACTIVE", "uuid-documenttagtaxonomy-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentTagTaxonomy 2", 18200.50, 80.0, "ACTIVE", "uuid-documenttagtaxonomy-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentTagTaxonomy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documenttagtaxonomy-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentTagTaxonomy 4", 32800.00, 210.0, "ACTIVE", "uuid-documenttagtaxonomy-04"),
    (5, "DOC-0005", "Executive Strategic DocumentTagTaxonomy 5", 65000.00, 400.0, "ACTIVE", "uuid-documenttagtaxonomy-05");

CREATE TABLE IF NOT EXISTS document_management_ocrtextextractions (
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

CREATE INDEX IF NOT EXISTS idx_document_management_ocrtextextractions_code ON document_management_ocrtextextractions(code);
CREATE INDEX IF NOT EXISTS idx_document_management_ocrtextextractions_org_status ON document_management_ocrtextextractions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_ocrtextextractions_priority ON document_management_ocrtextextractions(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_ocrtextextractions_created_at ON document_management_ocrtextextractions(created_at);

-- Operational seed data fixtures for document_management_ocrtextextractions
INSERT OR IGNORE INTO document_management_ocrtextextractions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OCR-0001", "Primary Operational OCRTextExtraction 1", 24500.00, 150.0, "ACTIVE", "uuid-ocrtextextraction-01"),
    (2, "OCR-0002", "Secondary Corporate OCRTextExtraction 2", 18200.50, 80.0, "ACTIVE", "uuid-ocrtextextraction-02"),
    (3, "OCR-0003", "Consolidated Branch OCRTextExtraction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ocrtextextraction-03"),
    (4, "OCR-0004", "Enterprise Audited OCRTextExtraction 4", 32800.00, 210.0, "ACTIVE", "uuid-ocrtextextraction-04"),
    (5, "OCR-0005", "Executive Strategic OCRTextExtraction 5", 65000.00, 400.0, "ACTIVE", "uuid-ocrtextextraction-05");

CREATE TABLE IF NOT EXISTS document_management_documentsignaturerequests (
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

CREATE INDEX IF NOT EXISTS idx_document_management_documentsignaturerequests_code ON document_management_documentsignaturerequests(code);
CREATE INDEX IF NOT EXISTS idx_document_management_documentsignaturerequests_org_status ON document_management_documentsignaturerequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_documentsignaturerequests_priority ON document_management_documentsignaturerequests(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_documentsignaturerequests_created_at ON document_management_documentsignaturerequests(created_at);

-- Operational seed data fixtures for document_management_documentsignaturerequests
INSERT OR IGNORE INTO document_management_documentsignaturerequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentSignatureRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-documentsignaturerequest-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentSignatureRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-documentsignaturerequest-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentSignatureRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documentsignaturerequest-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentSignatureRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-documentsignaturerequest-04"),
    (5, "DOC-0005", "Executive Strategic DocumentSignatureRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-documentsignaturerequest-05");

CREATE TABLE IF NOT EXISTS document_management_auditlogdocuments (
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

CREATE INDEX IF NOT EXISTS idx_document_management_auditlogdocuments_code ON document_management_auditlogdocuments(code);
CREATE INDEX IF NOT EXISTS idx_document_management_auditlogdocuments_org_status ON document_management_auditlogdocuments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_auditlogdocuments_priority ON document_management_auditlogdocuments(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_auditlogdocuments_created_at ON document_management_auditlogdocuments(created_at);

-- Operational seed data fixtures for document_management_auditlogdocuments
INSERT OR IGNORE INTO document_management_auditlogdocuments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "AUD-0001", "Primary Operational AuditLogDocument 1", 24500.00, 150.0, "ACTIVE", "uuid-auditlogdocument-01"),
    (2, "AUD-0002", "Secondary Corporate AuditLogDocument 2", 18200.50, 80.0, "ACTIVE", "uuid-auditlogdocument-02"),
    (3, "AUD-0003", "Consolidated Branch AuditLogDocument 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-auditlogdocument-03"),
    (4, "AUD-0004", "Enterprise Audited AuditLogDocument 4", 32800.00, 210.0, "ACTIVE", "uuid-auditlogdocument-04"),
    (5, "AUD-0005", "Executive Strategic AuditLogDocument 5", 65000.00, 400.0, "ACTIVE", "uuid-auditlogdocument-05");

CREATE TABLE IF NOT EXISTS document_management_retentionschedulepolicys (
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

CREATE INDEX IF NOT EXISTS idx_document_management_retentionschedulepolicys_code ON document_management_retentionschedulepolicys(code);
CREATE INDEX IF NOT EXISTS idx_document_management_retentionschedulepolicys_org_status ON document_management_retentionschedulepolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_retentionschedulepolicys_priority ON document_management_retentionschedulepolicys(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_retentionschedulepolicys_created_at ON document_management_retentionschedulepolicys(created_at);

-- Operational seed data fixtures for document_management_retentionschedulepolicys
INSERT OR IGNORE INTO document_management_retentionschedulepolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational RetentionSchedulePolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-retentionschedulepolicy-01"),
    (2, "RET-0002", "Secondary Corporate RetentionSchedulePolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-retentionschedulepolicy-02"),
    (3, "RET-0003", "Consolidated Branch RetentionSchedulePolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-retentionschedulepolicy-03"),
    (4, "RET-0004", "Enterprise Audited RetentionSchedulePolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-retentionschedulepolicy-04"),
    (5, "RET-0005", "Executive Strategic RetentionSchedulePolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-retentionschedulepolicy-05");

CREATE TABLE IF NOT EXISTS document_management_legalholdnotices (
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

CREATE INDEX IF NOT EXISTS idx_document_management_legalholdnotices_code ON document_management_legalholdnotices(code);
CREATE INDEX IF NOT EXISTS idx_document_management_legalholdnotices_org_status ON document_management_legalholdnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_legalholdnotices_priority ON document_management_legalholdnotices(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_legalholdnotices_created_at ON document_management_legalholdnotices(created_at);

-- Operational seed data fixtures for document_management_legalholdnotices
INSERT OR IGNORE INTO document_management_legalholdnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LEG-0001", "Primary Operational LegalHoldNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-legalholdnotice-01"),
    (2, "LEG-0002", "Secondary Corporate LegalHoldNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-legalholdnotice-02"),
    (3, "LEG-0003", "Consolidated Branch LegalHoldNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-legalholdnotice-03"),
    (4, "LEG-0004", "Enterprise Audited LegalHoldNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-legalholdnotice-04"),
    (5, "LEG-0005", "Executive Strategic LegalHoldNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-legalholdnotice-05");

CREATE TABLE IF NOT EXISTS document_management_archivalvaults (
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

CREATE INDEX IF NOT EXISTS idx_document_management_archivalvaults_code ON document_management_archivalvaults(code);
CREATE INDEX IF NOT EXISTS idx_document_management_archivalvaults_org_status ON document_management_archivalvaults(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_archivalvaults_priority ON document_management_archivalvaults(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_archivalvaults_created_at ON document_management_archivalvaults(created_at);

-- Operational seed data fixtures for document_management_archivalvaults
INSERT OR IGNORE INTO document_management_archivalvaults (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ARC-0001", "Primary Operational ArchivalVault 1", 24500.00, 150.0, "ACTIVE", "uuid-archivalvault-01"),
    (2, "ARC-0002", "Secondary Corporate ArchivalVault 2", 18200.50, 80.0, "ACTIVE", "uuid-archivalvault-02"),
    (3, "ARC-0003", "Consolidated Branch ArchivalVault 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-archivalvault-03"),
    (4, "ARC-0004", "Enterprise Audited ArchivalVault 4", 32800.00, 210.0, "ACTIVE", "uuid-archivalvault-04"),
    (5, "ARC-0005", "Executive Strategic ArchivalVault 5", 65000.00, 400.0, "ACTIVE", "uuid-archivalvault-05");

CREATE TABLE IF NOT EXISTS document_management_documentsharelinks (
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

CREATE INDEX IF NOT EXISTS idx_document_management_documentsharelinks_code ON document_management_documentsharelinks(code);
CREATE INDEX IF NOT EXISTS idx_document_management_documentsharelinks_org_status ON document_management_documentsharelinks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_documentsharelinks_priority ON document_management_documentsharelinks(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_documentsharelinks_created_at ON document_management_documentsharelinks(created_at);

-- Operational seed data fixtures for document_management_documentsharelinks
INSERT OR IGNORE INTO document_management_documentsharelinks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DOC-0001", "Primary Operational DocumentShareLink 1", 24500.00, 150.0, "ACTIVE", "uuid-documentsharelink-01"),
    (2, "DOC-0002", "Secondary Corporate DocumentShareLink 2", 18200.50, 80.0, "ACTIVE", "uuid-documentsharelink-02"),
    (3, "DOC-0003", "Consolidated Branch DocumentShareLink 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-documentsharelink-03"),
    (4, "DOC-0004", "Enterprise Audited DocumentShareLink 4", 32800.00, 210.0, "ACTIVE", "uuid-documentsharelink-04"),
    (5, "DOC-0005", "Executive Strategic DocumentShareLink 5", 65000.00, 400.0, "ACTIVE", "uuid-documentsharelink-05");

CREATE TABLE IF NOT EXISTS document_management_watermarktemplates (
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

CREATE INDEX IF NOT EXISTS idx_document_management_watermarktemplates_code ON document_management_watermarktemplates(code);
CREATE INDEX IF NOT EXISTS idx_document_management_watermarktemplates_org_status ON document_management_watermarktemplates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_watermarktemplates_priority ON document_management_watermarktemplates(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_watermarktemplates_created_at ON document_management_watermarktemplates(created_at);

-- Operational seed data fixtures for document_management_watermarktemplates
INSERT OR IGNORE INTO document_management_watermarktemplates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAT-0001", "Primary Operational WatermarkTemplate 1", 24500.00, 150.0, "ACTIVE", "uuid-watermarktemplate-01"),
    (2, "WAT-0002", "Secondary Corporate WatermarkTemplate 2", 18200.50, 80.0, "ACTIVE", "uuid-watermarktemplate-02"),
    (3, "WAT-0003", "Consolidated Branch WatermarkTemplate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-watermarktemplate-03"),
    (4, "WAT-0004", "Enterprise Audited WatermarkTemplate 4", 32800.00, 210.0, "ACTIVE", "uuid-watermarktemplate-04"),
    (5, "WAT-0005", "Executive Strategic WatermarkTemplate 5", 65000.00, 400.0, "ACTIVE", "uuid-watermarktemplate-05");

CREATE TABLE IF NOT EXISTS document_management_approvalsignoffflows (
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

CREATE INDEX IF NOT EXISTS idx_document_management_approvalsignoffflows_code ON document_management_approvalsignoffflows(code);
CREATE INDEX IF NOT EXISTS idx_document_management_approvalsignoffflows_org_status ON document_management_approvalsignoffflows(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_approvalsignoffflows_priority ON document_management_approvalsignoffflows(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_approvalsignoffflows_created_at ON document_management_approvalsignoffflows(created_at);

-- Operational seed data fixtures for document_management_approvalsignoffflows
INSERT OR IGNORE INTO document_management_approvalsignoffflows (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "APP-0001", "Primary Operational ApprovalSignoffFlow 1", 24500.00, 150.0, "ACTIVE", "uuid-approvalsignoffflow-01"),
    (2, "APP-0002", "Secondary Corporate ApprovalSignoffFlow 2", 18200.50, 80.0, "ACTIVE", "uuid-approvalsignoffflow-02"),
    (3, "APP-0003", "Consolidated Branch ApprovalSignoffFlow 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-approvalsignoffflow-03"),
    (4, "APP-0004", "Enterprise Audited ApprovalSignoffFlow 4", 32800.00, 210.0, "ACTIVE", "uuid-approvalsignoffflow-04"),
    (5, "APP-0005", "Executive Strategic ApprovalSignoffFlow 5", 65000.00, 400.0, "ACTIVE", "uuid-approvalsignoffflow-05");

CREATE TABLE IF NOT EXISTS document_management_batchscanningjobs (
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

CREATE INDEX IF NOT EXISTS idx_document_management_batchscanningjobs_code ON document_management_batchscanningjobs(code);
CREATE INDEX IF NOT EXISTS idx_document_management_batchscanningjobs_org_status ON document_management_batchscanningjobs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_document_management_batchscanningjobs_priority ON document_management_batchscanningjobs(priority);
CREATE INDEX IF NOT EXISTS idx_document_management_batchscanningjobs_created_at ON document_management_batchscanningjobs(created_at);

-- Operational seed data fixtures for document_management_batchscanningjobs
INSERT OR IGNORE INTO document_management_batchscanningjobs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BAT-0001", "Primary Operational BatchScanningJob 1", 24500.00, 150.0, "ACTIVE", "uuid-batchscanningjob-01"),
    (2, "BAT-0002", "Secondary Corporate BatchScanningJob 2", 18200.50, 80.0, "ACTIVE", "uuid-batchscanningjob-02"),
    (3, "BAT-0003", "Consolidated Branch BatchScanningJob 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-batchscanningjob-03"),
    (4, "BAT-0004", "Enterprise Audited BatchScanningJob 4", 32800.00, 210.0, "ACTIVE", "uuid-batchscanningjob-04"),
    (5, "BAT-0005", "Executive Strategic BatchScanningJob 5", 65000.00, 400.0, "ACTIVE", "uuid-batchscanningjob-05");

