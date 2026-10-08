import React, { useState, useEffect } from 'react';
import { financeService } from '../../services/financeService';
import { useNotification } from '../../context/NotificationContext';
import { StatCard } from '../../components/common/StatCard';
import { formatCurrency } from '../../utils/constants';
import Modal from '../../components/common/Modal';
import {
  DollarSign,
  TrendingUp,
  Receipt,
  CreditCard,
  Plus,
  RefreshCw,
  Wallet,
  ArrowUpRight,
  TrendingDown,
  PieChart,
} from 'lucide-react';

export const FinancePage = () => {
  const { showSuccess, showError } = useNotification();
  const [summary, setSummary] = useState(null);
  const [expenses, setExpenses] = useState([]);
  const [loading, setLoading] = useState(true);

  // Modals
  const [expenseModalOpen, setExpenseModalOpen] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  // Form state
  const [expenseForm, setExpenseForm] = useState({
    category: 'Utilities',
    amount: '',
    description: '',
    payment_method: 'Bank Transfer',
    reference: '',
  });

  const fetchData = async () => {
    setLoading(true);
    try {
      const [sumRes, expRes] = await Promise.all([
        financeService.getSummary(),
        financeService.getExpenses(),
      ]);
      setSummary(sumRes);
      setExpenses(expRes);
    } catch (err) {
      showError('Failed to load financial records');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleCreateExpense = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await financeService.createExpense({
        ...expenseForm,
        amount: parseFloat(expenseForm.amount) || 0,
      });
      showSuccess('Corporate expenditure logged');
      setExpenseModalOpen(false);
      setExpenseForm({
        category: 'Utilities',
        amount: '',
        description: '',
        payment_method: 'Bank Transfer',
        reference: '',
      });
      fetchData();
    } catch (err) {
      showError(err.response?.data?.detail || 'Failed to log expense');
    } finally {
      setSubmitting(false);
    }
  };

  const netBalance = (summary?.total_collected || 0) - (summary?.total_expenses || 0);

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Title & Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">Finance & Cash Flow</h1>
          <p className="text-xs text-slate-400 mt-1">
            Accounts receivable, accounts payable, operating expenses, and enterprise cash balance.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={fetchData}
            className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
            title="Refresh Finance"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
          </button>
          <button
            onClick={() => setExpenseModalOpen(true)}
            className="px-4 py-2.5 rounded-xl text-xs font-semibold text-white bg-emerald-600 hover:bg-emerald-500 shadow-lg shadow-emerald-600/30 transition-all flex items-center gap-1.5"
          >
            <Plus className="w-4 h-4" />
            <span>Log Expense</span>
          </button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        <StatCard
          title="Collected Cash"
          value={formatCurrency(summary?.total_collected || 0)}
          icon={CreditCard}
          color="emerald"
          subtitle="Realized customer collections"
        />
        <StatCard
          title="Operating Expenses"
          value={formatCurrency(summary?.total_expenses || 0)}
          icon={TrendingDown}
          color="amber"
          subtitle="Direct and operational spend"
        />
        <StatCard
          title="Accounts Receivable (AR)"
          value={formatCurrency(summary?.total_invoiced || 0)}
          icon={Receipt}
          color="indigo"
          subtitle="Customer invoices issued"
        />
        <StatCard
          title="Net Cash Position"
          value={formatCurrency(netBalance)}
          icon={Wallet}
          color={netBalance >= 0 ? 'emerald' : 'rose'}
          subtitle="Collections minus operational expenses"
        />
      </div>

      {/* Expenses Ledger */}
      <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
        <div className="p-4 border-b border-slate-800 flex items-center justify-between">
          <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300">
            Operating Expenditures Ledger
          </h3>
          <span className="text-xs text-slate-500">{expenses.length} recorded entries</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900/80 border-b border-slate-800 text-slate-400 font-semibold">
              <tr>
                <th className="p-4">Category</th>
                <th className="p-4">Description</th>
                <th className="p-4">Payment Method</th>
                <th className="p-4">Reference</th>
                <th className="p-4">Date</th>
                <th className="p-4 text-right">Amount</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {expenses.length === 0 ? (
                <tr>
                  <td colSpan="6" className="py-8 text-center text-slate-500">
                    No operating expenses logged yet.
                  </td>
                </tr>
              ) : (
                expenses.map((exp) => (
                  <tr key={exp.id} className="hover:bg-slate-800/40 transition-colors">
                    <td className="p-4">
                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase bg-slate-800 border border-slate-700 text-slate-300">
                        {exp.category}
                      </span>
                    </td>
                    <td className="p-4 text-white font-medium">{exp.description}</td>
                    <td className="p-4 text-slate-400">{exp.payment_method}</td>
                    <td className="p-4 font-mono text-slate-400">{exp.reference || '—'}</td>
                    <td className="p-4 text-slate-400">
                      {new Date(exp.expense_date).toLocaleDateString()}
                    </td>
                    <td className="p-4 text-right font-mono font-semibold text-rose-400">
                      - {formatCurrency(exp.amount)}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Log Expense Modal */}
      <Modal isOpen={expenseModalOpen} onClose={() => setExpenseModalOpen(false)} title="Log Operating Expenditure">
        <form onSubmit={handleCreateExpense} className="space-y-4 text-xs">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Category *</label>
              <select
                value={expenseForm.category}
                onChange={(e) => setExpenseForm({ ...expenseForm, category: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-emerald-500"
              >
                <option value="Utilities">Utilities</option>
                <option value="Rent">Facility & Rent</option>
                <option value="Salaries">Payroll / Salaries</option>
                <option value="Logistics">Logistics & Shipping</option>
                <option value="Marketing">Marketing & Advertising</option>
                <option value="Software">Software & Cloud Services</option>
                <option value="Maintenance">Equipment Maintenance</option>
                <option value="Miscellaneous">Miscellaneous</option>
              </select>
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Amount (₹) *</label>
              <input
                required
                type="number"
                step="0.01"
                placeholder="0.00"
                value={expenseForm.amount}
                onChange={(e) => setExpenseForm({ ...expenseForm, amount: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>
          </div>

          <div>
            <label className="block text-slate-400 mb-1 font-medium">Description *</label>
            <input
              required
              type="text"
              placeholder="e.g. AWS Cloud Hosting Invoice - Q3"
              value={expenseForm.description}
              onChange={(e) => setExpenseForm({ ...expenseForm, description: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-emerald-500"
            />
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Payment Method</label>
              <select
                value={expenseForm.payment_method}
                onChange={(e) => setExpenseForm({ ...expenseForm, payment_method: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-emerald-500"
              >
                <option value="Bank Transfer">Bank Transfer (NEFT/RTGS)</option>
                <option value="Corporate Credit Card">Corporate Credit Card</option>
                <option value="UPI">UPI</option>
                <option value="Cash">Cash Voucher</option>
              </select>
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Reference / Receipt #</label>
              <input
                type="text"
                placeholder="INV-99212"
                value={expenseForm.reference}
                onChange={(e) => setExpenseForm({ ...expenseForm, reference: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>
          </div>

          <div className="flex justify-end gap-3 pt-3 border-t border-slate-800">
            <button
              type="button"
              onClick={() => setExpenseModalOpen(false)}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={submitting}
              className="px-4 py-2 rounded-xl text-white font-semibold bg-emerald-600 hover:bg-emerald-500"
            >
              {submitting ? 'Logging...' : 'Record Expenditure'}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export default FinancePage;
