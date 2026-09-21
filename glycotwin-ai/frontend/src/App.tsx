import { motion } from 'framer-motion';
import {
  Activity,
  BarChart3,
  BriefcaseMedical,
  Download,
  Gauge,
  LayoutGrid,
  MoonStar,
  UserRound,
} from 'lucide-react';
import { useEffect, useMemo, useState } from 'react';

import DashboardPage from './pages/DashboardPage';
import DigitalTwinPage from './pages/DigitalTwinPage';
import PatientPage from './pages/PatientPage';
import PredictionsPage from './pages/PredictionsPage';
import SimulationPage from './pages/SimulationPage';
import {
  getDashboardSummary,
  getDigitalTwin,
  getExplanation,
  getPatient,
  getPatients,
  getPrediction,
  simulateScenario,
} from './services/api';
import type {
  DashboardSummary,
  DigitalTwin,
  ExplanationItem,
  PatientDetail,
  PatientSummary,
  Prediction,
  SimulationResult,
} from './types';

const navItems = [
  { key: 'overview', label: 'Overview', icon: LayoutGrid },
  { key: 'patients', label: 'Patients', icon: UserRound },
  { key: 'digital-twin', label: 'Digital Twin', icon: Activity },
  { key: 'predictions', label: 'Predictions', icon: BarChart3 },
  { key: 'simulation', label: 'What-if Simulation', icon: Gauge },
] as const;

function App() {
  const [activeView, setActiveView] = useState<(typeof navItems)[number]['key']>('overview');
  const [patients, setPatients] = useState<PatientSummary[]>([]);
  const [patientId, setPatientId] = useState('PT-001');
  const [patient, setPatient] = useState<PatientDetail | null>(null);
  const [prediction, setPrediction] = useState<Prediction | null>(null);
  const [summary, setSummary] = useState<DashboardSummary | null>(null);
  const [explanation, setExplanation] = useState<ExplanationItem[]>([]);
  const [twin, setTwin] = useState<DigitalTwin | null>(null);
  const [simulation, setSimulation] = useState<SimulationResult | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const refreshPatientData = async (selectedId: string) => {
    setLoading(true);
    setError(null);
    try {
      const [currentPatient, currentPrediction, currentTwin, currentExplanation, currentSummary] = await Promise.all([
        getPatient(selectedId),
        getPrediction(selectedId),
        getDigitalTwin(selectedId),
        getExplanation(selectedId),
        getDashboardSummary(),
      ]);

      setPatient(currentPatient);
      setPrediction(currentPrediction);
      setTwin(currentTwin);
      setExplanation(currentExplanation);
      setSummary(currentSummary);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unable to load patient data.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const fetchOverview = async () => {
      try {
        const [patientList, summaryData] = await Promise.all([getPatients(), getDashboardSummary()]);
        setPatients(patientList);
        setSummary(summaryData);
        if (patientList.length > 0) {
          setPatientId(patientList[0].patient_id);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unable to load patient list.');
      }
    };

    void fetchOverview();
  }, []);

  useEffect(() => {
    if (patientId) {
      void refreshPatientData(patientId);
    }
  }, [patientId]);

  const handleSimulate = async (mealCarbsChange: number, additionalSteps: number, sleepChangeHours: number) => {
    try {
      const response = await simulateScenario(patientId, mealCarbsChange, additionalSteps, sleepChangeHours);
      setSimulation(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unable to run simulation.');
    }
  };

  const patientName = useMemo(() => (patient ? `Patient ${patient.patient_id}` : 'Patient Selection'), [patient]);

  const exportSnapshot = () => {
    const snapshot = JSON.stringify({ patient, prediction, summary, explanation }, null, 2);
    const blob = new Blob([snapshot], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${patientId}-glycotwin-snapshot.json`;
    link.click();
    URL.revokeObjectURL(url);
  };

  const renderActiveView = () => {
    if (loading) {
      return <div className="rounded-2xl border border-dashed border-slate-300 bg-slate-100 p-8 text-slate-500">Loading patient telemetry and model outputs…</div>;
    }

    if (error) {
      return <div className="rounded-2xl border border-red-200 bg-red-50 p-8 text-red-700">{error}</div>;
    }

    switch (activeView) {
      case 'patients':
        return <PatientPage patient={patient} prediction={prediction} />;
      case 'digital-twin':
        return <DigitalTwinPage twin={twin} prediction={prediction} />;
      case 'predictions':
        return <PredictionsPage prediction={prediction} />;
      case 'simulation':
        return <SimulationPage simulation={simulation} onSimulate={handleSimulate} />;
      default:
        return <DashboardPage patient={patient} prediction={prediction} summary={summary} explanation={explanation} />;
    }
  };

  return (
    <div className="bio-shell min-h-screen text-slate-100">
      <div className="flex min-h-screen">
        <aside className="w-72 border-r border-teal-200/10 bg-[#061615]/90 px-5 py-6 text-slate-200 backdrop-blur-xl">
          <div className="mb-8 flex items-center gap-3">
            <div className="rounded-xl bg-teal-300/15 p-2 text-teal-200 shadow-[0_0_24px_rgba(85,230,193,0.18)]">
              <BriefcaseMedical size={20} />
            </div>
            <div>
              <div className="text-xl font-bold tracking-tight text-white">GlycoTwin AI</div>
              <div className="text-[10px] uppercase tracking-[0.24em] text-teal-300/70">Metabolic intelligence</div>
            </div>
          </div>

          <nav className="space-y-2">
            {navItems.map(({ key, label, icon: Icon }) => (
              <button
                key={key}
                type="button"
                onClick={() => setActiveView(key)}
                className={`flex w-full items-center gap-3 rounded-xl px-3 py-3 text-left text-sm font-medium transition ${
                  activeView === key ? 'bg-teal-300/15 text-teal-100 shadow-[inset_3px_0_0_#55e6c1]' : 'text-slate-400 hover:bg-teal-200/10 hover:text-teal-100'
                }`}
              >
                <Icon size={16} />
                {label}
              </button>
            ))}
          </nav>

          <div className="bio-card mt-10 rounded-2xl p-4 text-sm text-slate-300">
            <p className="font-medium text-slate-100">System Status</p>
            <p className="mt-1 flex items-center gap-2 text-emerald-400"><span className="h-2 w-2 rounded-full bg-emerald-400" /> Model online</p>
            <p className="mt-3 text-slate-400">Model version v1.8.2</p>
            <p className="mt-1 text-slate-400">Data timestamp {summary?.data_timestamp ?? '—'}</p>
          </div>
        </aside>

        <main className="flex-1">
          <header className="border-b border-teal-200/10 bg-[#071c25]/70 px-6 py-5 backdrop-blur-xl">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <div>
                <p className="text-sm uppercase tracking-[0.2em] text-teal-300/70">Digital Twin Command Center</p>
                <h1 className="mt-1 text-3xl font-bold text-white">{patientName}</h1>
              </div>

              <div className="flex items-center gap-3">
                <label className="flex items-center gap-2 rounded-xl border border-teal-200/15 bg-teal-100/5 px-3 py-2 text-sm text-slate-300">
                  <span>Patient</span>
                  <select
                    value={patientId}
                    onChange={(event) => setPatientId(event.target.value)}
                    className="bg-transparent font-medium text-teal-100 outline-none"
                    aria-label="Patient selector"
                  >
                    {patients.map((entry) => (
                      <option key={entry.patient_id} value={entry.patient_id}>{entry.patient_id}</option>
                    ))}
                  </select>
                </label>
                <div className="flex items-center gap-2 rounded-full bg-teal-300/10 px-3 py-2 text-sm font-medium text-teal-200">
                  <span className="h-2.5 w-2.5 rounded-full bg-emerald-500" />
                  Digital Twin Active
                </div>
              </div>
            </div>
          </header>

          <div className="p-6">
            <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="bio-card mb-6 rounded-2xl p-4">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div>
                  <p className="text-sm text-teal-100/60">Not for clinical diagnosis or treatment.</p>
                  <p className="text-sm font-medium text-slate-200">Model simulation only. Not clinical advice.</p>
                </div>
                <div className="flex gap-2 text-sm text-slate-600">
                  <button type="button" onClick={exportSnapshot} className="inline-flex items-center gap-2 rounded-xl border border-teal-200/15 bg-teal-100/5 px-3 py-2 transition hover:bg-teal-300/15"><Download size={15} /> Export snapshot</button>
                  <button type="button" onClick={() => setActiveView('simulation')} className="inline-flex items-center gap-2 rounded-xl border border-teal-200/15 bg-teal-100/5 px-3 py-2 transition hover:bg-teal-300/15"><MoonStar size={15} /> Run a scenario</button>
                </div>
              </div>
            </motion.div>

            {renderActiveView()}
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;
