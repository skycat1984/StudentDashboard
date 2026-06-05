from dataclasses import dataclass, field


@dataclass
class Pruefungsleistung:
    bezeichnung: str


@dataclass
class Modul:
    titel: str
    ects: int
    pruefungsleistungen: list[Pruefungsleistung] = field(default_factory=list)


@dataclass
class Semester:
    nummer: int
    module: list[Modul] = field(default_factory=list)


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

python_modul.pruefungsleistungen.append(portfolio)

semester1 = Semester(nummer=1)
semester1.module.append(python_modul)

studiengang = Studiengang("Softwareentwicklung")
studiengang.semester.append(semester1)

# Ausgabe

print(studiengang)