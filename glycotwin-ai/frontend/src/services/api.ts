import axios from 'axios';

import type {
  DashboardSummary,
  DigitalTwin,
  ExplanationItem,
  PatientDetail,
  PatientSummary,
  Prediction,
  SimulationResult,
} from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

export const getDashboardSummary = async (): Promise<DashboardSummary> => {
  const { data } = await api.get<DashboardSummary>('/api/dashboard/summary');
  return data;
};

export const getPatients = async (): Promise<PatientSummary[]> => {
  const { data } = await api.get<PatientSummary[]>('/api/patients');
  return data;
};

export const getPatient = async (patientId: string): Promise<PatientDetail> => {
  const { data } = await api.get<PatientDetail>(`/api/patients/${patientId}`);
  return data;
};

export const getPatientTimeline = async (patientId: string) => {
  const { data } = await api.get(`/api/patients/${patientId}/timeline`);
  return data;
};

export const getPrediction = async (patientId: string): Promise<Prediction> => {
  const { data } = await api.get<Prediction>(`/api/patients/${patientId}/prediction`);
  return data;
};

export const getExplanation = async (patientId: string): Promise<ExplanationItem[]> => {
  const { data } = await api.get<ExplanationItem[]>(`/api/patients/${patientId}/explanation`);
  return data;
};

export const getDigitalTwin = async (patientId: string): Promise<DigitalTwin> => {
  const { data } = await api.get<DigitalTwin>(`/api/patients/${patientId}/twin`);
  return data;
};

export const simulateScenario = async (
  patientId: string,
  mealCarbsChange: number,
  additionalSteps: number,
  sleepChangeHours: number,
): Promise<SimulationResult> => {
  const { data } = await api.post<SimulationResult>('/api/simulation', {
    patient_id: patientId,
    meal_carbs_change: mealCarbsChange,
    additional_steps: additionalSteps,
    sleep_change_hours: sleepChangeHours,
  });
  return data;
};

export { API_BASE_URL };
