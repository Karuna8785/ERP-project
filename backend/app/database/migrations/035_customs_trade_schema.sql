-- SmartERP Enterprise Titan Migration 035: Global Trade Compliance & Customs Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS customs_trade_customsdeclarationforms (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_customsdeclarationforms_code ON customs_trade_customsdeclarationforms(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_customsdeclarationforms_org_status ON customs_trade_customsdeclarationforms(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_customsdeclarationforms_priority ON customs_trade_customsdeclarationforms(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_customsdeclarationforms_created_at ON customs_trade_customsdeclarationforms(created_at);

-- Operational seed data fixtures for customs_trade_customsdeclarationforms
INSERT OR IGNORE INTO customs_trade_customsdeclarationforms (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomsDeclarationForm 1", 24500.00, 150.0, "ACTIVE", "uuid-customsdeclarationform-01"),
    (2, "CUS-0002", "Secondary Corporate CustomsDeclarationForm 2", 18200.50, 80.0, "ACTIVE", "uuid-customsdeclarationform-02"),
    (3, "CUS-0003", "Consolidated Branch CustomsDeclarationForm 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customsdeclarationform-03"),
    (4, "CUS-0004", "Enterprise Audited CustomsDeclarationForm 4", 32800.00, 210.0, "ACTIVE", "uuid-customsdeclarationform-04"),
    (5, "CUS-0005", "Executive Strategic CustomsDeclarationForm 5", 65000.00, 400.0, "ACTIVE", "uuid-customsdeclarationform-05");

CREATE TABLE IF NOT EXISTS customs_trade_harmonizedtariffschedules (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_harmonizedtariffschedules_code ON customs_trade_harmonizedtariffschedules(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_harmonizedtariffschedules_org_status ON customs_trade_harmonizedtariffschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_harmonizedtariffschedules_priority ON customs_trade_harmonizedtariffschedules(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_harmonizedtariffschedules_created_at ON customs_trade_harmonizedtariffschedules(created_at);

-- Operational seed data fixtures for customs_trade_harmonizedtariffschedules
INSERT OR IGNORE INTO customs_trade_harmonizedtariffschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HAR-0001", "Primary Operational HarmonizedTariffSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-harmonizedtariffschedule-01"),
    (2, "HAR-0002", "Secondary Corporate HarmonizedTariffSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-harmonizedtariffschedule-02"),
    (3, "HAR-0003", "Consolidated Branch HarmonizedTariffSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-harmonizedtariffschedule-03"),
    (4, "HAR-0004", "Enterprise Audited HarmonizedTariffSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-harmonizedtariffschedule-04"),
    (5, "HAR-0005", "Executive Strategic HarmonizedTariffSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-harmonizedtariffschedule-05");

CREATE TABLE IF NOT EXISTS customs_trade_countryoforigincerts (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_countryoforigincerts_code ON customs_trade_countryoforigincerts(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_countryoforigincerts_org_status ON customs_trade_countryoforigincerts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_countryoforigincerts_priority ON customs_trade_countryoforigincerts(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_countryoforigincerts_created_at ON customs_trade_countryoforigincerts(created_at);

-- Operational seed data fixtures for customs_trade_countryoforigincerts
INSERT OR IGNORE INTO customs_trade_countryoforigincerts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COU-0001", "Primary Operational CountryOfOriginCert 1", 24500.00, 150.0, "ACTIVE", "uuid-countryoforigincert-01"),
    (2, "COU-0002", "Secondary Corporate CountryOfOriginCert 2", 18200.50, 80.0, "ACTIVE", "uuid-countryoforigincert-02"),
    (3, "COU-0003", "Consolidated Branch CountryOfOriginCert 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-countryoforigincert-03"),
    (4, "COU-0004", "Enterprise Audited CountryOfOriginCert 4", 32800.00, 210.0, "ACTIVE", "uuid-countryoforigincert-04"),
    (5, "COU-0005", "Executive Strategic CountryOfOriginCert 5", 65000.00, 400.0, "ACTIVE", "uuid-countryoforigincert-05");

CREATE TABLE IF NOT EXISTS customs_trade_exportcontrolclassifications (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_exportcontrolclassifications_code ON customs_trade_exportcontrolclassifications(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_exportcontrolclassifications_org_status ON customs_trade_exportcontrolclassifications(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_exportcontrolclassifications_priority ON customs_trade_exportcontrolclassifications(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_exportcontrolclassifications_created_at ON customs_trade_exportcontrolclassifications(created_at);

-- Operational seed data fixtures for customs_trade_exportcontrolclassifications
INSERT OR IGNORE INTO customs_trade_exportcontrolclassifications (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExportControlClassification 1", 24500.00, 150.0, "ACTIVE", "uuid-exportcontrolclassification-01"),
    (2, "EXP-0002", "Secondary Corporate ExportControlClassification 2", 18200.50, 80.0, "ACTIVE", "uuid-exportcontrolclassification-02"),
    (3, "EXP-0003", "Consolidated Branch ExportControlClassification 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-exportcontrolclassification-03"),
    (4, "EXP-0004", "Enterprise Audited ExportControlClassification 4", 32800.00, 210.0, "ACTIVE", "uuid-exportcontrolclassification-04"),
    (5, "EXP-0005", "Executive Strategic ExportControlClassification 5", 65000.00, 400.0, "ACTIVE", "uuid-exportcontrolclassification-05");

CREATE TABLE IF NOT EXISTS customs_trade_sanctionpartyscreenings (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_sanctionpartyscreenings_code ON customs_trade_sanctionpartyscreenings(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_sanctionpartyscreenings_org_status ON customs_trade_sanctionpartyscreenings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_sanctionpartyscreenings_priority ON customs_trade_sanctionpartyscreenings(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_sanctionpartyscreenings_created_at ON customs_trade_sanctionpartyscreenings(created_at);

-- Operational seed data fixtures for customs_trade_sanctionpartyscreenings
INSERT OR IGNORE INTO customs_trade_sanctionpartyscreenings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SAN-0001", "Primary Operational SanctionPartyScreening 1", 24500.00, 150.0, "ACTIVE", "uuid-sanctionpartyscreening-01"),
    (2, "SAN-0002", "Secondary Corporate SanctionPartyScreening 2", 18200.50, 80.0, "ACTIVE", "uuid-sanctionpartyscreening-02"),
    (3, "SAN-0003", "Consolidated Branch SanctionPartyScreening 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-sanctionpartyscreening-03"),
    (4, "SAN-0004", "Enterprise Audited SanctionPartyScreening 4", 32800.00, 210.0, "ACTIVE", "uuid-sanctionpartyscreening-04"),
    (5, "SAN-0005", "Executive Strategic SanctionPartyScreening 5", 65000.00, 400.0, "ACTIVE", "uuid-sanctionpartyscreening-05");

CREATE TABLE IF NOT EXISTS customs_trade_importdutyassessments (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_importdutyassessments_code ON customs_trade_importdutyassessments(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_importdutyassessments_org_status ON customs_trade_importdutyassessments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_importdutyassessments_priority ON customs_trade_importdutyassessments(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_importdutyassessments_created_at ON customs_trade_importdutyassessments(created_at);

-- Operational seed data fixtures for customs_trade_importdutyassessments
INSERT OR IGNORE INTO customs_trade_importdutyassessments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "IMP-0001", "Primary Operational ImportDutyAssessment 1", 24500.00, 150.0, "ACTIVE", "uuid-importdutyassessment-01"),
    (2, "IMP-0002", "Secondary Corporate ImportDutyAssessment 2", 18200.50, 80.0, "ACTIVE", "uuid-importdutyassessment-02"),
    (3, "IMP-0003", "Consolidated Branch ImportDutyAssessment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-importdutyassessment-03"),
    (4, "IMP-0004", "Enterprise Audited ImportDutyAssessment 4", 32800.00, 210.0, "ACTIVE", "uuid-importdutyassessment-04"),
    (5, "IMP-0005", "Executive Strategic ImportDutyAssessment 5", 65000.00, 400.0, "ACTIVE", "uuid-importdutyassessment-05");

CREATE TABLE IF NOT EXISTS customs_trade_freetradeagreementclaims (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_freetradeagreementclaims_code ON customs_trade_freetradeagreementclaims(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_freetradeagreementclaims_org_status ON customs_trade_freetradeagreementclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_freetradeagreementclaims_priority ON customs_trade_freetradeagreementclaims(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_freetradeagreementclaims_created_at ON customs_trade_freetradeagreementclaims(created_at);

-- Operational seed data fixtures for customs_trade_freetradeagreementclaims
INSERT OR IGNORE INTO customs_trade_freetradeagreementclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FRE-0001", "Primary Operational FreeTradeAgreementClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-freetradeagreementclaim-01"),
    (2, "FRE-0002", "Secondary Corporate FreeTradeAgreementClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-freetradeagreementclaim-02"),
    (3, "FRE-0003", "Consolidated Branch FreeTradeAgreementClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-freetradeagreementclaim-03"),
    (4, "FRE-0004", "Enterprise Audited FreeTradeAgreementClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-freetradeagreementclaim-04"),
    (5, "FRE-0005", "Executive Strategic FreeTradeAgreementClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-freetradeagreementclaim-05");

CREATE TABLE IF NOT EXISTS customs_trade_bondedwarehouselogs (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_bondedwarehouselogs_code ON customs_trade_bondedwarehouselogs(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_bondedwarehouselogs_org_status ON customs_trade_bondedwarehouselogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_bondedwarehouselogs_priority ON customs_trade_bondedwarehouselogs(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_bondedwarehouselogs_created_at ON customs_trade_bondedwarehouselogs(created_at);

-- Operational seed data fixtures for customs_trade_bondedwarehouselogs
INSERT OR IGNORE INTO customs_trade_bondedwarehouselogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BON-0001", "Primary Operational BondedWarehouseLog 1", 24500.00, 150.0, "ACTIVE", "uuid-bondedwarehouselog-01"),
    (2, "BON-0002", "Secondary Corporate BondedWarehouseLog 2", 18200.50, 80.0, "ACTIVE", "uuid-bondedwarehouselog-02"),
    (3, "BON-0003", "Consolidated Branch BondedWarehouseLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bondedwarehouselog-03"),
    (4, "BON-0004", "Enterprise Audited BondedWarehouseLog 4", 32800.00, 210.0, "ACTIVE", "uuid-bondedwarehouselog-04"),
    (5, "BON-0005", "Executive Strategic BondedWarehouseLog 5", 65000.00, 400.0, "ACTIVE", "uuid-bondedwarehouselog-05");

CREATE TABLE IF NOT EXISTS customs_trade_antidumpingmeasures (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_antidumpingmeasures_code ON customs_trade_antidumpingmeasures(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_antidumpingmeasures_org_status ON customs_trade_antidumpingmeasures(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_antidumpingmeasures_priority ON customs_trade_antidumpingmeasures(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_antidumpingmeasures_created_at ON customs_trade_antidumpingmeasures(created_at);

-- Operational seed data fixtures for customs_trade_antidumpingmeasures
INSERT OR IGNORE INTO customs_trade_antidumpingmeasures (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ANT-0001", "Primary Operational AntiDumpingMeasure 1", 24500.00, 150.0, "ACTIVE", "uuid-antidumpingmeasure-01"),
    (2, "ANT-0002", "Secondary Corporate AntiDumpingMeasure 2", 18200.50, 80.0, "ACTIVE", "uuid-antidumpingmeasure-02"),
    (3, "ANT-0003", "Consolidated Branch AntiDumpingMeasure 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-antidumpingmeasure-03"),
    (4, "ANT-0004", "Enterprise Audited AntiDumpingMeasure 4", 32800.00, 210.0, "ACTIVE", "uuid-antidumpingmeasure-04"),
    (5, "ANT-0005", "Executive Strategic AntiDumpingMeasure 5", 65000.00, 400.0, "ACTIVE", "uuid-antidumpingmeasure-05");

CREATE TABLE IF NOT EXISTS customs_trade_carnetguarantees (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_carnetguarantees_code ON customs_trade_carnetguarantees(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_carnetguarantees_org_status ON customs_trade_carnetguarantees(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_carnetguarantees_priority ON customs_trade_carnetguarantees(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_carnetguarantees_created_at ON customs_trade_carnetguarantees(created_at);

-- Operational seed data fixtures for customs_trade_carnetguarantees
INSERT OR IGNORE INTO customs_trade_carnetguarantees (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAR-0001", "Primary Operational CarnetGuarantee 1", 24500.00, 150.0, "ACTIVE", "uuid-carnetguarantee-01"),
    (2, "CAR-0002", "Secondary Corporate CarnetGuarantee 2", 18200.50, 80.0, "ACTIVE", "uuid-carnetguarantee-02"),
    (3, "CAR-0003", "Consolidated Branch CarnetGuarantee 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-carnetguarantee-03"),
    (4, "CAR-0004", "Enterprise Audited CarnetGuarantee 4", 32800.00, 210.0, "ACTIVE", "uuid-carnetguarantee-04"),
    (5, "CAR-0005", "Executive Strategic CarnetGuarantee 5", 65000.00, 400.0, "ACTIVE", "uuid-carnetguarantee-05");

CREATE TABLE IF NOT EXISTS customs_trade_customsbrokerengagements (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_customsbrokerengagements_code ON customs_trade_customsbrokerengagements(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_customsbrokerengagements_org_status ON customs_trade_customsbrokerengagements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_customsbrokerengagements_priority ON customs_trade_customsbrokerengagements(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_customsbrokerengagements_created_at ON customs_trade_customsbrokerengagements(created_at);

-- Operational seed data fixtures for customs_trade_customsbrokerengagements
INSERT OR IGNORE INTO customs_trade_customsbrokerengagements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomsBrokerEngagement 1", 24500.00, 150.0, "ACTIVE", "uuid-customsbrokerengagement-01"),
    (2, "CUS-0002", "Secondary Corporate CustomsBrokerEngagement 2", 18200.50, 80.0, "ACTIVE", "uuid-customsbrokerengagement-02"),
    (3, "CUS-0003", "Consolidated Branch CustomsBrokerEngagement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customsbrokerengagement-03"),
    (4, "CUS-0004", "Enterprise Audited CustomsBrokerEngagement 4", 32800.00, 210.0, "ACTIVE", "uuid-customsbrokerengagement-04"),
    (5, "CUS-0005", "Executive Strategic CustomsBrokerEngagement 5", 65000.00, 400.0, "ACTIVE", "uuid-customsbrokerengagement-05");

CREATE TABLE IF NOT EXISTS customs_trade_letterofcreditcustomss (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_letterofcreditcustomss_code ON customs_trade_letterofcreditcustomss(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_letterofcreditcustomss_org_status ON customs_trade_letterofcreditcustomss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_letterofcreditcustomss_priority ON customs_trade_letterofcreditcustomss(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_letterofcreditcustomss_created_at ON customs_trade_letterofcreditcustomss(created_at);

-- Operational seed data fixtures for customs_trade_letterofcreditcustomss
INSERT OR IGNORE INTO customs_trade_letterofcreditcustomss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LET-0001", "Primary Operational LetterOfCreditCustoms 1", 24500.00, 150.0, "ACTIVE", "uuid-letterofcreditcustoms-01"),
    (2, "LET-0002", "Secondary Corporate LetterOfCreditCustoms 2", 18200.50, 80.0, "ACTIVE", "uuid-letterofcreditcustoms-02"),
    (3, "LET-0003", "Consolidated Branch LetterOfCreditCustoms 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-letterofcreditcustoms-03"),
    (4, "LET-0004", "Enterprise Audited LetterOfCreditCustoms 4", 32800.00, 210.0, "ACTIVE", "uuid-letterofcreditcustoms-04"),
    (5, "LET-0005", "Executive Strategic LetterOfCreditCustoms 5", 65000.00, 400.0, "ACTIVE", "uuid-letterofcreditcustoms-05");

CREATE TABLE IF NOT EXISTS customs_trade_tariffpreferencerules (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_tariffpreferencerules_code ON customs_trade_tariffpreferencerules(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_tariffpreferencerules_org_status ON customs_trade_tariffpreferencerules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_tariffpreferencerules_priority ON customs_trade_tariffpreferencerules(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_tariffpreferencerules_created_at ON customs_trade_tariffpreferencerules(created_at);

-- Operational seed data fixtures for customs_trade_tariffpreferencerules
INSERT OR IGNORE INTO customs_trade_tariffpreferencerules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAR-0001", "Primary Operational TariffPreferenceRule 1", 24500.00, 150.0, "ACTIVE", "uuid-tariffpreferencerule-01"),
    (2, "TAR-0002", "Secondary Corporate TariffPreferenceRule 2", 18200.50, 80.0, "ACTIVE", "uuid-tariffpreferencerule-02"),
    (3, "TAR-0003", "Consolidated Branch TariffPreferenceRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tariffpreferencerule-03"),
    (4, "TAR-0004", "Enterprise Audited TariffPreferenceRule 4", 32800.00, 210.0, "ACTIVE", "uuid-tariffpreferencerule-04"),
    (5, "TAR-0005", "Executive Strategic TariffPreferenceRule 5", 65000.00, 400.0, "ACTIVE", "uuid-tariffpreferencerule-05");

CREATE TABLE IF NOT EXISTS customs_trade_tradedisputefilings (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_tradedisputefilings_code ON customs_trade_tradedisputefilings(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_tradedisputefilings_org_status ON customs_trade_tradedisputefilings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_tradedisputefilings_priority ON customs_trade_tradedisputefilings(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_tradedisputefilings_created_at ON customs_trade_tradedisputefilings(created_at);

-- Operational seed data fixtures for customs_trade_tradedisputefilings
INSERT OR IGNORE INTO customs_trade_tradedisputefilings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TradeDisputeFiling 1", 24500.00, 150.0, "ACTIVE", "uuid-tradedisputefiling-01"),
    (2, "TRA-0002", "Secondary Corporate TradeDisputeFiling 2", 18200.50, 80.0, "ACTIVE", "uuid-tradedisputefiling-02"),
    (3, "TRA-0003", "Consolidated Branch TradeDisputeFiling 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tradedisputefiling-03"),
    (4, "TRA-0004", "Enterprise Audited TradeDisputeFiling 4", 32800.00, 210.0, "ACTIVE", "uuid-tradedisputefiling-04"),
    (5, "TRA-0005", "Executive Strategic TradeDisputeFiling 5", 65000.00, 400.0, "ACTIVE", "uuid-tradedisputefiling-05");

CREATE TABLE IF NOT EXISTS customs_trade_inspectionreleaseorders (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_inspectionreleaseorders_code ON customs_trade_inspectionreleaseorders(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_inspectionreleaseorders_org_status ON customs_trade_inspectionreleaseorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_inspectionreleaseorders_priority ON customs_trade_inspectionreleaseorders(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_inspectionreleaseorders_created_at ON customs_trade_inspectionreleaseorders(created_at);

-- Operational seed data fixtures for customs_trade_inspectionreleaseorders
INSERT OR IGNORE INTO customs_trade_inspectionreleaseorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INS-0001", "Primary Operational InspectionReleaseOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-inspectionreleaseorder-01"),
    (2, "INS-0002", "Secondary Corporate InspectionReleaseOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-inspectionreleaseorder-02"),
    (3, "INS-0003", "Consolidated Branch InspectionReleaseOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inspectionreleaseorder-03"),
    (4, "INS-0004", "Enterprise Audited InspectionReleaseOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-inspectionreleaseorder-04"),
    (5, "INS-0005", "Executive Strategic InspectionReleaseOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-inspectionreleaseorder-05");

CREATE TABLE IF NOT EXISTS customs_trade_dutydrawbackclaims (
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

CREATE INDEX IF NOT EXISTS idx_customs_trade_dutydrawbackclaims_code ON customs_trade_dutydrawbackclaims(code);
CREATE INDEX IF NOT EXISTS idx_customs_trade_dutydrawbackclaims_org_status ON customs_trade_dutydrawbackclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_customs_trade_dutydrawbackclaims_priority ON customs_trade_dutydrawbackclaims(priority);
CREATE INDEX IF NOT EXISTS idx_customs_trade_dutydrawbackclaims_created_at ON customs_trade_dutydrawbackclaims(created_at);

-- Operational seed data fixtures for customs_trade_dutydrawbackclaims
INSERT OR IGNORE INTO customs_trade_dutydrawbackclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DUT-0001", "Primary Operational DutyDrawbackClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-dutydrawbackclaim-01"),
    (2, "DUT-0002", "Secondary Corporate DutyDrawbackClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-dutydrawbackclaim-02"),
    (3, "DUT-0003", "Consolidated Branch DutyDrawbackClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dutydrawbackclaim-03"),
    (4, "DUT-0004", "Enterprise Audited DutyDrawbackClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-dutydrawbackclaim-04"),
    (5, "DUT-0005", "Executive Strategic DutyDrawbackClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-dutydrawbackclaim-05");

