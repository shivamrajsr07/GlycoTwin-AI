from __future__ import annotations

from pathlib import Path
from functools import lru_cache

import pandas as pd

from app.core.config import RAW_DATA_DIR


@lru_cache(maxsize=1)
def load_patients() -> pd.DataFrame:
    path = RAW_DATA_DIR / 'patients.csv'
    if not path.exists():
        raise FileNotFoundError(f'Missing patient data at {path}')
    return pd.read_csv(path)


@lru_cache(maxsize=1)
def load_wearable_data() -> pd.DataFrame:
    path = RAW_DATA_DIR / 'wearable_data.csv'
    if not path.exists():
        raise FileNotFoundError(f'Missing wearable data at {path}')
    return pd.read_csv(path)


@lru_cache(maxsize=1)
def load_labs() -> pd.DataFrame:
    path = RAW_DATA_DIR / 'labs.csv'
    if not path.exists():
        raise FileNotFoundError(f'Missing lab data at {path}')
    return pd.read_csv(path)


def patient_ids() -> list[str]:
    return load_patients()['patient_id'].tolist()
