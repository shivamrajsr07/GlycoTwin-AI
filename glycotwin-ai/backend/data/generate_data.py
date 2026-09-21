from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / 'data' / 'raw'
RAW_DIR.mkdir(parents=True, exist_ok=True)


def generate_patients(n_patients: int = 100, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    records = []
    for i in range(1, n_patients + 1):
        age = int(rng.integers(34, 79))
        sex = rng.choice(['Male', 'Female'])
        height = float(rng.uniform(155, 188))
        weight = float(rng.uniform(58, 120))
        bmi = weight / (height / 100) ** 2
        hba1c = float(rng.uniform(5.7, 8.3))
        fasting_glucose = float(rng.uniform(95, 170))
        cholesterol = float(rng.uniform(150, 250))
        systolic_bp = int(rng.integers(115, 170))
        diastolic_bp = int(rng.integers(75, 99))
        diabetes_duration = int(rng.integers(0, 15))
        family_history = bool(rng.integers(0, 2))
        medications = rng.choice(['Metformin', 'GLP-1', 'Sulfonylurea', 'Insulin', 'Combination'])
        patient_id = f'PT-{i:03d}'
        records.append({
            'patient_id': patient_id,
            'age': age,
            'sex': sex,
            'height': round(height, 1),
            'weight': round(weight, 1),
            'BMI': round(bmi, 1),
            'HbA1c': round(hba1c, 2),
            'fasting_glucose': round(fasting_glucose, 1),
            'cholesterol': round(cholesterol, 1),
            'systolic_bp': systolic_bp,
            'diastolic_bp': diastolic_bp,
            'diabetes_duration': diabetes_duration,
            'family_history': family_history,
            'medications': medications,
        })
    return pd.DataFrame(records)


def generate_wearable_data(patients: pd.DataFrame, days: int = 30, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for _, patient in patients.iterrows():
        patient_id = patient['patient_id']
        baseline_glucose = 118 + patient['BMI'] * 0.7 + patient['HbA1c'] * 8 + patient['diabetes_duration'] * 1.4
        sleep_bias = 0.8 * (patient['BMI'] / 30)
        meal_pattern = rng.integers(1, 7, size=days * 24)
        for hour in range(days * 24):
            timestamp = pd.Timestamp('2024-01-01') + pd.Timedelta(hours=hour) + pd.Timedelta(days=0)
            hour_of_day = hour % 24
            day = hour // 24
            is_meal = (hour_of_day in {8, 12, 18, 20})
            meal_carbs = 0.0
            if is_meal:
                meal_carbs = float(rng.normal(35, 20))
                meal_carbs = max(0, meal_carbs)
            steps = max(0, int(rng.normal(900, 600))) if hour_of_day not in {0, 1, 2, 3} else int(rng.normal(200, 150))
            sleep_duration = 7.0 + rng.normal(0, 1.0)
            sleep_quality = float(np.clip(rng.normal(75, 12), 35, 95))
            activity_level = float(np.clip((steps / 200) + (rng.normal(0, 1.2)), 0, 10))
            calories = float(steps * 0.045 + rng.normal(30, 25))
            heart_rate = float(68 + 18 * (1 / (1 + np.exp(-((steps - 500) / 600)))) + rng.normal(0, 5))
            hrv = float(np.clip(52 - (patient['BMI'] * 0.35) + 8 * (sleep_quality / 100) + rng.normal(0, 7), 12, 90))
            glucose = baseline_glucose + np.sin(hour / 5.2 + day) * 12 + rng.normal(0, 7)
            if meal_carbs > 0:
                glucose += meal_carbs * 0.9
            if steps < 500:
                glucose += 6
            if sleep_duration < 6:
                glucose += 9
            if patient['HbA1c'] > 7.1:
                glucose += 5
            glucose = max(70, min(250, glucose))
            row = {
                'patient_id': patient_id,
                'timestamp': timestamp,
                'glucose': round(float(glucose), 2),
                'heart_rate': round(float(heart_rate), 2),
                'hrv': round(float(hrv), 2),
                'steps': int(max(0, steps)),
                'sleep_duration': round(float(sleep_duration), 2),
                'sleep_quality': round(float(sleep_quality), 2),
                'activity_level': round(float(activity_level), 2),
                'calories': round(float(calories), 2),
                'meal_carbs': round(float(meal_carbs), 2),
            }
            rows.append(row)
    return pd.DataFrame(rows)


def generate_labs(patients: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, patient in patients.iterrows():
        for month in range(1, 7):
            rows.append({
                'patient_id': patient['patient_id'],
                'date': pd.Timestamp('2024-01-01') + pd.Timedelta(days=month * 30),
                'HbA1c': round(float(patient['HbA1c']) + np.random.default_rng(42 + month).normal(0, 0.2), 2),
                'fasting_glucose': round(float(patient['fasting_glucose']) + np.random.default_rng(10 + month).normal(0, 4), 1),
            })
    return pd.DataFrame(rows)


def main() -> None:
    patients = generate_patients(100, seed=42)
    wearable = generate_wearable_data(patients, days=30, seed=42)
    labs = generate_labs(patients)
    patients.to_csv(RAW_DIR / 'patients.csv', index=False)
    wearable.to_csv(RAW_DIR / 'wearable_data.csv', index=False)
    labs.to_csv(RAW_DIR / 'labs.csv', index=False)
    print(f'Created {len(patients)} patients and {len(wearable)} wearable records')


if __name__ == '__main__':
    main()
