import { LineChart, Line, ResponsiveContainer, XAxis, YAxis, Tooltip } from 'recharts';

import type { Prediction } from '../types';

export default function PredictionsPage({ prediction }: { prediction: Prediction | null }) {
  if (!prediction) return <div className="rounded-2xl border border-dashed p-8 text-slate-500">Prediction unavailable.</div>;

  const data = [
    { time: 'Now', value: prediction.current_glucose },
    { time: '+30m', value: prediction.current_glucose + 10 },
    { time: '+60m', value: prediction.predicted_glucose_2h * 0.9 },
    { time: '+120m', value: prediction.predicted_glucose_2h },
  ];

  return (
    <div className="space-y-6 rounded-2xl border border-slate-200 bg-white p-6 text-slate-900 shadow-sm">
      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <div><p className="text-sm text-slate-500">Prediction horizon</p><p className="text-xl font-semibold">2 hours</p></div>
        <div><p className="text-sm text-slate-500">Current glucose</p><p className="text-xl font-semibold">{prediction.current_glucose}</p></div>
        <div><p className="text-sm text-slate-500">Predicted glucose</p><p className="text-xl font-semibold">{prediction.predicted_glucose_2h}</p></div>
        <div><p className="text-sm text-slate-500">Confidence</p><p className="text-xl font-semibold">{prediction.confidence}</p></div>
      </div>

      <div className="h-64 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke="#0f172a" strokeWidth={3} dot={{ r: 4 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
