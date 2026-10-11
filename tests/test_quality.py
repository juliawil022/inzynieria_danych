"""Proste testy funkcji kontroli jakości na danych testowych."""
import pandas as pd
import pytest

from pipeline.quality import validate_pse, validate_weather, validate_serving


def test_validate_pse_accepts_valid_data(tmp_path):
    path = tmp_path / "pse.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01 00:00:00"],
        "actual_mw": [18000],
        "planned_mw": [17500],
    }).to_csv(path, index=False)
    validate_pse(path)


def test_validate_pse_rejects_duplicate_timestamps(tmp_path):
    path = tmp_path / "pse.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01 00:00:00", "2025-01-01 00:00:00"],
        "actual_mw": [18000, 18100],
        "planned_mw": [17500, 17600],
    }).to_csv(path, index=False)
    with pytest.raises(AssertionError):
        validate_pse(path)


def test_validate_weather_rejects_out_of_range_temperature(tmp_path):
    path = tmp_path / "weather.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01 00:00:00"],
        "temperature_c": [100],
        "relative_humidity_pct": [50],
        "precipitation_mm": [0],
        "wind_speed_kmh": [10],
    }).to_csv(path, index=False)
    with pytest.raises(AssertionError):
        validate_weather(path)


def test_validate_serving_checks_forecast_error(tmp_path):
    path = tmp_path / "serving.csv"
    pd.DataFrame({
        "timestamp": ["2025-01-01 00:00:00"],
        "actual_mw": [18000],
        "planned_mw": [17500],
        "forecast_error_mw": [0],
    }).to_csv(path, index=False)
    with pytest.raises(AssertionError):
        validate_serving(path)
