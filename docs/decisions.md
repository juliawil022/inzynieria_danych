# Rejestr decyzji projektowych

## D-001 — Python i Django
- Wybór: Python dla potoku, Django dla aplikacji.
- Alternatywy: Streamlit, Dash.
- Uzasadnienie: zespół już rozpoczął projekt Django i chce zbudować klasyczną aplikację webową.

## D-002 — Pliki JSON i CSV dla warstw
- Wybór: RAW jako JSON, CLEAN/SERVING jako CSV.
- Alternatywy: jedna baza dla wszystkich warstw, Parquet, DuckDB.
- Uzasadnienie: formaty są czytelne, proste do inspekcji i wystarczające dla prototypu. W przyszłości można przejść na Parquet lub bazę analityczną.

## D-003 — Jedna lokalizacja pogodowa w prototypie
- Wybór: współrzędne konfigurowalne, domyślnie okolice Warszawy.
- Alternatywy: średnia z wielu lokalizacji lub dane regionalne.
- Uzasadnienie: ogranicza zakres pierwszego przyrostu. Wyniki należy interpretować jako przybliżenie, nie reprezentację całej Polski.
