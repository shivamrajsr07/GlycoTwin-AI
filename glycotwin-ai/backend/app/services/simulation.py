from __future__ import annotations

from app.services.feature_engineering import compute_patient_features
from app.services.prediction import predict_glucose


def simulate_scenario(patient_id: str, meal_carbs_change: float, additional_steps: int, sleep_change_hours: float) -> dict:
    baseline = predict_glucose(patient_id)
    features = compute_patient_features(patient_id)

    adjusted = dict(features)
    adjusted['meal_carbs'] = max(0.0, float(features.get('meal_carbs', 0)) + float(meal_carbs_change))
    adjusted['steps_sum_6h'] = max(0.0, float(features.get('steps_sum_6h', 0)) + float(additional_steps))
    adjusted['sleep_duration'] = max(4.0, float(features.get('sleep_duration', 7.0)) + float(sleep_change_hours))

    predicted_base = baseline['predicted_glucose_2h']
    predicted_adj = predicted_base + (0.7 * meal_carbs_change) - (0.0035 * additional_steps) + (4.2 * max(0, 7.5 - adjusted['sleep_duration']))
    predicted_adj = max(70, predicted_adj)
    risk_score = int(max(0, min(100, baseline['risk_score'] + (predicted_base - predicted_adj) * 0.7)))
    scenario = {
        'patient_id': patient_id,
        'current_glucose': baseline['current_glucose'],
        'predicted_glucose_2h': round(predicted_adj, 1),
        'risk_score': risk_score,
        'risk_level': 'HIGH' if risk_score >= 75 else 'MODERATE' if risk_score >= 45 else 'LOW',
        'confidence': baseline['confidence'],
        'prediction_horizon_minutes': 120,
    }

    delta_glucose = round(predicted_base - predicted_adj, 1)
    delta_risk = baseline['risk_score'] - risk_score
    return {
        'baseline': {'predicted_glucose': round(predicted_base, 1), 'risk_score': baseline['risk_score']},
        'scenario': {'predicted_glucose': round(predicted_adj, 1), 'risk_score': risk_score},
        'delta': {'glucose': delta_glucose, 'risk': delta_risk},
        'feature_changes': {
            'meal_carbs': round(adjusted['meal_carbs'] - features['meal_carbs'], 1),
            'steps_6h': round(adjusted['steps_sum_6h'] - features['steps_sum_6h'], 1),
            'sleep_duration': round(adjusted['sleep_duration'] - features['sleep_duration'], 1),
        },
    }
