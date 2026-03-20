# CSV Analyzer

Ein einfaches Python-Tool zur Berechnung von statistischen Kennzahlen aus CSV-Daten.

---

## Features

* Durchschnitt berechnen (`average`)
* Median berechnen (`median`)
* Minimum berechnen (`min`)
* Maximum berechnen (`max`)
* Anzahl der Werte zählen (`count`)
* Summe berechnen (`sum`)
* Modus (häufigster Wert) berechnen (`mode`)
* Varianz berechnen (`variance`)
* Standardabweichung berechnen (`std_dev`)
* CSV-Dateien laden (`load_csv`)

---

## Installation

Repository klonen:

```bash
git clone https://github.com/lenn07/csv_analyzer.git
cd csv_analyzer
```

(Optional) virtuelle Umgebung erstellen:

```bash
python -m venv venv
venv\Scripts\activate
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

(Optional) Projekt im Entwicklungsmodus installieren:

```bash
pip install -e .
```

---

## Nutzung

Die öffentliche API besteht aus:

* `load_csv`
* `average`
* `median`
* `min`
* `max`
* `count`
* `sum`
* `mode`
* `variance`
* `std_dev`

### Beispiel

```python
from csv_analyzer import load_csv, average, median, min, max, count, sum, mode, variance, std_dev

# CSV laden
table = load_csv("data.csv")

# Statistiken berechnen (Spalte 0)
print("Average:", average(table, 0))
print("Median:", median(table, 0))
print("Min:", min(table, 0))
print("Max:", max(table, 0))
print("Count:", count(table, 0))
print("Sum:", sum(table, 0))
print("Mode:", mode(table, 0))
print("Variance:", variance(table, 0))
print("Std Dev:", std_dev(table, 0))
```

### CLI-Nutzung

Das Paket kann auch als Kommandozeilen-Tool verwendet werden:

```bash
python -m csv_analyzer
```

---

## Verhalten / Edge Cases

* Es werden keine Errors geworfen sondern lediglich eine Errormeldung in Form eines Strings.
* Die erste Zeile der Tabelle wird als Header behandelt.
* Spalten werden über Index angesprochen (0-basiert).

## Tests

Tests werden mit `pytest` ausgeführt:

```bash
python -m pytest -v
```

---

## Projektstruktur

```text
csv_analyzer/
│
├── __init__.py
├── __main__.py      # CLI
├── loader.py        # CSV-Loading-Funktionen
├── stats.py         # Statistische Berechnungen
├── transform.py     # Daten-Transformationen
└── validation.py    # Validierungsfunktionen
tests/
├── test_stats.py
data/
└── student_performance_prediction_dataset-2.csv
```

---

## Hinweis

Die Funktionen in `loader.py`, `transform.py` und `validation.py` sind interne Implementierungsdetails und nicht Teil der öffentlichen API.

## Ziel des Projekts

Dieses Projekt dient als Übung für:

* sauberes Python-Design
* Strukturierung von Modulen
* Schreiben von Tests mit pytest
* Definition einer klaren API

---

## Lizenz

MIT License
