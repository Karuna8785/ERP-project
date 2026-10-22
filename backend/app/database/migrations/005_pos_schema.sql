-- SmartERP Enterprise Titan Migration 005: Omnichannel Point-of-Sale (POS) DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS pos_posregisters (
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

CREATE INDEX IF NOT EXISTS idx_pos_posregisters_code ON pos_posregisters(code);
CREATE INDEX IF NOT EXISTS idx_pos_posregisters_org_status ON pos_posregisters(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_posregisters_priority ON pos_posregisters(priority);
CREATE INDEX IF NOT EXISTS idx_pos_posregisters_created_at ON pos_posregisters(created_at);

-- Operational seed data fixtures for pos_posregisters
INSERT OR IGNORE INTO pos_posregisters (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "POS-0001", "Primary Operational POSRegister 1", 24500.00, 150.0, "ACTIVE", "uuid-posregister-01"),
    (2, "POS-0002", "Secondary Corporate POSRegister 2", 18200.50, 80.0, "ACTIVE", "uuid-posregister-02"),
    (3, "POS-0003", "Consolidated Branch POSRegister 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-posregister-03"),
    (4, "POS-0004", "Enterprise Audited POSRegister 4", 32800.00, 210.0, "ACTIVE", "uuid-posregister-04"),
    (5, "POS-0005", "Executive Strategic POSRegister 5", 65000.00, 400.0, "ACTIVE", "uuid-posregister-05");

CREATE TABLE IF NOT EXISTS pos_postransactions (
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

CREATE INDEX IF NOT EXISTS idx_pos_postransactions_code ON pos_postransactions(code);
CREATE INDEX IF NOT EXISTS idx_pos_postransactions_org_status ON pos_postransactions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_postransactions_priority ON pos_postransactions(priority);
CREATE INDEX IF NOT EXISTS idx_pos_postransactions_created_at ON pos_postransactions(created_at);

-- Operational seed data fixtures for pos_postransactions
INSERT OR IGNORE INTO pos_postransactions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "POS-0001", "Primary Operational POSTransaction 1", 24500.00, 150.0, "ACTIVE", "uuid-postransaction-01"),
    (2, "POS-0002", "Secondary Corporate POSTransaction 2", 18200.50, 80.0, "ACTIVE", "uuid-postransaction-02"),
    (3, "POS-0003", "Consolidated Branch POSTransaction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-postransaction-03"),
    (4, "POS-0004", "Enterprise Audited POSTransaction 4", 32800.00, 210.0, "ACTIVE", "uuid-postransaction-04"),
    (5, "POS-0005", "Executive Strategic POSTransaction 5", 65000.00, 400.0, "ACTIVE", "uuid-postransaction-05");

CREATE TABLE IF NOT EXISTS pos_cashdrawers (
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

CREATE INDEX IF NOT EXISTS idx_pos_cashdrawers_code ON pos_cashdrawers(code);
CREATE INDEX IF NOT EXISTS idx_pos_cashdrawers_org_status ON pos_cashdrawers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_cashdrawers_priority ON pos_cashdrawers(priority);
CREATE INDEX IF NOT EXISTS idx_pos_cashdrawers_created_at ON pos_cashdrawers(created_at);

-- Operational seed data fixtures for pos_cashdrawers
INSERT OR IGNORE INTO pos_cashdrawers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAS-0001", "Primary Operational CashDrawer 1", 24500.00, 150.0, "ACTIVE", "uuid-cashdrawer-01"),
    (2, "CAS-0002", "Secondary Corporate CashDrawer 2", 18200.50, 80.0, "ACTIVE", "uuid-cashdrawer-02"),
    (3, "CAS-0003", "Consolidated Branch CashDrawer 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cashdrawer-03"),
    (4, "CAS-0004", "Enterprise Audited CashDrawer 4", 32800.00, 210.0, "ACTIVE", "uuid-cashdrawer-04"),
    (5, "CAS-0005", "Executive Strategic CashDrawer 5", 65000.00, 400.0, "ACTIVE", "uuid-cashdrawer-05");

CREATE TABLE IF NOT EXISTS pos_tendersplits (
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

CREATE INDEX IF NOT EXISTS idx_pos_tendersplits_code ON pos_tendersplits(code);
CREATE INDEX IF NOT EXISTS idx_pos_tendersplits_org_status ON pos_tendersplits(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_tendersplits_priority ON pos_tendersplits(priority);
CREATE INDEX IF NOT EXISTS idx_pos_tendersplits_created_at ON pos_tendersplits(created_at);

-- Operational seed data fixtures for pos_tendersplits
INSERT OR IGNORE INTO pos_tendersplits (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEN-0001", "Primary Operational TenderSplit 1", 24500.00, 150.0, "ACTIVE", "uuid-tendersplit-01"),
    (2, "TEN-0002", "Secondary Corporate TenderSplit 2", 18200.50, 80.0, "ACTIVE", "uuid-tendersplit-02"),
    (3, "TEN-0003", "Consolidated Branch TenderSplit 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-tendersplit-03"),
    (4, "TEN-0004", "Enterprise Audited TenderSplit 4", 32800.00, 210.0, "ACTIVE", "uuid-tendersplit-04"),
    (5, "TEN-0005", "Executive Strategic TenderSplit 5", 65000.00, 400.0, "ACTIVE", "uuid-tendersplit-05");

CREATE TABLE IF NOT EXISTS pos_giftcards (
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

CREATE INDEX IF NOT EXISTS idx_pos_giftcards_code ON pos_giftcards(code);
CREATE INDEX IF NOT EXISTS idx_pos_giftcards_org_status ON pos_giftcards(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_giftcards_priority ON pos_giftcards(priority);
CREATE INDEX IF NOT EXISTS idx_pos_giftcards_created_at ON pos_giftcards(created_at);

-- Operational seed data fixtures for pos_giftcards
INSERT OR IGNORE INTO pos_giftcards (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "GIF-0001", "Primary Operational GiftCard 1", 24500.00, 150.0, "ACTIVE", "uuid-giftcard-01"),
    (2, "GIF-0002", "Secondary Corporate GiftCard 2", 18200.50, 80.0, "ACTIVE", "uuid-giftcard-02"),
    (3, "GIF-0003", "Consolidated Branch GiftCard 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-giftcard-03"),
    (4, "GIF-0004", "Enterprise Audited GiftCard 4", 32800.00, 210.0, "ACTIVE", "uuid-giftcard-04"),
    (5, "GIF-0005", "Executive Strategic GiftCard 5", 65000.00, 400.0, "ACTIVE", "uuid-giftcard-05");

CREATE TABLE IF NOT EXISTS pos_couponvouchers (
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

CREATE INDEX IF NOT EXISTS idx_pos_couponvouchers_code ON pos_couponvouchers(code);
CREATE INDEX IF NOT EXISTS idx_pos_couponvouchers_org_status ON pos_couponvouchers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_couponvouchers_priority ON pos_couponvouchers(priority);
CREATE INDEX IF NOT EXISTS idx_pos_couponvouchers_created_at ON pos_couponvouchers(created_at);

-- Operational seed data fixtures for pos_couponvouchers
INSERT OR IGNORE INTO pos_couponvouchers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "COU-0001", "Primary Operational CouponVoucher 1", 24500.00, 150.0, "ACTIVE", "uuid-couponvoucher-01"),
    (2, "COU-0002", "Secondary Corporate CouponVoucher 2", 18200.50, 80.0, "ACTIVE", "uuid-couponvoucher-02"),
    (3, "COU-0003", "Consolidated Branch CouponVoucher 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-couponvoucher-03"),
    (4, "COU-0004", "Enterprise Audited CouponVoucher 4", 32800.00, 210.0, "ACTIVE", "uuid-couponvoucher-04"),
    (5, "COU-0005", "Executive Strategic CouponVoucher 5", 65000.00, 400.0, "ACTIVE", "uuid-couponvoucher-05");

CREATE TABLE IF NOT EXISTS pos_promotionrules (
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

CREATE INDEX IF NOT EXISTS idx_pos_promotionrules_code ON pos_promotionrules(code);
CREATE INDEX IF NOT EXISTS idx_pos_promotionrules_org_status ON pos_promotionrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_promotionrules_priority ON pos_promotionrules(priority);
CREATE INDEX IF NOT EXISTS idx_pos_promotionrules_created_at ON pos_promotionrules(created_at);

-- Operational seed data fixtures for pos_promotionrules
INSERT OR IGNORE INTO pos_promotionrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRO-0001", "Primary Operational PromotionRule 1", 24500.00, 150.0, "ACTIVE", "uuid-promotionrule-01"),
    (2, "PRO-0002", "Secondary Corporate PromotionRule 2", 18200.50, 80.0, "ACTIVE", "uuid-promotionrule-02"),
    (3, "PRO-0003", "Consolidated Branch PromotionRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-promotionrule-03"),
    (4, "PRO-0004", "Enterprise Audited PromotionRule 4", 32800.00, 210.0, "ACTIVE", "uuid-promotionrule-04"),
    (5, "PRO-0005", "Executive Strategic PromotionRule 5", 65000.00, 400.0, "ACTIVE", "uuid-promotionrule-05");

CREATE TABLE IF NOT EXISTS pos_returnexchanges (
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

CREATE INDEX IF NOT EXISTS idx_pos_returnexchanges_code ON pos_returnexchanges(code);
CREATE INDEX IF NOT EXISTS idx_pos_returnexchanges_org_status ON pos_returnexchanges(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_returnexchanges_priority ON pos_returnexchanges(priority);
CREATE INDEX IF NOT EXISTS idx_pos_returnexchanges_created_at ON pos_returnexchanges(created_at);

-- Operational seed data fixtures for pos_returnexchanges
INSERT OR IGNORE INTO pos_returnexchanges (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RET-0001", "Primary Operational ReturnExchange 1", 24500.00, 150.0, "ACTIVE", "uuid-returnexchange-01"),
    (2, "RET-0002", "Secondary Corporate ReturnExchange 2", 18200.50, 80.0, "ACTIVE", "uuid-returnexchange-02"),
    (3, "RET-0003", "Consolidated Branch ReturnExchange 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-returnexchange-03"),
    (4, "RET-0004", "Enterprise Audited ReturnExchange 4", 32800.00, 210.0, "ACTIVE", "uuid-returnexchange-04"),
    (5, "RET-0005", "Executive Strategic ReturnExchange 5", 65000.00, 400.0, "ACTIVE", "uuid-returnexchange-05");

CREATE TABLE IF NOT EXISTS pos_terminalsessions (
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

CREATE INDEX IF NOT EXISTS idx_pos_terminalsessions_code ON pos_terminalsessions(code);
CREATE INDEX IF NOT EXISTS idx_pos_terminalsessions_org_status ON pos_terminalsessions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_terminalsessions_priority ON pos_terminalsessions(priority);
CREATE INDEX IF NOT EXISTS idx_pos_terminalsessions_created_at ON pos_terminalsessions(created_at);

-- Operational seed data fixtures for pos_terminalsessions
INSERT OR IGNORE INTO pos_terminalsessions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TER-0001", "Primary Operational TerminalSession 1", 24500.00, 150.0, "ACTIVE", "uuid-terminalsession-01"),
    (2, "TER-0002", "Secondary Corporate TerminalSession 2", 18200.50, 80.0, "ACTIVE", "uuid-terminalsession-02"),
    (3, "TER-0003", "Consolidated Branch TerminalSession 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-terminalsession-03"),
    (4, "TER-0004", "Enterprise Audited TerminalSession 4", 32800.00, 210.0, "ACTIVE", "uuid-terminalsession-04"),
    (5, "TER-0005", "Executive Strategic TerminalSession 5", 65000.00, 400.0, "ACTIVE", "uuid-terminalsession-05");

CREATE TABLE IF NOT EXISTS pos_zreports (
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

CREATE INDEX IF NOT EXISTS idx_pos_zreports_code ON pos_zreports(code);
CREATE INDEX IF NOT EXISTS idx_pos_zreports_org_status ON pos_zreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_zreports_priority ON pos_zreports(priority);
CREATE INDEX IF NOT EXISTS idx_pos_zreports_created_at ON pos_zreports(created_at);

-- Operational seed data fixtures for pos_zreports
INSERT OR IGNORE INTO pos_zreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ZRE-0001", "Primary Operational ZReport 1", 24500.00, 150.0, "ACTIVE", "uuid-zreport-01"),
    (2, "ZRE-0002", "Secondary Corporate ZReport 2", 18200.50, 80.0, "ACTIVE", "uuid-zreport-02"),
    (3, "ZRE-0003", "Consolidated Branch ZReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-zreport-03"),
    (4, "ZRE-0004", "Enterprise Audited ZReport 4", 32800.00, 210.0, "ACTIVE", "uuid-zreport-04"),
    (5, "ZRE-0005", "Executive Strategic ZReport 5", 65000.00, 400.0, "ACTIVE", "uuid-zreport-05");

CREATE TABLE IF NOT EXISTS pos_offlinereceipts (
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

CREATE INDEX IF NOT EXISTS idx_pos_offlinereceipts_code ON pos_offlinereceipts(code);
CREATE INDEX IF NOT EXISTS idx_pos_offlinereceipts_org_status ON pos_offlinereceipts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_offlinereceipts_priority ON pos_offlinereceipts(priority);
CREATE INDEX IF NOT EXISTS idx_pos_offlinereceipts_created_at ON pos_offlinereceipts(created_at);

-- Operational seed data fixtures for pos_offlinereceipts
INSERT OR IGNORE INTO pos_offlinereceipts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OFF-0001", "Primary Operational OfflineReceipt 1", 24500.00, 150.0, "ACTIVE", "uuid-offlinereceipt-01"),
    (2, "OFF-0002", "Secondary Corporate OfflineReceipt 2", 18200.50, 80.0, "ACTIVE", "uuid-offlinereceipt-02"),
    (3, "OFF-0003", "Consolidated Branch OfflineReceipt 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-offlinereceipt-03"),
    (4, "OFF-0004", "Enterprise Audited OfflineReceipt 4", 32800.00, 210.0, "ACTIVE", "uuid-offlinereceipt-04"),
    (5, "OFF-0005", "Executive Strategic OfflineReceipt 5", 65000.00, 400.0, "ACTIVE", "uuid-offlinereceipt-05");

CREATE TABLE IF NOT EXISTS pos_hardwaredevices (
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

CREATE INDEX IF NOT EXISTS idx_pos_hardwaredevices_code ON pos_hardwaredevices(code);
CREATE INDEX IF NOT EXISTS idx_pos_hardwaredevices_org_status ON pos_hardwaredevices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_hardwaredevices_priority ON pos_hardwaredevices(priority);
CREATE INDEX IF NOT EXISTS idx_pos_hardwaredevices_created_at ON pos_hardwaredevices(created_at);

-- Operational seed data fixtures for pos_hardwaredevices
INSERT OR IGNORE INTO pos_hardwaredevices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "HAR-0001", "Primary Operational HardwareDevice 1", 24500.00, 150.0, "ACTIVE", "uuid-hardwaredevice-01"),
    (2, "HAR-0002", "Secondary Corporate HardwareDevice 2", 18200.50, 80.0, "ACTIVE", "uuid-hardwaredevice-02"),
    (3, "HAR-0003", "Consolidated Branch HardwareDevice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-hardwaredevice-03"),
    (4, "HAR-0004", "Enterprise Audited HardwareDevice 4", 32800.00, 210.0, "ACTIVE", "uuid-hardwaredevice-04"),
    (5, "HAR-0005", "Executive Strategic HardwareDevice 5", 65000.00, 400.0, "ACTIVE", "uuid-hardwaredevice-05");

CREATE TABLE IF NOT EXISTS pos_priceoverrides (
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

CREATE INDEX IF NOT EXISTS idx_pos_priceoverrides_code ON pos_priceoverrides(code);
CREATE INDEX IF NOT EXISTS idx_pos_priceoverrides_org_status ON pos_priceoverrides(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_priceoverrides_priority ON pos_priceoverrides(priority);
CREATE INDEX IF NOT EXISTS idx_pos_priceoverrides_created_at ON pos_priceoverrides(created_at);

-- Operational seed data fixtures for pos_priceoverrides
INSERT OR IGNORE INTO pos_priceoverrides (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PRI-0001", "Primary Operational PriceOverride 1", 24500.00, 150.0, "ACTIVE", "uuid-priceoverride-01"),
    (2, "PRI-0002", "Secondary Corporate PriceOverride 2", 18200.50, 80.0, "ACTIVE", "uuid-priceoverride-02"),
    (3, "PRI-0003", "Consolidated Branch PriceOverride 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-priceoverride-03"),
    (4, "PRI-0004", "Enterprise Audited PriceOverride 4", 32800.00, 210.0, "ACTIVE", "uuid-priceoverride-04"),
    (5, "PRI-0005", "Executive Strategic PriceOverride 5", 65000.00, 400.0, "ACTIVE", "uuid-priceoverride-05");

CREATE TABLE IF NOT EXISTS pos_customerloyaltys (
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

CREATE INDEX IF NOT EXISTS idx_pos_customerloyaltys_code ON pos_customerloyaltys(code);
CREATE INDEX IF NOT EXISTS idx_pos_customerloyaltys_org_status ON pos_customerloyaltys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_customerloyaltys_priority ON pos_customerloyaltys(priority);
CREATE INDEX IF NOT EXISTS idx_pos_customerloyaltys_created_at ON pos_customerloyaltys(created_at);

-- Operational seed data fixtures for pos_customerloyaltys
INSERT OR IGNORE INTO pos_customerloyaltys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerLoyalty 1", 24500.00, 150.0, "ACTIVE", "uuid-customerloyalty-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerLoyalty 2", 18200.50, 80.0, "ACTIVE", "uuid-customerloyalty-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerLoyalty 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customerloyalty-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerLoyalty 4", 32800.00, 210.0, "ACTIVE", "uuid-customerloyalty-04"),
    (5, "CUS-0005", "Executive Strategic CustomerLoyalty 5", 65000.00, 400.0, "ACTIVE", "uuid-customerloyalty-05");

CREATE TABLE IF NOT EXISTS pos_layawayorders (
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

CREATE INDEX IF NOT EXISTS idx_pos_layawayorders_code ON pos_layawayorders(code);
CREATE INDEX IF NOT EXISTS idx_pos_layawayorders_org_status ON pos_layawayorders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_layawayorders_priority ON pos_layawayorders(priority);
CREATE INDEX IF NOT EXISTS idx_pos_layawayorders_created_at ON pos_layawayorders(created_at);

-- Operational seed data fixtures for pos_layawayorders
INSERT OR IGNORE INTO pos_layawayorders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "LAY-0001", "Primary Operational LayawayOrder 1", 24500.00, 150.0, "ACTIVE", "uuid-layawayorder-01"),
    (2, "LAY-0002", "Secondary Corporate LayawayOrder 2", 18200.50, 80.0, "ACTIVE", "uuid-layawayorder-02"),
    (3, "LAY-0003", "Consolidated Branch LayawayOrder 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-layawayorder-03"),
    (4, "LAY-0004", "Enterprise Audited LayawayOrder 4", 32800.00, 210.0, "ACTIVE", "uuid-layawayorder-04"),
    (5, "LAY-0005", "Executive Strategic LayawayOrder 5", 65000.00, 400.0, "ACTIVE", "uuid-layawayorder-05");

CREATE TABLE IF NOT EXISTS pos_stockreservations (
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

CREATE INDEX IF NOT EXISTS idx_pos_stockreservations_code ON pos_stockreservations(code);
CREATE INDEX IF NOT EXISTS idx_pos_stockreservations_org_status ON pos_stockreservations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_pos_stockreservations_priority ON pos_stockreservations(priority);
CREATE INDEX IF NOT EXISTS idx_pos_stockreservations_created_at ON pos_stockreservations(created_at);

-- Operational seed data fixtures for pos_stockreservations
INSERT OR IGNORE INTO pos_stockreservations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "STO-0001", "Primary Operational StockReservation 1", 24500.00, 150.0, "ACTIVE", "uuid-stockreservation-01"),
    (2, "STO-0002", "Secondary Corporate StockReservation 2", 18200.50, 80.0, "ACTIVE", "uuid-stockreservation-02"),
    (3, "STO-0003", "Consolidated Branch StockReservation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-stockreservation-03"),
    (4, "STO-0004", "Enterprise Audited StockReservation 4", 32800.00, 210.0, "ACTIVE", "uuid-stockreservation-04"),
    (5, "STO-0005", "Executive Strategic StockReservation 5", 65000.00, 400.0, "ACTIVE", "uuid-stockreservation-05");

