# Studien-Dashboard

Dieses Repository enthält die Ergebnisse der ersten beiden Phasen des Portfolios „Objektorientierte und funktionale Programmierung mit Python“.

## Voraussetzungen

Für die Ausführung wird benötigt:

* Python 3.13
* Visual Studio Code oder eine andere Entwicklungsumgebung
* Git optional zum Klonen des Repositorys

Tkinter und SQLite müssen nicht zusätzlich installiert werden, da beide standardmäßig mit Python verfügbar sind.

## Installation

Repository klonen:

```bash
git clone <REPOSITORY-LINK>
```

In den Projektordner wechseln:

```bash
cd <PROJEKTORDNER>
```

Python-Version prüfen:

```bash
python --version
```

## Phase 1 – Machbarkeitsüberprüfung

Die Programme der ersten Phase dienen der Untersuchung technischer Grundlagen für den späteren Dashboard-Prototypen.

### Testprogramm 1: Tkinter

Datei:

```text
tkinter_test.py
```

Ziel:

* Untersuchung der Umsetzbarkeit einer grafischen Benutzeroberfläche mit Tkinter.

Ausführen:

```bash
python tkinter_test.py
```

Erwartetes Ergebnis:

* Ein Fenster mit dem Titel „Tkinter Test“ wird geöffnet.
* Ein Button wird angezeigt.
* Nach dem Anklicken erscheint eine Meldung.

### Testprogramm 2: SQLite

Datei:

```text
sqlite_test.py
```

Ziel:

* Untersuchung der lokalen Datenspeicherung mit SQLite.

Ausführen:

```bash
python sqlite_test.py
```

Erwartetes Ergebnis:

* Eine SQLite-Datenbankdatei wird erzeugt.
* Eine Tabelle wird angelegt.
* Ein Testdatensatz wird gespeichert.
* Die gespeicherten Daten werden ausgelesen und ausgegeben.

## Phase 2 – Untersuchung objektorientierter Konzepte

Die Programme der zweiten Phase untersuchen die Umsetzung objektorientierter Konzepte in Python und dienen als Grundlage für die spätere Gesamtarchitektur des Dashboard-Prototyps.

### Testprogramm 1: Dataclasses

Datei:

```text
test_dataclasses.py
```

Ziel:

* Untersuchung der Umsetzung von Domain-Klassen mit Python-Dataclasses.

Untersuchte Konzepte:

* Klassen und Objekte
* Dataclasses
* automatische Erzeugung von Standardmethoden

### Testprogramm 2: Enumerationen

Datei:

```text
test_enums.py
```

Ziel:

* Untersuchung der Umsetzung von Enumerationen mit Python.

Untersuchte Konzepte:

* Enum-Klassen
* feste Wertebereiche
* Vermeidung ungültiger Zustände

### Testprogramm 3: Beziehungen

Datei:

```text
test_beziehungen.py
```

Ziel:

* Untersuchung der Umsetzung von Beziehungen zwischen Klassen.

Untersuchte Konzepte:

* Aggregation
* Komposition
* Objektreferenzen
* Listen als Umsetzung von 1:n-Beziehungen

### Testprogramm 4: Service-Klassen

Datei:

```text
test_services.py
```

Ziel:

* Untersuchung der Trennung von Datenhaltung und Berechnungslogik.

Untersuchte Konzepte:

* Service-Klassen
* Berechnung von Kennzahlen
* Trennung von Domain- und Logikschicht

## Zweck des Repositorys

Die enthaltenen Testprogramme zeigen die technische und objektorientierte Umsetzbarkeit des geplanten Studien-Dashboard-Prototyps.

Untersucht wurden:

* grafische Benutzeroberflächen mit Tkinter
* lokale Datenspeicherung mit SQLite
* Domain-Klassen mit Dataclasses
* Enumerationen mit Python-Enums
* Beziehungen zwischen Klassen
* Service-Klassen zur Kapselung von Berechnungen
* Ausführung mit Python 3.13
* Versionsverwaltung mit Git und GitHub
