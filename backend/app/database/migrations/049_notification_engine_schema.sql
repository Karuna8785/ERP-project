-- SmartERP Enterprise Titan Migration 049: Omnichannel Notification & Alert Dispatcher DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS notification_engine_notificationtemplates (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationtemplates_code ON notification_engine_notificationtemplates(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationtemplates_org_status ON notification_engine_notificationtemplates(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationtemplates_priority ON notification_engine_notificationtemplates(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationtemplates_created_at ON notification_engine_notificationtemplates(created_at);

-- Operational seed data fixtures for notification_engine_notificationtemplates
INSERT OR IGNORE INTO notification_engine_notificationtemplates (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "NOT-0001", "Primary Operational NotificationTemplate 1", 24500.00, 150.0, "ACTIVE", "uuid-notificationtemplate-01"),
    (2, "NOT-0002", "Secondary Corporate NotificationTemplate 2", 18200.50, 80.0, "ACTIVE", "uuid-notificationtemplate-02"),
    (3, "NOT-0003", "Consolidated Branch NotificationTemplate 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-notificationtemplate-03"),
    (4, "NOT-0004", "Enterprise Audited NotificationTemplate 4", 32800.00, 210.0, "ACTIVE", "uuid-notificationtemplate-04"),
    (5, "NOT-0005", "Executive Strategic NotificationTemplate 5", 65000.00, 400.0, "ACTIVE", "uuid-notificationtemplate-05");

CREATE TABLE IF NOT EXISTS notification_engine_dispatchmessagequeues (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_dispatchmessagequeues_code ON notification_engine_dispatchmessagequeues(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_dispatchmessagequeues_org_status ON notification_engine_dispatchmessagequeues(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_dispatchmessagequeues_priority ON notification_engine_dispatchmessagequeues(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_dispatchmessagequeues_created_at ON notification_engine_dispatchmessagequeues(created_at);

-- Operational seed data fixtures for notification_engine_dispatchmessagequeues
INSERT OR IGNORE INTO notification_engine_dispatchmessagequeues (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIS-0001", "Primary Operational DispatchMessageQueue 1", 24500.00, 150.0, "ACTIVE", "uuid-dispatchmessagequeue-01"),
    (2, "DIS-0002", "Secondary Corporate DispatchMessageQueue 2", 18200.50, 80.0, "ACTIVE", "uuid-dispatchmessagequeue-02"),
    (3, "DIS-0003", "Consolidated Branch DispatchMessageQueue 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-dispatchmessagequeue-03"),
    (4, "DIS-0004", "Enterprise Audited DispatchMessageQueue 4", 32800.00, 210.0, "ACTIVE", "uuid-dispatchmessagequeue-04"),
    (5, "DIS-0005", "Executive Strategic DispatchMessageQueue 5", 65000.00, 400.0, "ACTIVE", "uuid-dispatchmessagequeue-05");

CREATE TABLE IF NOT EXISTS notification_engine_deliveryattemptlogs (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_deliveryattemptlogs_code ON notification_engine_deliveryattemptlogs(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_deliveryattemptlogs_org_status ON notification_engine_deliveryattemptlogs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_deliveryattemptlogs_priority ON notification_engine_deliveryattemptlogs(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_deliveryattemptlogs_created_at ON notification_engine_deliveryattemptlogs(created_at);

-- Operational seed data fixtures for notification_engine_deliveryattemptlogs
INSERT OR IGNORE INTO notification_engine_deliveryattemptlogs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DEL-0001", "Primary Operational DeliveryAttemptLog 1", 24500.00, 150.0, "ACTIVE", "uuid-deliveryattemptlog-01"),
    (2, "DEL-0002", "Secondary Corporate DeliveryAttemptLog 2", 18200.50, 80.0, "ACTIVE", "uuid-deliveryattemptlog-02"),
    (3, "DEL-0003", "Consolidated Branch DeliveryAttemptLog 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-deliveryattemptlog-03"),
    (4, "DEL-0004", "Enterprise Audited DeliveryAttemptLog 4", 32800.00, 210.0, "ACTIVE", "uuid-deliveryattemptlog-04"),
    (5, "DEL-0005", "Executive Strategic DeliveryAttemptLog 5", 65000.00, 400.0, "ACTIVE", "uuid-deliveryattemptlog-05");

CREATE TABLE IF NOT EXISTS notification_engine_userchannelpreferences (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_userchannelpreferences_code ON notification_engine_userchannelpreferences(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_userchannelpreferences_org_status ON notification_engine_userchannelpreferences(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_userchannelpreferences_priority ON notification_engine_userchannelpreferences(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_userchannelpreferences_created_at ON notification_engine_userchannelpreferences(created_at);

-- Operational seed data fixtures for notification_engine_userchannelpreferences
INSERT OR IGNORE INTO notification_engine_userchannelpreferences (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "USE-0001", "Primary Operational UserChannelPreference 1", 24500.00, 150.0, "ACTIVE", "uuid-userchannelpreference-01"),
    (2, "USE-0002", "Secondary Corporate UserChannelPreference 2", 18200.50, 80.0, "ACTIVE", "uuid-userchannelpreference-02"),
    (3, "USE-0003", "Consolidated Branch UserChannelPreference 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-userchannelpreference-03"),
    (4, "USE-0004", "Enterprise Audited UserChannelPreference 4", 32800.00, 210.0, "ACTIVE", "uuid-userchannelpreference-04"),
    (5, "USE-0005", "Executive Strategic UserChannelPreference 5", 65000.00, 400.0, "ACTIVE", "uuid-userchannelpreference-05");

CREATE TABLE IF NOT EXISTS notification_engine_emailtransportconfigs (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_emailtransportconfigs_code ON notification_engine_emailtransportconfigs(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_emailtransportconfigs_org_status ON notification_engine_emailtransportconfigs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_emailtransportconfigs_priority ON notification_engine_emailtransportconfigs(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_emailtransportconfigs_created_at ON notification_engine_emailtransportconfigs(created_at);

-- Operational seed data fixtures for notification_engine_emailtransportconfigs
INSERT OR IGNORE INTO notification_engine_emailtransportconfigs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "EMA-0001", "Primary Operational EmailTransportConfig 1", 24500.00, 150.0, "ACTIVE", "uuid-emailtransportconfig-01"),
    (2, "EMA-0002", "Secondary Corporate EmailTransportConfig 2", 18200.50, 80.0, "ACTIVE", "uuid-emailtransportconfig-02"),
    (3, "EMA-0003", "Consolidated Branch EmailTransportConfig 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-emailtransportconfig-03"),
    (4, "EMA-0004", "Enterprise Audited EmailTransportConfig 4", 32800.00, 210.0, "ACTIVE", "uuid-emailtransportconfig-04"),
    (5, "EMA-0005", "Executive Strategic EmailTransportConfig 5", 65000.00, 400.0, "ACTIVE", "uuid-emailtransportconfig-05");

CREATE TABLE IF NOT EXISTS notification_engine_smsgatewayproviders (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_smsgatewayproviders_code ON notification_engine_smsgatewayproviders(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_smsgatewayproviders_org_status ON notification_engine_smsgatewayproviders(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_smsgatewayproviders_priority ON notification_engine_smsgatewayproviders(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_smsgatewayproviders_created_at ON notification_engine_smsgatewayproviders(created_at);

-- Operational seed data fixtures for notification_engine_smsgatewayproviders
INSERT OR IGNORE INTO notification_engine_smsgatewayproviders (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SMS-0001", "Primary Operational SMSGatewayProvider 1", 24500.00, 150.0, "ACTIVE", "uuid-smsgatewayprovider-01"),
    (2, "SMS-0002", "Secondary Corporate SMSGatewayProvider 2", 18200.50, 80.0, "ACTIVE", "uuid-smsgatewayprovider-02"),
    (3, "SMS-0003", "Consolidated Branch SMSGatewayProvider 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-smsgatewayprovider-03"),
    (4, "SMS-0004", "Enterprise Audited SMSGatewayProvider 4", 32800.00, 210.0, "ACTIVE", "uuid-smsgatewayprovider-04"),
    (5, "SMS-0005", "Executive Strategic SMSGatewayProvider 5", 65000.00, 400.0, "ACTIVE", "uuid-smsgatewayprovider-05");

CREATE TABLE IF NOT EXISTS notification_engine_pushnotificationtokens (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_pushnotificationtokens_code ON notification_engine_pushnotificationtokens(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_pushnotificationtokens_org_status ON notification_engine_pushnotificationtokens(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_pushnotificationtokens_priority ON notification_engine_pushnotificationtokens(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_pushnotificationtokens_created_at ON notification_engine_pushnotificationtokens(created_at);

-- Operational seed data fixtures for notification_engine_pushnotificationtokens
INSERT OR IGNORE INTO notification_engine_pushnotificationtokens (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "PUS-0001", "Primary Operational PushNotificationToken 1", 24500.00, 150.0, "ACTIVE", "uuid-pushnotificationtoken-01"),
    (2, "PUS-0002", "Secondary Corporate PushNotificationToken 2", 18200.50, 80.0, "ACTIVE", "uuid-pushnotificationtoken-02"),
    (3, "PUS-0003", "Consolidated Branch PushNotificationToken 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-pushnotificationtoken-03"),
    (4, "PUS-0004", "Enterprise Audited PushNotificationToken 4", 32800.00, 210.0, "ACTIVE", "uuid-pushnotificationtoken-04"),
    (5, "PUS-0005", "Executive Strategic PushNotificationToken 5", 65000.00, 400.0, "ACTIVE", "uuid-pushnotificationtoken-05");

CREATE TABLE IF NOT EXISTS notification_engine_inappnotificationfeeds (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_inappnotificationfeeds_code ON notification_engine_inappnotificationfeeds(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_inappnotificationfeeds_org_status ON notification_engine_inappnotificationfeeds(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_inappnotificationfeeds_priority ON notification_engine_inappnotificationfeeds(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_inappnotificationfeeds_created_at ON notification_engine_inappnotificationfeeds(created_at);

-- Operational seed data fixtures for notification_engine_inappnotificationfeeds
INSERT OR IGNORE INTO notification_engine_inappnotificationfeeds (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INA-0001", "Primary Operational InAppNotificationFeed 1", 24500.00, 150.0, "ACTIVE", "uuid-inappnotificationfeed-01"),
    (2, "INA-0002", "Secondary Corporate InAppNotificationFeed 2", 18200.50, 80.0, "ACTIVE", "uuid-inappnotificationfeed-02"),
    (3, "INA-0003", "Consolidated Branch InAppNotificationFeed 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-inappnotificationfeed-03"),
    (4, "INA-0004", "Enterprise Audited InAppNotificationFeed 4", 32800.00, 210.0, "ACTIVE", "uuid-inappnotificationfeed-04"),
    (5, "INA-0005", "Executive Strategic InAppNotificationFeed 5", 65000.00, 400.0, "ACTIVE", "uuid-inappnotificationfeed-05");

CREATE TABLE IF NOT EXISTS notification_engine_webhookdispatchtargets (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_webhookdispatchtargets_code ON notification_engine_webhookdispatchtargets(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_webhookdispatchtargets_org_status ON notification_engine_webhookdispatchtargets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_webhookdispatchtargets_priority ON notification_engine_webhookdispatchtargets(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_webhookdispatchtargets_created_at ON notification_engine_webhookdispatchtargets(created_at);

-- Operational seed data fixtures for notification_engine_webhookdispatchtargets
INSERT OR IGNORE INTO notification_engine_webhookdispatchtargets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WEB-0001", "Primary Operational WebhookDispatchTarget 1", 24500.00, 150.0, "ACTIVE", "uuid-webhookdispatchtarget-01"),
    (2, "WEB-0002", "Secondary Corporate WebhookDispatchTarget 2", 18200.50, 80.0, "ACTIVE", "uuid-webhookdispatchtarget-02"),
    (3, "WEB-0003", "Consolidated Branch WebhookDispatchTarget 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-webhookdispatchtarget-03"),
    (4, "WEB-0004", "Enterprise Audited WebhookDispatchTarget 4", 32800.00, 210.0, "ACTIVE", "uuid-webhookdispatchtarget-04"),
    (5, "WEB-0005", "Executive Strategic WebhookDispatchTarget 5", 65000.00, 400.0, "ACTIVE", "uuid-webhookdispatchtarget-05");

CREATE TABLE IF NOT EXISTS notification_engine_notificationcategorygroups (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationcategorygroups_code ON notification_engine_notificationcategorygroups(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationcategorygroups_org_status ON notification_engine_notificationcategorygroups(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationcategorygroups_priority ON notification_engine_notificationcategorygroups(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_notificationcategorygroups_created_at ON notification_engine_notificationcategorygroups(created_at);

-- Operational seed data fixtures for notification_engine_notificationcategorygroups
INSERT OR IGNORE INTO notification_engine_notificationcategorygroups (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "NOT-0001", "Primary Operational NotificationCategoryGroup 1", 24500.00, 150.0, "ACTIVE", "uuid-notificationcategorygroup-01"),
    (2, "NOT-0002", "Secondary Corporate NotificationCategoryGroup 2", 18200.50, 80.0, "ACTIVE", "uuid-notificationcategorygroup-02"),
    (3, "NOT-0003", "Consolidated Branch NotificationCategoryGroup 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-notificationcategorygroup-03"),
    (4, "NOT-0004", "Enterprise Audited NotificationCategoryGroup 4", 32800.00, 210.0, "ACTIVE", "uuid-notificationcategorygroup-04"),
    (5, "NOT-0005", "Executive Strategic NotificationCategoryGroup 5", 65000.00, 400.0, "ACTIVE", "uuid-notificationcategorygroup-05");

CREATE TABLE IF NOT EXISTS notification_engine_ratelimitthrottlerules (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_ratelimitthrottlerules_code ON notification_engine_ratelimitthrottlerules(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_ratelimitthrottlerules_org_status ON notification_engine_ratelimitthrottlerules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_ratelimitthrottlerules_priority ON notification_engine_ratelimitthrottlerules(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_ratelimitthrottlerules_created_at ON notification_engine_ratelimitthrottlerules(created_at);

-- Operational seed data fixtures for notification_engine_ratelimitthrottlerules
INSERT OR IGNORE INTO notification_engine_ratelimitthrottlerules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RAT-0001", "Primary Operational RateLimitThrottleRule 1", 24500.00, 150.0, "ACTIVE", "uuid-ratelimitthrottlerule-01"),
    (2, "RAT-0002", "Secondary Corporate RateLimitThrottleRule 2", 18200.50, 80.0, "ACTIVE", "uuid-ratelimitthrottlerule-02"),
    (3, "RAT-0003", "Consolidated Branch RateLimitThrottleRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ratelimitthrottlerule-03"),
    (4, "RAT-0004", "Enterprise Audited RateLimitThrottleRule 4", 32800.00, 210.0, "ACTIVE", "uuid-ratelimitthrottlerule-04"),
    (5, "RAT-0005", "Executive Strategic RateLimitThrottleRule 5", 65000.00, 400.0, "ACTIVE", "uuid-ratelimitthrottlerule-05");

CREATE TABLE IF NOT EXISTS notification_engine_optoutsubscriptionlists (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_optoutsubscriptionlists_code ON notification_engine_optoutsubscriptionlists(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_optoutsubscriptionlists_org_status ON notification_engine_optoutsubscriptionlists(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_optoutsubscriptionlists_priority ON notification_engine_optoutsubscriptionlists(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_optoutsubscriptionlists_created_at ON notification_engine_optoutsubscriptionlists(created_at);

-- Operational seed data fixtures for notification_engine_optoutsubscriptionlists
INSERT OR IGNORE INTO notification_engine_optoutsubscriptionlists (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "OPT-0001", "Primary Operational OptOutSubscriptionList 1", 24500.00, 150.0, "ACTIVE", "uuid-optoutsubscriptionlist-01"),
    (2, "OPT-0002", "Secondary Corporate OptOutSubscriptionList 2", 18200.50, 80.0, "ACTIVE", "uuid-optoutsubscriptionlist-02"),
    (3, "OPT-0003", "Consolidated Branch OptOutSubscriptionList 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-optoutsubscriptionlist-03"),
    (4, "OPT-0004", "Enterprise Audited OptOutSubscriptionList 4", 32800.00, 210.0, "ACTIVE", "uuid-optoutsubscriptionlist-04"),
    (5, "OPT-0005", "Executive Strategic OptOutSubscriptionList 5", 65000.00, 400.0, "ACTIVE", "uuid-optoutsubscriptionlist-05");

CREATE TABLE IF NOT EXISTS notification_engine_templatelocalizationitems (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_templatelocalizationitems_code ON notification_engine_templatelocalizationitems(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_templatelocalizationitems_org_status ON notification_engine_templatelocalizationitems(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_templatelocalizationitems_priority ON notification_engine_templatelocalizationitems(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_templatelocalizationitems_created_at ON notification_engine_templatelocalizationitems(created_at);

-- Operational seed data fixtures for notification_engine_templatelocalizationitems
INSERT OR IGNORE INTO notification_engine_templatelocalizationitems (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TEM-0001", "Primary Operational TemplateLocalizationItem 1", 24500.00, 150.0, "ACTIVE", "uuid-templatelocalizationitem-01"),
    (2, "TEM-0002", "Secondary Corporate TemplateLocalizationItem 2", 18200.50, 80.0, "ACTIVE", "uuid-templatelocalizationitem-02"),
    (3, "TEM-0003", "Consolidated Branch TemplateLocalizationItem 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-templatelocalizationitem-03"),
    (4, "TEM-0004", "Enterprise Audited TemplateLocalizationItem 4", 32800.00, 210.0, "ACTIVE", "uuid-templatelocalizationitem-04"),
    (5, "TEM-0005", "Executive Strategic TemplateLocalizationItem 5", 65000.00, 400.0, "ACTIVE", "uuid-templatelocalizationitem-05");

CREATE TABLE IF NOT EXISTS notification_engine_digestaggregationschedules (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_digestaggregationschedules_code ON notification_engine_digestaggregationschedules(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_digestaggregationschedules_org_status ON notification_engine_digestaggregationschedules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_digestaggregationschedules_priority ON notification_engine_digestaggregationschedules(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_digestaggregationschedules_created_at ON notification_engine_digestaggregationschedules(created_at);

-- Operational seed data fixtures for notification_engine_digestaggregationschedules
INSERT OR IGNORE INTO notification_engine_digestaggregationschedules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "DIG-0001", "Primary Operational DigestAggregationSchedule 1", 24500.00, 150.0, "ACTIVE", "uuid-digestaggregationschedule-01"),
    (2, "DIG-0002", "Secondary Corporate DigestAggregationSchedule 2", 18200.50, 80.0, "ACTIVE", "uuid-digestaggregationschedule-02"),
    (3, "DIG-0003", "Consolidated Branch DigestAggregationSchedule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-digestaggregationschedule-03"),
    (4, "DIG-0004", "Enterprise Audited DigestAggregationSchedule 4", 32800.00, 210.0, "ACTIVE", "uuid-digestaggregationschedule-04"),
    (5, "DIG-0005", "Executive Strategic DigestAggregationSchedule 5", 65000.00, 400.0, "ACTIVE", "uuid-digestaggregationschedule-05");

CREATE TABLE IF NOT EXISTS notification_engine_bouncefailurereports (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_bouncefailurereports_code ON notification_engine_bouncefailurereports(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_bouncefailurereports_org_status ON notification_engine_bouncefailurereports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_bouncefailurereports_priority ON notification_engine_bouncefailurereports(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_bouncefailurereports_created_at ON notification_engine_bouncefailurereports(created_at);

-- Operational seed data fixtures for notification_engine_bouncefailurereports
INSERT OR IGNORE INTO notification_engine_bouncefailurereports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "BOU-0001", "Primary Operational BounceFailureReport 1", 24500.00, 150.0, "ACTIVE", "uuid-bouncefailurereport-01"),
    (2, "BOU-0002", "Secondary Corporate BounceFailureReport 2", 18200.50, 80.0, "ACTIVE", "uuid-bouncefailurereport-02"),
    (3, "BOU-0003", "Consolidated Branch BounceFailureReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-bouncefailurereport-03"),
    (4, "BOU-0004", "Enterprise Audited BounceFailureReport 4", 32800.00, 210.0, "ACTIVE", "uuid-bouncefailurereport-04"),
    (5, "BOU-0005", "Executive Strategic BounceFailureReport 5", 65000.00, 400.0, "ACTIVE", "uuid-bouncefailurereport-05");

CREATE TABLE IF NOT EXISTS notification_engine_engagementclicktrackers (
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

CREATE INDEX IF NOT EXISTS idx_notification_engine_engagementclicktrackers_code ON notification_engine_engagementclicktrackers(code);
CREATE INDEX IF NOT EXISTS idx_notification_engine_engagementclicktrackers_org_status ON notification_engine_engagementclicktrackers(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_notification_engine_engagementclicktrackers_priority ON notification_engine_engagementclicktrackers(priority);
CREATE INDEX IF NOT EXISTS idx_notification_engine_engagementclicktrackers_created_at ON notification_engine_engagementclicktrackers(created_at);

-- Operational seed data fixtures for notification_engine_engagementclicktrackers
INSERT OR IGNORE INTO notification_engine_engagementclicktrackers (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ENG-0001", "Primary Operational EngagementClickTracker 1", 24500.00, 150.0, "ACTIVE", "uuid-engagementclicktracker-01"),
    (2, "ENG-0002", "Secondary Corporate EngagementClickTracker 2", 18200.50, 80.0, "ACTIVE", "uuid-engagementclicktracker-02"),
    (3, "ENG-0003", "Consolidated Branch EngagementClickTracker 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-engagementclicktracker-03"),
    (4, "ENG-0004", "Enterprise Audited EngagementClickTracker 4", 32800.00, 210.0, "ACTIVE", "uuid-engagementclicktracker-04"),
    (5, "ENG-0005", "Executive Strategic EngagementClickTracker 5", 65000.00, 400.0, "ACTIVE", "uuid-engagementclicktracker-05");

