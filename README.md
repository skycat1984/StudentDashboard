Installationsanleitung – Studien-Dashboard

1. Voraussetzungen

Für die Ausführung des Studien-Dashboards werden benötigt:

* aktuelles Windows-Betriebssystem
* Python [GETESTETE VERSION] oder höher
* Internetzugang zum Herunterladen des Quellcodes

Der Prototyp verwendet ausschließlich Bestandteile der Python-Standardbibliothek, insbesondere Tkinter für die grafische Benutzeroberfläche und SQLite für die Datenspeicherung. Zusätzliche Python-Pakete müssen daher nicht installiert werden.

Bei der Installation von Python sollte die Option „Add Python to PATH“ aktiviert werden.

2. Quellcode herunterladen

Der vollständige Quellcode befindet sich im folgenden GitHub-Repository:

[GITHUB-LINK]

Das Repository kann über „Code“ und „Download ZIP“ heruntergeladen werden. Anschließend ist die ZIP-Datei vollständig zu entpacken.

Alternativ kann das Repository mit Git geklont werden:

```powershell
git clone [GITHUB-LINK]
```

3. Datenbank initialisieren

Zunächst ist PowerShell oder die Windows-Eingabeaufforderung im Hauptverzeichnis des entpackten Projekts zu öffnen.

Die SQLite-Datenbank mit den benötigten Tabellen und Beispieldaten wird mit folgendem Befehl erstellt:

```powershell
python init_database.py
```

Falls der Befehl `python` nicht erkannt wird, kann unter Windows alternativ verwendet werden:

```powershell
py init_database.py
```

Nach erfolgreicher Ausführung befindet sich die Datei `dashboard.db` im Hauptverzeichnis des Projekts.

4. Dashboard starten

Das Studien-Dashboard wird anschließend aus dem Hauptverzeichnis mit folgendem Befehl gestartet:

```powershell
python -m src.main
```

Alternativ:

```powershell
py -m src.main
```

Nach dem Start öffnet sich die grafische Benutzeroberfläche des Studien-Dashboards.

5. Beenden

Das Programm wird durch Schließen des Dashboard-Fensters beendet.
