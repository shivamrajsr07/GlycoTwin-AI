from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.services.digital_twin import update_digital_twin
from app.utils.data_loader import load_patients, load_wearable_data

router = APIRouter()


def _overview_risk(patient: dict) -> tuple[int, str]:
    score = min(
        100,
        max(
            0,
            28
            + 0.9 * float(patient['BMI'])
            + 9 * max(0, float(patient['HbA1c']) - 6)
            + 0.12 * max(0, float(patient['fasting_glucose']) - 110),
        ),
    )
    rounded_score = int(round(score))
    level = 'HIGH' if rounded_score >= 75 else 'MODERATE' if rounded_score >= 45 else 'LOW'
    return rounded_score, level


@router.get('/api/patients')
def list_patients() -> list[dict]:
    patients = load_patients().to_dict(orient='records')
    output = []
    for patient in patients:
        risk_score, risk_level = _overview_risk(patient)
        output.append({
            'patient_id': patient['patient_id'],
            'age': int(patient['age']),
            'sex': patient['sex'],
            'bmi': round(float(patient['BMI']), 1),
            'hba1c': round(float(patient['HbA1c']), 2),
            'diabetes_duration': int(patient['diabetes_duration']),
            'risk_score': risk_score,
            'risk_level': risk_level,
        })
    return output


@router.get('/api/patients/{patient_id}')
def patient_detail(patient_id: str) -> dict:
    patients = load_patients()
    patient = patients[patients['patient_id'] == patient_id]
    if patient.empty:
        raise HTTPException(status_code=404, detail='Patient not found')
    row = patient.iloc[0].to_dict()
    return {
        'patient_id': row['patient_id'],
        'age': int(row['age']),
        'sex': row['sex'],
        'height': float(row['height']),
        'weight': float(row['weight']),
        'bmi': round(float(row['BMI']), 1),
        'hba1c': round(float(row['HbA1c']), 2),
        'fasting_glucose': round(float(row['fasting_glucose']), 1),
        'cholesterol': round(float(row['cholesterol']), 1),
        'systolic_bp': int(row['systolic_bp']),
        'diastolic_bp': int(row['diastolic_bp']),
        'diabetes_duration': int(row['diabetes_duration']),
        'family_history': bool(row['family_history']),
        'medications': row['medications'],
    }


@router.get('/api/patients/{patient_id}/timeline')
def patient_timeline(patient_id: str) -> list[dict]:
    wearable = load_wearable_data()
    patient_series = wearable[wearable['patient_id'] == patient_id].sort_values('timestamp').tail(24)
    if patient_series.empty:
        raise HTTPException(status_code=404, detail='Patient timeline not found')
    result = patient_series.to_dict(orient='records')
    for row in result:
        row['timestamp'] = datetime.fromisoformat(str(row['timestamp'])) .isoformat()
    return result


@router.get('/api/patients/{patient_id}/twin')
def patient_twin(patient_id: str) -> dict:
    patients = load_patients()
    if patients[patients['patient_id'] == patient_id].empty:
        raise HTTPException(status_code=404, detail='Patient not found')
    return update_digital_twin(patient_id)
