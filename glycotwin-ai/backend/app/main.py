from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dashboard import router as dashboard_router
from app.api.health import router as health_router
from app.api.patients import router as patients_router
from app.api.predictions import router as predictions_router
from app.api.simulation import router as simulation_router
from app.core.config import API_TITLE, API_VERSION

app = FastAPI(title=API_TITLE, version=API_VERSION, description='GlycoTwin AI research prototype.')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(health_router)
app.include_router(patients_router)
app.include_router(predictions_router)
app.include_router(simulation_router)
app.include_router(dashboard_router)


@app.get('/')
def root() -> dict[str, str]:
    return {'message': 'GlycoTwin AI backend is running.'}
