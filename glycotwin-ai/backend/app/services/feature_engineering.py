from __future__ import annotations

import numpy as np
import pandas as pd

from app.utils.data_loader import load_patients, load_wearable_data


FEATURE_COLUMNS = [
    'age', 'BMI', 'HbA1c', 'fasting_glucose', 'cholesterol', 'systolic_bp', 'diastolic_bp',
    'diabetes_duration', 'current_glucose', 'glucose_rolling_mean', 'glucose_rolling_std',
    'glucose_slope', 'heart_rate', 'hrv', 'steps_last_1h', 'steps_last_6h', 'steps_last_24h',
    'sleep_duration', 'sleep_quality', 'activity_level', 'meal_carbs', 'hour', 'day_of_week',
    'is_night', 'is_meal_window', 'glucose_lag_1', 'glucose_lag_2', 'glucose_lag_3',
    'glucose_lag_6', 'glucose_lag_12', 'glucose_mean_3h', 'glucose_mean_6h', 'glucose_mean_12h',
    'glucose_std_6h', 'hr_mean_3h', 'steps_sum_6h'
]


def compute_patient_features(patient_id: str) -> dict:
    patients = load_patients().set_index('patient_id')
    wearable = load_wearable_data().copy()
    patient = patients.loc[patient_id]
    wearable = wearable[wearable['patient_id'] == patient_id].sort_values('timestamp').copy()
    if wearable.empty:
        raise ValueError(f'No wearable data for patient {patient_id}')

    wearable['timestamp'] = pd.to_datetime(wearable['timestamp'])
    wearable['hour'] = wearable['timestamp'].dt.hour
    wearable['day_of_week'] = wearable['timestamp'].dt.dayofweek
    wearable['is_night'] = wearable['hour'].isin([0, 1, 2, 3, 4, 5, 21, 22, 23]).astype(int)
    wearable['is_meal_window'] = wearable['hour'].isin([7, 8, 12, 13, 18, 19, 20]).astype(int)

    for lag in [1, 2, 3, 6, 12]:
        wearable[f'glucose_lag_{lag}'] = wearable['glucose'].shift(lag)

    for win in [3, 6, 12]:
        wearable[f'glucose_mean_{win}h'] = wearable['glucose'].rolling(window=win, min_periods=1).mean()

    wearable['glucose_rolling_mean'] = wearable['glucose'].rolling(window=6, min_periods=1).mean()
    wearable['glucose_rolling_std'] = wearable['glucose'].rolling(window=6, min_periods=1).std().fillna(0)
    wearable['glucose_slope'] = wearable['glucose'].diff().fillna(0)
    wearable['steps_last_1h'] = wearable['steps'].shift(1).rolling(window=1, min_periods=1).sum()
    wearable['steps_last_6h'] = wearable['steps'].shift(1).rolling(window=6, min_periods=1).sum()
    wearable['steps_last_24h'] = wearable['steps'].shift(1).rolling(window=24, min_periods=1).sum()
    wearable['hr_mean_3h'] = wearable['heart_rate'].rolling(window=3, min_periods=1).mean()
    wearable['steps_sum_6h'] = wearable['steps'].rolling(window=6, min_periods=1).sum()

    latest = wearable.iloc[-1].to_dict()
    features = {
        'patient_id': patient_id,
        'age': int(patient['age']),
        'BMI': float(patient['BMI']),
        'HbA1c': float(patient['HbA1c']),
        'fasting_glucose': float(patient['fasting_glucose']),
        'cholesterol': float(patient['cholesterol']),
        'systolic_bp': int(patient['systolic_bp']),
        'diastolic_bp': int(patient['diastolic_bp']),
        'diabetes_duration': int(patient['diabetes_duration']),
        'current_glucose': float(latest['glucose']),
        'glucose_rolling_mean': float(latest['glucose_rolling_mean']),
        'glucose_rolling_std': float(latest['glucose_rolling_std']),
        'glucose_slope': float(latest['glucose_slope']),
        'heart_rate': float(latest['heart_rate']),
        'hrv': float(latest['hrv']),
        'steps_last_1h': float(latest['steps_last_1h']),
        'steps_last_6h': float(latest['steps_last_6h']),
        'steps_last_24h': float(latest['steps_last_24h']),
        'sleep_duration': float(latest['sleep_duration']),
        'sleep_quality': float(latest['sleep_quality']),
        'activity_level': float(latest['activity_level']),
        'meal_carbs': float(latest['meal_carbs']),
        'hour': int(latest['hour']),
        'day_of_week': int(latest['day_of_week']),
        'is_night': int(latest['is_night']),
        'is_meal_window': int(latest['is_meal_window']),
        'glucose_lag_1': float(latest['glucose_lag_1']) if pd.notna(latest['glucose_lag_1']) else float(latest['glucose']),
        'glucose_lag_2': float(latest['glucose_lag_2']) if pd.notna(latest['glucose_lag_2']) else float(latest['glucose']),
        'glucose_lag_3': float(latest['glucose_lag_3']) if pd.notna(latest['glucose_lag_3']) else float(latest['glucose']),
        'glucose_lag_6': float(latest['glucose_lag_6']) if pd.notna(latest['glucose_lag_6']) else float(latest['glucose']),
        'glucose_lag_12': float(latest['glucose_lag_12']) if pd.notna(latest['glucose_lag_12']) else float(latest['glucose']),
        'glucose_mean_3h': float(latest['glucose_mean_3h']),
        'glucose_mean_6h': float(latest['glucose_mean_6h']),
        'glucose_mean_12h': float(latest['glucose_mean_12h']),
        'glucose_std_6h': float(latest['glucose_rolling_std']),
        'hr_mean_3h': float(latest['hr_mean_3h']),
        'steps_sum_6h': float(latest['steps_sum_6h']),
    }
    return features


def build_training_dataset(max_rows_per_patient: int = 40) -> pd.DataFrame:
    patients = load_patients()
    wearable = load_wearable_data()
    wearable = wearable.sort_values(['patient_id', 'timestamp']).copy()
    rows = []
    for patient_id in patients['patient_id'].tolist():
        patient = patients[patients['patient_id'] == patient_id].iloc[0]
        patient_wearable = wearable[wearable['patient_id'] == patient_id].copy()
        patient_wearable['hour'] = pd.to_datetime(patient_wearable['timestamp']).dt.hour
        patient_wearable['day_of_week'] = pd.to_datetime(patient_wearable['timestamp']).dt.dayofweek
        patient_wearable['is_night'] = patient_wearable['hour'].isin([0, 1, 2, 3, 4, 5, 21, 22, 23]).astype(int)
        patient_wearable['is_meal_window'] = patient_wearable['hour'].isin([7, 8, 12, 13, 18, 19, 20]).astype(int)
        for lag in [1, 2, 3, 6, 12]:
            patient_wearable[f'glucose_lag_{lag}'] = patient_wearable['glucose'].shift(lag)
        patient_wearable['glucose_rolling_mean'] = patient_wearable['glucose'].rolling(window=6, min_periods=1).mean()
        patient_wearable['glucose_rolling_std'] = patient_wearable['glucose'].rolling(window=6, min_periods=1).std().fillna(0)
        patient_wearable['glucose_slope'] = patient_wearable['glucose'].diff().fillna(0)
        patient_wearable['steps_last_1h'] = patient_wearable['steps'].shift(1).rolling(window=1, min_periods=1).sum()
        patient_wearable['steps_last_6h'] = patient_wearable['steps'].shift(1).rolling(window=6, min_periods=1).sum()
        patient_wearable['steps_last_24h'] = patient_wearable['steps'].shift(1).rolling(window=24, min_periods=1).sum()
        patient_wearable['hr_mean_3h'] = patient_wearable['heart_rate'].rolling(window=3, min_periods=1).mean()
        patient_wearable['steps_sum_6h'] = patient_wearable['steps'].rolling(window=6, min_periods=1).sum()
        patient_wearable['glucose_mean_3h'] = patient_wearable['glucose'].rolling(window=3, min_periods=1).mean()
        patient_wearable['glucose_mean_6h'] = patient_wearable['glucose'].rolling(window=6, min_periods=1).mean()
        patient_wearable['glucose_mean_12h'] = patient_wearable['glucose'].rolling(window=12, min_periods=1).mean()
        patient_wearable['glucose_std_6h'] = patient_wearable['glucose'].rolling(window=6, min_periods=1).std().fillna(0)

        sample_size = min(max_rows_per_patient, len(patient_wearable) - 3)
        if sample_size <= 0:
            continue
        indices = np.linspace(2, len(patient_wearable) - 3, num=sample_size, dtype=int)
        for idx in sorted(set(indices.tolist())):
            current = patient_wearable.iloc[idx]
            target = patient_wearable.iloc[min(idx + 2, len(patient_wearable) - 1)]
            row = {
                'patient_id': patient_id,
                'age': patient['age'],
                'BMI': patient['BMI'],
                'HbA1c': patient['HbA1c'],
                'fasting_glucose': patient['fasting_glucose'],
                'cholesterol': patient['cholesterol'],
                'systolic_bp': patient['systolic_bp'],
                'diastolic_bp': patient['diastolic_bp'],
                'diabetes_duration': patient['diabetes_duration'],
                'current_glucose': float(current['glucose']),
                'glucose_rolling_mean': float(current['glucose_rolling_mean']),
                'glucose_rolling_std': float(current['glucose_rolling_std']),
                'glucose_slope': float(current['glucose_slope']),
                'heart_rate': float(current['heart_rate']),
                'hrv': float(current['hrv']),
                'steps_last_1h': float(current['steps_last_1h']),
                'steps_last_6h': float(current['steps_last_6h']),
                'steps_last_24h': float(current['steps_last_24h']),
                'sleep_duration': float(current['sleep_duration']),
                'sleep_quality': float(current['sleep_quality']),
                'activity_level': float(current['activity_level']),
                'meal_carbs': float(current['meal_carbs']),
                'hour': int(current['hour']),
                'day_of_week': int(current['day_of_week']),
                'is_night': int(current['is_night']),
                'is_meal_window': int(current['is_meal_window']),
                'glucose_lag_1': float(current['glucose_lag_1']) if pd.notna(current['glucose_lag_1']) else float(current['glucose']),
                'glucose_lag_2': float(current['glucose_lag_2']) if pd.notna(current['glucose_lag_2']) else float(current['glucose']),
                'glucose_lag_3': float(current['glucose_lag_3']) if pd.notna(current['glucose_lag_3']) else float(current['glucose']),
                'glucose_lag_6': float(current['glucose_lag_6']) if pd.notna(current['glucose_lag_6']) else float(current['glucose']),
                'glucose_lag_12': float(current['glucose_lag_12']) if pd.notna(current['glucose_lag_12']) else float(current['glucose']),
                'glucose_mean_3h': float(current['glucose_mean_3h']),
                'glucose_mean_6h': float(current['glucose_mean_6h']),
                'glucose_mean_12h': float(current['glucose_mean_12h']),
                'glucose_std_6h': float(current['glucose_std_6h']),
                'hr_mean_3h': float(current['hr_mean_3h']),
                'steps_sum_6h': float(current['steps_sum_6h']),
                'future_glucose': float(target['glucose']),
                'spike_flag': int(float(target['glucose']) >= 180),
            }
            rows.append(row)
    return pd.DataFrame(rows)


def recent_timeline(patient_id: str) -> pd.DataFrame:
    wearable = load_wearable_data()
    patient_series = wearable[wearable['patient_id'] == patient_id].sort_values('timestamp').tail(24).copy()
    patient_series['timestamp'] = pd.to_datetime(patient_series['timestamp'])
    return patient_series
