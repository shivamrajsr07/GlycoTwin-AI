from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter

from app.utils.data_loader import load_patients
from app.api.patients import _overview_risk

router = APIRouter()


@router.get('/api/dashboard/summary')
def dashboard_summary() -> dict:
    patients = load_patients()
    risk_scores = [_overview_risk(row.to_dict())[0] for _, row in patients.iterrows()]
    high_risk = sum(1 for score in risk_scores if score >= 75)
    return {
        'total_patients': len(patients),
        'high_risk_patients': high_risk,
        'average_risk': round(sum(risk_scores) / max(len(risk_scores), 1), 2),
        'data_timestamp': datetime.utcnow().isoformat() + 'Z',
        'patient_id': patients.iloc[0]['patient_id'],
    }
