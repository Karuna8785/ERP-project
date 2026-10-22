-- SmartERP Enterprise Titan Migration 012: Human Capital & Talent Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS human_capital_jobopenings (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_jobopenings_code ON human_capital_jobopenings(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_jobopenings_org_status ON human_capital_jobopenings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_jobopenings_priority ON human_capital_jobopenings(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_jobopenings_created_at ON human_capital_jobopenings(created_at);

-- Operational seed data fixtures for human_capital_jobopenings
INSERT OR IGNORE INTO human_capital_jobopenings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "JOB-0001", "Primary Operational JobOpening 1", 24500.00, 150.0, "ACTIVE", "uuid-jobopening-01"),
    (2, "JOB-0002", "Secondary Corporate JobOpening 2", 18200.50, 80.0, "ACTIVE", "uuid-jobopening-02"),
    (3, "JOB-0003", "Consolidated Branch JobOpening 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-jobopening-03"),
    (4, "JOB-0004", "Enterprise Audited JobOpening 4", 32800.00, 210.0, "ACTIVE", "uuid-jobopening-04"),
    (5, "JOB-0005", "Executive Strategic JobOpening 5", 65000.00, 400.0, "ACTIVE", "uuid-jobopening-05");

CREATE TABLE IF NOT EXISTS human_capital_candidateprofiles (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_candidateprofiles_code ON human_capital_candidateprofiles(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_candidateprofiles_org_status ON human_capital_candidateprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_candidateprofiles_priority ON human_capital_candidateprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_candidateprofiles_created_at ON human_capital_candidateprofiles(created_at);

-- Operational seed data fixtures for human_capital_candidateprofiles
INSERT OR IGNORE INTO human_capital_candidateprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAN-0001", "Primary Operational CandidateProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-candidateprofile-01"),
    (2, "CAN-0002", "Secondary Corporate CandidateProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-candidateprofile-02"),
    (3, "CAN-0003", "Consolidated Branch CandidateProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-candidateprofile-03"),
    (4, "CAN-0004", "Enterprise Audited CandidateProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-candidateprofile-04"),
    (5, "CAN-0005", "Executive Strategic CandidateProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-candidateprofile-05");

CREATE TABLE IF NOT EXISTS human_capital_interviewschedules (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_interviewschedules_code ON human_capital_interviewschedules(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_interviewschedules_org_status ON human_capital_interviewschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_interviewschedules_priority ON human_capital_interviewschedules(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_interviewschedules_created_at ON human_capital_interviewschedules(created_at);

-- Operational seed data fixtures for human_capital_interviewschedules
INSERT OR IGNORE INTO human_capital_interviewschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INT-0001", "Primary Operational InterviewSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-interviewschedule-01"),
    (2, "INT-0002", "Secondary Corporate InterviewSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-interviewschedule-02"),
    (3, "INT-0003", "Consolidated Branch InterviewSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-interviewschedule-03"),
    (4, "INT-0004", "Enterprise Audited InterviewSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-interviewschedule-04"),
    (5, "INT-0005", "Executive Strategic InterviewSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-interviewschedule-05");

CREATE TABLE IF NOT EXISTS human_capital_offerletters (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_offerletters_code ON human_capital_offerletters(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_offerletters_org_status ON human_capital_offerletters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_offerletters_priority ON human_capital_offerletters(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_offerletters_created_at ON human_capital_offerletters(created_at);

-- Operational seed data fixtures for human_capital_offerletters
INSERT OR IGNORE INTO human_capital_offerletters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OFF-0001", "Primary Operational OfferLetter 1", 24500.00, 150.0, "ACTIVE", "uuid-offerletter-01"),
    (2, "OFF-0002", "Secondary Corporate OfferLetter 2", 18200.50, 80.0, "ACTIVE", "uuid-offerletter-02"),
    (3, "OFF-0003", "Consolidated Branch OfferLetter 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-offerletter-03"),
    (4, "OFF-0004", "Enterprise Audited OfferLetter 4", 32800.00, 210.0, "ACTIVE", "uuid-offerletter-04"),
    (5, "OFF-0005", "Executive Strategic OfferLetter 5", 65000.00, 400.0, "ACTIVE", "uuid-offerletter-05");

CREATE TABLE IF NOT EXISTS human_capital_onboardingchecklists (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_onboardingchecklists_code ON human_capital_onboardingchecklists(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_onboardingchecklists_org_status ON human_capital_onboardingchecklists(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_onboardingchecklists_priority ON human_capital_onboardingchecklists(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_onboardingchecklists_created_at ON human_capital_onboardingchecklists(created_at);

-- Operational seed data fixtures for human_capital_onboardingchecklists
INSERT OR IGNORE INTO human_capital_onboardingchecklists (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ONB-0001", "Primary Operational OnboardingChecklist 1", 24500.00, 150.0, "ACTIVE", "uuid-onboardingchecklist-01"),
    (2, "ONB-0002", "Secondary Corporate OnboardingChecklist 2", 18200.50, 80.0, "ACTIVE", "uuid-onboardingchecklist-02"),
    (3, "ONB-0003", "Consolidated Branch OnboardingChecklist 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-onboardingchecklist-03"),
    (4, "ONB-0004", "Enterprise Audited OnboardingChecklist 4", 32800.00, 210.0, "ACTIVE", "uuid-onboardingchecklist-04"),
    (5, "ONB-0005", "Executive Strategic OnboardingChecklist 5", 65000.00, 400.0, "ACTIVE", "uuid-onboardingchecklist-05");

CREATE TABLE IF NOT EXISTS human_capital_employeetrainingcourses (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_employeetrainingcourses_code ON human_capital_employeetrainingcourses(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_employeetrainingcourses_org_status ON human_capital_employeetrainingcourses(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_employeetrainingcourses_priority ON human_capital_employeetrainingcourses(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_employeetrainingcourses_created_at ON human_capital_employeetrainingcourses(created_at);

-- Operational seed data fixtures for human_capital_employeetrainingcourses
INSERT OR IGNORE INTO human_capital_employeetrainingcourses (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EMP-0001", "Primary Operational EmployeeTrainingCourse 1", 24500.00, 150.0, "ACTIVE", "uuid-employeetrainingcourse-01"),
    (2, "EMP-0002", "Secondary Corporate EmployeeTrainingCourse 2", 18200.50, 80.0, "ACTIVE", "uuid-employeetrainingcourse-02"),
    (3, "EMP-0003", "Consolidated Branch EmployeeTrainingCourse 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-employeetrainingcourse-03"),
    (4, "EMP-0004", "Enterprise Audited EmployeeTrainingCourse 4", 32800.00, 210.0, "ACTIVE", "uuid-employeetrainingcourse-04"),
    (5, "EMP-0005", "Executive Strategic EmployeeTrainingCourse 5", 65000.00, 400.0, "ACTIVE", "uuid-employeetrainingcourse-05");

CREATE TABLE IF NOT EXISTS human_capital_certificationrecords (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_certificationrecords_code ON human_capital_certificationrecords(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_certificationrecords_org_status ON human_capital_certificationrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_certificationrecords_priority ON human_capital_certificationrecords(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_certificationrecords_created_at ON human_capital_certificationrecords(created_at);

-- Operational seed data fixtures for human_capital_certificationrecords
INSERT OR IGNORE INTO human_capital_certificationrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CER-0001", "Primary Operational CertificationRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-certificationrecord-01"),
    (2, "CER-0002", "Secondary Corporate CertificationRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-certificationrecord-02"),
    (3, "CER-0003", "Consolidated Branch CertificationRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-certificationrecord-03"),
    (4, "CER-0004", "Enterprise Audited CertificationRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-certificationrecord-04"),
    (5, "CER-0005", "Executive Strategic CertificationRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-certificationrecord-05");

CREATE TABLE IF NOT EXISTS human_capital_successionplans (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_successionplans_code ON human_capital_successionplans(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_successionplans_org_status ON human_capital_successionplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_successionplans_priority ON human_capital_successionplans(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_successionplans_created_at ON human_capital_successionplans(created_at);

-- Operational seed data fixtures for human_capital_successionplans
INSERT OR IGNORE INTO human_capital_successionplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUC-0001", "Primary Operational SuccessionPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-successionplan-01"),
    (2, "SUC-0002", "Secondary Corporate SuccessionPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-successionplan-02"),
    (3, "SUC-0003", "Consolidated Branch SuccessionPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-successionplan-03"),
    (4, "SUC-0004", "Enterprise Audited SuccessionPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-successionplan-04"),
    (5, "SUC-0005", "Executive Strategic SuccessionPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-successionplan-05");

CREATE TABLE IF NOT EXISTS human_capital_performanceobjectives (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_performanceobjectives_code ON human_capital_performanceobjectives(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_performanceobjectives_org_status ON human_capital_performanceobjectives(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_performanceobjectives_priority ON human_capital_performanceobjectives(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_performanceobjectives_created_at ON human_capital_performanceobjectives(created_at);

-- Operational seed data fixtures for human_capital_performanceobjectives
INSERT OR IGNORE INTO human_capital_performanceobjectives (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PER-0001", "Primary Operational PerformanceObjective 1", 24500.00, 150.0, "ACTIVE", "uuid-performanceobjective-01"),
    (2, "PER-0002", "Secondary Corporate PerformanceObjective 2", 18200.50, 80.0, "ACTIVE", "uuid-performanceobjective-02"),
    (3, "PER-0003", "Consolidated Branch PerformanceObjective 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-performanceobjective-03"),
    (4, "PER-0004", "Enterprise Audited PerformanceObjective 4", 32800.00, 210.0, "ACTIVE", "uuid-performanceobjective-04"),
    (5, "PER-0005", "Executive Strategic PerformanceObjective 5", 65000.00, 400.0, "ACTIVE", "uuid-performanceobjective-05");

CREATE TABLE IF NOT EXISTS human_capital_peerreviewfeedbacks (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_peerreviewfeedbacks_code ON human_capital_peerreviewfeedbacks(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_peerreviewfeedbacks_org_status ON human_capital_peerreviewfeedbacks(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_peerreviewfeedbacks_priority ON human_capital_peerreviewfeedbacks(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_peerreviewfeedbacks_created_at ON human_capital_peerreviewfeedbacks(created_at);

-- Operational seed data fixtures for human_capital_peerreviewfeedbacks
INSERT OR IGNORE INTO human_capital_peerreviewfeedbacks (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PEE-0001", "Primary Operational PeerReviewFeedback 1", 24500.00, 150.0, "ACTIVE", "uuid-peerreviewfeedback-01"),
    (2, "PEE-0002", "Secondary Corporate PeerReviewFeedback 2", 18200.50, 80.0, "ACTIVE", "uuid-peerreviewfeedback-02"),
    (3, "PEE-0003", "Consolidated Branch PeerReviewFeedback 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-peerreviewfeedback-03"),
    (4, "PEE-0004", "Enterprise Audited PeerReviewFeedback 4", 32800.00, 210.0, "ACTIVE", "uuid-peerreviewfeedback-04"),
    (5, "PEE-0005", "Executive Strategic PeerReviewFeedback 5", 65000.00, 400.0, "ACTIVE", "uuid-peerreviewfeedback-05");

CREATE TABLE IF NOT EXISTS human_capital_disciplinaryactions (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_disciplinaryactions_code ON human_capital_disciplinaryactions(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_disciplinaryactions_org_status ON human_capital_disciplinaryactions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_disciplinaryactions_priority ON human_capital_disciplinaryactions(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_disciplinaryactions_created_at ON human_capital_disciplinaryactions(created_at);

-- Operational seed data fixtures for human_capital_disciplinaryactions
INSERT OR IGNORE INTO human_capital_disciplinaryactions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DisciplinaryAction 1", 24500.00, 150.0, "ACTIVE", "uuid-disciplinaryaction-01"),
    (2, "DIS-0002", "Secondary Corporate DisciplinaryAction 2", 18200.50, 80.0, "ACTIVE", "uuid-disciplinaryaction-02"),
    (3, "DIS-0003", "Consolidated Branch DisciplinaryAction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-disciplinaryaction-03"),
    (4, "DIS-0004", "Enterprise Audited DisciplinaryAction 4", 32800.00, 210.0, "ACTIVE", "uuid-disciplinaryaction-04"),
    (5, "DIS-0005", "Executive Strategic DisciplinaryAction 5", 65000.00, 400.0, "ACTIVE", "uuid-disciplinaryaction-05");

CREATE TABLE IF NOT EXISTS human_capital_healthsafetyincidents (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_healthsafetyincidents_code ON human_capital_healthsafetyincidents(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_healthsafetyincidents_org_status ON human_capital_healthsafetyincidents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_healthsafetyincidents_priority ON human_capital_healthsafetyincidents(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_healthsafetyincidents_created_at ON human_capital_healthsafetyincidents(created_at);

-- Operational seed data fixtures for human_capital_healthsafetyincidents
INSERT OR IGNORE INTO human_capital_healthsafetyincidents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HEA-0001", "Primary Operational HealthSafetyIncident 1", 24500.00, 150.0, "ACTIVE", "uuid-healthsafetyincident-01"),
    (2, "HEA-0002", "Secondary Corporate HealthSafetyIncident 2", 18200.50, 80.0, "ACTIVE", "uuid-healthsafetyincident-02"),
    (3, "HEA-0003", "Consolidated Branch HealthSafetyIncident 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-healthsafetyincident-03"),
    (4, "HEA-0004", "Enterprise Audited HealthSafetyIncident 4", 32800.00, 210.0, "ACTIVE", "uuid-healthsafetyincident-04"),
    (5, "HEA-0005", "Executive Strategic HealthSafetyIncident 5", 65000.00, 400.0, "ACTIVE", "uuid-healthsafetyincident-05");

CREATE TABLE IF NOT EXISTS human_capital_exitinterviews (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_exitinterviews_code ON human_capital_exitinterviews(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_exitinterviews_org_status ON human_capital_exitinterviews(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_exitinterviews_priority ON human_capital_exitinterviews(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_exitinterviews_created_at ON human_capital_exitinterviews(created_at);

-- Operational seed data fixtures for human_capital_exitinterviews
INSERT OR IGNORE INTO human_capital_exitinterviews (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXI-0001", "Primary Operational ExitInterview 1", 24500.00, 150.0, "ACTIVE", "uuid-exitinterview-01"),
    (2, "EXI-0002", "Secondary Corporate ExitInterview 2", 18200.50, 80.0, "ACTIVE", "uuid-exitinterview-02"),
    (3, "EXI-0003", "Consolidated Branch ExitInterview 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-exitinterview-03"),
    (4, "EXI-0004", "Enterprise Audited ExitInterview 4", 32800.00, 210.0, "ACTIVE", "uuid-exitinterview-04"),
    (5, "EXI-0005", "Executive Strategic ExitInterview 5", 65000.00, 400.0, "ACTIVE", "uuid-exitinterview-05");

CREATE TABLE IF NOT EXISTS human_capital_orghierarchynodes (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_orghierarchynodes_code ON human_capital_orghierarchynodes(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_orghierarchynodes_org_status ON human_capital_orghierarchynodes(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_orghierarchynodes_priority ON human_capital_orghierarchynodes(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_orghierarchynodes_created_at ON human_capital_orghierarchynodes(created_at);

-- Operational seed data fixtures for human_capital_orghierarchynodes
INSERT OR IGNORE INTO human_capital_orghierarchynodes (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ORG-0001", "Primary Operational OrgHierarchyNode 1", 24500.00, 150.0, "ACTIVE", "uuid-orghierarchynode-01"),
    (2, "ORG-0002", "Secondary Corporate OrgHierarchyNode 2", 18200.50, 80.0, "ACTIVE", "uuid-orghierarchynode-02"),
    (3, "ORG-0003", "Consolidated Branch OrgHierarchyNode 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-orghierarchynode-03"),
    (4, "ORG-0004", "Enterprise Audited OrgHierarchyNode 4", 32800.00, 210.0, "ACTIVE", "uuid-orghierarchynode-04"),
    (5, "ORG-0005", "Executive Strategic OrgHierarchyNode 5", 65000.00, 400.0, "ACTIVE", "uuid-orghierarchynode-05");

CREATE TABLE IF NOT EXISTS human_capital_compensationbands (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_compensationbands_code ON human_capital_compensationbands(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_compensationbands_org_status ON human_capital_compensationbands(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_compensationbands_priority ON human_capital_compensationbands(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_compensationbands_created_at ON human_capital_compensationbands(created_at);

-- Operational seed data fixtures for human_capital_compensationbands
INSERT OR IGNORE INTO human_capital_compensationbands (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CompensationBand 1", 24500.00, 150.0, "ACTIVE", "uuid-compensationband-01"),
    (2, "COM-0002", "Secondary Corporate CompensationBand 2", 18200.50, 80.0, "ACTIVE", "uuid-compensationband-02"),
    (3, "COM-0003", "Consolidated Branch CompensationBand 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-compensationband-03"),
    (4, "COM-0004", "Enterprise Audited CompensationBand 4", 32800.00, 210.0, "ACTIVE", "uuid-compensationband-04"),
    (5, "COM-0005", "Executive Strategic CompensationBand 5", 65000.00, 400.0, "ACTIVE", "uuid-compensationband-05");

CREATE TABLE IF NOT EXISTS human_capital_employeesurveys (
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

CREATE INDEX IF NOT EXISTS idx_human_capital_employeesurveys_code ON human_capital_employeesurveys(code);
CREATE INDEX IF NOT EXISTS idx_human_capital_employeesurveys_org_status ON human_capital_employeesurveys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_human_capital_employeesurveys_priority ON human_capital_employeesurveys(priority);
CREATE INDEX IF NOT EXISTS idx_human_capital_employeesurveys_created_at ON human_capital_employeesurveys(created_at);

-- Operational seed data fixtures for human_capital_employeesurveys
INSERT OR IGNORE INTO human_capital_employeesurveys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EMP-0001", "Primary Operational EmployeeSurvey 1", 24500.00, 150.0, "ACTIVE", "uuid-employeesurvey-01"),
    (2, "EMP-0002", "Secondary Corporate EmployeeSurvey 2", 18200.50, 80.0, "ACTIVE", "uuid-employeesurvey-02"),
    (3, "EMP-0003", "Consolidated Branch EmployeeSurvey 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-employeesurvey-03"),
    (4, "EMP-0004", "Enterprise Audited EmployeeSurvey 4", 32800.00, 210.0, "ACTIVE", "uuid-employeesurvey-04"),
    (5, "EMP-0005", "Executive Strategic EmployeeSurvey 5", 65000.00, 400.0, "ACTIVE", "uuid-employeesurvey-05");

