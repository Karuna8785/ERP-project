import React from 'react';
import { Outlet, Navigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import Navbar from './Navbar';
import Sidebar from './Sidebar';

export default function AppLayout() {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-[#190508] text-[#dfb15b]">
        <div className="flex flex-col items-center space-y-4">
          <div className="w-12 h-12 border-4 border-[#dfb15b] border-t-transparent rounded-full animate-spin"></div>
          <p className="text-sm font-serif font-medium tracking-wide text-[#dfcfb8]">Loading SmartERP Platform...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div className="min-h-screen flex flex-col bg-[#f9f6f0] text-[#1c1214]">
      <Navbar />
      <div className="flex-1 flex overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto p-6 lg:p-8 bg-[#f9f6f0]">
          <div className="max-w-7xl mx-auto">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  );
}
