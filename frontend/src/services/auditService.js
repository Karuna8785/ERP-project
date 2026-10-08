import api from './api';

export const auditService = {
  getLogs: async (params = {}) => {
    const res = await api.get('/audit/logs', { params });
    return res.data;
  },
  getMyLogs: async () => {
    const res = await api.get('/audit/my-logs');
    return res.data;
  },
  getRoles: async () => {
    const res = await api.get('/users/access/roles');
    return res.data;
  },
  getPermissions: async () => {
    const res = await api.get('/users/access/permissions');
    return res.data;
  },
};
