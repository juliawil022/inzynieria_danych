
import argparse

from pipeline.fetch_pse import fetch_pse
from pipeline.fetch_weather import fetch_weather
from pipeline.transform import transform_weather
from pipeline.quality import validate_weather


def main():
    parser = argparse.ArgumentParser(
        description="Pobieranie danych PSE i Open-Meteo."
    )

    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)

    args = parser.parse_args()

    pse_path = fetch_pse(args.start, args.end)
    weather_path = fetch_weather(args.start, args.end)

    clean_weather_path = transform_weather(weather_path)
    validate_weather(clean_weather_path)

if __name__ == "__main__":
    main()
