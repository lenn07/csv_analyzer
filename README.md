# CSV Analyzer

Ein einfaches Python-Tool zur Berechnung von statistischen Kennzahlen.

---

## Features

* Durchschnitt berechnen (`average`)
* Median berechnen (`median`)

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

* `average`
* `median`

### Beispiel

```python
from csv_analyzer import average, median

numbers = [[1], [2], [3], [4]]

print(average(numbers), 0)  # 2.5
print(median(numbers), 0)   # 2.5
```

---

## Verhalten / Edge Cases

* Es werden keine Errors geworfen sondern lediglich eine Errormeldung in Form eines Strings.

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
├── stats.py
├── loader.py        # interne Hilfsfunktionen
├── transform.py     # interne Hilfsfunktionen
└── validation.py    # interne Hilfsfunktionen
tests/
├── test_stats.py
└── test_loader.py
```

---

## Hinweis

Die Funktionen in `loader.py`, `transform.py` und `validation.py` sind interne Implementierungsdetails und nicht Teil der öffentlichen API.

---

## Ziel des Projekts

Dieses Projekt dient als Übung für:

* sauberes Python-Design
* Strukturierung von Modulen
* Schreiben von Tests mit pytest
* Definition einer klaren API

---

## Lizenz

MIT License
