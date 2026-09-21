import { useState } from 'react';

import type { SimulationResult } from '../types';

interface SimulationPageProps {
  simulation: SimulationResult | null;
  onSimulate: (mealCarbs: number, steps: number, sleep: number) => void;
}

export default function SimulationPage({ simulation, onSimulate }: SimulationPageProps) {
  const [mealCarbs, setMealCarbs] = useState(-30);
  const [steps, setSteps] = useState(3000);
  const [sleep, setSleep] = useState(1);

  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm text-slate-900">
      <h2 className="mb-4 text-xl font-semibold text-slate-900">What-if simulator</h2>
      <div className="grid gap-6 lg:grid-cols-[1fr_1fr]">
        <div className="space-y-4">
          <label className="block text-sm font-medium text-slate-700">Meal carbohydrate change <span className="font-semibold text-slate-900">{mealCarbs}g</span></label>
          <input type="range" min={-80} max={80} value={mealCarbs} onChange={(event) => setMealCarbs(Number(event.target.value))} className="w-full" />

          <label className="block text-sm font-medium text-slate-700">Additional activity <span className="font-semibold text-slate-900">{steps} steps</span></label>
          <input type="range" min={0} max={5000} step={250} value={steps} onChange={(event) => setSteps(Number(event.target.value))} className="w-full" />

          <label className="block text-sm font-medium text-slate-700">Sleep change <span className="font-semibold text-slate-900">{sleep} hours</span></label>
          <input type="range" min={-2} max={3} step={0.5} value={sleep} onChange={(event) => setSleep(Number(event.target.value))} className="w-full" />

          <button type="button" onClick={() => onSimulate(mealCarbs, steps, sleep)} className="rounded-xl bg-slate-900 px-4 py-3 font-medium text-white transition hover:bg-teal-800">Simulate Scenario</button>
        </div>

        <div className="space-y-4 rounded-2xl bg-slate-50 p-4">
          <h3 className="text-lg font-semibold text-slate-900">Scenario results</h3>
          {simulation ? (
            <>
              <div className="rounded-xl bg-white p-4">
                <p className="text-sm text-slate-500">Baseline</p>
                <p className="text-xl font-semibold">{simulation.baseline.predicted_glucose} mg/dL</p>
                <p className="text-sm">Risk {simulation.baseline.risk_score}</p>
              </div>
              <div className="rounded-xl bg-white p-4">
                <p className="text-sm text-slate-500">Simulated</p>
                <p className="text-xl font-semibold">{simulation.scenario.predicted_glucose} mg/dL</p>
                <p className="text-sm">Risk {simulation.scenario.risk_score}</p>
              </div>
              <p className="text-sm text-slate-600">Scenario suggests a lower predicted glucose trajectory.</p>
            </>
          ) : (
            <p className="text-sm text-slate-500">Run a scenario to compare current and simulated risk.</p>
          )}
        </div>
      </div>
    </div>
  );
}
