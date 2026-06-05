from dataclasses import dataclass
from datetime import date


@dataclass
class Student:
    matrikelnummer: str
    name: str
    startdatum: date
    studienmodell: str


@dataclass
class Modul:
    titel: str
    ects: int


student = Student(
    matrikelnummer="12345678",
    name="Max Mustermann",
    startdatum=date(2024, 10, 1),
    studienmodell="Teilzeit I"
)

modul = Modul(
    titel="Objektorientierte und funktionale Programmierung mit Python",
    ects=5
)

print(student)
print(modul)
print(f"{student.name} belegt das Modul {modul.titel} mit {modul.ects} ECTS.")