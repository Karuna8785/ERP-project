import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { crmService } from '../../services/crmService';
import { StatCard } from '../../components/common/StatCard';
import { formatCurrency } from '../../utils/constants';
import {
  Users,
  Target,
  UserCheck,
  TrendingUp,
  RefreshCw,
  Plus,
  ArrowUpRight,
  PhoneCall,
  Mail,
  Calendar,
  MessageSquare,
  Building,
} from 'lucide-react';

export const CRMOverviewPage = () => {
  const navigate = useNavigate();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchOverview = async () => {
    setLoading(true);
    try {
      const res = await crmService.getOverview();
      setData(res);
    } catch (err) {
      console.error('Failed to load CRM overview', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOverview();
  }, []);

  const breakdown = data?.lead_status_breakdown || {};
  const statusColors = {
    New: 'bg-blue-500/10 text-blue-400 border-blue-500/20',
    Contacted: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/20',
    Qualified: 'bg-purple-500/10 text-purple-400 border-purple-500/20',
    Proposal: 'bg-amber-500/10 text-amber-400 border-amber-500/20',
    Won: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20',
    Lost: 'bg-rose-500/10 text-rose-400 border-rose-500/20',
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* CRM Header Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-slate-900 via-cyan-950 to-slate-900 border border-cyan-500/20 p-6 sm:p-8">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xs font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                CRM & Pipeline
              </span>
              <span className="text-xs text-slate-400">Customer Relationship Management</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight mt-2">
              Customer Pipeline & Relationship Hub
            </h1>
            <p className="text-sm text-slate-300 mt-1 max-w-2xl">
              Track commercial leads, qualification stages, client interactions, account conversions, and relationship history.
            </p>
          </div>

          <div className="flex items-center space-x-3">
            <button
              onClick={fetchOverview}
              className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
              title="Refresh CRM Data"
            >
              <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
            </button>
            <button
              onClick={() => navigate('/crm/leads')}
              className="px-4 py-2 rounded-xl text-xs font-semibold text-white bg-cyan-600 hover:bg-cyan-500 shadow-lg shadow-cyan-600/30 transition-all flex items-center space-x-1.5"
            >
              <Plus className="w-4 h-4" />
              <span>Pipeline Leads</span>
            </button>
            <button
              onClick={() => navigate('/crm/customers')}
              className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-200 bg-slate-800 hover:bg-slate-700 border border-slate-700 transition-all flex items-center space-x-1.5"
            >
              <Building className="w-4 h-4" />
              <span>Customers</span>
            </button>
          </div>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        <StatCard
          title="Active Customers"
          value={data?.total_customers || 0}
          icon={UserCheck}
          color="emerald"
          subtitle="Converted corporate client accounts"
        />
        <StatCard
          title="Total Leads"
          value={data?.total_leads || 0}
          icon={Users}
          color="cyan"
          subtitle={`${data?.active_leads || 0} active in deal pipeline`}
        />
        <StatCard
          title="Pipeline Estimated Value"
          value={formatCurrency(data?.pipeline_value || 0)}
          icon={TrendingUp}
          color="indigo"
          subtitle="Total value of active deals"
        />
        <StatCard
          title="Converted Deals"
          value={data?.converted_leads || 0}
          icon={Target}
          color="amber"
          subtitle="Leads converted to customers"
        />
      </div>

      {/* Pipeline Funnel Stages */}
      <div className="glass-panel p-6 rounded-2xl border border-slate-800">
        <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300 mb-4">
          Lead Pipeline by Status Stage
        </h3>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
          {['New', 'Contacted', 'Qualified', 'Proposal', 'Won', 'Lost'].map((st) => {
            const item = breakdown[st] || { count: 0, value: 0 };
            return (
              <div
                key={st}
                className={`p-4 rounded-xl border ${statusColors[st] || 'bg-slate-800/40 border-slate-700'} space-y-1.5`}
              >
                <div className="text-xs font-semibold uppercase">{st}</div>
                <div className="text-2xl font-bold font-mono text-white">{item.count}</div>
                <div className="text-[11px] opacity-80 font-mono">{formatCurrency(item.value)}</div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Recent Leads and Interactions */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Recent Pipeline Leads */}
        <div className="glass-panel p-6 rounded-2xl border border-slate-800">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300">
              Recent Leads
            </h3>
            <button
              onClick={() => navigate('/crm/leads')}
              className="text-xs text-cyan-400 hover:text-cyan-300 flex items-center gap-1"
            >
              View all <ArrowUpRight className="w-3.5 h-3.5" />
            </button>
          </div>

          <div className="divide-y divide-slate-800">
            {data?.recent_leads?.length === 0 ? (
              <div className="py-6 text-center text-xs text-slate-500">No leads recorded yet.</div>
            ) : (
              data?.recent_leads?.map((lead) => (
                <div key={lead.id} className="py-3 flex items-center justify-between">
                  <div>
                    <div className="text-xs font-semibold text-white">
                      {lead.first_name} {lead.last_name}
                    </div>
                    <div className="text-[11px] text-slate-400">
                      {lead.company_name || 'Independent'} • {lead.email || lead.phone || 'No contact'}
                    </div>
                  </div>
                  <div className="text-right">
                    <span className="text-[10px] px-2 py-0.5 rounded-full font-bold uppercase bg-slate-800 border border-slate-700 text-cyan-300">
                      {lead.status}
                    </span>
                    <div className="text-xs font-mono font-semibold text-slate-300 mt-1">
                      {formatCurrency(lead.estimated_value || 0)}
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>

        {/* Recent Client Interactions */}
        <div className="glass-panel p-6 rounded-2xl border border-slate-800">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300">
              Recent Touchpoints & Logs
            </h3>
            <span className="text-xs text-slate-500">Communication Activity</span>
          </div>

          <div className="divide-y divide-slate-800">
            {data?.recent_interactions?.length === 0 ? (
              <div className="py-6 text-center text-xs text-slate-500">No touchpoints logged yet.</div>
            ) : (
              data?.recent_interactions?.map((act) => (
                <div key={act.id} className="py-3 flex items-start gap-3">
                  <div className="p-2 rounded-lg bg-slate-800 text-cyan-400 mt-0.5">
                    {act.interaction_type === 'call' && <PhoneCall className="w-3.5 h-3.5" />}
                    {act.interaction_type === 'email' && <Mail className="w-3.5 h-3.5" />}
                    {act.interaction_type === 'meeting' && <Calendar className="w-3.5 h-3.5" />}
                    {act.interaction_type === 'note' && <MessageSquare className="w-3.5 h-3.5" />}
                    {!['call', 'email', 'meeting', 'note'].includes(act.interaction_type) && (
                      <MessageSquare className="w-3.5 h-3.5" />
                    )}
                  </div>
                  <div className="flex-1">
                    <div className="text-xs font-semibold text-slate-200">{act.summary}</div>
                    <div className="text-[11px] text-slate-400 line-clamp-1 mt-0.5">{act.details}</div>
                    <div className="text-[10px] text-slate-500 mt-1">
                      {new Date(act.interaction_date).toLocaleString()}
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default CRMOverviewPage;
