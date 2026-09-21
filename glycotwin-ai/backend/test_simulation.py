from app.services.simulation import simulate_scenario


def test_simulation_returns_delta() -> None:
    simulation = simulate_scenario('PT-001', -30, 3000, 1)
    assert 'baseline' in simulation
    assert 'scenario' in simulation
    assert 'delta' in simulation
    assert 'glucose' in simulation['delta']
    assert 'risk' in simulation['delta']
