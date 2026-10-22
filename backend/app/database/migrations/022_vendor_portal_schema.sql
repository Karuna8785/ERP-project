-- SmartERP Enterprise Titan Migration 022: Supplier Collaboration & Vendor Portal DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS vendor_portal_vendorportalusers (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorportalusers_code ON vendor_portal_vendorportalusers(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorportalusers_org_status ON vendor_portal_vendorportalusers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorportalusers_priority ON vendor_portal_vendorportalusers(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorportalusers_created_at ON vendor_portal_vendorportalusers(created_at);

-- Operational seed data fixtures for vendor_portal_vendorportalusers
INSERT OR IGNORE INTO vendor_portal_vendorportalusers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorPortalUser 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorportaluser-01"),
    (2, "VEN-0002", "Secondary Corporate VendorPortalUser 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorportaluser-02"),
    (3, "VEN-0003", "Consolidated Branch VendorPortalUser 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorportaluser-03"),
    (4, "VEN-0004", "Enterprise Audited VendorPortalUser 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorportaluser-04"),
    (5, "VEN-0005", "Executive Strategic VendorPortalUser 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorportaluser-05");

CREATE TABLE IF NOT EXISTS vendor_portal_suppliercompanyprofiles (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_suppliercompanyprofiles_code ON vendor_portal_suppliercompanyprofiles(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_suppliercompanyprofiles_org_status ON vendor_portal_suppliercompanyprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_suppliercompanyprofiles_priority ON vendor_portal_suppliercompanyprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_suppliercompanyprofiles_created_at ON vendor_portal_suppliercompanyprofiles(created_at);

-- Operational seed data fixtures for vendor_portal_suppliercompanyprofiles
INSERT OR IGNORE INTO vendor_portal_suppliercompanyprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierCompanyProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-suppliercompanyprofile-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierCompanyProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-suppliercompanyprofile-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierCompanyProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-suppliercompanyprofile-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierCompanyProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-suppliercompanyprofile-04"),
    (5, "SUP-0005", "Executive Strategic SupplierCompanyProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-suppliercompanyprofile-05");

CREATE TABLE IF NOT EXISTS vendor_portal_poacknowledgements (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_poacknowledgements_code ON vendor_portal_poacknowledgements(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_poacknowledgements_org_status ON vendor_portal_poacknowledgements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_poacknowledgements_priority ON vendor_portal_poacknowledgements(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_poacknowledgements_created_at ON vendor_portal_poacknowledgements(created_at);

-- Operational seed data fixtures for vendor_portal_poacknowledgements
INSERT OR IGNORE INTO vendor_portal_poacknowledgements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "POA-0001", "Primary Operational POAcknowledgement 1", 24500.00, 150.0, "ACTIVE", "uuid-poacknowledgement-01"),
    (2, "POA-0002", "Secondary Corporate POAcknowledgement 2", 18200.50, 80.0, "ACTIVE", "uuid-poacknowledgement-02"),
    (3, "POA-0003", "Consolidated Branch POAcknowledgement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-poacknowledgement-03"),
    (4, "POA-0004", "Enterprise Audited POAcknowledgement 4", 32800.00, 210.0, "ACTIVE", "uuid-poacknowledgement-04"),
    (5, "POA-0005", "Executive Strategic POAcknowledgement 5", 65000.00, 400.0, "ACTIVE", "uuid-poacknowledgement-05");

CREATE TABLE IF NOT EXISTS vendor_portal_advanceshippingnotices (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_advanceshippingnotices_code ON vendor_portal_advanceshippingnotices(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_advanceshippingnotices_org_status ON vendor_portal_advanceshippingnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_advanceshippingnotices_priority ON vendor_portal_advanceshippingnotices(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_advanceshippingnotices_created_at ON vendor_portal_advanceshippingnotices(created_at);

-- Operational seed data fixtures for vendor_portal_advanceshippingnotices
INSERT OR IGNORE INTO vendor_portal_advanceshippingnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ADV-0001", "Primary Operational AdvanceShippingNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-advanceshippingnotice-01"),
    (2, "ADV-0002", "Secondary Corporate AdvanceShippingNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-advanceshippingnotice-02"),
    (3, "ADV-0003", "Consolidated Branch AdvanceShippingNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-advanceshippingnotice-03"),
    (4, "ADV-0004", "Enterprise Audited AdvanceShippingNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-advanceshippingnotice-04"),
    (5, "ADV-0005", "Executive Strategic AdvanceShippingNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-advanceshippingnotice-05");

CREATE TABLE IF NOT EXISTS vendor_portal_supplierinvoicesubmissions (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierinvoicesubmissions_code ON vendor_portal_supplierinvoicesubmissions(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierinvoicesubmissions_org_status ON vendor_portal_supplierinvoicesubmissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierinvoicesubmissions_priority ON vendor_portal_supplierinvoicesubmissions(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierinvoicesubmissions_created_at ON vendor_portal_supplierinvoicesubmissions(created_at);

-- Operational seed data fixtures for vendor_portal_supplierinvoicesubmissions
INSERT OR IGNORE INTO vendor_portal_supplierinvoicesubmissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierInvoiceSubmission 1", 24500.00, 150.0, "ACTIVE", "uuid-supplierinvoicesubmission-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierInvoiceSubmission 2", 18200.50, 80.0, "ACTIVE", "uuid-supplierinvoicesubmission-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierInvoiceSubmission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supplierinvoicesubmission-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierInvoiceSubmission 4", 32800.00, 210.0, "ACTIVE", "uuid-supplierinvoicesubmission-04"),
    (5, "SUP-0005", "Executive Strategic SupplierInvoiceSubmission 5", 65000.00, 400.0, "ACTIVE", "uuid-supplierinvoicesubmission-05");

CREATE TABLE IF NOT EXISTS vendor_portal_debitnoteclaims (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_debitnoteclaims_code ON vendor_portal_debitnoteclaims(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_debitnoteclaims_org_status ON vendor_portal_debitnoteclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_debitnoteclaims_priority ON vendor_portal_debitnoteclaims(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_debitnoteclaims_created_at ON vendor_portal_debitnoteclaims(created_at);

-- Operational seed data fixtures for vendor_portal_debitnoteclaims
INSERT OR IGNORE INTO vendor_portal_debitnoteclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEB-0001", "Primary Operational DebitNoteClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-debitnoteclaim-01"),
    (2, "DEB-0002", "Secondary Corporate DebitNoteClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-debitnoteclaim-02"),
    (3, "DEB-0003", "Consolidated Branch DebitNoteClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-debitnoteclaim-03"),
    (4, "DEB-0004", "Enterprise Audited DebitNoteClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-debitnoteclaim-04"),
    (5, "DEB-0005", "Executive Strategic DebitNoteClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-debitnoteclaim-05");

CREATE TABLE IF NOT EXISTS vendor_portal_paymentstatusquerys (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_paymentstatusquerys_code ON vendor_portal_paymentstatusquerys(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_paymentstatusquerys_org_status ON vendor_portal_paymentstatusquerys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_paymentstatusquerys_priority ON vendor_portal_paymentstatusquerys(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_paymentstatusquerys_created_at ON vendor_portal_paymentstatusquerys(created_at);

-- Operational seed data fixtures for vendor_portal_paymentstatusquerys
INSERT OR IGNORE INTO vendor_portal_paymentstatusquerys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAY-0001", "Primary Operational PaymentStatusQuery 1", 24500.00, 150.0, "ACTIVE", "uuid-paymentstatusquery-01"),
    (2, "PAY-0002", "Secondary Corporate PaymentStatusQuery 2", 18200.50, 80.0, "ACTIVE", "uuid-paymentstatusquery-02"),
    (3, "PAY-0003", "Consolidated Branch PaymentStatusQuery 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-paymentstatusquery-03"),
    (4, "PAY-0004", "Enterprise Audited PaymentStatusQuery 4", 32800.00, 210.0, "ACTIVE", "uuid-paymentstatusquery-04"),
    (5, "PAY-0005", "Executive Strategic PaymentStatusQuery 5", 65000.00, 400.0, "ACTIVE", "uuid-paymentstatusquery-05");

CREATE TABLE IF NOT EXISTS vendor_portal_qualityrejectionfeedbacks (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_qualityrejectionfeedbacks_code ON vendor_portal_qualityrejectionfeedbacks(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_qualityrejectionfeedbacks_org_status ON vendor_portal_qualityrejectionfeedbacks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_qualityrejectionfeedbacks_priority ON vendor_portal_qualityrejectionfeedbacks(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_qualityrejectionfeedbacks_created_at ON vendor_portal_qualityrejectionfeedbacks(created_at);

-- Operational seed data fixtures for vendor_portal_qualityrejectionfeedbacks
INSERT OR IGNORE INTO vendor_portal_qualityrejectionfeedbacks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "QUA-0001", "Primary Operational QualityRejectionFeedback 1", 24500.00, 150.0, "ACTIVE", "uuid-qualityrejectionfeedback-01"),
    (2, "QUA-0002", "Secondary Corporate QualityRejectionFeedback 2", 18200.50, 80.0, "ACTIVE", "uuid-qualityrejectionfeedback-02"),
    (3, "QUA-0003", "Consolidated Branch QualityRejectionFeedback 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-qualityrejectionfeedback-03"),
    (4, "QUA-0004", "Enterprise Audited QualityRejectionFeedback 4", 32800.00, 210.0, "ACTIVE", "uuid-qualityrejectionfeedback-04"),
    (5, "QUA-0005", "Executive Strategic QualityRejectionFeedback 5", 65000.00, 400.0, "ACTIVE", "uuid-qualityrejectionfeedback-05");

CREATE TABLE IF NOT EXISTS vendor_portal_vendordocumentsubmissions (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendordocumentsubmissions_code ON vendor_portal_vendordocumentsubmissions(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendordocumentsubmissions_org_status ON vendor_portal_vendordocumentsubmissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendordocumentsubmissions_priority ON vendor_portal_vendordocumentsubmissions(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendordocumentsubmissions_created_at ON vendor_portal_vendordocumentsubmissions(created_at);

-- Operational seed data fixtures for vendor_portal_vendordocumentsubmissions
INSERT OR IGNORE INTO vendor_portal_vendordocumentsubmissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorDocumentSubmission 1", 24500.00, 150.0, "ACTIVE", "uuid-vendordocumentsubmission-01"),
    (2, "VEN-0002", "Secondary Corporate VendorDocumentSubmission 2", 18200.50, 80.0, "ACTIVE", "uuid-vendordocumentsubmission-02"),
    (3, "VEN-0003", "Consolidated Branch VendorDocumentSubmission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendordocumentsubmission-03"),
    (4, "VEN-0004", "Enterprise Audited VendorDocumentSubmission 4", 32800.00, 210.0, "ACTIVE", "uuid-vendordocumentsubmission-04"),
    (5, "VEN-0005", "Executive Strategic VendorDocumentSubmission 5", 65000.00, 400.0, "ACTIVE", "uuid-vendordocumentsubmission-05");

CREATE TABLE IF NOT EXISTS vendor_portal_compliancecheckacknowledgements (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_compliancecheckacknowledgements_code ON vendor_portal_compliancecheckacknowledgements(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_compliancecheckacknowledgements_org_status ON vendor_portal_compliancecheckacknowledgements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_compliancecheckacknowledgements_priority ON vendor_portal_compliancecheckacknowledgements(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_compliancecheckacknowledgements_created_at ON vendor_portal_compliancecheckacknowledgements(created_at);

-- Operational seed data fixtures for vendor_portal_compliancecheckacknowledgements
INSERT OR IGNORE INTO vendor_portal_compliancecheckacknowledgements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational ComplianceCheckAcknowledgement 1", 24500.00, 150.0, "ACTIVE", "uuid-compliancecheckacknowledgement-01"),
    (2, "COM-0002", "Secondary Corporate ComplianceCheckAcknowledgement 2", 18200.50, 80.0, "ACTIVE", "uuid-compliancecheckacknowledgement-02"),
    (3, "COM-0003", "Consolidated Branch ComplianceCheckAcknowledgement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-compliancecheckacknowledgement-03"),
    (4, "COM-0004", "Enterprise Audited ComplianceCheckAcknowledgement 4", 32800.00, 210.0, "ACTIVE", "uuid-compliancecheckacknowledgement-04"),
    (5, "COM-0005", "Executive Strategic ComplianceCheckAcknowledgement 5", 65000.00, 400.0, "ACTIVE", "uuid-compliancecheckacknowledgement-05");

CREATE TABLE IF NOT EXISTS vendor_portal_supplierscorecardviews (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierscorecardviews_code ON vendor_portal_supplierscorecardviews(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierscorecardviews_org_status ON vendor_portal_supplierscorecardviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierscorecardviews_priority ON vendor_portal_supplierscorecardviews(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierscorecardviews_created_at ON vendor_portal_supplierscorecardviews(created_at);

-- Operational seed data fixtures for vendor_portal_supplierscorecardviews
INSERT OR IGNORE INTO vendor_portal_supplierscorecardviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierScorecardView 1", 24500.00, 150.0, "ACTIVE", "uuid-supplierscorecardview-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierScorecardView 2", 18200.50, 80.0, "ACTIVE", "uuid-supplierscorecardview-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierScorecardView 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supplierscorecardview-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierScorecardView 4", 32800.00, 210.0, "ACTIVE", "uuid-supplierscorecardview-04"),
    (5, "SUP-0005", "Executive Strategic SupplierScorecardView 5", 65000.00, 400.0, "ACTIVE", "uuid-supplierscorecardview-05");

CREATE TABLE IF NOT EXISTS vendor_portal_rfqresponsebids (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_rfqresponsebids_code ON vendor_portal_rfqresponsebids(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_rfqresponsebids_org_status ON vendor_portal_rfqresponsebids(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_rfqresponsebids_priority ON vendor_portal_rfqresponsebids(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_rfqresponsebids_created_at ON vendor_portal_rfqresponsebids(created_at);

-- Operational seed data fixtures for vendor_portal_rfqresponsebids
INSERT OR IGNORE INTO vendor_portal_rfqresponsebids (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RFQ-0001", "Primary Operational RFQResponseBid 1", 24500.00, 150.0, "ACTIVE", "uuid-rfqresponsebid-01"),
    (2, "RFQ-0002", "Secondary Corporate RFQResponseBid 2", 18200.50, 80.0, "ACTIVE", "uuid-rfqresponsebid-02"),
    (3, "RFQ-0003", "Consolidated Branch RFQResponseBid 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-rfqresponsebid-03"),
    (4, "RFQ-0004", "Enterprise Audited RFQResponseBid 4", 32800.00, 210.0, "ACTIVE", "uuid-rfqresponsebid-04"),
    (5, "RFQ-0005", "Executive Strategic RFQResponseBid 5", 65000.00, 400.0, "ACTIVE", "uuid-rfqresponsebid-05");

CREATE TABLE IF NOT EXISTS vendor_portal_cataloguepriceupdates (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_cataloguepriceupdates_code ON vendor_portal_cataloguepriceupdates(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_cataloguepriceupdates_org_status ON vendor_portal_cataloguepriceupdates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_cataloguepriceupdates_priority ON vendor_portal_cataloguepriceupdates(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_cataloguepriceupdates_created_at ON vendor_portal_cataloguepriceupdates(created_at);

-- Operational seed data fixtures for vendor_portal_cataloguepriceupdates
INSERT OR IGNORE INTO vendor_portal_cataloguepriceupdates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAT-0001", "Primary Operational CataloguePriceUpdate 1", 24500.00, 150.0, "ACTIVE", "uuid-cataloguepriceupdate-01"),
    (2, "CAT-0002", "Secondary Corporate CataloguePriceUpdate 2", 18200.50, 80.0, "ACTIVE", "uuid-cataloguepriceupdate-02"),
    (3, "CAT-0003", "Consolidated Branch CataloguePriceUpdate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cataloguepriceupdate-03"),
    (4, "CAT-0004", "Enterprise Audited CataloguePriceUpdate 4", 32800.00, 210.0, "ACTIVE", "uuid-cataloguepriceupdate-04"),
    (5, "CAT-0005", "Executive Strategic CataloguePriceUpdate 5", 65000.00, 400.0, "ACTIVE", "uuid-cataloguepriceupdate-05");

CREATE TABLE IF NOT EXISTS vendor_portal_vendorcontactdirectorys (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorcontactdirectorys_code ON vendor_portal_vendorcontactdirectorys(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorcontactdirectorys_org_status ON vendor_portal_vendorcontactdirectorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorcontactdirectorys_priority ON vendor_portal_vendorcontactdirectorys(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_vendorcontactdirectorys_created_at ON vendor_portal_vendorcontactdirectorys(created_at);

-- Operational seed data fixtures for vendor_portal_vendorcontactdirectorys
INSERT OR IGNORE INTO vendor_portal_vendorcontactdirectorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VEN-0001", "Primary Operational VendorContactDirectory 1", 24500.00, 150.0, "ACTIVE", "uuid-vendorcontactdirectory-01"),
    (2, "VEN-0002", "Secondary Corporate VendorContactDirectory 2", 18200.50, 80.0, "ACTIVE", "uuid-vendorcontactdirectory-02"),
    (3, "VEN-0003", "Consolidated Branch VendorContactDirectory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-vendorcontactdirectory-03"),
    (4, "VEN-0004", "Enterprise Audited VendorContactDirectory 4", 32800.00, 210.0, "ACTIVE", "uuid-vendorcontactdirectory-04"),
    (5, "VEN-0005", "Executive Strategic VendorContactDirectory 5", 65000.00, 400.0, "ACTIVE", "uuid-vendorcontactdirectory-05");

CREATE TABLE IF NOT EXISTS vendor_portal_supplierannouncementnotices (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierannouncementnotices_code ON vendor_portal_supplierannouncementnotices(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierannouncementnotices_org_status ON vendor_portal_supplierannouncementnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierannouncementnotices_priority ON vendor_portal_supplierannouncementnotices(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_supplierannouncementnotices_created_at ON vendor_portal_supplierannouncementnotices(created_at);

-- Operational seed data fixtures for vendor_portal_supplierannouncementnotices
INSERT OR IGNORE INTO vendor_portal_supplierannouncementnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupplierAnnouncementNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-supplierannouncementnotice-01"),
    (2, "SUP-0002", "Secondary Corporate SupplierAnnouncementNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-supplierannouncementnotice-02"),
    (3, "SUP-0003", "Consolidated Branch SupplierAnnouncementNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supplierannouncementnotice-03"),
    (4, "SUP-0004", "Enterprise Audited SupplierAnnouncementNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-supplierannouncementnotice-04"),
    (5, "SUP-0005", "Executive Strategic SupplierAnnouncementNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-supplierannouncementnotice-05");

CREATE TABLE IF NOT EXISTS vendor_portal_bankdetailverifications (
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

CREATE INDEX IF NOT EXISTS idx_vendor_portal_bankdetailverifications_code ON vendor_portal_bankdetailverifications(code);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_bankdetailverifications_org_status ON vendor_portal_bankdetailverifications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_bankdetailverifications_priority ON vendor_portal_bankdetailverifications(priority);
CREATE INDEX IF NOT EXISTS idx_vendor_portal_bankdetailverifications_created_at ON vendor_portal_bankdetailverifications(created_at);

-- Operational seed data fixtures for vendor_portal_bankdetailverifications
INSERT OR IGNORE INTO vendor_portal_bankdetailverifications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BAN-0001", "Primary Operational BankDetailVerification 1", 24500.00, 150.0, "ACTIVE", "uuid-bankdetailverification-01"),
    (2, "BAN-0002", "Secondary Corporate BankDetailVerification 2", 18200.50, 80.0, "ACTIVE", "uuid-bankdetailverification-02"),
    (3, "BAN-0003", "Consolidated Branch BankDetailVerification 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bankdetailverification-03"),
    (4, "BAN-0004", "Enterprise Audited BankDetailVerification 4", 32800.00, 210.0, "ACTIVE", "uuid-bankdetailverification-04"),
    (5, "BAN-0005", "Executive Strategic BankDetailVerification 5", 65000.00, 400.0, "ACTIVE", "uuid-bankdetailverification-05");

