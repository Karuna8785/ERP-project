import api from './api';

export const procurementService = {
  getSuppliers: async () => {
    const res = await api.get('/procurement/suppliers');
    return res.data;
  },
  createSupplier: async (data) => {
    const res = await api.post('/procurement/suppliers', data);
    return res.data;
  },
  getPurchaseOrders: async () => {
    const res = await api.get('/procurement/orders');
    return res.data;
  },
  createPurchaseOrder: async (data) => {
    const res = await api.post('/procurement/orders', data);
    return res.data;
  },
  receiveGoods: async (orderId, data = {}) => {
    const res = await api.post(`/procurement/orders/${orderId}/receive`, data);
    return res.data;
  },
};
