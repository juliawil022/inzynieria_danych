# Słownik danych

## `pse_load.csv`
- `timestamp`: data i godzina obserwacji z PSE.
- `actual_mw`: rzeczywiste zapotrzebowanie na moc, MW.
- `planned_mw`: planowane zapotrzebowanie na moc, MW.

## `weather.csv`
- `timestamp`: lokalny znacznik czasu z Open-Meteo.
- `temperature_c`: temperatura na wysokości 2 m, °C.
- `relative_humidity_pct`: wilgotność względna, %.
- `precipitation_mm`: suma opadu dla poprzedzającej godziny, mm.
- `wind_speed_kmh`: prędkość wiatru, km/h.

## `energy_weather_hourly.csv`
Zawiera kolumny CLEAN oraz:
- `forecast_error_mw`: `actual_mw - planned_mw`.
- `temperature_group`: uproszczona kategoria temperatury: chłodno, umiarkowanie, ciepło.
