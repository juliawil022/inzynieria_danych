
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def transform_weather(raw_path: Path) -> Path:
    """Zamienia godzinowy JSON Open-Meteo na uporządkowany CSV."""

    payload = json.loads(raw_path.read_text(encoding="utf-8"))
    hourly = payload.get("hourly", {})

    if "time" not in hourly:
        raise ValueError(
            "Brak kolumny time w odpowiedzi Open-Meteo."
        )

    df = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_c": hourly.get("temperature_2m"),
        "relative_humidity_pct": hourly.get(
            "relative_humidity_2m"
        ),
        "precipitation_mm": hourly.get("precipitation"),
        "wind_speed_kmh": hourly.get("wind_speed_10m"),
    })

    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce"
    )

    df = df.dropna(subset=["timestamp"])
    df = df.drop_duplicates(subset=["timestamp"])
    df = df.sort_values("timestamp")

    output_dir = ROOT / "data" / "clean"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "weather.csv"
    df.to_csv(output_path, index=False)

    print(f"Zapisano oczyszczoną pogodę: {output_path}")
    print(f"Liczba rekordów: {len(df)}")

    return output_path
