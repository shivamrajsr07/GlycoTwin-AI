from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from app.core.config import MODEL_DIR
from app.services.feature_engineering import FEATURE_COLUMNS, build_training_dataset, compute_patient_features


def _model_path(name: str) -> Path:
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    return MODEL_DIR / name


def _risk_level(score: float) -> str:
    if score >= 75:
        return 'HIGH'
    if score >= 45:
        return 'MODERATE'
    return 'LOW'


def _fallback_prediction(features: dict) -> dict:
    meal = float(features.get('meal_carbs', 0))
    sleep = float(features.get('sleep_duration', 7.0))
    steps = float(features.get('steps_sum_6h', 0))
    glucose = float(features.get('current_glucose', 120))
    bmi = float(features.get('BMI', 25))
    hba1c = float(features.get('HbA1c', 6.0))
    age = float(features.get('age', 50))

    predicted = (
        glucose
        + 0.52 * meal
        - 0.0035 * steps
        + 3.2 * max(0, 7.5 - sleep)
        + 0.8 * max(0, hba1c - 6)
        + 0.4 * max(0, bmi - 25)
        + 0.2 * max(0, age - 50)
        + 8
    )
    risk_score = min(100, max(0, 28 + 0.9 * bmi + 9 * max(0, hba1c - 6.0) + 0.35 * max(0, predicted - 140) + 0.08 * max(0, meal - 25) - 0.01 * steps / 2 + 3 * max(0, 7.5 - sleep)))
    confidence = float(np.clip(0.54 + 0.01 * abs(predicted - glucose) + 0.08 * min(1, hba1c / 8), 0.52, 0.96))
    return {
        'patient_id': features.get('patient_id', 'unknown'),
        'current_glucose': round(glucose, 1),
        'predicted_glucose_2h': round(float(predicted), 1),
        'risk_score': int(round(risk_score)),
        'risk_level': _risk_level(risk_score),
        'confidence': round(confidence, 2),
        'prediction_horizon_minutes': 120,
    }


def _model_predict(features: dict) -> dict | None:
    reg_path = _model_path('glucose_regressor.joblib')
    clf_path = _model_path('spike_classifier.joblib')
    if not reg_path.exists() or not clf_path.exists():
        return None
    reg = joblib.load(reg_path)
    clf = joblib.load(clf_path)
    x = pd.DataFrame([{column: float(features.get(column, 0)) for column in FEATURE_COLUMNS}], columns=FEATURE_COLUMNS)
    reg_pred = float(reg.predict(x)[0])
    proba = float(clf.predict_proba(x)[0][1])
    risk_score = int(np.clip((reg_pred - 120) * 1.2 + proba * 100, 0, 100))
    return {
        'patient_id': features.get('patient_id', 'unknown'),
        'current_glucose': float(features.get('current_glucose', 120)),
        'predicted_glucose_2h': round(reg_pred, 1),
        'risk_score': risk_score,
        'risk_level': _risk_level(risk_score),
        'confidence': round(float(np.clip(0.55 + proba * 0.4, 0.5, 0.96)), 2),
        'prediction_horizon_minutes': 120,
    }


def train_models_if_needed() -> None:
    reg_path = _model_path('glucose_regressor.joblib')
    clf_path = _model_path('spike_classifier.joblib')
    if reg_path.exists() and clf_path.exists():
        return
    dataset = build_training_dataset()
    if dataset.empty:
        return
    X = dataset[FEATURE_COLUMNS].fillna(0)
    y_reg = dataset['future_glucose']
    y_cls = dataset['spike_flag']

    reg = RandomForestRegressor(n_estimators=150, random_state=42, min_samples_leaf=2)
    reg.fit(X, y_reg)
    clf = RandomForestClassifier(n_estimators=120, random_state=42, class_weight='balanced')
    clf.fit(X, y_cls)

    joblib.dump(reg, reg_path)
    joblib.dump(clf, clf_path)


def predict_glucose(patient_id: str) -> dict:
    features = compute_patient_features(patient_id)
    model_prediction = _model_predict(features)
    if model_prediction is not None:
        return model_prediction
    return _fallback_prediction(features)


def predict_risk(patient_id: str) -> dict:
    return predict_glucose(patient_id)
