"""
Testprogramm: Beziehungen

Ziel:
Untersuchung der Umsetzung von Beziehungen zwischen Domain-Klassen
in Python.

Untersuchte Konzepte:
- Aggregation
- Komposition
- 1:n-Beziehungen
- field(default_factory=list)
"""

from dataclasses import dataclass, field


# Prüfungsleistung
@dataclass
class Pruefungsleistung:
    bezeichnung: str


# Modul mit Prüfungsleistungen
@dataclass
class Modul:
    titel: str
    ects: int
    pruefungsleistungen: list[Pruefungsleistung] = field(default_factory=list)


# Semester mit Modulen
@dataclass
class Semester:
    nummer: int
    module: list[Modul] = field(default_factory=list)


# Studiengang mit Semestern
@dataclass
class Studiengang:
    name: str
    semester: list[Semester] = field(default_factory=list)


# Testdaten erzeugen
portfolio = Pruefungsleistung("Portfolio")

python_modul = Modul(
    titel="Objektorientierte und funktionale Programmierung mit Python",
    ects=5
)

# Beziehung Modul -> Prüfungsleistung
python_modul.pruefungsleistungen.append(portfolio)

semester1 = Semester(nummer=1)

# Beziehung Semester -> Modul
semester1.module.append(python_modul)

studiengang = Studiengang("Softwareentwicklung")

# Beziehung Studiengang -> Semester
studiengang.semester.append(semester1)

# Ausgabe der Objektstruktur
print(studiengang)