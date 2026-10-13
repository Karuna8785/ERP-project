import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { useNotify } from '../../context/NotificationContext';
import { Eye, EyeOff, Lock, User, ArrowRight, Loader2 } from 'lucide-react';

export const Login = () => {
  const { login } = useAuth();
  const notify = useNotify();
  const navigate = useNavigate();

  const [usernameOrEmail, setUsernameOrEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
    setErrorMsg('');
    if (!usernameOrEmail || !password) {
      setErrorMsg('Please enter both username/email and password.');
      return;
    }

    setLoading(true);
    try {
      await login(usernameOrEmail, password);
      notify.success('Authentication successful! Welcome to SmartERP.');
      navigate('/');
    } catch (err) {
      const detail = err.response?.data?.detail || 'Invalid username or password.';
      setErrorMsg(detail);
      notify.error(detail);
    } finally {
      setLoading(false);
    }
  };

  const handleQuickLogin = async (user, pass) => {
    setUsernameOrEmail(user);
    setPassword(pass);
    setLoading(true);
    setErrorMsg('');
    try {
      await login(user, pass);
      notify.success(`Logged in as ${user}!`);
      navigate('/');
    } catch (err) {
      const detail = err.response?.data?.detail || 'Quick login failed';
      setErrorMsg(detail);
      notify.error(detail);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#190508] flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative overflow-hidden">
      {/* Background Lighting Gradients */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#5c1524]/30 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-10 right-10 w-80 h-80 bg-[#c59d5f]/10 rounded-full blur-3xl pointer-events-none" />

      {/* Header */}
      <div className="sm:mx-auto sm:w-full sm:max-w-md text-center z-10">
        <div className="inline-flex w-16 h-16 items-center justify-center mb-4">
          <svg className="w-16 h-16 drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)]" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M24 2.5L43.5 13.5V34.5L24 45.5L4.5 34.5V13.5L24 2.5Z" stroke="#dfb15b" strokeWidth="1.5" fill="#20060b" />
            <path d="M24 6.5L39.5 15.5V32.5L24 41.5L8.5 32.5V15.5L24 6.5Z" stroke="#c59d5f" strokeWidth="0.8" strokeDasharray="1.5 1.5" fill="none" opacity="0.75" />
            <text x="24" y="30.5" textAnchor="middle" fill="#dfb15b" fontFamily="'Cinzel', 'Playfair Display', Georgia, serif" fontSize="21" fontWeight="700">S</text>
          </svg>
        </div>
        <h2 className="text-3xl font-serif font-bold tracking-tight text-[#dfb15b]">
          Smart<span className="text-[#f5d791]">ERP</span> Portal
        </h2>
        <p className="mt-2 text-xs font-serif text-[#c59d5f] tracking-wide">
          Enterprise Unified Suite • Security & Access Control
        </p>
      </div>

      {/* Login Card */}
      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md z-10 px-4 sm:px-0">
        <div className="bg-[#ffffff] py-8 px-6 sm:px-10 rounded-2xl shadow-2xl border border-[#ece4d6]">
          {errorMsg && (
            <div className="mb-5 p-3.5 rounded-xl bg-[#fdf0f2] border border-[#f5cbce] text-[#9e1c31] text-xs font-medium">
              {errorMsg}
            </div>
          )}

          <form className="space-y-5" onSubmit={handleLoginSubmit}>
            {/* Username/Email */}
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#5f514d] mb-1.5">
                Username or Email
              </label>
              <div className="relative rounded-xl shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#a1938f]">
                  <User className="h-4 w-4" />
                </div>
                <input
                  type="text"
                  required
                  value={usernameOrEmail}
                  onChange={(e) => setUsernameOrEmail(e.target.value)}
                  placeholder="admin or user@smarterp.local"
                  className="block w-full pl-10 pr-3.5 py-2.5 bg-white border border-[#ded4c3] rounded-xl text-sm text-[#1c1214] placeholder-[#a1938f] focus:outline-none focus:ring-2 focus:ring-[#c59d5f] focus:border-transparent transition-all"
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#5f514d] mb-1.5">
                Password
              </label>
              <div className="relative rounded-xl shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-[#a1938f]">
                  <Lock className="h-4 w-4" />
                </div>
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••••••"
                  className="block w-full pl-10 pr-10 py-2.5 bg-white border border-[#ded4c3] rounded-xl text-sm text-[#1c1214] placeholder-[#a1938f] focus:outline-none focus:ring-2 focus:ring-[#c59d5f] focus:border-transparent transition-all"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute inset-y-0 right-0 pr-3.5 flex items-center text-[#8a7a76] hover:text-[#1c1214]"
                >
                  {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                </button>
              </div>
            </div>

            {/* Submit Button */}
            <div>
              <button
                type="submit"
                disabled={loading}
                className="w-full flex justify-center items-center py-2.5 px-4 rounded-xl text-sm font-semibold text-white bg-[#5c1524] hover:bg-[#4a101d] border border-[#781d30] shadow-md transition-all disabled:opacity-50 active:scale-[0.98]"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                    <span>Verifying Session...</span>
                  </>
                ) : (
                  <>
                    <span>Sign In to SmartERP</span>
                    <ArrowRight className="w-4 h-4 ml-2" />
                  </>
                )}
              </button>
            </div>
          </form>

          {/* Quick Demo Logins */}
          <div className="mt-6 pt-5 border-t border-[#ece4d6]">
            <span className="block text-[11px] font-bold uppercase tracking-wider text-[#7a6c69] text-center mb-3">
              One-Click Demo Credentials
            </span>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => handleQuickLogin('admin', 'Admin@123')}
                className="px-3 py-2 rounded-xl bg-[#faf6ee] hover:bg-[#5c1524] hover:text-white border border-[#e2d7c7] text-xs font-medium text-[#453738] transition-all text-center group"
              >
                <span className="block font-semibold">Admin</span>
                <span className="text-[10px] text-[#7a6c69] group-hover:text-white/80">Admin@123</span>
              </button>
              <button
                type="button"
                onClick={() => handleQuickLogin('salesmgr', 'Manager@123')}
                className="px-3 py-2 rounded-xl bg-[#faf6ee] hover:bg-[#5c1524] hover:text-white border border-[#e2d7c7] text-xs font-medium text-[#453738] transition-all text-center group"
              >
                <span className="block font-semibold">Sales Manager</span>
                <span className="text-[10px] text-[#7a6c69] group-hover:text-white/80">Manager@123</span>
              </button>
            </div>
          </div>

          {/* Register Link */}
          <div className="mt-6 text-center">
            <p className="text-xs text-[#7a6c69]">
              Need a new enterprise account?{' '}
              <Link to="/register" className="font-semibold text-[#5c1524] hover:underline">
                Register here
              </Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
