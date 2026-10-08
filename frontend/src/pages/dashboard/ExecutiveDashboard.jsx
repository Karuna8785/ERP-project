import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { reportService } from '../../services/reportService';
import { StatCard } from '../../components/common/StatCard';
import { formatCurrency } from '../../utils/constants';
import {
  DollarSign,
  Package,
  Users,
  ShoppingCart,
  Truck,
  FileText,
  AlertTriangle,
  RefreshCw,
  ArrowUpRight,
  TrendingUp,
  Activity,
  Layers,
  ShieldCheck,
  CheckCircle2,
} from 'lucide-react';

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
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Enterprise Executive Header Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 border border-indigo-500/20 p-6 sm:p-8">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xs font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                Live System Overview
              </span>
              <span className="text-xs text-slate-400">SmartERP Enterprise Suite</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight mt-2">
              Executive Performance Cockpit
            </h1>
            <p className="text-sm text-slate-300 mt-1 max-w-2xl">
              Cross-enterprise consolidation of sales revenue, operational expenses, inventory valuation, active workforce, and commercial pipeline.
            </p>
          </div>

          <div className="flex items-center space-x-3">
            <button
              onClick={fetchReport}
              className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
              title="Refresh Data"
            >
              <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
            </button>
            <button
              onClick={() => navigate('/sales')}
              className="px-4 py-2 rounded-xl text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 shadow-lg shadow-indigo-600/30 transition-all flex items-center space-x-1.5"
            >
              <span>Sales Pipeline</span>
              <ArrowUpRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Primary KPI Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        <StatCard
          title="Gross Invoiced Revenue"
          value={formatCurrency(kpis?.total_sales_revenue || 0)}
          icon={DollarSign}
          color="indigo"
          trend="up"
          trendValue="+12.8%"
          subtitle="Customer invoicing to date"
        />
        <StatCard
          title="Operating Expenses"
          value={formatCurrency(fin?.total_expenses || 0)}
          icon={TrendingUp}
          color="amber"
          subtitle="Corporate spend logged"
        />
        <StatCard
          title="Total Products in Catalog"
          value={inv?.total_products || 0}
          icon={Package}
          color="cyan"
          subtitle={`${inv?.low_stock_alerts || 0} low-stock triggers`}
        />
        <StatCard
          title="Active Workforce"
          value={hr?.total_employees || 0}
          icon={Users}
          color="emerald"
          subtitle={`${hr?.total_departments || 0} corporate departments`}
        />
      </div>

      {/* Cross-Module Quick Jump Hub */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        {[
          { label: 'Sales Orders', path: '/sales/orders', icon: ShoppingCart, count: kpis?.sales_orders_count || 0, color: 'text-indigo-400' },
          { label: 'CRM Leads', path: '/crm/leads', icon: Users, count: crm?.total_leads || 0, color: 'text-cyan-400' },
          { label: 'Inventory Stock', path: '/inventory/stock', icon: Package, count: inv?.total_products || 0, color: 'text-emerald-400' },
          { label: 'Purchase Orders', path: '/procurement', icon: Truck, count: fin?.purchase_orders_count || 0, color: 'text-amber-400' },
          { label: 'HR Attendance', path: '/hr/attendance', icon: Activity, count: hr?.total_employees || 0, color: 'text-purple-400' },
          { label: 'Security Audit', path: '/security/audit', icon: ShieldCheck, count: 'Live', color: 'text-teal-400' },
        ].map((item, idx) => {
          const Icon = item.icon;
          return (
            <div
              key={idx}
              onClick={() => navigate(item.path)}
              className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-slate-700 hover:bg-slate-800/60 transition-all cursor-pointer group"
            >
              <div className="flex items-center justify-between">
                <Icon className={`w-4 h-4 ${item.color}`} />
                <ArrowUpRight className="w-3.5 h-3.5 text-slate-500 group-hover:text-white transition-colors" />
              </div>
              <div className="mt-2 text-lg font-bold text-white font-mono">{item.count}</div>
              <div className="text-[11px] text-slate-400 truncate mt-0.5">{item.label}</div>
            </div>
          );
        })}
      </div>

      {/* Middle Section: Financial Trajectory & Department Summary */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Revenue vs Collections Trend */}
        <div className="lg:col-span-2 glass-panel p-6 rounded-2xl border border-slate-800">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300">
                Revenue Trajectory
              </h3>
              <p className="text-xs text-slate-500">Monthly invoiced volume vs cash collected</p>
            </div>
            <div className="flex items-center space-x-3 text-xs">
              <span className="flex items-center text-slate-400">
                <span className="w-2.5 h-2.5 rounded-sm bg-indigo-500 mr-1.5" />
                Invoiced
              </span>
              <span className="flex items-center text-slate-400">
                <span className="w-2.5 h-2.5 rounded-sm bg-emerald-400 mr-1.5" />
                Collected
              </span>
            </div>
          </div>

          <div className="space-y-4 pt-2">
            {trends.length === 0 ? (
              <div className="text-center py-8 text-xs text-slate-500">No trend data available</div>
            ) : (
              trends.map((item) => {
                const maxVal = Math.max(...trends.map((t) => Math.max(t.invoiced, t.collected)), 40000);
                const invoicedWidth = Math.min(100, Math.round((item.invoiced / maxVal) * 100));
                const collectedWidth = Math.min(100, Math.round((item.collected / maxVal) * 100));

                return (
                  <div key={item.month} className="space-y-1">
                    <div className="flex justify-between text-xs">
                      <span className="font-semibold text-slate-300">{item.month}</span>
                      <span className="font-mono text-slate-400">
                        {formatCurrency(item.invoiced)} / {formatCurrency(item.collected)}
                      </span>
                    </div>
                    <div className="h-3 w-full bg-slate-800/80 rounded-full overflow-hidden flex">
                      <div
                        style={{ width: `${invoicedWidth}%` }}
                        className="bg-indigo-500 h-full rounded-l-full transition-all duration-500"
                        title={`Invoiced: ${item.invoiced}`}
                      />
                      <div
                        style={{ width: `${collectedWidth * 0.4}%` }}
                        className="bg-emerald-400 h-full rounded-r-full transition-all duration-500"
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
        <div className="glass-panel p-6 rounded-2xl border border-slate-800 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300">
                Operational Highlights
              </h3>
              <Layers className="w-4 h-4 text-slate-500" />
            </div>

            <div className="space-y-3.5">
              <div className="p-3 rounded-xl bg-slate-800/40 border border-slate-700/50 flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-slate-200">Customer Accounts</div>
                  <div className="text-[11px] text-slate-400">CRM database active records</div>
                </div>
                <div className="text-sm font-bold font-mono text-cyan-400">
                  {crm?.total_customers || 0}
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-800/40 border border-slate-700/50 flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-slate-200">Warehouses Active</div>
                  <div className="text-[11px] text-slate-400">Storage depots connected</div>
                </div>
                <div className="text-sm font-bold font-mono text-indigo-400">
                  {inv?.total_warehouses || 0}
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-800/40 border border-slate-700/50 flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-slate-200">Pending Leave Approvals</div>
                  <div className="text-[11px] text-slate-400">HR requests awaiting review</div>
                </div>
                <div className="text-sm font-bold font-mono text-amber-400">
                  {hr?.pending_leaves || 0}
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-800/40 border border-slate-700/50 flex items-center justify-between">
                <div>
                  <div className="text-xs font-semibold text-slate-200">Low Stock Triggers</div>
                  <div className="text-[11px] text-slate-400">Products below reorder level</div>
                </div>
                <div className={`text-sm font-bold font-mono ${inv?.low_stock_alerts > 0 ? 'text-rose-400' : 'text-emerald-400'}`}>
                  {inv?.low_stock_alerts || 0}
                </div>
              </div>
            </div>
          </div>

          <div className="pt-4 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
            <span className="flex items-center gap-1.5 text-emerald-400">
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
