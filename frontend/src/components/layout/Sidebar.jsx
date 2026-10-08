import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  LayoutDashboard, 
  Boxes, 
  Users, 
  UserCheck, 
  ShoppingCart, 
  Truck, 
  DollarSign,
  Package,
  FolderTree,
  Warehouse,
  AlertTriangle,
  History,
  FileText,
  CreditCard,
  Receipt,
  ShieldCheck,
  Building,
  Target,
  Key,
} from 'lucide-react';

const mainNavigation = [
  { name: 'Executive Overview', path: '/', icon: LayoutDashboard },
  { 
    name: 'Sales Management', 
    path: '/sales', 
    icon: ShoppingCart, 
    children: [
      { name: 'Sales Overview', path: '/sales', icon: LayoutDashboard, end: true },
      { name: 'Quotations', path: '/sales/quotations', icon: FileText },
      { name: 'Sales Orders', path: '/sales/orders', icon: ShoppingCart },
      { name: 'Invoices', path: '/sales/invoices', icon: Receipt },
      { name: 'Payments', path: '/sales/payments', icon: CreditCard },
    ]
  },
  { 
    name: 'CRM & Pipeline', 
    path: '/crm', 
    icon: UserCheck, 
    children: [
      { name: 'CRM Overview', path: '/crm', icon: LayoutDashboard, end: true },
      { name: 'Leads & Pipeline', path: '/crm/leads', icon: Target },
      { name: 'Customers Directory', path: '/crm/customers', icon: Building },
    ]
  },
  { 
    name: 'Inventory & Stock', 
    path: '/inventory', 
    icon: Boxes, 
    children: [
      { name: 'Overview', path: '/inventory', icon: LayoutDashboard, end: true },
      { name: 'Products', path: '/inventory/products', icon: Package },
      { name: 'Categories', path: '/inventory/categories', icon: FolderTree },
      { name: 'Warehouses', path: '/inventory/warehouses', icon: Warehouse },
      { name: 'Stock Overview', path: '/inventory/stock', icon: Boxes },
      { name: 'Stock Movements', path: '/inventory/movements', icon: History },
      { name: 'Low Stock Alerts', path: '/inventory/low-stock', icon: AlertTriangle, alert: true },
    ]
  },
  { name: 'Procurement & POs', path: '/procurement', icon: Truck },
  { name: 'Finance & Ledger', path: '/finance', icon: DollarSign },
  { 
    name: 'HR & Personnel', 
    path: '/hr', 
    icon: Users,
    children: [
      { name: 'HR Overview', path: '/hr', icon: LayoutDashboard, end: true },
      { name: 'Employees', path: '/hr/employees', icon: Users },
      { name: 'Departments', path: '/hr/departments', icon: FolderTree },
      { name: 'Attendance', path: '/hr/attendance', icon: History },
      { name: 'Leaves', path: '/hr/leaves', icon: FileText },
    ]
  },
  {
    name: 'Security & Access',
    path: '/security/audit',
    icon: ShieldCheck,
    children: [
      { name: 'Audit Logs', path: '/security/audit', icon: History },
      { name: 'Roles & RBAC', path: '/security/roles', icon: Key },
    ]
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-slate-300 flex flex-col flex-shrink-0 min-h-[calc(100vh-4rem)] border-r border-slate-800">
      <div className="p-4 border-b border-slate-800">
        <div className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
          SmartERP Platform
        </div>
        <div className="text-xs text-indigo-400 mt-0.5">
          Unified Multi-Module Suite
        </div>
      </div>

      <nav className="flex-1 p-3 space-y-1 overflow-y-auto">
        {mainNavigation.map((item) => {
          const Icon = item.icon;
          if (item.children) {
            return (
              <div key={item.name} className="pt-2">
                <div className="flex items-center justify-between px-3 py-1.5 text-xs font-bold text-slate-300 uppercase tracking-wider bg-slate-800/60 rounded-lg border border-slate-800">
                  <div className="flex items-center space-x-2">
                    <Icon className="w-3.5 h-3.5 text-indigo-400" />
                    <span>{item.name}</span>
                  </div>
                </div>

                <div className="mt-1 pl-2 space-y-0.5">
                  {item.children.map((sub) => {
                    const SubIcon = sub.icon;
                    return (
                      <NavLink
                        key={sub.path}
                        to={sub.path}
                        end={sub.end}
                        className={({ isActive }) =>
                          `flex items-center justify-between px-3 py-1.5 text-xs font-medium rounded-lg transition-all ${
                            isActive
                              ? 'bg-indigo-600 text-white font-semibold shadow-sm shadow-indigo-500/20'
                              : 'text-slate-400 hover:text-white hover:bg-slate-800/60'
                          }`
                        }
                      >
                        <div className="flex items-center space-x-2.5">
                          <SubIcon className="w-3.5 h-3.5" />
                          <span>{sub.name}</span>
                        </div>
                        {sub.alert && (
                          <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse" />
                        )}
                      </NavLink>
                    );
                  })}
                </div>
              </div>
            );
          }

          return (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.path === '/'}
              className={({ isActive }) =>
                `flex items-center justify-between px-3 py-2 text-xs font-medium rounded-lg transition-all ${
                  isActive
                    ? 'bg-indigo-600 text-white font-semibold'
                    : 'text-slate-400 hover:text-white hover:bg-slate-800/60'
                }`
              }
            >
              <div className="flex items-center space-x-2.5">
                <Icon className="w-4 h-4" />
                <span>{item.name}</span>
              </div>
            </NavLink>
          );
        })}
      </nav>

      <div className="p-4 border-t border-slate-800 bg-slate-950/40">
        <div className="text-[11px] text-slate-400">
          Connected Backend:
        </div>
        <div className="text-xs font-semibold text-emerald-400 flex items-center gap-1.5 mt-0.5">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          All 7 Modules Active
        </div>
      </div>
    </aside>
  );
}
