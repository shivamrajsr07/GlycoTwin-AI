export interface PatientSummary {
  patient_id: string;
  age: number;
  sex: string;
  bmi: number;
  hba1c: number;
  diabetes_duration: number;
  risk_score?: number;
  risk_level?: string;
}

export interface PatientDetail {
  patient_id: string;
  age: number;
  sex: string;
  height: number;
  weight: number;
  bmi: number;
  hba1c: number;
  fasting_glucose: number;
  cholesterol: number;
  systolic_bp: number;
  diastolic_bp: number;
  diabetes_duration: number;
  family_history: boolean;
  medications: string;
}

export interface Prediction {
  patient_id: string;
  current_glucose: number;
  predicted_glucose_2h: number;
  risk_score: number;
  risk_level: string;
  confidence: number;
  prediction_horizon_minutes: number;
}

export interface ExplanationItem {
  feature: string;
  impact: number;
  direction: string;
}

export interface DigitalTwin {
  patient_id: string;
  physiological_state: {
    glucose: number;
    heart_rate: number;
    hrv: number;
    sleep: number;
    activity: number;
  };
  metabolic_state: {
    hba1c: number;
    bmi: number;
    diabetes_duration: number;
  };
  risk_state: {
    score: number;
    level: string;
  };
  prediction: {
    glucose_2h: number;
  };
}

export interface SimulationResult {
  baseline: { predicted_glucose: number; risk_score: number };
  scenario: { predicted_glucose: number; risk_score: number };
  delta: { glucose: number; risk: number };
  feature_changes?: {
    meal_carbs?: number;
    steps_6h?: number;
    sleep_duration?: number;
  };
}

export interface DashboardSummary {
  total_patients: number;
  high_risk_patients: number;
  average_risk: number;
  data_timestamp: string;
  patient_id: string;
}
