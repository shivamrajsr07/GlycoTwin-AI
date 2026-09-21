from dataclasses import dataclass
from typing import Optional


@dataclass
class PatientRecord:
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
