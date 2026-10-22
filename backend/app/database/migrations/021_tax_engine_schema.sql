-- SmartERP Enterprise Titan Migration 021: Global Tax Determination & Reporting DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS tax_engine_taxjurisdictions (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_taxjurisdictions_code ON tax_engine_taxjurisdictions(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxjurisdictions_org_status ON tax_engine_taxjurisdictions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxjurisdictions_priority ON tax_engine_taxjurisdictions(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxjurisdictions_created_at ON tax_engine_taxjurisdictions(created_at);

-- Operational seed data fixtures for tax_engine_taxjurisdictions
INSERT OR IGNORE INTO tax_engine_taxjurisdictions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxJurisdiction 1", 24500.00, 150.0, "ACTIVE", "uuid-taxjurisdiction-01"),
    (2, "TAX-0002", "Secondary Corporate TaxJurisdiction 2", 18200.50, 80.0, "ACTIVE", "uuid-taxjurisdiction-02"),
    (3, "TAX-0003", "Consolidated Branch TaxJurisdiction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxjurisdiction-03"),
    (4, "TAX-0004", "Enterprise Audited TaxJurisdiction 4", 32800.00, 210.0, "ACTIVE", "uuid-taxjurisdiction-04"),
    (5, "TAX-0005", "Executive Strategic TaxJurisdiction 5", 65000.00, 400.0, "ACTIVE", "uuid-taxjurisdiction-05");

CREATE TABLE IF NOT EXISTS tax_engine_taxrateschedules (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_taxrateschedules_code ON tax_engine_taxrateschedules(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxrateschedules_org_status ON tax_engine_taxrateschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxrateschedules_priority ON tax_engine_taxrateschedules(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxrateschedules_created_at ON tax_engine_taxrateschedules(created_at);

-- Operational seed data fixtures for tax_engine_taxrateschedules
INSERT OR IGNORE INTO tax_engine_taxrateschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxRateSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-taxrateschedule-01"),
    (2, "TAX-0002", "Secondary Corporate TaxRateSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-taxrateschedule-02"),
    (3, "TAX-0003", "Consolidated Branch TaxRateSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxrateschedule-03"),
    (4, "TAX-0004", "Enterprise Audited TaxRateSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-taxrateschedule-04"),
    (5, "TAX-0005", "Executive Strategic TaxRateSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-taxrateschedule-05");

CREATE TABLE IF NOT EXISTS tax_engine_taxexemptioncertificates (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_taxexemptioncertificates_code ON tax_engine_taxexemptioncertificates(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxexemptioncertificates_org_status ON tax_engine_taxexemptioncertificates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxexemptioncertificates_priority ON tax_engine_taxexemptioncertificates(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxexemptioncertificates_created_at ON tax_engine_taxexemptioncertificates(created_at);

-- Operational seed data fixtures for tax_engine_taxexemptioncertificates
INSERT OR IGNORE INTO tax_engine_taxexemptioncertificates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxExemptionCertificate 1", 24500.00, 150.0, "ACTIVE", "uuid-taxexemptioncertificate-01"),
    (2, "TAX-0002", "Secondary Corporate TaxExemptionCertificate 2", 18200.50, 80.0, "ACTIVE", "uuid-taxexemptioncertificate-02"),
    (3, "TAX-0003", "Consolidated Branch TaxExemptionCertificate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxexemptioncertificate-03"),
    (4, "TAX-0004", "Enterprise Audited TaxExemptionCertificate 4", 32800.00, 210.0, "ACTIVE", "uuid-taxexemptioncertificate-04"),
    (5, "TAX-0005", "Executive Strategic TaxExemptionCertificate 5", 65000.00, 400.0, "ACTIVE", "uuid-taxexemptioncertificate-05");

CREATE TABLE IF NOT EXISTS tax_engine_hsnsaccodemasters (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_hsnsaccodemasters_code ON tax_engine_hsnsaccodemasters(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_hsnsaccodemasters_org_status ON tax_engine_hsnsaccodemasters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_hsnsaccodemasters_priority ON tax_engine_hsnsaccodemasters(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_hsnsaccodemasters_created_at ON tax_engine_hsnsaccodemasters(created_at);

-- Operational seed data fixtures for tax_engine_hsnsaccodemasters
INSERT OR IGNORE INTO tax_engine_hsnsaccodemasters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HSN-0001", "Primary Operational HSNSACCodeMaster 1", 24500.00, 150.0, "ACTIVE", "uuid-hsnsaccodemaster-01"),
    (2, "HSN-0002", "Secondary Corporate HSNSACCodeMaster 2", 18200.50, 80.0, "ACTIVE", "uuid-hsnsaccodemaster-02"),
    (3, "HSN-0003", "Consolidated Branch HSNSACCodeMaster 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hsnsaccodemaster-03"),
    (4, "HSN-0004", "Enterprise Audited HSNSACCodeMaster 4", 32800.00, 210.0, "ACTIVE", "uuid-hsnsaccodemaster-04"),
    (5, "HSN-0005", "Executive Strategic HSNSACCodeMaster 5", 65000.00, 400.0, "ACTIVE", "uuid-hsnsaccodemaster-05");

CREATE TABLE IF NOT EXISTS tax_engine_crossbordertariffrules (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_crossbordertariffrules_code ON tax_engine_crossbordertariffrules(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_crossbordertariffrules_org_status ON tax_engine_crossbordertariffrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_crossbordertariffrules_priority ON tax_engine_crossbordertariffrules(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_crossbordertariffrules_created_at ON tax_engine_crossbordertariffrules(created_at);

-- Operational seed data fixtures for tax_engine_crossbordertariffrules
INSERT OR IGNORE INTO tax_engine_crossbordertariffrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CRO-0001", "Primary Operational CrossBorderTariffRule 1", 24500.00, 150.0, "ACTIVE", "uuid-crossbordertariffrule-01"),
    (2, "CRO-0002", "Secondary Corporate CrossBorderTariffRule 2", 18200.50, 80.0, "ACTIVE", "uuid-crossbordertariffrule-02"),
    (3, "CRO-0003", "Consolidated Branch CrossBorderTariffRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-crossbordertariffrule-03"),
    (4, "CRO-0004", "Enterprise Audited CrossBorderTariffRule 4", 32800.00, 210.0, "ACTIVE", "uuid-crossbordertariffrule-04"),
    (5, "CRO-0005", "Executive Strategic CrossBorderTariffRule 5", 65000.00, 400.0, "ACTIVE", "uuid-crossbordertariffrule-05");

CREATE TABLE IF NOT EXISTS tax_engine_reversechargeprovisions (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_reversechargeprovisions_code ON tax_engine_reversechargeprovisions(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_reversechargeprovisions_org_status ON tax_engine_reversechargeprovisions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_reversechargeprovisions_priority ON tax_engine_reversechargeprovisions(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_reversechargeprovisions_created_at ON tax_engine_reversechargeprovisions(created_at);

-- Operational seed data fixtures for tax_engine_reversechargeprovisions
INSERT OR IGNORE INTO tax_engine_reversechargeprovisions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REV-0001", "Primary Operational ReverseChargeProvision 1", 24500.00, 150.0, "ACTIVE", "uuid-reversechargeprovision-01"),
    (2, "REV-0002", "Secondary Corporate ReverseChargeProvision 2", 18200.50, 80.0, "ACTIVE", "uuid-reversechargeprovision-02"),
    (3, "REV-0003", "Consolidated Branch ReverseChargeProvision 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-reversechargeprovision-03"),
    (4, "REV-0004", "Enterprise Audited ReverseChargeProvision 4", 32800.00, 210.0, "ACTIVE", "uuid-reversechargeprovision-04"),
    (5, "REV-0005", "Executive Strategic ReverseChargeProvision 5", 65000.00, 400.0, "ACTIVE", "uuid-reversechargeprovision-05");

CREATE TABLE IF NOT EXISTS tax_engine_tdswithholdingcategorys (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_tdswithholdingcategorys_code ON tax_engine_tdswithholdingcategorys(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_tdswithholdingcategorys_org_status ON tax_engine_tdswithholdingcategorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_tdswithholdingcategorys_priority ON tax_engine_tdswithholdingcategorys(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_tdswithholdingcategorys_created_at ON tax_engine_tdswithholdingcategorys(created_at);

-- Operational seed data fixtures for tax_engine_tdswithholdingcategorys
INSERT OR IGNORE INTO tax_engine_tdswithholdingcategorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TDS-0001", "Primary Operational TDSWithholdingCategory 1", 24500.00, 150.0, "ACTIVE", "uuid-tdswithholdingcategory-01"),
    (2, "TDS-0002", "Secondary Corporate TDSWithholdingCategory 2", 18200.50, 80.0, "ACTIVE", "uuid-tdswithholdingcategory-02"),
    (3, "TDS-0003", "Consolidated Branch TDSWithholdingCategory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tdswithholdingcategory-03"),
    (4, "TDS-0004", "Enterprise Audited TDSWithholdingCategory 4", 32800.00, 210.0, "ACTIVE", "uuid-tdswithholdingcategory-04"),
    (5, "TDS-0005", "Executive Strategic TDSWithholdingCategory 5", 65000.00, 400.0, "ACTIVE", "uuid-tdswithholdingcategory-05");

CREATE TABLE IF NOT EXISTS tax_engine_taxinvoiceheaders (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoiceheaders_code ON tax_engine_taxinvoiceheaders(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoiceheaders_org_status ON tax_engine_taxinvoiceheaders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoiceheaders_priority ON tax_engine_taxinvoiceheaders(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoiceheaders_created_at ON tax_engine_taxinvoiceheaders(created_at);

-- Operational seed data fixtures for tax_engine_taxinvoiceheaders
INSERT OR IGNORE INTO tax_engine_taxinvoiceheaders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxInvoiceHeader 1", 24500.00, 150.0, "ACTIVE", "uuid-taxinvoiceheader-01"),
    (2, "TAX-0002", "Secondary Corporate TaxInvoiceHeader 2", 18200.50, 80.0, "ACTIVE", "uuid-taxinvoiceheader-02"),
    (3, "TAX-0003", "Consolidated Branch TaxInvoiceHeader 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxinvoiceheader-03"),
    (4, "TAX-0004", "Enterprise Audited TaxInvoiceHeader 4", 32800.00, 210.0, "ACTIVE", "uuid-taxinvoiceheader-04"),
    (5, "TAX-0005", "Executive Strategic TaxInvoiceHeader 5", 65000.00, 400.0, "ACTIVE", "uuid-taxinvoiceheader-05");

CREATE TABLE IF NOT EXISTS tax_engine_taxinvoicelineitems (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoicelineitems_code ON tax_engine_taxinvoicelineitems(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoicelineitems_org_status ON tax_engine_taxinvoicelineitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoicelineitems_priority ON tax_engine_taxinvoicelineitems(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxinvoicelineitems_created_at ON tax_engine_taxinvoicelineitems(created_at);

-- Operational seed data fixtures for tax_engine_taxinvoicelineitems
INSERT OR IGNORE INTO tax_engine_taxinvoicelineitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxInvoiceLineItem 1", 24500.00, 150.0, "ACTIVE", "uuid-taxinvoicelineitem-01"),
    (2, "TAX-0002", "Secondary Corporate TaxInvoiceLineItem 2", 18200.50, 80.0, "ACTIVE", "uuid-taxinvoicelineitem-02"),
    (3, "TAX-0003", "Consolidated Branch TaxInvoiceLineItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxinvoicelineitem-03"),
    (4, "TAX-0004", "Enterprise Audited TaxInvoiceLineItem 4", 32800.00, 210.0, "ACTIVE", "uuid-taxinvoicelineitem-04"),
    (5, "TAX-0005", "Executive Strategic TaxInvoiceLineItem 5", 65000.00, 400.0, "ACTIVE", "uuid-taxinvoicelineitem-05");

CREATE TABLE IF NOT EXISTS tax_engine_inputtaxcreditledgers (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_inputtaxcreditledgers_code ON tax_engine_inputtaxcreditledgers(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_inputtaxcreditledgers_org_status ON tax_engine_inputtaxcreditledgers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_inputtaxcreditledgers_priority ON tax_engine_inputtaxcreditledgers(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_inputtaxcreditledgers_created_at ON tax_engine_inputtaxcreditledgers(created_at);

-- Operational seed data fixtures for tax_engine_inputtaxcreditledgers
INSERT OR IGNORE INTO tax_engine_inputtaxcreditledgers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INP-0001", "Primary Operational InputTaxCreditLedger 1", 24500.00, 150.0, "ACTIVE", "uuid-inputtaxcreditledger-01"),
    (2, "INP-0002", "Secondary Corporate InputTaxCreditLedger 2", 18200.50, 80.0, "ACTIVE", "uuid-inputtaxcreditledger-02"),
    (3, "INP-0003", "Consolidated Branch InputTaxCreditLedger 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inputtaxcreditledger-03"),
    (4, "INP-0004", "Enterprise Audited InputTaxCreditLedger 4", 32800.00, 210.0, "ACTIVE", "uuid-inputtaxcreditledger-04"),
    (5, "INP-0005", "Executive Strategic InputTaxCreditLedger 5", 65000.00, 400.0, "ACTIVE", "uuid-inputtaxcreditledger-05");

CREATE TABLE IF NOT EXISTS tax_engine_monthlytaxreturngstrs (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_monthlytaxreturngstrs_code ON tax_engine_monthlytaxreturngstrs(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_monthlytaxreturngstrs_org_status ON tax_engine_monthlytaxreturngstrs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_monthlytaxreturngstrs_priority ON tax_engine_monthlytaxreturngstrs(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_monthlytaxreturngstrs_created_at ON tax_engine_monthlytaxreturngstrs(created_at);

-- Operational seed data fixtures for tax_engine_monthlytaxreturngstrs
INSERT OR IGNORE INTO tax_engine_monthlytaxreturngstrs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MON-0001", "Primary Operational MonthlyTaxReturnGSTR 1", 24500.00, 150.0, "ACTIVE", "uuid-monthlytaxreturngstr-01"),
    (2, "MON-0002", "Secondary Corporate MonthlyTaxReturnGSTR 2", 18200.50, 80.0, "ACTIVE", "uuid-monthlytaxreturngstr-02"),
    (3, "MON-0003", "Consolidated Branch MonthlyTaxReturnGSTR 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-monthlytaxreturngstr-03"),
    (4, "MON-0004", "Enterprise Audited MonthlyTaxReturnGSTR 4", 32800.00, 210.0, "ACTIVE", "uuid-monthlytaxreturngstr-04"),
    (5, "MON-0005", "Executive Strategic MonthlyTaxReturnGSTR 5", 65000.00, 400.0, "ACTIVE", "uuid-monthlytaxreturngstr-05");

CREATE TABLE IF NOT EXISTS tax_engine_annualtaxreconciliations (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_annualtaxreconciliations_code ON tax_engine_annualtaxreconciliations(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_annualtaxreconciliations_org_status ON tax_engine_annualtaxreconciliations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_annualtaxreconciliations_priority ON tax_engine_annualtaxreconciliations(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_annualtaxreconciliations_created_at ON tax_engine_annualtaxreconciliations(created_at);

-- Operational seed data fixtures for tax_engine_annualtaxreconciliations
INSERT OR IGNORE INTO tax_engine_annualtaxreconciliations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ANN-0001", "Primary Operational AnnualTaxReconciliation 1", 24500.00, 150.0, "ACTIVE", "uuid-annualtaxreconciliation-01"),
    (2, "ANN-0002", "Secondary Corporate AnnualTaxReconciliation 2", 18200.50, 80.0, "ACTIVE", "uuid-annualtaxreconciliation-02"),
    (3, "ANN-0003", "Consolidated Branch AnnualTaxReconciliation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-annualtaxreconciliation-03"),
    (4, "ANN-0004", "Enterprise Audited AnnualTaxReconciliation 4", 32800.00, 210.0, "ACTIVE", "uuid-annualtaxreconciliation-04"),
    (5, "ANN-0005", "Executive Strategic AnnualTaxReconciliation 5", 65000.00, 400.0, "ACTIVE", "uuid-annualtaxreconciliation-05");

CREATE TABLE IF NOT EXISTS tax_engine_taxaudittrails (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_taxaudittrails_code ON tax_engine_taxaudittrails(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxaudittrails_org_status ON tax_engine_taxaudittrails(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxaudittrails_priority ON tax_engine_taxaudittrails(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxaudittrails_created_at ON tax_engine_taxaudittrails(created_at);

-- Operational seed data fixtures for tax_engine_taxaudittrails
INSERT OR IGNORE INTO tax_engine_taxaudittrails (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxAuditTrail 1", 24500.00, 150.0, "ACTIVE", "uuid-taxaudittrail-01"),
    (2, "TAX-0002", "Secondary Corporate TaxAuditTrail 2", 18200.50, 80.0, "ACTIVE", "uuid-taxaudittrail-02"),
    (3, "TAX-0003", "Consolidated Branch TaxAuditTrail 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxaudittrail-03"),
    (4, "TAX-0004", "Enterprise Audited TaxAuditTrail 4", 32800.00, 210.0, "ACTIVE", "uuid-taxaudittrail-04"),
    (5, "TAX-0005", "Executive Strategic TaxAuditTrail 5", 65000.00, 400.0, "ACTIVE", "uuid-taxaudittrail-05");

CREATE TABLE IF NOT EXISTS tax_engine_ewaybillrecords (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_ewaybillrecords_code ON tax_engine_ewaybillrecords(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_ewaybillrecords_org_status ON tax_engine_ewaybillrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_ewaybillrecords_priority ON tax_engine_ewaybillrecords(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_ewaybillrecords_created_at ON tax_engine_ewaybillrecords(created_at);

-- Operational seed data fixtures for tax_engine_ewaybillrecords
INSERT OR IGNORE INTO tax_engine_ewaybillrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EWA-0001", "Primary Operational EWayBillRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-ewaybillrecord-01"),
    (2, "EWA-0002", "Secondary Corporate EWayBillRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-ewaybillrecord-02"),
    (3, "EWA-0003", "Consolidated Branch EWayBillRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ewaybillrecord-03"),
    (4, "EWA-0004", "Enterprise Audited EWayBillRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-ewaybillrecord-04"),
    (5, "EWA-0005", "Executive Strategic EWayBillRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-ewaybillrecord-05");

CREATE TABLE IF NOT EXISTS tax_engine_einvoiceirnregistrys (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_einvoiceirnregistrys_code ON tax_engine_einvoiceirnregistrys(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_einvoiceirnregistrys_org_status ON tax_engine_einvoiceirnregistrys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_einvoiceirnregistrys_priority ON tax_engine_einvoiceirnregistrys(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_einvoiceirnregistrys_created_at ON tax_engine_einvoiceirnregistrys(created_at);

-- Operational seed data fixtures for tax_engine_einvoiceirnregistrys
INSERT OR IGNORE INTO tax_engine_einvoiceirnregistrys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EIN-0001", "Primary Operational EInvoiceIRNRegistry 1", 24500.00, 150.0, "ACTIVE", "uuid-einvoiceirnregistry-01"),
    (2, "EIN-0002", "Secondary Corporate EInvoiceIRNRegistry 2", 18200.50, 80.0, "ACTIVE", "uuid-einvoiceirnregistry-02"),
    (3, "EIN-0003", "Consolidated Branch EInvoiceIRNRegistry 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-einvoiceirnregistry-03"),
    (4, "EIN-0004", "Enterprise Audited EInvoiceIRNRegistry 4", 32800.00, 210.0, "ACTIVE", "uuid-einvoiceirnregistry-04"),
    (5, "EIN-0005", "Executive Strategic EInvoiceIRNRegistry 5", 65000.00, 400.0, "ACTIVE", "uuid-einvoiceirnregistry-05");

CREATE TABLE IF NOT EXISTS tax_engine_taxpenaltynotices (
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

CREATE INDEX IF NOT EXISTS idx_tax_engine_taxpenaltynotices_code ON tax_engine_taxpenaltynotices(code);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxpenaltynotices_org_status ON tax_engine_taxpenaltynotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxpenaltynotices_priority ON tax_engine_taxpenaltynotices(priority);
CREATE INDEX IF NOT EXISTS idx_tax_engine_taxpenaltynotices_created_at ON tax_engine_taxpenaltynotices(created_at);

-- Operational seed data fixtures for tax_engine_taxpenaltynotices
INSERT OR IGNORE INTO tax_engine_taxpenaltynotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxPenaltyNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-taxpenaltynotice-01"),
    (2, "TAX-0002", "Secondary Corporate TaxPenaltyNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-taxpenaltynotice-02"),
    (3, "TAX-0003", "Consolidated Branch TaxPenaltyNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxpenaltynotice-03"),
    (4, "TAX-0004", "Enterprise Audited TaxPenaltyNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-taxpenaltynotice-04"),
    (5, "TAX-0005", "Executive Strategic TaxPenaltyNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-taxpenaltynotice-05");

