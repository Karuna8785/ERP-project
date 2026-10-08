import React, { useState, useEffect } from 'react';
import { crmService } from '../../services/crmService';
import { useNotification } from '../../context/NotificationContext';
import { formatCurrency } from '../../utils/constants';
import Modal from '../../components/common/Modal';
import {
  Users,
  Plus,
  Search,
  Filter,
  RefreshCw,
  Target,
  PhoneCall,
  Mail,
  Building,
  CheckCircle,
  Clock,
  ArrowRight,
  MessageSquare,
} from 'lucide-react';

export const LeadsPage = () => {
  const { showSuccess, showError } = useNotification();
  const [leads, setLeads] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('');

  // Modals
  const [createModalOpen, setCreateModalOpen] = useState(false);
  const [convertModalOpen, setConvertModalOpen] = useState(false);
  const [interactionModalOpen, setInteractionModalOpen] = useState(false);
  const [selectedLead, setSelectedLead] = useState(null);
  const [submitting, setSubmitting] = useState(false);

  // Forms
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    company_name: '',
    email: '',
    phone: '',
    status: 'New',
    source: 'Website',
    estimated_value: 0,
    notes: '',
  });

  const [interactionData, setInteractionData] = useState({
    interaction_type: 'call',
    summary: '',
    details: '',
  });

  const fetchLeads = async () => {
    setLoading(true);
    try {
      const params = {};
      if (statusFilter) params.status = statusFilter;
      if (searchTerm) params.search = searchTerm;
      const res = await crmService.getLeads(params);
      setLeads(res);
    } catch (err) {
      showError('Failed to fetch leads');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLeads();
  }, [statusFilter]);

  const handleSearch = (e) => {
    e.preventDefault();
    fetchLeads();
  };

  const handleCreateLead = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await crmService.createLead({
        ...formData,
        estimated_value: parseFloat(formData.estimated_value) || 0,
      });
      showSuccess('Lead added successfully');
      setCreateModalOpen(false);
      setFormData({
        first_name: '',
        last_name: '',
        company_name: '',
        email: '',
        phone: '',
        status: 'New',
        source: 'Website',
        estimated_value: 0,
        notes: '',
      });
      fetchLeads();
    } catch (err) {
      showError(err.response?.data?.detail || 'Failed to create lead');
    } finally {
      setSubmitting(false);
    }
  };

  const handleConvertLead = async () => {
    if (!selectedLead) return;
    setSubmitting(true);
    try {
      const res = await crmService.convertLead(selectedLead.id);
      showSuccess(`Lead converted to customer: ${res.customer_code}`);
      setConvertModalOpen(false);
      setSelectedLead(null);
      fetchLeads();
    } catch (err) {
      showError(err.response?.data?.detail || 'Conversion failed');
    } finally {
      setSubmitting(false);
    }
  };

  const handleLogInteraction = async (e) => {
    e.preventDefault();
    if (!selectedLead) return;
    setSubmitting(true);
    try {
      await crmService.createInteraction({
        ...interactionData,
        lead_id: selectedLead.id,
      });
      showSuccess('Communication touchpoint logged');
      setInteractionModalOpen(false);
      setInteractionData({ interaction_type: 'call', summary: '', details: '' });
      setSelectedLead(null);
    } catch (err) {
      showError(err.response?.data?.detail || 'Failed to log interaction');
    } finally {
      setSubmitting(false);
    }
  };

  const getStatusBadge = (status) => {
    const map = {
      New: 'bg-blue-500/10 text-blue-400 border-blue-500/20',
      Contacted: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/20',
      Qualified: 'bg-purple-500/10 text-purple-400 border-purple-500/20',
      Proposal: 'bg-amber-500/10 text-amber-400 border-amber-500/20',
      Won: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20',
      Lost: 'bg-rose-500/10 text-rose-400 border-rose-500/20',
    };
    return (
      <span className={`text-[10px] px-2 py-0.5 rounded-full font-bold uppercase border ${map[status] || 'bg-slate-800 text-slate-300 border-slate-700'}`}>
        {status}
      </span>
    );
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Page Title & Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">Leads & Deal Pipeline</h1>
          <p className="text-xs text-slate-400 mt-1">
            Qualify opportunities, log client touchpoints, and convert deals to active accounts.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={fetchLeads}
            className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
            title="Refresh Leads"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
          </button>
          <button
            onClick={() => setCreateModalOpen(true)}
            className="px-4 py-2.5 rounded-xl text-xs font-semibold text-white bg-cyan-600 hover:bg-cyan-500 shadow-lg shadow-cyan-600/30 transition-all flex items-center gap-1.5"
          >
            <Plus className="w-4 h-4" />
            <span>Create New Lead</span>
          </button>
        </div>
      </div>

      {/* Filter / Search Bar */}
      <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 flex flex-col md:flex-row items-center gap-4 justify-between">
        <form onSubmit={handleSearch} className="relative w-full md:w-96">
          <Search className="w-4 h-4 absolute left-3 top-3 text-slate-400" />
          <input
            type="text"
            placeholder="Search leads by name, company, email..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-slate-950 border border-slate-800 rounded-xl pl-9 pr-4 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-500"
          />
        </form>

        <div className="flex items-center gap-3 w-full md:w-auto">
          <Filter className="w-4 h-4 text-slate-400" />
          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            className="bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-200 focus:outline-none focus:border-cyan-500"
          >
            <option value="">All Statuses</option>
            <option value="New">New</option>
            <option value="Contacted">Contacted</option>
            <option value="Qualified">Qualified</option>
            <option value="Proposal">Proposal</option>
            <option value="Won">Won</option>
            <option value="Lost">Lost</option>
          </select>
        </div>
      </div>

      {/* Leads Table */}
      <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900/80 border-b border-slate-800 text-slate-400 font-semibold">
              <tr>
                <th className="p-4">Lead Code</th>
                <th className="p-4">Contact Person</th>
                <th className="p-4">Company</th>
                <th className="p-4">Status</th>
                <th className="p-4">Est. Value</th>
                <th className="p-4">Source</th>
                <th className="p-4 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {leads.length === 0 ? (
                <tr>
                  <td colSpan="7" className="py-8 text-center text-slate-500 text-xs">
                    No leads found matching your criteria.
                  </td>
                </tr>
              ) : (
                leads.map((lead) => (
                  <tr key={lead.id} className="hover:bg-slate-800/40 transition-colors">
                    <td className="p-4 font-mono font-semibold text-cyan-400">{lead.lead_code}</td>
                    <td className="p-4">
                      <div className="font-semibold text-white">
                        {lead.first_name} {lead.last_name}
                      </div>
                      <div className="text-[11px] text-slate-400">{lead.email || lead.phone || '—'}</div>
                    </td>
                    <td className="p-4 text-slate-300 font-medium">
                      {lead.company_name || 'Individual'}
                    </td>
                    <td className="p-4">{getStatusBadge(lead.status)}</td>
                    <td className="p-4 font-mono font-semibold text-slate-200">
                      {formatCurrency(lead.estimated_value || 0)}
                    </td>
                    <td className="p-4 text-slate-400">{lead.source}</td>
                    <td className="p-4 text-right space-x-2">
                      <button
                        onClick={() => {
                          setSelectedLead(lead);
                          setInteractionModalOpen(true);
                        }}
                        className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-medium border border-slate-700 transition-colors"
                        title="Log Interaction"
                      >
                        <MessageSquare className="w-3.5 h-3.5 inline mr-1" />
                        Log
                      </button>

                      {lead.status !== 'Won' && (
                        <button
                          onClick={() => {
                            setSelectedLead(lead);
                            setConvertModalOpen(true);
                          }}
                          className="px-2.5 py-1 rounded-lg bg-emerald-600/20 hover:bg-emerald-600 text-emerald-300 hover:text-white text-[11px] font-semibold border border-emerald-500/30 transition-all"
                          title="Convert to Account"
                        >
                          <Target className="w-3.5 h-3.5 inline mr-1" />
                          Convert
                        </button>
                      )}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Create Lead Modal */}
      <Modal isOpen={createModalOpen} onClose={() => setCreateModalOpen(false)} title="Create New Lead">
        <form onSubmit={handleCreateLead} className="space-y-4 text-xs">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">First Name *</label>
              <input
                required
                type="text"
                value={formData.first_name}
                onChange={(e) => setFormData({ ...formData, first_name: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Last Name *</label>
              <input
                required
                type="text"
                value={formData.last_name}
                onChange={(e) => setFormData({ ...formData, last_name: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Company Name</label>
              <input
                type="text"
                value={formData.company_name}
                onChange={(e) => setFormData({ ...formData, company_name: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Email Address</label>
              <input
                type="email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Phone</label>
              <input
                type="text"
                value={formData.phone}
                onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Estimated Deal Value (₹)</label>
              <input
                type="number"
                step="0.01"
                value={formData.estimated_value}
                onChange={(e) => setFormData({ ...formData, estimated_value: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Initial Status</label>
              <select
                value={formData.status}
                onChange={(e) => setFormData({ ...formData, status: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              >
                <option value="New">New</option>
                <option value="Contacted">Contacted</option>
                <option value="Qualified">Qualified</option>
                <option value="Proposal">Proposal</option>
              </select>
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Acquisition Source</label>
              <input
                type="text"
                value={formData.source}
                onChange={(e) => setFormData({ ...formData, source: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
          </div>

          <div>
            <label className="block text-slate-400 mb-1 font-medium">Internal Notes</label>
            <textarea
              rows="3"
              value={formData.notes}
              onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
            />
          </div>

          <div className="flex justify-end gap-3 pt-3 border-t border-slate-800">
            <button
              type="button"
              onClick={() => setCreateModalOpen(false)}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={submitting}
              className="px-4 py-2 rounded-xl text-white font-semibold bg-cyan-600 hover:bg-cyan-500"
            >
              {submitting ? 'Creating...' : 'Save Lead'}
            </button>
          </div>
        </form>
      </Modal>

      {/* Convert Lead Confirmation Modal */}
      <Modal isOpen={convertModalOpen} onClose={() => setConvertModalOpen(false)} title="Convert Lead to Customer">
        <div className="space-y-4 text-xs">
          <p className="text-slate-300">
            Are you sure you want to convert <span className="font-bold text-white">{selectedLead?.first_name} {selectedLead?.last_name}</span> ({selectedLead?.company_name || 'Individual'}) into an active Customer account?
          </p>
          <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1">
            <div className="text-slate-400">Lead Code: <span className="font-mono text-cyan-400">{selectedLead?.lead_code}</span></div>
            <div className="text-slate-400">Status will update to: <span className="font-bold text-emerald-400">Won</span></div>
            <div className="text-slate-400">A new commercial customer code will be provisioned.</div>
          </div>
          <div className="flex justify-end gap-3 pt-2">
            <button
              type="button"
              onClick={() => setConvertModalOpen(false)}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="button"
              disabled={submitting}
              onClick={handleConvertLead}
              className="px-4 py-2 rounded-xl text-white font-semibold bg-emerald-600 hover:bg-emerald-500"
            >
              {submitting ? 'Converting...' : 'Confirm Conversion'}
            </button>
          </div>
        </div>
      </Modal>

      {/* Log Interaction Modal */}
      <Modal isOpen={interactionModalOpen} onClose={() => setInteractionModalOpen(false)} title="Log Touchpoint / Interaction">
        <form onSubmit={handleLogInteraction} className="space-y-4 text-xs">
          <div>
            <label className="block text-slate-400 mb-1 font-medium">Channel Type</label>
            <select
              value={interactionData.interaction_type}
              onChange={(e) => setInteractionData({ ...interactionData, interaction_type: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
            >
              <option value="call">Phone Call</option>
              <option value="email">Email</option>
              <option value="meeting">Meeting</option>
              <option value="note">Internal Note</option>
            </select>
          </div>
          <div>
            <label className="block text-slate-400 mb-1 font-medium">Summary / Subject *</label>
            <input
              required
              type="text"
              placeholder="e.g. Discussed pricing quotation"
              value={interactionData.summary}
              onChange={(e) => setInteractionData({ ...interactionData, summary: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
            />
          </div>
          <div>
            <label className="block text-slate-400 mb-1 font-medium">Details & Next Steps</label>
            <textarea
              rows="3"
              placeholder="Meeting notes, client objections, commitments..."
              value={interactionData.details}
              onChange={(e) => setInteractionData({ ...interactionData, details: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-cyan-500"
            />
          </div>
          <div className="flex justify-end gap-3 pt-2">
            <button
              type="button"
              onClick={() => setInteractionModalOpen(false)}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={submitting}
              className="px-4 py-2 rounded-xl text-white font-semibold bg-cyan-600 hover:bg-cyan-500"
            >
              {submitting ? 'Saving...' : 'Record Log'}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export default LeadsPage;
