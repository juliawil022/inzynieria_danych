
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


def fetch_pse(start: str, end: str) -> Path:
    """Pobiera dane PSE i zachowuje odpowiedź źródłową w RAW."""

    url = os.getenv(
        "PSE_API_URL",
        "https://api.raporty.pse.pl/api/kse-load",
    )

    response = requests.get(url, timeout=60)
    response.raise_for_status()
    payload = response.json()

    # Zachowujemy odpowiedź API bez zmian, zanim zaczniemy
    # dopasowywać nazwy pól i filtrować daty.
    output_dir = ROOT / "data" / "raw" / "pse"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"pse_{start}_{end}.json"
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Zapisano PSE: {output_path}")

    return output_path
