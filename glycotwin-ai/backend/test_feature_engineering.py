from app.services.feature_engineering import compute_patient_features


def test_feature_engineering_has_required_keys() -> None:
    features = compute_patient_features('PT-001')
    required = ['patient_id', 'age', 'BMI', 'HbA1c', 'current_glucose', 'sleep_duration', 'meal_carbs', 'glucose_lag_1']
    for key in required:
        assert key in features, f'Missing required feature {key}'
