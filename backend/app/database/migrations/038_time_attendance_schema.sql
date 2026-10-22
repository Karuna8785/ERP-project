-- SmartERP Enterprise Titan Migration 038: Time, Attendance & Workforce Scheduling DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS time_attendance_biometricclockpunchs (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_biometricclockpunchs_code ON time_attendance_biometricclockpunchs(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_biometricclockpunchs_org_status ON time_attendance_biometricclockpunchs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_biometricclockpunchs_priority ON time_attendance_biometricclockpunchs(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_biometricclockpunchs_created_at ON time_attendance_biometricclockpunchs(created_at);

-- Operational seed data fixtures for time_attendance_biometricclockpunchs
INSERT OR IGNORE INTO time_attendance_biometricclockpunchs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BIO-0001", "Primary Operational BiometricClockPunch 1", 24500.00, 150.0, "ACTIVE", "uuid-biometricclockpunch-01"),
    (2, "BIO-0002", "Secondary Corporate BiometricClockPunch 2", 18200.50, 80.0, "ACTIVE", "uuid-biometricclockpunch-02"),
    (3, "BIO-0003", "Consolidated Branch BiometricClockPunch 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-biometricclockpunch-03"),
    (4, "BIO-0004", "Enterprise Audited BiometricClockPunch 4", 32800.00, 210.0, "ACTIVE", "uuid-biometricclockpunch-04"),
    (5, "BIO-0005", "Executive Strategic BiometricClockPunch 5", 65000.00, 400.0, "ACTIVE", "uuid-biometricclockpunch-05");

CREATE TABLE IF NOT EXISTS time_attendance_shiftrosterschedules (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftrosterschedules_code ON time_attendance_shiftrosterschedules(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftrosterschedules_org_status ON time_attendance_shiftrosterschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftrosterschedules_priority ON time_attendance_shiftrosterschedules(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftrosterschedules_created_at ON time_attendance_shiftrosterschedules(created_at);

-- Operational seed data fixtures for time_attendance_shiftrosterschedules
INSERT OR IGNORE INTO time_attendance_shiftrosterschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational ShiftRosterSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-shiftrosterschedule-01"),
    (2, "SHI-0002", "Secondary Corporate ShiftRosterSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-shiftrosterschedule-02"),
    (3, "SHI-0003", "Consolidated Branch ShiftRosterSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shiftrosterschedule-03"),
    (4, "SHI-0004", "Enterprise Audited ShiftRosterSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-shiftrosterschedule-04"),
    (5, "SHI-0005", "Executive Strategic ShiftRosterSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-shiftrosterschedule-05");

CREATE TABLE IF NOT EXISTS time_attendance_attendancedailyrecords (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_attendancedailyrecords_code ON time_attendance_attendancedailyrecords(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_attendancedailyrecords_org_status ON time_attendance_attendancedailyrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_attendancedailyrecords_priority ON time_attendance_attendancedailyrecords(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_attendancedailyrecords_created_at ON time_attendance_attendancedailyrecords(created_at);

-- Operational seed data fixtures for time_attendance_attendancedailyrecords
INSERT OR IGNORE INTO time_attendance_attendancedailyrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ATT-0001", "Primary Operational AttendanceDailyRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-attendancedailyrecord-01"),
    (2, "ATT-0002", "Secondary Corporate AttendanceDailyRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-attendancedailyrecord-02"),
    (3, "ATT-0003", "Consolidated Branch AttendanceDailyRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-attendancedailyrecord-03"),
    (4, "ATT-0004", "Enterprise Audited AttendanceDailyRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-attendancedailyrecord-04"),
    (5, "ATT-0005", "Executive Strategic AttendanceDailyRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-attendancedailyrecord-05");

CREATE TABLE IF NOT EXISTS time_attendance_overtimepreapprovals (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_overtimepreapprovals_code ON time_attendance_overtimepreapprovals(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_overtimepreapprovals_org_status ON time_attendance_overtimepreapprovals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_overtimepreapprovals_priority ON time_attendance_overtimepreapprovals(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_overtimepreapprovals_created_at ON time_attendance_overtimepreapprovals(created_at);

-- Operational seed data fixtures for time_attendance_overtimepreapprovals
INSERT OR IGNORE INTO time_attendance_overtimepreapprovals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OVE-0001", "Primary Operational OvertimePreApproval 1", 24500.00, 150.0, "ACTIVE", "uuid-overtimepreapproval-01"),
    (2, "OVE-0002", "Secondary Corporate OvertimePreApproval 2", 18200.50, 80.0, "ACTIVE", "uuid-overtimepreapproval-02"),
    (3, "OVE-0003", "Consolidated Branch OvertimePreApproval 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-overtimepreapproval-03"),
    (4, "OVE-0004", "Enterprise Audited OvertimePreApproval 4", 32800.00, 210.0, "ACTIVE", "uuid-overtimepreapproval-04"),
    (5, "OVE-0005", "Executive Strategic OvertimePreApproval 5", 65000.00, 400.0, "ACTIVE", "uuid-overtimepreapproval-05");

CREATE TABLE IF NOT EXISTS time_attendance_breaktimeintervals (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_breaktimeintervals_code ON time_attendance_breaktimeintervals(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_breaktimeintervals_org_status ON time_attendance_breaktimeintervals(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_breaktimeintervals_priority ON time_attendance_breaktimeintervals(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_breaktimeintervals_created_at ON time_attendance_breaktimeintervals(created_at);

-- Operational seed data fixtures for time_attendance_breaktimeintervals
INSERT OR IGNORE INTO time_attendance_breaktimeintervals (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BRE-0001", "Primary Operational BreakTimeInterval 1", 24500.00, 150.0, "ACTIVE", "uuid-breaktimeinterval-01"),
    (2, "BRE-0002", "Secondary Corporate BreakTimeInterval 2", 18200.50, 80.0, "ACTIVE", "uuid-breaktimeinterval-02"),
    (3, "BRE-0003", "Consolidated Branch BreakTimeInterval 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-breaktimeinterval-03"),
    (4, "BRE-0004", "Enterprise Audited BreakTimeInterval 4", 32800.00, 210.0, "ACTIVE", "uuid-breaktimeinterval-04"),
    (5, "BRE-0005", "Executive Strategic BreakTimeInterval 5", 65000.00, 400.0, "ACTIVE", "uuid-breaktimeinterval-05");

CREATE TABLE IF NOT EXISTS time_attendance_publicholidaycalendars (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_publicholidaycalendars_code ON time_attendance_publicholidaycalendars(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_publicholidaycalendars_org_status ON time_attendance_publicholidaycalendars(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_publicholidaycalendars_priority ON time_attendance_publicholidaycalendars(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_publicholidaycalendars_created_at ON time_attendance_publicholidaycalendars(created_at);

-- Operational seed data fixtures for time_attendance_publicholidaycalendars
INSERT OR IGNORE INTO time_attendance_publicholidaycalendars (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PUB-0001", "Primary Operational PublicHolidayCalendar 1", 24500.00, 150.0, "ACTIVE", "uuid-publicholidaycalendar-01"),
    (2, "PUB-0002", "Secondary Corporate PublicHolidayCalendar 2", 18200.50, 80.0, "ACTIVE", "uuid-publicholidaycalendar-02"),
    (3, "PUB-0003", "Consolidated Branch PublicHolidayCalendar 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-publicholidaycalendar-03"),
    (4, "PUB-0004", "Enterprise Audited PublicHolidayCalendar 4", 32800.00, 210.0, "ACTIVE", "uuid-publicholidaycalendar-04"),
    (5, "PUB-0005", "Executive Strategic PublicHolidayCalendar 5", 65000.00, 400.0, "ACTIVE", "uuid-publicholidaycalendar-05");

CREATE TABLE IF NOT EXISTS time_attendance_compoffentitlements (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_compoffentitlements_code ON time_attendance_compoffentitlements(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_compoffentitlements_org_status ON time_attendance_compoffentitlements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_compoffentitlements_priority ON time_attendance_compoffentitlements(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_compoffentitlements_created_at ON time_attendance_compoffentitlements(created_at);

-- Operational seed data fixtures for time_attendance_compoffentitlements
INSERT OR IGNORE INTO time_attendance_compoffentitlements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COM-0001", "Primary Operational CompOffEntitlement 1", 24500.00, 150.0, "ACTIVE", "uuid-compoffentitlement-01"),
    (2, "COM-0002", "Secondary Corporate CompOffEntitlement 2", 18200.50, 80.0, "ACTIVE", "uuid-compoffentitlement-02"),
    (3, "COM-0003", "Consolidated Branch CompOffEntitlement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-compoffentitlement-03"),
    (4, "COM-0004", "Enterprise Audited CompOffEntitlement 4", 32800.00, 210.0, "ACTIVE", "uuid-compoffentitlement-04"),
    (5, "COM-0005", "Executive Strategic CompOffEntitlement 5", 65000.00, 400.0, "ACTIVE", "uuid-compoffentitlement-05");

CREATE TABLE IF NOT EXISTS time_attendance_timesheetcorrections (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_timesheetcorrections_code ON time_attendance_timesheetcorrections(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_timesheetcorrections_org_status ON time_attendance_timesheetcorrections(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_timesheetcorrections_priority ON time_attendance_timesheetcorrections(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_timesheetcorrections_created_at ON time_attendance_timesheetcorrections(created_at);

-- Operational seed data fixtures for time_attendance_timesheetcorrections
INSERT OR IGNORE INTO time_attendance_timesheetcorrections (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIM-0001", "Primary Operational TimesheetCorrection 1", 24500.00, 150.0, "ACTIVE", "uuid-timesheetcorrection-01"),
    (2, "TIM-0002", "Secondary Corporate TimesheetCorrection 2", 18200.50, 80.0, "ACTIVE", "uuid-timesheetcorrection-02"),
    (3, "TIM-0003", "Consolidated Branch TimesheetCorrection 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-timesheetcorrection-03"),
    (4, "TIM-0004", "Enterprise Audited TimesheetCorrection 4", 32800.00, 210.0, "ACTIVE", "uuid-timesheetcorrection-04"),
    (5, "TIM-0005", "Executive Strategic TimesheetCorrection 5", 65000.00, 400.0, "ACTIVE", "uuid-timesheetcorrection-05");

CREATE TABLE IF NOT EXISTS time_attendance_latearrivalinfractions (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_latearrivalinfractions_code ON time_attendance_latearrivalinfractions(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_latearrivalinfractions_org_status ON time_attendance_latearrivalinfractions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_latearrivalinfractions_priority ON time_attendance_latearrivalinfractions(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_latearrivalinfractions_created_at ON time_attendance_latearrivalinfractions(created_at);

-- Operational seed data fixtures for time_attendance_latearrivalinfractions
INSERT OR IGNORE INTO time_attendance_latearrivalinfractions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LAT-0001", "Primary Operational LateArrivalInfraction 1", 24500.00, 150.0, "ACTIVE", "uuid-latearrivalinfraction-01"),
    (2, "LAT-0002", "Secondary Corporate LateArrivalInfraction 2", 18200.50, 80.0, "ACTIVE", "uuid-latearrivalinfraction-02"),
    (3, "LAT-0003", "Consolidated Branch LateArrivalInfraction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-latearrivalinfraction-03"),
    (4, "LAT-0004", "Enterprise Audited LateArrivalInfraction 4", 32800.00, 210.0, "ACTIVE", "uuid-latearrivalinfraction-04"),
    (5, "LAT-0005", "Executive Strategic LateArrivalInfraction 5", 65000.00, 400.0, "ACTIVE", "uuid-latearrivalinfraction-05");

CREATE TABLE IF NOT EXISTS time_attendance_remoteworkdeclarations (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_remoteworkdeclarations_code ON time_attendance_remoteworkdeclarations(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_remoteworkdeclarations_org_status ON time_attendance_remoteworkdeclarations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_remoteworkdeclarations_priority ON time_attendance_remoteworkdeclarations(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_remoteworkdeclarations_created_at ON time_attendance_remoteworkdeclarations(created_at);

-- Operational seed data fixtures for time_attendance_remoteworkdeclarations
INSERT OR IGNORE INTO time_attendance_remoteworkdeclarations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REM-0001", "Primary Operational RemoteWorkDeclaration 1", 24500.00, 150.0, "ACTIVE", "uuid-remoteworkdeclaration-01"),
    (2, "REM-0002", "Secondary Corporate RemoteWorkDeclaration 2", 18200.50, 80.0, "ACTIVE", "uuid-remoteworkdeclaration-02"),
    (3, "REM-0003", "Consolidated Branch RemoteWorkDeclaration 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-remoteworkdeclaration-03"),
    (4, "REM-0004", "Enterprise Audited RemoteWorkDeclaration 4", 32800.00, 210.0, "ACTIVE", "uuid-remoteworkdeclaration-04"),
    (5, "REM-0005", "Executive Strategic RemoteWorkDeclaration 5", 65000.00, 400.0, "ACTIVE", "uuid-remoteworkdeclaration-05");

CREATE TABLE IF NOT EXISTS time_attendance_shiftswaprequests (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftswaprequests_code ON time_attendance_shiftswaprequests(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftswaprequests_org_status ON time_attendance_shiftswaprequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftswaprequests_priority ON time_attendance_shiftswaprequests(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftswaprequests_created_at ON time_attendance_shiftswaprequests(created_at);

-- Operational seed data fixtures for time_attendance_shiftswaprequests
INSERT OR IGNORE INTO time_attendance_shiftswaprequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational ShiftSwapRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-shiftswaprequest-01"),
    (2, "SHI-0002", "Secondary Corporate ShiftSwapRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-shiftswaprequest-02"),
    (3, "SHI-0003", "Consolidated Branch ShiftSwapRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shiftswaprequest-03"),
    (4, "SHI-0004", "Enterprise Audited ShiftSwapRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-shiftswaprequest-04"),
    (5, "SHI-0005", "Executive Strategic ShiftSwapRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-shiftswaprequest-05");

CREATE TABLE IF NOT EXISTS time_attendance_oncallrosterdutys (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_oncallrosterdutys_code ON time_attendance_oncallrosterdutys(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_oncallrosterdutys_org_status ON time_attendance_oncallrosterdutys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_oncallrosterdutys_priority ON time_attendance_oncallrosterdutys(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_oncallrosterdutys_created_at ON time_attendance_oncallrosterdutys(created_at);

-- Operational seed data fixtures for time_attendance_oncallrosterdutys
INSERT OR IGNORE INTO time_attendance_oncallrosterdutys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ONC-0001", "Primary Operational OnCallRosterDuty 1", 24500.00, 150.0, "ACTIVE", "uuid-oncallrosterduty-01"),
    (2, "ONC-0002", "Secondary Corporate OnCallRosterDuty 2", 18200.50, 80.0, "ACTIVE", "uuid-oncallrosterduty-02"),
    (3, "ONC-0003", "Consolidated Branch OnCallRosterDuty 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-oncallrosterduty-03"),
    (4, "ONC-0004", "Enterprise Audited OnCallRosterDuty 4", 32800.00, 210.0, "ACTIVE", "uuid-oncallrosterduty-04"),
    (5, "ONC-0005", "Executive Strategic OnCallRosterDuty 5", 65000.00, 400.0, "ACTIVE", "uuid-oncallrosterduty-05");

CREATE TABLE IF NOT EXISTS time_attendance_geofenceclockinzones (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_geofenceclockinzones_code ON time_attendance_geofenceclockinzones(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_geofenceclockinzones_org_status ON time_attendance_geofenceclockinzones(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_geofenceclockinzones_priority ON time_attendance_geofenceclockinzones(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_geofenceclockinzones_created_at ON time_attendance_geofenceclockinzones(created_at);

-- Operational seed data fixtures for time_attendance_geofenceclockinzones
INSERT OR IGNORE INTO time_attendance_geofenceclockinzones (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GEO-0001", "Primary Operational GeofenceClockInZone 1", 24500.00, 150.0, "ACTIVE", "uuid-geofenceclockinzone-01"),
    (2, "GEO-0002", "Secondary Corporate GeofenceClockInZone 2", 18200.50, 80.0, "ACTIVE", "uuid-geofenceclockinzone-02"),
    (3, "GEO-0003", "Consolidated Branch GeofenceClockInZone 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-geofenceclockinzone-03"),
    (4, "GEO-0004", "Enterprise Audited GeofenceClockInZone 4", 32800.00, 210.0, "ACTIVE", "uuid-geofenceclockinzone-04"),
    (5, "GEO-0005", "Executive Strategic GeofenceClockInZone 5", 65000.00, 400.0, "ACTIVE", "uuid-geofenceclockinzone-05");

CREATE TABLE IF NOT EXISTS time_attendance_statutoryworkinghourss (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_statutoryworkinghourss_code ON time_attendance_statutoryworkinghourss(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_statutoryworkinghourss_org_status ON time_attendance_statutoryworkinghourss(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_statutoryworkinghourss_priority ON time_attendance_statutoryworkinghourss(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_statutoryworkinghourss_created_at ON time_attendance_statutoryworkinghourss(created_at);

-- Operational seed data fixtures for time_attendance_statutoryworkinghourss
INSERT OR IGNORE INTO time_attendance_statutoryworkinghourss (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STA-0001", "Primary Operational StatutoryWorkingHours 1", 24500.00, 150.0, "ACTIVE", "uuid-statutoryworkinghours-01"),
    (2, "STA-0002", "Secondary Corporate StatutoryWorkingHours 2", 18200.50, 80.0, "ACTIVE", "uuid-statutoryworkinghours-02"),
    (3, "STA-0003", "Consolidated Branch StatutoryWorkingHours 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-statutoryworkinghours-03"),
    (4, "STA-0004", "Enterprise Audited StatutoryWorkingHours 4", 32800.00, 210.0, "ACTIVE", "uuid-statutoryworkinghours-04"),
    (5, "STA-0005", "Executive Strategic StatutoryWorkingHours 5", 65000.00, 400.0, "ACTIVE", "uuid-statutoryworkinghours-05");

CREATE TABLE IF NOT EXISTS time_attendance_shiftallowancecredits (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftallowancecredits_code ON time_attendance_shiftallowancecredits(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftallowancecredits_org_status ON time_attendance_shiftallowancecredits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftallowancecredits_priority ON time_attendance_shiftallowancecredits(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_shiftallowancecredits_created_at ON time_attendance_shiftallowancecredits(created_at);

-- Operational seed data fixtures for time_attendance_shiftallowancecredits
INSERT OR IGNORE INTO time_attendance_shiftallowancecredits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SHI-0001", "Primary Operational ShiftAllowanceCredit 1", 24500.00, 150.0, "ACTIVE", "uuid-shiftallowancecredit-01"),
    (2, "SHI-0002", "Secondary Corporate ShiftAllowanceCredit 2", 18200.50, 80.0, "ACTIVE", "uuid-shiftallowancecredit-02"),
    (3, "SHI-0003", "Consolidated Branch ShiftAllowanceCredit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-shiftallowancecredit-03"),
    (4, "SHI-0004", "Enterprise Audited ShiftAllowanceCredit 4", 32800.00, 210.0, "ACTIVE", "uuid-shiftallowancecredit-04"),
    (5, "SHI-0005", "Executive Strategic ShiftAllowanceCredit 5", 65000.00, 400.0, "ACTIVE", "uuid-shiftallowancecredit-05");

CREATE TABLE IF NOT EXISTS time_attendance_timecardsignoffs (
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

CREATE INDEX IF NOT EXISTS idx_time_attendance_timecardsignoffs_code ON time_attendance_timecardsignoffs(code);
CREATE INDEX IF NOT EXISTS idx_time_attendance_timecardsignoffs_org_status ON time_attendance_timecardsignoffs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_time_attendance_timecardsignoffs_priority ON time_attendance_timecardsignoffs(priority);
CREATE INDEX IF NOT EXISTS idx_time_attendance_timecardsignoffs_created_at ON time_attendance_timecardsignoffs(created_at);

-- Operational seed data fixtures for time_attendance_timecardsignoffs
INSERT OR IGNORE INTO time_attendance_timecardsignoffs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIM-0001", "Primary Operational TimecardSignoff 1", 24500.00, 150.0, "ACTIVE", "uuid-timecardsignoff-01"),
    (2, "TIM-0002", "Secondary Corporate TimecardSignoff 2", 18200.50, 80.0, "ACTIVE", "uuid-timecardsignoff-02"),
    (3, "TIM-0003", "Consolidated Branch TimecardSignoff 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-timecardsignoff-03"),
    (4, "TIM-0004", "Enterprise Audited TimecardSignoff 4", 32800.00, 210.0, "ACTIVE", "uuid-timecardsignoff-04"),
    (5, "TIM-0005", "Executive Strategic TimecardSignoff 5", 65000.00, 400.0, "ACTIVE", "uuid-timecardsignoff-05");

