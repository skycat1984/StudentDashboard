# Studien-Dashboard

Ein prototypisches Studien-Dashboard zur übersichtlichen Darstellung des persönlichen Studienfortschritts.

Das Projekt wurde im Rahmen des Kurses **„Objektorientierte und funktionale Programmierung mit Python“** entwickelt. Der Schwerpunkt liegt auf der objektorientierten Modellierung, der Trennung der Verantwortlichkeiten und der Umsetzung einer übersichtlichen Schichtenarchitektur.

## Funktionen

Das Dashboard stellt folgende Informationen dar:

* erreichte und gesamte ECTS
* ECTS-Fortschritt in Prozent
* bisherigen Zeitfortschritt
* aktuellen Notendurchschnitt
* Anzahl bestandener Module
* Anzahl offener Module
* aktuell belegte Module
* prognostiziertes Abschlussdatum
* aktuellen Studienstatus

## Technische Grundlagen

* Python 3.13
* Tkinter für die grafische Benutzeroberfläche
* SQLite für die lokale Datenspeicherung
* ausschließlich Bestandteile der Python-Standardbibliothek
* keine zusätzlichen Python-Pakete erforderlich

## Architektur

Die Anwendung verwendet ein Schichtenmodell mit klar getrennten Verantwortlichkeiten:

* `domain`: fachliche Klassen und Enumerationen
* `repositories`: Datenbankzugriff und Erzeugung der Domain-Objekte
* `services`: fachliche Berechnungen
* `controller`: Koordination von Repositories und Services
* `dto`: Übergabe der aufbereiteten Dashboard-Daten
* `views`: grafische Darstellung mit Tkinter
* `application`: Erzeugung und Verdrahtung der Anwendungskomponenten

Die Klasse `DashboardApp` bildet den Composition Root der Anwendung. Sie erzeugt die benötigten Repositories, Services, den Controller und die View und verbindet die einzelnen Bestandteile miteinander.

## Projektstruktur

```text
StudentDashboard/
├── init_database.py
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── main.py
│   ├── application/
│   ├── controller/
│   ├── domain/
│   ├── dto/
│   ├── repositories/
│   ├── services/
│   └── views/
└── test/
    ├── phase1/
    ├── phase2/
    └── README_TESTPGMS.md
```

Die Datei `dashboard.db` wird durch das Initialisierungsskript erzeugt und ist nicht Bestandteil des Repositorys.

## Voraussetzungen

Für die Ausführung des Studien-Dashboards werden benötigt:

* ein aktuelles Windows-Betriebssystem
* Python 3.13
* Internetzugang zum Herunterladen des Projekts

Nach dem Herunterladen benötigt die Anwendung keine Internetverbindung.

## Installation und Start

### 1. Projekt herunterladen

Das Projekt kann über GitHub als ZIP-Datei heruntergeladen oder mit Git geklont werden:

```powershell
git clone https://github.com/skycat1984/StudentDashboard.git
```

Beim Klonen des Repositorys anschließend in das Projektverzeichnis wechseln:

```powershell
cd StudentDashboard
```

Beim Herunterladen als ZIP-Datei muss die Datei zunächst entpackt werden.

PowerShell oder die Windows-Eingabeaufforderung ist anschließend im Hauptverzeichnis des Projekts zu öffnen. Dabei handelt es sich um den Ordner, in dem sich die Datei `init_database.py` befindet.

### 2. Datenbank initialisieren

Die SQLite-Datenbank mit den benötigten Tabellen und Beispieldaten wird mit folgendem Befehl erstellt:

```powershell
py -3.13 init_database.py
```

Falls der Windows-Python-Launcher `py` nicht verfügbar ist, kann alternativ folgender Befehl verwendet werden:

```powershell
python init_database.py
```

Bei Verwendung des Befehls `python` muss sichergestellt sein, dass damit Python 3.13 ausgeführt wird.

Nach erfolgreicher Ausführung befindet sich die Datei `dashboard.db` im Hauptverzeichnis des Projekts.

### 3. Anwendung starten

Das Dashboard wird aus dem Hauptverzeichnis des Projekts mit folgendem Befehl gestartet:

```powershell
py -3.13 -m src.main
```

Falls der Windows-Python-Launcher `py` nicht verfügbar ist, kann alternativ folgender Befehl verwendet werden:

```powershell
python -m src.main
```

Nach dem Start öffnet sich die grafische Benutzeroberfläche des Studien-Dashboards.

## Bedienung

Der Prototyp ist als reine Anzeigeanwendung umgesetzt. Die dargestellten Daten werden aus der lokal erzeugten SQLite-Datenbank geladen.

Es sind keine Eingaben durch die Benutzerin oder den Benutzer erforderlich. Das Programm wird durch Schließen des Dashboard-Fensters beendet.

## Testprogramme

Im Verzeichnis `test` befinden sich die im Projektverlauf erstellten Testprogramme.

Die Testprogramme aus Phase 1 dienten der Überprüfung grundlegender Python-Konzepte und technischer Umsetzungsmöglichkeiten. Die Testprogramme aus Phase 2 überprüfen ausgewählte Bestandteile der objektorientierten Architektur und der fachlichen Logik.

Weitere Hinweise zur Ausführung befinden sich in der Datei:

```text
test/README_TESTPGMS.md
```

## Hinweise

* Vor dem ersten Start muss `init_database.py` ausgeführt werden.
* Eine bereits vorhandene Datei `dashboard.db` wird bei der erneuten Initialisierung ersetzt.
* Die Datenbankdatei wird ausschließlich lokal gespeichert.
* Die Anwendung verwendet keine externen Webdienste.
* Es müssen keine zusätzlichen Python-Pakete installiert werden.
* Die Anwendung muss aus dem Hauptverzeichnis mit `-m src.main` gestartet werden.

## Projektstatus

Der aktuelle Stand ist ein funktionsfähiger Prototyp zur Demonstration der objektorientierten Modellierung, einer klaren Schichtenarchitektur und der technischen Umsetzbarkeit des Studien-Dashboards.
