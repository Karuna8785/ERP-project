-- SmartERP Enterprise Titan Migration 036: Reverse Logistics & Customer Returns (RMA) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS returns_rma_returnmerchandiseauths (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_returnmerchandiseauths_code ON returns_rma_returnmerchandiseauths(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnmerchandiseauths_org_status ON returns_rma_returnmerchandiseauths(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnmerchandiseauths_priority ON returns_rma_returnmerchandiseauths(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnmerchandiseauths_created_at ON returns_rma_returnmerchandiseauths(created_at);

-- Operational seed data fixtures for returns_rma_returnmerchandiseauths
INSERT OR IGNORE INTO returns_rma_returnmerchandiseauths (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational ReturnMerchandiseAuth 1", 24500.00, 150.0, "ACTIVE", "uuid-returnmerchandiseauth-01"),
    (2, "RET-0002", "Secondary Corporate ReturnMerchandiseAuth 2", 18200.50, 80.0, "ACTIVE", "uuid-returnmerchandiseauth-02"),
    (3, "RET-0003", "Consolidated Branch ReturnMerchandiseAuth 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-returnmerchandiseauth-03"),
    (4, "RET-0004", "Enterprise Audited ReturnMerchandiseAuth 4", 32800.00, 210.0, "ACTIVE", "uuid-returnmerchandiseauth-04"),
    (5, "RET-0005", "Executive Strategic ReturnMerchandiseAuth 5", 65000.00, 400.0, "ACTIVE", "uuid-returnmerchandiseauth-05");

CREATE TABLE IF NOT EXISTS returns_rma_receivinginspectionqas (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_receivinginspectionqas_code ON returns_rma_receivinginspectionqas(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_receivinginspectionqas_org_status ON returns_rma_receivinginspectionqas(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_receivinginspectionqas_priority ON returns_rma_receivinginspectionqas(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_receivinginspectionqas_created_at ON returns_rma_receivinginspectionqas(created_at);

-- Operational seed data fixtures for returns_rma_receivinginspectionqas
INSERT OR IGNORE INTO returns_rma_receivinginspectionqas (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REC-0001", "Primary Operational ReceivingInspectionQA 1", 24500.00, 150.0, "ACTIVE", "uuid-receivinginspectionqa-01"),
    (2, "REC-0002", "Secondary Corporate ReceivingInspectionQA 2", 18200.50, 80.0, "ACTIVE", "uuid-receivinginspectionqa-02"),
    (3, "REC-0003", "Consolidated Branch ReceivingInspectionQA 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-receivinginspectionqa-03"),
    (4, "REC-0004", "Enterprise Audited ReceivingInspectionQA 4", 32800.00, 210.0, "ACTIVE", "uuid-receivinginspectionqa-04"),
    (5, "REC-0005", "Executive Strategic ReceivingInspectionQA 5", 65000.00, 400.0, "ACTIVE", "uuid-receivinginspectionqa-05");

CREATE TABLE IF NOT EXISTS returns_rma_restockingfeerules (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_restockingfeerules_code ON returns_rma_restockingfeerules(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_restockingfeerules_org_status ON returns_rma_restockingfeerules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_restockingfeerules_priority ON returns_rma_restockingfeerules(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_restockingfeerules_created_at ON returns_rma_restockingfeerules(created_at);

-- Operational seed data fixtures for returns_rma_restockingfeerules
INSERT OR IGNORE INTO returns_rma_restockingfeerules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RES-0001", "Primary Operational RestockingFeeRule 1", 24500.00, 150.0, "ACTIVE", "uuid-restockingfeerule-01"),
    (2, "RES-0002", "Secondary Corporate RestockingFeeRule 2", 18200.50, 80.0, "ACTIVE", "uuid-restockingfeerule-02"),
    (3, "RES-0003", "Consolidated Branch RestockingFeeRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-restockingfeerule-03"),
    (4, "RES-0004", "Enterprise Audited RestockingFeeRule 4", 32800.00, 210.0, "ACTIVE", "uuid-restockingfeerule-04"),
    (5, "RES-0005", "Executive Strategic RestockingFeeRule 5", 65000.00, 400.0, "ACTIVE", "uuid-restockingfeerule-05");

CREATE TABLE IF NOT EXISTS returns_rma_customerrefundcreditnotes (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_customerrefundcreditnotes_code ON returns_rma_customerrefundcreditnotes(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_customerrefundcreditnotes_org_status ON returns_rma_customerrefundcreditnotes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_customerrefundcreditnotes_priority ON returns_rma_customerrefundcreditnotes(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_customerrefundcreditnotes_created_at ON returns_rma_customerrefundcreditnotes(created_at);

-- Operational seed data fixtures for returns_rma_customerrefundcreditnotes
INSERT OR IGNORE INTO returns_rma_customerrefundcreditnotes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerRefundCreditNote 1", 24500.00, 150.0, "ACTIVE", "uuid-customerrefundcreditnote-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerRefundCreditNote 2", 18200.50, 80.0, "ACTIVE", "uuid-customerrefundcreditnote-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerRefundCreditNote 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerrefundcreditnote-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerRefundCreditNote 4", 32800.00, 210.0, "ACTIVE", "uuid-customerrefundcreditnote-04"),
    (5, "CUS-0005", "Executive Strategic CustomerRefundCreditNote 5", 65000.00, 400.0, "ACTIVE", "uuid-customerrefundcreditnote-05");

CREATE TABLE IF NOT EXISTS returns_rma_quarantinedispositions (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_quarantinedispositions_code ON returns_rma_quarantinedispositions(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_quarantinedispositions_org_status ON returns_rma_quarantinedispositions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_quarantinedispositions_priority ON returns_rma_quarantinedispositions(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_quarantinedispositions_created_at ON returns_rma_quarantinedispositions(created_at);

-- Operational seed data fixtures for returns_rma_quarantinedispositions
INSERT OR IGNORE INTO returns_rma_quarantinedispositions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "QUA-0001", "Primary Operational QuarantineDisposition 1", 24500.00, 150.0, "ACTIVE", "uuid-quarantinedisposition-01"),
    (2, "QUA-0002", "Secondary Corporate QuarantineDisposition 2", 18200.50, 80.0, "ACTIVE", "uuid-quarantinedisposition-02"),
    (3, "QUA-0003", "Consolidated Branch QuarantineDisposition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-quarantinedisposition-03"),
    (4, "QUA-0004", "Enterprise Audited QuarantineDisposition 4", 32800.00, 210.0, "ACTIVE", "uuid-quarantinedisposition-04"),
    (5, "QUA-0005", "Executive Strategic QuarantineDisposition 5", 65000.00, 400.0, "ACTIVE", "uuid-quarantinedisposition-05");

CREATE TABLE IF NOT EXISTS returns_rma_warrantyverifications (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_warrantyverifications_code ON returns_rma_warrantyverifications(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_warrantyverifications_org_status ON returns_rma_warrantyverifications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_warrantyverifications_priority ON returns_rma_warrantyverifications(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_warrantyverifications_created_at ON returns_rma_warrantyverifications(created_at);

-- Operational seed data fixtures for returns_rma_warrantyverifications
INSERT OR IGNORE INTO returns_rma_warrantyverifications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAR-0001", "Primary Operational WarrantyVerification 1", 24500.00, 150.0, "ACTIVE", "uuid-warrantyverification-01"),
    (2, "WAR-0002", "Secondary Corporate WarrantyVerification 2", 18200.50, 80.0, "ACTIVE", "uuid-warrantyverification-02"),
    (3, "WAR-0003", "Consolidated Branch WarrantyVerification 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-warrantyverification-03"),
    (4, "WAR-0004", "Enterprise Audited WarrantyVerification 4", 32800.00, 210.0, "ACTIVE", "uuid-warrantyverification-04"),
    (5, "WAR-0005", "Executive Strategic WarrantyVerification 5", 65000.00, 400.0, "ACTIVE", "uuid-warrantyverification-05");

CREATE TABLE IF NOT EXISTS returns_rma_refurbishmentworkorders (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_refurbishmentworkorders_code ON returns_rma_refurbishmentworkorders(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_refurbishmentworkorders_org_status ON returns_rma_refurbishmentworkorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_refurbishmentworkorders_priority ON returns_rma_refurbishmentworkorders(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_refurbishmentworkorders_created_at ON returns_rma_refurbishmentworkorders(created_at);

-- Operational seed data fixtures for returns_rma_refurbishmentworkorders
INSERT OR IGNORE INTO returns_rma_refurbishmentworkorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REF-0001", "Primary Operational RefurbishmentWorkOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-refurbishmentworkorder-01"),
    (2, "REF-0002", "Secondary Corporate RefurbishmentWorkOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-refurbishmentworkorder-02"),
    (3, "REF-0003", "Consolidated Branch RefurbishmentWorkOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-refurbishmentworkorder-03"),
    (4, "REF-0004", "Enterprise Audited RefurbishmentWorkOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-refurbishmentworkorder-04"),
    (5, "REF-0005", "Executive Strategic RefurbishmentWorkOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-refurbishmentworkorder-05");

CREATE TABLE IF NOT EXISTS returns_rma_scrapauthorizations (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_scrapauthorizations_code ON returns_rma_scrapauthorizations(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_scrapauthorizations_org_status ON returns_rma_scrapauthorizations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_scrapauthorizations_priority ON returns_rma_scrapauthorizations(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_scrapauthorizations_created_at ON returns_rma_scrapauthorizations(created_at);

-- Operational seed data fixtures for returns_rma_scrapauthorizations
INSERT OR IGNORE INTO returns_rma_scrapauthorizations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SCR-0001", "Primary Operational ScrapAuthorization 1", 24500.00, 150.0, "ACTIVE", "uuid-scrapauthorization-01"),
    (2, "SCR-0002", "Secondary Corporate ScrapAuthorization 2", 18200.50, 80.0, "ACTIVE", "uuid-scrapauthorization-02"),
    (3, "SCR-0003", "Consolidated Branch ScrapAuthorization 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-scrapauthorization-03"),
    (4, "SCR-0004", "Enterprise Audited ScrapAuthorization 4", 32800.00, 210.0, "ACTIVE", "uuid-scrapauthorization-04"),
    (5, "SCR-0005", "Executive Strategic ScrapAuthorization 5", 65000.00, 400.0, "ACTIVE", "uuid-scrapauthorization-05");

CREATE TABLE IF NOT EXISTS returns_rma_carrierreturnwaybills (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_carrierreturnwaybills_code ON returns_rma_carrierreturnwaybills(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_carrierreturnwaybills_org_status ON returns_rma_carrierreturnwaybills(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_carrierreturnwaybills_priority ON returns_rma_carrierreturnwaybills(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_carrierreturnwaybills_created_at ON returns_rma_carrierreturnwaybills(created_at);

-- Operational seed data fixtures for returns_rma_carrierreturnwaybills
INSERT OR IGNORE INTO returns_rma_carrierreturnwaybills (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAR-0001", "Primary Operational CarrierReturnWaybill 1", 24500.00, 150.0, "ACTIVE", "uuid-carrierreturnwaybill-01"),
    (2, "CAR-0002", "Secondary Corporate CarrierReturnWaybill 2", 18200.50, 80.0, "ACTIVE", "uuid-carrierreturnwaybill-02"),
    (3, "CAR-0003", "Consolidated Branch CarrierReturnWaybill 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-carrierreturnwaybill-03"),
    (4, "CAR-0004", "Enterprise Audited CarrierReturnWaybill 4", 32800.00, 210.0, "ACTIVE", "uuid-carrierreturnwaybill-04"),
    (5, "CAR-0005", "Executive Strategic CarrierReturnWaybill 5", 65000.00, 400.0, "ACTIVE", "uuid-carrierreturnwaybill-05");

CREATE TABLE IF NOT EXISTS returns_rma_customerreturnreasons (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_customerreturnreasons_code ON returns_rma_customerreturnreasons(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_customerreturnreasons_org_status ON returns_rma_customerreturnreasons(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_customerreturnreasons_priority ON returns_rma_customerreturnreasons(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_customerreturnreasons_created_at ON returns_rma_customerreturnreasons(created_at);

-- Operational seed data fixtures for returns_rma_customerreturnreasons
INSERT OR IGNORE INTO returns_rma_customerreturnreasons (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerReturnReason 1", 24500.00, 150.0, "ACTIVE", "uuid-customerreturnreason-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerReturnReason 2", 18200.50, 80.0, "ACTIVE", "uuid-customerreturnreason-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerReturnReason 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerreturnreason-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerReturnReason 4", 32800.00, 210.0, "ACTIVE", "uuid-customerreturnreason-04"),
    (5, "CUS-0005", "Executive Strategic CustomerReturnReason 5", 65000.00, 400.0, "ACTIVE", "uuid-customerreturnreason-05");

CREATE TABLE IF NOT EXISTS returns_rma_replacementshipments (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_replacementshipments_code ON returns_rma_replacementshipments(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_replacementshipments_org_status ON returns_rma_replacementshipments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_replacementshipments_priority ON returns_rma_replacementshipments(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_replacementshipments_created_at ON returns_rma_replacementshipments(created_at);

-- Operational seed data fixtures for returns_rma_replacementshipments
INSERT OR IGNORE INTO returns_rma_replacementshipments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REP-0001", "Primary Operational ReplacementShipment 1", 24500.00, 150.0, "ACTIVE", "uuid-replacementshipment-01"),
    (2, "REP-0002", "Secondary Corporate ReplacementShipment 2", 18200.50, 80.0, "ACTIVE", "uuid-replacementshipment-02"),
    (3, "REP-0003", "Consolidated Branch ReplacementShipment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-replacementshipment-03"),
    (4, "REP-0004", "Enterprise Audited ReplacementShipment 4", 32800.00, 210.0, "ACTIVE", "uuid-replacementshipment-04"),
    (5, "REP-0005", "Executive Strategic ReplacementShipment 5", 65000.00, 400.0, "ACTIVE", "uuid-replacementshipment-05");

CREATE TABLE IF NOT EXISTS returns_rma_returnanalyticsmetrics (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_returnanalyticsmetrics_code ON returns_rma_returnanalyticsmetrics(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnanalyticsmetrics_org_status ON returns_rma_returnanalyticsmetrics(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnanalyticsmetrics_priority ON returns_rma_returnanalyticsmetrics(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnanalyticsmetrics_created_at ON returns_rma_returnanalyticsmetrics(created_at);

-- Operational seed data fixtures for returns_rma_returnanalyticsmetrics
INSERT OR IGNORE INTO returns_rma_returnanalyticsmetrics (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational ReturnAnalyticsMetric 1", 24500.00, 150.0, "ACTIVE", "uuid-returnanalyticsmetric-01"),
    (2, "RET-0002", "Secondary Corporate ReturnAnalyticsMetric 2", 18200.50, 80.0, "ACTIVE", "uuid-returnanalyticsmetric-02"),
    (3, "RET-0003", "Consolidated Branch ReturnAnalyticsMetric 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-returnanalyticsmetric-03"),
    (4, "RET-0004", "Enterprise Audited ReturnAnalyticsMetric 4", 32800.00, 210.0, "ACTIVE", "uuid-returnanalyticsmetric-04"),
    (5, "RET-0005", "Executive Strategic ReturnAnalyticsMetric 5", 65000.00, 400.0, "ACTIVE", "uuid-returnanalyticsmetric-05");

CREATE TABLE IF NOT EXISTS returns_rma_vendorchargebackclaims (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_vendorchargebackclaims_code ON returns_rma_vendorchargebackclaims(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_vendorchargebackclaims_org_status ON returns_rma_vendorchargebackclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_vendorchargebackclaims_priority ON returns_rma_vendorchargebackclaims(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_vendorchargebackclaims_created_at ON returns_rma_vendorchargebackclaims(created_at);

-- Operational seed data fixtures for returns_rma_vendorchargebackclaims
INSERT OR IGNORE INTO returns_rma_vendorchargebackclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorChargebackClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorchargebackclaim-01"),
    (2, "VEN-0002", "Secondary Corporate VendorChargebackClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorchargebackclaim-02"),
    (3, "VEN-0003", "Consolidated Branch VendorChargebackClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorchargebackclaim-03"),
    (4, "VEN-0004", "Enterprise Audited VendorChargebackClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorchargebackclaim-04"),
    (5, "VEN-0005", "Executive Strategic VendorChargebackClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorchargebackclaim-05");

CREATE TABLE IF NOT EXISTS returns_rma_packagingconditionlogs (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_packagingconditionlogs_code ON returns_rma_packagingconditionlogs(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_packagingconditionlogs_org_status ON returns_rma_packagingconditionlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_packagingconditionlogs_priority ON returns_rma_packagingconditionlogs(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_packagingconditionlogs_created_at ON returns_rma_packagingconditionlogs(created_at);

-- Operational seed data fixtures for returns_rma_packagingconditionlogs
INSERT OR IGNORE INTO returns_rma_packagingconditionlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAC-0001", "Primary Operational PackagingConditionLog 1", 24500.00, 150.0, "ACTIVE", "uuid-packagingconditionlog-01"),
    (2, "PAC-0002", "Secondary Corporate PackagingConditionLog 2", 18200.50, 80.0, "ACTIVE", "uuid-packagingconditionlog-02"),
    (3, "PAC-0003", "Consolidated Branch PackagingConditionLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-packagingconditionlog-03"),
    (4, "PAC-0004", "Enterprise Audited PackagingConditionLog 4", 32800.00, 210.0, "ACTIVE", "uuid-packagingconditionlog-04"),
    (5, "PAC-0005", "Executive Strategic PackagingConditionLog 5", 65000.00, 400.0, "ACTIVE", "uuid-packagingconditionlog-05");

CREATE TABLE IF NOT EXISTS returns_rma_returnpolicyrules (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_returnpolicyrules_code ON returns_rma_returnpolicyrules(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnpolicyrules_org_status ON returns_rma_returnpolicyrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnpolicyrules_priority ON returns_rma_returnpolicyrules(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_returnpolicyrules_created_at ON returns_rma_returnpolicyrules(created_at);

-- Operational seed data fixtures for returns_rma_returnpolicyrules
INSERT OR IGNORE INTO returns_rma_returnpolicyrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational ReturnPolicyRule 1", 24500.00, 150.0, "ACTIVE", "uuid-returnpolicyrule-01"),
    (2, "RET-0002", "Secondary Corporate ReturnPolicyRule 2", 18200.50, 80.0, "ACTIVE", "uuid-returnpolicyrule-02"),
    (3, "RET-0003", "Consolidated Branch ReturnPolicyRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-returnpolicyrule-03"),
    (4, "RET-0004", "Enterprise Audited ReturnPolicyRule 4", 32800.00, 210.0, "ACTIVE", "uuid-returnpolicyrule-04"),
    (5, "RET-0005", "Executive Strategic ReturnPolicyRule 5", 65000.00, 400.0, "ACTIVE", "uuid-returnpolicyrule-05");

CREATE TABLE IF NOT EXISTS returns_rma_depotrepairstatuss (
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

CREATE INDEX IF NOT EXISTS idx_returns_rma_depotrepairstatuss_code ON returns_rma_depotrepairstatuss(code);
CREATE INDEX IF NOT EXISTS idx_returns_rma_depotrepairstatuss_org_status ON returns_rma_depotrepairstatuss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_returns_rma_depotrepairstatuss_priority ON returns_rma_depotrepairstatuss(priority);
CREATE INDEX IF NOT EXISTS idx_returns_rma_depotrepairstatuss_created_at ON returns_rma_depotrepairstatuss(created_at);

-- Operational seed data fixtures for returns_rma_depotrepairstatuss
INSERT OR IGNORE INTO returns_rma_depotrepairstatuss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DepotRepairStatus 1", 24500.00, 150.0, "ACTIVE", "uuid-depotrepairstatus-01"),
    (2, "DEP-0002", "Secondary Corporate DepotRepairStatus 2", 18200.50, 80.0, "ACTIVE", "uuid-depotrepairstatus-02"),
    (3, "DEP-0003", "Consolidated Branch DepotRepairStatus 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-depotrepairstatus-03"),
    (4, "DEP-0004", "Enterprise Audited DepotRepairStatus 4", 32800.00, 210.0, "ACTIVE", "uuid-depotrepairstatus-04"),
    (5, "DEP-0005", "Executive Strategic DepotRepairStatus 5", 65000.00, 400.0, "ACTIVE", "uuid-depotrepairstatus-05");

