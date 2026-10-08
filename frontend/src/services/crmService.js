import api from './api';

export const crmService = {
  getOverview: async () => {
    const res = await api.get('/crm/overview');
    return res.data;
  },
  getCustomers: async (params = {}) => {
    const res = await api.get('/crm/customers', { params });
    return res.data;
  },
  createCustomer: async (customerData) => {
    const res = await api.post('/crm/customers', customerData);
    return res.data;
  },
  getLeads: async (params = {}) => {
    const res = await api.get('/crm/leads', { params });
    return res.data;
  },
  createLead: async (leadData) => {
    const res = await api.post('/crm/leads', leadData);
    return res.data;
  },
  updateLead: async (id, leadData) => {
    const res = await api.put(`/crm/leads/${id}`, leadData);
    return res.data;
  },
  convertLead: async (id, convertData = {}) => {
    const res = await api.post(`/crm/leads/${id}/convert`, convertData);
    return res.data;
  },
  getInteractions: async (params = {}) => {
    const res = await api.get('/crm/interactions', { params });
    return res.data;
  },
  createInteraction: async (interactionData) => {
    const res = await api.post('/crm/interactions', interactionData);
    return res.data;
  },
  getCustomerTimeline: async (customerId) => {
    const res = await api.get(`/crm/customers/${customerId}/timeline`);
    return res.data;
  },
};
