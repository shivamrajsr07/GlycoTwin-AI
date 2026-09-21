from app.services.prediction import predict_glucose


def test_prediction_output_shapes() -> None:
    prediction = predict_glucose('PT-001')
    assert 'patient_id' in prediction
    assert 'predicted_glucose_2h' in prediction
    assert 'risk_score' in prediction
    assert 'risk_level' in prediction
    assert prediction['prediction_horizon_minutes'] == 120
