# Studien-Dashboard

Ein prototypisches Studien-Dashboard zur übersichtlichen Darstellung des persönlichen Studienfortschritts.

Das Projekt wurde im Rahmen des Kurses „Objektorientierte und funktionale Programmierung mit Python“ entwickelt. Der Schwerpunkt liegt auf der objektorientierten Modellierung und einer klaren Trennung der Verantwortlichkeiten innerhalb der Anwendung.

## Funktionen

Das Dashboard zeigt unter anderem:

* erreichte und gesamte ECTS
* ECTS-Fortschritt in Prozent
* bisherigen Zeitfortschritt
* aktuellen Notendurchschnitt
* Anzahl bestandener Module
* Anzahl offener Module
* aktuell gebuchte Kurse
* prognostiziertes Abschlussdatum
* aktuellen Studienstatus

## Technische Grundlagen

* Python 3.12.x
* getestet mit Python 3.12.10
* Tkinter für die grafische Benutzeroberfläche
* SQLite für die lokale Datenspeicherung
* ausschließlich Python-Standardbibliothek
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

Die Klasse `DashboardApp` bildet den Composition Root der Anwendung.

## Projektstruktur

```text
StudentDashboard/
├── init_database.py
├── README.md
├── .gitignore
└── src/
    ├── main.py
    ├── application/
    ├── controller/
    ├── domain/
    ├── dto/
    ├── repositories/
    ├── services/
    └── views/
```

Die Datei `dashboard.db` wird durch das Initialisierungsskript erzeugt und ist nicht Bestandteil des Repositorys.

## Installation

### 1. Repository herunterladen

Das Projekt kann über GitHub als ZIP-Datei heruntergeladen oder mit Git geklont werden:

```powershell
git clone https://github.com/skycat1984/StudentDashboard.git
```

Anschließend in das Projektverzeichnis wechseln:

```powershell
cd StudentDashboard
```

### 2. Datenbank initialisieren

Im Hauptverzeichnis des Projekts folgenden Befehl ausführen:

```powershell
python init_database.py
```

Falls `python` unter Windows nicht erkannt wird:

```powershell
py -3.12 init_database.py
```

Das Skript erstellt die SQLite-Datenbank `dashboard.db` mit den benötigten Tabellen und Beispieldaten.

### 3. Anwendung starten

Das Dashboard wird aus dem Hauptverzeichnis gestartet:

```powershell
python -m src.main
```

Alternativ:

```powershell
py -3.12 -m src.main
```

Nach dem Start öffnet sich die grafische Benutzeroberfläche.

## Bedienung

Der Prototyp ist als reine Anzeigeanwendung umgesetzt. Die dargestellten Daten werden aus der lokal erzeugten SQLite-Datenbank geladen. Das Programm wird durch Schließen des Dashboard-Fensters beendet.

## Hinweise

* Die Anwendung wurde für ein aktuelles Windows-Betriebssystem entwickelt und getestet.
* Vor dem ersten Start muss `init_database.py` ausgeführt werden.
* Die Datenbankdatei `dashboard.db` wird lokal erzeugt.
* Die Anwendung verwendet keine externen Webdienste und benötigt nach dem Herunterladen keine Internetverbindung.

## Projektstatus

Der aktuelle Stand ist ein funktionsfähiger Prototyp zur Demonstration der objektorientierten Modellierung, des Schichtenmodells und der technischen Umsetzbarkeit des Studien-Dashboards.
::: 
