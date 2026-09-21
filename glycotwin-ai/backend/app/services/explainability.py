from __future__ import annotations

from app.services.feature_engineering import compute_patient_features


def explain_risk(patient_id: str) -> list[dict]:
    features = compute_patient_features(patient_id)
    contributions = [
        ('meal_carbs', float(features.get('meal_carbs', 0)) * 0.75),
        ('sleep_duration', (7.5 - float(features.get('sleep_duration', 7.5))) * 1.9),
        ('steps_sum_6h', (float(features.get('steps_sum_6h', 0)) / 1200) * 0.7),
        ('HbA1c', max(0.0, float(features.get('HbA1c', 6.0)) - 6.0) * 1.5),
        ('BMI', max(0.0, float(features.get('BMI', 25)) - 25) * 0.5),
        ('current_glucose', max(0.0, float(features.get('current_glucose', 120)) - 120) * 0.22),
        ('heart_rate', max(0.0, float(features.get('heart_rate', 75)) - 75) * 0.35),
    ]

    normalized = []
    total = sum(abs(v) for _, v in contributions) or 1
    for name, value in contributions:
        direction = 'increase' if value >= 0 else 'decrease'
        impact = round(abs(value) / total, 2)
        normalized.append({'feature': name, 'impact': impact, 'direction': direction})
    sorted_out = sorted(normalized, key=lambda item: item['impact'], reverse=True)[:5]
    for item in sorted_out:
        item['impact'] = round(float(item['impact']), 2)
    return sorted_out
