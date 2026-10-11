
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


def fetch_weather(start: str, end: str) -> Path:
    """Pobiera godzinowe dane pogodowe z Open-Meteo i zapisuje RAW JSON."""

    url = os.getenv(
        "OPEN_METEO_ARCHIVE_URL",
        "https://archive-api.open-meteo.com/v1/archive",
    )

    params = {
        "latitude": float(os.getenv("WEATHER_LATITUDE", "52.2297")),
        "longitude": float(os.getenv("WEATHER_LONGITUDE", "21.0122")),
        "start_date": start,
        "end_date": end,
        "hourly": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "wind_speed_10m"
        ),
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "precipitation_unit": "mm",
        "timezone": os.getenv(
            "WEATHER_TIMEZONE", "Europe/Warsaw"
        ),
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    payload = response.json()

    if payload.get("error"):
        raise RuntimeError(
            f"Błąd Open-Meteo: {payload.get('reason')}"
        )

    output_dir = ROOT / "data" / "raw" / "weather"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"weather_{start}_{end}.json"
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Zapisano pogodę: {output_path}")
    return output_path
