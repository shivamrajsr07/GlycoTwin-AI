from __future__ import annotations

from app.services.prediction import predict_glucose
from app.utils.data_loader import load_patients, load_wearable_data


def update_digital_twin(patient_id: str) -> dict:
    patients = load_patients().set_index('patient_id')
    wearable = load_wearable_data()
    patient = patients.loc[patient_id]
    patient_wearable = wearable[wearable['patient_id'] == patient_id].sort_values('timestamp')
    latest = patient_wearable.iloc[-1]
    prediction = predict_glucose(patient_id)

    return {
        'patient_id': patient_id,
        'physiological_state': {
            'glucose': round(float(latest['glucose']), 1),
            'heart_rate': round(float(latest['heart_rate']), 1),
            'hrv': round(float(latest['hrv']), 1),
            'sleep': round(float(latest['sleep_duration']), 1),
            'activity': int(latest['steps']),
        },
        'metabolic_state': {
            'hba1c': float(patient['HbA1c']),
            'bmi': float(patient['BMI']),
            'diabetes_duration': int(patient['diabetes_duration']),
        },
        'risk_state': {
            'score': int(prediction['risk_score']),
            'level': prediction['risk_level'],
        },
        'prediction': {
            'glucose_2h': round(float(prediction['predicted_glucose_2h']), 1),
        },
    }
