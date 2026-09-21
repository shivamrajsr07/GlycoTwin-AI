import type { DigitalTwin, Prediction } from '../types';

export default function DigitalTwinPage({ twin, prediction }: { twin: DigitalTwin | null; prediction: Prediction | null }) {
  if (!twin || !prediction) return <div className="rounded-2xl border border-dashed p-8 text-slate-500">Digital twin state unavailable.</div>;

  return (
    <div className="grid gap-6 lg:grid-cols-2">
      <div className="rounded-2xl border border-slate-200 bg-white p-6 text-slate-900 shadow-sm">
        <h3 className="mb-4 text-xl font-semibold text-slate-900">Digital Twin State</h3>
        <div className="space-y-4">
          <div className="rounded-xl bg-slate-50 p-4">
            <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Physiological state</p>
            <p className="mt-2 text-lg font-semibold">Glucose: {twin.physiological_state.glucose} mg/dL</p>
            <p>Heart rate: {twin.physiological_state.heart_rate} bpm</p>
            <p>HRV: {twin.physiological_state.hrv}</p>
          </div>
          <div className="rounded-xl bg-slate-50 p-4">
            <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Metabolic state</p>
            <p className="mt-2">HbA1c: {twin.metabolic_state.hba1c}</p>
            <p>BMI: {twin.metabolic_state.bmi}</p>
            <p>Diabetes duration: {twin.metabolic_state.diabetes_duration} years</p>
          </div>
        </div>
      </div>

      <div className="rounded-2xl border border-slate-200 bg-white p-6 text-slate-900 shadow-sm">
        <h3 className="mb-4 text-xl font-semibold text-slate-900">Prediction</h3>
        <div className="rounded-xl bg-slate-900 p-4 text-white">
          <p className="text-sm text-slate-300">Predicted glucose in 2h</p>
          <p className="mt-2 text-4xl font-bold">{prediction.predicted_glucose_2h}</p>
          <p className="mt-2 text-sm text-slate-300">Model confidence {prediction.confidence}</p>
        </div>
      </div>
    </div>
  );
}
