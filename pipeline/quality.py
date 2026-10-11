
from pathlib import Path

import pandas as pd


def validate_weather(path: Path) -> None:
    df = pd.read_csv(path)

    assert not df.empty, "Brak danych pogodowych."
    assert df["timestamp"].notna().all(), (
        "Brak znacznika czasu."
    )
    assert not df["timestamp"].duplicated().any(), (
        "Powielone znaczniki czasu."
    )
    assert df["temperature_c"].notna().all(), (
        "Brak temperatury."
    )
    assert df["temperature_c"].between(-90, 65).all(), (
        "Temperatura poza zakresem kontrolnym."
    )

    print("Testy jakości pogody zakończone poprawnie.")
