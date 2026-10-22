-- SmartERP Enterprise Titan Migration 006: Enterprise Service Desk & SLA Management DDL Schema
-- High-throughput relational database tables with indexes, foreign keys, and audit fixtures

CREATE TABLE IF NOT EXISTS helpdesk_supporttickets (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_supporttickets_code ON helpdesk_supporttickets(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_supporttickets_org_status ON helpdesk_supporttickets(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_supporttickets_priority ON helpdesk_supporttickets(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_supporttickets_created_at ON helpdesk_supporttickets(created_at);

-- Operational seed data fixtures for helpdesk_supporttickets
INSERT OR IGNORE INTO helpdesk_supporttickets (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SUP-0001", "Primary Operational SupportTicket 1", 24500.00, 150.0, "ACTIVE", "uuid-supportticket-01"),
    (2, "SUP-0002", "Secondary Corporate SupportTicket 2", 18200.50, 80.0, "ACTIVE", "uuid-supportticket-02"),
    (3, "SUP-0003", "Consolidated Branch SupportTicket 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-supportticket-03"),
    (4, "SUP-0004", "Enterprise Audited SupportTicket 4", 32800.00, 210.0, "ACTIVE", "uuid-supportticket-04"),
    (5, "SUP-0005", "Executive Strategic SupportTicket 5", 65000.00, 400.0, "ACTIVE", "uuid-supportticket-05");

CREATE TABLE IF NOT EXISTS helpdesk_ticketmessages (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketmessages_code ON helpdesk_ticketmessages(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketmessages_org_status ON helpdesk_ticketmessages(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketmessages_priority ON helpdesk_ticketmessages(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketmessages_created_at ON helpdesk_ticketmessages(created_at);

-- Operational seed data fixtures for helpdesk_ticketmessages
INSERT OR IGNORE INTO helpdesk_ticketmessages (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIC-0001", "Primary Operational TicketMessage 1", 24500.00, 150.0, "ACTIVE", "uuid-ticketmessage-01"),
    (2, "TIC-0002", "Secondary Corporate TicketMessage 2", 18200.50, 80.0, "ACTIVE", "uuid-ticketmessage-02"),
    (3, "TIC-0003", "Consolidated Branch TicketMessage 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ticketmessage-03"),
    (4, "TIC-0004", "Enterprise Audited TicketMessage 4", 32800.00, 210.0, "ACTIVE", "uuid-ticketmessage-04"),
    (5, "TIC-0005", "Executive Strategic TicketMessage 5", 65000.00, 400.0, "ACTIVE", "uuid-ticketmessage-05");

CREATE TABLE IF NOT EXISTS helpdesk_slapolicys (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_slapolicys_code ON helpdesk_slapolicys(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_slapolicys_org_status ON helpdesk_slapolicys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_slapolicys_priority ON helpdesk_slapolicys(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_slapolicys_created_at ON helpdesk_slapolicys(created_at);

-- Operational seed data fixtures for helpdesk_slapolicys
INSERT OR IGNORE INTO helpdesk_slapolicys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SLA-0001", "Primary Operational SLAPolicy 1", 24500.00, 150.0, "ACTIVE", "uuid-slapolicy-01"),
    (2, "SLA-0002", "Secondary Corporate SLAPolicy 2", 18200.50, 80.0, "ACTIVE", "uuid-slapolicy-02"),
    (3, "SLA-0003", "Consolidated Branch SLAPolicy 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-slapolicy-03"),
    (4, "SLA-0004", "Enterprise Audited SLAPolicy 4", 32800.00, 210.0, "ACTIVE", "uuid-slapolicy-04"),
    (5, "SLA-0005", "Executive Strategic SLAPolicy 5", 65000.00, 400.0, "ACTIVE", "uuid-slapolicy-05");

CREATE TABLE IF NOT EXISTS helpdesk_escalationrules (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_escalationrules_code ON helpdesk_escalationrules(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_escalationrules_org_status ON helpdesk_escalationrules(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_escalationrules_priority ON helpdesk_escalationrules(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_escalationrules_created_at ON helpdesk_escalationrules(created_at);

-- Operational seed data fixtures for helpdesk_escalationrules
INSERT OR IGNORE INTO helpdesk_escalationrules (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "ESC-0001", "Primary Operational EscalationRule 1", 24500.00, 150.0, "ACTIVE", "uuid-escalationrule-01"),
    (2, "ESC-0002", "Secondary Corporate EscalationRule 2", 18200.50, 80.0, "ACTIVE", "uuid-escalationrule-02"),
    (3, "ESC-0003", "Consolidated Branch EscalationRule 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-escalationrule-03"),
    (4, "ESC-0004", "Enterprise Audited EscalationRule 4", 32800.00, 210.0, "ACTIVE", "uuid-escalationrule-04"),
    (5, "ESC-0005", "Executive Strategic EscalationRule 5", 65000.00, 400.0, "ACTIVE", "uuid-escalationrule-05");

CREATE TABLE IF NOT EXISTS helpdesk_ticketcategorys (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketcategorys_code ON helpdesk_ticketcategorys(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketcategorys_org_status ON helpdesk_ticketcategorys(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketcategorys_priority ON helpdesk_ticketcategorys(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_ticketcategorys_created_at ON helpdesk_ticketcategorys(created_at);

-- Operational seed data fixtures for helpdesk_ticketcategorys
INSERT OR IGNORE INTO helpdesk_ticketcategorys (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIC-0001", "Primary Operational TicketCategory 1", 24500.00, 150.0, "ACTIVE", "uuid-ticketcategory-01"),
    (2, "TIC-0002", "Secondary Corporate TicketCategory 2", 18200.50, 80.0, "ACTIVE", "uuid-ticketcategory-02"),
    (3, "TIC-0003", "Consolidated Branch TicketCategory 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-ticketcategory-03"),
    (4, "TIC-0004", "Enterprise Audited TicketCategory 4", 32800.00, 210.0, "ACTIVE", "uuid-ticketcategory-04"),
    (5, "TIC-0005", "Executive Strategic TicketCategory 5", 65000.00, 400.0, "ACTIVE", "uuid-ticketcategory-05");

CREATE TABLE IF NOT EXISTS helpdesk_cannedresponses (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_cannedresponses_code ON helpdesk_cannedresponses(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_cannedresponses_org_status ON helpdesk_cannedresponses(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_cannedresponses_priority ON helpdesk_cannedresponses(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_cannedresponses_created_at ON helpdesk_cannedresponses(created_at);

-- Operational seed data fixtures for helpdesk_cannedresponses
INSERT OR IGNORE INTO helpdesk_cannedresponses (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CAN-0001", "Primary Operational CannedResponse 1", 24500.00, 150.0, "ACTIVE", "uuid-cannedresponse-01"),
    (2, "CAN-0002", "Secondary Corporate CannedResponse 2", 18200.50, 80.0, "ACTIVE", "uuid-cannedresponse-02"),
    (3, "CAN-0003", "Consolidated Branch CannedResponse 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-cannedresponse-03"),
    (4, "CAN-0004", "Enterprise Audited CannedResponse 4", 32800.00, 210.0, "ACTIVE", "uuid-cannedresponse-04"),
    (5, "CAN-0005", "Executive Strategic CannedResponse 5", 65000.00, 400.0, "ACTIVE", "uuid-cannedresponse-05");

CREATE TABLE IF NOT EXISTS helpdesk_knowledgearticles (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_knowledgearticles_code ON helpdesk_knowledgearticles(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_knowledgearticles_org_status ON helpdesk_knowledgearticles(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_knowledgearticles_priority ON helpdesk_knowledgearticles(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_knowledgearticles_created_at ON helpdesk_knowledgearticles(created_at);

-- Operational seed data fixtures for helpdesk_knowledgearticles
INSERT OR IGNORE INTO helpdesk_knowledgearticles (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "KNO-0001", "Primary Operational KnowledgeArticle 1", 24500.00, 150.0, "ACTIVE", "uuid-knowledgearticle-01"),
    (2, "KNO-0002", "Secondary Corporate KnowledgeArticle 2", 18200.50, 80.0, "ACTIVE", "uuid-knowledgearticle-02"),
    (3, "KNO-0003", "Consolidated Branch KnowledgeArticle 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-knowledgearticle-03"),
    (4, "KNO-0004", "Enterprise Audited KnowledgeArticle 4", 32800.00, 210.0, "ACTIVE", "uuid-knowledgearticle-04"),
    (5, "KNO-0005", "Executive Strategic KnowledgeArticle 5", 65000.00, 400.0, "ACTIVE", "uuid-knowledgearticle-05");

CREATE TABLE IF NOT EXISTS helpdesk_customersatisfactions (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_customersatisfactions_code ON helpdesk_customersatisfactions(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_customersatisfactions_org_status ON helpdesk_customersatisfactions(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_customersatisfactions_priority ON helpdesk_customersatisfactions(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_customersatisfactions_created_at ON helpdesk_customersatisfactions(created_at);

-- Operational seed data fixtures for helpdesk_customersatisfactions
INSERT OR IGNORE INTO helpdesk_customersatisfactions (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CUS-0001", "Primary Operational CustomerSatisfaction 1", 24500.00, 150.0, "ACTIVE", "uuid-customersatisfaction-01"),
    (2, "CUS-0002", "Secondary Corporate CustomerSatisfaction 2", 18200.50, 80.0, "ACTIVE", "uuid-customersatisfaction-02"),
    (3, "CUS-0003", "Consolidated Branch CustomerSatisfaction 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-customersatisfaction-03"),
    (4, "CUS-0004", "Enterprise Audited CustomerSatisfaction 4", 32800.00, 210.0, "ACTIVE", "uuid-customersatisfaction-04"),
    (5, "CUS-0005", "Executive Strategic CustomerSatisfaction 5", 65000.00, 400.0, "ACTIVE", "uuid-customersatisfaction-05");

CREATE TABLE IF NOT EXISTS helpdesk_warrantyclaims (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_warrantyclaims_code ON helpdesk_warrantyclaims(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_warrantyclaims_org_status ON helpdesk_warrantyclaims(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_warrantyclaims_priority ON helpdesk_warrantyclaims(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_warrantyclaims_created_at ON helpdesk_warrantyclaims(created_at);

-- Operational seed data fixtures for helpdesk_warrantyclaims
INSERT OR IGNORE INTO helpdesk_warrantyclaims (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "WAR-0001", "Primary Operational WarrantyClaim 1", 24500.00, 150.0, "ACTIVE", "uuid-warrantyclaim-01"),
    (2, "WAR-0002", "Secondary Corporate WarrantyClaim 2", 18200.50, 80.0, "ACTIVE", "uuid-warrantyclaim-02"),
    (3, "WAR-0003", "Consolidated Branch WarrantyClaim 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-warrantyclaim-03"),
    (4, "WAR-0004", "Enterprise Audited WarrantyClaim 4", 32800.00, 210.0, "ACTIVE", "uuid-warrantyclaim-04"),
    (5, "WAR-0005", "Executive Strategic WarrantyClaim 5", 65000.00, 400.0, "ACTIVE", "uuid-warrantyclaim-05");

CREATE TABLE IF NOT EXISTS helpdesk_rmaauthorizations (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_rmaauthorizations_code ON helpdesk_rmaauthorizations(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_rmaauthorizations_org_status ON helpdesk_rmaauthorizations(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_rmaauthorizations_priority ON helpdesk_rmaauthorizations(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_rmaauthorizations_created_at ON helpdesk_rmaauthorizations(created_at);

-- Operational seed data fixtures for helpdesk_rmaauthorizations
INSERT OR IGNORE INTO helpdesk_rmaauthorizations (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "RMA-0001", "Primary Operational RMAAuthorization 1", 24500.00, 150.0, "ACTIVE", "uuid-rmaauthorization-01"),
    (2, "RMA-0002", "Secondary Corporate RMAAuthorization 2", 18200.50, 80.0, "ACTIVE", "uuid-rmaauthorization-02"),
    (3, "RMA-0003", "Consolidated Branch RMAAuthorization 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-rmaauthorization-03"),
    (4, "RMA-0004", "Enterprise Audited RMAAuthorization 4", 32800.00, 210.0, "ACTIVE", "uuid-rmaauthorization-04"),
    (5, "RMA-0005", "Executive Strategic RMAAuthorization 5", 65000.00, 400.0, "ACTIVE", "uuid-rmaauthorization-05");

CREATE TABLE IF NOT EXISTS helpdesk_servicecontracts (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_servicecontracts_code ON helpdesk_servicecontracts(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_servicecontracts_org_status ON helpdesk_servicecontracts(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_servicecontracts_priority ON helpdesk_servicecontracts(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_servicecontracts_created_at ON helpdesk_servicecontracts(created_at);

-- Operational seed data fixtures for helpdesk_servicecontracts
INSERT OR IGNORE INTO helpdesk_servicecontracts (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "SER-0001", "Primary Operational ServiceContract 1", 24500.00, 150.0, "ACTIVE", "uuid-servicecontract-01"),
    (2, "SER-0002", "Secondary Corporate ServiceContract 2", 18200.50, 80.0, "ACTIVE", "uuid-servicecontract-02"),
    (3, "SER-0003", "Consolidated Branch ServiceContract 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-servicecontract-03"),
    (4, "SER-0004", "Enterprise Audited ServiceContract 4", 32800.00, 210.0, "ACTIVE", "uuid-servicecontract-04"),
    (5, "SER-0005", "Executive Strategic ServiceContract 5", 65000.00, 400.0, "ACTIVE", "uuid-servicecontract-05");

CREATE TABLE IF NOT EXISTS helpdesk_agentworkloads (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_agentworkloads_code ON helpdesk_agentworkloads(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_agentworkloads_org_status ON helpdesk_agentworkloads(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_agentworkloads_priority ON helpdesk_agentworkloads(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_agentworkloads_created_at ON helpdesk_agentworkloads(created_at);

-- Operational seed data fixtures for helpdesk_agentworkloads
INSERT OR IGNORE INTO helpdesk_agentworkloads (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "AGE-0001", "Primary Operational AgentWorkload 1", 24500.00, 150.0, "ACTIVE", "uuid-agentworkload-01"),
    (2, "AGE-0002", "Secondary Corporate AgentWorkload 2", 18200.50, 80.0, "ACTIVE", "uuid-agentworkload-02"),
    (3, "AGE-0003", "Consolidated Branch AgentWorkload 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-agentworkload-03"),
    (4, "AGE-0004", "Enterprise Audited AgentWorkload 4", 32800.00, 210.0, "ACTIVE", "uuid-agentworkload-04"),
    (5, "AGE-0005", "Executive Strategic AgentWorkload 5", 65000.00, 400.0, "ACTIVE", "uuid-agentworkload-05");

CREATE TABLE IF NOT EXISTS helpdesk_timetrackings (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_timetrackings_code ON helpdesk_timetrackings(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_timetrackings_org_status ON helpdesk_timetrackings(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_timetrackings_priority ON helpdesk_timetrackings(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_timetrackings_created_at ON helpdesk_timetrackings(created_at);

-- Operational seed data fixtures for helpdesk_timetrackings
INSERT OR IGNORE INTO helpdesk_timetrackings (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "TIM-0001", "Primary Operational TimeTracking 1", 24500.00, 150.0, "ACTIVE", "uuid-timetracking-01"),
    (2, "TIM-0002", "Secondary Corporate TimeTracking 2", 18200.50, 80.0, "ACTIVE", "uuid-timetracking-02"),
    (3, "TIM-0003", "Consolidated Branch TimeTracking 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-timetracking-03"),
    (4, "TIM-0004", "Enterprise Audited TimeTracking 4", 32800.00, 210.0, "ACTIVE", "uuid-timetracking-04"),
    (5, "TIM-0005", "Executive Strategic TimeTracking 5", 65000.00, 400.0, "ACTIVE", "uuid-timetracking-05");

CREATE TABLE IF NOT EXISTS helpdesk_fieldservicejobs (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_fieldservicejobs_code ON helpdesk_fieldservicejobs(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_fieldservicejobs_org_status ON helpdesk_fieldservicejobs(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_fieldservicejobs_priority ON helpdesk_fieldservicejobs(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_fieldservicejobs_created_at ON helpdesk_fieldservicejobs(created_at);

-- Operational seed data fixtures for helpdesk_fieldservicejobs
INSERT OR IGNORE INTO helpdesk_fieldservicejobs (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "FIE-0001", "Primary Operational FieldServiceJob 1", 24500.00, 150.0, "ACTIVE", "uuid-fieldservicejob-01"),
    (2, "FIE-0002", "Secondary Corporate FieldServiceJob 2", 18200.50, 80.0, "ACTIVE", "uuid-fieldservicejob-02"),
    (3, "FIE-0003", "Consolidated Branch FieldServiceJob 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-fieldservicejob-03"),
    (4, "FIE-0004", "Enterprise Audited FieldServiceJob 4", 32800.00, 210.0, "ACTIVE", "uuid-fieldservicejob-04"),
    (5, "FIE-0005", "Executive Strategic FieldServiceJob 5", 65000.00, 400.0, "ACTIVE", "uuid-fieldservicejob-05");

CREATE TABLE IF NOT EXISTS helpdesk_incidentreports (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_incidentreports_code ON helpdesk_incidentreports(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_incidentreports_org_status ON helpdesk_incidentreports(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_incidentreports_priority ON helpdesk_incidentreports(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_incidentreports_created_at ON helpdesk_incidentreports(created_at);

-- Operational seed data fixtures for helpdesk_incidentreports
INSERT OR IGNORE INTO helpdesk_incidentreports (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "INC-0001", "Primary Operational IncidentReport 1", 24500.00, 150.0, "ACTIVE", "uuid-incidentreport-01"),
    (2, "INC-0002", "Secondary Corporate IncidentReport 2", 18200.50, 80.0, "ACTIVE", "uuid-incidentreport-02"),
    (3, "INC-0003", "Consolidated Branch IncidentReport 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-incidentreport-03"),
    (4, "INC-0004", "Enterprise Audited IncidentReport 4", 32800.00, 210.0, "ACTIVE", "uuid-incidentreport-04"),
    (5, "INC-0005", "Executive Strategic IncidentReport 5", 65000.00, 400.0, "ACTIVE", "uuid-incidentreport-05");

CREATE TABLE IF NOT EXISTS helpdesk_changerequests (
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

CREATE INDEX IF NOT EXISTS idx_helpdesk_changerequests_code ON helpdesk_changerequests(code);
CREATE INDEX IF NOT EXISTS idx_helpdesk_changerequests_org_status ON helpdesk_changerequests(organization_id, status);
CREATE INDEX IF NOT EXISTS idx_helpdesk_changerequests_priority ON helpdesk_changerequests(priority);
CREATE INDEX IF NOT EXISTS idx_helpdesk_changerequests_created_at ON helpdesk_changerequests(created_at);

-- Operational seed data fixtures for helpdesk_changerequests
INSERT OR IGNORE INTO helpdesk_changerequests (id, code, title, amount, quantity, status, uuid_token) VALUES
    (1, "CHA-0001", "Primary Operational ChangeRequest 1", 24500.00, 150.0, "ACTIVE", "uuid-changerequest-01"),
    (2, "CHA-0002", "Secondary Corporate ChangeRequest 2", 18200.50, 80.0, "ACTIVE", "uuid-changerequest-02"),
    (3, "CHA-0003", "Consolidated Branch ChangeRequest 3", 9400.00, 45.0, "PENDING_APPROVAL", "uuid-changerequest-03"),
    (4, "CHA-0004", "Enterprise Audited ChangeRequest 4", 32800.00, 210.0, "ACTIVE", "uuid-changerequest-04"),
    (5, "CHA-0005", "Executive Strategic ChangeRequest 5", 65000.00, 400.0, "ACTIVE", "uuid-changerequest-05");

