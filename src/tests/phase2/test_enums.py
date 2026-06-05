"""
Testprogramm: Enumerationen

Ziel:
Untersuchung der Umsetzung von Enumerationen in Python.

Untersuchte Konzepte:
- Enum-Klassen
- feste Wertebereiche
- Typsicherheit
- Vermeidung ungültiger Zustände

Erkenntnis:
Python stellt mit dem Modul enum eine integrierte Unterstützung für
Enumerationen bereit. Die im UML-Klassendiagramm definierten
Enumerationen können direkt als Python-Enums umgesetzt werden.
Dadurch werden fachliche Zustände eindeutig definiert und die
Verwendung ungültiger Werte wird verhindert.

Dieses Testprogramm untersucht anhand der Enumerationen
Studienmodell, Abschluss, Prüfungsart, Belegungsstatus und
Prüfungsstatus die Umsetzung der im Studien-Dashboard
verwendeten Wertebereiche.
"""

from enum import Enum


# Studienmodelle des Studiengangs
class Studienmodell(Enum):
    VOLLZEIT = "Vollzeit"
    TEILZEIT_I = "Teilzeit I"
    TEILZEIT_II = "Teilzeit II"


# Mögliche Abschlüsse
class Abschluss(Enum):
    BACHELOR = "Bachelor"
    MASTER = "Master"


# Mögliche Prüfungsarten
class Pruefungsart(Enum):
    KLAUSUR = "Klausur"
    PORTFOLIO = "Portfolio"
    HAUSARBEIT = "Hausarbeit"
    PROJEKTARBEIT = "Projektarbeit"
    FACHPRASENTATION = "Fachpräsentation"


# Status einer Modulbelegung
class Belegungsstatus(Enum):
    GEBUCHT = "Gebucht"
    ABGESCHLOSSEN = "Abgeschlossen"


# Status eines Prüfungsergebnisses
class Pruefungsstatus(Enum):
    OFFEN = "Offen"
    BESTANDEN = "Bestanden"
    NICHT_BESTANDEN = "Nicht bestanden"


# Ausgabe einzelner Enum-Werte
print("Studienmodell:")
print(Studienmodell.VOLLZEIT)
print(Studienmodell.VOLLZEIT.value)

print("\nAbschluss:")
print(Abschluss.BACHELOR)

# Iteration über alle definierten Prüfungsarten
print("\nPrüfungsart:")
for art in Pruefungsart:
    print("-", art.value)

print("\nBelegungsstatus:")
print(Belegungsstatus.ABGESCHLOSSEN.value)

print("\nPrüfungsstatus:")
print(Pruefungsstatus.BESTANDEN.value)