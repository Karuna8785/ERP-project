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
  Landmark,
  LayoutGrid
} from 'lucide-react';

const mainNavigation = [
  { 
    name: 'SALES MANAGEMENT', 
    path: '/sales', 
    icon: Landmark, 
    children: [
      { name: 'Sales Overview', path: '/sales', icon: LayoutGrid, end: true },
      { name: 'Quotations', path: '/sales/quotations', icon: FileText },
      { name: 'Sales Orders', path: '/sales/orders', icon: ShoppingCart },
      { name: 'Invoices', path: '/sales/invoices', icon: Receipt },
      { name: 'Payments', path: '/sales/payments', icon: CreditCard },
    ]
  },
  { 
    name: 'CRM & PIPELINE', 
    path: '/crm', 
    icon: UserCheck, 
    children: [
      { name: 'CRM Overview', path: '/crm', icon: LayoutGrid, end: true },
      { name: 'Leads & Pipeline', path: '/crm/leads', icon: Target },
      { name: 'Customers Directory', path: '/crm/customers', icon: Building },
    ]
  },
  { 
    name: 'INVENTORY & STOCK', 
    path: '/inventory', 
    icon: Boxes, 
    children: [
      { name: 'Overview', path: '/inventory', icon: LayoutGrid, end: true },
      { name: 'Products', path: '/inventory/products', icon: Package },
      { name: 'Categories', path: '/inventory/categories', icon: FolderTree },
      { name: 'Warehouses', path: '/inventory/warehouses', icon: Warehouse },
      { name: 'Stock Overview', path: '/inventory/stock', icon: Boxes },
      { name: 'Stock Movements', path: '/inventory/movements', icon: History },
      { name: 'Low Stock Alerts', path: '/inventory/low-stock', icon: AlertTriangle, alert: true },
    ]
  },
  { 
    name: 'PROCUREMENT & POS', 
    path: '/procurement', 
    icon: Truck,
    children: [
      { name: 'Procurement Overview', path: '/procurement', icon: LayoutGrid, end: true },
    ]
  },
  { 
    name: 'FINANCE & LEDGER', 
    path: '/finance', 
    icon: DollarSign,
    children: [
      { name: 'Finance Overview', path: '/finance', icon: LayoutGrid, end: true },
    ]
  },
  { 
    name: 'HR & PERSONNEL', 
    path: '/hr', 
    icon: Users,
    children: [
      { name: 'HR Overview', path: '/hr', icon: LayoutGrid, end: true },
      { name: 'Employees', path: '/hr/employees', icon: Users },
      { name: 'Departments', path: '/hr/departments', icon: FolderTree },
      { name: 'Attendance', path: '/hr/attendance', icon: History },
      { name: 'Leaves', path: '/hr/leaves', icon: FileText },
    ]
  },
  {
    name: 'SECURITY & ACCESS',
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
    <aside className="w-64 bg-[#190508] text-[#dfcfb8] flex flex-col flex-shrink-0 min-h-[calc(100vh-4rem)] border-r border-[#2e0c14] shadow-xl">
      {/* Platform Title */}
      <div className="px-5 py-4 border-b border-[#2e0c14]">
        <div className="text-[11px] font-bold uppercase tracking-widest text-[#c59d5f]">
          SMARTERP PLATFORM
        </div>
        <div className="text-xs text-[#a98650] mt-0.5 font-medium">
          Unified Multi-Module Suite
        </div>
      </div>

      <nav className="flex-1 px-3 py-3 space-y-2 overflow-y-auto">
        {/* Executive Overview top button */}
        <div className="pb-1">
          <NavLink
            to="/"
            end
            className={({ isActive }) =>
              `flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-xs sm:text-sm font-medium transition-all duration-150 ${
                isActive
                  ? 'bg-[#5c1524] text-white font-semibold border border-[#842034] shadow-sm'
                  : 'text-[#dfcfb8] hover:text-white hover:bg-[#2b0d14]/70'
              }`
            }
          >
            <LayoutGrid className="w-4 h-4 text-[#dfb15b] shrink-0" />
            <span>Executive Overview</span>
          </NavLink>
        </div>

        {/* Section Groups */}
        {mainNavigation.map((item) => {
          const Icon = item.icon;
          return (
            <div key={item.name} className="pt-2">
              <div className="flex items-center space-x-2 px-2.5 py-1 text-[11px] font-bold text-[#c59d5f] uppercase tracking-wider">
                <Icon className="w-3.5 h-3.5 text-[#c59d5f] shrink-0" />
                <span>{item.name}</span>
              </div>

              <div className="mt-1 space-y-0.5">
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
                            ? 'bg-[#5c1524] text-white font-semibold border border-[#842034] shadow-sm'
                            : 'text-[#dfcfb8] hover:text-white hover:bg-[#2b0d14]/70'
                        }`
                      }
                    >
                      <div className="flex items-center space-x-2.5">
                        <SubIcon className="w-3.5 h-3.5 text-[#c59d5f]/80 shrink-0" />
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
        })}
      </nav>
    </aside>
  );
}
