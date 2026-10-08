import React, { useState, useEffect } from 'react';
import { crmService } from '../../services/crmService';
import { useNotification } from '../../context/NotificationContext';
import { formatCurrency } from '../../utils/constants';
import Modal from '../../components/common/Modal';
import {
  Building,
  Plus,
  Search,
  RefreshCw,
  Mail,
  Phone,
  MapPin,
  Clock,
  History,
  DollarSign,
  User,
} from 'lucide-react';

export const CustomersPage = () => {
  const { showSuccess, showError } = useNotification();
  const [customers, setCustomers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  // Modals
  const [createModalOpen, setCreateModalOpen] = useState(false);
  const [timelineModalOpen, setTimelineModalOpen] = useState(false);
  const [selectedCustomer, setSelectedCustomer] = useState(null);
  const [timeline, setTimeline] = useState([]);
  const [timelineLoading, setTimelineLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  // Form State
  const [formData, setFormData] = useState({
    company_name: '',
    contact_name: '',
    email: '',
    phone: '',
    address: '',
    city: '',
    country: 'India',
    credit_limit: 100000,
    annual_revenue: 0,
    industry: 'Technology',
    customer_type: 'B2B',
  });

  const fetchCustomers = async () => {
    setLoading(true);
    try {
      const res = await crmService.getCustomers({ search: searchTerm });
      setCustomers(res);
    } catch (err) {
      showError('Failed to fetch customers');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCustomers();
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    fetchCustomers();
  };

  const handleCreateCustomer = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await crmService.createCustomer({
        ...formData,
        credit_limit: parseFloat(formData.credit_limit) || 0,
        annual_revenue: parseFloat(formData.annual_revenue) || 0,
      });
      showSuccess('Customer registered successfully');
      setCreateModalOpen(false);
      setFormData({
        company_name: '',
        contact_name: '',
        email: '',
        phone: '',
        address: '',
        city: '',
        country: 'India',
        credit_limit: 100000,
        annual_revenue: 0,
        industry: 'Technology',
        customer_type: 'B2B',
      });
      fetchCustomers();
    } catch (err) {
      showError(err.response?.data?.detail || 'Failed to create customer');
    } finally {
      setSubmitting(false);
    }
  };

  const handleViewTimeline = async (cust) => {
    setSelectedCustomer(cust);
    setTimelineModalOpen(true);
    setTimelineLoading(true);
    try {
      const res = await crmService.getCustomerTimeline(cust.id);
      setTimeline(res);
    } catch (err) {
      showError('Failed to load customer history timeline');
    } finally {
      setTimelineLoading(false);
    }
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">Customer Directory</h1>
          <p className="text-xs text-slate-400 mt-1">
            Accounts, commercial credit limits, communication history, and interactions.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={fetchCustomers}
            className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
            title="Refresh"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
          </button>
          <button
            onClick={() => setCreateModalOpen(true)}
            className="px-4 py-2.5 rounded-xl text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 shadow-lg shadow-indigo-600/30 transition-all flex items-center gap-1.5"
          >
            <Plus className="w-4 h-4" />
            <span>Add Customer</span>
          </button>
        </div>
      </div>

      {/* Search */}
      <div className="p-4 rounded-xl bg-slate-900 border border-slate-800">
        <form onSubmit={handleSearch} className="relative w-full md:w-96">
          <Search className="w-4 h-4 absolute left-3 top-3 text-slate-400" />
          <input
            type="text"
            placeholder="Search customers by company, name, email..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-slate-950 border border-slate-800 rounded-xl pl-9 pr-4 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
          />
        </form>
      </div>

      {/* Customers Table */}
      <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900/80 border-b border-slate-800 text-slate-400 font-semibold">
              <tr>
                <th className="p-4">Customer Code</th>
                <th className="p-4">Company Name</th>
                <th className="p-4">Contact Person</th>
                <th className="p-4">Industry / Type</th>
                <th className="p-4">Credit Limit</th>
                <th className="p-4">Status</th>
                <th className="p-4 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {customers.length === 0 ? (
                <tr>
                  <td colSpan="7" className="py-8 text-center text-slate-500 text-xs">
                    No customers found in database.
                  </td>
                </tr>
              ) : (
                customers.map((cust) => (
                  <tr key={cust.id} className="hover:bg-slate-800/40 transition-colors">
                    <td className="p-4 font-mono font-semibold text-indigo-400">
                      {cust.customer_code}
                    </td>
                    <td className="p-4">
                      <div className="font-semibold text-white">{cust.company_name}</div>
                      <div className="text-[11px] text-slate-400">
                        {cust.city ? `${cust.city}, ` : ''}{cust.country || 'India'}
                      </div>
                    </td>
                    <td className="p-4">
                      <div className="text-slate-200 font-medium">{cust.contact_name || '—'}</div>
                      <div className="text-[11px] text-slate-400">{cust.email || cust.phone || '—'}</div>
                    </td>
                    <td className="p-4">
                      <span className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-medium text-[10px] border border-slate-700">
                        {cust.industry || 'General'}
                      </span>
                    </td>
                    <td className="p-4 font-mono font-semibold text-slate-200">
                      {formatCurrency(cust.credit_limit || 0)}
                    </td>
                    <td className="p-4">
                      <span className="text-[10px] px-2 py-0.5 rounded-full font-bold uppercase bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                        {cust.status || 'Active'}
                      </span>
                    </td>
                    <td className="p-4 text-right">
                      <button
                        onClick={() => handleViewTimeline(cust)}
                        className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-medium border border-slate-700 transition-colors"
                      >
                        <History className="w-3.5 h-3.5 inline mr-1" />
                        Timeline
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Create Customer Modal */}
      <Modal isOpen={createModalOpen} onClose={() => setCreateModalOpen(false)} title="Register Customer Account">
        <form onSubmit={handleCreateCustomer} className="space-y-4 text-xs">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Company Name *</label>
              <input
                required
                type="text"
                value={formData.company_name}
                onChange={(e) => setFormData({ ...formData, company_name: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Contact Person *</label>
              <input
                required
                type="text"
                value={formData.contact_name}
                onChange={(e) => setFormData({ ...formData, contact_name: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Email Address</label>
              <input
                type="email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Phone</label>
              <input
                type="text"
                value={formData.phone}
                onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">City</label>
              <input
                type="text"
                value={formData.city}
                onChange={(e) => setFormData({ ...formData, city: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Industry</label>
              <input
                type="text"
                value={formData.industry}
                onChange={(e) => setFormData({ ...formData, industry: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Commercial Credit Limit (₹)</label>
              <input
                type="number"
                value={formData.credit_limit}
                onChange={(e) => setFormData({ ...formData, credit_limit: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Annual Revenue (₹)</label>
              <input
                type="number"
                value={formData.annual_revenue}
                onChange={(e) => setFormData({ ...formData, annual_revenue: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
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
              className="px-4 py-2 rounded-xl text-white font-semibold bg-indigo-600 hover:bg-indigo-500"
            >
              {submitting ? 'Saving...' : 'Register Customer'}
            </button>
          </div>
        </form>
      </Modal>

      {/* Customer Timeline Modal */}
      <Modal
        isOpen={timelineModalOpen}
        onClose={() => setTimelineModalOpen(false)}
        title={`History & Touchpoint Timeline — ${selectedCustomer?.company_name || ''}`}
      >
        <div className="space-y-4 text-xs max-h-[60vh] overflow-y-auto">
          {timelineLoading ? (
            <div className="py-8 text-center text-slate-400 flex items-center justify-center gap-2">
              <RefreshCw className="w-4 h-4 animate-spin" />
              <span>Loading customer records...</span>
            </div>
          ) : timeline.length === 0 ? (
            <div className="py-8 text-center text-slate-500">
              No historical interactions logged yet for this customer.
            </div>
          ) : (
            <div className="relative pl-6 border-l-2 border-slate-800 space-y-4">
              {timeline.map((item) => (
                <div key={item.id} className="relative">
                  <div className="absolute -left-[31px] top-1 w-3 h-3 rounded-full bg-indigo-500 ring-4 ring-slate-950" />
                  <div className="p-3 rounded-xl bg-slate-950 border border-slate-800">
                    <div className="flex items-center justify-between">
                      <span className="font-semibold text-white capitalize">{item.interaction_type}</span>
                      <span className="text-[10px] text-slate-500">
                        {new Date(item.interaction_date).toLocaleString()}
                      </span>
                    </div>
                    <div className="text-slate-300 font-medium mt-1">{item.summary}</div>
                    {item.details && (
                      <div className="text-slate-400 text-[11px] mt-1 bg-slate-900/60 p-2 rounded-lg">
                        {item.details}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </Modal>
    </div>
  );
};

export default CustomersPage;
