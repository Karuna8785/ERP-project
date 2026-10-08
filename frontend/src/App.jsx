import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { NotificationProvider } from './context/NotificationContext';
import AppLayout from './components/layout/AppLayout';
import ProtectedRoute from './routes/ProtectedRoute';

// Auth Pages
import { Login } from './pages/auth/Login';
import Register from './pages/auth/Register';
import { ProfilePage } from './pages/profile/ProfilePage';

// Executive Cockpit
import ExecutiveDashboard from './pages/dashboard/ExecutiveDashboard';

// Sales Module
import { SalesDashboard } from './pages/dashboard/SalesDashboard';
import { QuotationsPage } from './pages/sales/QuotationsPage';
import { SalesOrdersPage } from './pages/sales/SalesOrdersPage';
import { InvoicesPage } from './pages/sales/InvoicesPage';
import { PaymentsPage } from './pages/sales/PaymentsPage';

// CRM Module
import CRMOverviewPage from './pages/crm/CRMOverviewPage';
import LeadsPage from './pages/crm/LeadsPage';
import CustomersPage from './pages/crm/CustomersPage';

// Inventory Module
import InventoryLayout from './pages/inventory/InventoryLayout';
import InventoryOverview from './pages/inventory/InventoryOverview';
import ProductsPage from './pages/inventory/ProductsPage';
import CategoriesPage from './pages/inventory/CategoriesPage';
import WarehousesPage from './pages/inventory/WarehousesPage';
import StockOverviewPage from './pages/inventory/StockOverviewPage';
import StockMovementsPage from './pages/inventory/StockMovementsPage';
import LowStockPage from './pages/inventory/LowStockPage';

// Procurement & Purchasing
import ProcurementPage from './pages/procurement/ProcurementPage';

// Finance & Accounting
import FinancePage from './pages/finance/FinancePage';

// HR Module
import HRDashboard from './pages/hr/HRDashboard';
import EmployeeList from './pages/hr/employees/EmployeeList';
import DepartmentList from './pages/hr/departments/DepartmentList';
import AttendanceList from './pages/hr/attendance/AttendanceList';
import LeaveList from './pages/hr/leaves/LeaveList';

// Security & Audit
import AuditLogsPage from './pages/security/AuditLogsPage';
import RolesPermissionsPage from './pages/security/RolesPermissionsPage';

export default function App() {
  return (
    <BrowserRouter>
      <NotificationProvider>
        <AuthProvider>
          <Routes>
            {/* Public Auth Routes */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />

            {/* Protected Routes */}
            <Route element={<ProtectedRoute />}>
              <Route element={<AppLayout />}>
                {/* Executive Dashboard */}
                <Route path="/" element={<ExecutiveDashboard />} />
                <Route path="/dashboard" element={<Navigate to="/" replace />} />
                <Route path="/profile" element={<ProfilePage />} />

                {/* Sales & Distribution */}
                <Route path="/sales" element={<SalesDashboard />} />
                <Route path="/sales/quotations" element={<QuotationsPage />} />
                <Route path="/sales/orders" element={<SalesOrdersPage />} />
                <Route path="/sales/invoices" element={<InvoicesPage />} />
                <Route path="/sales/payments" element={<PaymentsPage />} />

                {/* CRM & Pipeline */}
                <Route path="/crm" element={<CRMOverviewPage />} />
                <Route path="/crm/leads" element={<LeadsPage />} />
                <Route path="/crm/customers" element={<CustomersPage />} />

                {/* Inventory & Warehousing */}
                <Route path="/inventory" element={<InventoryLayout />}>
                  <Route index element={<InventoryOverview />} />
                  <Route path="products" element={<ProductsPage />} />
                  <Route path="categories" element={<CategoriesPage />} />
                  <Route path="warehouses" element={<WarehousesPage />} />
                  <Route path="stock" element={<StockOverviewPage />} />
                  <Route path="movements" element={<StockMovementsPage />} />
                  <Route path="low-stock" element={<LowStockPage />} />
                </Route>

                {/* Procurement & Suppliers */}
                <Route path="/procurement" element={<ProcurementPage />} />

                {/* Finance & Accounting */}
                <Route path="/finance" element={<FinancePage />} />

                {/* HR & Personnel */}
                <Route path="/hr" element={<HRDashboard />} />
                <Route path="/hr/employees" element={<EmployeeList />} />
                <Route path="/hr/departments" element={<DepartmentList />} />
                <Route path="/hr/attendance" element={<AttendanceList />} />
                <Route path="/hr/leaves" element={<LeaveList />} />

                {/* Security & Access */}
                <Route path="/security/audit" element={<AuditLogsPage />} />
                <Route path="/security/roles" element={<RolesPermissionsPage />} />
              </Route>
            </Route>

            {/* Fallback */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </AuthProvider>
      </NotificationProvider>
    </BrowserRouter>
  );
}
