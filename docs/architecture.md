# Architektura

```text
PSE public API ───────┐
                      ├─> RAW JSON ─> CLEAN CSV ─┐
Open-Meteo Archive ───┘                          ├─> SERVING CSV ─> Django
                                                ┘
```

RAW zachowuje odpowiedzi źródłowe. CLEAN normalizuje kolumny i typy. SERVING łączy dane po wspólnym znaczniku czasu. Testy jakości blokują publikację wyniku przy krytycznych błędach.
