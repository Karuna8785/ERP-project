import api from './api';

export const financeService = {
  getSummary: async () => {
    const res = await api.get('/finance/summary');
    return res.data;
  },
  getExpenses: async () => {
    const res = await api.get('/finance/expenses');
    return res.data;
  },
  createExpense: async (data) => {
    const res = await api.post('/finance/expenses', data);
    return res.data;
  },
};
