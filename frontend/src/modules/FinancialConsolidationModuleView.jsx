import React, { useState } from "react";
import { Layers, Plus, Search, Filter, RefreshCw, ChevronRight, CheckCircle2, TrendingUp, AlertTriangle } from "lucide-react";

export const FinancialConsolidationModuleView = () => {
  const [activeTab, setActiveTab] = useState("ConsolidationEntityGroup");
  const [searchTerm, setSearchTerm] = useState("");
  const [filterStatus, setFilterStatus] = useState("ALL");

  const entities = [
    { name: "ConsolidationEntityGroup", label: "ConsolidationEntityGroup" },
    { name: "IntercompanyEliminationEntry", label: "IntercompanyEliminationEntry" },
    { name: "ConsolidatedTrialBalance", label: "ConsolidatedTrialBalance" },
    { name: "CurrencyTranslationRate", label: "CurrencyTranslationRate" },
    { name: "MinorityInterestShare", label: "MinorityInterestShare" },
    { name: "JointVentureEquityShare", label: "JointVentureEquityShare" },
    { name: "FinancialAdjustmentVoucher", label: "FinancialAdjustmentVoucher" },
    { name: "GoodwillImpairmentSchedule", label: "GoodwillImpairmentSchedule" },
    { name: "SegmentalReportingUnit", label: "SegmentalReportingUnit" },
    { name: "ConsolidatedCashFlow", label: "ConsolidatedCashFlow" },
    { name: "StatutoryBalanceSheet", label: "StatutoryBalanceSheet" },
    { name: "ConsolidatedIncomeStatement", label: "ConsolidatedIncomeStatement" },
    { name: "AuditTrailElimination", label: "AuditTrailElimination" },
    { name: "TaxProvisioningConsolidated", label: "TaxProvisioningConsolidated" },
    { name: "FinancialClosingChecklist", label: "FinancialClosingChecklist" },
    { name: "ExecutiveBoardFinancialReport", label: "ExecutiveBoardFinancialReport" }
  ];

  const sampleRows = [
    { id: 1, code: `${activeTab.slice(0, 3).toUpperCase()}-0001`, title: `Primary Operational ${activeTab} 1`, amount: 24500.0, qty: 150, status: "ACTIVE", priority: "HIGH" },
    { id: 2, code: `${activeTab.slice(0, 3).toUpperCase()}-0002`, title: `Secondary Corporate ${activeTab} 2`, amount: 18200.5, qty: 80, status: "ACTIVE", priority: "MEDIUM" },
    { id: 3, code: `${activeTab.slice(0, 3).toUpperCase()}-0003`, title: `Consolidated Branch ${activeTab} 3`, amount: 9400.0, qty: 45, status: "PENDING_APPROVAL", priority: "LOW" },
    { id: 4, code: `${activeTab.slice(0, 3).toUpperCase()}-0004`, title: `Enterprise Audited ${activeTab} 4`, amount: 32800.0, qty: 210, status: "ACTIVE", priority: "CRITICAL" },
    { id: 5, code: `${activeTab.slice(0, 3).toUpperCase()}-0005`, title: `Executive Strategic ${activeTab} 5`, amount: 65000.0, qty: 400, status: "ACTIVE", priority: "HIGH" },
  ];

  return (
    <div className="space-y-6">
      <div className="bg-white rounded-2xl p-6 border border-[#ece4d6] shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs font-bold text-[#c59d5f] uppercase tracking-wider">
            <Layers className="w-3.5 h-3.5" />
            <span>Titan Enterprise Suite</span>
          </div>
          <h1 className="text-2xl font-serif font-bold text-[#1c1214] mt-1">
            Multi-Entity Financial Consolidation & Reporting
          </h1>
          <p className="text-xs text-[#5f514d] mt-1">
            Unified operational management, transaction auditing, and business intelligence.
          </p>
        </div>
        <div className="flex items-center space-x-3">
          <button className="px-4 py-2 rounded-xl text-xs font-semibold text-[#5c1524] bg-[#faf7f2] border border-[#ece4d6] hover:bg-[#f3ede1] transition-all flex items-center space-x-1.5 shadow-sm">
            <RefreshCw className="w-3.5 h-3.5" />
            <span>Sync Ledger</span>
          </button>
          <button className="px-4 py-2 rounded-xl text-xs font-semibold text-white bg-[#5c1524] hover:bg-[#4a101d] transition-all flex items-center space-x-1.5 shadow-sm">
            <Plus className="w-4 h-4" />
            <span>New {activeTab}</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white p-4 rounded-xl border border-[#ece4d6] shadow-sm">
          <div className="text-xs text-[#71655e]">Total Operational Volume</div>
          <div className="text-xl font-bold font-mono text-[#1c1214] mt-1">₹149,900.50</div>
          <div className="text-[10px] text-emerald-600 flex items-center mt-1">
            <TrendingUp className="w-3 h-3 mr-1" />
            <span>+12.4% vs last fiscal month</span>
          </div>
        </div>
        <div className="bg-white p-4 rounded-xl border border-[#ece4d6] shadow-sm">
          <div className="text-xs text-[#71655e]">Active Records</div>
          <div className="text-xl font-bold font-mono text-[#1c1214] mt-1">1,248 units</div>
          <div className="text-[10px] text-[#71655e] mt-1">99.8% compliance rate</div>
        </div>
        <div className="bg-white p-4 rounded-xl border border-[#ece4d6] shadow-sm">
          <div className="text-xs text-[#71655e]">Pending Verification</div>
          <div className="text-xl font-bold font-mono text-amber-600 mt-1">3 items</div>
          <div className="text-[10px] text-amber-700 flex items-center mt-1">
            <AlertTriangle className="w-3 h-3 mr-1" />
            <span>Requires manager signoff</span>
          </div>
        </div>
        <div className="bg-white p-4 rounded-xl border border-[#ece4d6] shadow-sm">
          <div className="text-xs text-[#71655e]">Average Operating Margin</div>
          <div className="text-xl font-bold font-mono text-emerald-700 mt-1">34.2%</div>
          <div className="text-[10px] text-emerald-600 mt-1">Strong financial health</div>
        </div>
      </div>

      <div className="flex space-x-2 overflow-x-auto pb-2 border-b border-[#ece4d6]">
        {entities.map((ent) => (
          <button
            key={ent.name}
            onClick={() => setActiveTab(ent.name)}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition-colors ${
              activeTab === ent.name
                ? "bg-[#5c1524] text-white font-semibold shadow-sm"
                : "bg-white text-[#5f514d] hover:bg-[#faf7f2] border border-[#ece4d6]"
            }}}
          >
            {ent.label}
          </button>
        ))}
      </div>

      <div className="bg-white rounded-2xl border border-[#ece4d6] shadow-sm overflow-hidden">
        <div className="p-4 border-b border-[#ece4d6] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="relative w-full sm:w-72">
            <Search className="w-4 h-4 absolute left-3 top-2.5 text-[#a1938f]" />
            <input
              type="text"
              placeholder={`Filter ${activeTab} records...`}
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-3 py-1.5 text-xs rounded-xl border border-[#ded4c3] focus:outline-none focus:ring-2 focus:ring-[#c59d5f]"
            />
          </div>
          <div className="flex items-center space-x-2">
            <select
              value={filterStatus}
              onChange={(e) => setFilterStatus(e.target.value)}
              className="px-3 py-1.5 text-xs rounded-xl border border-[#ded4c3] bg-white text-[#5f514d]"
            >
              <option value="ALL">All Statuses</option>
              <option value="ACTIVE">Active</option>
              <option value="PENDING_APPROVAL">Pending Approval</option>
              <option value="COMPLETED">Completed</option>
            </select>
          </div>
        </div>

        <table className="w-full text-left text-xs">
          <thead className="bg-[#faf7f2] border-b border-[#ece4d6] text-[#63554e] uppercase font-bold">
            <tr>
              <th className="px-4 py-3">Code</th>
              <th className="px-4 py-3">Title</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Priority</th>
              <th className="px-4 py-3 text-right">Amount</th>
              <th className="px-4 py-3 text-right">Quantity</th>
              <th className="px-4 py-3 text-center">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-[#ece4d6] text-[#241a1c]">
            {sampleRows.map((row) => (
              <tr key={row.id} className="hover:bg-[#fbf9f4] transition-colors">
                <td className="px-4 py-3 font-semibold text-[#5c1524]">{row.code}</td>
                <td className="px-4 py-3 font-medium">{row.title}</td>
                <td className="px-4 py-3">
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-[#ecf7f0] text-[#1b7340] border border-[#cae8d5]">
                    {row.status}
                  </span>
                </td>
                <td className="px-4 py-3">
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-slate-100 text-slate-700">
                    {row.priority}
                  </span>
                </td>
                <td className="px-4 py-3 text-right font-mono">₹{row.amount.toLocaleString()}.00</td>
                <td className="px-4 py-3 text-right font-mono">{row.qty} units</td>
                <td className="px-4 py-3 text-center">
                  <button className="text-[#c59d5f] hover:underline flex items-center justify-center space-x-0.5 mx-auto">
                    <span>Inspect</span>
                    <ChevronRight className="w-3 h-3" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default FinancialConsolidationModuleView;
