-- SmartERP Enterprise Titan Migration 040: Corporate Travel & Expense Reimbursement DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS travel_expense_travelauthorizationrequests (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_travelauthorizationrequests_code ON travel_expense_travelauthorizationrequests(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelauthorizationrequests_org_status ON travel_expense_travelauthorizationrequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelauthorizationrequests_priority ON travel_expense_travelauthorizationrequests(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelauthorizationrequests_created_at ON travel_expense_travelauthorizationrequests(created_at);

-- Operational seed data fixtures for travel_expense_travelauthorizationrequests
INSERT OR IGNORE INTO travel_expense_travelauthorizationrequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TravelAuthorizationRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-travelauthorizationrequest-01"),
    (2, "TRA-0002", "Secondary Corporate TravelAuthorizationRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-travelauthorizationrequest-02"),
    (3, "TRA-0003", "Consolidated Branch TravelAuthorizationRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-travelauthorizationrequest-03"),
    (4, "TRA-0004", "Enterprise Audited TravelAuthorizationRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-travelauthorizationrequest-04"),
    (5, "TRA-0005", "Executive Strategic TravelAuthorizationRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-travelauthorizationrequest-05");

CREATE TABLE IF NOT EXISTS travel_expense_flightreservationbookings (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_flightreservationbookings_code ON travel_expense_flightreservationbookings(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_flightreservationbookings_org_status ON travel_expense_flightreservationbookings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_flightreservationbookings_priority ON travel_expense_flightreservationbookings(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_flightreservationbookings_created_at ON travel_expense_flightreservationbookings(created_at);

-- Operational seed data fixtures for travel_expense_flightreservationbookings
INSERT OR IGNORE INTO travel_expense_flightreservationbookings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FLI-0001", "Primary Operational FlightReservationBooking 1", 24500.00, 150.0, "ACTIVE", "uuid-flightreservationbooking-01"),
    (2, "FLI-0002", "Secondary Corporate FlightReservationBooking 2", 18200.50, 80.0, "ACTIVE", "uuid-flightreservationbooking-02"),
    (3, "FLI-0003", "Consolidated Branch FlightReservationBooking 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-flightreservationbooking-03"),
    (4, "FLI-0004", "Enterprise Audited FlightReservationBooking 4", 32800.00, 210.0, "ACTIVE", "uuid-flightreservationbooking-04"),
    (5, "FLI-0005", "Executive Strategic FlightReservationBooking 5", 65000.00, 400.0, "ACTIVE", "uuid-flightreservationbooking-05");

CREATE TABLE IF NOT EXISTS travel_expense_hotelaccommodationrecords (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_hotelaccommodationrecords_code ON travel_expense_hotelaccommodationrecords(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_hotelaccommodationrecords_org_status ON travel_expense_hotelaccommodationrecords(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_hotelaccommodationrecords_priority ON travel_expense_hotelaccommodationrecords(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_hotelaccommodationrecords_created_at ON travel_expense_hotelaccommodationrecords(created_at);

-- Operational seed data fixtures for travel_expense_hotelaccommodationrecords
INSERT OR IGNORE INTO travel_expense_hotelaccommodationrecords (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HOT-0001", "Primary Operational HotelAccommodationRecord 1", 24500.00, 150.0, "ACTIVE", "uuid-hotelaccommodationrecord-01"),
    (2, "HOT-0002", "Secondary Corporate HotelAccommodationRecord 2", 18200.50, 80.0, "ACTIVE", "uuid-hotelaccommodationrecord-02"),
    (3, "HOT-0003", "Consolidated Branch HotelAccommodationRecord 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hotelaccommodationrecord-03"),
    (4, "HOT-0004", "Enterprise Audited HotelAccommodationRecord 4", 32800.00, 210.0, "ACTIVE", "uuid-hotelaccommodationrecord-04"),
    (5, "HOT-0005", "Executive Strategic HotelAccommodationRecord 5", 65000.00, 400.0, "ACTIVE", "uuid-hotelaccommodationrecord-05");

CREATE TABLE IF NOT EXISTS travel_expense_expensereportvouchers (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_expensereportvouchers_code ON travel_expense_expensereportvouchers(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_expensereportvouchers_org_status ON travel_expense_expensereportvouchers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_expensereportvouchers_priority ON travel_expense_expensereportvouchers(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_expensereportvouchers_created_at ON travel_expense_expensereportvouchers(created_at);

-- Operational seed data fixtures for travel_expense_expensereportvouchers
INSERT OR IGNORE INTO travel_expense_expensereportvouchers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExpenseReportVoucher 1", 24500.00, 150.0, "ACTIVE", "uuid-expensereportvoucher-01"),
    (2, "EXP-0002", "Secondary Corporate ExpenseReportVoucher 2", 18200.50, 80.0, "ACTIVE", "uuid-expensereportvoucher-02"),
    (3, "EXP-0003", "Consolidated Branch ExpenseReportVoucher 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-expensereportvoucher-03"),
    (4, "EXP-0004", "Enterprise Audited ExpenseReportVoucher 4", 32800.00, 210.0, "ACTIVE", "uuid-expensereportvoucher-04"),
    (5, "EXP-0005", "Executive Strategic ExpenseReportVoucher 5", 65000.00, 400.0, "ACTIVE", "uuid-expensereportvoucher-05");

CREATE TABLE IF NOT EXISTS travel_expense_perdiemallowancerates (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_perdiemallowancerates_code ON travel_expense_perdiemallowancerates(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_perdiemallowancerates_org_status ON travel_expense_perdiemallowancerates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_perdiemallowancerates_priority ON travel_expense_perdiemallowancerates(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_perdiemallowancerates_created_at ON travel_expense_perdiemallowancerates(created_at);

-- Operational seed data fixtures for travel_expense_perdiemallowancerates
INSERT OR IGNORE INTO travel_expense_perdiemallowancerates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PER-0001", "Primary Operational PerDiemAllowanceRate 1", 24500.00, 150.0, "ACTIVE", "uuid-perdiemallowancerate-01"),
    (2, "PER-0002", "Secondary Corporate PerDiemAllowanceRate 2", 18200.50, 80.0, "ACTIVE", "uuid-perdiemallowancerate-02"),
    (3, "PER-0003", "Consolidated Branch PerDiemAllowanceRate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-perdiemallowancerate-03"),
    (4, "PER-0004", "Enterprise Audited PerDiemAllowanceRate 4", 32800.00, 210.0, "ACTIVE", "uuid-perdiemallowancerate-04"),
    (5, "PER-0005", "Executive Strategic PerDiemAllowanceRate 5", 65000.00, 400.0, "ACTIVE", "uuid-perdiemallowancerate-05");

CREATE TABLE IF NOT EXISTS travel_expense_corporatecreditcardfeeds (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_corporatecreditcardfeeds_code ON travel_expense_corporatecreditcardfeeds(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_corporatecreditcardfeeds_org_status ON travel_expense_corporatecreditcardfeeds(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_corporatecreditcardfeeds_priority ON travel_expense_corporatecreditcardfeeds(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_corporatecreditcardfeeds_created_at ON travel_expense_corporatecreditcardfeeds(created_at);

-- Operational seed data fixtures for travel_expense_corporatecreditcardfeeds
INSERT OR IGNORE INTO travel_expense_corporatecreditcardfeeds (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COR-0001", "Primary Operational CorporateCreditCardFeed 1", 24500.00, 150.0, "ACTIVE", "uuid-corporatecreditcardfeed-01"),
    (2, "COR-0002", "Secondary Corporate CorporateCreditCardFeed 2", 18200.50, 80.0, "ACTIVE", "uuid-corporatecreditcardfeed-02"),
    (3, "COR-0003", "Consolidated Branch CorporateCreditCardFeed 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-corporatecreditcardfeed-03"),
    (4, "COR-0004", "Enterprise Audited CorporateCreditCardFeed 4", 32800.00, 210.0, "ACTIVE", "uuid-corporatecreditcardfeed-04"),
    (5, "COR-0005", "Executive Strategic CorporateCreditCardFeed 5", 65000.00, 400.0, "ACTIVE", "uuid-corporatecreditcardfeed-05");

CREATE TABLE IF NOT EXISTS travel_expense_receiptocrscans (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_receiptocrscans_code ON travel_expense_receiptocrscans(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_receiptocrscans_org_status ON travel_expense_receiptocrscans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_receiptocrscans_priority ON travel_expense_receiptocrscans(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_receiptocrscans_created_at ON travel_expense_receiptocrscans(created_at);

-- Operational seed data fixtures for travel_expense_receiptocrscans
INSERT OR IGNORE INTO travel_expense_receiptocrscans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REC-0001", "Primary Operational ReceiptOCRScan 1", 24500.00, 150.0, "ACTIVE", "uuid-receiptocrscan-01"),
    (2, "REC-0002", "Secondary Corporate ReceiptOCRScan 2", 18200.50, 80.0, "ACTIVE", "uuid-receiptocrscan-02"),
    (3, "REC-0003", "Consolidated Branch ReceiptOCRScan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-receiptocrscan-03"),
    (4, "REC-0004", "Enterprise Audited ReceiptOCRScan 4", 32800.00, 210.0, "ACTIVE", "uuid-receiptocrscan-04"),
    (5, "REC-0005", "Executive Strategic ReceiptOCRScan 5", 65000.00, 400.0, "ACTIVE", "uuid-receiptocrscan-05");

CREATE TABLE IF NOT EXISTS travel_expense_mileagereimbursements (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_mileagereimbursements_code ON travel_expense_mileagereimbursements(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_mileagereimbursements_org_status ON travel_expense_mileagereimbursements(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_mileagereimbursements_priority ON travel_expense_mileagereimbursements(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_mileagereimbursements_created_at ON travel_expense_mileagereimbursements(created_at);

-- Operational seed data fixtures for travel_expense_mileagereimbursements
INSERT OR IGNORE INTO travel_expense_mileagereimbursements (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MIL-0001", "Primary Operational MileageReimbursement 1", 24500.00, 150.0, "ACTIVE", "uuid-mileagereimbursement-01"),
    (2, "MIL-0002", "Secondary Corporate MileageReimbursement 2", 18200.50, 80.0, "ACTIVE", "uuid-mileagereimbursement-02"),
    (3, "MIL-0003", "Consolidated Branch MileageReimbursement 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-mileagereimbursement-03"),
    (4, "MIL-0004", "Enterprise Audited MileageReimbursement 4", 32800.00, 210.0, "ACTIVE", "uuid-mileagereimbursement-04"),
    (5, "MIL-0005", "Executive Strategic MileageReimbursement 5", 65000.00, 400.0, "ACTIVE", "uuid-mileagereimbursement-05");

CREATE TABLE IF NOT EXISTS travel_expense_travelpolicyrules (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_travelpolicyrules_code ON travel_expense_travelpolicyrules(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelpolicyrules_org_status ON travel_expense_travelpolicyrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelpolicyrules_priority ON travel_expense_travelpolicyrules(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelpolicyrules_created_at ON travel_expense_travelpolicyrules(created_at);

-- Operational seed data fixtures for travel_expense_travelpolicyrules
INSERT OR IGNORE INTO travel_expense_travelpolicyrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TravelPolicyRule 1", 24500.00, 150.0, "ACTIVE", "uuid-travelpolicyrule-01"),
    (2, "TRA-0002", "Secondary Corporate TravelPolicyRule 2", 18200.50, 80.0, "ACTIVE", "uuid-travelpolicyrule-02"),
    (3, "TRA-0003", "Consolidated Branch TravelPolicyRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-travelpolicyrule-03"),
    (4, "TRA-0004", "Enterprise Audited TravelPolicyRule 4", 32800.00, 210.0, "ACTIVE", "uuid-travelpolicyrule-04"),
    (5, "TRA-0005", "Executive Strategic TravelPolicyRule 5", 65000.00, 400.0, "ACTIVE", "uuid-travelpolicyrule-05");

CREATE TABLE IF NOT EXISTS travel_expense_foreigncurrencyreceipts (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_foreigncurrencyreceipts_code ON travel_expense_foreigncurrencyreceipts(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_foreigncurrencyreceipts_org_status ON travel_expense_foreigncurrencyreceipts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_foreigncurrencyreceipts_priority ON travel_expense_foreigncurrencyreceipts(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_foreigncurrencyreceipts_created_at ON travel_expense_foreigncurrencyreceipts(created_at);

-- Operational seed data fixtures for travel_expense_foreigncurrencyreceipts
INSERT OR IGNORE INTO travel_expense_foreigncurrencyreceipts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FOR-0001", "Primary Operational ForeignCurrencyReceipt 1", 24500.00, 150.0, "ACTIVE", "uuid-foreigncurrencyreceipt-01"),
    (2, "FOR-0002", "Secondary Corporate ForeignCurrencyReceipt 2", 18200.50, 80.0, "ACTIVE", "uuid-foreigncurrencyreceipt-02"),
    (3, "FOR-0003", "Consolidated Branch ForeignCurrencyReceipt 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-foreigncurrencyreceipt-03"),
    (4, "FOR-0004", "Enterprise Audited ForeignCurrencyReceipt 4", 32800.00, 210.0, "ACTIVE", "uuid-foreigncurrencyreceipt-04"),
    (5, "FOR-0005", "Executive Strategic ForeignCurrencyReceipt 5", 65000.00, 400.0, "ACTIVE", "uuid-foreigncurrencyreceipt-05");

CREATE TABLE IF NOT EXISTS travel_expense_cashadvancerequests (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_cashadvancerequests_code ON travel_expense_cashadvancerequests(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_cashadvancerequests_org_status ON travel_expense_cashadvancerequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_cashadvancerequests_priority ON travel_expense_cashadvancerequests(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_cashadvancerequests_created_at ON travel_expense_cashadvancerequests(created_at);

-- Operational seed data fixtures for travel_expense_cashadvancerequests
INSERT OR IGNORE INTO travel_expense_cashadvancerequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAS-0001", "Primary Operational CashAdvanceRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-cashadvancerequest-01"),
    (2, "CAS-0002", "Secondary Corporate CashAdvanceRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-cashadvancerequest-02"),
    (3, "CAS-0003", "Consolidated Branch CashAdvanceRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cashadvancerequest-03"),
    (4, "CAS-0004", "Enterprise Audited CashAdvanceRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-cashadvancerequest-04"),
    (5, "CAS-0005", "Executive Strategic CashAdvanceRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-cashadvancerequest-05");

CREATE TABLE IF NOT EXISTS travel_expense_expenseapprovalflows (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_expenseapprovalflows_code ON travel_expense_expenseapprovalflows(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_expenseapprovalflows_org_status ON travel_expense_expenseapprovalflows(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_expenseapprovalflows_priority ON travel_expense_expenseapprovalflows(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_expenseapprovalflows_created_at ON travel_expense_expenseapprovalflows(created_at);

-- Operational seed data fixtures for travel_expense_expenseapprovalflows
INSERT OR IGNORE INTO travel_expense_expenseapprovalflows (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EXP-0001", "Primary Operational ExpenseApprovalFlow 1", 24500.00, 150.0, "ACTIVE", "uuid-expenseapprovalflow-01"),
    (2, "EXP-0002", "Secondary Corporate ExpenseApprovalFlow 2", 18200.50, 80.0, "ACTIVE", "uuid-expenseapprovalflow-02"),
    (3, "EXP-0003", "Consolidated Branch ExpenseApprovalFlow 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-expenseapprovalflow-03"),
    (4, "EXP-0004", "Enterprise Audited ExpenseApprovalFlow 4", 32800.00, 210.0, "ACTIVE", "uuid-expenseapprovalflow-04"),
    (5, "EXP-0005", "Executive Strategic ExpenseApprovalFlow 5", 65000.00, 400.0, "ACTIVE", "uuid-expenseapprovalflow-05");

CREATE TABLE IF NOT EXISTS travel_expense_nonreimbursableitems (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_nonreimbursableitems_code ON travel_expense_nonreimbursableitems(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_nonreimbursableitems_org_status ON travel_expense_nonreimbursableitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_nonreimbursableitems_priority ON travel_expense_nonreimbursableitems(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_nonreimbursableitems_created_at ON travel_expense_nonreimbursableitems(created_at);

-- Operational seed data fixtures for travel_expense_nonreimbursableitems
INSERT OR IGNORE INTO travel_expense_nonreimbursableitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "NON-0001", "Primary Operational NonReimbursableItem 1", 24500.00, 150.0, "ACTIVE", "uuid-nonreimbursableitem-01"),
    (2, "NON-0002", "Secondary Corporate NonReimbursableItem 2", 18200.50, 80.0, "ACTIVE", "uuid-nonreimbursableitem-02"),
    (3, "NON-0003", "Consolidated Branch NonReimbursableItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-nonreimbursableitem-03"),
    (4, "NON-0004", "Enterprise Audited NonReimbursableItem 4", 32800.00, 210.0, "ACTIVE", "uuid-nonreimbursableitem-04"),
    (5, "NON-0005", "Executive Strategic NonReimbursableItem 5", 65000.00, 400.0, "ACTIVE", "uuid-nonreimbursableitem-05");

CREATE TABLE IF NOT EXISTS travel_expense_travelriskassessments (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_travelriskassessments_code ON travel_expense_travelriskassessments(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelriskassessments_org_status ON travel_expense_travelriskassessments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelriskassessments_priority ON travel_expense_travelriskassessments(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_travelriskassessments_created_at ON travel_expense_travelriskassessments(created_at);

-- Operational seed data fixtures for travel_expense_travelriskassessments
INSERT OR IGNORE INTO travel_expense_travelriskassessments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TRA-0001", "Primary Operational TravelRiskAssessment 1", 24500.00, 150.0, "ACTIVE", "uuid-travelriskassessment-01"),
    (2, "TRA-0002", "Secondary Corporate TravelRiskAssessment 2", 18200.50, 80.0, "ACTIVE", "uuid-travelriskassessment-02"),
    (3, "TRA-0003", "Consolidated Branch TravelRiskAssessment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-travelriskassessment-03"),
    (4, "TRA-0004", "Enterprise Audited TravelRiskAssessment 4", 32800.00, 210.0, "ACTIVE", "uuid-travelriskassessment-04"),
    (5, "TRA-0005", "Executive Strategic TravelRiskAssessment 5", 65000.00, 400.0, "ACTIVE", "uuid-travelriskassessment-05");

CREATE TABLE IF NOT EXISTS travel_expense_preferredvendorhotels (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_preferredvendorhotels_code ON travel_expense_preferredvendorhotels(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_preferredvendorhotels_org_status ON travel_expense_preferredvendorhotels(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_preferredvendorhotels_priority ON travel_expense_preferredvendorhotels(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_preferredvendorhotels_created_at ON travel_expense_preferredvendorhotels(created_at);

-- Operational seed data fixtures for travel_expense_preferredvendorhotels
INSERT OR IGNORE INTO travel_expense_preferredvendorhotels (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRE-0001", "Primary Operational PreferredVendorHotel 1", 24500.00, 150.0, "ACTIVE", "uuid-preferredvendorhotel-01"),
    (2, "PRE-0002", "Secondary Corporate PreferredVendorHotel 2", 18200.50, 80.0, "ACTIVE", "uuid-preferredvendorhotel-02"),
    (3, "PRE-0003", "Consolidated Branch PreferredVendorHotel 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-preferredvendorhotel-03"),
    (4, "PRE-0004", "Enterprise Audited PreferredVendorHotel 4", 32800.00, 210.0, "ACTIVE", "uuid-preferredvendorhotel-04"),
    (5, "PRE-0005", "Executive Strategic PreferredVendorHotel 5", 65000.00, 400.0, "ACTIVE", "uuid-preferredvendorhotel-05");

CREATE TABLE IF NOT EXISTS travel_expense_spendauditanomalys (
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

CREATE INDEX IF NOT EXISTS idx_travel_expense_spendauditanomalys_code ON travel_expense_spendauditanomalys(code);
CREATE INDEX IF NOT EXISTS idx_travel_expense_spendauditanomalys_org_status ON travel_expense_spendauditanomalys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_travel_expense_spendauditanomalys_priority ON travel_expense_spendauditanomalys(priority);
CREATE INDEX IF NOT EXISTS idx_travel_expense_spendauditanomalys_created_at ON travel_expense_spendauditanomalys(created_at);

-- Operational seed data fixtures for travel_expense_spendauditanomalys
INSERT OR IGNORE INTO travel_expense_spendauditanomalys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SPE-0001", "Primary Operational SpendAuditAnomaly 1", 24500.00, 150.0, "ACTIVE", "uuid-spendauditanomaly-01"),
    (2, "SPE-0002", "Secondary Corporate SpendAuditAnomaly 2", 18200.50, 80.0, "ACTIVE", "uuid-spendauditanomaly-02"),
    (3, "SPE-0003", "Consolidated Branch SpendAuditAnomaly 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-spendauditanomaly-03"),
    (4, "SPE-0004", "Enterprise Audited SpendAuditAnomaly 4", 32800.00, 210.0, "ACTIVE", "uuid-spendauditanomaly-04"),
    (5, "SPE-0005", "Executive Strategic SpendAuditAnomaly 5", 65000.00, 400.0, "ACTIVE", "uuid-spendauditanomaly-05");

