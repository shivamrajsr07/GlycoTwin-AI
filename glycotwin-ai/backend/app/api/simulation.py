from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.models.schemas import SimulationRequest
from app.services.simulation import simulate_scenario
from app.utils.data_loader import load_patients

router = APIRouter()


@router.post('/api/simulation')
def run_simulation(request: SimulationRequest) -> dict:
    patients = load_patients()
    if patients[patients['patient_id'] == request.patient_id].empty:
        raise HTTPException(status_code=404, detail='Patient not found')
    return simulate_scenario(
        request.patient_id,
        request.meal_carbs_change,
        request.additional_steps,
        request.sleep_change_hours,
    )
