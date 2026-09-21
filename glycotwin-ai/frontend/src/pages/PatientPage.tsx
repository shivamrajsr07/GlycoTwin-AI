import type { PatientDetail, Prediction } from '../types';

export default function PatientPage({ patient, prediction }: { patient: PatientDetail | null; prediction: Prediction | null }) {
  if (!patient || !prediction) return <div className="rounded-2xl border border-dashed p-8 text-slate-500">Patient history unavailable.</div>;

  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 text-slate-900 shadow-sm">
      <h2 className="mb-4 text-xl font-semibold text-slate-900">Patient details</h2>
      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <div><p className="text-sm text-slate-500">Patient ID</p><p className="font-semibold">{patient.patient_id}</p></div>
        <div><p className="text-sm text-slate-500">Sex</p><p className="font-semibold">{patient.sex}</p></div>
        <div><p className="text-sm text-slate-500">Age</p><p className="font-semibold">{patient.age}</p></div>
        <div><p className="text-sm text-slate-500">BMI</p><p className="font-semibold">{patient.bmi}</p></div>
        <div><p className="text-sm text-slate-500">HbA1c</p><p className="font-semibold">{patient.hba1c}</p></div>
        <div><p className="text-sm text-slate-500">Fasting glucose</p><p className="font-semibold">{patient.fasting_glucose}</p></div>
        <div><p className="text-sm text-slate-500">Blood pressure</p><p className="font-semibold">{patient.systolic_bp}/{patient.diastolic_bp}</p></div>
        <div><p className="text-sm text-slate-500">Diabetes duration</p><p className="font-semibold">{patient.diabetes_duration} years</p></div>
      </div>
      <div className="mt-6 rounded-xl bg-slate-50 p-4">
        <p className="text-sm text-slate-500">Latest risk estimate</p>
        <p className="text-3xl font-bold text-slate-900">{prediction.risk_score}</p>
      </div>
    </div>
  );
}
