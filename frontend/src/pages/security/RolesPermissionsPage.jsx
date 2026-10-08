import React, { useState, useEffect } from 'react';
import { auditService } from '../../services/auditService';
import { useNotification } from '../../context/NotificationContext';
import {
  Shield,
  Key,
  CheckCircle2,
  Lock,
  RefreshCw,
  Users,
} from 'lucide-react';

export const RolesPermissionsPage = () => {
  const { showError } = useNotification();
  const [roles, setRoles] = useState([]);
  const [permissions, setPermissions] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    setLoading(true);
    try {
      const [rRes, pRes] = await Promise.all([
        auditService.getRoles(),
        auditService.getPermissions(),
      ]);
      setRoles(rRes);
      setPermissions(pRes);
    } catch (err) {
      showError('Failed to fetch roles and permissions');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <Lock className="w-6 h-6 text-indigo-400" />
            <h1 className="text-2xl font-bold text-white tracking-tight">Access Control & RBAC</h1>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Enterprise Role-Based Access Control matrix, permission scopes, and granted module authorizations.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={fetchData}
            className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
            title="Refresh RBAC Data"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
          </button>
        </div>
      </div>

      {/* Roles Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {roles.map((role) => (
          <div
            key={role.id}
            className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-3"
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-400">
                {role.name}
              </span>
              <Shield className="w-4 h-4 text-indigo-400" />
            </div>
            <p className="text-xs text-slate-400 min-h-[32px]">{role.description || 'System access level'}</p>
            <div className="pt-2 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-500">
              <span>Tier Policy</span>
              <span className="text-emerald-400 font-semibold">Active & Enforced</span>
            </div>
          </div>
        ))}
      </div>

      {/* Permissions Matrix */}
      <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
        <div className="p-4 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Key className="w-4 h-4 text-indigo-400" />
            <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300">
              System Permissions Catalog
            </h3>
          </div>
          <span className="text-xs text-slate-500">{permissions.length} granular scopes</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900/80 border-b border-slate-800 text-slate-400 font-semibold">
              <tr>
                <th className="p-4">Permission Code</th>
                <th className="p-4">Resource Scope</th>
                <th className="p-4">Action</th>
                <th className="p-4">Description</th>
                <th className="p-4 text-right">Protection</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono">
              {permissions.length === 0 ? (
                <tr>
                  <td colSpan="5" className="py-8 text-center text-slate-500 font-sans">
                    No permissions loaded.
                  </td>
                </tr>
              ) : (
                permissions.map((perm) => (
                  <tr key={perm.id} className="hover:bg-slate-800/40 transition-colors">
                    <td className="p-4 text-indigo-400 font-semibold">{perm.name}</td>
                    <td className="p-4 text-slate-300">{perm.resource || perm.name.split(':')[0]}</td>
                    <td className="p-4">
                      <span className="text-[10px] px-2 py-0.5 rounded font-bold uppercase bg-slate-800 border border-slate-700 text-slate-300">
                        {perm.action || perm.name.split(':')[1] || 'ALL'}
                      </span>
                    </td>
                    <td className="p-4 font-sans text-slate-400 text-[11px]">{perm.description || 'Access authorization scope'}</td>
                    <td className="p-4 text-right font-sans">
                      <span className="text-[11px] text-emerald-400 flex items-center justify-end gap-1 font-semibold">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                        JWT Secured
                      </span>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default RolesPermissionsPage;
