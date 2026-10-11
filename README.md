## 1. Cel projektu

Projekt realizowany w ramach przedmiotu Inżynieria danych. Jego celem jest zbudowanie powtarzalnego potoku danych oraz aplikacji internetowej analizującej zależności między warunkami pogodowymi a krajowym zapotrzebowaniem na moc w Krajowym Systemie Elektroenergetycznym (KSE).

## 2. Problem i odbiorca

Odbiorcą rozwiązania jest analityk energetyczny zainteresowany monitorowaniem zapotrzebowania na moc oraz analizą jego zmian w różnych warunkach pogodowych.

Aplikacja ma wspierać analizę historyczną, porównywanie planowanego i rzeczywistego zapotrzebowania oraz wyszukiwanie zależności między temperaturą a obciążeniem systemu.

Wyniki mają charakter analityczny. Sama korelacja nie dowodzi, że pogoda jest bezpośrednią przyczyną zmian zapotrzebowania.

## 3. Pytania analityczne

1. Jak zmienia się rzeczywiste zapotrzebowanie na moc w czasie?
2. Jaki związek występuje między temperaturą a zapotrzebowaniem na moc?
3. Czy zapotrzebowanie różni się w okresach chłodnych, umiarkowanych i gorących?
4. Jakie są różnice między planowanym a rzeczywistym zapotrzebowaniem?

## 4. Źródła danych

- **PSE:** publiczne dane o planowanym i rzeczywistym zapotrzebowaniu na moc KSE, udostępniane przez portal raportowy PSE.
- **Open-Meteo:** godzinowe dane pogodowe, w tym temperatura, wilgotność, opady i prędkość wiatru.

Linki:
- https://raporty.pse.pl/
- https://www.pse.pl/mapa-raportow
- https://open-meteo.com/en/docs/historical-weather-api

Schemat odpowiedzi PSE, częstotliwość pomiarów i dostępne pola należy potwierdzić na podstawie aktualnej odpowiedzi API. Warunki korzystania ze źródeł oraz wymagania dotyczące atrybucji należy sprawdzić i opisać przed oddaniem projektu.

## 5. Architektura rozwiązania

Potok składa się z następujących etapów:

1. **Pozyskanie:** automatyczne pobieranie danych z API PSE i Open-Meteo.
2. **RAW:** zapis oryginalnych odpowiedzi JSON.
3. **CLEAN:** czyszczenie danych, ujednolicanie typów i znaczników czasu oraz usuwanie duplikatów.
4. **SERVING:** połączenie danych energetycznych i pogodowych we wspólnym modelu analitycznym.
5. **Aplikacja:** Django udostępniające przygotowane dane w postaci wykresów i filtrów.

Dane surowe są przechowywane oddzielnie od danych oczyszczonych i gotowych do analizy. Pozwala to ponawiać transformacje bez konieczności każdorazowego pobierania źródeł.

## 6. Perspektywa biznesowa

Rozwiązanie może ograniczyć czas potrzebny na ręczne przygotowywanie zestawień oraz ułatwić obserwację sezonowości i odchyleń prognoz od rzeczywistych wartości. Potencjalną wartość można mierzyć czasem przygotowania analizy, kompletnością danych i możliwością jej powtarzalnego odtworzenia.

Prototyp wykorzystuje bezpłatne biblioteki i publiczne interfejsy danych. Główne koszty utrzymania to czas pracy, lokalne zasoby obliczeniowe oraz ewentualne zmiany w API.

## 7. Perspektywa dziedzinowa

Zapotrzebowanie na moc jest wyrażane w MW. Nie należy utożsamiać go z energią wyrażaną w MWh. Planowane i rzeczywiste wartości muszą być porównywane dla zgodnych przedziałów czasu.

Na zapotrzebowanie mogą wpływać również pora dnia, dzień tygodnia, sezon, święta i inne czynniki. Pogoda z jednej lokalizacji nie opisuje w pełni warunków w całej Polsce, dlatego lokalizacja pogodowa jest przybliżeniem.

## 8. Perspektywa techniczna

Python odpowiada za pobieranie, transformacje i testy danych. Django stanowi warstwę aplikacyjną, a SQLite może służyć do przechowywania danych aplikacji. Pliki JSON i CSV zapewniają prosty, czytelny podział warstw danych.

Dla stukrotnie większego wolumenu należałoby rozważyć PostgreSQL, Parquet, ładowanie przyrostowe, harmonogram zadań, monitoring i wydajniejsze przetwarzanie.

## 9. Perspektywa prawna i etyczna

Projekt nie wymaga danych osobowych. Należy przestrzegać warunków korzystania z API, podawać źródła i respektować ewentualne ograniczenia licencyjne.

Błędne dopasowanie czasu, niekompletne dane lub nadmierna interpretacja korelacji mogą prowadzić do mylnych wniosków. Autorzy odpowiadają za poprawność transformacji, testy, dokumentację i jawne przedstawienie ograniczeń.

## 10. Kontrola jakości

Planowane kontrole obejmują:
- kompletność znaczników czasu;
- unikalność rekordów;
- kompletność wymaganych wartości;
- poprawność typów liczbowych;
- kontrolę zakresów temperatury i zapotrzebowania;
- integralność po połączeniu źródeł;
- poprawność obliczenia różnicy między wartościami planowanymi i rzeczywistymi.

Błędy krytyczne powinny być widoczne w terminalu i blokować publikację niepoprawnego wyniku.

## 11. Ograniczenia i dalszy rozwój

Najważniejsze ograniczenia to zależność od aktualnego schematu API PSE, możliwe różnice częstotliwości i stref czasowych, przybliżony charakter reprezentacji pogody dla całego kraju oraz fakt, że korelacja nie oznacza przyczynowości.

Możliwe rozszerzenia obejmują agregację pogody z wielu lokalizacji, historię uruchomień potoku, eksport CSV, automatyczne odświeżanie i analizę sezonową.