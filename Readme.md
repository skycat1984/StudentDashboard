# Studien-Dashboard – Phase 1

Dieses Repository enthält zwei kleine Testprogramme zur Machbarkeitsüberprüfung für den späteren Studien-Dashboard-Prototypen.

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

## Testprogramm 1: Tkinter

Das Tkinter-Testprogramm prüft, ob eine einfache grafische Benutzeroberfläche erstellt werden kann.

Ausführen:

```bash
python tkinter_test.py
```

Erwartetes Ergebnis:

* Es öffnet sich ein Fenster mit dem Titel „Tkinter Test“.
* Ein Button „Tkinter testen“ wird angezeigt.
* Beim Klicken auf den Button erscheint eine Meldung.

## Testprogramm 2: SQLite

Das SQLite-Testprogramm prüft, ob Daten lokal gespeichert und wieder ausgelesen werden können.

Ausführen:

```bash
python sqlite_test.py
```

Erwartetes Ergebnis:

* Es wird eine SQLite-Datenbankdatei `dashboard.db` erstellt.
* Eine Tabelle `student` wird angelegt.
* Ein Testdatensatz wird gespeichert.
* Der gespeicherte Datensatz wird in der Konsole ausgegeben.

## Zweck der Testprogramme

Die Testprogramme zeigen, dass die geplanten technischen Grundlagen für den späteren Dashboard-Prototypen funktionieren:

* grafische Oberfläche mit Tkinter
* lokale Datenspeicherung mit SQLite
* Ausführung über Python 3.13
* Verwaltung des Codes über Git/GitHub
