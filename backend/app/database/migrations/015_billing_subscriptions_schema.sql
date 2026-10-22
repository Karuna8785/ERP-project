-- SmartERP Enterprise Titan Migration 015: Subscription Billing & Revenue Recognition DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS billing_subscriptions_subscriptionplans (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_subscriptionplans_code ON billing_subscriptions_subscriptionplans(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_subscriptionplans_org_status ON billing_subscriptions_subscriptionplans(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_subscriptionplans_priority ON billing_subscriptions_subscriptionplans(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_subscriptionplans_created_at ON billing_subscriptions_subscriptionplans(created_at);

-- Operational seed data fixtures for billing_subscriptions_subscriptionplans
INSERT OR IGNORE INTO billing_subscriptions_subscriptionplans (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUB-0001", "Primary Operational SubscriptionPlan 1", 24500.00, 150.0, "ACTIVE", "uuid-subscriptionplan-01"),
    (2, "SUB-0002", "Secondary Corporate SubscriptionPlan 2", 18200.50, 80.0, "ACTIVE", "uuid-subscriptionplan-02"),
    (3, "SUB-0003", "Consolidated Branch SubscriptionPlan 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-subscriptionplan-03"),
    (4, "SUB-0004", "Enterprise Audited SubscriptionPlan 4", 32800.00, 210.0, "ACTIVE", "uuid-subscriptionplan-04"),
    (5, "SUB-0005", "Executive Strategic SubscriptionPlan 5", 65000.00, 400.0, "ACTIVE", "uuid-subscriptionplan-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_customersubscriptions (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_customersubscriptions_code ON billing_subscriptions_customersubscriptions(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_customersubscriptions_org_status ON billing_subscriptions_customersubscriptions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_customersubscriptions_priority ON billing_subscriptions_customersubscriptions(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_customersubscriptions_created_at ON billing_subscriptions_customersubscriptions(created_at);

-- Operational seed data fixtures for billing_subscriptions_customersubscriptions
INSERT OR IGNORE INTO billing_subscriptions_customersubscriptions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerSubscription 1", 24500.00, 150.0, "ACTIVE", "uuid-customersubscription-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerSubscription 2", 18200.50, 80.0, "ACTIVE", "uuid-customersubscription-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerSubscription 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customersubscription-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerSubscription 4", 32800.00, 210.0, "ACTIVE", "uuid-customersubscription-04"),
    (5, "CUS-0005", "Executive Strategic CustomerSubscription 5", 65000.00, 400.0, "ACTIVE", "uuid-customersubscription-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_billingintervalschedules (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingintervalschedules_code ON billing_subscriptions_billingintervalschedules(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingintervalschedules_org_status ON billing_subscriptions_billingintervalschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingintervalschedules_priority ON billing_subscriptions_billingintervalschedules(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingintervalschedules_created_at ON billing_subscriptions_billingintervalschedules(created_at);

-- Operational seed data fixtures for billing_subscriptions_billingintervalschedules
INSERT OR IGNORE INTO billing_subscriptions_billingintervalschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BIL-0001", "Primary Operational BillingIntervalSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-billingintervalschedule-01"),
    (2, "BIL-0002", "Secondary Corporate BillingIntervalSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-billingintervalschedule-02"),
    (3, "BIL-0003", "Consolidated Branch BillingIntervalSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-billingintervalschedule-03"),
    (4, "BIL-0004", "Enterprise Audited BillingIntervalSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-billingintervalschedule-04"),
    (5, "BIL-0005", "Executive Strategic BillingIntervalSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-billingintervalschedule-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_meteredusageevents (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_meteredusageevents_code ON billing_subscriptions_meteredusageevents(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_meteredusageevents_org_status ON billing_subscriptions_meteredusageevents(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_meteredusageevents_priority ON billing_subscriptions_meteredusageevents(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_meteredusageevents_created_at ON billing_subscriptions_meteredusageevents(created_at);

-- Operational seed data fixtures for billing_subscriptions_meteredusageevents
INSERT OR IGNORE INTO billing_subscriptions_meteredusageevents (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "MET-0001", "Primary Operational MeteredUsageEvent 1", 24500.00, 150.0, "ACTIVE", "uuid-meteredusageevent-01"),
    (2, "MET-0002", "Secondary Corporate MeteredUsageEvent 2", 18200.50, 80.0, "ACTIVE", "uuid-meteredusageevent-02"),
    (3, "MET-0003", "Consolidated Branch MeteredUsageEvent 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-meteredusageevent-03"),
    (4, "MET-0004", "Enterprise Audited MeteredUsageEvent 4", 32800.00, 210.0, "ACTIVE", "uuid-meteredusageevent-04"),
    (5, "MET-0005", "Executive Strategic MeteredUsageEvent 5", 65000.00, 400.0, "ACTIVE", "uuid-meteredusageevent-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_invoicechargeitems (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_invoicechargeitems_code ON billing_subscriptions_invoicechargeitems(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_invoicechargeitems_org_status ON billing_subscriptions_invoicechargeitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_invoicechargeitems_priority ON billing_subscriptions_invoicechargeitems(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_invoicechargeitems_created_at ON billing_subscriptions_invoicechargeitems(created_at);

-- Operational seed data fixtures for billing_subscriptions_invoicechargeitems
INSERT OR IGNORE INTO billing_subscriptions_invoicechargeitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INV-0001", "Primary Operational InvoiceChargeItem 1", 24500.00, 150.0, "ACTIVE", "uuid-invoicechargeitem-01"),
    (2, "INV-0002", "Secondary Corporate InvoiceChargeItem 2", 18200.50, 80.0, "ACTIVE", "uuid-invoicechargeitem-02"),
    (3, "INV-0003", "Consolidated Branch InvoiceChargeItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-invoicechargeitem-03"),
    (4, "INV-0004", "Enterprise Audited InvoiceChargeItem 4", 32800.00, 210.0, "ACTIVE", "uuid-invoicechargeitem-04"),
    (5, "INV-0005", "Executive Strategic InvoiceChargeItem 5", 65000.00, 400.0, "ACTIVE", "uuid-invoicechargeitem-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_discountcoupons (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_discountcoupons_code ON billing_subscriptions_discountcoupons(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_discountcoupons_org_status ON billing_subscriptions_discountcoupons(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_discountcoupons_priority ON billing_subscriptions_discountcoupons(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_discountcoupons_created_at ON billing_subscriptions_discountcoupons(created_at);

-- Operational seed data fixtures for billing_subscriptions_discountcoupons
INSERT OR IGNORE INTO billing_subscriptions_discountcoupons (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DiscountCoupon 1", 24500.00, 150.0, "ACTIVE", "uuid-discountcoupon-01"),
    (2, "DIS-0002", "Secondary Corporate DiscountCoupon 2", 18200.50, 80.0, "ACTIVE", "uuid-discountcoupon-02"),
    (3, "DIS-0003", "Consolidated Branch DiscountCoupon 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-discountcoupon-03"),
    (4, "DIS-0004", "Enterprise Audited DiscountCoupon 4", 32800.00, 210.0, "ACTIVE", "uuid-discountcoupon-04"),
    (5, "DIS-0005", "Executive Strategic DiscountCoupon 5", 65000.00, 400.0, "ACTIVE", "uuid-discountcoupon-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_paymentmethodprofiles (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_paymentmethodprofiles_code ON billing_subscriptions_paymentmethodprofiles(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_paymentmethodprofiles_org_status ON billing_subscriptions_paymentmethodprofiles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_paymentmethodprofiles_priority ON billing_subscriptions_paymentmethodprofiles(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_paymentmethodprofiles_created_at ON billing_subscriptions_paymentmethodprofiles(created_at);

-- Operational seed data fixtures for billing_subscriptions_paymentmethodprofiles
INSERT OR IGNORE INTO billing_subscriptions_paymentmethodprofiles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PAY-0001", "Primary Operational PaymentMethodProfile 1", 24500.00, 150.0, "ACTIVE", "uuid-paymentmethodprofile-01"),
    (2, "PAY-0002", "Secondary Corporate PaymentMethodProfile 2", 18200.50, 80.0, "ACTIVE", "uuid-paymentmethodprofile-02"),
    (3, "PAY-0003", "Consolidated Branch PaymentMethodProfile 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-paymentmethodprofile-03"),
    (4, "PAY-0004", "Enterprise Audited PaymentMethodProfile 4", 32800.00, 210.0, "ACTIVE", "uuid-paymentmethodprofile-04"),
    (5, "PAY-0005", "Executive Strategic PaymentMethodProfile 5", 65000.00, 400.0, "ACTIVE", "uuid-paymentmethodprofile-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_dunningsequences (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_dunningsequences_code ON billing_subscriptions_dunningsequences(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_dunningsequences_org_status ON billing_subscriptions_dunningsequences(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_dunningsequences_priority ON billing_subscriptions_dunningsequences(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_dunningsequences_created_at ON billing_subscriptions_dunningsequences(created_at);

-- Operational seed data fixtures for billing_subscriptions_dunningsequences
INSERT OR IGNORE INTO billing_subscriptions_dunningsequences (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DUN-0001", "Primary Operational DunningSequence 1", 24500.00, 150.0, "ACTIVE", "uuid-dunningsequence-01"),
    (2, "DUN-0002", "Secondary Corporate DunningSequence 2", 18200.50, 80.0, "ACTIVE", "uuid-dunningsequence-02"),
    (3, "DUN-0003", "Consolidated Branch DunningSequence 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dunningsequence-03"),
    (4, "DUN-0004", "Enterprise Audited DunningSequence 4", 32800.00, 210.0, "ACTIVE", "uuid-dunningsequence-04"),
    (5, "DUN-0005", "Executive Strategic DunningSequence 5", 65000.00, 400.0, "ACTIVE", "uuid-dunningsequence-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_revenuecontractasc606s (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_revenuecontractasc606s_code ON billing_subscriptions_revenuecontractasc606s(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_revenuecontractasc606s_org_status ON billing_subscriptions_revenuecontractasc606s(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_revenuecontractasc606s_priority ON billing_subscriptions_revenuecontractasc606s(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_revenuecontractasc606s_created_at ON billing_subscriptions_revenuecontractasc606s(created_at);

-- Operational seed data fixtures for billing_subscriptions_revenuecontractasc606s
INSERT OR IGNORE INTO billing_subscriptions_revenuecontractasc606s (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "REV-0001", "Primary Operational RevenueContractASC606 1", 24500.00, 150.0, "ACTIVE", "uuid-revenuecontractasc606-01"),
    (2, "REV-0002", "Secondary Corporate RevenueContractASC606 2", 18200.50, 80.0, "ACTIVE", "uuid-revenuecontractasc606-02"),
    (3, "REV-0003", "Consolidated Branch RevenueContractASC606 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-revenuecontractasc606-03"),
    (4, "REV-0004", "Enterprise Audited RevenueContractASC606 4", 32800.00, 210.0, "ACTIVE", "uuid-revenuecontractasc606-04"),
    (5, "REV-0005", "Executive Strategic RevenueContractASC606 5", 65000.00, 400.0, "ACTIVE", "uuid-revenuecontractasc606-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_performanceobligations (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_performanceobligations_code ON billing_subscriptions_performanceobligations(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_performanceobligations_org_status ON billing_subscriptions_performanceobligations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_performanceobligations_priority ON billing_subscriptions_performanceobligations(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_performanceobligations_created_at ON billing_subscriptions_performanceobligations(created_at);

-- Operational seed data fixtures for billing_subscriptions_performanceobligations
INSERT OR IGNORE INTO billing_subscriptions_performanceobligations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PER-0001", "Primary Operational PerformanceObligation 1", 24500.00, 150.0, "ACTIVE", "uuid-performanceobligation-01"),
    (2, "PER-0002", "Secondary Corporate PerformanceObligation 2", 18200.50, 80.0, "ACTIVE", "uuid-performanceobligation-02"),
    (3, "PER-0003", "Consolidated Branch PerformanceObligation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-performanceobligation-03"),
    (4, "PER-0004", "Enterprise Audited PerformanceObligation 4", 32800.00, 210.0, "ACTIVE", "uuid-performanceobligation-04"),
    (5, "PER-0005", "Executive Strategic PerformanceObligation 5", 65000.00, 400.0, "ACTIVE", "uuid-performanceobligation-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_deferredrevenueamortizations (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_deferredrevenueamortizations_code ON billing_subscriptions_deferredrevenueamortizations(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_deferredrevenueamortizations_org_status ON billing_subscriptions_deferredrevenueamortizations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_deferredrevenueamortizations_priority ON billing_subscriptions_deferredrevenueamortizations(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_deferredrevenueamortizations_created_at ON billing_subscriptions_deferredrevenueamortizations(created_at);

-- Operational seed data fixtures for billing_subscriptions_deferredrevenueamortizations
INSERT OR IGNORE INTO billing_subscriptions_deferredrevenueamortizations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEF-0001", "Primary Operational DeferredRevenueAmortization 1", 24500.00, 150.0, "ACTIVE", "uuid-deferredrevenueamortization-01"),
    (2, "DEF-0002", "Secondary Corporate DeferredRevenueAmortization 2", 18200.50, 80.0, "ACTIVE", "uuid-deferredrevenueamortization-02"),
    (3, "DEF-0003", "Consolidated Branch DeferredRevenueAmortization 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-deferredrevenueamortization-03"),
    (4, "DEF-0004", "Enterprise Audited DeferredRevenueAmortization 4", 32800.00, 210.0, "ACTIVE", "uuid-deferredrevenueamortization-04"),
    (5, "DEF-0005", "Executive Strategic DeferredRevenueAmortization 5", 65000.00, 400.0, "ACTIVE", "uuid-deferredrevenueamortization-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_creditbalanceadjustments (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_creditbalanceadjustments_code ON billing_subscriptions_creditbalanceadjustments(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_creditbalanceadjustments_org_status ON billing_subscriptions_creditbalanceadjustments(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_creditbalanceadjustments_priority ON billing_subscriptions_creditbalanceadjustments(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_creditbalanceadjustments_created_at ON billing_subscriptions_creditbalanceadjustments(created_at);

-- Operational seed data fixtures for billing_subscriptions_creditbalanceadjustments
INSERT OR IGNORE INTO billing_subscriptions_creditbalanceadjustments (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CRE-0001", "Primary Operational CreditBalanceAdjustment 1", 24500.00, 150.0, "ACTIVE", "uuid-creditbalanceadjustment-01"),
    (2, "CRE-0002", "Secondary Corporate CreditBalanceAdjustment 2", 18200.50, 80.0, "ACTIVE", "uuid-creditbalanceadjustment-02"),
    (3, "CRE-0003", "Consolidated Branch CreditBalanceAdjustment 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-creditbalanceadjustment-03"),
    (4, "CRE-0004", "Enterprise Audited CreditBalanceAdjustment 4", 32800.00, 210.0, "ACTIVE", "uuid-creditbalanceadjustment-04"),
    (5, "CRE-0005", "Executive Strategic CreditBalanceAdjustment 5", 65000.00, 400.0, "ACTIVE", "uuid-creditbalanceadjustment-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_churnnotices (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_churnnotices_code ON billing_subscriptions_churnnotices(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_churnnotices_org_status ON billing_subscriptions_churnnotices(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_churnnotices_priority ON billing_subscriptions_churnnotices(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_churnnotices_created_at ON billing_subscriptions_churnnotices(created_at);

-- Operational seed data fixtures for billing_subscriptions_churnnotices
INSERT OR IGNORE INTO billing_subscriptions_churnnotices (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHU-0001", "Primary Operational ChurnNotice 1", 24500.00, 150.0, "ACTIVE", "uuid-churnnotice-01"),
    (2, "CHU-0002", "Secondary Corporate ChurnNotice 2", 18200.50, 80.0, "ACTIVE", "uuid-churnnotice-02"),
    (3, "CHU-0003", "Consolidated Branch ChurnNotice 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-churnnotice-03"),
    (4, "CHU-0004", "Enterprise Audited ChurnNotice 4", 32800.00, 210.0, "ACTIVE", "uuid-churnnotice-04"),
    (5, "CHU-0005", "Executive Strategic ChurnNotice 5", 65000.00, 400.0, "ACTIVE", "uuid-churnnotice-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_usagetiertierings (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_usagetiertierings_code ON billing_subscriptions_usagetiertierings(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_usagetiertierings_org_status ON billing_subscriptions_usagetiertierings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_usagetiertierings_priority ON billing_subscriptions_usagetiertierings(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_usagetiertierings_created_at ON billing_subscriptions_usagetiertierings(created_at);

-- Operational seed data fixtures for billing_subscriptions_usagetiertierings
INSERT OR IGNORE INTO billing_subscriptions_usagetiertierings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USA-0001", "Primary Operational UsageTierTiering 1", 24500.00, 150.0, "ACTIVE", "uuid-usagetiertiering-01"),
    (2, "USA-0002", "Secondary Corporate UsageTierTiering 2", 18200.50, 80.0, "ACTIVE", "uuid-usagetiertiering-02"),
    (3, "USA-0003", "Consolidated Branch UsageTierTiering 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-usagetiertiering-03"),
    (4, "USA-0004", "Enterprise Audited UsageTierTiering 4", 32800.00, 210.0, "ACTIVE", "uuid-usagetiertiering-04"),
    (5, "USA-0005", "Executive Strategic UsageTierTiering 5", 65000.00, 400.0, "ACTIVE", "uuid-usagetiertiering-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_taxjurisdictionrules (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_taxjurisdictionrules_code ON billing_subscriptions_taxjurisdictionrules(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_taxjurisdictionrules_org_status ON billing_subscriptions_taxjurisdictionrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_taxjurisdictionrules_priority ON billing_subscriptions_taxjurisdictionrules(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_taxjurisdictionrules_created_at ON billing_subscriptions_taxjurisdictionrules(created_at);

-- Operational seed data fixtures for billing_subscriptions_taxjurisdictionrules
INSERT OR IGNORE INTO billing_subscriptions_taxjurisdictionrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TAX-0001", "Primary Operational TaxJurisdictionRule 1", 24500.00, 150.0, "ACTIVE", "uuid-taxjurisdictionrule-01"),
    (2, "TAX-0002", "Secondary Corporate TaxJurisdictionRule 2", 18200.50, 80.0, "ACTIVE", "uuid-taxjurisdictionrule-02"),
    (3, "TAX-0003", "Consolidated Branch TaxJurisdictionRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-taxjurisdictionrule-03"),
    (4, "TAX-0004", "Enterprise Audited TaxJurisdictionRule 4", 32800.00, 210.0, "ACTIVE", "uuid-taxjurisdictionrule-04"),
    (5, "TAX-0005", "Executive Strategic TaxJurisdictionRule 5", 65000.00, 400.0, "ACTIVE", "uuid-taxjurisdictionrule-05");

CREATE TABLE IF NOT EXISTS billing_subscriptions_billingreconciliations (
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

CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingreconciliations_code ON billing_subscriptions_billingreconciliations(code);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingreconciliations_org_status ON billing_subscriptions_billingreconciliations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingreconciliations_priority ON billing_subscriptions_billingreconciliations(priority);
CREATE INDEX IF NOT EXISTS idx_billing_subscriptions_billingreconciliations_created_at ON billing_subscriptions_billingreconciliations(created_at);

-- Operational seed data fixtures for billing_subscriptions_billingreconciliations
INSERT OR IGNORE INTO billing_subscriptions_billingreconciliations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BIL-0001", "Primary Operational BillingReconciliation 1", 24500.00, 150.0, "ACTIVE", "uuid-billingreconciliation-01"),
    (2, "BIL-0002", "Secondary Corporate BillingReconciliation 2", 18200.50, 80.0, "ACTIVE", "uuid-billingreconciliation-02"),
    (3, "BIL-0003", "Consolidated Branch BillingReconciliation 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-billingreconciliation-03"),
    (4, "BIL-0004", "Enterprise Audited BillingReconciliation 4", 32800.00, 210.0, "ACTIVE", "uuid-billingreconciliation-04"),
    (5, "BIL-0005", "Executive Strategic BillingReconciliation 5", 65000.00, 400.0, "ACTIVE", "uuid-billingreconciliation-05");

