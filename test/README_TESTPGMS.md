# Testprogramme des Studien-Dashboards

Dieses Verzeichnis enthält die Testprogramme, die während der ersten beiden Phasen des Portfolios **„Objektorientierte und funktionale Programmierung mit Python“** erstellt wurden.

Die Programme dienten der Machbarkeitsüberprüfung sowie der Untersuchung ausgewählter objektorientierter Konzepte. Es handelt sich um eigenständig ausführbare Test- und Demonstrationsprogramme, nicht um automatisierte Unit-Tests.

## Voraussetzungen

Für die Ausführung werden benötigt:

* Python 3.13
* ein aktuelles Windows-Betriebssystem
* optional Visual Studio Code oder eine andere Entwicklungsumgebung

Tkinter und SQLite sind Bestandteile der Python-Standardbibliothek und müssen nicht zusätzlich installiert werden.

## Ausführung

PowerShell oder die Windows-Eingabeaufforderung ist im Hauptverzeichnis des Projekts zu öffnen. Dabei handelt es sich um den Ordner, in dem sich die Datei `init_database.py` befindet.

Die installierte Python-Version kann mit folgendem Befehl geprüft werden:

```powershell
python --version
```

Falls der Befehl `python` unter Windows nicht erkannt wird, kann alternativ der Windows-Python-Launcher verwendet werden:

```powershell
py --version
```

Die einzelnen Testprogramme werden mit den nachfolgend angegebenen Befehlen ausgeführt.

---

## Phase 1 – Machbarkeitsüberprüfung

Die Testprogramme der ersten Phase dienten der Untersuchung der technischen Grundlagen für den späteren Dashboard-Prototyp.

### Testprogramm 1: Grafische Benutzeroberfläche mit Tkinter

Datei:

```text
test/phase1/tkinter_test.py
```

Ziel:

* Untersuchung der Umsetzbarkeit einer grafischen Benutzeroberfläche mit Tkinter
* Erzeugung eines Fensters mit Überschrift und Schaltfläche
* Anzeige eines Dialogfensters nach einer Benutzeraktion

Ausführen:

```powershell
python test/phase1/tkinter_test.py
```

Alternativ:

```powershell
py test/phase1/tkinter_test.py
```

Erwartetes Ergebnis:

* Ein Fenster mit dem Titel „Tkinter Test“ wird geöffnet.
* Eine Überschrift und eine Schaltfläche werden angezeigt.
* Nach dem Anklicken der Schaltfläche erscheint eine Meldung.
* Das Programm wird durch Schließen des Fensters beendet.

### Testprogramm 2: Lokale Datenspeicherung mit SQLite

Datei:

```text
test/phase1/sqlite_test.py
```

Ziel:

* Untersuchung der lokalen Datenspeicherung mit SQLite
* Erzeugung einer Tabelle
* Einfügen und Auslesen eines Datensatzes
* Verwendung parametrisierter SQL-Anweisungen

Ausführen:

```powershell
python test/phase1/sqlite_test.py
```

Alternativ:

```powershell
py test/phase1/sqlite_test.py
```

Erwartetes Ergebnis:

* Im Arbeitsspeicher wird eine SQLite-Datenbank erzeugt.
* Die Tabelle `student` wird angelegt.
* Ein Testdatensatz wird gespeichert.
* Der gespeicherte Datensatz wird in der Konsole ausgegeben.

Das Testprogramm verwendet eine In-Memory-Datenbank. Es wird daher keine dauerhafte Datenbankdatei angelegt und die produktive Datei `dashboard.db` wird nicht verändert.

---

## Phase 2 – Untersuchung objektorientierter Konzepte

Die Testprogramme der zweiten Phase untersuchen die Umsetzung ausgewählter objektorientierter Konzepte in Python. Die gewonnenen Erkenntnisse bildeten eine Grundlage für die Architektur und Implementierung des Dashboard-Prototyps.

### Testprogramm 1: Dataclasses

Datei:

```text
test/phase2/test_dataclasses.py
```

Ziel:

* Untersuchung der Umsetzung von Domain-Klassen mit Python-Dataclasses
* Erzeugung und Verwendung von Objekten der Klassen `Student` und `Modul`

Untersuchte Konzepte:

* Klassen und Objekte
* Dataclasses
* Typannotationen
* automatische Erzeugung von `__init__`
* automatische Erzeugung von `__repr__`
* automatische Erzeugung von `__eq__`

Ausführen:

```powershell
python test/phase2/test_dataclasses.py
```

Alternativ:

```powershell
py test/phase2/test_dataclasses.py
```

Erwartetes Ergebnis:

* Die erzeugten Objekte werden mit ihrer automatisch erzeugten Textdarstellung ausgegeben.
* Der Zugriff auf die Attribute der Objekte wird demonstriert.

### Testprogramm 2: Enumerationen

Datei:

```text
test/phase2/test_enums.py
```

Ziel:

* Untersuchung der Umsetzung fest definierter Wertebereiche mit Python-Enumerationen
* Vermeidung beliebiger und fachlich ungültiger Zeichenketten

Untersuchte Konzepte:

* Enum-Klassen
* feste Wertebereiche
* eindeutige fachliche Zustände
* Zugriff auf Enum-Mitglieder und deren Werte
* Iteration über Enum-Mitglieder

Ausführen:

```powershell
python test/phase2/test_enums.py
```

Alternativ:

```powershell
py test/phase2/test_enums.py
```

Erwartetes Ergebnis:

* Werte der definierten Enumerationen werden in der Konsole ausgegeben.
* Die Iteration über die verschiedenen Prüfungsarten wird demonstriert.

### Testprogramm 3: Beziehungen zwischen Domain-Klassen

Datei:

```text
test/phase2/test_relations.py
```

Ziel:

* Untersuchung der Umsetzung von Beziehungen zwischen Domain-Klassen
* Abbildung einer verschachtelten Objektstruktur für das Studien-Dashboard

Untersuchte Konzepte:

* Aggregation und Komposition
* Objektreferenzen
* 1:n-Beziehungen
* Listen als Sammlung zusammengehöriger Objekte
* `field(default_factory=list)`

Ausführen:

```powershell
python test/phase2/test_relations.py
```

Alternativ:

```powershell
py test/phase2/test_relations.py
```

Erwartetes Ergebnis:

* Ein Studiengang mit Semester, Modul und Prüfungsleistung wird erzeugt.
* Die vollständige verschachtelte Objektstruktur wird in der Konsole ausgegeben.

### Testprogramm 4: Service-Klassen

Datei:

```text
test/phase2/test_services.py
```

Ziel:

* Untersuchung der Trennung von Domain-Objekten und fachlicher Berechnungslogik
* Berechnung ausgewählter Kennzahlen des Studien-Dashboards

Untersuchte Konzepte:

* Service-Klassen
* Trennung von Daten und Berechnungslogik
* Verarbeitung von Domain-Objekten
* Berechnung des ECTS-Fortschritts
* Berechnung des Notendurchschnitts

Ausführen:

```powershell
python test/phase2/test_services.py
```

Alternativ:

```powershell
py test/phase2/test_services.py
```

Erwartetes Ergebnis:

* Der berechnete ECTS-Fortschritt wird in Prozent ausgegeben.
* Der berechnete Notendurchschnitt wird ausgegeben.

### Testprogramm 5: Sichtbarkeit und Kapselung

Datei:

```text
test/phase2/test_visibility.py
```

Ziel:

* Untersuchung der Umsetzung von Sichtbarkeit und Kapselung in Python
* Vergleich der UML-Sichtbarkeit mit den Konventionen der Programmiersprache Python

Untersuchte Konzepte:

* öffentliche Attribute
* interne Attribute mit einfachem Unterstrich
* Attribute mit doppeltem Unterstrich
* Name Mangling
* Properties
* Property-Setter
* Validierung von Attributwerten
* Umgehung einer Property durch direkten Attributzugriff

Ausführen:

```powershell
python test/phase2/test_visibility.py
```

Alternativ:

```powershell
py test/phase2/test_visibility.py
```

Erwartetes Ergebnis:

* Auf ein öffentliches Attribut wird direkt zugegriffen.
* Ein interner Wert wird über eine Property gelesen und geändert.
* Ein leerer Name wird durch die Validierung des Property-Setters abgelehnt.
* Der direkte Zugriff auf ein internes Attribut mit einfachem Unterstrich bleibt technisch möglich.
* Der direkte Zugriff auf ein Attribut mit doppeltem Unterstrich führt zu einem `AttributeError`.
* Der Zugriff über den durch Name Mangling erzeugten Attributnamen wird demonstriert.

### Testprogramm 6: Properties, Polymorphie und Duck Typing

Datei:

```text
test/phase2/test_ducktyping.py
```

Ziel:

* Untersuchung weiterer objektorientierter Konzepte und ihrer möglichen Anwendung im Studien-Dashboard
* Gegenüberstellung von vererbungsbasierter Polymorphie und Duck Typing

Untersuchte Konzepte:

* kontrollierter Attributzugriff mit Properties
* Validierung durch einen Property-Setter
* abstrakte Basisklassen
* vererbungsbasierte Polymorphie
* Duck Typing
* Austauschbarkeit von Objekten mit derselben erwarteten Methode

Ausführen:

```powershell
python test/phase2/test_ducktyping.py
```

Alternativ:

```powershell
py test/phase2/test_ducktyping.py
```

Erwartetes Ergebnis:

* Eine gültige Note wird gespeichert und ausgegeben.
* Eine ungültige Note wird durch den Property-Setter abgelehnt.
* Unterschiedliche Unterklassen werden über dieselbe Methode verarbeitet.
* Zwei verschiedene Repository-Klassen werden ohne gemeinsame Oberklasse durch denselben Controller verwendet.

---

## Zweck der Testprogramme

Die Testprogramme dokumentieren die schrittweise Untersuchung der technischen und objektorientierten Umsetzungsmöglichkeiten des Studien-Dashboards.

Untersucht wurden insbesondere:

* grafische Benutzeroberflächen mit Tkinter
* lokale Datenspeicherung mit SQLite
* Domain-Klassen mit Dataclasses
* fest definierte Wertebereiche mit Python-Enums
* Beziehungen zwischen Domain-Klassen
* Auslagerung fachlicher Berechnungen in Service-Klassen
* Kapselung und Sichtbarkeit in Python
* Properties und Validierungen
* vererbungsbasierte Polymorphie
* Duck Typing

Die Erkenntnisse aus diesen Programmen wurden bei der Entwicklung des finalen Dashboard-Prototyps berücksichtigt.
