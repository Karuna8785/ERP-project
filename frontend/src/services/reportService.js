import api from './api';

export const reportService = {
  getExecutiveReport: async () => {
    const res = await api.get('/reports/executive');
    return res.data;
  },
};
