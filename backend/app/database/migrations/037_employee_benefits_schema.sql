-- SmartERP Enterprise Titan Migration 037: Employee Total Rewards & Benefits Administration DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS employee_benefits_benefitplandefinitions (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitplandefinitions_code ON employee_benefits_benefitplandefinitions(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitplandefinitions_org_status ON employee_benefits_benefitplandefinitions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitplandefinitions_priority ON employee_benefits_benefitplandefinitions(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitplandefinitions_created_at ON employee_benefits_benefitplandefinitions(created_at);

-- Operational seed data fixtures for employee_benefits_benefitplandefinitions
INSERT OR IGNORE INTO employee_benefits_benefitplandefinitions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BEN-0001", "Primary Operational BenefitPlanDefinition 1", 24500.00, 150.0, "ACTIVE", "uuid-benefitplandefinition-01"),
    (2, "BEN-0002", "Secondary Corporate BenefitPlanDefinition 2", 18200.50, 80.0, "ACTIVE", "uuid-benefitplandefinition-02"),
    (3, "BEN-0003", "Consolidated Branch BenefitPlanDefinition 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-benefitplandefinition-03"),
    (4, "BEN-0004", "Enterprise Audited BenefitPlanDefinition 4", 32800.00, 210.0, "ACTIVE", "uuid-benefitplandefinition-04"),
    (5, "BEN-0005", "Executive Strategic BenefitPlanDefinition 5", 65000.00, 400.0, "ACTIVE", "uuid-benefitplandefinition-05");

CREATE TABLE IF NOT EXISTS employee_benefits_employeeenrollmentrecords (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeenrollmentrecords_code ON employee_benefits_employeeenrollmentrecords(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeenrollmentrecords_org_status ON employee_benefits_employeeenrollmentrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeenrollmentrecords_priority ON employee_benefits_employeeenrollmentrecords(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeenrollmentrecords_created_at ON employee_benefits_employeeenrollmentrecords(created_at);

-- Operational seed data fixtures for employee_benefits_employeeenrollmentrecords
INSERT OR IGNORE INTO employee_benefits_employeeenrollmentrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EMP-0001", "Primary Operational EmployeeEnrollmentRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-employeeenrollmentrecord-01"),
    (2, "EMP-0002", "Secondary Corporate EmployeeEnrollmentRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-employeeenrollmentrecord-02"),
    (3, "EMP-0003", "Consolidated Branch EmployeeEnrollmentRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-employeeenrollmentrecord-03"),
    (4, "EMP-0004", "Enterprise Audited EmployeeEnrollmentRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-employeeenrollmentrecord-04"),
    (5, "EMP-0005", "Executive Strategic EmployeeEnrollmentRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-employeeenrollmentrecord-05");

CREATE TABLE IF NOT EXISTS employee_benefits_healthinsurancepolicys (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_healthinsurancepolicys_code ON employee_benefits_healthinsurancepolicys(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_healthinsurancepolicys_org_status ON employee_benefits_healthinsurancepolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_healthinsurancepolicys_priority ON employee_benefits_healthinsurancepolicys(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_healthinsurancepolicys_created_at ON employee_benefits_healthinsurancepolicys(created_at);

-- Operational seed data fixtures for employee_benefits_healthinsurancepolicys
INSERT OR IGNORE INTO employee_benefits_healthinsurancepolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HEA-0001", "Primary Operational HealthInsurancePolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-healthinsurancepolicy-01"),
    (2, "HEA-0002", "Secondary Corporate HealthInsurancePolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-healthinsurancepolicy-02"),
    (3, "HEA-0003", "Consolidated Branch HealthInsurancePolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-healthinsurancepolicy-03"),
    (4, "HEA-0004", "Enterprise Audited HealthInsurancePolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-healthinsurancepolicy-04"),
    (5, "HEA-0005", "Executive Strategic HealthInsurancePolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-healthinsurancepolicy-05");

CREATE TABLE IF NOT EXISTS employee_benefits_retirementpensionfunds (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_retirementpensionfunds_code ON employee_benefits_retirementpensionfunds(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_retirementpensionfunds_org_status ON employee_benefits_retirementpensionfunds(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_retirementpensionfunds_priority ON employee_benefits_retirementpensionfunds(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_retirementpensionfunds_created_at ON employee_benefits_retirementpensionfunds(created_at);

-- Operational seed data fixtures for employee_benefits_retirementpensionfunds
INSERT OR IGNORE INTO employee_benefits_retirementpensionfunds (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational RetirementPensionFund 1", 24500.00, 150.0, "ACTIVE", "uuid-retirementpensionfund-01"),
    (2, "RET-0002", "Secondary Corporate RetirementPensionFund 2", 18200.50, 80.0, "ACTIVE", "uuid-retirementpensionfund-02"),
    (3, "RET-0003", "Consolidated Branch RetirementPensionFund 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-retirementpensionfund-03"),
    (4, "RET-0004", "Enterprise Audited RetirementPensionFund 4", 32800.00, 210.0, "ACTIVE", "uuid-retirementpensionfund-04"),
    (5, "RET-0005", "Executive Strategic RetirementPensionFund 5", 65000.00, 400.0, "ACTIVE", "uuid-retirementpensionfund-05");

CREATE TABLE IF NOT EXISTS employee_benefits_wellnessreimbursements (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_wellnessreimbursements_code ON employee_benefits_wellnessreimbursements(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_wellnessreimbursements_org_status ON employee_benefits_wellnessreimbursements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_wellnessreimbursements_priority ON employee_benefits_wellnessreimbursements(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_wellnessreimbursements_created_at ON employee_benefits_wellnessreimbursements(created_at);

-- Operational seed data fixtures for employee_benefits_wellnessreimbursements
INSERT OR IGNORE INTO employee_benefits_wellnessreimbursements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WEL-0001", "Primary Operational WellnessReimbursement 1", 24500.00, 150.0, "ACTIVE", "uuid-wellnessreimbursement-01"),
    (2, "WEL-0002", "Secondary Corporate WellnessReimbursement 2", 18200.50, 80.0, "ACTIVE", "uuid-wellnessreimbursement-02"),
    (3, "WEL-0003", "Consolidated Branch WellnessReimbursement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-wellnessreimbursement-03"),
    (4, "WEL-0004", "Enterprise Audited WellnessReimbursement 4", 32800.00, 210.0, "ACTIVE", "uuid-wellnessreimbursement-04"),
    (5, "WEL-0005", "Executive Strategic WellnessReimbursement 5", 65000.00, 400.0, "ACTIVE", "uuid-wellnessreimbursement-05");

CREATE TABLE IF NOT EXISTS employee_benefits_lifeinsurancecoverages (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_lifeinsurancecoverages_code ON employee_benefits_lifeinsurancecoverages(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_lifeinsurancecoverages_org_status ON employee_benefits_lifeinsurancecoverages(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_lifeinsurancecoverages_priority ON employee_benefits_lifeinsurancecoverages(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_lifeinsurancecoverages_created_at ON employee_benefits_lifeinsurancecoverages(created_at);

-- Operational seed data fixtures for employee_benefits_lifeinsurancecoverages
INSERT OR IGNORE INTO employee_benefits_lifeinsurancecoverages (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LIF-0001", "Primary Operational LifeInsuranceCoverage 1", 24500.00, 150.0, "ACTIVE", "uuid-lifeinsurancecoverage-01"),
    (2, "LIF-0002", "Secondary Corporate LifeInsuranceCoverage 2", 18200.50, 80.0, "ACTIVE", "uuid-lifeinsurancecoverage-02"),
    (3, "LIF-0003", "Consolidated Branch LifeInsuranceCoverage 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-lifeinsurancecoverage-03"),
    (4, "LIF-0004", "Enterprise Audited LifeInsuranceCoverage 4", 32800.00, 210.0, "ACTIVE", "uuid-lifeinsurancecoverage-04"),
    (5, "LIF-0005", "Executive Strategic LifeInsuranceCoverage 5", 65000.00, 400.0, "ACTIVE", "uuid-lifeinsurancecoverage-05");

CREATE TABLE IF NOT EXISTS employee_benefits_flexiblespendingaccounts (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_flexiblespendingaccounts_code ON employee_benefits_flexiblespendingaccounts(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_flexiblespendingaccounts_org_status ON employee_benefits_flexiblespendingaccounts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_flexiblespendingaccounts_priority ON employee_benefits_flexiblespendingaccounts(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_flexiblespendingaccounts_created_at ON employee_benefits_flexiblespendingaccounts(created_at);

-- Operational seed data fixtures for employee_benefits_flexiblespendingaccounts
INSERT OR IGNORE INTO employee_benefits_flexiblespendingaccounts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FLE-0001", "Primary Operational FlexibleSpendingAccount 1", 24500.00, 150.0, "ACTIVE", "uuid-flexiblespendingaccount-01"),
    (2, "FLE-0002", "Secondary Corporate FlexibleSpendingAccount 2", 18200.50, 80.0, "ACTIVE", "uuid-flexiblespendingaccount-02"),
    (3, "FLE-0003", "Consolidated Branch FlexibleSpendingAccount 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-flexiblespendingaccount-03"),
    (4, "FLE-0004", "Enterprise Audited FlexibleSpendingAccount 4", 32800.00, 210.0, "ACTIVE", "uuid-flexiblespendingaccount-04"),
    (5, "FLE-0005", "Executive Strategic FlexibleSpendingAccount 5", 65000.00, 400.0, "ACTIVE", "uuid-flexiblespendingaccount-05");

CREATE TABLE IF NOT EXISTS employee_benefits_dependentbeneficiarys (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_dependentbeneficiarys_code ON employee_benefits_dependentbeneficiarys(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_dependentbeneficiarys_org_status ON employee_benefits_dependentbeneficiarys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_dependentbeneficiarys_priority ON employee_benefits_dependentbeneficiarys(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_dependentbeneficiarys_created_at ON employee_benefits_dependentbeneficiarys(created_at);

-- Operational seed data fixtures for employee_benefits_dependentbeneficiarys
INSERT OR IGNORE INTO employee_benefits_dependentbeneficiarys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEP-0001", "Primary Operational DependentBeneficiary 1", 24500.00, 150.0, "ACTIVE", "uuid-dependentbeneficiary-01"),
    (2, "DEP-0002", "Secondary Corporate DependentBeneficiary 2", 18200.50, 80.0, "ACTIVE", "uuid-dependentbeneficiary-02"),
    (3, "DEP-0003", "Consolidated Branch DependentBeneficiary 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dependentbeneficiary-03"),
    (4, "DEP-0004", "Enterprise Audited DependentBeneficiary 4", 32800.00, 210.0, "ACTIVE", "uuid-dependentbeneficiary-04"),
    (5, "DEP-0005", "Executive Strategic DependentBeneficiary 5", 65000.00, 400.0, "ACTIVE", "uuid-dependentbeneficiary-05");

CREATE TABLE IF NOT EXISTS employee_benefits_benefitclaimsubmissions (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitclaimsubmissions_code ON employee_benefits_benefitclaimsubmissions(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitclaimsubmissions_org_status ON employee_benefits_benefitclaimsubmissions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitclaimsubmissions_priority ON employee_benefits_benefitclaimsubmissions(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitclaimsubmissions_created_at ON employee_benefits_benefitclaimsubmissions(created_at);

-- Operational seed data fixtures for employee_benefits_benefitclaimsubmissions
INSERT OR IGNORE INTO employee_benefits_benefitclaimsubmissions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BEN-0001", "Primary Operational BenefitClaimSubmission 1", 24500.00, 150.0, "ACTIVE", "uuid-benefitclaimsubmission-01"),
    (2, "BEN-0002", "Secondary Corporate BenefitClaimSubmission 2", 18200.50, 80.0, "ACTIVE", "uuid-benefitclaimsubmission-02"),
    (3, "BEN-0003", "Consolidated Branch BenefitClaimSubmission 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-benefitclaimsubmission-03"),
    (4, "BEN-0004", "Enterprise Audited BenefitClaimSubmission 4", 32800.00, 210.0, "ACTIVE", "uuid-benefitclaimsubmission-04"),
    (5, "BEN-0005", "Executive Strategic BenefitClaimSubmission 5", 65000.00, 400.0, "ACTIVE", "uuid-benefitclaimsubmission-05");

CREATE TABLE IF NOT EXISTS employee_benefits_deductionpayrollmaps (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_deductionpayrollmaps_code ON employee_benefits_deductionpayrollmaps(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_deductionpayrollmaps_org_status ON employee_benefits_deductionpayrollmaps(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_deductionpayrollmaps_priority ON employee_benefits_deductionpayrollmaps(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_deductionpayrollmaps_created_at ON employee_benefits_deductionpayrollmaps(created_at);

-- Operational seed data fixtures for employee_benefits_deductionpayrollmaps
INSERT OR IGNORE INTO employee_benefits_deductionpayrollmaps (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DED-0001", "Primary Operational DeductionPayrollMap 1", 24500.00, 150.0, "ACTIVE", "uuid-deductionpayrollmap-01"),
    (2, "DED-0002", "Secondary Corporate DeductionPayrollMap 2", 18200.50, 80.0, "ACTIVE", "uuid-deductionpayrollmap-02"),
    (3, "DED-0003", "Consolidated Branch DeductionPayrollMap 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-deductionpayrollmap-03"),
    (4, "DED-0004", "Enterprise Audited DeductionPayrollMap 4", 32800.00, 210.0, "ACTIVE", "uuid-deductionpayrollmap-04"),
    (5, "DED-0005", "Executive Strategic DeductionPayrollMap 5", 65000.00, 400.0, "ACTIVE", "uuid-deductionpayrollmap-05");

CREATE TABLE IF NOT EXISTS employee_benefits_openenrollmentwindows (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_openenrollmentwindows_code ON employee_benefits_openenrollmentwindows(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_openenrollmentwindows_org_status ON employee_benefits_openenrollmentwindows(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_openenrollmentwindows_priority ON employee_benefits_openenrollmentwindows(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_openenrollmentwindows_created_at ON employee_benefits_openenrollmentwindows(created_at);

-- Operational seed data fixtures for employee_benefits_openenrollmentwindows
INSERT OR IGNORE INTO employee_benefits_openenrollmentwindows (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OPE-0001", "Primary Operational OpenEnrollmentWindow 1", 24500.00, 150.0, "ACTIVE", "uuid-openenrollmentwindow-01"),
    (2, "OPE-0002", "Secondary Corporate OpenEnrollmentWindow 2", 18200.50, 80.0, "ACTIVE", "uuid-openenrollmentwindow-02"),
    (3, "OPE-0003", "Consolidated Branch OpenEnrollmentWindow 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-openenrollmentwindow-03"),
    (4, "OPE-0004", "Enterprise Audited OpenEnrollmentWindow 4", 32800.00, 210.0, "ACTIVE", "uuid-openenrollmentwindow-04"),
    (5, "OPE-0005", "Executive Strategic OpenEnrollmentWindow 5", 65000.00, 400.0, "ACTIVE", "uuid-openenrollmentwindow-05");

CREATE TABLE IF NOT EXISTS employee_benefits_carrierbillingreconciles (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_carrierbillingreconciles_code ON employee_benefits_carrierbillingreconciles(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_carrierbillingreconciles_org_status ON employee_benefits_carrierbillingreconciles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_carrierbillingreconciles_priority ON employee_benefits_carrierbillingreconciles(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_carrierbillingreconciles_created_at ON employee_benefits_carrierbillingreconciles(created_at);

-- Operational seed data fixtures for employee_benefits_carrierbillingreconciles
INSERT OR IGNORE INTO employee_benefits_carrierbillingreconciles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAR-0001", "Primary Operational CarrierBillingReconcile 1", 24500.00, 150.0, "ACTIVE", "uuid-carrierbillingreconcile-01"),
    (2, "CAR-0002", "Secondary Corporate CarrierBillingReconcile 2", 18200.50, 80.0, "ACTIVE", "uuid-carrierbillingreconcile-02"),
    (3, "CAR-0003", "Consolidated Branch CarrierBillingReconcile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-carrierbillingreconcile-03"),
    (4, "CAR-0004", "Enterprise Audited CarrierBillingReconcile 4", 32800.00, 210.0, "ACTIVE", "uuid-carrierbillingreconcile-04"),
    (5, "CAR-0005", "Executive Strategic CarrierBillingReconcile 5", 65000.00, 400.0, "ACTIVE", "uuid-carrierbillingreconcile-05");

CREATE TABLE IF NOT EXISTS employee_benefits_cobracontinuationlogs (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_cobracontinuationlogs_code ON employee_benefits_cobracontinuationlogs(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_cobracontinuationlogs_org_status ON employee_benefits_cobracontinuationlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_cobracontinuationlogs_priority ON employee_benefits_cobracontinuationlogs(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_cobracontinuationlogs_created_at ON employee_benefits_cobracontinuationlogs(created_at);

-- Operational seed data fixtures for employee_benefits_cobracontinuationlogs
INSERT OR IGNORE INTO employee_benefits_cobracontinuationlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COB-0001", "Primary Operational COBRAContinuationLog 1", 24500.00, 150.0, "ACTIVE", "uuid-cobracontinuationlog-01"),
    (2, "COB-0002", "Secondary Corporate COBRAContinuationLog 2", 18200.50, 80.0, "ACTIVE", "uuid-cobracontinuationlog-02"),
    (3, "COB-0003", "Consolidated Branch COBRAContinuationLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cobracontinuationlog-03"),
    (4, "COB-0004", "Enterprise Audited COBRAContinuationLog 4", 32800.00, 210.0, "ACTIVE", "uuid-cobracontinuationlog-04"),
    (5, "COB-0005", "Executive Strategic COBRAContinuationLog 5", 65000.00, 400.0, "ACTIVE", "uuid-cobracontinuationlog-05");

CREATE TABLE IF NOT EXISTS employee_benefits_employeeassistanceprogs (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeassistanceprogs_code ON employee_benefits_employeeassistanceprogs(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeassistanceprogs_org_status ON employee_benefits_employeeassistanceprogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeassistanceprogs_priority ON employee_benefits_employeeassistanceprogs(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_employeeassistanceprogs_created_at ON employee_benefits_employeeassistanceprogs(created_at);

-- Operational seed data fixtures for employee_benefits_employeeassistanceprogs
INSERT OR IGNORE INTO employee_benefits_employeeassistanceprogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EMP-0001", "Primary Operational EmployeeAssistanceProg 1", 24500.00, 150.0, "ACTIVE", "uuid-employeeassistanceprog-01"),
    (2, "EMP-0002", "Secondary Corporate EmployeeAssistanceProg 2", 18200.50, 80.0, "ACTIVE", "uuid-employeeassistanceprog-02"),
    (3, "EMP-0003", "Consolidated Branch EmployeeAssistanceProg 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-employeeassistanceprog-03"),
    (4, "EMP-0004", "Enterprise Audited EmployeeAssistanceProg 4", 32800.00, 210.0, "ACTIVE", "uuid-employeeassistanceprog-04"),
    (5, "EMP-0005", "Executive Strategic EmployeeAssistanceProg 5", 65000.00, 400.0, "ACTIVE", "uuid-employeeassistanceprog-05");

CREATE TABLE IF NOT EXISTS employee_benefits_voluntarybenefitoptions (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_voluntarybenefitoptions_code ON employee_benefits_voluntarybenefitoptions(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_voluntarybenefitoptions_org_status ON employee_benefits_voluntarybenefitoptions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_voluntarybenefitoptions_priority ON employee_benefits_voluntarybenefitoptions(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_voluntarybenefitoptions_created_at ON employee_benefits_voluntarybenefitoptions(created_at);

-- Operational seed data fixtures for employee_benefits_voluntarybenefitoptions
INSERT OR IGNORE INTO employee_benefits_voluntarybenefitoptions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "VOL-0001", "Primary Operational VoluntaryBenefitOption 1", 24500.00, 150.0, "ACTIVE", "uuid-voluntarybenefitoption-01"),
    (2, "VOL-0002", "Secondary Corporate VoluntaryBenefitOption 2", 18200.50, 80.0, "ACTIVE", "uuid-voluntarybenefitoption-02"),
    (3, "VOL-0003", "Consolidated Branch VoluntaryBenefitOption 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-voluntarybenefitoption-03"),
    (4, "VOL-0004", "Enterprise Audited VoluntaryBenefitOption 4", 32800.00, 210.0, "ACTIVE", "uuid-voluntarybenefitoption-04"),
    (5, "VOL-0005", "Executive Strategic VoluntaryBenefitOption 5", 65000.00, 400.0, "ACTIVE", "uuid-voluntarybenefitoption-05");

CREATE TABLE IF NOT EXISTS employee_benefits_benefitcostanalyticss (
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

CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitcostanalyticss_code ON employee_benefits_benefitcostanalyticss(code);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitcostanalyticss_org_status ON employee_benefits_benefitcostanalyticss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitcostanalyticss_priority ON employee_benefits_benefitcostanalyticss(priority);
CREATE INDEX IF NOT EXISTS idx_employee_benefits_benefitcostanalyticss_created_at ON employee_benefits_benefitcostanalyticss(created_at);

-- Operational seed data fixtures for employee_benefits_benefitcostanalyticss
INSERT OR IGNORE INTO employee_benefits_benefitcostanalyticss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BEN-0001", "Primary Operational BenefitCostAnalytics 1", 24500.00, 150.0, "ACTIVE", "uuid-benefitcostanalytics-01"),
    (2, "BEN-0002", "Secondary Corporate BenefitCostAnalytics 2", 18200.50, 80.0, "ACTIVE", "uuid-benefitcostanalytics-02"),
    (3, "BEN-0003", "Consolidated Branch BenefitCostAnalytics 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-benefitcostanalytics-03"),
    (4, "BEN-0004", "Enterprise Audited BenefitCostAnalytics 4", 32800.00, 210.0, "ACTIVE", "uuid-benefitcostanalytics-04"),
    (5, "BEN-0005", "Executive Strategic BenefitCostAnalytics 5", 65000.00, 400.0, "ACTIVE", "uuid-benefitcostanalytics-05");

