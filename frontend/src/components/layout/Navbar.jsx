import React from 'react';
import { useAuth } from '../../context/AuthContext';
import { LogOut, Shield } from 'lucide-react';

export default function Navbar() {
  const { user, logout } = useAuth();

  return (
    <header className="h-16 bg-[#190508] border-b border-[#2e0c14] px-6 flex items-center justify-between sticky top-0 z-30 shadow-md">
      {/* Brand Identity */}
      <div className="flex items-center space-x-3.5">
        {/* Heraldic Crest Emblem */}
        <div className="relative flex items-center justify-center shrink-0">
          <svg className="w-9 h-9 drop-shadow-[0_2px_4px_rgba(0,0,0,0.6)]" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M24 2.5L43.5 13.5V34.5L24 45.5L4.5 34.5V13.5L24 2.5Z" stroke="#dfb15b" strokeWidth="1.5" fill="#20060b" />
            <path d="M24 6.5L39.5 15.5V32.5L24 41.5L8.5 32.5V15.5L24 6.5Z" stroke="#c59d5f" strokeWidth="0.8" strokeDasharray="1.5 1.5" fill="none" opacity="0.75" />
            <text x="24" y="30.5" textAnchor="middle" fill="#dfb15b" fontFamily="'Cinzel', 'Playfair Display', Georgia, serif" fontSize="21" fontWeight="700">S</text>
          </svg>
        </div>

        {/* Brand Text */}
        <div className="flex items-center space-x-3">
          <span className="text-2xl font-serif font-bold tracking-tight text-[#dfb15b]">
            Smart<span className="text-[#f5d791]">ERP</span>
          </span>
          <span className="h-5 w-[1px] bg-[#4a261a]" />
          <span className="text-xs sm:text-sm font-serif font-medium tracking-wide text-[#c5a059]">
            Enterprise Unified Suite
          </span>
        </div>
      </div>

      {/* User Session & Logout */}
      <div className="flex items-center space-x-4 sm:space-x-6">
        {user && (
          <div className="flex items-center space-x-3">
            {/* Avatar */}
            <div className="w-9 h-9 rounded-full bg-[#24080e] border border-[#c59d5f] text-[#dfb15b] flex items-center justify-center font-serif font-bold text-sm shadow-inner">
              {user.full_name ? user.full_name[0].toUpperCase() : 'S'}
            </div>
            <div className="text-left hidden sm:block">
              <div className="text-xs font-semibold text-[#fdfbf7] tracking-wide">
                {user.full_name || 'System Administrator'}
              </div>
              <div className="text-[10px] font-bold text-[#dfb15b] flex items-center gap-1 uppercase tracking-wider mt-0.5">
                <Shield className="w-3 h-3 text-[#dfb15b]" />
                {user.is_superuser ? 'ADMIN' : (user.roles?.[0]?.name || 'ADMIN')}
              </div>
            </div>
          </div>
        )}

        <div className="h-6 w-[1px] bg-[#3a151e]" />

        <button
          onClick={logout}
          className="flex items-center space-x-1.5 px-2.5 py-1.5 text-xs font-medium text-[#dfcfb8] hover:text-[#dfb15b] transition-colors group"
          title="Logout"
        >
          <LogOut className="w-4 h-4 text-[#dfb15b] group-hover:translate-x-0.5 transition-transform" />
          <span className="hidden sm:inline">Logout</span>
        </button>
      </div>
    </header>
  );
}
