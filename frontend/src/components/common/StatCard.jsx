import React from 'react';
import { ArrowUp, ArrowDown } from 'lucide-react';

export const StatCard = ({
  title,
  value,
  subtitle,
  icon: Icon,
  color = 'indigo',
  trend,
  trendValue,
}) => {
  // Handle trend as object (e.g. { positive: true, value: '+12.8%' }) or string ('up' / 'down')
  const isUp = typeof trend === 'object' ? trend?.positive : trend === 'up';
  const displayTrendVal = typeof trend === 'object' ? trend?.value : trendValue;

  return (
    <div className="bg-white rounded-2xl p-6 border border-[#ece4d6] shadow-[0_2px_8px_rgba(40,20,10,0.04)] hover:shadow-md transition-all duration-200 group">
      {/* Top row: Title & Circular Icon */}
      <div className="flex items-start justify-between">
        <span className="text-[11px] font-bold tracking-wider uppercase text-[#5a4e48] pt-1">
          {title}
        </span>
        {Icon && (
          <div className="w-10 h-10 rounded-full bg-[#fbf3e6] border border-[#f0dfc8] flex items-center justify-center text-[#b8860b] group-hover:scale-105 transition-transform shrink-0">
            <Icon className="w-4 h-4 stroke-[2]" />
          </div>
        )}
      </div>

      {/* Value & Trend */}
      <div className="mt-4 flex items-baseline gap-3">
        <div className="text-3xl font-serif font-bold text-[#1a1112] tracking-tight">
          {value}
        </div>
        {displayTrendVal && (
          <div
            className={`inline-flex items-center text-xs font-bold ${
              isUp ? 'text-[#1e7e48]' : 'text-[#a32235]'
            }`}
          >
            {isUp ? (
              <ArrowUp className="w-3.5 h-3.5 mr-0.5 stroke-[2.5]" />
            ) : (
              <ArrowDown className="w-3.5 h-3.5 mr-0.5 stroke-[2.5]" />
            )}
            {displayTrendVal}
          </div>
        )}
      </div>

      {/* Subtitle */}
      {subtitle && (
        <p className="mt-2 text-xs text-[#71655e] font-medium leading-relaxed">
          {subtitle}
        </p>
      )}
    </div>
  );
};

export default StatCard;
