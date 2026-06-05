"""
Testprogramm: Dataclasses

Ziel:
Untersuchung der Umsetzung von Domain-Klassen mit Python-Dataclasses.

Untersuchte Konzepte:
- Klassen und Objekte
- Dataclasses
- Typannotationen
- automatische Erzeugung von Standardmethoden

Erkenntnis:
Die Verwendung von Dataclasses bietet in Python den Vorteil, dass
Standardmethoden wie der Konstruktor (__init__), die Textdarstellung
(__repr__) und Vergleichsoperationen (__eq__) automatisch erzeugt werden.
Dadurch reduziert sich der Implementierungsaufwand für die Domain-Klassen
erheblich.

Dieses Testprogramm untersucht anhand der Klassen Student und Modul,
ob sich die im UML-Klassendiagramm vorgesehenen Domain-Klassen
sinnvoll als Dataclasses umsetzen lassen.
"""

from dataclasses import dataclass
from datetime import date


# Beispiel einer Domain-Klasse aus dem Studien-Dashboard
@dataclass
class Student:
    matrikelnummer: str
    name: str
    startdatum: date
    studienmodell: str


# Beispiel einer weiteren Domain-Klasse
@dataclass
class Modul:
    titel: str
    ects: int


# Erzeugen eines Studenten-Objekts
student = Student(
    matrikelnummer="12345678",
    name="Max Mustermann",
    startdatum=date(2024, 10, 1),
    studienmodell="Teilzeit I"
)

# Erzeugen eines Modul-Objekts
modul = Modul(
    titel="Objektorientierte und funktionale Programmierung mit Python",
    ects=5
)

# Ausgabe der automatisch erzeugten Textdarstellung (__repr__)
print(student)
print(modul)

# Zugriff auf die Attribute der Objekte
print(
    f"{student.name} belegt das Modul "
    f"{modul.titel} mit {modul.ects} ECTS."
)