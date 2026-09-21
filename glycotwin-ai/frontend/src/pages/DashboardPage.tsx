import { motion } from 'framer-motion';
import { AlertTriangle, ArrowUpRight, HeartPulse, MoonStar, TimerReset } from 'lucide-react';
import type { ReactNode } from 'react';

import type { DashboardSummary, ExplanationItem, PatientDetail, Prediction } from '../types';

interface DashboardPageProps {
  patient: PatientDetail | null;
  prediction: Prediction | null;
  summary: DashboardSummary | null;
  explanation: ExplanationItem[];
}

function MetricCard({ title, value, icon }: { title: string; value: ReactNode; icon: ReactNode }) {
  return (
    <div className="bio-card rounded-2xl p-4">
      <div className="mb-3 flex items-center justify-between text-teal-100/55">
        <span className="text-sm font-medium">{title}</span>
        <span className="text-teal-300">{icon}</span>
      </div>
      <div className="text-2xl font-bold text-white">{value}</div>
    </div>
  );
}

export default function DashboardPage({ patient, prediction, summary, explanation }: DashboardPageProps) {
  if (!patient || !prediction || !summary) {
    return <div className="rounded-2xl border border-dashed border-slate-300 bg-slate-100 p-8 text-slate-500">Loading patient dashboard…</div>;
  }

  const riskTone = prediction.risk_score >= 75 ? 'text-red-600' : prediction.risk_score >= 45 ? 'text-amber-600' : 'text-emerald-600';

  return (
    <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} className="space-y-6">
      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <MetricCard title="Current glucose" value={`${prediction.current_glucose} mg/dL`} icon={<HeartPulse size={16} />} />
        <MetricCard title="Risk score" value={<span className={riskTone}>{prediction.risk_score} / 100</span>} icon={<AlertTriangle size={16} />} />
        <MetricCard title="Predicted spike" value={`${prediction.predicted_glucose_2h} mg/dL`} icon={<ArrowUpRight size={16} />} />
        <MetricCard title="Confidence" value={`${(prediction.confidence * 100).toFixed(0)}%`} icon={<TimerReset size={16} />} />
      </div>

      <div className="grid gap-6 xl:grid-cols-[1.4fr_0.6fr]">
        <div className="bio-card rounded-2xl p-6">
          <div className="mb-2 flex items-center justify-between">
            <h2 className="text-lg font-semibold text-white">Patient summary</h2>
            <span className="rounded-full bg-teal-300/15 px-2 py-1 text-xs font-semibold text-teal-200">Digital Twin Active</span>
          </div>
          <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
            <div><p className="text-sm text-teal-100/55">Name</p><p className="text-lg font-semibold text-white">Patient {patient.patient_id}</p></div>
            <div><p className="text-sm text-teal-100/55">Patient ID</p><p className="text-lg font-semibold text-white">{patient.patient_id}</p></div>
            <div><p className="text-sm text-teal-100/55">Age</p><p className="text-lg font-semibold text-white">{patient.age}</p></div>
            <div><p className="text-sm text-teal-100/55">BMI</p><p className="text-lg font-semibold text-white">{patient.bmi}</p></div>
          </div>
        </div>

        <div className="rounded-2xl border border-indigo-300/20 bg-gradient-to-br from-indigo-950 via-[#142753] to-[#0b3740] p-6 text-white shadow-[0_20px_60px_rgba(41,76,160,0.25)]">
          <p className="text-sm uppercase tracking-[0.2em] text-indigo-200">Risk overview</p>
          <div className="mt-3 text-5xl font-bold text-white">{prediction.risk_score}<span className="text-xl text-slate-300"> / 100</span></div>
          <p className="mt-2 text-lg font-medium text-teal-200">{prediction.risk_level} RISK</p>
          <p className="mt-2 text-sm text-indigo-100/70">Predicted glucose spike within 2 hours</p>
        </div>
      </div>

      <div className="bio-card rounded-2xl p-6">
        <h3 className="mb-4 text-lg font-semibold text-white">AI explanation</h3>
        <div className="space-y-3">
          {explanation.map((item) => (
            <div key={item.feature} className="flex items-center justify-between gap-4 rounded-xl border border-teal-100/10 bg-black/10 px-3 py-2">
              <div>
                <p className="font-medium text-teal-50">{item.feature}</p>
                <p className="text-xs text-teal-100/55">{item.direction}</p>
              </div>
              <div className="w-32 rounded-full bg-teal-950">
                <div className="rounded-full bg-gradient-to-r from-teal-400 to-cyan-300 py-1.5" style={{ width: `${Math.max(12, item.impact * 100)}%` }} />
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        <div className="bio-card rounded-2xl p-6">
          <p className="text-sm text-teal-100/55">System status</p>
          <p className="mt-2 text-xl font-semibold text-white">Nominal</p>
        </div>
        <div className="bio-card rounded-2xl p-6">
          <p className="text-sm text-teal-100/55">Model version</p>
          <p className="mt-2 text-xl font-semibold text-white">v1.8.2</p>
        </div>
        <div className="bio-card rounded-2xl p-6">
          <p className="text-sm text-teal-100/55">Data timestamp</p>
          <p className="mt-2 text-xl font-semibold text-white">{summary.data_timestamp}</p>
        </div>
      </div>

      <div className="bio-card rounded-2xl p-6">
        <div className="mb-4 flex items-center justify-between">
          <h3 className="text-lg font-semibold text-white">Alerts</h3>
          <MoonStar className="text-teal-300" size={18} />
        </div>
        <ul className="space-y-2 text-sm text-teal-50/80">
          <li>• High carbohydrate load detected</li>
          <li>• Reduced sleep may increase glucose variability</li>
          <li>• Low activity over previous 6 hours</li>
        </ul>
      </div>
    </motion.div>
  );
}
