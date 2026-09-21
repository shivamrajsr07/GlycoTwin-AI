from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class PatientSummary(BaseModel):
    patient_id: str
    age: int
    sex: str
    bmi: float
    hba1c: float
    diabetes_duration: int
    risk_score: int | None = None
    risk_level: Literal['LOW', 'MODERATE', 'HIGH', 'CRITICAL'] | None = None


class PatientDetail(BaseModel):
    patient_id: str
    age: int
    sex: str
    height: float
    weight: float
    bmi: float
    hba1c: float
    fasting_glucose: float
    cholesterol: float
    systolic_bp: int
    diastolic_bp: int
    diabetes_duration: int
    family_history: bool
    medications: str


class PredictionResponse(BaseModel):
    patient_id: str
    current_glucose: float
    predicted_glucose_2h: float
    risk_score: int
    risk_level: str
    confidence: float
    prediction_horizon_minutes: int = 120


class DigitalTwinResponse(BaseModel):
    patient_id: str
    physiological_state: dict[str, Any]
    metabolic_state: dict[str, Any]
    risk_state: dict[str, Any]
    prediction: dict[str, Any]


class ExplanationItem(BaseModel):
    feature: str
    impact: float
    direction: str


class SimulationRequest(BaseModel):
    patient_id: str
    meal_carbs_change: float = Field(default=0.0, ge=-200, le=200)
    additional_steps: int = Field(default=0, ge=-10000, le=10000)
    sleep_change_hours: float = Field(default=0.0, ge=-5, le=5)


class SimulationResponse(BaseModel):
    baseline: dict[str, float | int]
    scenario: dict[str, float | int]
    delta: dict[str, float | int]


class DashboardSummary(BaseModel):
    total_patients: int
    high_risk_patients: int
    average_risk: float
    data_timestamp: str
    patient_id: str
