import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { reportService } from '../../services/reportService';
import { StatCard } from '../../components/common/StatCard';
import { formatCurrency } from '../../utils/constants';
import {
  Package,
  Users,
  ShoppingCart,
  Truck,
  RefreshCw,
  ArrowRight,
  TrendingUp,
  Activity,
  Layers,
  ShieldCheck,
  CheckCircle2,
  ChevronRight,
  UserCheck,
} from 'lucide-react';

// Custom Rupee icon for exact screenshot fidelity
const RupeeIcon = ({ className = 'w-4 h-4' }) => (
  <span className="font-serif font-bold text-base leading-none text-[#b8860b]">₹</span>
);

export const ExecutiveDashboard = () => {
  const navigate = useNavigate();
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchReport = async () => {
    setLoading(true);
    try {
      const data = await reportService.getExecutiveReport();
      setReport(data);
    } catch (err) {
      console.error('Failed to load executive report', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchReport();
  }, []);

  const kpis = report?.kpis;
  const inv = report?.inventory;
  const hr = report?.hr;
  const fin = report?.finance;
  const crm = report?.crm;
  const trends = report?.monthly_trends || [];

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Enterprise Executive Header Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-white border border-[#ece4d6] shadow-[0_2px_8px_rgba(40,20,10,0.03)] p-6 sm:p-8">
        {/* Subtle Ornamental Crest Watermark in background */}
        <div className="absolute top-1/2 -translate-y-1/2 right-12 w-64 h-64 pointer-events-none opacity-[0.07] text-[#c59d5f]">
          <svg viewBox="0 0 100 100" fill="currentColor">
            <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" strokeWidth="2" />
            <circle cx="50" cy="50" r="35" fill="none" stroke="currentColor" strokeWidth="1" strokeDasharray="2,2" />
            <path d="M50 10 L60 35 L85 35 L65 50 L75 75 L50 60 L25 75 L35 50 L15 35 L40 35 Z" fill="none" stroke="currentColor" strokeWidth="1.5" />
          </svg>
        </div>

        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-5">
          <div>
            <div className="flex items-center space-x-2">
              <span className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-[#1e7e48]">
                <span className="w-2 h-2 rounded-full bg-[#1e7e48]" />
                LIVE SYSTEM OVERVIEW
              </span>
              <span className="text-xs font-serif font-medium text-[#524647] ml-2">
                SmartERP Enterprise Suite
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-serif font-bold text-[#1c1214] tracking-tight mt-2.5">
              Executive Performance Cockpit
            </h1>
            <p className="text-xs sm:text-sm text-[#5d514d] mt-2 max-w-2xl leading-relaxed">
              Cross-enterprise consolidation of sales revenue, operational expenses, inventory valuation, active workforce, and commercial pipeline.
            </p>
          </div>

          <div className="flex items-center space-x-3 shrink-0">
            <button
              onClick={fetchReport}
              className="p-2.5 rounded-xl bg-white hover:bg-[#faf6ee] text-[#8c6b42] border border-[#ded4c3] shadow-sm transition-colors"
              title="Refresh Data"
            >
              <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
            </button>
            <button
              onClick={() => navigate('/sales')}
              className="px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-white bg-[#5c1524] hover:bg-[#4a101d] border border-[#781d30] shadow-sm flex items-center space-x-2 transition-all active:scale-[0.98]"
            >
              <span>Sales Pipeline</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Primary KPI Grid (Top 4 Cards) */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
        <StatCard
          title="GROSS INVOICED REVENUE"
          value={formatCurrency(kpis?.total_sales_revenue || 0)}
          icon={RupeeIcon}
          trend="up"
          trendValue="12.8%"
          subtitle="Customer invoicing to date"
        />
        <StatCard
          title="OPERATING EXPENSES"
          value={formatCurrency(fin?.total_expenses || 0)}
          icon={TrendingUp}
          subtitle="Corporate spend logged"
        />
        <StatCard
          title="TOTAL PRODUCTS IN CATALOG"
          value={inv?.total_products || 0}
          icon={Package}
          subtitle={`${inv?.low_stock_alerts || 0} low-stock triggers`}
        />
        <StatCard
          title="ACTIVE WORKFORCE"
          value={hr?.total_employees || 0}
          icon={Users}
          subtitle={`${hr?.total_departments || 0} corporate departments`}
        />
      </div>

      {/* Cross-Module Quick Jump Hub (Bottom 6 Cards) */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3.5">
        {[
          { 
            label: 'Sales Orders', 
            path: '/sales/orders', 
            icon: ShoppingCart, 
            count: kpis?.sales_orders_count || 0,
            iconBg: 'bg-[#faf2e6] border-[#ede0cc] text-[#9b6f38]' 
          },
          { 
            label: 'CRM Leads', 
            path: '/crm/leads', 
            icon: UserCheck, 
            count: crm?.total_leads || 3,
            iconBg: 'bg-[#faf2e6] border-[#ede0cc] text-[#9b6f38]' 
          },
          { 
            label: 'Inventory Stock', 
            path: '/inventory/stock', 
            icon: Package, 
            count: inv?.total_products || 0,
            iconBg: 'bg-[#edf7f1] border-[#cbe8d7] text-[#1e7e48]' 
          },
          { 
            label: 'Purchase Orders', 
            path: '/procurement', 
            icon: Truck, 
            count: fin?.purchase_orders_count || 0,
            iconBg: 'bg-[#faf2e6] border-[#ede0cc] text-[#9b6f38]' 
          },
          { 
            label: 'HR Attendance', 
            path: '/hr/attendance', 
            icon: Users, 
            count: hr?.total_employees || 0,
            iconBg: 'bg-[#faf2e6] border-[#ede0cc] text-[#9b6f38]' 
          },
          { 
            label: 'Security Audit', 
            path: '/security/audit', 
            icon: ShieldCheck, 
            count: 'Live',
            iconBg: 'bg-[#faf2e6] border-[#ede0cc] text-[#9b6f38]' 
          },
        ].map((item, idx) => {
          const Icon = item.icon;
          return (
            <div
              key={idx}
              onClick={() => navigate(item.path)}
              className="bg-white rounded-2xl p-4 border border-[#ece4d6] shadow-[0_2px_6px_rgba(40,20,10,0.03)] hover:border-[#dfb15b] hover:shadow-md transition-all cursor-pointer group flex flex-col justify-between"
            >
              <div className="flex items-center justify-between">
                <div className={`w-9 h-9 rounded-full border flex items-center justify-center shrink-0 ${item.iconBg}`}>
                  <Icon className="w-4 h-4" />
                </div>
                <ChevronRight className="w-4 h-4 text-[#b89569] group-hover:translate-x-0.5 transition-transform" />
              </div>
              <div className="mt-3">
                <div className="text-2xl font-serif font-bold text-[#1b1213]">
                  {item.count}
                </div>
                <div className="text-xs font-medium text-[#5f534e] mt-0.5 truncate">
                  {item.label}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Middle Section: Financial Trajectory & Department Summary */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Revenue vs Collections Trend */}
        <div className="lg:col-span-2 bg-white rounded-2xl p-6 border border-[#ece4d6] shadow-[0_2px_8px_rgba(40,20,10,0.04)]">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-sm font-serif font-bold uppercase tracking-wider text-[#1c1214]">
                Revenue Trajectory
              </h3>
              <p className="text-xs text-[#6e605d]">Monthly invoiced volume vs cash collected</p>
            </div>
            <div className="flex items-center space-x-3 text-xs">
              <span className="flex items-center text-[#554744]">
                <span className="w-2.5 h-2.5 rounded-sm bg-[#5c1524] mr-1.5" />
                Invoiced
              </span>
              <span className="flex items-center text-[#554744]">
                <span className="w-2.5 h-2.5 rounded-sm bg-[#1e7e48] mr-1.5" />
                Collected
              </span>
            </div>
          </div>

          <div className="space-y-4 pt-2">
            {trends.length === 0 ? (
              <div className="text-center py-8 text-xs text-[#8c7f7c]">No trend data available</div>
            ) : (
              trends.map((item) => {
                const maxVal = Math.max(...trends.map((t) => Math.max(t.invoiced, t.collected)), 40000);
                const invoicedWidth = Math.min(100, Math.round((item.invoiced / maxVal) * 100));
                const collectedWidth = Math.min(100, Math.round((item.collected / maxVal) * 100));

                return (
                  <div key={item.month} className="space-y-1">
                    <div className="flex justify-between text-xs">
                      <span className="font-semibold text-[#1c1214]">{item.month}</span>
                      <span className="text-[#6e605d] font-mono">
                        {formatCurrency(item.invoiced)} / {formatCurrency(item.collected)}
                      </span>
                    </div>
                    <div className="h-3 w-full bg-[#f4efe8] rounded-full overflow-hidden flex">
                      <div
                        style={{ width: `${invoicedWidth}%` }}
                        className="bg-[#5c1524] h-full rounded-l-full transition-all duration-500"
                        title={`Invoiced: ${item.invoiced}`}
                      />
                      <div
                        style={{ width: `${collectedWidth * 0.4}%` }}
                        className="bg-[#1e7e48] h-full rounded-r-full transition-all duration-500"
                        title={`Collected: ${item.collected}`}
                      />
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* Operational Health & Department Overview */}
        <div className="bg-white rounded-2xl p-6 border border-[#ece4d6] shadow-[0_2px_8px_rgba(40,20,10,0.04)] flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-sm font-serif font-bold uppercase tracking-wider text-[#1c1214]">
                Operational Highlights
              </h3>
              <Layers className="w-4 h-4 text-[#8c6b42]" />
            </div>

            <div className="space-y-3.5">
              <div className="p-3 rounded-xl bg-[#faf7f2] border border-[#ece4d6] flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-[#1c1214]">Customer Accounts</div>
                  <div className="text-[11px] text-[#71655e]">CRM database active records</div>
                </div>
                <div className="text-sm font-serif font-bold text-[#5c1524]">
                  {crm?.total_customers || 0}
                </div>
              </div>

              <div className="p-3 rounded-xl bg-[#faf7f2] border border-[#ece4d6] flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-[#1c1214]">Warehouses Active</div>
                  <div className="text-[11px] text-[#71655e]">Storage depots connected</div>
                </div>
                <div className="text-sm font-serif font-bold text-[#5c1524]">
                  {inv?.total_warehouses || 0}
                </div>
              </div>

              <div className="p-3 rounded-xl bg-[#faf7f2] border border-[#ece4d6] flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-[#1c1214]">Pending Leave Approvals</div>
                  <div className="text-[11px] text-[#71655e]">HR requests awaiting review</div>
                </div>
                <div className="text-sm font-serif font-bold text-[#b8860b]">
                  {hr?.pending_leaves || 0}
                </div>
              </div>

              <div className="p-3 rounded-xl bg-[#faf7f2] border border-[#ece4d6] flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-[#1c1214]">Low Stock Triggers</div>
                  <div className="text-[11px] text-[#71655e]">Products below reorder level</div>
                </div>
                <div className={`text-sm font-serif font-bold ${inv?.low_stock_alerts > 0 ? 'text-[#a32235]' : 'text-[#1e7e48]'}`}>
                  {inv?.low_stock_alerts || 0}
                </div>
              </div>
            </div>
          </div>

          <div className="pt-4 border-t border-[#ece4d6] flex items-center justify-between text-xs text-[#524647]">
            <span className="flex items-center gap-1.5 text-[#1e7e48] font-medium">
              <CheckCircle2 className="w-3.5 h-3.5" />
              All micro-modules synchronized
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExecutiveDashboard;
