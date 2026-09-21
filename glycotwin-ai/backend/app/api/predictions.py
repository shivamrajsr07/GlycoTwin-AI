from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.services.explainability import explain_risk
from app.services.prediction import predict_glucose
from app.utils.data_loader import load_patients

router = APIRouter()


@router.get('/api/patients/{patient_id}/prediction')
def patient_prediction(patient_id: str) -> dict:
    patients = load_patients()
    if patients[patients['patient_id'] == patient_id].empty:
        raise HTTPException(status_code=404, detail='Patient not found')
    return predict_glucose(patient_id)


@router.get('/api/patients/{patient_id}/explanation')
def patient_explanation(patient_id: str) -> list[dict]:
    patients = load_patients()
    if patients[patients['patient_id'] == patient_id].empty:
        raise HTTPException(status_code=404, detail='Patient not found')
    return explain_risk(patient_id)
